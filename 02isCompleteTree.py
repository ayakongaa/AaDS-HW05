from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCompleteTree(root):
    if root is None:
        return True

    queue = deque([root])
    should_be_leaf = False

    while queue:
        node = queue.popleft()

        if node is None:
            should_be_leaf = True
        else:
            if should_be_leaf:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


heap = Node(20,
            Node(15,
                 Node(7),
                 Node(9)),
            Node(10))
print(isCompleteTree(heap)) 
