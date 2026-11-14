
                     --------------- DATA_INGESTION FOR TXT FILES----------------------


# read a file
file = open("test.txt", "r")
contents = file.read()
print(contents)

# using with:
with open("test.txt", "r") as file:
    contents = file.read()
    print(contents)

# TXT
# READING A FILE
with open("/Users/keerthanasreearrola/Downloads/test.txt", "r") as file:
    contents = file.read()
    print(contents)

# WRITING A FILE
with open("/Users/keerthanasreearrola/Downloads/test.txt", "w") as file:
    file.write("This is a Data Engineering Class.")
    file.write("\n we are learning data ingestion concepts.")
    file.write("\n we are writing functions.")
with open("/Users/keerthanasreearrola/Downloads/test.txt", "r") as file:
    contents = file.read()
    print(contents)

# APPEND A TXT FILE
with open("/Users/keerthanasreearrola/Downloads/test.txt", "a") as file:
    file.write("This is a Data Engineering Class.")
    file.write("\n we are learning data ingestion concepts.")

with open("/Users/keerthanasreearrola/Downloads/test.txt", "r") as file:
    contents = file.read()
    print(contents)

# READING A FILE WITH FUNCTION
def read_txt_file(filename):
    with open(filename, "r") as file:
        return file.read()

filename = "/Users/keerthanasreearrola/Downloads/test.txt"
content = read_txt_file(filename)
print(content)

# WRITING A FILE WITH FUNCTION
def write_txt_file(filename, contents):
    with open(filename, "w") as file:
        file.write(contents)

filename = "/Users/keerthanasreearrola/Downloads/test.txt"
write_txt_file(filename, "We are writing some functions.")
display_result = read_txt_file(filename)
print(display_result)

# APPEND A TXT FILE WITH FUNCTION

def append_txt_file(filename, contents):
    with open(filename, "a") as file:
        file.write(contents)

filename = "/Users/keerthanasreearrola/Downloads/test.txt"
append_txt_file(filename, "We are in TN, United states.")
append_txt_file(filename, "We are living in Knoxville.")
final_result = read_txt_file(filename)
print(final_result)











