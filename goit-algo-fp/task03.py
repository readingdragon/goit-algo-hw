# Завдання 3. Дерева, алгоритм Дейкстри

import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(dict)

    def add_node(self, value):
        self.edges.setdefault(value, {})

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  # для неорієнтованого графа


def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float("infinity") for node in graph.edges}
    distances[start] = 0
    shortest_path = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                shortest_path[neighbor] = current_node

    return distances, shortest_path

# cтворення графа та додавання вузлів та ребер
graph = Graph()
nodes = ["A", "B", "C", "D", "E"]
for node in nodes:
    graph.add_node(node)

edges = [
    ("A", "B", 5), ("A", "C", 9), ("B", "C", 6), 
    ("B", "D", 1), ("C", "D", 8), ("C", "E", 6), ("D", "E", 11)
]

for from_node, to_node, weight in edges:
    graph.add_edge(from_node, to_node, weight)

# алгоритм Дейкстри
start_node = "A"
distances, paths = dijkstra(graph, start_node)

# результати
print(f"Distances from {start_node}: {distances}")
print(f"Shortest paths form {start_node}:", paths)
