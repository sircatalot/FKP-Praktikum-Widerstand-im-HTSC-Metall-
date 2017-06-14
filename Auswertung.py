# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:25:59 2017

@author: stefho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funktionen

def read_from_file(filename):                   #Liest Daten ein
    return np.loadtxt(filename, skiprows=10)


def resistance(U,I):
    r = []
    for i in range(len(U)):
        r.append(U[i]*10**3/I[i])
    return np.array(r)



def derivative(r,T,step):
    j = list(T).index(90.0100)
    n = list(T).index(100.021)
    d=[]
    for i in range(j,n):
        d.append((r[i+int(step/2)]-r[i-int(step/2)])/(T[i+int(step/2)]-T[i-int(step/2)]))
       
    return d


def derivative5point(r,T,h):
    T = list(T)
    for i in T:
        if i >= 90:
            j = T.index(i)
            break
    for i in T:
        if i >= 100:
            n = T.index(i)
            break
        
    d=[]

    for i in range(j,n):
        d.append((-r[i+2*h]+8*r[i+h]-8*r[i-h]+r[i-2*h])/(12*h))
        
    return d, j, n

       
def func(x,mu,sigma,a):
    return a*np.exp(-0.5*(x-mu)**2/(sigma**2))

# Daten
# Magnetfeld 0
x1= read_from_file('Measurement0T.txt')[: ,0]

U1p= read_from_file('Measurement0T.txt')[: ,2]
U1n= read_from_file('Measurement0T.txt')[: ,4]
I1p= read_from_file('Measurement0T.txt')[: ,1]
I1n= read_from_file('Measurement0T.txt')[: ,3]

r1p= resistance(U1p,I1p)
r1n= resistance(U1n,I1n)

r1= r1p+r1n

d1, j1, n1= derivative5point(r1,x1,10)   

popt1, pcov = curve_fit(func, x1[j1:n1], d1, p0 =(94,0.5,0.1))

# Magnetfeld 1
x2= read_from_file('Measurement042T.txt')[: ,0]

U2p= read_from_file('Measurement042T.txt')[: ,2]
U2n= read_from_file('Measurement042T.txt')[: ,4]
I2p= read_from_file('Measurement042T.txt')[: ,1]
I2n= read_from_file('Measurement042T.txt')[: ,3]

r2p= resistance(U2p,I2p)
r2n= resistance(U2n,I2n)

r2= r2p+r2n

d2, j2,n2= derivative5point(r2,x2,10)   

popt2, pcov = curve_fit(func, x2[j2:n2], d2, p0 =(94,0.5,0.1))

# Magnetfeld 2 
x3= read_from_file('Measurement07T.txt')[: ,0]

U3p= read_from_file('Measurement07T.txt')[: ,2]
U3n= read_from_file('Measurement07T.txt')[: ,4]
I3p= read_from_file('Measurement07T.txt')[: ,1]
I3n= read_from_file('Measurement07T.txt')[: ,3]

r3p= resistance(U3p,I3p)
r3n= resistance(U3n,I3n)

r3= r3p+r3n

d3, j3,n3= derivative5point(r3,x3,10)   

popt3, pcov = curve_fit(func, x3[j3:n3], d3, p0 =(94,0.5,0.1))




print(popt1,popt2,popt3)


#Plot

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

ax1.plot(x1[j1:n1], d1, 'blue', label='Data, $B$ = 0T')
ax1.axvline(94.28436814, color='black', linestyle='--')
ax1.axhline(y=0.17,xmin=0.428436814,xmax=0.465754213,c="black", linestyle='-')
ax1.plot(x1[j1:n1], func( x1[j1:n1], *popt1), 'r-', label='Fit')

ax2.plot(x2[j2:n2], d2, 'orange', label='Data, $B$ = 0.42T')
ax2.axvline(94.01142045, color='black', linestyle='--')
ax2.axhline(y=0.14,xmin=0.401142045,xmax=0.445761792,c="black", linestyle='-')
ax2.plot(x2[j2:n2], func( x2[j2:n2], *popt2), 'r-', label='Fit')

ax3.plot(x3[j3:n3], d3, 'green',label='Data, $B$ = 0.7T')
ax3.axvline(94.14833148, color='black', linestyle='--')
ax3.axhline(y=0.135,xmin=0.414833148,xmax=0.467751921,c="black", linestyle='-')
ax3.plot(x3[j3:n3], func( x3[j3:n3], *popt3), 'r-', label='Fit')

ax2.set_ylabel('Derivatve of resistance [ $ {\mathrm{m} \Omega}/{\mathrm{K}}$ ]')
plt.xlabel('Temperature [K]')

ax1.legend()
ax2.legend()
ax3.legend()
plt.savefig('Criticaltemperature.jpg', dpi= 300)
plt.show()
