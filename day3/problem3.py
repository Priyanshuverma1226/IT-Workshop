# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    a=0 
    for  value in args:
        a+=value
        
    return a
print(add_all_nums(2,2,2,2,2))
