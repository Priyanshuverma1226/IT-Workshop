# Write code that repeatedly prompts the user for input, and then outputs the number of items that the user entered the input before the user entered "pumpkin spice latte" (with any capitalization) For example, an interaction with the user might look like What is your order? (User input:) Pumpkin pie What is your order? (User input:) Candy What is your order? (User input:) pumPkin Spice latte 2 The number 2 is printed because the user ordered two items before ordering a pumpkin spice latte.


def create_stack():
    l=[]
    return l


def push(s,value):
    s.append(value)
    print("Push is DOne")

def pop(s):
    s.pop()
    print("Remove is Done")


def display(s):
    for i in s:
        print(i)


if __name__ == '__main__':
    stack = create_stack()   



    while True:
        choice=int(input("Press 1 key to Place Order \nPress 2 key to Remove order\nPress 3 key to Display order \n"))
        match choice:
            case 1:
                push(stack,str(input("What is your order?:")))
            case 2:
                pop(stack)
            case 3:
                display(stack)
            case other:
                print("Invalid Choices")



