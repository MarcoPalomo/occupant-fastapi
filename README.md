# Intégration d'un modèle MVC avec FastAPI, SQLAlchemy et JavaScript pour notre app `Okipan`

###### Nous voulons structurer l'application de manière plus claire et faciliter sa maintenance.

* Model: Représente les données et les règles métier. Ici, ce sera géré par SQLAlchemy et Python.
* View: Interface utilisateur, développée en JavaScript et affichant les données fournies par le modèle.
* Controller: Gère les interactions entre le modèle et la vue, c'est-à-dire les requêtes HTTP. C'est FastAPI qui va jouer ce rôle.


### Setup :

Lancer le build de l'image ...

```bash

docker build -t mon-app-room-occupancy .
```

...puis instancier le conteneur Docker.

```bash

docker run -p 8000:8000 -v $(pwd)/data:/app/data mon-app-room-occupancy
```


Ceci va persister dans notre répertoire ``data``en local, les données de notre application dans une base de données *sqlite*.