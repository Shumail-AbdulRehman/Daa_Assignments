import random

RECURSION_DEPTH_THRESHOLD = 10

def hybrid_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    if depth > RECURSION_DEPTH_THRESHOLD:
        return merge_sort(arr)
    
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return hybrid_sort(left, depth + 1) + middle + hybrid_sort(right, depth + 1)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

arr = [random.randint(1, 100) for _ in range(20)]
print("Original array:", arr)
sorted_arr = hybrid_sort(arr)
print("Sorted array:", sorted_arr)
