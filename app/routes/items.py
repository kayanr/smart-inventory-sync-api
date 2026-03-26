from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.item import Item
from app.schemas.items import (
    DeleteResponse,
    ItemCreate,
    ItemCreateResponse,
    ItemDetailResponse,
    ItemUpdate,
    ItemUpdateResponse,
    SearchResponse,
)

router = APIRouter()


@router.post("/items", response_model=ItemCreateResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(name=item.name, quantity=item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        "message": "Item created",
        "item": new_item,
    }


@router.get("/items/{item_id}", response_model=ItemDetailResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "message": "Item fetched",
        "item": item,
    }


@router.put("/items/{item_id}", response_model=ItemUpdateResponse)
def update_item(item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = item_update.name
    item.quantity = item_update.quantity
    db.commit()
    db.refresh(item)

    return {
        "message": "Item updated",
        "item": item,
    }


@router.delete("/items/{item_id}", response_model=DeleteResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"message": "Item deleted"}


@router.get("/search", response_model=SearchResponse)
def search_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()

    return {
        "message": "Search results",
        "items": items,
    }