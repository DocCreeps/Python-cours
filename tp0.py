# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:35:44 2021

@author: Dorian
"""
from math import sqrt

#soit une équation ax2 + bx +c 
a = float(input('entrez une valeur pour a : \n '))
b = float(input('entrez une valeur pour b : \n '))
c = float(input('entrez une valeur pour c : \n '))

#calcul de delta
delta = b*b - 4 * a * c
print("delta ", delta)
#si delta inférieur a 0
if delta <0:
 print("Pas de solutions")
 #si delta égale 0
if delta ==0:
 print("Une solution pour x") 
 #calcul X
 x=-b/2*a 
 print("X= ",x)
    
#si delta supérieur 0
if delta >0:
  print("deux solution pour x")
  #calcul racine de delta
  racinedelta = sqrt(delta)
  #calcul X1
  x1 = b - racinedelta/2*a
  #calcul X2
  x2 = b + racinedelta/2*a
  print("X1= ", x1)
  print("X2= ",x2)
  
  
print("fin du programme avec delta ")

    
    
    
    


