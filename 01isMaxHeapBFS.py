from collections import deque


def isMaxHeap(arr):
    n = len(arr)
    if n <= 1:
        return True

    queue = deque()
    queue.append(0)

    while queue:
        i = queue.popleft()

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            if arr[i] < arr[left]:
                return False
            queue.append(left)

        if right < n:
            if arr[i] < arr[right]:
                return False
            queue.append(right)

    return True
    
    
s = [int(x) for x in input().split()]
print(isMaxHeap(s))
