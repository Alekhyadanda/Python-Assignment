

"""-----------1. Write a function to add integer values of an array------"""
n=int(input("enter array size"))
m=[]
l=0
print("enter numbers")
for i in range(0,n):
    k=int(input())
    l+=k
print(l)

"""-----2. Write a function to calculate the average value of an array of integers-----"""

n=int(input("enter size of an array"))
arr=[]
m=0
l=0
print("enter n numbers")
for i in range(0,n):
    k=int(input())
    m+=k
l=m//n
print(l)

"""-----------3. Write a program to find the index of an array element -----"""

arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to find "))

if x in arr:
    print("Index of", x, "is", arr.index(x))
else:
    print(x, "is not in the array")

"""----------4. Write a function to test if array contains a specific value -------"""

arr = [10, 20, 30, 40, 50]
x = int(input("Enter the element to check "))

if x in arr:
    print(x, "is present in the array")
else:
    print(x, "is not present in the array")

"""-------5. Write a function to remove a specific element from an array ---------"""

def remove_element(arr, element):
    if element in arr:
        arr.remove(element)

arr = [1, 2, 3, 4, 2, 5]
remove_element(arr, 2)
print(arr)

"""-------------6. Write a function to copy an array to another array ----------"""

def copy_array(arr):
    return arr[:]
arr1 = [1, 2, 3, 4, 5]
arr2 = copy_array(arr1)
print(arr2)

"""--------------7. Write a function to insert an element at a specific position in the array ------"""


def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        return "Invalid position"

    arr.insert(position, element)
    return arr


arr = [1, 2, 3, 4, 5]
element = 99
position = 2

print("Original Array:", arr)
arr = insert_element(arr, element, position)
print("Array after insertion:", arr)

"""-----------8. Write a function to find the minimum and maximum value of an array ------"""


def find_min_max(arr):
    if not arr:
        return None, None

    min_val = min(arr)
    max_val = max(arr)

    return min_val, max_val

arr = [3, 1, 9, 7, 2, 8]
min_val, max_val = find_min_max(arr)
print(f"Minimum: {min_val}, Maximum: {max_val}")

"""----------9. Write a function to reverse an array of integer values ---------"""

def reverse_array(arr):
    return arr[::-1]
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(f"Reversed Array: {reversed_arr}")

"""----------------10. Write a function to find the duplicate values of an array ---"""

def find_duplicates(arr):
    duplicates = set()
    seen = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)
arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8]
duplicates = find_duplicates(arr)
print(f"Duplicate values: {duplicates}")

"""-------------11. Write a program to find the common values between two arrays ----------"""

def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

common_values = find_common_values(arr1, arr2)
print(f"Common values: {common_values}")

"""-------------12. Write a method to remove duplicate elements from an array -------"""


def remove_duplicates(arr):
    unique_list = []
    seen = set()

    for num in arr:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)

    return unique_list
arr = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8]
unique_arr = remove_duplicates(arr)
print(f"Array after removing duplicates: {unique_arr}")

"""----------------13. Write a method to find the second largest number in an array -----------"""


def second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two unique numbers"

    unique_numbers = list(set(arr))
    unique_numbers.sort(reverse=True)

    return unique_numbers[1]
arr = [10, 20, 4, 45, 99, 99, 33]
second_largest_num = second_largest(arr)
print(f"Second Largest Number: {second_largest_num}")

"""-----------14. Write a method to find the second largest number in an array ----------"""

def second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two unique numbers"

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num

    return second if second != float('-inf') else "No second largest number"
arr = [10, 20, 4, 45, 99, 99, 33]
second_largest_num = second_largest(arr)
print(f"Second Largest Number: {second_largest_num}")

"""-------------15. Write a method to find number of even number and odd numbers in an array --------"""

def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count

    return even_count, odd_count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(arr)

print(f"Even Numbers: {even_count}, Odd Numbers: {odd_count}")

"""---------------16. Write a function to get the difference of largest and smallest value --------"""

def difference_largest_smallest(arr):
    if not arr:
        return "Array cannot be empty"

    return max(arr) - min(arr)
arr = [10, 2, 8, 4, 99, 15]
difference = difference_largest_smallest(arr)
print(f"Difference between largest and smallest value: {difference}")

"""--------------17. Write a method to verify if the array contains two specified elements(12,23) -----"""

def contains_elements(arr, elem1=12, elem2=23):
    return elem1 in arr and elem2 in arr
arr = [5, 12, 7, 23, 19, 45]
result = contains_elements(arr)

print(f"Array contains both 12 and 23: {result}")

"""----------18. Write a program to remove the duplicate elements and return the new array -------"""

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
arr = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8]
unique_arr = remove_duplicates(arr)

print(f"New array after removing duplicates: {unique_arr}")



















