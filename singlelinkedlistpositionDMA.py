class Node:
    def __init_(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end =' ')
            current = current.next
a_list = LinkedList()
n = int(input('how many elements would you like to inset:'))
for i in range(n):
    data = int(input('Enter data item:'))
    a_list.append(data)
 
print('The Linked List:',end ='  ')
a_list.display()


    