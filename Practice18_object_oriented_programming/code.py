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
