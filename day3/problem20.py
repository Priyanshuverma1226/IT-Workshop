# Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:    
            return False
    return True
    
print(is_prime(7))