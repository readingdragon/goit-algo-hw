import random
import timeit

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(f'Type of sort - insertion sort')

# merge sort
def merge_sort(arr):
    def merge_sort_alg(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort_alg(left_half)
            merge_sort_alg(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    print(f'Type of sort - merge sort')

# Timsort
def timsort(arr):
    print(f'Type of sort - Timsort')
    return sorted(arr)

# генерація тестових даних
def generate_test_data(size):
    random_data = [random.randint(0, size) for _ in range(size)]
    sorted_data = sorted(random_data)
    return random_data, sorted_data

# Функція для вимірювання часу виконання алгоритму
def measure_sorting_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)

    measured_time = timeit.default_timer() - start_time

    print(f'Spent time: {measured_time}')
    return 

# розмір даних
sizes = [100, 10000, 28989]

for size in sizes:
    random_data, sorted_data = generate_test_data(size)
    print('-'*42)
    print(f'Test data: size - {size}, type - random data ')
    measure_sorting_time(insertion_sort, random_data.copy())
    
    print('-'*42)
    print(f'Test data: size - {size}, type: random data: ')
    measure_sorting_time(merge_sort, random_data.copy())

    print('-'*42)
    print(f'Test data: size - {size}, type: random data: ')
    measure_sorting_time(timsort, random_data.copy())

    print('-'*42)
    print(f'Test data: size - {size}, type: sorted data: ')
    measure_sorting_time(insertion_sort, random_data.copy())
    
    print('-'*42)
    print(f'Test data: size - {size}, type: sorted data: ')
    measure_sorting_time(merge_sort, random_data.copy())

    print('-'*42)
    print(f'Test data: size - {size}, type: sorted data: ')
    measure_sorting_time(timsort, random_data.copy())