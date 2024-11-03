# Завдання 6. Жадібні алгоритми та динамічне програмування

budget = 333

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if info["cost"] <= budget:
            budget -= info["cost"]
            total_calories += info["calories"]
            selected_items.append(item)

    return selected_items, total_calories

selected_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    # оптимальний набір страв
    selected_items = []
    total_calories = dp[n][budget]
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item = item_names[i - 1]
            selected_items.append(item)
            b -= items[item]['cost']
    
    selected_items.reverse()
    return selected_items, total_calories

selected_items, total_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")