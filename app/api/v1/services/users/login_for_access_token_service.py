from sqlmodel import Session

from app.api.base.exceptions import ForbiddenException, UnauthorizedException
from app.api.v1.schemas.users import Token, UserLoginRequest
from app.api.v1.services.auth import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
)


def login_for_access_token(db: Session, request: UserLoginRequest):
    user = authenticate_user(db, request.email, request.password)

    if not user:
        raise UnauthorizedException("incorrectEmailOrPassword")
    if not user.email_verified_at:
        raise ForbiddenException("haveNotVerifyEmail")

    access_token, expire_at = create_access_token(user.email)

    refresh_token, refresh_expire_at = create_refresh_token(user.email)

    return Token(
        token_type="bearer",
        access_token=access_token,
        expire_at=expire_at,
        refresh_token=refresh_token,
        refresh_expire_at=refresh_expire_at,
    )
