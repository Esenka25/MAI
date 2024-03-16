import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp

START_T = 0


def Rot2D(X, Y, Alpha):
    RotX = X * np.cos(Alpha) - Y * np.sin(Alpha)
    RotY = X * np.sin(Alpha) + Y * np.cos(Alpha)
    return RotX, RotY


t = sp.Symbol('t')

x = 2 + sp.cos(6 * t)
y = t + sp.sin(6 * t)
Vx = sp.diff(x, t)
Vy = sp.diff(y, t)
Wx = sp.diff(Vx, t)
Wy = sp.diff(Vy, t)

F_x = sp.lambdify(t, x)
F_y = sp.lambdify(t, y)
F_Vx = sp.lambdify(t, Vx)
F_Vy = sp.lambdify(t, Vy)
F_Wx = sp.lambdify(t, Wx)
F_Wy = sp.lambdify(t, Wy)

t = np.linspace(0, 10, 1001)

x = F_x(t)
y = F_y(t)
Vx = F_Vx(t)
Vy = F_Vy(t)
Wx = F_Wx(t)
Wy = F_Wy(t)

# график
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
ax.set(xlim=[1, 4], ylim=[-7, 75])
ax.plot(x, y)

# точка
dot = ax.plot(x[START_T], y[START_T], marker='o')[0]

k_V = 1
# сокрость
V_line = \
ax.plot([x[START_T], x[START_T] + k_V * Vx[START_T]], [y[START_T], y[START_T] + k_V * Vy[START_T]], color=[1, 0, 0])[0]

# стрелка скорости
Alpha_V = np.arctan2(Vy, Vx)
a = 1
b = 0.3
x_arr = np.array([-a, 0, -a])
y_arr = np.array([b, 0, -b])
RotVX, RotVY = Rot2D(x_arr, y_arr, Alpha_V[START_T])
V_Arrow = ax.plot(x[START_T] + k_V * Vx[START_T] + RotVX, y[START_T] + k_V * Vy[START_T] + RotVY, color=[1, 0, 0],
                  label="Скорость (k=1)")[0]

k_W = 0.5
# ускорение
W_line = \
ax.plot([x[START_T], x[START_T] + k_W * Wx[START_T]], [y[START_T], y[START_T] + k_W * Wy[START_T]], color=[0, 0, 0.6],
        label="Ускорение (k=0.5)")[0]

# стрелка ускорения
Alpha_W = np.arctan2(Wy, Wx)
RotWX, RotWY = Rot2D(x_arr, y_arr, Alpha_W[START_T])
W_Arrow = ax.plot(x[START_T] + k_W * Wx[START_T] + RotWX, y[START_T] + k_W * Wy[START_T] + RotWY, color=[0, 0, 0.6])[0]

# центр кривизны
CurvX = x - Vy * ((Vx ** 2 + Vy ** 2) / (Vx * Wy - Vy * Wx))
CurvY = y - Vx * ((Vx ** 2 + Vy ** 2) / (Vx * Wy - Vy * Wx))
Curv_Center = ax.plot(CurvX[START_T], CurvY[START_T], marker='X', color=[0, 0.6, 0], label="Центр кривизны")[0]
Curv_Rline = ax.plot([x[START_T], CurvX[START_T]], [y[START_T], CurvY[START_T]])[0]

Curv_R = (Vx ** 2 + Vy ** 2) ** (1.5) / (Vx * Wy - Vy * Wx)
Circle_X = Curv_R * np.cos(t)
Circle_Y = Curv_R * np.sin(t)

Circle_ = plt.Circle((CurvX[START_T], CurvY[START_T]), Curv_R[START_T], color=[0, 0.6, 0], fill=0)
Curv_Circle = ax.add_artist(Circle_)


# анимация
def TheMagicOfThtMovement(i):
    dot.set_data(x[i], y[i])

    Curv_Center.set_data([CurvX[i]], [CurvY[i]])

    Curv_Rline.set_data([x[i], CurvX[i]], [y[i], CurvY[i]])

    Curv_Circle.center = ([CurvX[i]], [CurvY[i]])
    Curv_Circle.set_radius(Curv_R[i])

    V_line.set_data([x[i], x[i] + k_V * Vx[i]], [y[i], y[i] + k_V * Vy[i]])

    RotVX, RotVY = Rot2D(x_arr, y_arr, Alpha_V[i])
    V_Arrow.set_data(x[i] + k_V * Vx[i] + RotVX, y[i] + k_V * Vy[i] + RotVY)

    W_line.set_data([x[i], x[i] + k_W * Wx[i]], [y[i], y[i] + k_W * Wy[i]])

    RotWX, RotWY = Rot2D(x_arr, y_arr, Alpha_W[i])
    W_Arrow.set_data(x[i] + k_W * Wx[i] + RotWX, y[i] + k_W * Wy[i] + RotWY)

    return [dot, Curv_Center, Curv_Rline, Curv_Circle, V_line, V_Arrow, W_line, W_Arrow]


kino = FuncAnimation(fig, TheMagicOfThtMovement, frames=len(t), interval=12)

ax.legend()

plt.show()