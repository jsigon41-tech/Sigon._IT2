
# Preorder Traversal using JOHN SIGON

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


# Preorder Traversal
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Display Result
print("Name: JOHN SIGON")
print("Preorder Traversal (Root - Left - Right):")
preorder(root)
