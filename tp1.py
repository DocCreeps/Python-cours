# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:47:44 2021

@author: dorian
"""
from math import sin

#sin x= sigma((-1)^n * X^(2n +1)) / (2n+1)

n = float(input('entrez une valeur pour n : \n '))
print(n)
i = 1
N = i
X = 0
while i <= (n):
   N= N*i 
   i += 1
   x= i - ((i^2)/3)
   X = x + X

print("N = ", N)
print("X = ", X)
  
print("sin x =", sin(X))

#pi = 



   




