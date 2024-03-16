#импорт необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from math import pi, cos

#фу-ция систем уравнений
def odesys(y, t, M, m, c, l, r, g):
    dy = np.zeros(4)
    dy[0] = y[2]
    dy[1] = y[3]
    a11 = M/2 + m
    a12 = 0
    a21 = 0
    a22 = l+y[0]
    b1 = m*g*np.cos(y[1]) - c*(y[0] + (m*g/c)) + m*(l+y[0])*(y[3]**2)
    b2 = -g*np.sin(y[1]) - 2*(y[2])*(y[3]) + 2*r*(y[1]**2)
    dy[2] = (b1 * a22 - b2 * a12) / (a11 * a22 - a12 * a21)
    dy[3] = (b2 * a11 - b1 * a21) / (a11 * a22 - a12 * a21)
    return dy

#задача параметров
Steps = 1001
t_fin = 20
t = np.linspace(0, t_fin, Steps)
M = 1
m = 0.1
r = 0.4
l = 1
c = 1
g = 9.81

#начальное состояние
x0 = 0.02
phi0 = pi/3
dx0 = 0.2
dphi0 = pi
y0 = [x0, phi0, dx0, dphi0]
Y = odeint(odesys, y0, t, (M, m, c, l, r, g))

#решение
x = Y[:, 0]
phi = Y[:, 1]
dx = Y[:, 2]
dphi = Y[:, 3]  #скорость
ddx = [odesys(y, t, M, m, c, l, r, g)[2] for y, t in zip(Y, t)] #ускорение
ddphi = [odesys(y, t, M, m, c, l, r, g)[3] for y, t in zip(Y, t)]

#графики
fig_for_graphs = plt.figure(figsize=[13, 7])
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 1)
ax_for_graphs.plot(t, x, color="blue")
ax_for_graphs.set_title("x(t)")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 2)
ax_for_graphs.plot(t, phi, color="red")
ax_for_graphs.set_title(r"$\varphi(t)$")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 3)
ax_for_graphs.plot(t, dx, color="green")
ax_for_graphs.set_title(r"$\dot{x}(t)$")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 4)
ax_for_graphs.plot(t, dphi, color="black")
ax_for_graphs.set_title(r"$\dot{\varphi}(t)$")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 5)
ax_for_graphs.plot(t, ddx, color="green")
ax_for_graphs.set_title(r"$\ddot{x}(t)$")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)
ax_for_graphs = fig_for_graphs.add_subplot(2, 3, 6)
ax_for_graphs.plot(t, ddphi, color="black")
ax_for_graphs.set_title(r"$\ddot{\varphi}(t)$")
ax_for_graphs.set(xlim=[0, t_fin])
ax_for_graphs.grid(True)

#анимация
SprX_0 = r + 0.2
X_B = -r * np.cos(phi)
Y_B = -r * np.sin(phi)
X_A = X_B + (l + x - r * phi) * np.sin(phi)
Y_A = Y_B - (l + x - r * phi) * np.cos(phi)
psi = np.linspace(0, 6.28, 150)
X_Cirle = r * np.sin(psi)
Y_Cirle = r * np.cos(psi)
X_Ground = [0, 0, r + 3]
Y_Ground = [r + 3, 0, 0]
X_Low = [r - 0.5, r + 0.5]
Y_Low = [-2.5 * r, -2.5 * r]
X_High = [-r / 2, r / 2]
Y_High = [r + 1, r + 1]
X_Crep_1 = [X_High[0] / 2, 0]
Y_Crep_1 = [Y_High[0], 0]
X_Crep_2 = [0, X_High[1] / 2]
Y_Crep_2 = [0, Y_High[0]]
K = 19
Sh = 0.2
b = 1 / (K - 2)
X_Spr = np.zeros(K)
Y_Spr = np.zeros(K)
X_Spr[0] = 0
Y_Spr[0] = 0
X_Spr[K - 1] = 0
Y_Spr[K - 1] = 1
for i in range(K - 2):
    Y_Spr[i + 1] = b * ((i + 1) - 1 / 2)
    X_Spr[i + 1] = Sh * (-1) ** i
L_Spr = SprX_0 + x
X_C = r
Y_C = 0
X_D = r
Y_D = Y_Low[0] + L_Spr
fig = plt.figure(figsize=[15, 7])
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[-3, 3], ylim=[-2, 2])
# ax.axis("equal")
ax.plot(X_Ground, Y_Ground, color="black", linewidth=1)
ax.plot(X_Low, Y_Low, color="black", linewidth=3)
ax.plot(X_High, Y_High, color="black", linewidth=3)
ax.plot(X_Crep_1, Y_Crep_1, color="black", linewidth=1)
ax.plot(X_Crep_2, Y_Crep_2, color="black", linewidth=1)
Drawed_cirle = ax.plot(0 + X_Cirle, 0 + Y_Cirle, color="black")
Drawed_Spring = ax.plot(r + X_Spr, Y_Low[0] + Y_Spr * L_Spr[0], color="blue")[0]
Line_CD = ax.plot([X_C, X_D], [Y_C, Y_D[0]], color="blue")[0]
Line_BA = ax.plot([X_B[0], X_A[0]], [Y_B[0], Y_A[0]])[0]
Point_B = ax.plot(X_B[0], Y_B[0], marker="o", color="orange")[0]
Point_A = ax.plot(X_A[0], Y_A[0], marker="o", markersize=10, color="red")[0]
def anima(i):
    Point_A.set_data(X_A[i], Y_A[i])
    Point_B.set_data(X_B[i], Y_B[i])
    Line_BA.set_data([X_B[i], X_A[i]], [Y_B[i], Y_A[i]])
    Line_CD.set_data([X_C, X_D], [Y_C, Y_D[i]])
    Drawed_Spring.set_data(r + X_Spr, Y_Low[0] + Y_Spr * L_Spr[i])
    return Point_A, Point_B, Line_BA, Line_CD, Drawed_Spring
anim = FuncAnimation(fig, anima, frames=len(t), interval=40, blit=True)
plt.show()