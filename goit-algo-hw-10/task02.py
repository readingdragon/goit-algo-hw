import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return (x + 6) ** 2

# Нижня, верхня межа та к-сть точок
a, b, n = 0, 2, 66666

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

target_area = y_random < f(x_random)

analytical_solution = (b**3) / 3 + 6 * b**2 + 36 * b

monte_carlo_solution = (b - a) * (f(b)) * np.sum(target_area) / n

quad_solution, _ = quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 500)
y = f(x)

print(f"Значення інтеграла знайдене аналітично: {analytical_solution:.6f}")
print(f"Значення інтеграла знайдене методом Монте-Карло: {monte_carlo_solution:.6f}")
print(f"Значення інтеграла знайдене за допомогою функції quad: {quad_solution:.6f}")

# Створення графіка
plt.figure(figsize=(11, 6))
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.facecolor'] = '#242424'
plt.rcParams['axes.edgecolor'] = '#036896'
plt.rcParams['axes.labelcolor'] = 'y'
plt.rcParams['xtick.color'] = 'c'
plt.rcParams['ytick.color'] = 'c'
plt.rcParams['grid.alpha'] = '0.4'

plt.axvline(a, color='xkcd:sky blue', linestyle='--', linewidth=1, label='a')
plt.axvline(b, color='xkcd:sky blue', linestyle='--', linewidth=1, label='b')

plt.axhline(0, color='xkcd:sky blue',linewidth=0.5)
plt.axvline(0, color='xkcd:sky blue',linewidth=0.5)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
plt.fill_between(ix, iy, color='#036896', alpha=0.3)

# Малювання функції
plt.plot(x, y, 'k-', label='Функція', color="yellow", lw=1)
plt.title('Графік інтегрування f(x) = (x + 6) ** 2 від ' + str(a) + ' до ' + str(b), fontsize=12, color="#f09902")
plt.xlabel('$x$');
plt.ylabel('$y$');
plt.legend(loc='upper left', shadow=True, labelcolor = 'xkcd:sky blue', frameon = False)
plt.grid(True, color = '#036896')

plt.show()