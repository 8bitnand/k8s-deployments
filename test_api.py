from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"response": "Hello World"}


def test_read_random():
    response = client.get("/random")
    assert response.status_code == 200
    number = response.json()["random_number"]
    assert 0 < number < 100
