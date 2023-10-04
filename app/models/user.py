import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlmodel import Field, SQLModel


class GenderCode(str, enum.Enum):
    Male = "MALE"
    Female = "FE_MALE"


class User(SQLModel, table=True):
    __tablename__: str = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(
        nullable=False, sa_column=Column(String(255), default=None, unique=True)
    )
    password: str = Field(nullable=False, sa_column=Column(String(255)), default=None)
    name: Optional[str] = Field(
        nullable=True, sa_column=Column(String(255)), default=None
    )
    email_verified_at: datetime = Field(nullable=True, default=None)
    gender_code: Optional[GenderCode]
    role_code: Optional[str] = Field(
        nullable=True, sa_column=Column(String(20)), default=None
    )
    created_at: datetime = Field(
        default=None, sa_column=Column(TIMESTAMP, server_default=func.now())
    )
    created_by: Optional[int] = Field(
        nullable=True, sa_column=Column(Integer), default=None
    )
    updated_at: datetime = Field(
        default=None, sa_column=Column(TIMESTAMP, server_default=func.now())
    )
    updated_by: Optional[int] = Field(
        nullable=True, sa_column=Column(Integer), default=None
    )
    deleted_at: datetime = Field(
        default=None, sa_column=Column(TIMESTAMP, server_default=None)
    )
    deleted_by: Optional[int] = Field(
        nullable=True, sa_column=Column(Integer), default=None
    )
