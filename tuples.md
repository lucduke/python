# Les tuples


(!) Tuple : conteneur immuable (dont on ne peut modifier les valeurs)



## Créer un tuple

```python
mon_tuple = () #Vide
mon_tuple = (X,) #Une seule valeur
mon_tuple = (X,Y,Z)
```



## Accéder à un élément d'un tuple

```python
Accéder à l'élément d'indice X : mon_tuple[X]
```



## Cas d'usage

2 raisons d'utiliser les tuples

- Affectation multiple de variables
- Retour multiple de fonction



## Exemples

### Exemple 1
```python
(var1, var2) = (17, 56)
```

### Exemple 2
```python
def get_player_position():
    posX = 148
    posY = 45

    return (posX, posY)


coordX = 0
coordY = 0
print("Position du joueur : ({}/{})".format(coordX, coordY))


(coordX, coordY) = get_player_position()
print("Position du joueur : ({}/{})".format(coordX, coordY))
```