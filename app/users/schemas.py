from pydantic import BaseModel

class SUserRegister(BaseModel):
    username: str
    password: str