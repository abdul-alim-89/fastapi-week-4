from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres:admin@localhost:5432/testing"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=5,
    pool_pre_ping=True,
    echo=True,)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()