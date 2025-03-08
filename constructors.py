"""1. Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class """

class Example:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            print(f"One-argument constructor called with value: {arg1}")
        else:
            print(f"Two-argument constructor called with values: {arg1}, {arg2}")

    @staticmethod
    def display():
        print("Object created successfully")

class Main:
    def __init__(self):
        obj1 = Example()
        obj1.display()

        obj2 = Example(10)
        obj2.display()

        obj3 = Example(10, 20)
        obj3.display()

Main()


"""----------2. Call the constructors(both default and argument constructors) of super class from a child class-----"""

class SuperClass:
    def __init__(self, arg1=None):
        if arg1 is None:
            print("SuperClass Default Constructor Called")
        else:
            print(f"SuperClass Argument Constructor Called with value: {arg1}")

class ChildClass(SuperClass):
    def __init__(self, arg1=None):
        if arg1 is None:
            super().__init__()
        else:
            super().__init__(arg1)
        print("ChildClass Constructor Called")

child1 = ChildClass()
child2 = ChildClass(10)


"""--------3. Apply private, public, protected and default access modifiers to the constructor------"""

class SuperClass:
    def __init__(self):
        self.public_var = "Public constructor"   # Public
        self._protected_var = "Protected constructor"  # Protected
        self.__private_var = "Private constructor"  # Private

    def display(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")

class ChildClass(SuperClass):
    def __init__(self):
        super().__init__()
        print("ChildClass constructor called")
        print(f"Accessing Public: {self.public_var}")
        print(f"Accessing Protected: {self._protected_var}")
        try:
            print(f"Accessing Private: {self.__private_var}")
        except AttributeError:
            print("Private variable is not accessible directly")

# Create an object of the ChildClass
child = ChildClass()
child.display()


"""---------4. Write a program which illustrates the concept of attributes of a constructor.---------"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.display()
person2.display()
