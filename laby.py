# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:35:29 2021

@author: dorian
"""
import random
import matplotlib.pyplot as plt

#demande des valeur pour la hauteur et largeur du labyrinthe
x = int(input("Largeur du labyrinthe:  "))  
y = int(input("Hauteur du labyrinthe:  ")) 
South = 0 
East = 1 
North = 2 
West = 3 
direction = 3

def generate(x,y):
    lab= [['-' for i in range(x)]for h in range(y)]
    
    return lab





laby = generate(x, y)

print (laby)

# le graphique:
plt.show(laby)
# on cache les graduations:
plt.xticks([])
plt.yticks([])
