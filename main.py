from fastapi import FastAPI
f
app = FastAPI()

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

@app.get("/products", response_model=list[ProductCreate])
def get_products():
    return products

@app.post("/products")
def create_product(product: ProductCreate):
    products.append(product.model_dump())
    return {"success": True, "message": "Product created successfully"}
