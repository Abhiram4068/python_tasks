num=int(input("Enter a number:"))
sum_dig=0
while num!=0:
    temp=num%10
    sum_dig+=temp
    num//=10
print(sum_dig)