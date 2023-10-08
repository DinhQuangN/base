import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlmodel import Field, SQLModel


class RoleCodeTree(str, enum.Enum):
    Tree = "TREE"
    Pot = "POT"


class Category(SQLModel, table=True):
    __tablename__: str = "categories"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(
        nullable=True, sa_column=Column(String(255)), default=None
    )
    role_code: Optional[RoleCodeTree]
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
