from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.user import GenderCode


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    gender_code: Optional[GenderCode] = None
    role_code: Optional[str] = None


class UserLoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token_type: str
    access_token: str
    expire_at: datetime
    refresh_token: str
    refresh_expire_at: datetime


class TokenPayload(BaseModel):
    exp: datetime
    sub: str
    refresh: bool
