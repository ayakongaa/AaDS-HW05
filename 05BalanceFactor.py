def calculateHeightsAndBalance(node):
    if node is None:
        return 0 

    leftHeight = calculateHeightsAndBalance(node.left)
    rightHeight = calculateHeightsAndBalance(node.right)

    node.balanceFactor = leftHeight - rightHeight

    return 1 + max(leftHeight, rightHeight)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balanceFactor = 0

root = Node(10,
            Node(5,
                 Node(3),
                 Node(7)),
            Node(15,
                 None,
                 Node(20)))

calculateHeightsAndBalance(root)

print(root.balanceFactor)
print(root.left.balanceFactor)
print(root.right.balanceFactor)
