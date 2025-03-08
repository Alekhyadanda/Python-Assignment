"""----------1. Write a program to read text file---------"""

with open('sample.txt', 'r') as file:
    content = file.read()

    print(content)

"""--------2. Write a program to write text to .txt file using  InputStream------------ """

with open('output.txt', 'w') as file:
    text = input("Enter the text to write to the file: ")
    file.write(text)
    print("Text has been written to the file successfully.")


"""-----------3. Write a program to read a file stream------------"""

with open('sample.txt', 'r') as file:
    for line in file:
        print(line, end='')


"""----------4. Write a program to read a file stream supports random access --------------"""

with open('sample.txt', 'r') as file:
    file.seek(10)
    content = file.read(20)
    print("Content read from position 10:", content)

    file.seek(0)
    content = file.read(10)
    print("Content read from position 0:", content)


"""--------5. Write a program to read a file a just to a particular index using seek() ------------"""

with open('sample.txt', 'r') as file:
    file.seek(15)
    content = file.read(10)
    print("Content from position 15:", content)


"""------------6. Write a program to check whether a file is having read access and write access permissions -----------"""

import os

file_path = 'sample.txt'

if os.access(file_path, os.R_OK):
    print(f"The file {file_path} has read access.")
else:
    print(f"The file {file_path} does not have read access.")

if os.access(file_path, os.W_OK):
    print(f"The file {file_path} has write access.")
else:
    print(f"The file {file_path} does not have write access.")

