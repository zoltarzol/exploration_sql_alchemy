# <span style="color: #339933;">DEVIA P3 / FastFood</span>
### <span style="color: #339933;">par Elias et ZoLTaR</span>
## <span style="color: #dd7700;">Bibliothèques utilisées : Django, SQLAlchemy, Faker</span>
### <span style="color: #5599ff;">1. Creation de l'environnement et des dépendances</span>

- Option 1 : génération automatique de l'environnement
```sh
conda deactivate
conda create --name restaurant_BI --file req_conda.txt
conda activate restaurant_BI
```

- Option 2 : Génération manuelle de l'environnement minicondas
```sh
conda deactivate
conda create -n restaurant_BI
conda activate restaurant_BI
conda install sqlalchemy
conda install django
conda install python-dotenv
conda install faker
```

### <span style="color: #5599ff;">2. Création du fichier .env avec la clé secrète Django</span>

```sh
# Assurez-vous d'être à la racine du projet, au même niveau que manage.py

echo -n "SECRET_KEY=" > .env
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' >> .env
```

### <span style="color: #5599ff;">Annexes : ressources complémentaires</span>

- Diagramme UML EER (schéma logique Entités-Relations étendu)

![alt text](restaurant_BI_EER.png "EER Model")

- Script SQL pour la génération du schéma de données (version MySQL Server) => <a href="https://github.com/zoltarzol/restaurant_BI/blob/dev_cedric/create_schema_mysql.sql">create_schema_mysql.sql</a><br>

```
CREATE SCHEMA IF NOT EXISTS `FastFood` ;

CREATE TABLE IF NOT EXISTS `FastFood`.`Poste` (
  `id_Poste` INT NOT NULL,
  `nom` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id_Poste`))
ENGINE = InnoDB;

[...]
```

- Premiers tests avec SQLAlchemy => <a href="https://github.com/zoltarzol/restaurant_BI/blob/dev_cedric/tests_SQLAlchemy.py">tests_SQLAlchemy.py</a><br>
(script executable séparément, affichage en console)

```py
[...]

# Jointure de tables
results = session.query(Employe, Poste.nom).filter(Employe.id_Poste == Poste.id_Poste).all()
print(sep, "Jointure pour afficher le poste des employés\n", "LIGNES:", len(results), "\n")
for r in results:
    print(r[0], "occupe le poste de", r[1])
print(sep)
```
