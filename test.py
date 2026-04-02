import requests

url_data = "https://dummyjson.com/carts/add"
json_data = {
    "userId": 1,
    "products": [
        {
            "id": 152,
            "quantity": 4,
        }
    ]
}
res = requests.post(url=url_data, json=json_data)
print(res.json())
