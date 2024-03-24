from fastapi import HTTPException, status

class AppException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"

class PasswordEasyException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пароль не соответствует требованиям безопасности"

class UserNotExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь не существует"