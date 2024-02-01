import os

if os.path.exists("./hello"):
    with open("./hello/test.txt",'r') as file:
     print(file.read())
else:
    print("File does not exist.")