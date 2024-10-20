def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_limit = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_limit = arr[mid]
            high = mid - 1

    return (iterations, upper_limit)

# Test:
array = [0.3, 8.2, 1.5, 0.3, 3.8, 5.1, 6.9, 8.8, 99.9]
sorted_arr = sorted(array)
target_value = 5.2

result = binary_search(sorted_arr, target_value)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
