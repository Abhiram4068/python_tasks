#Validate Integer Input and Raise ValueError
n=input("Enter an integer:")
try:
    value=int(n)
    print(value)
except ValueError:
    print("Enter integer only")
