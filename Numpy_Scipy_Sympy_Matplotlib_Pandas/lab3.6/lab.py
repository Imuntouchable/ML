from sympy import symbols, expand, factor, collect, cancel, apart, trigsimp, expand_trig, powsimp, sin, cos
# Определение символьных переменных
x, y = symbols('x y')

# Символьные выражения
expression1 = (x + 1)**3
expression2 = x**4 - 1
expression3 = x*y + x - y - 1

# Расширение выражения
expanded_expression1 = expand(expression1)

# Факторизация алгебраического выражения
factored_expression2 = factor(expression2)

# Сбор общих членов выражения
collected_expression3 = collect(expression3, x)

# Преобразование рациональной формы в стандартную форму
rational_expression1 = (x**2 - 1)/(x + 2)
canceled_expression1 = cancel(rational_expression1)

# Разложение частичной дроби на рациональную функцию
partial_fraction_expression1 = (x**2 + 3*x + 2)/(x + 2)
apart_expression1 = apart(partial_fraction_expression1)

# Тригонометрическое упрощение
trig_expression1 = sin(x)**2 + cos(x)**2
trigsimp_expression1 = trigsimp(trig_expression1)

# Тригонометрическое разворачивание
expand_trig_expression1 = expand_trig(trig_expression1)

# Упрощение выражения со степенями
power_expression1 = (x + 1)**2
powsimp_expression1 = powsimp(power_expression1)

# Вывод результатов
print("Расширение выражения:")
display(expanded_expression1)
print("Факторизация алгебраического выражения:")
display(factored_expression2)
print("Сбор общих членов выражения:")
display(collected_expression3)
print("Преобразование рациональной формы в стандартную форму:")
display(canceled_expression1)
print("Разложение частичной дроби на рациональную функцию:")
display(apart_expression1)
print("Тригонометрическое упрощение:")
display(trigsimp_expression1)
print("Тригонометрическое разворачивание:")
display(expand_trig_expression1)
print("Упрощение выражения со степенями:")
display(powsimp_expression1)