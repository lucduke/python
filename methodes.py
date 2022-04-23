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
    lieu_habitation = "Terre"
    
    def __init__(self, c_nom, c_age=1):
        print("Création d'un humain...")
        self.nom = c_nom
        self.age = c_age
        Humain.humain_crees += 1
        
    def parler(self, c_message): #self = méthode standard
        print("{} a dit : {}".format(self.nom, c_message))
        return c_message
        
    def changer_planete(cls, c_nouvelle_planete): #cls = méthode de classe
        Humain.lieu_habitation = c_nouvelle_planete
        
    changer_planete = classmethod(changer_planete)
    
    def definition():
        print("L'Humain est classé comme l'être le plus civilisé")
    
    definition = staticmethod(definition)

print("Lancement du programme")

Humain.definition()
 
h1 = Humain("Jojo")
print("Nom de h1 : {}".format(h1.nom))
print("Age de h1 : {}".format(h1.age))
print("Nombre d'humain : {}".format(Humain.humain_crees))

h1.parler("Bonjour à tous")
resultat = h1.parler("Comment allez vous ?")

print("Planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planète actuelle : {}".format(Humain.lieu_habitation))
