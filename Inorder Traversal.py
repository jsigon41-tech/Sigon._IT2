
# Inorder Traversal using JOHN SIGON

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree using JOHN SIGON
root = Node("J")
root.left = Node("O")
root.right = Node("H")

root.left.left = Node("N")
root.left.right = Node("S")

root.right.left = Node("I")
root.right.right = Node("G")

root.left.left.left = Node("O")
root.left.left.right = Node("N")


# Inorder Traversal
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Display Result
print("Name: JOHN SIGON")
print("Inorder Traversal (Left - Root - Right):")
inorder(root)

