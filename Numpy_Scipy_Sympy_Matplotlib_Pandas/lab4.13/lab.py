import sympy as sp
import pandas as pd

# Определение символьных переменных и функции
x = sp.Symbol('x')
y = sp.Function('y')(x)

# Начальное условие
y0 = 1

# Отрезок [x0; b] и шаг h
x0 = 1
b = 6
h = 0.5

# Определение правой части ОДУ
f = x**2 - y

# Решение ОДУ с использованием функции dsolve
eq = sp.Eq(sp.Derivative(y, x), f)
solution = sp.dsolve(eq, ics={y.subs(x, x0): y0})

# Создание списка значений x и y
x_values = [x0 + i * h for i in range(int((b - x0) / h) + 1)]
y_values = [solution.rhs.subs(x, val) for val in x_values]

# Создание DataFrame из списков значений
df = pd.DataFrame({'x': x_values, 'y': y_values})

# Вывод таблицы значений
print(df)

# Построение графика решения
sp.plot(solution.rhs, (x, x0, b), xlabel='x', ylabel='y', title='Решение ОДУ: $y\' = x^2 - y$, $y(1) = 1$')
