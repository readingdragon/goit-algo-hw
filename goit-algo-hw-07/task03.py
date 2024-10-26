class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calc_sum(root):
    if root is None:
        return 0
    
    # Повертаємо значення поточного вузла плюс суми значень у лівому та правому піддеревах
    return root.key + calc_sum(root.left) + calc_sum(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(33)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(66)

total_sum = calc_sum(root)
print("Сума всіх значень у дереві:", total_sum)