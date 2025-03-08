
"""--------PYTHON BASICS---------"""
"""---------1.Write a program to print your name.-------------"""

print("Alekhya")

"""---------2.Write a program for a Single line comment and multi-line comments----------"""""

print("single line comment")
print("multi line comments")

"""-3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console.---"""

x=20
h=True
k="amma"
l=40.98
u=34.324567876543234567
print(x,h,k,l,u,sep="\n")

"""---4.Define the local and Global variables with the same name and print both variables and
understand the scope of the variables---------"""

x=20
def my():
    x=90
    print(x)
print(x)
my()
print(x)

