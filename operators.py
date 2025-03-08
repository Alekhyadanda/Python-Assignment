"""OPERATORS"""
"""---------1.Write a function for arithmetic operators(+,-,*,/)------"""

a=input("enter a number")
b=input("enter a number")
sumk=float(a)+float(b)
mini =float(a)-float(b)
multi=float(a)*float(b)
div=float(a)/float(b)
print('{0} and {1} is {2}'.format(a,b,sumk))
print('{0} and {1} is {2}'.format(a,b,mini))
print('{0} and {1} is {2}'.format(a,b,multi))
print('{0} and {1} is {2}'.format(a,b,div))

"""--------2.Write a method for increment and decrement operators(++, --)--------"""

a=0
b=10
while a<=5:
    print(a)
    a+=1
while b>=5:
    print(b)
    b-=1

"""---------3.Write a program to find the two numbers equal or not.-----------"""

a=int(input("enter a number"))
b=int(input("enter a number"))
if a==b:
    print("they are equal")
else:
    print("they are not equal")

"""-----------4.Program for relational operators (<,<==, >, >==)-------------"""

a=int(input("enter a number"))
b=int(input("enter a number"))
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

"""-------------5.Print the smaller and larger number-----------"""

a=int(input("enter a number"))
b=int(input("enter a number"))
if a>b:
    print('larger number is:',a)
else:
    print('larger number is:',b)
if a>b:
    print('smaller number is:',b)
else:
    print('smaller number is:',a)
