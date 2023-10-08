from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from jose import jwt
from pydantic import EmailStr
from sqlmodel import Session, select

from app.api.base.exceptions import ConflictException
from app.api.v1.schemas.users import CreateUserRequest
from app.api.v1.services.auth import get_password_hash
from app.config import settings
from app.models.user import RoleCode, User

email_verification_failed = """
    <html>
        <head>
            <title>メール確認</title>
        </head>
        <body>
            <h2>資格情報を検証できませんでした</h2>
        </body>
    </html>
"""


async def create_user(
    db: Session, request: CreateUserRequest, mail_connection: ConnectionConfig
):
    user = db.exec(select(User).where(User.email == request.email)).first()
    if user:
        raise ConflictException(detail="user already exist")
    new_user = User(
        name=request.name,
        email=request.email,
        password=get_password_hash(request.password),
        gender_code=request.gender_code,
        role_code=RoleCode.User,
    )
    db.add(new_user)
    db.commit()

    try:
        token = jwt.encode(
            {"email": request.email}, settings.VERIFY_KEY, algorithm=settings.ALGORITHM
        )

        url = f"{settings.APP_URL}/v1/auth/verify-email/?token={token}"
        template_data = {"url": url}

        message = MessageSchema(
            subject="[Salesbox]会員登録のご案内",
            recipients=[EmailStr(request.email)],
            template_body=template_data,
            subtype=MessageType.html,
        )
        fm = FastMail(mail_connection)
        await fm.send_message(message, template_name="register.html")
    except Exception as e:
        db.rollback()
        raise e

    return new_user.id
