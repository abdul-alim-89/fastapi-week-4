from typing import Annotated
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserCreate, UserOut
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from models.user import User
from core.security import hash_password, verify_hash_password, generate_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
router = APIRouter(prefix='/user', tags=["User"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    try:
        payload = decode_token(token)

        user_id = int(payload["sub"])

    except (jwt.InvalidTokenError, KeyError, ValueError) as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=err)

    user = db.scalars(select(User).where(User.id == user_id))

    if user is None or not user.is_active:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorize user")

    return user

CurrentUser = Annotated[User, Depends(get_current_user)]

@router.post("/register")
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    exit_user = db.scalars(select(User).where(User.email == user.email)).first()
    print(exit_user)
    if exit_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user already exit")
    user = User(email = user.email, hash_password = hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"success": True, "message": "User created successfully"}

@router.post("/login")
def user_login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    #print(form.model_dump())
    print(type(form))
    exit_user = db.scalars(select(User).where(User.email == form.username)).first()

    if exit_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    is_correct_pswd = verify_hash_password(form.password, exit_user.hash_password)

    if not is_correct_pswd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong password")

    return generate_token(exit_user.id)
    

@router.get("/me")
def me(user: CurrentUser):
    return user
    
