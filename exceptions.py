"""----------EXCEPTIONS----"""
"""----------1. Write a program to generate Arithmetic Exception without exception handling ---------"""

result = 10 / 0
print("Result:", result)

"""------------2. Handle the Arithmetic exception using try-catch block -------"""

try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

"""---------3. Write a method which throws exception, Call that method in main class without try block ----"""

def throw_exception():
    raise ZeroDivisionError("This is an exception")

def main():
    throw_exception()

main()


"""----------3. Write a method which throws exception, Call that method in main class without try block ------"""

def throw_exception():
    raise ArithmeticError("This is an exception")

def main():
    throw_exception()

main()

"""---------4. Write a program with multiple catch blocks -----"""

def handle_exceptions():
    try:
        a = int(input("Enter a number: "))
        re = 10 / a
        print("Result:", re)
        numbers = [1, 2, 3]
        print(numbers[5])
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except IndexError:
        print("Error: List index out of range.")

handle_exceptions()

"""--------------5. Write a program to throw exception with your own message -------"""

def throw_custom_exception():
    raise Exception("This is my custom exception message")

throw_custom_exception()

"""--------6. Write a program to create your own exception ------"""

class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_value(value):
    if value < 0:
        raise MyCustomException("Negative values are not allowed")

check_value(-5)


"""------7. Write a program with finally block ------"""

def divide_numbers(a, b):
    try:
        res= a / b
        print("Result:", res)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution completed.")

divide_numbers(10, 0)


"""--------8. Write a program to generate Arithmetic Exception ------"""

result = 10 / 0
print("Result:", result)


"""--------9. Write a program to generate FileNotFoundException --------"""

file = open("non_existent_file.txt", "r")

"""--------10. Write a program to generate ClassNotFoundException --------"""

class Example:
    pass

try:
    cls = getattr(__import__("builtins"), "NonExistentClass")
except AttributeError:
    print("Error: ClassNotFoundException - Class does not exist")

"""-------11. Write a program to generate IOException --------"""

with open("/invalid/path/to/file.txt", "r") as file:
    content = file.read()

"""-----------12. Write a program to generate NoSuchFieldException ------------"""


class Example:
    def __init__(self):
        self.name = "Python"

obj = Example()

try:
    print(getattr(obj, "age"))
except AttributeError:
    print("Error: NoSuchFieldException - Attribute does not exist")




