def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    pivot_index = low - 1  # Index of the smaller element

    for i in range(low, high):
        if arr[i] < pivot:
            pivot_index += 1  # Increment index of smaller element
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]  # Swap

    # Swap the pivot element with the element at pivot_index + 1
    arr[pivot_index + 1], arr[high] = arr[high], arr[pivot_index + 1]
    return pivot_index + 1  # Return the partitioning index

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pi - 1)  # Recursively sort the left subarray
        quick_sort(arr, pi + 1, high)  # Recursively sort the right subarray

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividing
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Sort recursively
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare each & merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
