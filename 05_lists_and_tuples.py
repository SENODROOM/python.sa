"""
05 - Lists and Tuples
Covers: list creation, indexing, slicing, methods, tuples, list comprehensions
"""

fruits = ["apple", "banana", "cherry", "date"]

print("Original list:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

fruits.append("elderberry")
fruits.insert(1, "avocado")
print("After append/insert:", fruits)

fruits.remove("banana")
popped = fruits.pop()
print("After remove/pop:", fruits, "| popped:", popped)

fruits.sort()
print("Sorted:", fruits)

# List comprehension - squares of even numbers
squares = [x * x for x in range(1, 11) if x % 2 == 0]
print("Squares of even numbers 1-10:", squares)

# Tuples (immutable)
coordinates = (10.5, 20.3)
x, y = coordinates
print(f"Coordinates: x={x}, y={y}")

# Tuple in a list, common pattern for records
students = [("Ali", 85), ("Sara", 92), ("Zain", 78)]
for student_name, mark in students:
    print(f"{student_name}: {mark}")

top_student = max(students, key=lambda s: s[1])
print("Top student:", top_student)
