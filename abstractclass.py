"""------ABSTRACT CLASS------"""
"""--------1. Create an abstract class with abstract and non-abstract methods------------"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    @staticmethod
    def non_abstract_method():
        print("This is a non-abstract method in the abstract class.")


class ConcreteClass(MyAbstractClass):

    def abstract_method(self):
        print("Implemented the abstract method in the concrete class.")


obj = ConcreteClass()
obj.abstract_method()
obj.non_abstract_method()


"""-----------2. Create a sub class for an abstract class. Create an object in the child class for the  
abstract class and access the non-abstract methods---------"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    @staticmethod
    def non_abstract_method():
        print("This is a non-abstract method in the abstract class.")


class ChildClass(MyAbstractClass):

    def abstract_method(self):
        print("Implemented the abstract method in the child class.")

    def access_non_abstract_method(self):
        self.non_abstract_method()


obj = ChildClass()
obj.abstract_method()
obj.access_non_abstract_method()


"""---------3. Create an instance for the child class in child class and call abstract methods ------------"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    @staticmethod
    def non_abstract_method():
        print("This is a non-abstract method in the abstract class.")


class ChildClass(MyAbstractClass):

    def abstract_method(self):
        print("Implemented the abstract method in the child class.")

    @staticmethod
    def call_abstract_method_in_child():
        child_instance = ChildClass()
        child_instance.abstract_method()


ChildClass.call_abstract_method_in_child()

"""-----------4. Create an instance for the child class in child class and call non-abstract methods-----------"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    @staticmethod
    def non_abstract_method():
        print("This is a non-abstract method in the abstract class.")


class ChildClass(MyAbstractClass):

    def abstract_method(self):
        print("Implemented the abstract method in the child class.")

    @staticmethod
    def call_non_abstract_method_in_child():
        child_instance = ChildClass()
        child_instance.non_abstract_method()


ChildClass.call_non_abstract_method_in_child()
