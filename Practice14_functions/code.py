'''
Introduction to functions in python
'''

# Example 1


def hello():
    print("Hello!")


hello()


# Example 2

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")


# Example 3

friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]


add_friend()


'''
Functions with arguments and parameters
'''

# Example 1


def say_hello(name, surname):
    print(f"Hello, {name} {surname}")


say_hello("Bob", "Smith")
# Alternative
say_hello(surname="Bob", name="Smith")  # swap of the previous line


# Example 2

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You Fool!")


divide(15, 3)


'''
Default parameter values
'''

# Example 1

default_y = 3


def add(x, y=default_y):
    print(x + y)


add(5)


'''
Functions returning value
'''

# Example 1


def add(x, y):
    return x + y


result = add(5, 8)
print(result)
