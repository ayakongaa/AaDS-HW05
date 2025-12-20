def isMaxHeap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False

    return True


s = [int(x) for x in input().split()]
print(isMaxHeap(s))
