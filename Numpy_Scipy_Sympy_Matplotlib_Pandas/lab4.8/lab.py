from sympy.plotting import plot
from sympy import symbols, interpolate

# Define symbols
x = symbols('x')
xs, ys, txy = symbols('xs, ys, txy')

# Define data points
ys = [-5, 4, 6, -3, -8]
xs = [-5, -4, -3, 0, 1]

# Plot the data points
pmar1 = plot(0, markers=[{'args': [[-5, -4, -3, 0, 1], [-5, 4, 6, -3, -8], "o"]}],
             xlabel='xs', ylabel='ys', xlim=(-7,3), ylim=(-9,7))

# Interpolate the data points
int1 = interpolate([(x1, y1) for x1, y1 in zip(xs, ys)], x)
pint1 = plot(int1, markers=[{"args": [[5, 4, 3, 8, 1], [-5, 4, 6, -3, -8], "o"]}], 
             xlim=(-7,3), ylim=(-9,7))
pint2 = plot(int1, xlim=(-7,3), ylim=(-9,7), show=False)

# Combine the plots
pint1.append(pint2[0])
pint1.show()

# Evaluate the interpolating polynomial at specific points
a1 = int1.subs(x, -4.5)
a2 = int1.subs(x, -3.5)
