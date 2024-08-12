from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# Определение функции уравнения
def equation1(x):
    return np.exp(x) - (x + 1)**2

# Определение производной функции
def derivative1(x):
    return np.exp(x) - 2*(x + 1)


# 2. Выбор отрезка
# Отрезок [-2, 0.5] содержит один корень

# 3. Таблица значений на отрезке
x_table = np.linspace(-2, 0.5, 10)
f_values = equation1(x_table)
f_prime_values = derivative1(x_table)

print("Таблица значений:")
print(" x      f(x)      f'(x)")
for x, f, f_prime in zip(x_table, f_values, f_prime_values):
    print(f"{x:.3f}  {f:.3f}  {f_prime:.3f}")

# 4. Проверка условия существования единственного корня
# Функция меняет знак на отрезке [-2, 0.5], следовательно, существует единственный корень на этом отрезке

# 5. Решение уравнения
root1 = fsolve(equation1, -1)  # Начальное приближение корня: -1

print("\nРешение уравнения 1:")
print("Корень:", root1)
print("Значение функции в корне:", equation1(root1))

# Задание коэффициентов для второго уравнения
coefficients = [1, -1, -2, 3, -3]

# Сформировать полином
poly = np.poly1d(coefficients)

print("\nПолином:")
print(poly)

x_values = np.linspace(-2, 2, 400)
plt.plot(x_values, equation1(x_values), label='f(x)')
plt.plot(x_values, derivative1(x_values), label="f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функции f(x) и ее первой производной')
plt.legend()
plt.grid(True)
plt.show()