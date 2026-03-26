from fastapi import FastAPI

from app.database import Base, engine
from app.models.item import Item
from app.routes.health import router as health_router
from app.routes.items import router as items_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Smart Inventory Sync API")

app.include_router(health_router)
app.include_router(items_router)