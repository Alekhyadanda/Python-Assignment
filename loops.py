"""-----LOOPS---------"""
"""--------1.Write a program to print  “Bright IT Career”  ten times using for loop-------"""

a = "Bright IT Career"
for i in range(0, 10):
    print(a)
"""------2.Write a java program to print 1 to 20 numbers using the while loop.---------"""

a = 1
while a <= 20:
    print(a)
    a += 1
"""--------3.Program to equal operator and not equal operators-------"""
a = int(input("enter a number"))
b = int(input("enter a number"))
print(a == b)
print(a != b)

"""-------4.Write a program to print the odd and even numbers.---------"""
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in b:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

"""--------5. Write a program to print largest number among three numbers.------"""

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

"""------6.Write a  program to print even number between 10 and 20 using while--------"""
a = 10
while a <= 19:
    a += 1
    print(a)

"""------------7.Write a program to print 1 to 10 using the do-while loop statement.-------"""

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

"""----------8. Write a program to find Armstrong number or not -----"""

n = int(input())
temp = n
p = len(str(n))
s = 0

while temp > 0:
    d = temp % 10
    s += d ** p
    temp //= 10

if n == s:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number")

"""----9. Write a program to find the prime or not.----"""

n=int(input("enter a number"))
count=0
for i in range(2,n):
    if n%i!=0:
        count+=1
if count==0:
    print("prime number")
else:
    print("Not Prime Number")

"""------10. Write a program to palindrome or not. -------"""

n = int(input())
temp = n
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10

if n == rev:
    print(n, "is a Palindrome number")
else:
    print(n, "is not a Palindrome number")



"""----11. Program to check whether a number is EVEN or ODD using switch----"""

value=int(input("enter a number"))
if value%2==0:
    num=0
else:
    num=1
match num:
    case 0:
        print("Even")
    case 1:
        print("Odd")


"""-------12.Print gender (Male/Female) program according to given M/F using switch-----"""

value=input("enter M/F only")
match value:
    case 'M':
        print("male")
    case 'F':
        print("Female")
    case _:
        print("out of category")








