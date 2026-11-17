
# Binary Tree using SIGON

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create Binary Tree
root = Node("S")
root.left = Node("I")
root.right = Node("G")
root.left.left = Node("O")
root.left.right = Node("N")

# BFS - Level Order Traversal
def BFS(root):
    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# DFS - Preorder Traversal
def DFS(root):
    if root:
        print(root.value, end=" ")
        DFS(root.left)
        DFS(root.right)

print("BINARY TREE - SIGON")

print("\nBFS Traversal:")
BFS(root)

print("\n\nDFS Traversal:")
DFS(root)
