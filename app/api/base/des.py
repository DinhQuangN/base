from typing import Generator

from fastapi.routing import APIRoute
from sqlmodel import Session

from app.db import engine


def get_db():
    with Session(engine) as session:
        yield session


def get_session() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


def custom_generate_unique_id(route: APIRoute) -> str:
    return route.name
