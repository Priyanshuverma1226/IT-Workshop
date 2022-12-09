# Write a function with the signature match_pattern(list1, list2) which returns True iff the pattern list2 appears in list1. In other words, we return True iff there is an i such that 0 ≤ i ≤ len(list1)-len(list2) and list1[i] = list2[0] list1[i + 1] =list2[1] . . . list1[i + len(list2)- 1] = list2[-1] For example, if list1 is [4, 10, 2, 3, 50, 100]andlist2is[2, 3, 50], match_pattern(list1, list2) returns True since the pattern [2, 3, 50] appears in list1

def match_pattern(list1, list):
    for i in  list1:
        for j in list2:
            if i == j:
                print(i)
                

list1=[1,2,3]
list2=[3,4,2]
match_pattern(list1, list2)
