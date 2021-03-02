# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021

@author: dorian
"""
from math import sin
from math import cos

"""
def sinus(i,SinX):
 sinx= i - ((i^3)/3)
 SinX = sinx + SinX
 return SinX

def cosinus(i,CosX):
 cosx = i-((i^2)/2)  
 CosX = cosx + CosX
 return CosX

def un(i,A):
  a = (sin(i)*sin(i))+(cos(i)*cos(i))
  A =a + A 
  return A

def pi(i)
 if i%2 != 0 :
    pi = pi + 1/i
 return pi
""" 
 
#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)
n = float(input('entrez une valeur pour n : \n '))

i = 1
N = i
SinX = 0
CosX = 0
A = 0
pi =0 
while i <= (n):
   N= N*i 
   #sin x= x-((x^3)/3 )+ ...
   sinx= i - ((i^3)/3)
   #cos x= 1-((x^2)/2 )+ ...
   cosx = 1-((i^2)/2)
   
   #1= (sin (x)^2)+(cos(x)^2)+...
   a = (sin(i)*sin(i))+(cos(i)*cos(i))
   
   SinX = sinx + SinX
   CosX = cosx + CosX
   A =a + A 
   
   # pi = 1-(1/3)+(1/5)-(1/7)+(1/9)-....

   if i%2 != 0 :
    pi = pi + 1/i
   
   i += 1
print("N= ",N)
print("sin x =", sin(SinX))
print("cos x = ", cos(CosX))
print("1= ",A)
print("pi =", pi)

#pi =4* (((-1)^i)/(2*i+1))
#p/4 = pi + 1/i 



 






   




