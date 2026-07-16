"""
01 - Variables and Basic Input/Output
Covers: variables, data types, input(), print(), type conversion
"""

# Declaring variables of different types
name = "Alex"
age = 25
height_m = 1.75
is_student = True

print("Name:", name)
print("Age:", age)
print("Height (m):", height_m)
print("Is student:", is_student)
print("Type of age:", type(age))

# Getting input from the user (converted to correct type)
user_name = input("What is your name? ")
user_age = int(input("What is your age? "))

print(f"Hello {user_name}, next year you will be {user_age + 1} years old.")
