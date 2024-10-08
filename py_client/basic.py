import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={"product_id": 123}, json={
#     "query": "Hello, world"
# })

get_response = requests.post(endpoint, json={
    "title": "Abc123",
    "content": "Hello, world",
    "price": "123.45"
})
print(get_response.text)

# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON (XML)
# JSON -> JAVASCRIPT OBJECT NOTATION
print(get_response.json())