"""
07 - String Manipulation
Covers: string methods, formatting, slicing, palindrome check
"""

text = "  Hello, Python World!  "

print("Original:", repr(text))
print("Stripped:", text.strip())
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Replace:", text.replace("Python", "Beginner"))
print("Split:", text.strip().split(" "))

# String slicing
word = "Programming"
print("Reversed:", word[::-1])
print("First 4 chars:", word[:4])
print("Every 2nd char:", word[::2])

# f-strings and formatting
name = "Bilal"
score = 87.5678
print(f"{name} scored {score:.2f} points")
print(f"{name:>15}")  # right aligned
print(f"{name:*^15}")  # centered, padded with *


def is_palindrome(s):
    """Check if a string reads the same forwards and backwards."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


test_words = ["racecar", "hello", "A man a plan a canal Panama"]
for w in test_words:
    print(f"'{w}' is palindrome? {is_palindrome(w)}")


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")


print("Vowels in 'Programming':", count_vowels("Programming"))
