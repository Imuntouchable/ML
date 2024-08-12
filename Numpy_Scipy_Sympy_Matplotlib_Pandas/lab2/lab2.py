import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f1(x):
    return np.log10(2 + x) + x**2 - 3

def f2(x):
    return np.log(1 + 2*x) - 2 + x

def f3(x, y):
    return 15*x**2 + 7*y**2 * np.cos(x+y) + 2*y - 9*x*np.sqrt(np.abs(y)) + 6

x_values = np.linspace(-10, 10, 20)
f1_values = f1(x_values)
f2_values = f2(x_values)
plt.plot(x_values, f1_values, label='f1(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x_values, f2_values, label='f2(x)', color='red', linestyle='--', linewidth=2)
plt.legend()
plt.title('Графики функций f1(x) и f2(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(x_values, f1_values, label='f1(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x_values, f2_values, label='f2(x)', color='red', linestyle='--', linewidth=2)
plt.legend()
plt.title('Графики функций f1(x) и f2(x)')
plt.xlabel('x')
plt.ylabel('y')
df_f1 = pd.DataFrame({'x': x_values, 'f1(x)': f1_values})
df_f2 = pd.DataFrame({'x': x_values, 'f2(x)': f2_values})
x_values = np.linspace(-5, 5, 20)
y_values = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_values, y_values)
Z = f3(X, Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('График функции f3(x, y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
df_f3 = pd.DataFrame(Z, index=x_values, columns=y_values)
print("Таблица значений для f1(x):")
print(df_f1)
print("\nТаблица значений для f2(x):")
print(df_f2)
print("\nТаблица значений для f3(x, y):")
print(df_f3)
plt.show()
