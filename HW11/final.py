# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

x_limit = [-40, 40]
coeff = [-12, -18, 5, 10, -30]
color = 'b'

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

x = np.arange(x_limit[0], x_limit[1], 0.1)

change_x = []
change_dir = 1

for i in range (len(x) - 1):
    if change_dir == 1:
        if func(x[i], *coeff ) < func(x[i+1], *coeff):
            change_x.append((x[i], func(x[i], *coeff)))
            change_dir = -1
    else:
        if func(x[i], *coeff ) > func(x[i+1], *coeff):
                change_x.append((x[i], func(x[i], *coeff)))
                change_dir = 1

print(len(change_x))
print(f'Корни функции\n{change_x}')

def change_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

plt.figure(figsize=(10,7))
plt.title(f'На промежутке {x_limit} функция имеет {len(change_x)} корней')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.plot('r', label="Возрастание")
plt.plot('b', label="Убывание")
current_x = np.arange(x_limit[0], change_x[0][0], 0.1)
plt.plot(current_x, func(current_x, *coeff), change_color())
for i in range(len(change_x) - 1):
    current_x = np.arange(change_x[i][0], change_x[i+1][0], 0.1)
    plt.plot(current_x, func(current_x, *coeff), change_color())
current_x = np.arange(change_x[-1][0], x_limit[1], 0.1)
plt.plot(current_x, func(current_x, *coeff), change_color())
plt.legend()
plt.show()

