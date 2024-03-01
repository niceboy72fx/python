dict = [{"username" : "hutao7" , "password": "1232456" , "role": "user"},
		{"username" : "hutao8" , "password": "1232456" , "role": "administrator"},
		{"username" : "hutao9" , "password": "1232456", "role": "admin"}]

find_account = lambda username, password: next(({"username": username , "role": item["role"]  , "status" : True  } for item in dict if item["username"] == username and item["password"] == password), {"username": "" , "role": ""  , "status" : False  })

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    find_acc = find_account(username, password)
    if find_acc["status"] != True:
        print("user and pass not match!")
        continue
    else:
        print("login succeed !")
        match find_acc["role"]:
            case "user":
                    print("user login!")
            case "administrator":
                    print("administrator login!")
            case "admin":
                    print("admin login!")
        break


