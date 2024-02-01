import os

path = os.path.join("./hello","test.txt")
with open(path,'w') as file:
     file.write("hola")