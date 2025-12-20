class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderMin(node, k, counter):
    if node is None:
        return None

    leftResult = inorderMin(node.left, k, counter)
    if leftResult is not None:
        return leftResult

    counter[0] += 1

    if counter[0] == k:
        return node.val

    return inorderMin(node.right, k, counter)


root = Node(20,
            Node(15,
                 Node(7),
                 Node(9)),
            Node(10))

k = 3
counter = [0]
result = inorderMin(root, k, counter)
print(result)
