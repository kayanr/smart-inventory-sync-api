from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.items import (
    DeleteResponse,
    ItemCreate,
    ItemCreateResponse,
    ItemDetailResponse,
    ItemUpdate,
    ItemUpdateResponse,
    SearchResponse,
)
from app.services.items import (
    create_item,
    delete_item,
    get_item_by_id,
    search_items,
    update_item,
)

router = APIRouter()


@router.post("/items", response_model=ItemCreateResponse)
async def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = create_item(db, item)

    return {
        "message": "Item created",
        "item": new_item,
    }


@router.get("/items/{item_id}", response_model=ItemDetailResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "message": "Item fetched",
        "item": item,
    }


@router.put("/items/{item_id}", response_model=ItemUpdateResponse)
async def update_item_route(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db),
):
    item = get_item_by_id(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = update_item(db, item, item_update)

    return {
        "message": "Item updated",
        "item": updated_item,
    }


@router.delete("/items/{item_id}", response_model=DeleteResponse)
async def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    delete_item(db, item)

    return {"message": "Item deleted"}


@router.get("/search", response_model=SearchResponse)
async def search_items_route(
    name: str | None = None,
    min_quantity: int | None = None,
    db: Session = Depends(get_db),
):
    items = search_items(db, name=name, min_quantity=min_quantity)

    return {
        "message": "Search results",
        "items": items,
    }
