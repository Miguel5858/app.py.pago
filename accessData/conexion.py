from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        return self.SessionLocal()

# Definimos cómo conectarnos a nuestra base de datos MySQL.
DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3307/DBPagos"

# Crea la base de datos si no existe
def create_database():
    engine = create_engine("mysql+mysqlconnector://root:admin@localhost:3307/")
    with engine.connect() as connection:
        connection.execute(text("CREATE DATABASE IF NOT EXISTS DBPagos"))

create_database()
