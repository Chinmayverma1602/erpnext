import json
import requests

base_url = "http://localhost:8080"

headers = {
    "Authorization": "token df7f7b5d1deaec3:4a2f9bb2dfd7072"
}
doc_type ="User"
response = requests.get(f"{base_url}/api/resource/{doc_type}",headers=headers)

if response.status_code == 200:
    print (response.json())
else:
    print("Failed to fetch data")