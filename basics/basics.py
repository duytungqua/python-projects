#print

print("Hello, World!")

# Variables and Data Types
x = 5               # Integer
y = 3.14            # Float
name = "Alice"      # String
is_student = True   # Boolean       

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # Accessing list element        
fruits.append("date") # Adding an element to the list
print(fruits)

#indentation
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# Loops
for fruit in fruits:
    print(fruit)    

i = 0
while i < 5:
    print(i)
    i += 1

#break and continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers less than 5

# Functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))

# Classes
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"  