from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_book():
    # Test getting an existing book
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "The Great Gatsby"

    # Test getting a non-existent book
    response = client.get("/api/v1/books/999")
    assert response.status_code == 404