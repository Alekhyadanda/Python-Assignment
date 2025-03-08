"""-------PACKAGES----"""
"""---------1. Create a program to create two class. 
1.1. Create a constructor and a method for each class 
1.2. Create a __init__.py for adding all packages 
1.3. Import the respective packages 
1.4. Call each class by creating an object to it  
1.5. Create a program by all the above--------"""

class ClassA:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from {self.name} in ClassA!")

class ClassB:
    def __init__(self, age):
        self.age = age

    def display(self):
        print(f"Age is {self.age} in ClassB!")

objA = ClassA("ClassA Object")
objA.greet()

objB = ClassB(25)
objB.display()

