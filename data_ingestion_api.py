#                            ***** DATA INGETSION FOR API *******

import requests

# READ A API
url = "https://dummyjson.com/products"
response = requests.get(url)
data = response.json()
print(data)

# READ A API with function

def read_api(url):
    response = requests.get(url)
    data = response.json()
    print(data)
url = "https://dummyjson.com/products"
read_api(url)

