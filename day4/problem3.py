# Write a function with the signature duplicates(list0), which returns True iff list0 contains at least two adjacent elements with the same value.


def duplicates(list1, list):
    k=0
    for i in  list1:
        for j in list2:
            if k==2:
                return True
            if i == j:
                k=k+1
    return False

list1=[1,2,3]
list2=[6,4,8]
print(duplicates(list1, list2))
