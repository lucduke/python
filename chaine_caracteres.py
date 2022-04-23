#coding:utf-8

"""
Classe str			: string (chaines de caractères)
Méthode associée	: str.upper(), str.lower(), str.capitalize(), str.title()
					: str.center(<largeur>, [caractere_remplissage]) #[] argument optionnel
					: str.find(<chaine>, [debut], [fin])
					: str.index(<chaine>, [debut], [fin])
					: str.strip() #enleve les espaces après le tout premier mot et le dernier
					: str.replace(<ancienne>, <nouvelle>, [occurences])
					: str.split(<caractère>) #permet de découper une chaine de caractère et de renvoyer le résultat dans une liste
					: str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric(, str.isalphanum()
					: str.islower(), str.isupper()
					: str.isidentifier(), str.iskeyword()

Pour afficher aide 	: help(<classe>)

"""
ma_chaine = "Bonjour tout le monde"

ma_chaine1 = ma_chaine.upper()
print(ma_chaine1)

ma_chaine1 = ma_chaine.lower()
print(ma_chaine1)

ma_chaine1 = ma_chaine.capitalize()
print(ma_chaine1)

ma_chaine1 = ma_chaine.title()
print(ma_chaine1)

ma_chaine1 = ma_chaine.center(50, "-")
print(ma_chaine1)

print(ma_chaine.find("Super")) #va renvoyer -1 car Super n'est pas dans ma chaine de caractères
print(ma_chaine.find("tout")) #va renvoyer la position où "tout" apparait

try:
	print(ma_chaine.index("Super"))
except ValueError:
	print("Je n'ai pas trouvé")

print(ma_chaine.index("tout")) #va renvoyer -1 car Super n'est pas dans ma chaine de caractères

ma_chaine = "   Bonjour tout le monde   "
print(ma_chaine.strip())

print(ma_chaine.replace("o","a"))
print(ma_chaine.replace("o","a",1))

print(ma_chaine.split(" "))

ch = "Le language Python"

if "language" in ch:
	print("Touvé")
else:
	print("Non trouvé")