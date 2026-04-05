from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.items import ItemCreate, ItemUpdate


def create_item(db: Session, item_data: ItemCreate) -> Item:
    new_item = Item(name=item_data.name, quantity=item_data.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_item_by_id(db: Session, item_id: int) -> Item | None:
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db: Session, item: Item, item_data: ItemUpdate) -> Item:
    item.name = item_data.name
    item.quantity = item_data.quantity
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item: Item) -> None:
    db.delete(item)
    db.commit()


def search_items(
    db: Session,
    name: str | None = None,
    min_quantity: int | None = None,
) -> list[Item]:
    query = db.query(Item)

    if name is not None:
        query = query.filter(Item.name.ilike(f"%{name}%"))

    if min_quantity is not None:
        query = query.filter(Item.quantity >= min_quantity)

    return query.all()
