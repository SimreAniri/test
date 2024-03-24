import re
from pydantic import BaseModel, validator

from app.exceptions import PasswordEasyException, UserAlreadyExistsException, UserNotExistsException
from app.users.dao import UsersDAO

class SUserRegister(BaseModel):
    username: str
    password: str

    @validator("username")
    @classmethod
    async def validate_username(cls, value):
        existing_user = await UsersDAO.find_one_or_none(username=value)
        if existing_user:
            raise UserAlreadyExistsException
        return value

    @validator("password")
    @classmethod
    def validate_password(cls, value):
        if re.match(r"([0-9]*[a-zA-Z][0-9]*){6,30}", value):
            return value
        raise PasswordEasyException
    
class SUser(BaseModel):
    username: str

    @validator("username")
    @classmethod
    async def validate_username(cls, value):
        existing_user = await UsersDAO.find_one_or_none(username=value)
        if existing_user:
            return value
        raise UserNotExistsException
        
class SUserText(SUser):
    textdata: str