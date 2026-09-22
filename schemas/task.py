from datetime import date
from pydantic import BaseModel, Field, ConfigDict

class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str = Field(min_length=3)
    description: str
    due_date: date | None = None

class TaskUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str | None = Field(min_length=3, default=None)
    description: str | None = None
    due_date: date | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    due_date: date | None = None