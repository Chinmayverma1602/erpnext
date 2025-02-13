import json
import requests

base_url = "http://localhost:8080"
headers = {
    "Authorization": "token df7f7b5d1deaec3:4a2f9bb2dfd7072",
    "Content-Type": "application/json"
}

# Corrected user data structure
user_data = {
    "doctype": "User",
    "email": "example@email.com",
    "first_name": "John",
    "last_name": "Doe",
    "send_welcome_email": 0,
    "language": "en",
    "user_type": "System User"
}

response = requests.post(
    f"{base_url}/api/resource/User",
    headers=headers,
    data=json.dumps(user_data)
)

if response.status_code == 200:
    print("User created successfully:")
    print(response.json())
else:
    print(f"Failed to create user. Status code: {response.status_code}")
    print(response.text)