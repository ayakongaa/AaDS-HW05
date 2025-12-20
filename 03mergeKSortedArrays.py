import heapq

def mergeKSortedArrays(sortedArrays):
    merged_array = []
    min_heap = []

    for i in range(len(sortedArrays)):
        if sortedArrays[i]:
            heapq.heappush(min_heap, (sortedArrays[i][0], i, 0))

    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)

        if element_idx + 1 < len(sortedArrays[array_idx]):
            next_value = sortedArrays[array_idx][element_idx + 1]
            heapq.heappush(
                min_heap,
                (next_value, array_idx, element_idx + 1)
            )

    return merged_array


arr = [[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9] ]

print(mergeKSortedArrays(arr))
