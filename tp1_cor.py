# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:03:51 2021

@author: Dorian
"""
import math

X = math.radians(float(input("Angle:\n")))
Sinus, Cosinus, PiSur4 = 0, 0, 0

for n in range(7):
    Sinus += (-1) ** n * X ** (2 * n + 1) / math.factorial(2 * n + 1)

for m in range(7):
    Cosinus += (-1) ** m * X ** (2 * m) / math.factorial(2 * m)

for o in range(50000):
    PiSur4 += ((-1)**o / (2*o + 1)) * 4

print("sinus", Sinus)
print("cosinus", Cosinus)
print("pi", PiSur4)
print("pi", math.pi)
