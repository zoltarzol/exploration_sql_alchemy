from a_create_classes import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Fichier SQLite de test
bdd_locale = "fastfood.sqlite"

# Initialisation de session SQLAlchemy
engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Création des pays
pays = [Pays(1, 'France', datetime.now()),Pays(2, 'Allemagne', datetime.now()),Pays(3, 'Italie', datetime.now())]

# Création des codes postaux
code_postaux = [
    CodePostal(1, '75000', 1, datetime.now()),
    CodePostal(2, '76000', 1, datetime.now()),
    CodePostal(3, '77000', 1, datetime.now()),
    CodePostal(4, '10117', 2, datetime.now()),
    CodePostal(5, '10118', 2, datetime.now()),
    CodePostal(6, '10119', 2, datetime.now()),
    CodePostal(7, '00100', 3, datetime.now()),
    CodePostal(8, '00200', 3, datetime.now()),
    CodePostal(9, '00300', 3, datetime.now())]

# Création des villes
villes = [
    Ville(1, 'Paris', 1, datetime.now()),
    Ville(2, 'Rouen', 2, datetime.now()),
    Ville(3, 'Le Havre', 3, datetime.now()),
    Ville(4, 'Berlin', 4, datetime.now()),
    Ville(5, 'Dresde', 5, datetime.now()),
    Ville(6, 'Hambourg', 6, datetime.now()),
    Ville(7, 'Rome', 7, datetime.now()),
    Ville(8, 'Milan', 8, datetime.now()),
    Ville(9, 'Naples', 9, datetime.now())]

# Création des adresses
adresses = [
    Adresse(1, '1', 'Rue', 1, datetime.now()),
    Adresse(2, '2', 'Rue', 1, datetime.now()),
    Adresse(3, '3', 'Rue', 1, datetime.now()),
    Adresse(4, '4', 'Rue', 1, datetime.now()),
    Adresse(5, '5', 'Rue', 1, datetime.now()),
    Adresse(6, '6', 'Rue', 1, datetime.now()),
    Adresse(7, '1', 'Rue', 2, datetime.now()),
    Adresse(8, '2', 'Rue', 2, datetime.now()),
    Adresse(9, '3', 'Rue', 2, datetime.now()),
    Adresse(10, '4', 'Rue', 2, datetime.now()),
    Adresse(11, '5', 'Rue', 2, datetime.now()),
    Adresse(12, '6', 'Rue', 2, datetime.now()),
    Adresse(13, '1', 'Rue', 3, datetime.now()),
    Adresse(14, '2', 'Rue', 3, datetime.now()),
    Adresse(15, '3', 'Rue', 3, datetime.now()),
    Adresse(16, '4', 'Rue', 3, datetime.now()),
    Adresse(17, '5', 'Rue', 3, datetime.now()),
    Adresse(18, '6', 'Rue', 3, datetime.now()),
    Adresse(19, '1', 'Rue', 4, datetime.now()),
    Adresse(20, '2', 'Rue', 4, datetime.now()),
    Adresse(21, '3', 'Rue', 4, datetime.now()),
    Adresse(22, '4', 'Rue', 4, datetime.now()),
    Adresse(23, '5', 'Rue', 4, datetime.now()),
    Adresse(24, '6', 'Rue', 4, datetime.now()),
    Adresse(25, '1', 'Rue', 5, datetime.now()),
    Adresse(26, '2', 'Rue', 5, datetime.now()),
    Adresse(27, '3', 'Rue', 5, datetime.now()),
    Adresse(28, '4', 'Rue', 5, datetime.now()),
    Adresse(29, '5', 'Rue', 5, datetime.now()),
    Adresse(30, '6', 'Rue', 5, datetime.now()),
    Adresse(31, '1', 'Rue', 6, datetime.now()),
    Adresse(32, '2', 'Rue', 6, datetime.now()),
    Adresse(33, '3', 'Rue', 6, datetime.now()),
    Adresse(34, '4', 'Rue', 6, datetime.now()),
    Adresse(35, '5', 'Rue', 6, datetime.now()),
    Adresse(36, '6', 'Rue', 6, datetime.now()),
    Adresse(37, '1', 'Rue', 7, datetime.now()),
    Adresse(38, '2', 'Rue', 7, datetime.now()),
    Adresse(39, '3', 'Rue', 7, datetime.now()),
    Adresse(40, '4', 'Rue', 7, datetime.now()),
    Adresse(41, '5', 'Rue', 7, datetime.now()),
    Adresse(42, '6', 'Rue', 7, datetime.now()),
    Adresse(43, '1', 'Rue', 8, datetime.now()),
    Adresse(44, '2', 'Rue', 8, datetime.now()),
    Adresse(45, '3', 'Rue', 8, datetime.now()),
    Adresse(46, '4', 'Rue', 8, datetime.now()),
    Adresse(47, '5', 'Rue', 8, datetime.now()),
    Adresse(48, '6', 'Rue', 8, datetime.now()),
    Adresse(49, '1', 'Rue', 9, datetime.now()),
    Adresse(50, '2', 'Rue', 9, datetime.now()),
    Adresse(51, '3', 'Rue', 9, datetime.now()),
    Adresse(52, '4', 'Rue', 9, datetime.now()),
    Adresse(53, '5', 'Rue', 9, datetime.now()),
    Adresse(54, '6', 'Rue', 9, datetime.now())] 

session.add_all(pays)
# session.add_all(code_postaux)
# session.add_all(villes)
# session.add_all(adresses)
session.commit()