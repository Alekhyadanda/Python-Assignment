"""--------1. Write two methods with the same name but different number of parameters of same type and call the methods -------------"""

class Example:
    @staticmethod
    def display(*args):
        if len(args) == 1:
            print(f"Method with one parameter: {args[0]}")
        elif len(args) == 2:
            print(f"Method with two parameters: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

Example.display(10)
Example.display(10, 20)
Example.display(10, 20, 30)


"""-----------2. Write two methods with the same name but different number of parameters of different 
data type and call the methods  ---------"""

class Example:
    @staticmethod
    def display(*args):
        if len(args) == 1:
            if isinstance(args[0], int):
                print(f"Method with one integer parameter: {args[0]}")
            elif isinstance(args[0], str):
                print(f"Method with one string parameter: {args[0]}")
            else:
                print("Invalid argument type")
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], str):
                print(f"Method with an integer and a string parameter: {args[0]}, {args[1]}")
            else:
                print("Invalid argument types")
        else:
            print("Invalid number of arguments")

Example.display(10)
Example.display("Hello")
Example.display(10, "World")


"""---------3. Write two methods with the same name and same number of parameters of same type ---------"""

class Example:
    @staticmethod
    def display(arg1):
        if isinstance(arg1, int):
            print(f"Method with integer parameter: {arg1}")
        elif isinstance(arg1, str):
            print(f"Method with string parameter: {arg1}")
        elif isinstance(arg1, bool):
            print(f"Method with boolean parameter: {arg1}")
        else:
            print("Invalid argument type")

Example.display(10)
Example.display("Hello")   
Example.display(True)
