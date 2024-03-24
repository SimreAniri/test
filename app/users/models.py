from typing import Optional
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import TEXT
from app.database import Base

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    password: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    textdata: Mapped[Optional[str]] = mapped_column(TEXT, nullable=True)