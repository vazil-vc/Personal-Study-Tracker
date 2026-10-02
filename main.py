from register import registration
from login import login
from subject import Subject
from menu import menu
import json
try:
    file = open("users.json", "r")
    users = json.load(file)
    file.close()
except FileNotFoundError:
    users = []
while True:
    try:
        choice=int(input("1. register\n2. login\n3. exit\nenter the your choice:"))
    except ValueError:
        print("enter a number")
        continue
    if choice==1:
        reg=registration()
        users.append(reg)
        file = open("users.json", "w")
        json.dump(users, file)
        file.close()
        print("registered")
    elif choice==2:
        if login(users):
            print("login successfully")
            menu()
        else:
            print("wrong user name or password")
    elif choice==3:
        print("thank you")
        break
    else: 
        print("wrong choice")    