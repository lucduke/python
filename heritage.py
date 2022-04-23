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

Fonctions utiles	:
		isinstance(<objet>, <classe>)				: vérifie qu'un objet est de la classe renseignée
		issubclasse(<classe fille>, <classe mère>)	: vérifie qu'une classe est une classe fille d'une autre                   
"""

class Vehicule:
    """
    Classe mère des véhicules
    """
    
    def __init__(self, c_nom, c_quantite_essence):
        self.nom = c_nom
        self.quantite_essence = c_quantite_essence

    def se_deplacer(self):
    	print("Le véhicule {} se déplace ...".format(self.nom))


class Voiture(Vehicule):
    """
    Classe fille des voitures
    Il est possible de faire une classe fille d'une classe fille
    On peut redéfinir, si on le souhaite, une méthode (cf. exemple avec se_deplacer)
    On peut également avoir des héritages multiples
    """
    def __init__(self, c_nom_voiture, c_quantite_essence, c_puissance):
    	Vehicule.__init__(self, c_nom_voiture, c_quantite_essence)
    	self.puissance = c_puissance

    def se_deplacer(self):
    	print("La voiture {} se déplace ...".format(self.nom))


print("Lancement du programme")
 
v1 = Vehicule("F22 Raptor", 2400)
v1.se_deplacer()
print(isinstance(v1, Vehicule))
print(isinstance(v1, Voiture))


v2 = Voiture("Toyota Supra", 90, 420)
v2.se_deplacer()
print(v2.puissance, "CH")
print(isinstance(v2, Vehicule))
print(isinstance(v2, Voiture))

print(issubclass(Voiture, Vehicule))
