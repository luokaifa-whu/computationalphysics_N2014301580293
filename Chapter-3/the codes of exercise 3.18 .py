# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:01:08 2016

@author: luokaifa
"""


import math     # import packages
import matplotlib.pyplot as plt

#设置变量及其初值
q=0.5
Omega_D=2.0/3.0
F_D=1.2
g=9.8
l=9.8
t = 0.04    #t为步长！
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
for i in range(0,2400):
    temp_omega = omega[i]+(-g/l*math.sin(theta[i])-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)
    if theta[i+1] > math.pi:
        theta[i+1] = theta[i+1] - 2*math.pi
    if theta[i+1] < -math.pi:
        theta[i+1] = theta[i+1] + 2*math.pi
    
#绘图部分
plt.figure(figsize = [8,6])
plt.plot(theta,omega, 'r')           #这里是绘制的相位图
plt.xlabel('theta(radians)')
plt.ylabel('omega(radians/s)')     
#plt.ylim(-12,12) 
plt.legend({'omega versus theta  F_D=0.5'},loc='upper center')
plt.title('The Realistic Pendulum')
