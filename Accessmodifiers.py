"""-----------8.Access Modifiers--------"""
"""----------1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method. 
Create a sub class and try to access the private fields and methods from sub class. ---------"""

class Parent:
    def __init__(self):
        self.__private_field = "This is a private field"

    @staticmethod
    def __private_method():
        return "This is a private method"

    def get_private_field(self):
        return self.__private_field

    @staticmethod
    def call_private_method():
        return Parent.__private_method()


class Child(Parent):
    def access_private_field(self):
        return getattr(self, "_Parent__private_field", "Cannot access private field from subclass")

    @staticmethod
    def access_private_method():
        return "Cannot access private method from subclass"


def main():
    parent_obj = Parent()
    print(parent_obj.get_private_field())
    print(Parent.call_private_method())

    child_obj = Child()
    print(child_obj.access_private_field())
    print(Child.access_private_method())


main()

"""---------2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package.  
Also, Access the PROTECTED fields and methods from child class located in a different 
package 
Access the PROTECTED fields and methods from any class in different package ----"""


class Parent:
    def __init__(self):
        self._protected_field = "This is a protected field"

    def _protected_method(self):
        return "This is a protected method"

    def access_protected(self):
        return f"Field: {self._protected_field}, Method: {self._protected_method()}"


class SameModuleClass:
    def access_protected(self):
        parent = Parent()
        return f"Accessing Protected: {parent._protected_field}, {parent._protected_method()}"


class Child(Parent):
    def access_protected(self):
        return f"Accessing Protected from Child: {self._protected_field}, {self._protected_method()}"


class External:
    def access_protected(self):
        parent = Parent()
        try:
            return f"External Access: {parent._protected_field}, {parent._protected_method()}"
        except AttributeError:
            return "Cannot access protected members from an external class"


def main():
    print(SameModuleClass().access_protected())
    print(Child().access_protected())
    print(External().access_protected())


main()


