from fastapi import APIRouter, HTTPException

from app.data.store import items_db
from app.schemas.items import (
    ItemCreate,
    ItemCreateResponse,
    ItemDetailResponse,
    ItemResponse,
    SearchResponse,
)

router = APIRouter()


@router.post("/items", response_model=ItemCreateResponse)
def create_item(item: ItemCreate):
    new_item = {
        "id": len(items_db) + 1,
        "name": item.name,
        "quantity": item.quantity,
    }
    items_db.append(new_item)

    return {
        "message": "Item created",
        "item": new_item,
    }


@router.get("/items/{item_id}", response_model=ItemDetailResponse)
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return {
                "message": "Item fetched",
                "item": item,
            }

    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/search", response_model=SearchResponse)
def search_items():
    return {
        "message": "Search results",
        "items": items_db,
    }