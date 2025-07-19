import pytest
import requests

BASE_URL = "https://reqres.in/api"

def test_get_user():
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id