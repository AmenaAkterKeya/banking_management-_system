from user_id import User_id
from admin_id import admin_id

while True:
    print(f"**** Welcome ****")
    print("1.sing in User")
    print("2.sign in Admin")
    print("3.Exit")
    option = int(input("Enter the option: "))

    if option == 1:
        User_id()
    elif option == 2:
        admin_id()
    elif option == 3:
        break
    else:
        print("Invalid option")



