from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tests_SQLAlchemy import Pays, Poste
import unidecode, time

# Fichier SQLite de test
bdd_locale = "fastfood.sqlite"

# Initialisation d'une session SQLAlchemy
Base = declarative_base()
engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker('fr_FR')

liste_pays = sorted(list(set([unidecode.unidecode(fake.country()).split(' (')[0] for i in range(10)])))

liste_objets_pays = []

for i in range(len(liste_pays)):
    liste_objets_pays.append(Pays(i+1,liste_pays[i]))

for x in liste_objets_pays:
    session.add(x)

session.commit()

liste_objets_poste = [Poste(1,"Directeur"),Poste(2,"Manager"),Poste(3,"Caissier"),Poste(1,"Cuisinier"),]

for x in liste_objets_poste:
    session.add(x)

session.commit()