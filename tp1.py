# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021
@author: Dorian
"""
import math
"""
#function qui calcul le X pour le sin
def sinus(x,X):
 X=X + (x - ((x^3)/3))
 return X
#function qui calcul le X pour le cos
def cosinus(x,X):
 X =  X +(1-((x^2)/2))
 return X
"""
n = math.radians(float(input('entrez une valeur pour l\'angle n : \n ')))
SinX, CosX, pi4, pi= 0,0,0,0


   #sin x= x-((x^3)/3 )+ ...
#SinX= sinus(n,SinX)
   #cos 1 – ((x^2)/2!) + ...
#CosX= cosinus(n,CosX)   

c,t=1,1


for i in range(5000):   
   #p/4 = pi + 1/i
   if i%2 != 0 :
    if c==0:
      pi4 = pi4 - 1/i
      c+=1
    elif c== 1 :
      pi4 = pi4 + 1/i
      c=0 
   
   i += 1
   
#pi =4* sigma (((-1)^i)/(2*i+1))
   
for o in range(50000):
    pi += ((-1)**o / (2*o + 1)) * 4  
   #1= (sin(x)^2)+ (cos(x)^2)
A=(math.sin(SinX)**2)+(math.cos(CosX)**2)

#affichage des résultats    

print("sin ",SinX)
print("cos ",CosX)
print("1= ",A)
print("pi/4 =", pi4)
print("pi = ", pi)
#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)




 






   




