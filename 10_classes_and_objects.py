"""
10 - Object-Oriented Programming Basics
Covers: classes, __init__, methods, inheritance, super(), polymorphism
"""


class Animal:
    def __init__(self, name, sound="..."):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, sound="Woof")
        self.tricks = []

    def learn_trick(self, trick):
        self.tricks.append(trick)

    def make_sound(self):
        # Overriding the parent method (polymorphism)
        return f"{self.name} barks: {self.sound}!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, sound="Meow")


class BankAccount:
    """A simple class demonstrating encapsulation."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # convention: "protected" attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance


if __name__ == "__main__":
    animals = [Dog("Rex"), Cat("Whiskers"), Animal("Generic Creature")]

    for animal in animals:
        print(animal.make_sound())

    rex = animals[0]
    rex.learn_trick("sit")
    rex.learn_trick("roll over")
    print(f"{rex.name}'s tricks: {rex.tricks}")

    account = BankAccount("Fatima", 100)
    account.deposit(50)
    account.withdraw(30)
    print(f"{account.owner}'s balance: {account.balance}")
