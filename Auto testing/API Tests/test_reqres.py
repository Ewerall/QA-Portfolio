import pytest
import requests
import time

BASE_URL = "https://reqres.in/api"

def test_get_user(base_url, api_headers, auth_token):
    user_id = 2
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    response = requests.get(
        f"{base_url}/users/{user_id}",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id

def test_create_user(base_url, user_data, auth_token, api_headers):
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    response = requests.post(
        f"{base_url}/users",
        json=user_data,
        headers=headers
    )
    print(f"Create User Response: {response.status_code} - {response.text}")
    assert response.status_code == 201
    return response.json()["id"] 

'''
return = bad, but i wanted three tests for create, update, and delete at the same time, so i have to use return in test_create_user
'''

def test_update_user(base_url, user_data, auth_token, api_headers):
    user_id = test_create_user(base_url, user_data, auth_token, api_headers)
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    
    updated_data = {"job": "Senior QA"}
    response = requests.put(
        f"{base_url}/users/{user_id}",
        json=updated_data,
        headers=headers
    )
    print(f"Update User Response: {response.status_code} - {response.text}")
    assert response.status_code == 200

def test_delete_user(base_url, user_data, auth_token, api_headers):
    user_id = test_create_user(base_url, user_data, auth_token, api_headers)
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    
    response = requests.delete(
        f"{base_url}/users/{user_id}",
        headers=headers
    )
    print(f"Delete User Response: {response.status_code}")
    assert response.status_code == 204
    
def test_endpoint_time(base_url, api_headers):
    start_time = time.time()
    response = requests.get(
        f"{base_url}/users?delay=1", 
        headers=api_headers
    )
    response_time = time.time() - start_time
    
    assert response.status_code == 200
    assert response_time < 2.0
    
    
@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (23, 404),
    (999, 404),
])
def test_get_user_status(base_url, api_headers, auth_token, user_id, expected_status):
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{base_url}/users/{user_id}", headers=headers)
    assert response.status_code == expected_status
    
def test_successful_login(base_url, api_headers):
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{base_url}/login", json=payload, headers=api_headers)
    assert response.status_code == 200
    assert "token" in response.json()

@pytest.mark.parametrize("email, password, expected_error", [
    ("fake@test.com", "cityslicka", "user not found"),
    ("eve.holt@reqres.in", "", "Missing password"),
    ("", "pupu", "Missing email or username"),
])
def test_failed_login(base_url, api_headers, email, password, expected_error):
    payload = {"email": email, "password": password}
    response = requests.post(f"{base_url}/login", json=payload, headers=api_headers)
    assert response.status_code == 400
    assert expected_error.lower() in response.json()["error"].lower()