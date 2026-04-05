import pytest

from tests.conftest import get_test_client


@pytest.mark.anyio
async def test_health_check():
    async with get_test_client() as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_create_and_get_item():
    async with get_test_client() as client:
        create_response = await client.post(
            "/items",
            json={
                "name": "Keyboard",
                "quantity": 5,
            },
        )

        assert create_response.status_code == 200
        created_item = create_response.json()["item"]
        item_id = created_item["id"]

        get_response = await client.get(f"/items/{item_id}")

    assert get_response.status_code == 200
    assert get_response.json()["item"]["name"] == "Keyboard"
    assert get_response.json()["item"]["quantity"] == 5


@pytest.mark.anyio
async def test_search_items():
    async with get_test_client() as client:
        response = await client.get("/search")

    assert response.status_code == 200
    assert "items" in response.json()


@pytest.mark.anyio
async def test_update_and_delete_item():
    async with get_test_client() as client:
        create_response = await client.post(
            "/items",
            json={
                "name": "Mouse",
                "quantity": 10,
            },
        )

        assert create_response.status_code == 200
        item_id = create_response.json()["item"]["id"]

        update_response = await client.put(
            f"/items/{item_id}",
            json={
                "name": "Wireless Mouse",
                "quantity": 12,
            },
        )

        assert update_response.status_code == 200
        assert update_response.json()["item"]["name"] == "Wireless Mouse"
        assert update_response.json()["item"]["quantity"] == 12

        delete_response = await client.delete(f"/items/{item_id}")

        assert delete_response.status_code == 200
        assert delete_response.json() == {"message": "Item deleted"}

        get_response = await client.get(f"/items/{item_id}")

    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Item not found"}


@pytest.mark.anyio
async def test_create_item_with_invalid_quantity():
    async with get_test_client() as client:
        response = await client.post(
            "/items",
            json={
                "name": "Monitor",
                "quantity": "five",
            },
        )

    assert response.status_code == 422


@pytest.mark.anyio
async def test_search_items_with_filters():
    async with get_test_client() as client:
        await client.post(
            "/items",
            json={
                "name": "Mechanical Keyboard",
                "quantity": 7,
            },
        )
        await client.post(
            "/items",
            json={
                "name": "USB Cable",
                "quantity": 2,
            },
        )

        response = await client.get("/search?name=Key&min_quantity=5")

        assert response.status_code == 200
        items = response.json()["items"]

    assert len(items) >= 1
    assert all("Key" in item["name"] for item in items)
    assert all(item["quantity"] >= 5 for item in items)
