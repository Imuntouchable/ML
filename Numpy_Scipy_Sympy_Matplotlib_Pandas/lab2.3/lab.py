import numpy as np
from scipy.integrate import quad


# Описание подынтегральной функции f(x)
def f(x):
    return x**2 * np.log(x)

# Вычисление определенного интеграла с использованием метода трапеций
def inttrap(x, y):
    return np.trapz(y, x)

# Задание пределов интегрирования и шага
a = 0.4
b = 3.2
h = 0.01

# Вычисление значений подынтегральной функции на интервале [a, b]
x_values = np.arange(a, b + h, h)
y_values = f(x_values)

# Вычисление определенного интеграла методом трапеций
integral_trap = inttrap(x_values, y_values)
print("Определенный интеграл методом трапеций:", integral_trap)

# Вычисление определенного интеграла методом Симпсона
integral_simpson, error = quad(f, a, b)
print("Определенный интеграл методом Симпсона:", integral_simpson)

# Определение функции y(x)
def y(x):
    return x**2 + np.sin(x/2) + 1

# Задание точек, в которых вычисляется производная
x_points = np.array([0.5, 1.5, 2.5])

# Шаг дифференцирования
dx = 1e-6

# Функция для численного дифференцирования (центральная разностная схема)
def numerical_derivative(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

# Вычисление производной в нескольких точках
derivatives_vectorized = numerical_derivative(y, x_points, dx)

# Вычисление производной в каждой точке по отдельности
derivatives_separately = [numerical_derivative(y, x_point, dx) for x_point in x_points]

# Вывод результатов
for i in range(len(x_points)):
    print("Точка:", x_points[i])
    print("Производная (векторизованная):", derivatives_vectorized[i])
    print("Производная (по отдельности):", derivatives_separately[i])