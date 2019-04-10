from app.database.sqlalchemy_initial import ENGINE
from app.database.sqlalchemy_initial import BASE

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import SmallInteger
from sqlalchemy.orm import relationship

from app.database.models.note import Note


class User(BASE):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable=False)
    lastname = Column(String(30))
    age = Column(SmallInteger)
    height = Column(Integer)
    weight = Column(Integer)
    
    notes = relationship('Note', backref = 'user')
    
    def __init__(self, name):
        self.name = name
    


