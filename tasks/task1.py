while True:
    num1=int(input('enter a number:'))
    num2=int(input('enter another number:'))
    choice=int(input('1-ADD,2-SUBTRACT,3-MULTIPLY,4-DIVIDE,5-Exit:'))
    if choice==1:
        print(f"SUM:{num1+num2}")
    elif choice==2:
        print(f"DIFFERENCE:{num1-num2}")
    elif choice==3:
        print(f"PRODUCT:{num1*num2}")
    elif choice==4:
        print(f"QUOTIENT:{num1//num2}")
    elif choice==5:
        print('Exiting...')
        break
    else:
        print('invalid input')
    choice2=input("Do you want to continue?(yes/no)").lower()
    if choice2!="yes":
        print('Exiting...')
        break