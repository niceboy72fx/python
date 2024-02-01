file_path = "test.txt"


with open(file_path, "r+") as file:
    content = file.read()
    update2 = content + "updated"
    file.write(update2)