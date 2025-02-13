import json
import requests

base_url = "http://localhost:8080"
headers = {
    "Authorization": "token df7f7b5d1deaec3:4a2f9bb2dfd7072",
    "Content-Type": "application/json"
}


address_data = {
    "doctype": "Address",
    "title": "Main Office",               # Standard title field
    "address_title": "Main Office",       # Alternative title field
    "name": "Main Office",                # Name field that might be used as title
    "address_name": "Main Office",        # Another possible title field
    "address_line1": "123 Main Street",
    "address_line2": "Suite 456",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "booth_number": "B123",
    "is_primary_address": 1,              # Added this field as it might be required
    "is_shipping_address": 0,             # Added this field as it might be required
    "address_type": "Office"              # Added address type
}

# Make the POST request
response = requests.post(
    f"{base_url}/api/resource/Address",
    headers=headers,
    data=json.dumps(address_data)
)

# Check the response with more detailed error handling
if response.status_code == 200:
    print("Address created successfully:")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Failed to create address. Status code: {response.status_code}")
    try:
        error_details = response.json()
        print("Error details:")
        print(json.dumps(error_details, indent=2))
    except:
        print(response.text)