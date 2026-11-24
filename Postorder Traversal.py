
# Postorder Traversal using JOHN SIGON

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


# Postorder Traversal
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Display Result
print("Name: JOHN SIGON")
print("Postorder Traversal (Left - Right - Root):")
postorder(root)
