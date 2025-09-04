
def greet():
    return "Hello from func.py!"

def add(a, b):
    return a + b

greet()
add(3, 4)

#Default function parameters
def power(base, exponent = 2):
    return base ** exponent
power(3)
power(2, 3)