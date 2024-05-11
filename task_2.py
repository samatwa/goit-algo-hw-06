import networkx as nx
from task_1 import G

# DFS
dfs_tree = nx.dfs_tree(G, source='A')
print(list(dfs_tree.edges()))  

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))  