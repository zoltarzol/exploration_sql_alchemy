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

# Fichier SQLite de test
bdd_locale = "tests_SQLAlchemy.sqlite"

# Creation d'une nouvelle classe de base SQLAlchemy.
Base = declarative_base()

# Les classes ci-dessous sont les équivalences sous forme d'objets des tables en base de données (ici SQLite)
# Dans cette exploration, 2 classes (et donc 2 tables) sont créées, avec une liaison Clé étrangère
# >> un Employe occupe un Poste, la clé étrangère est nommée id_Poste dans les deux tables Employe et Poste

# Création de la classe Poste
class Poste(Base):
    # Déclaration du nom de la table
    __tablename__ = "Poste"

    # Déclaration de la clé primaire id_Employe
    id_Poste = Column("id_Poste", Integer, primary_key=True)
    # Déclaration des autres colonnes
    nom = Column("nom", String)

    # Initialisateur
    def __init__(self, id_Poste, nom):
        self.id_Poste = id_Poste
        self.nom = nom    

# Création de la classe Employe
class Employe(Base):
    __tablename__ = "Employe"

    # Déclaration de la clé primaire id_Employe
    id_Employe = Column("id_Employe", Integer, primary_key=True)
    # Déclaration des autres colonnes
    prenom = Column("prenom", String)
    nom = Column("nom", String)
    date_naissance = Column("date_naissance", Date)
    # Déclaration de la clé étrangère Employe.id_Poste relié à la clé primaire Poste.id_Poste
    id_Poste = Column(String, ForeignKey("Poste.id_Poste"))

    # Initialisateur
    def __init__(self, id_Employe, prenom, nom, date_naissance, id_Poste):
        self.id_Employe = id_Employe
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        self.id_Poste = id_Poste

    # Redéfinition de l'affichage de l'objet
    def __repr__(self):
        return f"(id={self.id_Employe}) {self.prenom.capitalize()} {self.nom.capitalize()} né(e) le {self.date_naissance.strftime('%d/%m/%Y')}"

# String de séparation pour l'affichage des résultats en console
sep = "\n--------------------------------------------------------------------------\n"

# Si le fichier mydb.sqlite n'existe pas dans le répertoire courant, la base est crée et initialisée
if(not os.path.isfile(f"{bdd_locale}")):
    engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    postes = [
        Poste(1, "Secrétaire"),
        Poste(2, "Directeur"),
        Poste(3, "Développeur"),
        Poste(4, "Graphiste"),
        Poste(5, "Manager")]
    employes = [
        Employe(1, "Charlie", "Chocodan", datetime.date(1980,3,11),1),
        Employe(2, "Marcel", "Lenoir", datetime.date(1981,3,11), 2),
        Employe(3, "Nicolas", "Pontier", datetime.date(1982,3,11), 3),
        Employe(4, "Charlie", "Tournant", datetime.date(1983,3,11), 3),
        Employe(5, "Guillaume", "Lenoir", datetime.date(1984,3,11), 4),
        Employe(6, "Lucie", "Tournant", datetime.date(1985,3,11), 4),
        Employe(7, "Gérard", "Majax", datetime.date(1986,3,11), 5)]

    for p in postes:
        session.add(p)

    for e in employes:
        session.add(e)

    session.commit()

# Si le fichier mc_zonald.sqlite existe, on passe les étapes de création de base et d'initialisation des données
else:
    engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

# SELECT * FROM Employe
results = session.query(Employe).all()
print (sep, "Liste des employés\n", "Total:", len(results), results, sep)

# SELECT * FROM table WHERE column = "abc"
results = session.query(Employe).filter(Employe.prenom == "Charlie").all()
print(sep, "Liste des employés avec prenom = \"Charlie\"\n", "Total:", len(results), results, sep)

# SELECT * FROM table WHERE date_column = datetime.date(year,month,day)
results = session.query(Employe).filter(Employe.date_naissance > datetime.date(1982,1,1)).all()
print(sep, "Liste des employé(e)(s) nés après le 1er janvier 1982\n", "Total:", len(results), results, sep)

# SELECT * FROM table WHERE date_column = datetime.date(year,month,day)
results = session.query(Employe).filter(Employe.prenom.like("%a%")).all()
print(sep, "Liste des employé(e)(s) dont le prénom contient un \'a\'\n", "Total:", len(results), results, sep)

# Jointure de tables
results = session.query(Employe, Poste.nom).filter(Employe.id_Poste == Poste.id_Poste).all()
for r in results:
    print(r[0], "occupe le poste de", r[1])