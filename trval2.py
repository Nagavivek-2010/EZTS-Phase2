class Node:
    def __init__(self,Key):
        self.left = None
        self.left =None
        self.right = None
def insert(root,Key):
    if root is None:
        return Node(Key)
    else:
        if root.val == Key:
            return root
        elif root.val < Key:
            root.right = insert(root.right,Key)
        else:
            root.left = insert(root.left,Key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r = Node(50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)
inorder(r)
        