# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))