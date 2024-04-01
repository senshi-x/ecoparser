from sqlmodel import SQLModel, create_engine
from os import getenv
sqlite_file_name = "database.db"
from dotenv import load_dotenv

load_dotenv()
connstring= f"mariadb+mariadbconnector://{getenv('DB_USER')}:{getenv('DB_PASS')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
print(connstring)
engine = create_engine(connstring, pool_recycle=3600, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)