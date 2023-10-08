from fastapi import APIRouter

from app.api.v1.routes import auth, users

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])
