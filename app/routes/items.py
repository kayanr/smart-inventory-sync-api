from fastapi import APIRouter

from app.schemas.items import ItemCreate

router = APIRouter()


@router.post("/items")
def create_item(item: ItemCreate):
    return {
        "message": "Item received",
        "item": item.model_dump(),
    }


@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "message": "Item fetched",
        "item_id": item_id,
    }


@router.get("/search")
def search_items(name: str | None = None, min_quantity: int | None = None):
    return {
        "message": "Search results",
        "filters": {
            "name": name,
            "min_quantity": min_quantity,
        },
    }