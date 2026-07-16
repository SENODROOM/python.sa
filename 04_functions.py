"""
04 - Functions
Covers: defining functions, parameters, default args, *args/**kwargs, return values
"""


def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"


def add_all(*numbers):
    """Sum an arbitrary number of arguments."""
    return sum(numbers)


def describe_person(**details):
    """Print key-value pairs passed as keyword arguments."""
    for key, value in details.items():
        print(f"{key}: {value}")


def is_even(n):
    return n % 2 == 0


def factorial(n):
    """Recursive factorial function."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(greet("Sara"))
    print(greet("Sara", greeting="Hi"))

    print("Sum:", add_all(1, 2, 3, 4, 5))

    describe_person(name="Sara", age=30, city="Lahore")

    print("Is 7 even?", is_even(7))
    print("Is 8 even?", is_even(8))

    print("5! =", factorial(5))
