from datetime import date
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str
    due_date: date = Field(default=None)

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: date | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    due_date: date | None = None