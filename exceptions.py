#coding:utf-8

"""
Gérer les exceptions :  try/except (+else, finally)
                        on prut déclarer plusieurs exceptions avec leur type
                        
Types d'exceptions :    ValueError
                        NameError
                        TypeError
                        ZeroDivisionError
                        OSError
                        AssertionError
"""

try: #on teste
    ageUtilisateur = int(ageUtilisateur)
except: #en cas d'erreur
    print("L'âge indiqué est incorrect")
else: #si pas d'erreur
    Print("tu as", ageUtilisateur), "ans")
finally: #dans tous les cas
    print("FIN DU PROGRAMME")
    
try:
    age = input("Quel âge as-tu ?")
    age = int(age)
    
    assert age > 25 #je veux que age soit plus grand que 25
except AssertionError:
    print("J'ai attrapé l'exception")
