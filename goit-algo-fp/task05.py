# Завдання 5. Візуалізація обходу бінарного дерева

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#ADD8E6"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    fig, ax = plt.subplots()

    nx.draw(
        tree,
        with_labels=True,
        node_color=colors,
        node_shape="8",
        node_size=2200,
        font_size=9,
        font_color="black",
        edge_color="gold",
        pos=pos,
        labels=labels,
        arrows=False,
    )

    fig.set_facecolor('#333333')
    plt.show()

def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = build_heap_tree(heap, left_index) if left_index < len(heap) else None
    node.right = build_heap_tree(heap, right_index) if right_index < len(heap) else None
    return node

def generate_color_gradient(start_color, steps):
    start_rgb = [int(start_color[i:i+2], 16) for i in (1, 3, 5)]
    color_gradient = []
    for step in range(steps):
        new_rgb = [min(255, int(start_rgb[i] + (255 - start_rgb[i]) * step / (steps - 1))) for i in range(3)]
        color_gradient.append(f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}")
    return color_gradient

def bfs_traversal(tree_root):
    queue = deque([tree_root])
    visited = []
    colors = generate_color_gradient("#ADD8E6", 8)

    step = 0
    while queue:
        node = queue.popleft()
        node.color = colors[min(step, len(colors) - 1)]
        visited.append(node.val)
        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    draw_tree(tree_root)

    return visited

def dfs_traversal(tree_root):
    stack = [tree_root]
    visited = []
    colors = generate_color_gradient("#FFD700", 8)

    step = 0
    while stack:
        node = stack.pop()
        node.color = colors[min(step, len(colors) - 1)]
        visited.append(node.val)
        step += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    draw_tree(tree_root)

    return visited

def visualize_heap(heap):
    root = build_heap_tree(heap)
    print("BFS Traversal:")
    bfs_order = bfs_traversal(root)
    print("Order:", bfs_order)

    print("\nDFS Traversal:")
    dfs_order = dfs_traversal(root)
    print("Order:", dfs_order)

# приклад бінарної купи у вигляді списку
heap = [10, 5, 3, 8, 2, 6, 1]

# візуалізація обходів дерева
visualize_heap(heap)