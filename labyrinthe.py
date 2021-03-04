# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:08:18 2021

@author: doria
"""
from random import shuffle, randint
import matplotlib.pyplot as plt

#retourne les cases adjacente [y][x]

def adja(x,y, largeur, hauteur) :
	
	voisins = []
	for (xx,yy) in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] :
		if 0 <= xx < largeur and 0 <= yy < hauteur :
			voisins.append((xx,yy))
	shuffle(voisins)
	return voisins

#générations du laby
def generate(largeur, hauteur):
	# aucune cellule n'est visitée (donc elles sont toutes mises à False) :
	vu = [[False] * largeur   for _ in range(hauteur)]

	verti = [["|  "] * largeur + ['|'] for _ in range( hauteur)]
	hori = [["+--"] * largeur + ['+'] for _ in range( hauteur + 1)]
    
	def visit(x, y):
		# on marque la cellule actuelle comme étant visitée :
		vu[y][x] = True

		# pour chaque case adjacente  de la cellule actuelle :
		for (xx, yy) in adja(x,y, largeur, hauteur) :
			# si deja connecter, on ne fait rien :
			if vu[yy][xx]: continue
			# sinon on fait tomber le mur séparateur :
			if xx == x: hori[max(y, yy)][x] = "+  "
			if yy == y: verti[y][max(x, xx)] = "   "
			# et on continue avec cette cellule:
			visit(xx, yy)    
	# définie une entrée et une sortie:
	visit( randint(0,largeur-1) , randint(0,hauteur-1) )
    
    
	# on dessine la grille :
	for i in range(hauteur) :
        
		print(*hori[i])
		print(*verti[i])
        
	print(*hori[hauteur])
   
     
    
Largeur = int(input("Largeur du labyrinthe:  "))  
Hauteur = int(input("Hauteur du labyrinthe:  ")) 

laby = generate(Largeur,Hauteur)
print(laby)





