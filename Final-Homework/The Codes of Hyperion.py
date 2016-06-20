# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:39:44 2016

@author: luokaifa
"""

import math
import matplotlib.pylab as plt

#两体系统的参量
M = 1       #mass of Saturn
m = 1       #mass of Hyperion
G = 4*math.pi**2/M   #gravitaional paramenter
a = 2    #the value of semimajor
e = 0.5    # the eccentricity
# Hyperion公转的运动变量，thete和omega
omega1 = []
theta1 = []
x = []
y = []
vx = []
vy = []
r = []

#设置Hyperion的初始运动参数
x.append(1)
y.append(0)
vx.append(0)
vy.append(math.sqrt(3)*math.pi)

# Hyperion自转的运动变量
omega2 = []
theta2 = []
time = []
omega2.append(0)
theta2.append(0)
time.append(0)
t=0.0001

#Hyperion 公转的描述模型
for i in range(0,100000):
    r.append(math.sqrt(x[i]*x[i]+y[i]*y[i]))
    vx.append(vx[i]-4*math.pi**2*x[i]/(r[i]*r[i]*r[i])*t)
    vy.append(vy[i]-4*math.pi**2*y[i]/(r[i]*r[i]*r[i])*t)
    x.append(x[i]+vx[i+1]*t)
    y.append(y[i]+vy[i+1]*t)
    
#Hyperion Spin的描述模型
for i in range(0,100000):
    temp_omega2 = omega2[i]-(3*G*M/(r[i]*r[i]*r[i]*r[i]*r[i]))*(x[i]*math.sin(theta2[0])-y[i]*math.cos(theta2[0]))*(x[i]*math.cos(theta2[0])+y[i]*math.sin(theta2[0]))*t
    omega2.append(temp_omega2)
    temp_theta2 = omega2[i+1]*t+theta2[i]
    theta2.append(temp_theta2)
    time.append(i*t+t)
    if theta2[i+1] > math.pi:
        theta2[i+1] = theta2[i+1]-2*math.pi
    if theta2[i+1] < -math.pi:
        theta2[i+1] = theta2[i+1]+2*math.pi
        
#绘图部分
plt.figure(figsize = [8,6])
plt.plot(time,omega2,'r')
plt.xlim(0,10)
#plt.ylim(-4,4)
plt.xlabel('time(yr)')
plt.ylabel('theta(radians)')     
plt.legend({'Circular orbit'},loc='upper center')
plt.title('Hyperion  theta versus time')
