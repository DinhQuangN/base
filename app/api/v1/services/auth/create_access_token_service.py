from datetime import datetime, timedelta, timezone
from typing import Tuple

from jose import jwt

from app.api.v1.schemas.users import TokenPayload
from app.config import settings


def create_access_token(
    subject: str,
) -> Tuple[str, datetime]:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = TokenPayload(
        exp=expire,
        sub=subject,
        refresh=False,
    )
    encoded_jwt: str = jwt.encode(
        to_encode.dict(),
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt, expire


def create_refresh_token(subject: str) -> Tuple[str, datetime]:
    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    to_encode = TokenPayload(exp=expire, sub=subject, refresh=True)
    encoded_jwt: str = jwt.encode(
        to_encode.dict(),
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt, expire
