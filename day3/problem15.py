# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.



def sum_of_even(num):
    a=0
    for i in range(0, num+1):
        if i%2==0:
            a+=i
    return a

print(sum_of_even(5))