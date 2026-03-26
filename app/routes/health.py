from fastapi import APIRouter

from app.schemas.common import HealthResponse, MessageResponse

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def read_root():
    return {"message": "Welcome to Smart Inventory Sync API"}


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "ok"}