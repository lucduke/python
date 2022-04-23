#coding:utf-8

"""
Classe              : plan de conception, genre (ex : humain)
Objet               : instance de classe (ex : Julien)

Attribut            : variable de classe (ex : prénom, âge, sexe, taille ...)
Propriété           : manière de manipuler les attributs (lecture seule, accès non autorisé en dehors de la classe, ...)
					  principe d'encapsulation

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
    
    def __init__(self, c_nom, c_age):
        print("Création d'un humain...")
        self.nom = c_nom
        self._age = c_age

    def _getage(self):
    	if self._age <= 1:
    		return str(self._age) + " an"
    	else:
    		return str(self._age) + " ans"

    def _setage(self, nouvel_age):
    	if nouvel_age < 0:
    		self._age = 0
    	else:
    		self._age = nouvel_age

    # property(<getter>, <setter>, <deleter>, <helper>)
    age = property(_getage, _setage)


print("Lancement du programme")

h1 = Humain("Jojo", 45)
print("{} a {}".format(h1.nom, h1.age))

h1.age = -1
print("{} a {}".format(h1.nom, h1.age))

h1.age = 41
print("{} a {}".format(h1.nom, h1.age))
