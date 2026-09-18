from fastapi import APIRouter, HTTPException, status
from models.schemas import ProductCreate

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

@router.get("/", response_model=list[ProductCreate])
def get_products():
    return products

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    exit_product = False
    for prod in products:
        if prod["id"] == product_dict["id"]:
            exit_product = True
            break

    if exit_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="product id already exit")

    products.append(product_dict)
    return {"success": True, "message": "Product created successfully"}

@router.get("/{id}", response_model=ProductCreate)
def get_single_product(id: int):
    exit_product = None
    for product in products:
        if product["id"] == id:
            exit_product = product
            break

    if exit_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return exit_product

