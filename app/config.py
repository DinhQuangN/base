from typing import Any, Dict, Optional

from pydantic import BaseSettings, EmailStr, validator
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    PROJECT_NAME: str = "Base-fastapi"

    DB_CONNECTION: Optional[str]
    DB_HOST: Optional[str]
    DB_PORT: Optional[str]
    DB_DATABASE: Optional[str]
    DB_USERNAME: Optional[str]
    DB_PASSWORD: Optional[str]
    SECURITY_BCRYPT_DEFAULT_ROUNDS: int = 12
    # REFRESH_TOKEN_EXPIRE_MINUTES: int

    SECRET_KEY: str
    VERIFY_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    SQLALCHEMY_DATABASE_URI: str = ""

    FE_URL: str
    APP_URL: str

    AMOUNT_PER_DOWNLOAD: int
    AMOUNT_PER_JOB_ITEM: int
    HASHIDS_SALT: str

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM: EmailStr
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool

    CLIENT_ID: str
    CLIENT_SECRET: str
    SLACK_HOST: str

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str) and v:
            return v
        if not (connection := values.get("DB_CONNECTION")):
            raise ValueError(
                "must specify at least DB_CONNECTION or SQLALCHEMY_DATABASE_URI",
            )
        username = values.get("DB_USERNAME")
        password = values.get("DB_PASSWORD")
        host = values.get("DB_HOST")
        port = values.get("DB_PORT")
        database = values.get("DB_DATABASE")
        return URL(
            connection,
            username,
            password,
            host,
            port,
            database,
        ).render_as_string(False)

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
