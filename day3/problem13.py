# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(numbers):
    a=0
    for i in range(1,numbers+1):
        a+= i
    return a
print(sum_of_numbers(10))