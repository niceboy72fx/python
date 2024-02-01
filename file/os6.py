import os
absolute_path = os.path.join("/media/darkside72fx/New Volume/Python/python/file/hello","test_absolute.txt")
relative_path = os.path.join("./hello", "test_relative.txt")

with open(absolute_path,'w') as file:
     file.write("absolute_path")
    
with open(relative_path,'w') as file:
     file.write("relative_path")