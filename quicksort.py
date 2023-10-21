def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_arr = quicksort(arr)

print("Sorted array:", sorted_arr)
