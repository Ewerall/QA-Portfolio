import pytest
import requests

def test_create_user(base_url, new_user_data, auth_token, api_headers):
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    response = requests.post(
        f"{base_url}/users",
        json=new_user_data,
        headers=headers
    )
    print(f"Create User Response: {response.status_code} - {response.text}")
    assert response.status_code == 201
    return response.json()["id"] 

'''
it's bad, but I wanted three tests for create, update, and delete at the same time, so I have to use return in test_create_user
'''

def test_update_user(base_url, new_user_data, auth_token, api_headers):
    user_id = test_create_user(base_url, new_user_data, auth_token, api_headers)
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    
    updated_data = {"job": "Senior QA"}
    response = requests.put(
        f"{base_url}/users/{user_id}",
        json=updated_data,
        headers=headers
    )
    print(f"Update User Response: {response.status_code} - {response.text}")
    assert response.status_code == 200

def test_delete_user(base_url, new_user_data, auth_token, api_headers):
    user_id = test_create_user(base_url, new_user_data, auth_token, api_headers)
    headers = {**api_headers, "Authorization": f"Bearer {auth_token}"}
    
    response = requests.delete(
        f"{base_url}/users/{user_id}",
        headers=headers
    )
    print(f"Delete User Response: {response.status_code}")
    assert response.status_code == 204