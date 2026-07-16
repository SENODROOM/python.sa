"""
08 - Exception Handling
Covers: try/except/else/finally, multiple exceptions, raising custom exceptions
"""


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
    except TypeError:
        print("Error: both inputs must be numbers.")
        return None
    else:
        print("Division succeeded.")
        return result
    finally:
        print(f"Attempted to divide {a} by {b}")


class NegativeNumberError(Exception):
    """Custom exception for invalid negative input."""
    pass


def take_square_root(n):
    if n < 0:
        raise NegativeNumberError(f"Cannot take square root of negative number: {n}")
    return n ** 0.5


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(10, "a"))

    for value in [16, -4]:
        try:
            print(f"sqrt({value}) = {take_square_root(value)}")
        except NegativeNumberError as e:
            print("Caught custom error:", e)

    # Handling input errors from the user
    while True:
        user_input = input("Enter an integer (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
        try:
            number = int(user_input)
            print("You entered:", number)
        except ValueError:
            print("That's not a valid integer, try again.")
