# Return a New List with Distinct Elements from a List
def rep_el(li):
    li2=[]
    for l in li:
        if l not in li2:
            li2.append(l)
    return li2
li=[1,2,2,5,6,4,4,6,1,9,8,7,5,22,44]
print(rep_el(li))