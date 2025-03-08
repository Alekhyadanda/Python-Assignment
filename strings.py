"""-----------STRINGS--------"""

"""-----------1. Different ways creating a string -----------"""
str1 = 'Hello'
str2 = "Hello"
str3 = '''Hello'''
str4 = """Hello"""
str5 = str(123)
str6 = ''.join(['H', 'e', 'l', 'l', 'o'])
str7 = "{}".format("Hello")
str8 = f"{'Hello'}"
str9 = bytes("Hello", "utf-8").decode("utf-8")

print(str1, str2, str3, str4, str5, str6, str7, str8, str9)

"""----------2. Concatenating two strings using + operator ----------"""

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

"""----------3. Finding the length of the string -------"""

str1 = "Hello, World!"
length = len(str1)
print(length)

"""-------4. Extract a string using Substring --------"""

str1 = "Hello, World!"
substring = str1[7:12]
print(substring)

"""-----5. Searching in strings using index() -------"""

str1 = "Hello, World!"
index = str1.index("World")
print(index)

"""-----------6. Matching a String Against a Regular Expression With matches() --------"""

import re

pattern = r"\d{3}-\d{2}-\d{4}"
string = "My SSN is 123-45-6789"
match = re.match(pattern, string)

print(match is not None)


"""--------7. Comparing strings  ---------"""

str1 = "apple"
str2 = "banana"

print(str1 == str2)
print(str1 != str2)
print(str1 < str2)
print(str1 > str2)


"""----------8. startsWith(), endsWith() and compareTo() ----------"""

str1 = "Hello, World!"

print(str1.startswith("Hello"))
print(str1.endswith("World!"))
print((str1 > "Apple") - (str1 < "Apple"))


"""---------9. Trimming strings with strip() -------"""

str1 = "   Hello, World!   "
trimmed_str = str1.strip()
print(trimmed_str)

"""--------10. Replacing characters in strings with replace() --------"""

str1 = "Hello, World!"
new_str = str1.replace("World", "Python")
print(new_str)

"""---------11. Splitting strings with split() ----------"""

str1 = "apple,banana,cherry"
split_str = str1.split(",")
print(split_str)


"""----------12. Converting integer objects to Strings --------"""

num = 123
str_num = str(num)
print(str_num)


"""----------13. Converting to uppercase and lowercase --------"""

str1 = "Hello, World!"
uppercase_str = str1.upper()
lowercase_str = str1.lower()

print(uppercase_str)
print(lowercase_str)
