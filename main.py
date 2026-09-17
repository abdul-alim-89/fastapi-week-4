from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

products = [{
    "name": "Nike Shoes",
    "price": 250.00,
    "in_stock": True,
    "tags": ["sport", "running"],
    "category": {"id": 100, "name": "shoes"}
},{
    "name": "Sony Wireless Headphones",
    "price": 180.00,
    "in_stock": True,
    "tags": ["audio", "bluetooth"],
    "category": {"id": 101, "name": "electronics"}
  },
  {
    "name": "Leather Travel Duffel",
    "price": 125.50,
    "in_stock": False,
    "tags": ["travel", "bags"],
    "category": {"id": 102, "name": "accessories"}
}]

class Category(BaseModel):
    id: int
    name: str

class ProductCreate(BaseModel):
    name: str = Field(min_legth=3)
    price: float = Field(gt=0)
    in_stock: bool = True
    tags: list[str] = []
    category: Category



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

