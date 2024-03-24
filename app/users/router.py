from fastapi import APIRouter

from app.users.dao import UsersDAO
from app.users.schemas import SUser, SUserRegister, SUserText

router = APIRouter(
    tags=["Пользователь"]
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    username = await user_data.username
    await UsersDAO.add(username=username,
                       password=user_data.password)
    return username

@router.post("/write_data")
async def write_data(user_data: SUserText):
    username = await user_data.username
    await UsersDAO.update_data(username=username,
                       textdata=user_data.textdata)
    return username, user_data.textdata