# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:21:48 2016

@author: luokaifa
"""

import matplotlib.pyplot as plt


#设置变量及其初值
delta = 10
b = 8./3.
r = 25  #the measures of the temperature difference across the fluid and other parameters.
t = 0.0001   #the footsize


#set the lists
x = []
y = []
z = []
time = []
x.append(1.0)
y.append(0)
z.append(1.0)
display_x=[]
display_y=[]
display_z=[]
time.append(0.0)

#set the loop
for i in range(0,500000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    if t*i > 30:
        display_x.append(x[i+1])
        display_y.append(y[i+1])
        display_z.append(y[i+1])
    time.append(t*i+t)
plt.plot(display_y,display_z,'r')
plt.ylim(0,50)
plt.xlim(-30,30)
plt.xlabel('x')
plt.ylabel('Y')
plt.title('Phase space plot,r=25')
plt.legend({'Y versus X,after t=30s'},loc='upper center')
