#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:13:30 2020

@author: joseramos
"""


import numpy as np


import matplotlib.pyplot as plt

from matplotlib import cm

pi = np.pi
sin = np.sin

x = np.arange(0,2*np.pi,0.1)

y = np.arange(0,2*pi,0.1)

s=0
r=0
v = np.zeros((len(x),len(x)))
for i in x:
    for j in y:
        v[s][r] += sin(j)
        s += 1
    r += 1
    s = 0
    
plt.figure(0)
plt.title('Potencial, con n = ')
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = cm.gray)
plt.show()

v = v.T
plt.figure(1)
plt.title('Potencial,')
plt.xlabel('X')
plt.ylabel('Y')
plt.pcolormesh(x,y,v,cmap = cm.gray)
plt.show()