from sqlalchemy import update
from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def update_data(cls, username: str, textdata: str):
        async with async_session_maker() as session:
            query = update(Users).where(Users.username==username).values(textdata=textdata)
            await session.execute(query)
            await session.commit()