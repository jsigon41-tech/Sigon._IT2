
# Graph using SIGON

graph = {
    'S': ['I', 'N'],
    'I': ['G', 'S', 'N'],
    'G': ['I', 'O'],
    'O': ['G', 'N'],
    'N': ['I', 'O', 'S']
}

# BFS - Breadth First Search
def BFS(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            print(vertex, end=" ")

            for neighbor in sorted(graph[vertex]):
                if neighbor not in visited:
                    queue.append(neighbor)

# DFS - Depth First Search
def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = []

    visited.append(vertex)
    print(vertex, end=" ")

    for neighbor in sorted(graph[vertex]):
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

print("GRAPH - SIGON")

print("\nBFS Traversal:")
BFS(graph, 'S')

print("\n\nDFS Traversal:")
DFS(graph, 'S')
