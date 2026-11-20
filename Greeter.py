
# OOP PYTHON - LESSON 1
# Code Lab Activity
# Name: Reymark O. Nagrana


# PART 1: ENVIRONMENT SETUP

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to OOP in Python.")


g = Greeter("Reymark")
g.greet()


# PART 2 AND 3: CAR CLASS

class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self, km):
        if km <= 0:
            print("Distance must be positive.")
            return
        print(f"The car traveled {km} km.")

    def age(self, year):
        return year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)

print("\nCAR INFORMATION")
print(car1)
print(car2)
print(car3)

print("\nCAR METHODS")
car1.drive(50)
print("Car Age:", car1.age(2026))


# PART 4: LIBRARY BOOK MINI PROJECT

class LibraryBook:
    book_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        LibraryBook.book_count += 1

    def borrow(self):
        if self.is_borrowed:
            print("This book is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print("This book was not borrowed.")

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"LibraryBook(title={self.title!r}, author={self.author!r})"


book1 = LibraryBook("Python Basics", "John Smith")
book2 = LibraryBook("Introduction to Programming", "Jane Doe")

print("\nLIBRARY BOOK")

book1.borrow()
book2.borrow()
book1.return_book()

print(book1)
print(book2)

print(repr(book1))
print("Total Books:", LibraryBook.book_count)
