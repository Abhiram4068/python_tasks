# Check Whether a Number is Prime
def check_prime(num1):
    flag=0
    for i in range(2,num1):
        if num1%i==0:
            flag=1
    if flag==0:
        return "Is prime"
    else:
        return "Not prime"
num1=int(input("Enter a number:"))
print(check_prime(num1))
