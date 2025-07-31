import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def api_headers():
    return {"x-api-key": "reqres-free-v1"}

@pytest.fixture
def user_data():
    return {"name": "Vasya", "job": "QA Engineer"}

@pytest.fixture(scope="session")
def auth_token(base_url, api_headers):
    auth_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(
        f"{base_url}/login", 
        json=auth_data,
        headers=api_headers
    )
    assert response.status_code == 200
    return response.json()["token"]

