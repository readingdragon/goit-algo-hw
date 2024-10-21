import networkx as nx
import matplotlib.pyplot as plt

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
    ("Vault_76", "Vault_111"),
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

# аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree}")
