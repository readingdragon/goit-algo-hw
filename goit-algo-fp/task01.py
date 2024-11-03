# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def sorted_insert(head, node):
    if not head or node.data <= head.data:
        node.next = head
        return node
    current = head
    while current.next and current.next.data < node.data:
        current = current.next
    node.next = current.next
    current.next = node
    return head


def insertion_sort(head):
    sorted_head = None
    while head:
        next_node = head.next
        sorted_head = sorted_insert(sorted_head, head)
        head = next_node
    return sorted_head


def merge_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


# вузли списків
node1 = Node(1)
node2 = Node(66)
node3 = Node(24)
node1.next = node2
node2.next = node3

node4 = Node(11)
node5 = Node(6)
node6 = Node(25)
node4.next = node5
node5.next = node6

# реверс списку
reversed_list = reverse_list(node1)
print("Reversed list:", end=" ")
print_list(reversed_list)

# сортуємо список
sorted_list = insertion_sort(reversed_list)
print("Sorted list:", end=" ")
print_list(sorted_list)

# злиття списків
merged_list = merge_lists(sorted_list, node4)
print("Merged list:", end=" ")
print_list(merged_list)