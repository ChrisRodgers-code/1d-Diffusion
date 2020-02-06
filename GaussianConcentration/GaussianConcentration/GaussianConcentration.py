import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

#length scale is cm and time scale is seconds
D = 0.282 #cm^2/s
ux = 1.0 #cm/s

xmin = -5 #cm
xmax = 5 #cm
xgrain = 100

fig = plt.figure()
ax = plt.axes(xlim=(xmin,xmax),ylim=(0,1))
line, = ax.plot([],[], lw=3)

def init():
    line.set_data([],[])
    return line, 

def animate(i):
    x = np.linspace(xmin,xmax,xgrain)
    dt = 0.1
    cx = 1/np.sqrt(4*np.pi*D*(1+dt*i))*np.exp(-(x-ux*(1+dt*i))**2/(4*D*(1+dt*i)))
    line.set_data(x,cx)
    return line,

anim = FuncAnimation(fig, animate,init_func=init,frames=1000,interval=20,blit=True)

plt.show()