# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:21:48 2016

@author: luokaifa
"""

import matplotlib.pyplot as plt


#设置变量及其初值
delta = 10
b = 8./3.  #the measures of the temperature difference across the fluid and other parameters.
t = 0.0001   #the footsize


r = 350
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
for i in range(0,300000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)

#plt.figure(figsize=())
plt.plot(time,z,'r')
plt.legend({'r=350'})
plt.title('Phase space plot,r is large enough')

"""
r = 163
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
for i in range(0,300000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)

#plt.figure(figsize=())
plt.subplot(2,2,1)
plt.plot(time,z,'r')
plt.legend({'r=163'})
plt.title('Phase space plot,r>=163')

r = 170
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
for i in range(0,300000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)

plt.subplot(2,2,2)
plt.plot(time,z,'b')
plt.legend({'r=170'})

r = 185
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
for i in range(0,300000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)

plt.subplot(2,2,3)
plt.plot(time,z,'g')
plt.legend({'r=185'})


r = 200
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
for i in range(0,300000):
    x.append(delta*(y[i]-x[i])*t+x[i])
    y.append((-x[i+1]*z[i]+r*x[i+1]-y[i])*t+y[i])
    z.append((x[i+1]*y[i+1]-b*z[i])*t+z[i])
    time.append(t*i+t)

plt.subplot(2,2,4)
plt.plot(time,z,'y')
plt.legend({'r=200'})
#plt.ylim(0,50)
plt.xlim(0,30)
"""
