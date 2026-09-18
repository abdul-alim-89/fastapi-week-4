from fastapi import APIRouter

router = APIRouter(prefix="/item", tags=["items"])

@router.get("/search")
def search_item(q: str | None = None):
    """Search for items using the provided search query."""
    return {"success" : True, "message": f"Your search term : {q}"}

@router.get("/{item_id}")
def get_single_item(item_id: int):
    """Get a single item by its ID."""
    return {"success": True, "message": f"Your item id is {item_id}"}

