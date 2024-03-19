import numpy as np
import matplotlib.pyplot as plt

L = 1.0
N = 1000

xs,h  = np.linspace(0,L,N,retstep=True)
us = np.where(xs<L/2,2*xs,2-2*xs)

dt = .0001

mu = dt/h**2

t = 0
tf = 10.0

line, = plt.plot(xs,us)
plt.ylim(-.5,1.1)

A = np.eye(N-2)*(mu+1) -(mu/2)* np.eye(N-2,k=1) -(mu/2)*np.eye(N-2,k=-1)
B = np.linalg.inv(A)
C = np.eye(N-2)*(1-mu)+(mu/2)*np.eye(N-2,k=-1)+(mu/2)*np.eye(N-2,k=1)

while t<tf:
    us [1:-1]=np.dot(C,us[1:-1])
    us [1:-1] = np.dot(B,us[1:-1])
    t += dt
    line.set_ydata(us)
    plt.pause(.0000001)

plt.show()
