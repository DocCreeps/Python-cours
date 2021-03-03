# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:17:12 2021

@author: dorian
"""
import time
import numpy as np
import matplotlib.pyplot as plt
for i in range(30):
    x = np.linspace(0, 2*np.pi, i)
    y = np.cos(x)
    plt.plot(x, y)
    plt.show() # affiche la figure a l'ecran
    time.sleep(1)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  
# Fonction pour la 3D
import numpy as np

# Tableau pour les 3 axes
# Création d'un tableau de 100 points entre -4*pi et 4*pi
for i in range(100) :
    theta = np.linspace(-4 * np.pi, 4 * np.pi, i)
    z = np.linspace(-2, 2, i)  # Création du tableau de l'axe z entre -2 et 2
    r = z**2 + 1
    x = r * np.sin(theta)  # Création du tableau de l'axe x
    y = r * np.cos(theta)  # Création du tableau de l'axe y

# Tracé du résultat en 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # Affichage en 3D
    ax.plot(x, y, z, label='Courbe')  # Tracé de la courbe 3D
    plt.title("Courbe 3D")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()
    time.sleep(0.5)
