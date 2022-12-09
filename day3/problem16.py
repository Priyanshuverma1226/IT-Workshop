# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    o=0
    e=0
    for i in range(1, num+1):
        if i%2==0:
            e+=1
        elif i%2!=0:
            o+=1

            
    print(f"Odd numbers {o}")
    print(f"Even numbers {e}")

evens_and_odds(10)
