from fastapi import FastAPI, Field
from pydantic import BaseModel

app = FastAPI()

class ProductCreate(BaseModel):
    name: str = Field(min_legth=3)
    price: float = Field(gt=0)
    in_stock: bool = True
    tags: list[str] = []

@app.get("/")
def welcome():
    """Initial function"""
    return {"message" : "Welcome to fastapi"}

@app.get("/item/{item_id}")
def get_single_item(item_id: int):
    """Get a single item by its ID."""
    return {"success": True, "message": f"Your item id is {item_id}"}

@app.get("/search")
def search_item(q: str | None = None):
    """Search for items using the provided search query."""
    return {"success" : True, "message": f"Your search term : {q}"}
