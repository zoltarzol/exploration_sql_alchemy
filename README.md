# Brief - Projet "restaurant_BI"
## Réalisé par Elias et ZoLTaR
## Technologies utilisées : Python, Django, SQLite, SQLAlchemy
<br>

### Installation des prérequis pour lancer l'application Web

```sh
conda create -n restaurant_BI
conda activate restaurant_BI
conda install sqlalchemy
conda install django
conda install python-dotenv
```

### Fichiers supplémentaires

- Diagramme UML EER (schéma logique Entités-Relations étendu)
<br>

![alt text](restaurant_BI_EER.png "EER Model")

- Création du schéma de données (compatible MySQL Server

perl -ne 's/^\[(.+)\].*/`cat $1`/e;print' create_schema.sql "Script de génération de schéma MySQL")