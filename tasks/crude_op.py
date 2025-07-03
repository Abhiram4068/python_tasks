user_details={}
while True:
    user_choice=int(input("Enter your choice:1-ADD,2-UPDATE,3-DELETE,4-VIEW,5-LOGIN:"))
    if user_choice==1:
        user_details["name"]=input("Enter your name:")
        user_details["age"] = int(input("Enter your age:"))
        user_details["username"] = input("Enter your Username:")
        user_details["password"] = input("Enter your password:")
    elif user_choice==2:
        update_choice = int(input("Enter your choice:1-NAME,2-AGE,3-USERNAME,4-PASSWORD"))
        if update_choice==1:
            user_details["name"] = input("Enter your new name:")
            print("Name Updated!!!")
        elif update_choice==2:
            user_details["age"] = input("Enter your new age:")
            print("Age Updated!!!")
        elif update_choice==3:
            user_details["username"] = input("Enter your new username:")
            print("Username Updated!!!")
        elif update_choice==4:
            user_details["password"] = input("Enter your new password:")
            print("Password Updated!!!")
    elif user_choice==3:
        user_details.clear()
        print("Deleted!!!")
    elif user_choice==4:
        print("Your Details:")
        print(user_details)
    elif user_choice==5:
        uname=input("Enter the username:")
        wd=input("Enter the password")
        if uname==user_details["username"] and wd==user_details["password"]:
            print("Login Successful")
        else:
            print("Invalid username or password")
    else:
        print("Enter a valid input")
    cont_choice=input("Do you want to continue?(yes/no)").lower()
    if cont_choice!="yes":
        print("Exiting...")
        break