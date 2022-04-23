#coding:utf-8

"""
Classe              : plan de conception, genre (ex : humain)
Objet               : instance de classe (ex : Julien)

Attribut            : variable de classe (ex : prénom, âge, sexe, taille ...)
Propriété           : manière de manipuler les attributs (lecture seule, accès non autorisé en dehors de la classe, ...)

Méthode             : fonction d'une classe (ex : manger, marcher, parler, dormir, mourir) 
Méthode de classe   : fonction d'une classe (explication à venir plus tard)
Méthode statique    : fonction d'une classe, mais indépendante de celle-ci

Héritage            : classe fille qui hérite d'une classe mère (Fille est une sorte de mère)
                    : classe chat hérite de la classe animal (chat est une sorte d'animal)
"""

class Humain:
    """
    Classe des êtres humain
    """
    
    humain_crees = 0
    
    def __init__(self, c_prenom, c_age=1):
        print("Création d'un humain...")
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_crees += 1

print("Lancement du programme")
 
h1 = Humain("Jojo")
print("Prénom de h1 : {}".format(h1.prenom))
print("Age de h1 : {}".format(h1.age))
print("Nombre d'humain : {}".format(Humain.humain_crees))

h1.prenom = "Jaja"
print("Prénom de h1 : {}".format(h1.prenom))

h2 = Humain("Toto", 10)
print("Prénom de h2 : {}".format(h2.prenom))
print("Age de h2 : {}".format(h2.age))
print("Nombre d'humain : {}".format(Humain.humain_crees))