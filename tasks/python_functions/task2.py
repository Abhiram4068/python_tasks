def sum_list(items):
    sum_elements=0
    for item in items:
        sum_elements+=item
    return sum_elements
items=[12,52,6,8,0,1,2,78,36]
print(f"{sum_list(items)} is the sum of the elements in the list")
