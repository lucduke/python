
# Installation sous debian

``` bash
sudo apt update
sudo apt install python3 python3-dev python3-venv -y
```


# Création d'un environnement virtuel

``` bash
cd your-project
python3 -m venv myvirtualenv
```

Pour activer l'environnement virtuel

``` bash
source myvirtualenv/bin/activate
```

Pour désactiver l'environnement virtuel

``` bash
deactivate
```


# Extraire la liste des dépendances de son projet

``` bash
pip freeze > requirements.txt
```

# Importer les dépendances d'un projet

``` bash
pip install -r requirements.txt
```