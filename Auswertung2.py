# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:48:54 2017

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funktionen

def read_from_file(filename):                   #Liest Daten ein
    return np.loadtxt(filename, skiprows=1)


def resistance(U,I):
    r = []
    for i in range(len(U)):
        r.append(U[i]*10**3/I[i])
    return np.array(r)


x3v = read_from_file('Messung07T.txt')[: ,0]
x3n = read_from_file('Messung07T.txt')[: ,5]
x3= (np.array(x3v)+np.array(x3n))*0.5

U3p= read_from_file('Messung07T.txt')[: ,2]
U3n= read_from_file('Messung07T.txt')[: ,4]
I3p= read_from_file('Messung07T.txt')[: ,1]
I3n= read_from_file('Messung07T.txt')[: ,3]

r3p= resistance(U3p,I3p)
r3n= resistance(U3n,I3n)

r3= (r3p+r3n)/2


plt.plot(x3,r3,'green',label='Average resistance')
plt.plot(x3,r3p,'orange',label='Resistance in positive direction')
plt.plot(x3,r3n,'blue',label='Resistance in negative direction')
plt.xlabel('Temperature [K]')
plt.ylabel('Resistance [m$\Omega$]')
plt.legend(loc=4)
plt.show()