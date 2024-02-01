import os

if os.path.exists("./hello"):
    try:
        with open("./hello/test.txt",'r') as file:
            print(file.read())
    except Exception as e :
        print("couldn't open file")
else:
    print("File does not exist.")