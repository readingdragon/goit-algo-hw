import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

# вершини - підземні бункери-сховища 
nodes = ["Vault_6", "Vault_13", "Vault_33", "Vault_76", "Vault_101", "Vault_111", "Vault_114"]
G.add_nodes_from(nodes)

# Додаємо ребра представленні як шляхи між нашими локаціями
edges = [
    ("Vault_6", "Vault_13"),
    ("Vault_13", "Vault_33"),
    ("Vault_13", "Vault_101"),
    ("Vault_13", "Vault_114"),
    ("Vault_33", "Vault_76"),
    ("Vault_33", "Vault_114"),
    ("Vault_114", "Vault_101"),
    ("Vault_111", "Vault_114"),
    ("Vault_33", "Vault_111"),
]
G.add_edges_from(edges)

# будуєм граф
fig, ax = plt.subplots()

nx.draw(
    G,
    with_labels=True,
    node_color="#0e68ad",
    node_shape="8",
    node_size=2200,
    font_size=9,
    font_color="lightgray",
    edge_color="gold",
)

fig.set_facecolor('#333333')
plt.show()

def dfs(graph, start, road_to):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            if node == road_to:
                return path
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def bfs(graph, start, road_to):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            if node == road_to:
                return path
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

start_vault = "Vault_6"
road_to = "Vault_76"

dfs_path = dfs(G, start_vault, road_to)
bfs_path = bfs(G, start_vault, road_to)

print('-'*40)
print(f"Важкий шлях знайдений DFS: {dfs_path}")
print('-'*40)
print(f"Важкий шлях знайдений BFS: {bfs_path}")
print('-'*40)
   
# аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree}")
