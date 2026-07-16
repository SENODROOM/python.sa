"""
09 - File Handling
Covers: reading/writing text files, context managers, appending, CSV-like parsing
"""

import os

filename = "sample_notes.txt"

# Writing to a file
with open(filename, "w") as f:
    f.write("Line 1: Learning Python\n")
    f.write("Line 2: File handling is useful\n")
    f.write("Line 3: Practice makes perfect\n")

# Reading the whole file
with open(filename, "r") as f:
    content = f.read()
print("Full file content:")
print(content)

# Reading line by line
with open(filename, "r") as f:
    print("Line by line:")
    for line_number, line in enumerate(f, start=1):
        print(f"  {line_number}: {line.strip()}")

# Appending to a file
with open(filename, "a") as f:
    f.write("Line 4: Appended later\n")

with open(filename, "r") as f:
    print("After appending:")
    print(f.read())

# Simple CSV-style read/write (no external library)
records = [("Ali", 85), ("Sara", 92), ("Zain", 78)]
csv_filename = "students.csv"

with open(csv_filename, "w") as f:
    f.write("name,score\n")
    for student_name, score in records:
        f.write(f"{student_name},{score}\n")

with open(csv_filename, "r") as f:
    lines = f.read().splitlines()
    header = lines[0].split(",")
    print("CSV header:", header)
    for row in lines[1:]:
        parts = row.split(",")
        print(f"  {parts[0]} -> {parts[1]}")

# Clean up generated files
os.remove(filename)
os.remove(csv_filename)
