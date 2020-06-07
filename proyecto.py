#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:21:27 2020

@author: joseramos
@author: raul aguilar
@author: julio lazo

PROYECTO TEORIA ELECTROMAGNETICA


"""

import numpy as np


import matplotlib.pyplot as plt

from matplotlib import cm


color = cm.gray

"""
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict
from mpl_toolkits.mplot3d import axes3d


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

# Make the direction data for the arrows
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

plt.ion()

plt.show()

"""


"""La pregunta 3.1 """

sin = np.sin
pi = np.pi
arctan = np.arctan
sinh = np.sinh

a = 3

b = a*1.5

dx = 0.01

x = np.arange(0,a,dx)

y = np.linspace(0,b,len(x))

def cn(n):
    f = []
    for i in y:
        s = (sin(n*pi/b*i))
        f.append(s*arctan(i/a))
    t = sinh(n*pi*a/b)
    I = np.trapz(f)
    I = I*2/b
    I = I/t
    return I

n = [3,6,11,21]

def V(x,y,n):
    v = np.zeros((len(x),len(x)))
    for k in range(1,n):
        c = cn(k)
        r = 0
        s = 0
        for i in x:
            for j in y:
                v[s][r] += c*sin(k*pi*j/b)*sinh(k*pi*i/b)
                s += 1
            r += 1
            s = 0
    return v

v = V(x,y,n[0])

#x,y = np.meshgrid(x,y)

plt.figure(0)
plt.title('Potencial, con n = '+str(n[0]-1))
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = color)
plt.show()

v = V(x,y,n[1])

plt.figure(1)
plt.title('Potencial, con n = '+str(n[1]-1))
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = color)
plt.show()

v = V(x,y,n[2])

plt.figure(2)
plt.title('Potencial, con n = '+str(n[2]-1))
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = color)
plt.show()

v = V(x,y,n[3])

plt.figure(3)
plt.title('Potencial, con n = '+str(n[3]-1))
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = color)
plt.show()