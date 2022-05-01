# Les dictionnaires

C'est un système de tableau associatif (clef --> valeur)



## Créer un dictionnaire

```python
dico = {} #Vide
dico = {key1:value1, key2:value2}
```



## Accéder à une valeur d'un dictionnaire

```python
dico = {key:value}
dico[key]
```

<u>Exemple</u>

```python
dico = {"name":"Jason"}
print(dico["name"])
```



## Ajouter une valeur au dictionnaire

```python
dico[key2] = value2
```

<u>Exemple</u>

```python
dico = {"nom":"Bourne"}
print(dico["nom"])
dico["prenom"] = "Jason"
print(dico["prenom"])
```



## Supprimer une valeur du dictionnaire

```python
dico.pop(key)
del dico[key]
```

<u>Exemple</u>

```python
dico = {"nom":"Bourne", "prenom":"Jason"}
print(dico)

valeur_supprimee = dico.pop("prenom")
print(valeur_supprimee)
```



## Vérifier la présence d'une clef dans un dictionnaire

```python
dico = {"nom":"Bourne", "prenom":"Jason"}
if "prenom" in dico:
    print("OK")
else:
    print("NOK")
```



## Parcourir un dictionnaire

```python
dico = {"nom":"Bourne", "prenom":"Jason"}

for key in dico:
    print(key)

for key in dico.keys():
    print(key)
```

```python
dico = {"nom":"Bourne", "prenom":"Jason"}

for value in dico.values():
    print(value)
```

```python
dico = {"nom":"Bourne", "prenom":"Jason"}

for k, v in dico.items():
    print("Clé: {} - Valeur: {}".format(k, v))
```

