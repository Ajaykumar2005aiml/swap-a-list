def swap_adjacent_elements(arr):
    n = len(arr)
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Example usage
input_array = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original array:", input_array)

swap_adjacent_elements(input_array)
print("Array after swapping adjacent elements:", input_array)
