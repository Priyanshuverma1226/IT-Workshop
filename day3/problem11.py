# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.


def add_item(list, item):
    list.append(item)
    return list
l=[]
add_item(l,52)
add_item(l,32)
add_item(l,25)

print(l)