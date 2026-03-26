from fastapi import APIRouter

from app.schemas.items import (
    ItemCreate,
    ItemCreateResponse,
    ItemDetailResponse,
    SearchResponse,
)

router = APIRouter()


@router.post("/items", response_model=ItemCreateResponse)
def create_item(item: ItemCreate):
    return {
        "message": "Item received",
        "item": item.model_dump(),
    }


@router.get("/items/{item_id}", response_model=ItemDetailResponse)
def get_item(item_id: int):
    return {
        "message": "Item fetched",
        "item_id": item_id,
    }


@router.get("/search", response_model=SearchResponse)
def search_items(name: str | None = None, min_quantity: int | None = None):
    return {
        "message": "Search results",
        "filters": {
            "name": name,
            "min_quantity": min_quantity,
        },
    }