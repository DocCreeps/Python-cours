# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:25:21 2021

@author: dorian
"""
import time
import numpy as np
import matplotlib.pyplot as plt
#Soit Y = -2X^2 + 4X+ 2
# tracer la courbe 

r=float(input('entrez une valeur pour le nombre de fin : \n '))
for i in range(int(r)):
    #x= np.lindpace(deb,fin,nbdepoint)
    x = np.linspace(0, r, i)
    y = (-2*(x)**2) + (4*x)+2

    plt.plot(x,y)
    plt.show() # affiche la figure a l'ecran
    time.sleep(1)
