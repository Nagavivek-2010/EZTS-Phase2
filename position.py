class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist__:
    def __init__(self):
        self.head=None
        
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):#1iteration 1 happen
            temp=temp.next
            
        np.next=temp.next
        temp.next=np
        def display(self):
             while temp:
                 print(temp.data,'-->',end=" ")
                 temp=temp.next
obj=singlelinkedlist()
n= Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.insert_position(3,1000)
obj.display()