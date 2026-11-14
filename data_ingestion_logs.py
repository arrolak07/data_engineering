#__________________ DATA INGESTION_LOGS__________________
import logging
from _pyrepl import content
from datetime import datetime

# LOGS
# READ A LOG
with open("/Users/keerthanasreearrola/Downloads/test.log", "r") as file:
    for line in file:
        print(line, end="")
# WRITE A LOG
# just a normal log
with open("/Users/keerthanasreearrola/Downloads/test1.log", "w") as file:
        file.write("Application started\n")
        file.write("Reading CSV file\n")
        file.write("Data ingestion completed\n")
with open("/Users/keerthanasreearrola/Downloads/test1.log", "r") as file:
    for line in file:
        print(line, end="")

# writing an actual log with timestamps, error , info
logging.basicConfig(
    filename ="/Users/keerthanasreearrola/Downloads/test1.log" ,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.info("Application started")
logging.info("Reading CSV file")
logging.warning("Missing values")
logging.error("Data ingestion failed")
logging.info("Appplication completed")
logging.info("Reading CSV file")
logging.warning("Missing values")

with open("/Users/keerthanasreearrola/Downloads/test1.log", "r") as file:
    for line in file:
        print(line, end="")

# APPEND A LOG FILE
logging.basicConfig(
    filename = "/Users/keerthanasreearrola/Downloads/test1.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.info("Application started")
logging.info("Reading CSV file")
logging.warning("Duplicate values")
logging.error("Data ingestion failed")

with open("/Users/keerthanasreearrola/Downloads/test1.log", "r") as file:
    for line in file:
        print(line, end="")
        

# USING FUNCTIONS

# READ A LOG FILE
def read_log_file(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")

filename= "/Users/keerthanasreearrola/Downloads/test1.log"
contents = read_log_file(filename)
print(contents)

# WRITE A LOG FILE
# WITH JUST A MESSAGE
def write_log_file(filepath, contents):
    with open(filepath, "w") as file:
        file.write(contents)

filepath = "/Users/keerthanasreearrola/Downloads/test1.log"
write_log_file(filepath, "Application started\n")
write_log_file(filepath, "Reading CSV file\n")
write_log_file(filepath, "Data ingestion completed\n")
display_result = read_log_file(filepath)
print(display_result)


# WITH PROPER TIMESTAMP, ERROR INFO...
def write_log_file(filepath, content):
    with open(filepath, "w") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {content}\n")
filepath = "/Users/keerthanasreearrola/Downloads/test1.log"
write_log_file(filepath, "Application started\n")
display_result = read_log_file(filepath)
print(display_result)

# APPEND A LOG FILE
def append_log_file(filepath, contents):
    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {contents}\n")
filepath = "/Users/keerthanasreearrola/Downloads/test1.log"
append_log_file(filepath, "Reading CSV\n")
append_log_file(filepath, "Data ingestion completed\n")
display_result = read_log_file(filepath)
print(display_result)
