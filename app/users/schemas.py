import re
from pydantic import BaseModel, validator

from app.exceptions import PasswordEasyException, UserAlreadyExistsException, UserNotExistsException
from app.users.dao import UsersDAO

class SUserRegister(BaseModel):
    username: str
    password: str

    @validator("password")
    @classmethod
    def validate_password(cls, value):
        if re.match(r"([0-9]*[a-zA-Z][0-9]*){6,30}", value):
            return value
        raise PasswordEasyException
    
class SUserText(BaseModel):
    username: str
    textdata: str