"""
SIMPLE NUMPY PROJECT: CLEAN SENSOR DATA
1. Read csv file
2. Clean the data (remove any duplicates, remove missing data)
3. scale values 0-1
4. save the clean data to new csv file
"""
import numpy as np

# 1. READ the CSV file
#    skip_header=1 skips the column name row.
#    usecols=1 reads only the 2nd column (temperature).
filepath = "/Users/keerthanasreearrola/Downloads/sensor_readings.csv"
temps = np.genfromtxt(filepath, delimiter=",", skip_header=1, usecols=1)
print("1. Read from CSV:", temps.size, "readings")
print("   ", temps)

# 2. Find bad values (missing and wrong)
bad = np.isnan(temps) | (temps < -50)
print("Bad values:", bad.sum(), "out of", temps.size)
# Finding the Bad percentage
print("Bad Percentage: ",round((bad.sum())/temps.size * 100, 2), "%")

# 3. Cleaned Data
clean = temps[~bad]
print("   ", clean)


# 4. FIND repeated values
values, counts = np.unique(clean, return_counts=True)
print("4. Repeated:", values[counts > 1])

# 5. SORT
print("5. Sorted  :", np.sort(clean))

# 6. STATS
average = np.mean(clean)
print("6. Average:", round(average, 2))
print("   Median :", np.median(clean))
print("   Std dev:", round(np.std(clean), 2))
print("   Highest:", np.max(clean))
print("   Lowest :", np.min(clean))

# 7. LABEL each reading (np.where)
labels = np.where(clean > average, "High", "Normal")
print("7. High readings:", np.sum(labels == "High"), "| Normal readings:", np.sum(labels == "Normal"))

# 8. SCALE values to 0 - 1
scaled = (clean - clean.min()) / (clean.max() - clean.min())
print("8. Scaled  :", np.round(scaled, 2))

# 9. SAVE the clean data to a new CSV file
table = np.column_stack((clean, scaled))
np.savetxt("clean_sensor_readings.csv", table, delimiter=",", fmt="%.2f",
           header="temperature,scaled", comments="")
print("9. Saved: clean_sensor_readings.csv")


