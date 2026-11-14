
# parameter funtion

def show_message(course):
    print("Welcome to " + course)

show_message("data engineering")

# parameter function
def greet(name):
    print("Hello, " + name)
greet("Keerthana")
greet("Sree")
# Add function (multiple parameter)
def add(a,b):
    return a + b
result = add(1, 2)
print(result)

# Default parameter
def greet(name="Sree"):
    print("Hello, " + name)
greet("Keerthana")
greet()

# Default parameter
def power(base, exponent=2):
    return base ** exponent
print(power(2, 3))
print(power(2))

# args
def add_numbers(*args):
   return sum(args)

print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(1,2))

print(add_numbers(*range(1,5)))

# FUNCTION BASED CALCULATOR
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    return a / b

print(add(10, 2))
print(subtract(10, 2))
print(multiply(10, 2))
print(divide(10, 2))


# check if the number is positive

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

print(is_positive(10))
print(is_positive(-10))

# check if the number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(-5))

