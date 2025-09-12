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