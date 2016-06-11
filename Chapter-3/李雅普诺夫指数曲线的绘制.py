# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 07:41:30 2016

@author: luoka
"""

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
F_D=50.0
g=9.8
l=9.8
t = 0.001   #t为步长！
temp_omega = 0.
temp_theta = 0.

#设置数组
theta = []
com_theta = []     #set  the list of  comparing pendulum
com_omega = []
omega = []
t_theta = []
delta = []       # the errors of two thetas
theta.append(0.2)
omega.append(0.0)
com_theta.append(0.199)    #the pendulum for comparing
com_omega.append(0.0)
delta.append(0.001)
t_theta.append(0.0)
log = []
log.append(0.001)
t_log = []
t_log.append(0.0)

#循环，也就是差分方程
for i in range(0,140000):
    temp_omega = omega[i]+(-g/l*math.sin(theta[i])-q*omega[i]+F_D*math.sin(Omega_D*t*i))*t
    comtemp_omega = com_omega[i]+(-g/l*math.sin(com_theta[i])-q*com_omega[i]+F_D*math.sin(Omega_D*t*i))*t
    omega.append(temp_omega)
    com_omega.append(comtemp_omega)
    temp_theta = omega[i+1]*t+theta[i]
    comtemp_theta = com_omega[i+1]*t+com_theta[i]
    theta.append(temp_theta)
    com_theta.append(comtemp_theta)
    if theta[i+1]>= com_theta[i+1]:
        temp_delta = theta[i+1]-com_theta[i+1]
    else: 
        temp_delta = com_theta[i+1]-theta[i+1]
    delta.append(temp_delta)
    t_theta.append(t*(i+1))
    

#绘图部分
plt.figure(figsize = [7,6])
plt.xlim(0,150)
plt.ylim(10**(-6),0.01)
plt.semilogy(t_theta,delta,'r')   #绘制图像
#plt.semilogy(t_log,log)
plt.xlabel('time(s)')
plt.ylabel('delta_theta(radians)')     
plt.legend({'delta_omega versus time  F_D=50.0'},loc='upper right')
plt.title('The Predictable Realistic Pendulum')
