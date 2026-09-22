from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, DATE, DATETIME, func
from datetime import date, datetime

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    due_date: Mapped[date] = mapped_column(DATE)
    created_at: Mapped[datetime] = mapped_column(DATETIME(timezone=True), server_default=func.now())