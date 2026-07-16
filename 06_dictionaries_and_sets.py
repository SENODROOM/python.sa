"""
06 - Dictionaries and Sets
Covers: dict creation, access, methods, iteration, sets and set operations
"""

student = {
    "name": "Ayesha",
    "age": 21,
    "courses": ["Math", "Physics"]
}

print("Student dict:", student)
print("Name:", student["name"])
print("Age (with get):", student.get("age"))
print("GPA (missing, default):", student.get("gpa", "N/A"))

student["gpa"] = 3.8
student.update({"age": 22})
print("After updates:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

print("Iterating items:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Word frequency counter using a dictionary
text = "the quick brown fox jumps over the lazy dog the fox runs"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print("Word counts:", word_counts)

# Sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric difference:", a ^ b)
