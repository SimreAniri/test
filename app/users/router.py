from fastapi import APIRouter

from app.users.schemas import SUserRegister

router = APIRouter(
    tags=["Пользователь"]
)

@router.post("/register")
def register_user(user_data: SUserRegister):
    pass