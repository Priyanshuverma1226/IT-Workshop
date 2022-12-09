# Write a function with the signature list1_start_with_list2(list1, list2), which returns True iff list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2. Note: len(lis) is the length of the list lis, i.e., the number of elements in lis. First write the function without using slicing (“slicing” means saying things like list1[2:5]), and using a loop.


def list1_start_with_list2(list1, list2):
    for i in range(len(list2)):
        if list1[i] == list2[i]:
            return True
    return False
list1=[23,25,65,85,85]
list2=[45,25,75,96,74]

a=list1_start_with_list2(list1, list2)
print(a)

def slice(s,start,end):
    
    for i in range(start,end):
        print(s[i],end='')
slice("Priyanshu",2,5)

