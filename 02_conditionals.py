"""
02 - Conditionals
Covers: if / elif / else, comparison and logical operators
"""

number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")

# Grading example using elif chain
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Logical operators
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age >= 18 and has_id:
    print("You may enter.")
else:
    print("Entry denied.")
