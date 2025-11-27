# Python File Detection

import os

file_path = "test.pdf"

if os.path.exists(file_path):
    print(f"The location {file_path} exists" )
else:
    print("That location doesnt exist")

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists" )
else:
    print("That location doesnt exist")

file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists" )
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesnt exist")
