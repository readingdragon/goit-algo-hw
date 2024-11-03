# Завдання 7. Використання методу Монте-Карло

import numpy as np
import matplotlib.pyplot as plt

# імітація кидків кубиків
def roll_dice(num_rolls):
    dice1 = np.random.randint(1, 7, size=num_rolls)
    dice2 = np.random.randint(1, 7, size=num_rolls)
    return dice1 + dice2

num_rolls = 99999

# імітуємо кидки
sums = roll_dice(num_rolls)

sums_list = np.arange(2, 13)
sum_counts, _ = np.histogram(sums, bins=np.arange(2, 14))

# перетворюємо кількість на ймовірності
probabilities_list = sum_counts / num_rolls

# графік результатів
plt.rcParams['figure.facecolor'] = '#333333'
plt.rcParams['axes.facecolor'] = '#242424'
plt.rcParams['axes.labelcolor'] = 'y'
plt.rcParams['xtick.color'] = 'c'
plt.rcParams['ytick.color'] = 'c'
plt.rcParams['grid.alpha'] = '0.4'
plt.figure(figsize=(11, 6))
plt.bar(sums_list, probabilities_list, color="#036896", alpha=0.7, edgecolor='0')
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум чисел на кубиках (Монте-Карло)",  fontsize=12, color="#f09902")
plt.xticks(range(2, 13))
plt.grid(True, color = '#036896')
plt.show()

# таблиця ймовірностей
print("="*20)
print("Сума\t|Ймовірність")
print("="*20)
for k, v in zip(sums_list, probabilities_list):
    print(f"{k}\t|{v:.5f}")
