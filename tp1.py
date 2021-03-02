# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021

@author: dorian
"""
from math import sin
from math import cos


def sinus(x,X):
 X=X + (x - ((x^3)/3))
 return X

def cosinus(x,X):
 X =  X +(1-((x^2)/2))
 return X


"""
def pif(n,cp, pis):
 if n%2 != 0 :
    if cp==0:
      cp+=1
      pis = pis - 1/n
      
    elif cp== 1 :
      cp=0
      pis = pis + 1/n
    
 return pis
"""

 
#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)

n = float(input('entrez une valeur pour n : \n '))

i = 1
N = i
SinX = 0
CosX = 0

pi =0
c=1
while i <= (n):
   N= N*i 
   #sin x= x-((x^3)/3 )+ ...
   SinX=sinus(i,SinX)
   CosX=cosinus(i, CosX)
   
   if i%2 != 0 :
    if c==0:
      pi = pi - 1/i
      c+=1
    elif c== 1 :
      pi = pi + 1/i
      c=0
   
   
   i += 1
A=(sin(SinX)*sin(SinX))+(cos(CosX)*cos(CosX))    
print("N= ",N)
print("sin ",SinX,"=", sin(SinX))
print("cos ",CosX, "=", cos(CosX))
print("1= ",A)
print("pi/4 =", pi)


#pi =4* (((-1)^i)/(2*i+1))
#p/4 = pi + 1/i 



 






   




