# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:42:35 2021

@author: doria
"""


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
