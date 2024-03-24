from fastapi import APIRouter

from app.exceptions import UserAlreadyExistsException, UserNotExistsException
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserText

router = APIRouter(
    tags=["Пользователь"]
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        raise UserAlreadyExistsException
    await UsersDAO.add(username=user_data.username,
                       password=user_data.password)
    return user_data.username

@router.post("/write_data")
async def write_data(user_data: SUserText):
    existing_user = await UsersDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        await UsersDAO.update_data(username=user_data.username,
                                   textdata=user_data.textdata)
        return user_data.username, user_data.textdata
    raise UserNotExistsException

@router.get("/get_data/{username}")
async def wrget_dataite_data(username: str):
    user = await UsersDAO.find_one_or_none(username=username)
    if user:
        return user.textdata
    raise UserNotExistsException