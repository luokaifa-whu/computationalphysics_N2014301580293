# program: it will give a plot of a cosine curve
# the form of this curve is 15*cos(2*pi/30*x), it will move toward -x axisfrom 

from math import *
import time
import os

main_tab = [' '*75]*40  # the matrix that will be print
i,j,k=1,1,1             # set loop variables

while k<= 500:          # set the scale in the -x direction
    while j<=75:        # this loop make the matrix like a sine curve
        fx=int(15*cos(2*3.14/30*j+2*3.14/100*k))
        tab_temp=main_tab[20-fx-1]
        tab_temp=list(tab_temp)                 
        tab_temp[j-1]='*'
        tab_temp=''.join(tab_temp)
        main_tab[20-fx-1]=tab_temp
        j=j+1
    while i<=40:          #print the matrix
        print main_tab[i-1]
        i=i+1
    time.sleep(0.01)      
    os.system('cls')      # clear the screen
    i,j,k=1,1,k+1         # reset the loop variables
    main_tab = [' '*75]*40
