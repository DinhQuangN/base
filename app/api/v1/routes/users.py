from fastapi import APIRouter

from app.api.base.des import custom_generate_unique_id

router = APIRouter(generate_unique_id_function=custom_generate_unique_id)
