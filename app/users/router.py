from fastapi import APIRouter

from app.users.schemas import SUserRegister

router = APIRouter(
    tags=["Пользователь"]
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    return user_data.password
