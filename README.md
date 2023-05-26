# Openclassrooms P11 - Améliorez une application Web Python par des tests et du débogage

Cette application implémente un système de réservation pour les organisateurs de compétition. Elle permettra à des clubs d'inscrire des athlètes à des compétitions, elle sera également en charge de la gestion des soldes de points pour chaque club, ainsi que des soldes de places disponibles pour chaque competition.

Le but de ce projet est de deboguer [l'application existante](https://github.com/OpenClassrooms-Student-Center/Python_Testing), et de mettre en place un ensemble de tests.

## Mise en place de l'environnement python :

1. Création de l'environnement virtuel :
    ```
    python -m venv env
    ```

2. Installation des packages nécessairs :

    ```
    pip install -r ./requirements.txt
    ```


3. Activation de l'environnement virtuel :

    ```
    ./env/Scripts/activate
    ```


## Lancement du serveur local :

1. Mettre en place l'environnement virtuel

2. Mettre en place la variable d'environnement flask :

    ```
    set FLASK_APP=app/server.py
    ```

3. Lancer le serveur flask :

    ```
    flask run
    ```

## Lancement des tests :

``` 
pyhon -m pytest 
```

## Lancement des tests de performance :

1. Lancer le server

2. Lancement des tests de performance :

    ``` 
    locust -f .\tests\locust\locustfile.py --config .\tests\locust\locust.conf 
    ```

## Courverture de test :

1. Depuis la racine du projet, lancer :

```
pytest --cov=.\app --cov-report html
```

2. Ouvir le fichier ``` .\htmlcov\index.html ``` pour accéder au rapport de couverture
