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
        choice=int(input("Press 1 key to PUSH \nPress 2 key to POP\nPress 3 key to Display \n"))
        match choice:
            case 1:
                push(stack,int(input("Enter the element to be pushed:")))
            case 2:
                pop(stack)
            case 3:
                display(stack)
            case other:
                print("Invalid Choices")
