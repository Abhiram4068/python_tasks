def product_list(items):
    pr_elements=1
    for item in items:
        pr_elements*=item
    return pr_elements
items=[12,52,6,8,-1,1,2,78,36]
print(f"{product_list(items)} is the product of the elements in the list")
