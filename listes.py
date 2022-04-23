# coding:utf-8

# Création d'une liste
inventaire = list()
inventaire = []
inventaire = [1, 6, 15]
inventaire = [0] * 10 # pour initialiser la liste avec 10 fois le même élément

# Afficher les éléments d'une liste
"""
liste[X]    --> affiche élément d'indice X
liste[-X]   --> affiche Xème élément en partant de la fin X

liste[:]    --> affiche tous les éléments 
liste[:X]   --> affiche les X premiers éléments
liste[X:]   --> affiche les X derniers éléments
liste[X:Y]   --> affiche les éléments d'indice X jusqu'à l'indice Y (exclus)

len(<list>) --> retourne le nombre d'élément d'une liste
"""

inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
print(inventaire[1]) # pour afficher épée
print(inventaire[:]) # pour afficher toute la liste
print(inventaire[:2]) # pour afficher les deux premiers éléments de la liste
print(inventaire[2:]) # pour afficher les deux derniers éléments de la liste
print(inventaire[-1]) # pour afficher le dernier élément

# Parcourir une liste
# Avec une boucle while
inventaire = range(20)
i = 0
while i < len(inventaire):
    print(inventaire[i])
    i += 1

for valeur in inventaire:
    print(valeur)

# Modifier un élément d'une liste
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
inventaire[1] = 'manteau'
inventaire[:2] = ['manteau','gourde']

# Rechercher un élément dans une liste
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
if 'bouclier' in inventaire:
    print("J'ai un bouclier")
else:
    print("Je n'en ai pas")

# Ajouter des éléments dans une liste
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
inventaire.append('gourde')
inventaire.insert(1,'jean')

# Supprimer des éléments dans une liste
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
inventaire.remove('bouclier')
del inventaire[2]

# Récupérer l'index d'une valeur
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
inventaire.index('potion')

# Trier une liste
inventaire = ['arc','épée','bouclier','potion','flêche','tunique']
inventaire.sort()
inventaire.reverse()

# Compter dans une liste
inventaire = ['arc','épée','bouclier','arc','potion','flêche','tunique']
inventaire.count('arc')

# Copîer une liste
liste2 = inventaire.copy()
liste2.append('toto')

# Etendre une liste avec une autre liste
liste1 = ['arc','bouclier','tunique']
liste2 = ['potion','flêche']
liste1.extend(liste2)

# Enumerer une liste sous forme de tuple
liste1 = ['arc','bouclier','tunique']
for key, value in enumerate(liste1):
    print('Element indice {} --> valeur {}'.format(key,value))
