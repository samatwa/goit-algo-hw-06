graph = {
    'A': {'B':5, 'D':9},
    'B': {'A':5, 'C':7, 'E':8},
    'C': {'B':7, 'D':3, 'F':5},
    'D': {'A':9, 'C':3, 'E':6, 'G':7},
    'E': {'B':8, 'D':6, 'F':4},
    'F': {'C':5, 'E':4, 'G':5},
    'G': {'D':7, 'F':5},
}

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)

    return distances

print(dijkstra(graph, 'A'))