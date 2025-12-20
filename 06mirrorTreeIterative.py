from collections import deque

def mirrorTreeIterative(node):
    if node is None:
        return None

    queue = deque([node])

    while queue:
        current = queue.popleft()

        temp = current.left
        current.left = current.right
        current.right = temp

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return node

def inOrder(node):
    if node is None:
        return []
    return inOrder(node.left) + [node.val] + inOrder(node.right)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1,
            Node(2, Node(4), Node(5)),
            Node(3, Node(6), Node(7)))

mirrorTreeIterative(root)
print(inOrder(root))
