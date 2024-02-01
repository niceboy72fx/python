
file = open('test.txt', 'r')

try:
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print(f"The file  does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

