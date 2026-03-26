from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    quantity: int


class ItemUpdate(BaseModel):
    name: str
    quantity: int


class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int


class ItemDetailResponse(BaseModel):
    message: str
    item: ItemResponse


class ItemCreateResponse(BaseModel):
    message: str
    item: ItemResponse


class ItemUpdateResponse(BaseModel):
    message: str
    item: ItemResponse


class DeleteResponse(BaseModel):
    message: str


class SearchResponse(BaseModel):
    message: str
    items: list[ItemResponse]