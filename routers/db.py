from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(tags=["DB"])

@router.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"success": True, "message": "DB connection successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Db connection failed")

