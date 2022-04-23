#coding:utf-8

"""
Boucles :   while / for
Mots-clés:  break (casse la boucle)
            continue (revient au début de la boucle)
"""

compteur = 0

while compteur <5:
    print("Je suis une phrase")
    compteur += 1
    
jeuLance = True
print("")

"""
Exemple de boucle infinie
"""
while jeuLance:
    #Fais des instructions en rapport avec le jeu
    choixMenu = input("> ")
    
    if choixMenu == "again":
        continue
    elif choixMenu == "quit":
        jeuLance = False
    else:
        print("Commande introuvable")

print("A bientôt")


"""
"""

phrase = "Bonjour tout le monde :) !"

for letter in phrase:
    print(letter)
    
print("A bientôt...")