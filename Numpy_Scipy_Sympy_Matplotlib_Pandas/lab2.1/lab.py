import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

x = np.array([-5, -3.5, -2.5, -1.5, -0.5, 0, 0.5])
y = np.array([2.44, 2.13, 1.455, 0.803, 0.49, 0.375, -6.51*10**-3])

# Создаем DataFrame для хранения результатов интерполяции
df_interp = pd.DataFrame({'x': x, 'y': y})

fig = go.Figure()

# Добавляем исходные данные на график
fig.add_trace(go.Scatter(x=x,
                         y=y,
                         mode='markers',
                         marker=dict(color='LightSkyBlue', size=15, line=dict(color='MediumPurple', width=3)),
                         name="Исходные данные"))

# Интерполируем данные
interp_func = interp1d(x, y, kind='cubic')

# Генерируем значения для построения графика интерполяции
x_interp = np.linspace(x.min(), x.max(), 100)
y_interp = interp_func(x_interp)

# Строим график интерполяции
fig.add_trace(go.Scatter(x=x_interp,
                         y=y_interp,
                         name="Интерполяция"))

# Вычисляем среднеквадратичное отклонение
y_pred = interp_func(x)
df_interp['interp'] = y_pred
sko = np.sqrt(np.mean((y - y_pred) ** 2))

# Выводим результаты интерполяции
print("Результаты интерполяции:")
print(df_interp)

fig.update_layout(title="Построение графика интерполяции",
                  xaxis_title="Значение аргумента",
                  yaxis_title="Значение интерполяции")

fig.show()
