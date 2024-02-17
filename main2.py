def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)

        if target < arr[mid]:
            right = mid - 1
            upper_bound = arr[mid]
        else:
            left = mid + 1
            if mid + 1 < len(arr):
                upper_bound = arr[mid + 1]

    return (iterations, upper_bound)

# Приклад використання
arr = [1.1, 2.2, 3.3, 4.4, 5.5]
target = 3.3
print(binary_search_with_upper_bound(arr, target))

target = 3.0
print(binary_search_with_upper_bound(arr, target))
