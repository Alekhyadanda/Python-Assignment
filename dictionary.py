"""----------------DICTIONARY-------"""

"""---------1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name 
1.1. Adding the values in dictionary 
1.2. Updating the values in dictionary 
1.3. Accessing the value in dictionary 
1.4. Create a nested loop dictionary 
1.5. Access the values of nested loop diction------"""

students = dict([(101, "Alice"), (102, "Bob"), (103, "Charlie"), (104, "David"), (105, "Emma")])

students[106] = "Frank"
students[107] = "Grace"

print("Dictionary after adding values:", students)

students[102] = "Brian"
print("Dictionary after updating Bob to Brian:", students)

print("Accessing Student ID 103:", students[103])

nested_students = dict(
    [
        (201, {"name": "John", "age": 20, "grade": "A"}),
        (202, {"name": "Lisa", "age": 21, "grade": "B"}),
        (203, {"name": "Mark", "age": 22, "grade": "A+"}),
    ]
)

print("Nested Dictionary:",  nested_students)

print("Accessing John's details:", nested_students[201])
print("Accessing John's grade:", nested_students[201]["grade"])






