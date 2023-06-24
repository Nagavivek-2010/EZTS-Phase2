class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head = None
        self.last=None
        
    def Enqueue(self,data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last. next
             
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
a_queue = Queue()
             
while 1:
    print('Enqueue <value>')
    print('Dequeue')
    print('quit')
    do = input('what would you like to do?' ).spilt()
    print("do",do)
    print("do[0]",do[0])
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation =='pop':
        dequeue=a_queue.dequeue()
        if popped is None:
            print("Queue is Empty")
        else:
            print("Dequeue value:", int(popped))
    elif operation == 'quit':
        break
    
        
    
