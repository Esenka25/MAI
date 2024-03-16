import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

W = 0.8 # длина тележки
H = 0.2 # высота тележки
r = 0.1 # радиус колёс
x0 = 0 # начало движения
l = 0.5 # длина палки

t = np.linspace(0, 10, 1001)
s = W/2 + t%2.6
phi = (np.pi/2)*np.sin(3*(t%2.6))

xA = x0 + s
yA = 2*r + H/2
xB = xA + l*np.sin(phi)
yB = yA - abs(l*np.cos(phi))
xT = np.array([-W/2, -W/2, W/2, W/2, 0.28*W, 0.3*W, 0.32*W, -0.32*W, -0.3*W, -0.28*W, -W/2])
yT = np.array([-H/2, H/2, H/2, -H/2, -H/2,-H/2-r,-H/2,-H/2,-H/2-r,-H/2,-H/2])
Alpha = np.linspace(0,6.29,50)
xK = r*np.sin(Alpha)
yK = r*np.cos(Alpha)

N = 2
r1=0.03
r2=0.1
Beta0 = np.linspace(0,1,50*N+1)
Betas = Beta0*(N*2*np.pi+phi[0]-np.pi)
xS = -(r1+(r2-r1)*Betas/(N*2*np.pi-phi[0]))*np.sin(Betas)
yS = (r1+(r2-r1)*Betas/(N*2*np.pi-phi[0]))*np.cos(Betas)


fig = plt.figure(figsize=[13,9])
ax = fig.add_subplot(1,1,1)
ax.axis('equal')
ax.set(xlim=[-0.5,3],ylim=[-0.25,1])

ax.plot([0,0,2.75],[1.75,0,0],color=[0,0.5,0],linewidth=4)

SpiralnayaPruzzhina = ax.plot(xS+xA[0], yS+yA, color=[1, 0.5, 0.5])[0]


Telega = ax.plot(xA[0]+xT,yA+yT,color=[0,0,0])[0]
AB = ax.plot([xA[0], xB[0]], [yA, yB[0]], color=[1,0,0])[0]
A = ax.plot(xA[0],yA,'o',color=[1,0,0])[0]
B = ax.plot(xB[0],yB[0],'o',color=[0,0.75,0],markersize=20,markerfacecolor=[0,1,0],linewidth=2)[0]
K1 = ax.plot(xK+xA[0]-W*0.3,yK+r,color=[0,0,0])[0]
K2 = ax.plot(xK+xA[0]+W*0.3,yK+r,color=[0,0,0])[0]


def kadr(i):
    A.set_data(xA[i],yA)
    B.set_data(xB[i], yB[i])
    AB.set_data([xA[i], xB[i]], [yA, yB[i]])
    Telega.set_data(xA[i]+xT, yA+yT)
    K1.set_data(xK+xA[i]-W*0.3,yK+r)
    K2.set_data(xK + xA[i] + W * 0.3, yK + r)

    Betas = Beta0 * (N * 2 * np.pi + phi[i] - np.pi)
    xS = -(r1 + (r2 - r1) * Betas / (N * 2 * np.pi - phi[i])) * np.sin(Betas)
    yS = (r1 + (r2 - r1) * Betas / (N * 2 * np.pi - phi[i])) * np.cos(Betas)
    SpiralnayaPruzzhina.set_data(xS+xA[i], yS+yA)
    return [A, B, AB, Telega, K1, K2, SpiralnayaPruzzhina]

kino = FuncAnimation(fig,kadr,interval = t[1]-t[0],frames=len(t))

plt.show()
