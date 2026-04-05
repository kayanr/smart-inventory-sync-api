from pathlib import Path
import sys

import httpx
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.database import Base, create_db_session, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test_inventory.db"

test_engine, TestSessionLocal = create_db_session(TEST_DATABASE_URL)
Base.metadata.drop_all(bind=test_engine)
Base.metadata.create_all(bind=test_engine)


async def override_get_db():
    db: Session = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def clear_database():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)


def get_test_client():
    clear_database()
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://testserver")
