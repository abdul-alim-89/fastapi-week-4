from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Product"])

products = [{
    "id": 1,
    "name": "Nike Shoes",
    "price": 250.00,
    "in_stock": True,
    "tags": ["sport", "running"],
    "category": {"id": 100, "name": "shoes"}
},{
    "id": 2,
    "name": "Sony Wireless Headphones",
    "price": 180.00,
    "in_stock": True,
    "tags": ["audio", "bluetooth"],
    "category": {"id": 101, "name": "electronics"}
  },
  {
    "id": 3,
    "name": "Leather Travel Duffel",
    "price": 125.50,
    "in_stock": False,
    "tags": ["travel", "bags"],
    "category": {"id": 102, "name": "accessories"}
}]
