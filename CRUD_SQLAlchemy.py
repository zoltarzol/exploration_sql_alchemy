from a_create_classes import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from datetime import datetime

# Base de données de travail
bdd_locale = "fastfood.sqlite"

# Suppression de toutes les données d'une table
def vider_table(db, table):

    # Initialisation d'un moteur SQLAlchemy
    engine = create_engine(f"sqlite:///{db}", echo=True)
    
    # Ouverture de la connexion
    con = engine.connect()

    # Execution d'un ordre SQL (ici une suppression de toutes les données d'une table)
    con.execute(text('DELETE FROM ' + table))

    # VACUUM est une commande SQL qui est utilisée pour nettoyer et optimiser les tables et les index d'une base de données. Elle permet de réindexer, de reconstruire et d'analyser les tables et les index, ce qui améliore leur performance. Cette commande est utile pour les bases de données qui sont mises à jour fréquemment, car elle permet de réduire leur taille en supprimant les enregistrements supprimés, et en réorganisant les données existantes.
    con.execute(text('VACUUM'))

    # Fermeture de la connexion
    con.close()

# Creation d'un pays
def creer_pays(nom):
    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    x = Pays(nom)
    session.add(x)
    session.commit()

# Récupération de tous les éléments d'une table sous forme de 
def get_all_users():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(User).all()
    return users

# Update
def update_email(name, new_email):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    user.email = new_email
    session.commit()

# Delete
def delete_user(name):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///users.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    session.delete(user)
    session.commit()

######################
# TEST DES FONCTIONS #
######################

vider_table(bdd_locale, "pays")
creer_pays("Russie")