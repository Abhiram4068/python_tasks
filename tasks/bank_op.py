import re
bank_data={}
while True:
    user_choice = int(input("Enter your choice:1-ADD ACCOUNT,2-LOGIN,3-EXIT:"))
    if user_choice==1:
        bank_data["name"]=input("Enter your name:")
        while True:
            u_name=input("Enter your username:")
            pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
            if re.fullmatch(pattern,u_name):
                bank_data["username"]=u_name
                break
            else:
                print("Invalid username...Enter again")
        bank_data["password"]=input("Enter your password:")
        bank_data["balance"] = 0
        print("Account created.")
    elif user_choice==2:
        uname=input("Enter the username:")
        paword=input("Enter the password:")
        if uname==bank_data["username"] and paword==bank_data["password"]:
            print("Login Successful")
            while True:
                user_choice=int(input("Enter your choice:1-DEPOSIT,2-CHECK BALANCE,3-WITHDRAW,4-LOGOUT:"))
                if user_choice == 1:
                    bank_data["balance"] += int(input("Enter the amount to be deposited:"))
                    print("Amount deposited!!!")
                elif user_choice == 2:
                    print(f"Your balance:{bank_data['balance']}")
                elif user_choice == 3:
                    with_amount = int(input("Enter the amount to be withdrawn:"))
                    if with_amount < 500:
                        print("Withdraw amount should be greater than 500.")
                    elif with_amount>bank_data["balance"] :
                        print("Your account doesnt have that much amount")
                    else:
                        bank_data['balance'] -= with_amount
                        print(f"New Balance:{bank_data['balance']}")
                elif user_choice == 4:
                    print("Logged out successfully...")
                    break
                exit_choice=input("Do you want to LOGOUT?(y/n)")
                if exit_choice!="n":
                    break
        else:
            print("Invalid username or password")
    elif user_choice==3:
        print("Exiting...")
        break