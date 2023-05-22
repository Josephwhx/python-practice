'''
unpacking arguments (*args) - used when total number of arguments are still unknown
'''

# Example 1


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))


def multiply(*args):
    total = 1
    for arg in args:
        total = total * args

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 5, 7, operator="*"))


'''
unpacking keyword arguments (**kwargs)
'''

# Example 1


def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# Example 2

def both(*args, ** kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)