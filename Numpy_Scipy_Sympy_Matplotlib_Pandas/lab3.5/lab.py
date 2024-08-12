from sympy import *
from sympy.plotting import *

init_printing(use_latex=True)

x, y = symbols('x, y', real=True)
a, b = symbols('alpha, beta', real=True)
ex1 = (208 * log(x, 10) + x**2) / (Abs(x - y**2) - exp(-y))
display(ex1)
size = 3
p1 = plot3d(ex1, (x, -size, size), (y, -size, size),
       title='График 1-го выражения', zlabel='z')
ex2 = (x*exp(x*y) + 8*sin(x)**2) / (x*(x - y)*(3*x + y))
p2 = plot3d(ex2, (x, -size, size), (y, -size, size),
            title='График 2-го выражения', zlabel='z')
display(ex2)
ex3 = 6*x**2 + 7*x*(y**2)*cos(x + y) + 2*y - 9*sqrt(Abs(y)) + 6
p3 = plot3d(ex3, (x, -size, size), (y, -size, size),
            title='График 3-го выражения', zlabel='z')
ex4 = log(2 + x, 10) + x**2 - 3
size = 5
p4 = plot(ex4, (x, -size, size),
          markers=[{'args': [[0.26], [0], 'o']}],
          legend=True,
          title='График 4-го выражения',
          xlabel='x', ylabel='y');

ex5 = log(1 + 2*x) - 2 + x
p5 = plot(ex5, (x, -size, size),
          markers=[{'args': [[2.6], [0], 'o']}],
          legend=True,
          title='График 5-го выражения',
          xlabel='x', ylabel='y');
ex6 = 15*a**2 + 7*b**2 * cos(a + b) + 2*b - 9*a*sqrt(Abs(b)) + 6
p1 = plot3d(ex6, (a, -size, size), (b, -size, size),
       title='График 6-го выражения', zlabel='z')


a_, b_ = -5, 15
p4 = plot(ex4, (x, a_, b_),
          markers=[{'args': [[0.26, 2.6], [0, 0], 'o']}],
          legend=True,
          title='График двух функций с помощью "append"',
          xlabel='x', ylabel='y', show=False)

p5 = plot(ex5, (x, a_, b_), show=False)
p4.append(p5[0])
p4.show()



p4 = plot(ex4, (x, a_, b_),
          markers=[{'args': [[0.26, 2.6], [0, 0], 'o']}],
          legend=True,
          title='График двух функций с помощью "extend"',
          xlabel='x', ylabel='y', show=False)
p5 = plot(ex5, (x, a_, b_), show=False)
p4.extend(p5)
p4.show()