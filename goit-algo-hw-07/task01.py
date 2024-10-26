class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def find_max(root):
    if root is None:
        return None

    current = root
    while current.right:
        current = current.right
    # ключ крайнього правого вузла є найбільшим значенням
    return current.key

# тест
root = Node(10)
root.left = Node(5)
root.right = Node(33)
root.right.right = Node(66)

max_value = find_max(root)
print("Найбільше значення в дереві:", max_value)