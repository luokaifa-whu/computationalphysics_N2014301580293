# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:39:44 2016

@author: luoka
"""

import math
import matplotlib.pylab as plt

#两体系统的参量
M = 1                      # mass of Saturn
m = 0.01                      # mass of Hyperion
G = 4*math.pi**2/M         # gravitaional paramenter
a = 1                      # the value of semimajor
e = 0.5                    # the eccentricity

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
vy.append(5)

# Hyperion自转的运动变量
omega2 = []
theta2 = []
time = []
omega2.append(0)
theta2.append(0)
time.append(0)
t=0.0001


#绘制李雅普诺夫指数的比较模型
com_theta2 = []
com_omega2 = []
delta_theta2 = []
com_theta2.append(0.01)
com_omega2.append(0)
delta_theta2.append(0.01)



#Hyperion 公转的描述模型
for i in range(0,100000):
    r.append(math.sqrt(x[i]*x[i]+y[i]*y[i]))
    vx.append(vx[i]-4*math.pi**2*x[i]/(r[i]*r[i]*r[i])*t)
    vy.append(vy[i]-4*math.pi**2*y[i]/(r[i]*r[i]*r[i])*t)
    x.append(x[i]+vx[i+1]*t)
    y.append(y[i]+vy[i+1]*t)
    

#Hyperion Spin的描述模型
for i in range(0,100000):
    temp_omega2 = omega2[i]-(3*G*M/(r[i]*r[i]*r[i]*r[i]*r[i]))*(x[i]*math.sin(theta2[i])-y[i]*math.cos(theta2[i]))*(x[i]*math.cos(theta2[i])+y[i]*math.sin(theta2[i]))*t
    omega2.append(temp_omega2)
    temp_theta2 = omega2[i+1]*t+theta2[i]
    theta2.append(temp_theta2)
    time.append(i*t+t)
    if theta2[i+1] > math.pi:
        theta2[i+1] = theta2[i+1]-2*math.pi
    if theta2[i+1] < -math.pi:
        theta2[i+1] = theta2[i+1]+2*math.pi


#Hperion公转轨迹的绘图部分
plt.figure(figsize = (12,16))
plt.title('Hyperion Circular orbit')
plt.subplot(2,2,1)
plt.scatter(0,0,s=200,c='red')
plt.plot(x,y,'b')
plt.xlim(-1.2,1.2)
plt.ylim(-1.2,1.2)
plt.xlabel('time(yr)')
plt.ylabel('theta(radians)')     
plt.legend({'theta versus time'},loc='upper right',fancybox="n")



#Hyperion 自转运动的绘图部分
plt.subplot(2,2,2)
#plt.figure(figsize = [8,6])
plt.plot(time,theta2,'b')
plt.xlim(0,10)
#plt.ylim(-4,4)
plt.xlabel('time(yr)')
plt.ylabel('theta(radians)')     
plt.legend({'theta versus time'},loc='upper center')

#Hyperion 自转运动的绘图部分
plt.subplot(2,2,3)
#plt.figure(figsize = [8,6])
plt.scatter(theta2,omega2,s=0.001,c='blue')
#plt.xlim(0,10)
#plt.ylim(-4,4)
plt.xlabel('theta(radians)')
plt.ylabel('omega(radians/s)')     
plt.legend({'omega versus theta'},loc='lower center')
 



#李雅普诺夫指数的模型
for i in range(0,100000):
    temp_omega2 = omega2[i]-(3*G*M/(r[i]*r[i]*r[i]*r[i]*r[i]))*(x[i]*math.sin(theta2[i])-y[i]*math.cos(theta2[i]))*(x[i]*math.cos(theta2[i])+y[i]*math.sin(theta2[i]))*t
    temp_com_omega2 = com_omega2[i]-(3*G*M/(r[i]*r[i]*r[i]*r[i]*r[i]))*(x[i]*math.sin(theta2[i])-y[i]*math.cos(theta2[i]))*(x[i]*math.cos(theta2[i])+y[i]*math.sin(theta2[i]))*t
    omega2.append(temp_omega2)
    com_omega2.append(temp_com_omega2)
    temp_theta2 = omega2[i+1]*t+theta2[i]
    temp_com_theta2 = com_omega2[i+1]*t+com_theta2[i]
    theta2.append(temp_theta2)
    com_theta2.append(temp_com_theta2)
    if theta2[i+1]>= com_theta2[i+1]:
        temp_delta_theta2 = theta2[i+1]-com_theta2[i+1]
    else: 
        temp_delta_theta2 = com_theta2[i+1]-theta2[i+1]
    delta_theta2.append(temp_delta_theta2)

#李雅普诺夫指数的绘图部分
plt.subplot(2,2,4)
#plt.figure(figsize = [8,6])
#plt.xlim(0,10)
#plt.ylim(10**(-6),0.01)
#plt.semilogy(time,delta_theta2,'y')      # x轴线性变化、y轴对数变化的坐标系
plt.plot(time,delta_theta2,'y')         # 正常的线性变化直角坐标系
plt.xlabel('time(s)')
plt.ylabel('delta_theta(radians)')     
plt.legend({'delta_theta versus time'},loc='upper center')
#plt.title('delta_theta versus time')
