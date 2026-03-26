from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    quantity: int


class ItemResponse(BaseModel):
    name: str
    quantity: int


class ItemDetailResponse(BaseModel):
    message: str
    item_id: int


class ItemCreateResponse(BaseModel):
    message: str
    item: ItemResponse


class SearchFilters(BaseModel):
    name: str | None = None
    min_quantity: int | None = None


class SearchResponse(BaseModel):
    message: str
    filters: SearchFilters