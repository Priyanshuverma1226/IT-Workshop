# Write a function that, when called, returns the next digit of π (approx 3.14159...). You may assume that the function will not be called more than 10 times. The function would be used like this: print(next_digit_pi()) # 3 print(next_digit_pi()) # 1 print(next_digit_pi()) # 4 print(next_digit_pi()) # 1 You may import math and use math.pi

import math



def next_digit_pi(n):
    return round(math.pi, n)

print(next_digit_pi(int(input('Number of digits :- '))))