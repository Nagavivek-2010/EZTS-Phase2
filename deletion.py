class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def deletebegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deletelast(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
            prev.next=None
    def position(self,pos):
        temp=self.head.next
        prev=self.head        
        for i in range(1,pos-1):
             temp=temp.next
             prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        while temp:
            print(temp.data,'-->',end=" ")
            temp=temp.next
            
            
    def search(self):
        temp=self.head
obj=LinkedList()
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