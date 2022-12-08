from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tests_SQLAlchemy import Pays
import unidecode

# Fichier SQLite de test
bdd_locale = "fastfood.sqlite"

# Initialisation d'une session SQLAlchemy
Base = declarative_base()
engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker('en_US')

liste_pays = []
for i in range(1000):
    liste_pays.append(fake.country())

set_pays = set(liste_pays)
liste_pays_final = list(set_pays)
liste_pays_final.sort()
liste_objets_pays = []

for i in range(len(liste_pays_final)):
    liste_objets_pays.append(Pays(i+1,liste_pays_final[i]))

for p in liste_objets_pays:
    session.add(p)

session.commit()