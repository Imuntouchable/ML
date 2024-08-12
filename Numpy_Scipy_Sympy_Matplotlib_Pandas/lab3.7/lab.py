from sympy import symbols, Piecewise, plot

# Определение символьной переменной
x = symbols('x')

# Кусочно-заданные функции
f1 = Piecewise((x, x >= 0), (-x, x < 0))
f2 = Piecewise((x**3, x <= -1), (2*x, (-1 < x) & (x < 1)), (x**2, x >= 1))
f3 = Piecewise((x, x <= 1), (x**2, x > 1))
display(f1)
display(f2)
display(f3)
# Построение графиков
p1 = plot(f1, show=False, line_color='blue', label='f1: |x|')
p2 = plot(f2, show=False, line_color='green', label='f2: x^3 if x <= -1, 2x if -1 < x < 1, x^2 if x >= 1')
p3 = plot(f3, show=False, line_color='red', label='f3: x if x <= 1, x^2 if x > 1')

# Отображение графиков
p1.extend(p2)
p1.extend(p3)
p1.legend = True
p1.show()