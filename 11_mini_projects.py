"""
11 - Mini Projects
Three small self-contained beginner projects in one file:
  1. Number guessing game
  2. Simple calculator
  3. To-do list manager (in-memory)
Run this file and pick an option from the menu.
"""

import random


def number_guessing_game():
    secret = random.randint(1, 50)
    attempts = 0
    print("I'm thinking of a number between 1 and 50.")
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


def simple_calculator():
    print("Simple Calculator (type 'q' to quit)")
    while True:
        expr = input("Enter expression like '3 + 4': ")
        if expr.lower() == "q":
            break
        try:
            a_str, op, b_str = expr.split()
            a, b = float(a_str), float(b_str)
        except ValueError:
            print("Invalid format. Use: number operator number")
            continue

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Cannot divide by zero.")
                continue
            result = a / b
        else:
            print("Unknown operator. Use +, -, *, /")
            continue

        print(f"Result: {result}")


def todo_list_manager():
    tasks = []
    print("To-Do List (commands: add, remove, list, quit)")
    while True:
        command = input("> ").strip().lower()
        if command == "quit":
            break
        elif command == "add":
            task = input("Task description: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif command == "remove":
            if not tasks:
                print("List is empty.")
                continue
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            index = int(input("Number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        elif command == "list":
            if not tasks:
                print("No tasks yet.")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("Unknown command. Try: add, remove, list, quit")


if __name__ == "__main__":
    menu = """
Choose a mini project:
  1. Number Guessing Game
  2. Simple Calculator
  3. To-Do List Manager
  q. Quit
"""
    print(menu)
    choice = input("Choice: ").strip()
    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        simple_calculator()
    elif choice == "3":
        todo_list_manager()
    else:
        print("Goodbye!")
