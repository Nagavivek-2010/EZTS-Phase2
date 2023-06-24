class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None
def Inorder(root):
    current = root
    stack = []
    done = 0
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data,end=" ")
            current = current.right
        else:
            break
    print()
root = Node(1)
root.left = Node(12)
root.right = Node(45)
root.left.left = Node(5)
root.left.right = Node(90)
Inorder(root)