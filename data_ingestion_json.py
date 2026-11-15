import json

# READ A JSON FILE
with open("/Users/keerthanasreearrola/Downloads/countries.json", "r") as file:
    data = json.load(file)
print(data)

# READ A JSON WITH FUNCTION
def read_json(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
        return data

filepath = "/Users/keerthanasreearrola/Downloads/countries.json"
display_result = read_json(filepath)
print(display_result)

# WRITE A JSON FILE

data = {
    "countries": [
        {
            "name": "India",
            "code": "IN",
            "capital": "New Delhi",
            "region": "Asia",
            "population": "13800000000",
            "currency": "INR"
        }
    ]
}
with open("/Users/keerthanasreearrola/Downloads/countries.json", "w") as file:
    json.dump(data, file)
with open("/Users/keerthanasreearrola/Downloads/countries.json", "r") as file:
    data = json.load(file)
print(data)


# WRITE A JSON FILE USING FUNCTION

def write_json(filepath, data):
    with open(filepath, "w") as file:
        data = json.dump(data, file)
        return data

filepath = "/Users/keerthanasreearrola/Downloads/countries.json"
data = {
    "countries": [
        {
            "name": "United States",
            "code": "US",
            "capital": "Washington DC",
            "region": "North America",
            "population": "100000000",
            "currency": "USD"
        }
    ]
}
write_json(filepath,data)
result = read_json(filepath)
print(result)


#APPEND JSON FILE

new_data = {
    "countries": [
        {
            "name": "United States",
            "code": "US",
            "capital": "Washington DC",
            "region": "North America",
            "population": "100000000",
            "currency": "USD"
        }
    ]
}
filepath = "/Users/keerthanasreearrola/Downloads/countries.json"

# READ EXISTING DATA
with open(filepath, "r") as file:
    data = json.load(file)

# APPEND NEW DATA
"""
data: Entire JSON data
data["countries"]: Accesses the countries list
.append(): Adds a new item to the list
new_data: The country dictionary we want to add
"""
data["countries"].append(new_data)

# WRITE UPDATED DATA
with open(filepath, "w") as file:
    json.dump(data, file, indent=4)

# READ AND PRINT
with open(filepath, "r") as file:
    data = json.load(file)
print(data)

# APPEND TO JSON USING FUNCTION

filepath = "/Users/keerthanasreearrola/Downloads/countries.json"
new_country = {
    "countries": [
        {"name": "Nepal",
        "code": "NP",
        "capital": "Kathmandu",
        "region": "Asia",
        "population": 29136808,
        "currency": "NPR"}
    ]
}
def append_json():
    data = read_json(filepath)
    data["countries"].append(new_country)
    write_json(filepath, data)
append_json()
result = read_json(filepath)
print(result)

