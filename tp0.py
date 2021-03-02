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

#correction

import math



def carre(x): #calcule le carré
 return x*x;



def delta(a, b, c): #calcule delta
 return (carre(b)-(4*a*c))



a= float(input("Entrez a :\n")) #demande un paramettre en entrée
b= float(input("Entrez b :\n"))
c= float(input("Entrez c :\n"))



d = float(delta(a, b, c)) # affecte le resultat de la fonction delta a d en le castant en float



print ("Delta egal : ", d)



if d > 0 :
 rd = math.sqrt(d) # affecte la racine carré de delta a rd
 x = (-b-rd)/(2*a)
 y = (-b+rd)/(2*a)
 print (" donc supérieur a 0, donc la solution est soit ", x,", soit ", y)
if d < 0 :
 print (" donc inférieur a 0, donc n'a pas de solution dans les réels.")
if d == 0 :
 x = -b/(2*a)
 print (" donc égal a 0, donc la solution est ",x)

#fin correction

    
    
    
    


