# Smart Inventory Sync API

A backend service built with FastAPI for learning and implementing inventory management fundamentals. The project currently provides a working inventory API backed by SQLite through SQLAlchemy.

## Current Status

Implemented so far:

- FastAPI application setup
- Root and health-check endpoints
- Route organization with `APIRouter`
- Pydantic request and response schemas
- SQLite database setup with SQLAlchemy
- Database-backed item CRUD endpoints
- Item search with optional filters

Planned next:

- Automated tests with pytest
- Supplier sync and transformation flow
- Docker and CI polish

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite

## Available Endpoints

- `GET /`
- `GET /health`
- `POST /items`
- `GET /items/{item_id}`
- `PUT /items/{item_id}`
- `DELETE /items/{item_id}`
- `GET /search`

## Project Structure

```text
app/
  main.py
  database.py
  models/
    item.py
  routes/
    health.py
    items.py
  schemas/
    common.py
    items.py
```

## Getting Started

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the development server

```bash
python -m uvicorn app.main:app --reload
```

### 4. Open the API

- Swagger UI: `http://127.0.0.1:8000/docs`
- Root endpoint: `http://127.0.0.1:8000/`
- Health check: `http://127.0.0.1:8000/health`

## Database

The app uses SQLite with this local database file:

- `inventory.db`

The database table is created automatically on startup through SQLAlchemy metadata.

## Search Behavior

`GET /search` supports these optional query parameters:

- `name`
- `min_quantity`

Examples:

```text
/search
/search?name=Key
/search?min_quantity=5
/search?name=Key&min_quantity=5
```

## Example Request

Create an item:

```json
{
  "name": "Keyboard",
  "quantity": 5
}
```

## Notes

- Data is now stored in SQLite instead of an in-memory list.
- Automated tests have not been added yet.
- Supplier sync functionality has not been implemented yet.
