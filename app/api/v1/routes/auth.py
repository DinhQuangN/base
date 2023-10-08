from fastapi import APIRouter, Depends
from fastapi_mail import ConnectionConfig
from sqlmodel import Session

from app.api.base.deps import custom_generate_unique_id, get_session, mail_connection
from app.api.v1.schemas.users import CreateUserRequest, Token, UserLoginRequest
from app.api.v1.services.users import create_user, login_for_access_token

router = APIRouter(generate_unique_id_function=custom_generate_unique_id)


@router.post("/login", response_model=Token)
def login(request: UserLoginRequest, db: Session = Depends(get_session)):
    return login_for_access_token(db, request)


@router.post("/register")
async def register(
    request: CreateUserRequest,
    db: Session = Depends(get_session),
    mail_connect: ConnectionConfig = Depends(mail_connection),
):
    return await create_user(db, request, mail_connect)
