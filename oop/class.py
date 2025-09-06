class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def greet():
        return f"Hello, my name is years old."  
    
#instance
person1 = Person("Alice", 30)
print(person1.greet())