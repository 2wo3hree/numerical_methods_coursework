import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Длина пространственной области
L = 1.0

# Параметры сетки
Nx = 100
Nt = 100
dx = L / (Nx - 1)
dt = 0.01
c = 1.0

# Начальные условия
x = np.linspace(0, L, Nx)
u_initial = np.cos(np.pi * x / L)

# Решение уравнения переноса схемой "бегущего" счета
u = np.zeros((Nt, Nx))
u[0, :] = u_initial

# Применение начального условия u(t, 0) = e^(-t)
u[:, 0] = np.exp(-np.arange(Nt) * dt)

for n in range(1, Nt):
    for i in range(1, Nx):
        u[n, i] = u[n - 1, i] - c * dt / dx * (u[n - 1, i] - u[n - 1, i - 1]) + ( i * dx + n * dt) * dx * dt

# Построение трехмерного графика
X, T = np.meshgrid(x, np.arange(Nt) * dt)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')

ax.set_xlabel('Пространство (x)')
ax.set_ylabel('Время (t)')
ax.set_zlabel('Значение u')
ax.set_title('Решение уравнения переноса')

# Изменение диапазона значений по z
ax.set_zlim(-1, 1.5)

plt.show()