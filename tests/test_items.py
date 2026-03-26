from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item():
    create_response = client.post(
        "/items",
        json={
            "name": "Keyboard",
            "quantity": 5,
        },
    )

    assert create_response.status_code == 200
    created_item = create_response.json()["item"]
    item_id = created_item["id"]

    get_response = client.get(f"/items/{item_id}")

    assert get_response.status_code == 200
    assert get_response.json()["item"]["name"] == "Keyboard"
    assert get_response.json()["item"]["quantity"] == 5


def test_search_items():
    response = client.get("/search")

    assert response.status_code == 200
    assert "items" in response.json()


def test_update_and_delete_item():
    create_response = client.post(
        "/items",
        json={
            "name": "Mouse",
            "quantity": 10,
        },
    )

    assert create_response.status_code == 200
    item_id = create_response.json()["item"]["id"]

    update_response = client.put(
        f"/items/{item_id}",
        json={
            "name": "Wireless Mouse",
            "quantity": 12,
        },
    )

    assert update_response.status_code == 200
    assert update_response.json()["item"]["name"] == "Wireless Mouse"
    assert update_response.json()["item"]["quantity"] == 12

    delete_response = client.delete(f"/items/{item_id}")

    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Item deleted"}

    get_response = client.get(f"/items/{item_id}")

    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Item not found"}


def test_create_item_with_invalid_quantity():
    response = client.post(
        "/items",
        json={
            "name": "Monitor",
            "quantity": "five",
        },
    )

    assert response.status_code == 422


def test_search_items_with_filters():
    client.post(
        "/items",
        json={
            "name": "Mechanical Keyboard",
            "quantity": 7,
        },
    )
    client.post(
        "/items",
        json={
            "name": "USB Cable",
            "quantity": 2,
        },
    )

    response = client.get("/search?name=Key&min_quantity=5")

    assert response.status_code == 200
    items = response.json()["items"]

    assert len(items) >= 1
    assert all("Key" in item["name"] for item in items)
    assert all(item["quantity"] >= 5 for item in items)
