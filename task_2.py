import networkx as nx
from collections import deque
from task_1 import G


# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D', 'F'],
    'D': ['A', 'C', 'E', 'G'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['D', 'F'],
}


# DFS за допогою бібліотеки networkx
dfs_tree = nx.dfs_tree(G, source='A')
print(list(dfs_tree.edges())) 

# Рекурсивна реалізація алгоритму DFS 
def dfs_recursive(graph,vertex,visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex,end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)
    return visited

dfs_recursive(graph,'A')
print()
print()


# BFS за допогою бібліотеки networkx
bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))  

# Ітеративна реалізація алгоритму BFS
def bfs_iterative(graph, start):
    visited =set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(set(graph[vertex])-visited)
    return visited
bfs_iterative(graph,'A')