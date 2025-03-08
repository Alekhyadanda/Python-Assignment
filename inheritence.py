"""---------------A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members---------"""


class A:
    var = "Class A Variable"

    @staticmethod
    def method1():
        print("Method1 of class A")

    @staticmethod
    def method2():
        print("Method2 of class A")

    def override_method(self):
        print("Overridden method in class A")


class B(A):
    var = "Class B Variable"

    @staticmethod
    def method3():
        print("Method3 of class B")

    @staticmethod
    def method4():
        print("Method4 of class B")

    def override_method(self):
        print("Overridden method in class B")


class C(B):
    var = "Class C Variable"

    @staticmethod
    def method5():
        print("Method5 of class C")

    @staticmethod
    def method6():
        print("Method6 of class C")

    def override_method(self):
        print("Overridden method in class C")


class Main:
    @staticmethod
    def main():
        obj_a = A()
        obj_b = B()
        obj_c = C()

        A.method1()
        A.method2()
        obj_a.override_method()

        B.method1()
        B.method2()
        B.method3()
        B.method4()
        obj_b.override_method()

        C.method1()
        C.method2()
        C.method3()
        C.method4()
        C.method5()
        C.method6()
        obj_c.override_method()

        ref_a = obj_b
        ref_a.override_method()

        ref_a = obj_c
        ref_a.override_method()

        obj_a = A()
        obj_b = B()
        obj_c = C()

        print(obj_a.var)
        print(obj_b.var)
        print(obj_c.var)

        ref_a = obj_b
        print(ref_a.var)

        ref_a = obj_c
        print(ref_a.var)


Main.main()
