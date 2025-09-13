def add (a, b):
    return a + b

def multi(a , b):
    return a, b


print(add (3, 4))
print(multi(3, 4))

#Default parameter
def greet(name = "Guest"):
    return f"Hello, {name}!"

def create_user(name, age, active=True):
    print(f"Name={name}, Age={age}, Active={active}")
create_user("Alice", True, 30)   # ❌ Wrong: active=True, age=30
create_user(name = "Alice", age = 30)  # ✅ Correct
create_user(age = 30, name = "Alice")  # ✅ Correct

print(greet())          # Uses default parameter
print(greet("Bob"))     # Overrides default parameter

#keyword arguments
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."
print(describe_person(age=25, name="Alice", city="New York"))

#recursion function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)