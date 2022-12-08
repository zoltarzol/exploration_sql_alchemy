# <span style="color: #339933;">DEVIA P3 / FastFood</span>
### <span style="color: #339933;">par Elias et ZoLTaR</span>
## <span style="color: #dd7700;">Bibliothèques utilisées : Django, SQLAlchemy, Faker</span>
### <span style="color: #5599ff;">1. Installation des prérequis pour lancer l'application Web</span>

- Avec minicondas - creation d'environnement
```sh
conda deactivate
conda create --name restaurant_BI --file req_conda.txt
conda activate restaurant_BI
```

- Avec minicondas - liste de commandes
```sh
conda deactivate
conda create -n restaurant_BI
conda activate restaurant_BI
conda install sqlalchemy
conda install django
conda install python-dotenv
conda install faker
```

### <span style="color: #5599ff;">Annexes : ressources complémentaires</span>

- Diagramme UML EER (schéma logique Entités-Relations étendu)

![alt text](restaurant_BI_EER.png "EER Model")

- Script de génération du schéma de données (compatible MySQL Server) => <a href="https://github.com/zoltarzol/restaurant_BI/blob/dev_cedric/create_schema_mysql.sql">create_schema_mysql.sql</a> (aperçu ci-dessous)

```
CREATE SCHEMA IF NOT EXISTS `FastFood` ;

CREATE TABLE IF NOT EXISTS `FastFood`.`Poste` (
  `id_Poste` INT NOT NULL,
  `nom` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id_Poste`))
ENGINE = InnoDB;

[...]

CREATE TABLE IF NOT EXISTS `FastFood`.`TicketCaisse` (
  `id_TicketCaisse` INT NOT NULL,
  `date_heure` DATETIME NOT NULL,
  `moyen_paiement` VARCHAR(45) NOT NULL,
  `id_vendeur` INT NOT NULL,
  PRIMARY KEY (`id_TicketCaisse`),
  INDEX `fk_id_vendeur_idx` (`id_vendeur` ASC) VISIBLE,
  CONSTRAINT `fk_id_vendeur`
    FOREIGN KEY (`id_vendeur`)
    REFERENCES `FastFood`.`Employe` (`id_Employe`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
```

- Premiers tests avec SQLAlchemy => <a href="https://github.com/zoltarzol/restaurant_BI/blob/dev_cedric/tests_SQLAlchemy.py">tests_SQLAlchemy.py</a> (aperçu ci-dessous)

```py
# Conventions de nommage :
# - classes et tables : CamelCase
# - clés primaires ou secondaires : id_{Table}
# - noms des attributs de classes et des colonnes : snake_case

# Import des classes et fonctions de SQLAlchemy, ainsi que de datetime et os
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

[...]

# Jointure de tables
results = session.query(Employe, Poste.nom).filter(Employe.id_Poste == Poste.id_Poste).all()
print(sep, "Jointure pour afficher le poste des employés\n", "LIGNES:", len(results), "\n")
for r in results:
    print(r[0], "occupe le poste de", r[1])
print(sep)
```
