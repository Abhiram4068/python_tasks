def find_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("Enter a number:"))
print(f"Factorial:{find_fact(n)}")