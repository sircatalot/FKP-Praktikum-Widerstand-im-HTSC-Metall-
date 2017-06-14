# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:52:52 2017

@author: simon
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
        r.append(U[i]/I[i]*10**3)
    return np.array(r)

    
def func(x,a,b,c):
    return a*np.exp(b*-1.0/x)+c

#Data 1
U1p= read_from_file('Measurement0T.txt')[: ,2]
U1n= read_from_file('Measurement0T.txt')[: ,4]
I1p= read_from_file('Measurement0T.txt')[: ,1]
I1n= read_from_file('Measurement0T.txt')[: ,3]

T1= read_from_file('Measurement0T.txt')[: ,0]
r1p = resistance(U1p,I1p)
r1n = resistance(U1n,I1n)
r1 = (r1p +r1n)/2

#Data 2
U2p= read_from_file('Measurement042T.txt')[: ,2]
U2n= read_from_file('Measurement042T.txt')[: ,4]
I2p= read_from_file('Measurement042T.txt')[: ,1]
I2n= read_from_file('Measurement042T.txt')[: ,3]

T2= read_from_file('Measurement042T.txt')[: ,0]
r2p = resistance(U2p,I2p)
r2n = resistance(U2n,I2n)
r2 = (r2p +r2n)/2
#Data 3
U3p= read_from_file('Measurement07T.txt')[: ,2]
U3n= read_from_file('Measurement07T.txt')[: ,4]
I3p= read_from_file('Measurement07T.txt')[: ,1]
I3n= read_from_file('Measurement07T.txt')[: ,3]

T3= read_from_file('Measurement07T.txt')[: ,0]
r3p = resistance(U3p,I3p)
r3n = resistance(U3n,I3n)
r3 = (r3p +r3n)/2

"""
popt, pcov = curve_fit(func, T[932:1255], r[932:1255], p0=(10,10,90))
plt.plot( T[932:1255], func( T[932:1255], *popt), 'r-', label='fit')
"""


plt.plot(T1,r1 , "C0", label = "$B=0T$")
plt.plot(T2,r2, "C1", label = "$B=042T$")
plt.plot(T3,r3, "C2",label = "$B=07T$")
plt.title("Resistance of $\mathrm{YBa_{2}Cu_{3}O_{7-\delta}}$")
plt.xlabel( "Temperature[K]")
plt.ylabel( "Resistance[$\mathrm{m\Omega}$]")
plt.legend(loc=4)

plt.show()