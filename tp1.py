# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021
@author: Dorian
"""
import math

n = math.radians(float(input('entrez une valeur pour l\'angle n : \n ')))
SinX, CosX, pi4, pi= 0,0,0,0

for x in range(9):
 SinX += (-1) ** x * n ** (2 * x + 1) / math.factorial(2 * x + 1)

for y in range(9):
 CosX += (-1) ** y * n ** (2 * y) / math.factorial(2 * y)

c,t=1,1

nbtour = int(input('entrez un nombre de tours : '))

#pi =4* sigma (((-1)^i)/(2*i+1))

for p in range(nbtour):
    pi += ((-1)**p / (2*p + 1)) * 4  

#1= (sin(x)^2)+ (cos(x)^2)
A=(math.sin(SinX)**2)+(math.cos(CosX)**2)

#affichage des résultats    

print("sin x= ",SinX)
print("cos x= ",CosX)
print("1= ",A)

print("pi = ", pi)
print("valeur exacte de pi = ", math.pi)
#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)




 






   




