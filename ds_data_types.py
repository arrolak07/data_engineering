"""
# Operations on Lists

# Define a list
my_list = [1, 2, 3, 4, 5]

# Append an element
my_list.append(6)
print(my_list)

# Insert an element at a specific index
my_list.insert(2, 10)
print(my_list)

# Remove an element
my_list.remove(3)
print(my_list)

# Access an element using indexing
print(my_list[0])  # Output: 1

# Slice the list
print(my_list[1:4])  # Output: [2, 10, 4]


# Operation on Tuples

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Concatenate two tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)

# Access an element using indexing
print(my_tuple[0])  # Output: 1

# Slice the tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Operations on Sets

# Define a set
my_set = {1, 2, 3, 4, 5}

# Add an element
my_set.add(6)
print(my_set)

# Remove an element
my_set.remove(3)
print(my_set)

# Check for membership
print(2 in my_set)  # Output: True

# Union of two sets
other_set = {4, 5, 6, 7}
union_set = my_set.union(other_set)

print(union_set)  # Output: {1, 2, 4, 5, 6, 7}



# Operation on Dictionary

# Define a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Access a value using a key
print(my_dict['name'])  # Output: John

# Add a new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)

# Modify a value
my_dict['age'] = 35
print(my_dict)

# Remove a key-value pair
del my_dict['city']

print(my_dict)  # Output: {'name': 'John', 'age': 35, 'gender': 'Male'}


# Generate a new list using list comprehension
squared_numbers = [x ** 2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Generate squared numbers using a for loop
squared_numbers = []
for number in range(1, 6):
    squared_numbers.append(number ** 2)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
"""




