"""
03 - Loops
Covers: for loops, while loops, range(), break, continue
"""

# For loop - print numbers 1 to 10
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# For loop - sum of a list
numbers = [4, 8, 15, 16, 23, 42]
total = 0
for n in numbers:
    total += n
print(f"Sum of {numbers} = {total}")

# While loop - countdown
print("Countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# break and continue
print("Skipping multiples of 3, stopping at 20:")
for i in range(1, 30):
    if i == 20:
        break
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Nested loop - multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
