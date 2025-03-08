"""----------STATIC-----------"""
"""----------1. Define a static variable and access that through a class  ---"""

class MyClass:
    static_var = "I am a static variable"

    @classmethod
    def access_static(cls):
        return cls.static_var

print(MyClass.static_var)
print(MyClass.access_static())

obj = MyClass()
print(obj.static_var)

"""-------------2. Define a static variable and access that through a instance ---------"""

class MyClass:
    static_var = "I am a static variable"

    def access_static(self):
        return self.static_var

obj = MyClass()
print(obj.static_var)
print(obj.access_static())


"""---------3. Define a static variable and change within the instance --------"""

class MyClass:
    static_var = "I am a static variable"

    def change_static(self, new_value):
        self.static_var = new_value

obj = MyClass()
obj.change_static("Changed inside instance")

print(obj.static_var)
print(MyClass.static_var)


"""-------4. Define a static variable and change within the class -----------"""

class MyClass:
    static_var = "I am a static variable"

    @classmethod
    def change_static(cls, new_value):
        cls.static_var = new_value

MyClass.change_static("Changed inside class")

print(MyClass.static_var)

obj = MyClass()
print(obj.static_var)


