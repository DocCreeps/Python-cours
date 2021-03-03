# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:08:18 2021

@author: doria
"""
from random import shuffle, randint
import matplotlib.pyplot as plt


def voisinage(x,y, largeur, hauteur) :
	
	#retourne les voisins de la case [y][x]
	
	voisins = []
	for (xx,yy) in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] :
		if 0 <= xx < largeur and 0 <= yy < hauteur :
			voisins.append((xx,yy))
	shuffle(voisins)
	return voisins

def cree_dedale(largeur, hauteur):

	# aucune cellule n'est visitée (donc elles sont toutes mises à False) :
	vu = [[False] * largeur   for _ in range(hauteur)]

	vertical = [["|  "] * largeur + ['|'] for _ in range( hauteur)]
	horizontal = [["+--"] * largeur + ['+'] for _ in range( hauteur + 1)]
    
	def on_visite(x, y):
		# on marque la cellule actuelle comme étant visitée :
		vu[y][x] = True

		# pour chaque voisine  de la cellule actuelle :
		for (xx, yy) in voisinage(x,y, largeur, hauteur) :
			# si elle est visitée, on ne fait rien :
			if vu[yy][xx]: continue
			# sinon on fait tomber le mur séparateur :
			if xx == x: horizontal[max(y, yy)][x] = "+  "
			if yy == y: vertical[y][max(x, xx)] = "   "
			# et on repart de cette nouvelle cellule :
			on_visite(xx, yy)

	# on part d'une cellule au hasard :
	on_visite( randint(0,largeur-1) , randint(0,hauteur-1) )

	# on dessine la grille :
	for i in range(hauteur) :
		print(*horizontal[i])
		print(*vertical[i])
	print(*horizontal[hauteur])

x = int(input("Largeur du labyrinthe:  "))  
y = int(input("Hauteur du labyrinthe:  ")) 

laby = cree_dedale(x,y)
plt.plot(x,y, 'r' )
plt.show()



