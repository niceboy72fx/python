import os

absolute_path = "/media/darkside72fx/New Volume/Python/python/file/hello"
relative_path = "./hello"
print(os.path.isabs(absolute_path))
print(os.path.isabs(relative_path))