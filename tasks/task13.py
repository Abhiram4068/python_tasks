li=[2,5,66,8,1,2,5,6,7,10,11]
odd_li=[]
even_li=[]
for items in li:
    if items%2==0:
        even_li.append(items)
    else:
        odd_li.append(items)
print(f"Odd List:{odd_li}")
print(f"Even List:{even_li}")