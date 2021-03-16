# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:56:35 2021

@author: doria
"""
#import de la fonction randint de la librairie random
from numpy.random import randint
#import de la librairie matpolib
import matplotlib.pyplot as plt

#création d'une classe pile qui va servir a créée le chemin A verif
class Pile:
    #fonction qui permet initialisée une liste
    def __init__(self):
        self.lst = [] 
     #fonction qui permet  de remplire la liste
    def empty(self):
        return self.lst == [] 
     #fonction qui permet 
    def push(self, x):
        self.lst.append(x)
 #fonction qui permet d'afficher un message en cas d'erreur
    def pop(self):
        if self.empty():
            raise ValueError("pile vide") 
        return self.lst.pop()
    
#fonction qui va parcourire le laby    
def explorer(laby): 
    pile = Pile()
    pile.push((0, laby.q - 1)) 
    laby.tab[0][laby.q - 1].etat = False 
    while True:
        i, j = pile.pop()
        if i == laby.p - 1 and j == 0:
            break
        if j > 0 and laby.tab[i][j].S and laby.tab[i][j-1].etat:
            pile.push((i, j)) 
            pile.push((i, j-1)) 
            laby.tab[i][j-1].etat = False
        elif i < laby.p-1 and laby.tab[i][j].E and laby.tab[i+1][j].etat: 
            pile.push((i, j))
            pile.push((i+1, j))
            laby.tab[i+1][j].etat = False
        elif j < laby.q-1 and laby.tab[i][j].N and laby.tab[i][j+1].etat: 
            pile.push((i, j))
            pile.push((i, j+1))
            laby.tab[i][j+1].etat = False
        elif i > 0 and laby.tab[i][j].W and laby.tab[i-1][j].etat: 
            pile.push((i, j))
            pile.push((i-1, j))
            laby.tab[i-1][j].etat = False
    return pile.lst
 
   #class qui va définire les case du laby en initilisant les mur dans toute les directions et son etas a false
class Case:
    #fonction qui va permetre l'initialisation des case du laby elle prend en paramétres l'appel a l'instance de la classe
    def __init__(self):
        self.N = False 
        self.W = False 
        self.S = False 
        self.E = False 
        self.etat = False

  # class qui permet la définition d'un objet labyrinthe
class Labyrinthe:
    #fonction qui permet l'intialisation du laby qui prend en parametre l'appel a l'instance de la classe(self) une valeur p et une valeur q
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.tab = [[Case() for j in range(q)] for i in range(p)]
    #fonction qui permet d'afficher le laby qui prend en parametre l'appel a l'instance de la classe (self)
    def show(self):
        plt.plot([0, 0, self.p, self.p, 0], [0, self.q, self.q, 0, 0], linewidth=2) 
        for i in range(self.p-1):
            for j in range(self.q):
                if not self.tab[i][j].E:
                    plt.plot([i+1, i+1], [j, j+1], 'b') 
        for j in range(self.q-1):
            for i in range(self.p):
                if not self.tab[i][j].N:
                    plt.plot([i, i+1], [j+1, j+1], 'b') 
        
        plt.axis([-1, self.p+1, -1, self.q+1])
        plt.show()
        
   #fonction pour afficher la solution     
    def solution(self):
        sol = explorer(self) 
        X, Y = [], []
        for (i, j) in sol:
            X.append(i+.5)
            Y.append(j+.5) 
        X.append(self.p-.5)
        Y.append(.5)
        plt.plot(X, Y, 'r', linewidth=2) 
        self.show()
#fonction de création du laby
def creation(p, q):
    laby = Labyrinthe(p, q)
    pile = Pile()
    i, j = randint(p), randint(q) 
    pile.push((i, j)) 
    laby.tab[i][j].etat = True 
    while not pile.empty():
        i, j = pile.pop()
        v = []
        if j < q-1 and not laby.tab[i][j+1].etat:
            v.append('N')
        if i > 0 and not laby.tab[i-1][j].etat:
            v.append('W')
        if j > 0 and not laby.tab[i][j-1].etat:
            v.append('S')
        if i < p-1 and not laby.tab[i+1][j].etat:
            v.append('E') 
        if len(v) > 1:
            pile.push((i, j)) 
        if len(v) > 0:
            c = v[randint(len(v))] 
            if c == 'N':
                laby.tab[i][j].N = True
                laby.tab[i][j+1].S = True
                laby.tab[i][j+1].etat = True 
                pile.push((i, j+1))
            elif c == 'W':
                laby.tab[i][j].W = True 
                laby.tab[i-1][j].E = True 
                laby.tab[i-1][j].etat = True 
                pile.push((i-1, j))
            elif c == 'S':
                laby.tab[i][j].S = True 
                laby.tab[i][j-1].N = True 
                laby.tab[i][j-1].etat = True 
                pile.push((i, j-1))
            else:
                laby.tab[i][j].E = True 
                laby.tab[i+1][j].W = True 
                laby.tab[i+1][j].etat = True 
                pile.push((i+1, j))
    return laby


#demande a l'utilisateur de rentrez la hauteur et la largeur
La = int(input("Largeur du labyrinthe:  "))  
Ha = int(input("Hauteur du labyrinthe:  ")) 

#créée le laby
laby = creation(La,Ha ) 
#affiche la solution séléctionner 
laby.solution()
