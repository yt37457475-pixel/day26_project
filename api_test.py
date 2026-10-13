import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=15)

print("Status:", response.status_code)

if response.status_code == 200:
    user = response.json()
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
else:
    print("Request failed")