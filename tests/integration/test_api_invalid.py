
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_invalid_op_returns_422():
    r = client.post("/api/calc", json={"a": 1, "b": 2, "op": "pow"})
    assert r.status_code == 422
    assert "op must be one of add|sub|mul|div" in r.text
