from sqlalchemy.sql import text
from sqlmodel import Session

from .verify_password_service import verify_password


def authenticate_user(db: Session, email: str, password: str):
    query = """SELECT u.* FROM users u WHERE u.email = :email"""
    result = db.execute(text(query), {"email": email})
    user = result.first()

    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
