# tests/test_app.py
import pytest
from keep_alive import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data

def test_addition(client):
    response = client.post("/calculate", data={
        "number_one": "5",
        "number_two": "3",
        "operation": "add"
    })
    assert response.status_code == 200
    assert b"8.0" in response.data

def test_subtraction(client):
    response = client.post("/calculate", data={
        "number_one": "10",
        "number_two": "4",
        "operation": "subtract"
    })
    assert response.status_code == 200
    assert b"6.0" in response.data

def test_multiplication(client):
    response = client.post("/calculate", data={
        "number_one": "6",
        "number_two": "7",
        "operation": "multiply"
    })
    assert response.status_code == 200
    assert b"42.0" in response.data

def test_division(client):
    response = client.post("/calculate", data={
        "number_one": "20",
        "number_two": "5",
        "operation": "divide"
    })
    assert response.status_code == 200
    assert b"4.0" in response.data

def test_invalid_operation(client):
    """Test that an invalid operation returns the page without result."""
    response = client.post("/calculate", data={
        "number_one": "10",
        "number_two": "5",
        "operation": "mod"
    })
    assert response.status_code == 200
    # Should not contain any numeric result
    assert b"result=" not in response.data