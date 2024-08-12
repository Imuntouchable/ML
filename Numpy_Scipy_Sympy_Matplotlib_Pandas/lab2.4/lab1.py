import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Определение функции правой части ОДУ первого порядка
def model(y, x):
    return np.cos(y) + x**2

# Начальное условие
y0 = 1

# Отрезок [x0; b] и шаг h
x0 = 1
b = 6
h = 0.5

# Создание массива точек x на отрезке [x0; b] с шагом h
x_values = np.arange(x0, b + h, h)

# Решение ОДУ с помощью odeint
solution = odeint(model, y0, x_values)

# Создание DataFrame для хранения решения
solution_df = pd.DataFrame({'x': x_values, 'y': solution[:, 0]})

# Вывод таблицы с решением
print(solution_df)

# Построение графика для ОДУ первого порядка
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_values, solution, marker='o', label='Решение ОДУ 1-го порядка')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Решение ОДУ 1-го порядка: $y\' = \cos(y) + x^2$')
plt.legend()
plt.grid(True)

# Определение функции правой части системы ОДУ второго порядка
def system_model(y, x):
    y1, y2 = y
    return [y2, 2 * np.exp(x) + 2 * y2 - y1]

# Начальные условия
y0 = [2, 5]

# Отрезок [x0; b] и шаг h
x0 = 0
b = 1
h = 0.1

# Создание массива точек x на отрезке [x0; b] с шагом h
x_values = np.arange(x0, b + h, h)

# Решение системы ОДУ с помощью odeint
solution_system = odeint(system_model, y0, x_values)

# Создание DataFrame для хранения решения
solution_df_system = pd.DataFrame({'x': x_values, 'y1': solution_system[:, 0], 'y2': solution_system[:, 1]})

# Вывод таблицы с решением
print(solution_df_system)

# Построение графика для системы ОДУ второго порядка
plt.subplot(1, 2, 2)
plt.plot(x_values, solution_system[:, 0], marker='o', label='$y_1$')
plt.plot(x_values, solution_system[:, 1], marker='o', label='$y_2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Решение системы ОДУ 2-го порядка: $y\'\' - 2y\' + y = 2e^x$')
plt.legend()
plt.grid(True)

# Вывод графиков
plt.tight_layout()
plt.show()
