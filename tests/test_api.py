from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    url = "/docs"
    response = client.get(url)
    assert response.status_code == 200
