from sympy import *
from IPython.display import display
import matplotlib.pyplot as plt

init_printing(use_latex=True)

x, y = symbols('x, y', real=True)
a, b = symbols('alpha, beta', real=True)
ex1 = (208 * log(x, 10) + x**2) / (Abs(x - y**2) - exp(-y))
ex2 = (x*exp(x*y) + 8*sin(x)**2) / (x*(x - y)*(3*x + y))
ex3 = 6*x**2 + 7*x*(y**2)*cos(x + y) + 2*y - 9*sqrt(Abs(y)) + 6
ex4 = log(2 + x, 10) + x**2 - 3
ex5 = log(1 + 2*x) - 2 + x
ex6 = 15*a**2 + 7*b**2 * cos(a + b) + 2*b - 9*a*sqrt(Abs(b)) + 6
exprs = [ex1, ex2, ex3, ex4, ex5, ex6]
for i, exp in enumerate(exprs):
    print(f"Выражение {i+1}: ")
    display(exp)
    print("Внутреннее представление выражения:")
    display(srepr(exp))
    print("Атомы: ", exp.atoms())
    print("Func: ", exp.func)
    print("Args: ", exp.args)
    print('\n')
dots = [(1, 0), (E, 0.9), (pi ,pi/12)]
for x_y in dots:
    x_val, y_val = x_y
    print(f"\nОценка численных значений для x = {x_val} и y = {y_val}:")
    for i, exp in enumerate(exprs):
        res = exp.subs({x:x_val, y:y_val, a:x_val, b:y_val}).evalf(n=5)
        print(f"Для выражения {i+1}: результат оценивается как {res}")


