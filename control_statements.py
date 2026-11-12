"""

# Hello program
print("Hello World!")

# Type checking
print(type(5))
print(type("Hello"))

# type conversion
x = 5
print(type(x))
y = int(x)
print(type(y))

# single line comment

# Type checking the x
x = 5.67
print(type(x))

# Multi-line comment

First checking the type of x 
secondly converting it to the appropriate type

x = 5
print(type(x))
y = int(x)
print(type(y))

# create variables or your name and age, then print them
name = "Keerthana"
age = 25
print(name)
print(age)

# create variables for two numbers and print their sum
number1 = 15
number2 = 7
sum = number1 + number2
print("Sum:", sum) # 22

# Arithmetic Operators
x = 10
y = 5
print("Addition:", x + y)  # 15
print("Subtraction:", x - y)  #5
print("Multiplication:", x * y)  #50
print("Division:", x / y)  #2.0
print("Modulo:", x % y) #0
print("Floor division:", x // y)  #2
print("Exponent:", x ** y) #100000

# Comparison Operators
a = 15
b = 3
print(a==b) #False
print(a!=b) #True
print(a>b) #True
print(a<b) #False

# Logical Operators

print(a>10 and b<2) #False
print(a==15 or b>5) #True
print(not(a==15)) #False

# looping through the list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



# looping through the string
name = "Keerthana"
for letter in name:
    print(letter)

# while loop
a = 1
while a <= 5:
    print(a)
    a += 1

# checking the list of items are even or odd
numbers = [3,4,6,2,9]
for number in numbers:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

"""


# Modify the code to also print if the number is positive, negative, or zero
number = int(input("Enter a number: "))
# Check if the number is even or odd
if number > 0:
    if number % 2 == 0:
        print(f"{number} is positive even number")
    else:
        print(f"{number} is positive odd number")
elif number < 0:
    if number % 2 == 0:
        print(f"{number} is negative even number")
    else:
        print(f"{number} is negative odd number")
else:
    print("It's Zero")



# GRADE CHECKER
marks = int(input("Enter your marks: "))
if marks > 100 or marks < 0:
    print("Invalid Marks")
else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")

# SUM OF NUMBERS
# Modify the code to calculate the sum of even numbers only using for loop

total = 0
for i in range(1,6):
    if i % 2 == 0:
        total += i
print("Sum of numbers from 1 to 5:", total)

# GUESSING GAME
# Task: Limit the number of attempts to 3
secret_number = 7
guess = 0
count = 0
while count < 3:
    count += 1
    guess = int(input("Guess a number (1-10): "))
    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")
if guess!=secret_number:
    print("Chances are completed.")

# LOGICAL OPERATORS
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (Y/N): ").lower() == "y"
if has_id and age >= 18:
    print("You can enter")
else:
    print("You can not enter")

# CALCULATOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
    print("Modulo:", a % b)
else:
    print("Division is not possible")
    print("Modulo is not possible")


# Add comparisons operator to check which number is greater
print("Is first number greater?", a > b)
print("Are both numbers equal?", a == b)
print("Are both numbers different?", a != b)

# Nested Control Flow
# Task: Add a feature to classify numbers as small(<10), medium(10-100) or large(>100)
num = int(input("Enter a number: "))

# Number classification
if num < 10:
    print("It's a small number")

elif num >=10 and num <= 100:
    print("It's a medium number")

else:
    print("It's a large number")

# Positive, negative, zero and even/odd classification
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

elif num < 0:
    if num % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")

else:
    print("The number is zero.")

# Mathod 2:
num = int(input("Enter a number: "))

if num < 10:
    print("Its a small number")

    if num > 0:
        if num % 2 == 0:
            print("Positive even number")
        else:
            print("Positive odd number")

    elif num < 0:
        if num % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")

    else:
        print("The number is zero.")

elif num >= 10 and num <= 100:
    print("Its a medium number")

    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

elif num > 100:
    print("Its a large number")

    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

