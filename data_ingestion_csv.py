import csv
from csv import reader, DictReader
# READ CSV FILE USING csv.reader -> each row is returned as a list
with open("/Users/keerthanasreearrola/Downloads/test.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# READ CSV FILE USING csv.DictReader -> read CSV data using column names instead of indexes
with open("/Users/keerthanasreearrola/Downloads/test.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# WRITE CSV FILE
# with csv.writer
columns = ["id", "name"]
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerow([1,"keerthana"])
    writer.writerow([2,"mounika"])
    writer.writerow( [3,"kate"])
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# with csv.DictWriter
columns = ["id", "name"]
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerow({"id": 1, "name": "srisailam"})
    writer.writerow({"id": 2, "name": "mounika"})
    writer.writerow({"id": 3, "name": "vijayalaxmi"})
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# APPEND A CSV FILE
# with csv.writer
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([4,"swetha"])
    writer.writerow([5,"rahul"])
    writer.writerow([6,"sravani"])

with open("/Users/keerthanasreearrola/Downloads/test1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# with csv.DictWriter
columns = ["id", "name"]
with open("/Users/keerthanasreearrola/Downloads/test1.csv", "a", ) as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writerow({"id": 9, "name": "srii"})
    writer.writerow({"id": 10, "name": "arrola"})
    writer.writerow({"id": 11, "name": "ram"})

with open("/Users/keerthanasreearrola/Downloads/test1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# WITH FUNCTIONS
# READ A CSV FILE

def  read_csv_file(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))

filepath = "/Users/keerthanasreearrola/Downloads/test1.csv"
result = read_csv_file(filepath)
print(result)

# WRITE A CSV FILE

def write_csv_file(file_path, rows, columns):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerow(rows)

filepath = "/Users/keerthanasreearrola/Downloads/test1.csv"
cols = ["id", "name"]
write_csv_file(filepath, {"id": 16, "name": "ABCDE"}, cols)

result = read_csv_file(filepath)
print(result)

# APPEND A CSV FILE

def append_csv_file(file_path, rows, columns):
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(rows)

filepath = "/Users/keerthanasreearrola/Downloads/test1.csv"
cols = ["id", "name"]
append_csv_file(filepath, {"id": 1, "name": "sree"}, cols)
append_csv_file(filepath, {"id": 2, "name": "arrola"}, cols)
append_csv_file(filepath, {"id": 3, "name": "keerthana"}, cols)
append_csv_file(filepath, {"id": 4, "name": "mounika"}, cols)
result = read_csv_file(filepath)
print(result)
