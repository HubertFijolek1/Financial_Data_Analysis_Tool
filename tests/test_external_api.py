import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_external_data_invalid_url(monkeypatch):
    # Simulate a failure when calling fetch_external_data
    async def fake_fetch(url: str):
        raise Exception("Dummy error")
    monkeypatch.setattr("external_api.fetch_external_data", fake_fetch)
    response = client.get("/external-data", params={"url": "http://invalid.url"})
    assert response.status_code == 500
    assert "Error fetching data" in response.json()["detail"]

def test_get_external_data_success(monkeypatch):
    # Simulate a successful response
    async def fake_fetch(url: str):
        return {"dummy": "data"}
    monkeypatch.setattr("external_api.fetch_external_data", fake_fetch)
    response = client.get("/external-data", params={"url": "http://example.com"})
    assert response.status_code == 200
    assert response.json() == {"data": {"dummy": "data"}}
