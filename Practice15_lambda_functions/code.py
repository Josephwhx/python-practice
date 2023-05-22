# Example 1
def add(x, y): return x + y


print(add(5, 7))


# Example 2

def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [doubled(x) for x in sequence]
# Alternative
doubled = map(double, sequence)
# Using lambda function
doubled = [(lambda x: x*2)(x) for x in sequence]

# Overview
'''Lambdas are just functions without name.'''
