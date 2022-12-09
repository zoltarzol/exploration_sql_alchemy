# Conventions de nommage :
# - classes et tables : CamelCase
# - clés primaires ou secondaires : id_{Table}
# - noms des attributs de classes et des colonnes : snake_case

# Import des classes et fonctions de SQLAlchemy, ainsi que de datetime et os
from sqlalchemy import ForeignKey, Column, String, Integer, Date, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Creation d'une nouvelle classe de base SQLAlchemy.
Base = declarative_base()

# Les classes ci-dessous sont les équivalences sous forme d'objets des tables en base de données (ici SQLite)

# Création de la classe Pays
class Pays(Base):
    # Déclaration du nom de la table
    __tablename__ = "Pays"

    # Déclaration de la clé primaire id_Pays
    id_Pays = Column(Integer, primary_key=True)

    # Déclaration des autres colonnes
    nom = Column(String)
    date_creation = Column(DateTime)

    # Initialisateur
    def __init__(self, id_Pays, nom, date_creation):
        self.id_Pays = id_Pays
        self.nom = nom
        self.date_creation = date_creation

# Création de la classe Poste
class Poste(Base):
    # Déclaration du nom de la table
    __tablename__ = "Poste"

    # Déclaration de la clé primaire id_Poste
    id_Poste = Column(Integer, primary_key=True)

    # Déclaration des autres colonnes
    nom = Column(String)
    date_creation = Column(DateTime)

    # Initialisateur
    def __init__(self, id_Poste, nom, date_creation):
        self.id_Poste = id_Poste
        self.nom = nom
        self.date_creation = date_creation

class Carte(Base):
    __tablename__ = 'Carte'

    id_Carte = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    id_Restaurant = Column(String(45))
    date_creation = Column(DateTime)
    
    def __init__(self, id_Carte, nom, id_Restaurant, date_creation):
        self.id_Carte = id_Carte
        self.nom = nom
        self.id_Restaurant = id_Restaurant
        self.date_creation = date_creation

class CodePostal(Base):
    __tablename__ = 'CodePostal'

    id_CodePostal = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False)
    id_Pays = Column(Integer, ForeignKey('Pays.id_Pays'))
    date_creation = Column(DateTime)

    def __init__(self, id_CodePostal, code, id_Pays, date_creation):
        self.id_CodePostal = id_CodePostal
        self.code = code
        self.id_Pays = id_Pays
        self.date_creation = date_creation

class Ville(Base):
    __tablename__ = 'Ville'

    id_Ville = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    id_CodePostal = Column(Integer, ForeignKey('CodePostal.id_CodePostal'))
    date_creation = Column(DateTime)

    def __init__(self, id_Ville, nom, id_CodePostal, date_creation):
        self.id_Ville = id_Ville
        self.nom = nom
        self.id_CodePostal = id_CodePostal
        self.date_creation = date_creation

class Adresse(Base):
    __tablename__ = 'Adresse'

    id_Adresse = Column(Integer, primary_key=True)
    numero_adresse = Column(String(45))
    voie_adresse = Column(String(45))
    id_Ville = Column(Integer, ForeignKey('Ville.id_Ville'))
    date_creation = Column(DateTime)

    def __init__(self, id_Adresse, numero_adresse, voie_adresse, id_Ville, date_creation):
        self.id_Adresse = id_Adresse
        self.numero_adresse = numero_adresse
        self.voie_adresse = voie_adresse
        self.id_Ville = id_Ville
        self.date_creation = date_creation

class Ingredient(Base):
    __tablename__ = 'Ingredient'

    id_Ingredient = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    prix_achat = Column(Float, nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_Ingredient, nom, prix_achat, date_creation):
        self.id_Ingredient = id_Ingredient
        self.nom = nom
        self.prix_achat = prix_achat
        self.date_creation = date_creation

class Item(Base):
    __tablename__ = 'Item'

    id_Item = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    type = Column(String(10), nullable=False)
    taille_boisson = Column(String(10))
    prix_vente = Column(Float, nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_Item, nom, type, taille_boisson, prix_vente, date_creation):
        self.id_Item = id_Item
        self.nom = nom
        self.type = type
        self.taille_boisson = taille_boisson
        self.prix_vente = prix_vente
        self.date_creation = date_creation

class Recette(Base):
    __tablename__ = 'Recette'

    id_Recette = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    quantité = Column(Integer, nullable=False)
    id_Ingredient = Column(Integer, ForeignKey('Ingredient.id_Ingredient'), nullable=False)
    id_Item = Column(Integer, ForeignKey('Item.id_Item'), nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_Recette, nom, quantité, id_Ingredient, id_Item, date_creation):
        self.id_Recette = id_Recette
        self.nom = nom
        self.quantité = quantité
        self.id_Ingredient = id_Ingredient
        self.id_Item = id_Item
        self.date_creation = date_creation

class Menu(Base):
    __tablename__ = 'Menu'

    id_Menu = Column(Integer, primary_key=True)
    nom = Column(String(45), nullable=False)
    id_Item_plat = Column(Integer, ForeignKey('Item.id_Item'), nullable=False)
    id_Item_boisson = Column(Integer, ForeignKey('Item.id_Item'), nullable=False)
    id_Item_dessert = Column(Integer, ForeignKey('Item.id_Item'), nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_Menu, nom, id_Item_plat, id_Item_boisson, id_Item_dessert, date_creation):
        self.id_Menu = id_Menu
        self.nom = nom
        self.id_Item_plat = id_Item_plat
        self.id_Item_boisson = id_Item_boisson
        self.id_Item_dessert = id_Item_dessert
        self.date_creation = date_creation

class Restaurant(Base):
    __tablename__ = 'Restaurant'
    id_Restaurant = Column(Integer, primary_key=True)
    nom = Column(String(45))
    espace_enfants = Column(Boolean)
    borne_service = Column(Boolean)
    accessible_pmr = Column(Boolean)
    parking = Column(Boolean)
    id_Carte = Column(Integer, ForeignKey('Carte.id_Carte'))
    id_Employe_directeur = Column(Integer, ForeignKey('Employe.id_Employe'))
    id_Adresse = Column(Integer, ForeignKey('Adresse.id_Adresse'))
    date_creation = Column(DateTime)

    def __init__(self, nom, espace_enfants, borne_service, accessible_pmr, parking, id_Carte, id_Employe_directeur, id_Adresse, date_creation):
        self.nom = nom
        self.espace_enfants = espace_enfants
        self.borne_service = borne_service
        self.accessible_pmr = accessible_pmr
        self.parking = parking
        self.id_Carte = id_Carte
        self.id_Employe_directeur = id_Employe_directeur
        self.id_Adresse = id_Adresse
        self.date_creation = date_creation

class Employe(Base):
    __tablename__ = 'Employe'
    id_Employe = Column(Integer, primary_key=True)
    prenom = Column(String(45))
    nom = Column(String(45))
    date_embauche = Column(DateTime)
    num_compte = Column(String(10))
    experience = Column(Boolean)
    id_Poste = Column(Integer, ForeignKey('Poste.id_Poste'))
    id_Employe_responsable = Column(Integer, ForeignKey('Employe.id_Employe'))
    id_Restaurant = Column(Integer, ForeignKey('Restaurant.id_Restaurant'))
    id_Adresse_restaurant = Column(Integer, ForeignKey('Adresse.id_Adresse'))
    date_creation = Column(DateTime)

    def __init__(self, prenom, nom, date_embauche, num_compte, experience, id_Poste, id_Employe_responsable, id_Restaurant, id_Adresse_restaurant, date_creation):
        self.prenom = prenom
        self.nom = nom
        self.date_embauche = date_embauche
        self.num_compte = num_compte
        self.experience = experience
        self.id_Poste = id_Poste
        self.id_Employe_responsable = id_Employe_responsable
        self.id_Restaurant = id_Restaurant
        self.id_Adresse_restaurant = id_Adresse_restaurant
        self.date_creation = date_creation

class Salaire(Base):
    __tablename__ = 'Salaire'
   
    id_Salaire = Column(Integer, primary_key=True)
    note = Column(Integer, nullable=False)
    montant = Column(Float, nullable=False)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime)
    id_Employe = Column(Integer, nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_Salaire, note, montant, date_debut, date_fin, id_Employe, date_creation):
        self.id_Salaire = id_Salaire
        self.note = note
        self.montant = montant
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.id_Employe = id_Employe
        self.date_creation = date_creation

class TicketCaisse(Base):
    __tablename__ = 'TicketCaisse'
   
    id_TicketCaisse = Column(Integer, primary_key=True)
    date_heure = Column(DateTime, nullable=False)
    moyen_paiement = Column(String, nullable=False)
    id_vendeur = Column(Integer, nullable=False)
    date_creation = Column(DateTime)

    def __init__(self, id_TicketCaisse, date_heure, moyen_paiement, id_vendeur, date_creation):
        self.id_TicketCaisse = id_TicketCaisse
        self.date_heure = date_heure
        self.moyen_paiement = moyen_paiement
        self.id_vendeur = id_vendeur
        self.date_creation = date_creation
