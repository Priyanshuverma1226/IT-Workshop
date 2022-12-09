# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(l):
    for i in range(len(l)-1, 0, -1):
        l[i], l[i-1] = l[i-1], l[i]
    return l

print(reverse_list([2,3,5]))