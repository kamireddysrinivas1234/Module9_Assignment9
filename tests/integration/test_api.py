
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

import pytest
@pytest.mark.parametrize("a,b,op,expected", [
    (2,3,"add",5.0),
    (7,2,"sub",5.0),
    (3,4,"mul",12.0),
    (9,3,"div",3.0),
])
def test_api_calc(a,b,op,expected):
    r = client.post("/api/calc", json={"a": a, "b": b, "op": op})
    assert r.status_code == 200
    assert r.json()["result"] == expected

def test_divide_by_zero_400():
    r = client.post("/api/calc", json={"a": 1, "b": 0, "op": "div"})
    assert r.status_code == 400
    assert "Division by zero" in r.json()["detail"]
