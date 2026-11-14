import json
# READ A JSON FILE
with open("/Users/keerthanasreearrola/Downloads/countries.json", "r") as file:
    data = json.load(file)
print(data)

# READ A JSON WITH FUNCTION
def read_json():
    with open("/Users/keerthanasreearrola/Downloads/countries.json", "r") as file:
        data = json.load(file)
read_json()

# WRITE A JSON FILE
