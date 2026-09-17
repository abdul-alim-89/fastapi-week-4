from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """Intial function"""
    return {"message" : "Welcome to fastapi"}

@app.get("/item/{item_id}")
def get_single_item(item_id: int):
    """Get a single item by its ID."""
    return {"success": True, "message": f"Your item id is {item_id}"}

@app.get("/search")
def search_item(q: str | None = None):
    """Search for items using the provided search query."""
    return {"success" : True, "message": f"Your search term : {q}"}
