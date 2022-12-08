from pandas.io import sql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

bdd_locale = "fastfood.sqlite"

# Initialisation d'un moteur SQLAlchemy
engine = create_engine(f"sqlite:///{bdd_locale}", echo=True)

sql.execute('DELETE FROM Pays', engine)
sql.execute('VACUUM', engine)