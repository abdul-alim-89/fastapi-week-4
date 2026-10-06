import datetime
from sqlalchemy import String, func, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from database import Base

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    hash_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="user")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    