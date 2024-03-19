
import numpy as np
import matplotlib.pyplot as plt

L = 1.0         #Length of rod
N = 100         # No. of lattice points

xs,h  = np.linspace(0,L,N,retstep=True)     #lattice
us = np.where(xs<L/2,2*xs,2-2*xs)           #initial u values

dt = .00004                                 #time step
#dt = .0001

mu = dt/h**2

t = 0
tf = 10.0

line = plt.plot(xs,us)[0]


while t<tf:
    t += dt
    us [1:-1]  = mu*(us[0:-2] + us[2:]) + (1 - 2*mu)*us[1:-1]
    us[0] = 0
    us[-1] = np.sin(25*t)**2
    line.set_ydata(us)
    plt.pause(.0000001)

plt.show()
