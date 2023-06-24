queue=[]
def enqueue():
    element=input("Enter Element:")
    queue.append(element)
    print(element,"is added in queue")
def dequeue():
    if not queue:
        print("Q is empty")    
    else:
        e=queue.pop(0)
        print("Removed element:",e)
def display():
    print(queue)
while 1:
    print("Select the operations that you want perform on stack \n 1.enqueue \n 2.remove \n 3.display \n 4.quit :")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else :
        print("Enter the correct operations")
             