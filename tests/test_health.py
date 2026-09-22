from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_webhook_accepts_json():
    r = client.post("/webhooks/test", json={"ping": 1})
    assert r.status_code == 200
    assert r.json()["source"] == "test"
