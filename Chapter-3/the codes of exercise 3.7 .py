# -*- coding: utf-8 -*-
"""
Created on Sun May 29 10:42:04 2016

@author: luokaifa
"""


import math     # import packages
import matplotlib.pyplot as plt

#设置变量及其初值
q=1.0
Omega_D=2.0
F_D=0.2
g=9.8
l=1.0
i = 0.1
t = 0.001    #t为步长！
temp_omega = 0.
temp_theta = 0.

#设置数组
theta = []
omega = []
t_theta = []
theta.append(0.2)
omega.append(0.0)
t_theta.append(0.0)


#循环，也就是差分方程
for i in range(0,20000):
    temp_omega = (-g/l*theta[i]-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t+omega[i]
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)
    
#绘图部分
plt.subplot(2,2,1)
plt.plot(t_theta,omega, 'g')
plt.ylabel('theta(radians)')
plt.xlabel('time(s)')
plt.title('Different driving frequency')
plt.legend('2.0',fontsize='small',loc='lower center')

#Omega 为共振频率
Omega_D= math.sqrt(9.8-0.25)
theta = []
omega = []
t_theta = []
theta.append(0.2)
omega.append(0.0)
t_theta.append(0.0)
for i in range(0,20000):
    temp_omega = (-g/l*theta[i]-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t+omega[i]
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)
    
plt.subplot(2,2,2)
plt.plot(t_theta,omega, 'k')
plt.legend('resonance',fontsize='small',loc='lower center')

#Omega 为4.0
Omega_D= 4.0
theta = []
omega = []
t_theta = []
theta.append(0.2)
omega.append(0.0)
t_theta.append(0.0)
for i in range(0,20000):
    temp_omega = (-g/l*theta[i]-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t+omega[i]
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)

plt.subplot(2,2,3)
plt.plot(t_theta,omega, 'r')
plt.legend('4.0',fontsize='small',loc='lower center')

#Omega 为10.0
Omega_D= 10.0
theta = []
omega = []
t_theta = []
theta.append(0.2)
omega.append(0.0)
t_theta.append(0.0)
for i in range(0,20000):
    temp_omega = (-g/l*theta[i]-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t+omega[i]
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)


plt.subplot(2,2,4)
plt.plot(t_theta,omega, 'm')
plt.legend('10.0',fontsize='small',loc='lower center')
