try:
    file = open("test.txt",'w')
    content = file.write("jdsjdj")
    print(content)
    
    file2 = open("test2.txt", 'w')
    content2 = file2.write("holaa2s")
    print(content2)
except FileNotFoundError:
    print(f"The file  does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
