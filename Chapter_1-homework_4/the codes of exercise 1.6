# -*- coding: utf-8 -*-
"""
Created on Mon April 4 12:23:45 2016
   Population growth problems
@author: Luo Kaifa
"""

# Update: 201604018

# PROGRAM population_growth_problem

# Purpose: This program solves for a rate equation of the population growth problem
#                   dN/dt = aN - bN**2
# where a and b are two parameters depend on the initial population N
# We solve a rate equation rised from population problem with Euler method. 


# import the tools
from pylab import *
import numpy as py

#set the vars. and paras.
a = 0.
b = 0.
N0 = 0.
dt = 1.
time = 0.
n = 0.
c = 0.  #c is a para. rised by interger
N1 = []
N2 = []
error = []
t = []

#input the paras.
a = float(raw_input('please input the first-order coefficient a:'))
b = float(raw_input('please input the second-order coefficient b:'))
N0 = float(raw_input('please input the initial number of population N0:'))
time = float(raw_input('please input the total time of population growth:'))
dt = float(raw_input('please input the numerical step size:'))
N1.append(float(N0))
N2.append(float(N0))
t.append(0)
c = float(1-a/(b*N0))
n = int(time/dt)

# calculate the time dependence of N_A & N_B using Euler method
for i in range(n+1): 
    N1.append(N1[i]+(a*N1[i]+b*N1[i]*N1[i])*dt)
    N2.append(a/(b*(1-c*np.exp(-a*(t[0]+i*dt)))))
    error.append(N2[i]-N1[i])
    t.append(t[i]+dt)
    


figure(figsize=(14,7),dpi=80)
subplot(121)
plot(t,N1,'-r',linewidth=2,label='Simulation')
plot(t,N1,'-g',linewidth=2,label='Theory')
xlabel('time')
ylabel('number of population')
title('The population growth',fontsize=20)
legend(loc = 'best')

subplot(122)
plot(t,N1,'-r',linewidth=2,label='errors')
xlabel('time')
ylabel('difference between theory and simulation')
title('errors of this simulation',fontsize=20)
legend(loc = 'best')

savefig('population growth curve.jpg')
