import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'This field is done',
    'price': 10.45,
    'content': 'This is a sample product'
}
# get_response = requests.get(endpoint, params={"product_id": 123}, json={
#     "query": "Hello, world"
# })

get_response = requests.post(endpoint, json=data)

# print(get_response.text)

# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON (XML)
# JSON -> JAVASCRIPT OBJECT NOTATION
print(get_response.json())