from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse

password = "MyDataBase@123"
encoded_password = urllib.parse.quote(password, safe = '')

db_url = f"mysql+pymysql://root:{encoded_password}@localhost:3306/mydb"

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)