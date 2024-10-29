import timeit

# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result

# Функція динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    used_coins = [{} for _ in range(amount + 1)]

    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= sub_amount:
                if min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                    min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                    used_coins[sub_amount] = used_coins[sub_amount - coin].copy()
                    used_coins[sub_amount][coin] = used_coins[sub_amount].get(coin, 0) + 1

    return used_coins[amount] if min_coins[amount] != float('inf') else {}

# Функція для вимірювання часу виконання алгоритму
def measure_sorting_time(algo, amount):
    start_time = timeit.default_timer()
    algo(amount)

    measured_time = timeit.default_timer() - start_time

    return measured_time

# тест
amount = 256

print(find_coins_greedy(amount))
print(find_min_coins(amount))

print(f"Жадібний алгоритм впорався за: {measure_sorting_time(find_coins_greedy, amount)} сек.")
print(f"Алгоритм динамічного програмування впорався за: {measure_sorting_time(find_min_coins, amount)} сек.")

amount = 25333303

print(find_coins_greedy(amount))
print(find_min_coins(amount))

print(f"Жадібний алгоритм впорався за: {measure_sorting_time(find_coins_greedy, amount)} сек.")
print(f"Алгоритм динамічного програмування впорався за: {measure_sorting_time(find_min_coins, amount)} сек.")
