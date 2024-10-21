import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

# вершини - підземні бункери-сховища 
nodes = ["Vault_6", "Vault_13", "Vault_33", "Vault_76", "Vault_101", "Vault_111", "Vault_114"]
G.add_nodes_from(nodes)

# Додаємо ребра представленні як шляхи між нашими локаціями
edges = [
    ("Vault_6", "Vault_13", 15),
    ("Vault_13", "Vault_33", 69),
    ("Vault_13", "Vault_101", 23),
    ("Vault_13", "Vault_114", 15),
    ("Vault_33", "Vault_76", 76),
    ("Vault_33", "Vault_114", 11),
    ("Vault_114", "Vault_101", 219),
    ("Vault_111", "Vault_114", 51),
    ("Vault_33", "Vault_111", 6),
]
G.add_weighted_edges_from(edges)

def dijkstra(graph, start_vault):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vault] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight.get('weight')

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

print('-'*40)
start_vault = "Vault_6"

shortest_paths = dijkstra(G, start_vault)

print(f"Найкоротший шлях від {start_vault} ")
for vault, distance in shortest_paths.items():
    print(f"до {vault}: {distance} кілометрів.")

# будуєм граф
fig, ax = plt.subplots()
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="#0e68ad",
    node_shape="8",
    node_size=2200,
    font_size=9,
    font_color="lightgray",
    edge_color="gold",
)

fig.set_facecolor('#333333')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size='8', font_color="y", bbox=dict(facecolor="#333333", edgecolor="yellow", boxstyle="round,pad=0.5", linewidth=0.2))
plt.show()