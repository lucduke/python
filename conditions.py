#coding:utf-8

"""
Opérateurs de comparaison :     == (égal à)
                                != (différent de)
                                < (plus petit que)
                                > (plus grand que)
                                <= (plus petit ou égal à)
                                >= (plus grand ou égal à)

Mots clefs de condition :       if / elif / else

Conditions multiples :          and (ET)
                                or (OU, L'UN OU L'AUTRE)
                                in / not in (DANS / PAS DANS)
                                
age > 0 ET age <= 100 --> 0 < age <= 100
"""

identifiant = "christophe"
motDePasse = "password123"

print("Interface de connection")

userId = input("Entrer votre identifiant : ")
userPassword = input("Entrer votre mot de passe :")

if userPassword == motDePasse and userId == identifiant:
    print("Vous êtes connectés, bienvenue", userId)

print("On n'est plus dans la condition if")

lettreHasard = "a"

if lettreHasard in "aeuo":
    print("C'est une voyelle")
elif lettreHasard == "y":
    print("C'est une voyelle")
elif lettreHasard == "i":
    print("C'est une voyelle")
else:
    print("C'est une consonne")

jeuCharge = True

if jeuCharge:
    print("Le jeu est en marche")
else:
    print("Le jeu n'est pas lancé")

if not jeuCharge:
    print("Le jeu n'est pas lancé")
else:
    print("Le jeu est en marche")