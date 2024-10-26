class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left:
        current = current.left
    # ключ крайнього лівого вузла є найменьшим значенням
    return current.key

# тест
root = Node(10)
root.left = Node(5)
root.right = Node(33)
root.right.right = Node(66)

min_value = find_min(root)
print("Найменьше значення в дереві:", min_value)