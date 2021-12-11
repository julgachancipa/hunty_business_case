from sqlalchemy import create_engine, MetaData

from settings import Settings

settings = Settings()

user = settings.MYSQL_USER
password = settings.MYSQL_PASSWORD
host = settings.MYSQL_HOST
port = settings.MYSQL_PORT
db = settings.MYSQL_DATABASE

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}")

meta = MetaData()

conn = engine.connect()
