#check palindrome
def check_pal(num1):
    temp2=num1
    rev=0
    while num1!=0:
        temp=num1%10
        rev=rev*10+temp
        num1//=10
    if rev==temp2:
        return "Is palindrome"
    else:
        return "Not palindrome"
num1=int(input("Enter a number:"))
print(check_pal(num1))