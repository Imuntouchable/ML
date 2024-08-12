import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.optimize import minimize, fmin
import pandas as pd

# Определение функции f(x)
def f(x):
    return np.exp(x) - (x + 1)**2 - 2

# Генерация значений x
x_values = np.linspace(-2, 2, 100)
# Вычисление значений функции f(x)
y_values = f(x_values)

# Построение графика функции f(x)
plt.plot(x_values, y_values, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True)
plt.legend()

# Вычисление первой производной функции f(x) на отрезке [-2, 2]
first_derivative_values = derivative(f, x_values, dx=1e-6, n=1)

# Вычисление второй производной функции f(x) на отрезке [-2, 2]
second_derivative_values = derivative(f, x_values, dx=1e-6, n=2)

# Печать значений первой и второй производной
print("Значения первой производной:")
print(first_derivative_values)
print("\nЗначения второй производной:")
print(second_derivative_values)

# Создаем DataFrame для хранения результатов производных
derivatives_table = pd.DataFrame({
    'x_values': x_values,
    'first_derivative': first_derivative_values,
    'second_derivative': second_derivative_values
})

# Выводим таблицу
print("\nТаблица значений первой и второй производных:")
print(derivatives_table)

x0 = -1.5  # Начальная точка поиска минимума

# Определение вспомогательной функции costf1
def costf1(x):
    return f(x)

# Найти минимум функции f(x) с использованием minimize
result_minimize = minimize(costf1, x0, method='BFGS')
x_min_minimize = result_minimize.x[0]
f_min_minimize = result_minimize.fun

# Найти минимум функции f(x) с использованием fmin
x_min_fmin = fmin(f, x0)

# Вывести результаты
print("\nКоордината точки минимума f(x) с использованием minimize:", x_min_minimize)
print("Значение функции в этой точке:", f_min_minimize)
print("\nКоордината точки минимума f(x) с использованием fmin:", x_min_fmin)
print("Значение функции в этой точке:", f(x_min_fmin))


# Определение функции F(x1, x2)
def F(x1, x2):
    return (2*x1)**2 + x2**2 + x1*x2 + 5*x1 + 18

# Генерация значений x1 и x2
x1_values = np.linspace(-5, 5, 100)
x2_values = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1_values, x2_values)
# Вычисление значений функции F(x1, x2)
Z = F(X1, X2)

# Построение графика функции F(x1, x2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Z, cmap='viridis')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('F(x1, x2)')
plt.title('График функции F(x1, x2)')

# Построение линий уровней функции F(x1, x2)
plt.contour(X1, X2, Z, levels=20)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Линии уровней функции F(x1, x2)')
plt.grid(True)
plt.colorbar(label='F(x1, x2)')
plt.show()

# Выбор начальной точки поиска минимума (x0, y0)
x0, y0 = -4, -4

# Определение вспомогательной функции costf2
def costf2(params):
    x1, x2 = params
    return F(x1, x2)

# Определение вспомогательной функции costf2_grad
def costf2_grad(params):
    x1, x2 = params
    return [derivative(F, x1, dx=1e-6), derivative(F, x2, dx=1e-6)]

# Найти минимум функции F(x1, x2) с использованием minimize
result_minimize = minimize(costf2, [x0, y0], method='BFGS', jac=costf2_grad)
x_min_minimize = result_minimize.x[0]
y_min_minimize = result_minimize.x[1]
F_min_minimize = result_minimize.fun

# Найти минимум функции F(x1, x2) с использованием fminsearch
x_min_fminsearch = fmin(lambda params: F(params[0], params[1]), [x0, y0])

# Вывести результаты
print("\nКоординаты точки минимума F(x1, x2) с использованием minimize:", x_min_minimize, y_min_minimize)
print("Значение функции в этой точке:", F_min_minimize)
print("\nКоординаты точки минимума F(x1, x2) с использованием fminsearch:", x_min_fminsearch[0], x_min_fminsearch[1])
print("Значение функции в этой точке:", F(x_min_fminsearch[0], x_min_fminsearch[1]))
