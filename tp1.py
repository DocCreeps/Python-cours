# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021

@author: dorian
"""
from math import sin
from math import cos

#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)

n = float(input('entrez une valeur pour n : \n '))
print(n)
i = 1
N = i
SinX = 0
CosX = 0
while i <= (n):
   N= N*i 
   i += 1
   sinx= i - ((i^3)/3)
   cosx = 1-((i^2)/2)
   SinX = sinx + SinX
   CosX = cosx + CosX
   

print("N = ", N)
print("SINX = ", SinX)
print("COSX = ", CosX)

print("sin x =", sin(SinX))
print("cos x = ", cos(CosX))

#pi = 



   




