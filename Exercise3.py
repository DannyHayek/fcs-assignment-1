username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "admin":
    if password == "1234":
        print("Access granted!")
    else:
        print("Access denied!")
else:
    print("Access denied!")