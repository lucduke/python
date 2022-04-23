#coding:utf-8

"""
Fonction avec arguments obligatoires :         def nomFonction(arg1, arg2):

Fonction avec arguments optionnels :           def nomFonction(arg1, arg2 = "toto"):

Fonction avec arguments infinis :                   def nomFonction(*arg1):

Fonctions avec retour :                                 def nomFonction(arg1, arg2):
                                                                        return arg2

"""

def lePlusGrandNombre(nombre1, nombre2=100):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "EGALITE !"

print(lePlusGrandNombre(110))
