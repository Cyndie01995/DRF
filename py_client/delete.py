import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

product_id = input("What is the product id you want to use \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')    

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"


# get_response = requests.get(endpoint, params={"product_id": 123}, json={
#     "query": "Hello, world"
# })

    get_response = requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code==204)
# print(get_response.text)

# HTTP REQUEST -> HTML
# REST API HTTP Request -> JSON (XML)
# JSON -> JAVASCRIPT OBJECT NOTATION
# print(get_response.json())