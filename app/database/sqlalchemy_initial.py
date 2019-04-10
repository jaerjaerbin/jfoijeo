from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


ENGINE = create_engine('sqlite:///database.db', echo = True)
BASE = declarative_base()
