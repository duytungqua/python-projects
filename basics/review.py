#class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
#instance
person1 = Person("Alice", 30)
print(person1.greet())

#print
print("Review Complete!")
# Review of Python Basics

#variables and data types
a = 10               # Integer
b = 2.5              # Float
text = "Python"      # String
is_active = False    # Boolean
print(a, b, text, is_active)
