def fahrenheit(temp):
    f=(temp*9/5)+32
    print(f)
def celsius(temp):
    c=(temp-32)*5/9
    print(c)
while True:
    temp=int(input("Enter the temperature:"))
    choice=input("f-fahrenheit,c-celsius:").lower()
    if choice=="f":
        fahrenheit(temp)
    elif choice=="c":
        celsius(temp)
    else:
        print("Invalid")
    c=input("Do you want to continue?(y/n)")
    if c!="y":
        break