import pytest
from fastapi.testclient import TestClient

from app.main import app, items


@pytest.fixture
def client():
    items.clear()
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonsoir"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_read_item(client):
    payload = {"name": "Café", "price": 2.5}

    response = client.post("/items/1", json=payload)
    assert response.status_code == 201
    assert response.json() == payload

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == payload


def test_create_duplicate_item(client):
    payload = {"name": "Café", "price": 2.5}
    client.post("/items/1", json=payload)

    response = client.post("/items/1", json=payload)
    assert response.status_code == 409


def test_read_unknown_item(client):
    response = client.get("/items/42")
    assert response.status_code == 404
