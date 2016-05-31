# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:42:04 2016

@author: luokaifa
"""


import math     # import packages
import matplotlib.pyplot as plt

#设置变量及其初值
q=0.0
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
for i in range(0,1000):
    temp_omega = omega[i]-g/l*math.sin(theta[i])*(t*i)
    omega.append(temp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    theta.append(temp_theta)
    t_theta.append(t*i)
    
#绘图部分
plt.figure(figsize = [10,6])
plt.plot(theta,omega, 'r')           #这里是绘制的相位图
plt.ylabel('omega(radians/s)')
plt.xlabel('theta(radians)')      
plt.ylim(-20,20)
plt.title('The Nonlinear Pendulum')
