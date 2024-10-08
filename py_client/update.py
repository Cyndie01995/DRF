import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/2/update/"

# get_response = requests.get(endpoint, params={"product_id": 123}, json={
#     "query": "Hello, world"
# })

data = {
    "title": "This is Ada, Ada is a girl",
    "content": "This is a sample product",
    "price": 129.45
}

get_response = requests.put(endpoint, json=data)

# print(get_response.text)

# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON (XML)
# JSON -> JAVASCRIPT OBJECT NOTATION
print(get_response.json())