def selection_sort(arr):
    n = len(arr)
    print(f"Original Array: {arr}\n")
    
    for i in range(n):
        min_index = i
        # Find the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Step {i + 1}: Swapped {arr[i]} with {arr[min_index]} -> {arr}")
    
    return arr

# Example usage
example_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(example_array)

print("\n✅ Sorted Array:", sorted_array)
def selection_sort(arr):
    n = len(arr)
    print(f"Original Array: {arr}\n")
    
    for i in range(n):
        min_index = i
        # Find the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Step {i + 1}: Swapped {arr[i]} with {arr[min_index]} -> {arr}")
    
    return arr

# Example usage
example_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(example_array)

print("\n✅ Sorted Array:", sorted_array)
