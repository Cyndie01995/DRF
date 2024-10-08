import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/1/"

# get_response = requests.get(endpoint, params={"product_id": 123}, json={
#     "query": "Hello, world"
# })

get_response = requests.get(endpoint)

# print(get_response.text)

# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON (XML)
# JSON -> JAVASCRIPT OBJECT NOTATION
print(get_response.json())