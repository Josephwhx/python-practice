# Without using class
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))
print(student.name)
print(student.grades)
print(student.average_grade())


'''
Magic methods - __str__ and __repr__
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # magic methods to display value when object is print
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)
print(bob)


'''
Class inheritance 
'''

# Example 1


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print("Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnect()


'''
Class Composition
'''

# Example 1


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)

'''Main difference between composition and inheritance, inheritance means a book is a bookshelf where composition mean a bookshelf has many books'''
