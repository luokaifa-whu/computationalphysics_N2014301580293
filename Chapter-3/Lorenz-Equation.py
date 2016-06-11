# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:21:48 2016

@author: luokaifa
"""

import matplotlib.pyplot as plt


#设置变量及其初值
delta = 10
b = 8./3.
r = 5  #the measures of the temperature difference across the fluid and other parameters.
t = 0.0001   #the footsize


#set the lists
x = []
y = []
z = []
time = []
x.append(1.0)
y.append(0)
z.append(0)
time.append(0.0)

#set the loop
for i in range(0,500000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)
plt.plot(time,y,label='r=5')

r=10
x = []
y = []
z = []
time = []
x.append(1.0)
y.append(0)
z.append(0)
time.append(0.0)
for i in range(0,500000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)
plt.plot(time,y,label='r=10')

r=25
x = []
y = []
z = []
time = []
x.append(1.0)
y.append(0)
z.append(0)
time.append(0.0)
for i in range(0,500000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)
plt.plot(time,y,label='r=25')


#plt.ylim()
plt.xlim(0,50)
plt.xlabel('time(s)')
plt.ylabel('y')
plt.title('Lorenz model y versus time')
plt.legend(loc='upper left')
