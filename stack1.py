stack=[]
def push():
    element=int(input("Enter the elements that you want insert:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("Removed Element:",e)
        print(stack)
def display():
    print(stack)
def top():
    if not stack:
        print("stack is empty please insert")
    else:
        element=int(input("Enter the elements that you want insert:"))
        stack.append(element)
        print(stack)    
while 1:
    print("Select the operations that you want perform on stack \n 1.push \n 2.pop \n 3.display \n 4.quit \n 5.TOP:")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
         display()
    elif choice==4:
        break
    elif choice==5:
        top()
    else :
        print("Enter the correct operations")
         