import numpy as np
import matplotlib.pyplot as plt

s = 0.2; x0 = 3

f = lambda x: (1/np.sqrt(2*np.pi*s**2))*np.exp((-(x-x0)**2)/(2*s**2))

V0 = 40

def V(x):
    if (x<=7) and (x>=6):
        return V0
    else:
        return 0
        
#V = lambda x : 0.1*x**2
        
N = 300
dt = 0.01

xs, h = np.linspace(-10.0,10.0,N,retstep=True,endpoint= True)

psi0 = f(xs)

Vs = np.array ([V(i) for i in xs])

kt = 2j/dt

A = np.diag(-2 +(kt-Vs)*h**2) + np.eye(N,k=1) + np.eye(N,k=-1)
B =  np.linalg.inv(A)
U =  B*(4*1j*h**2)/dt - np.eye(N)

t = 0
tf = 2

k = 0
psi = psi0

line = plt.plot(xs,psi)[0]
line1 = plt.plot(xs, Vs, ":")[0]
plt.ylim([-1.5,1.5])     
while t<tf:
    psi = np.dot(U,psi)
    t += dt    
    line.set_ydata(psi)
    plt.pause(.1)

plt.show()

