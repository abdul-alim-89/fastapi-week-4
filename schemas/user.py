from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    EDITOR = "editor"
    TEACHER = "teacher"

class UserCreate(BaseModel):

    email: EmailStr
    password: str
    is_active: bool = True
    role: UserRole

class UserOut(BaseModel):

    id: int
    email: EmailStr
    is_active: bool
    role : UserRole
