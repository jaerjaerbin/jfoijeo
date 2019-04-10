from app.database.sqlalchemy_initial import ENGINE
from app.database.sqlalchemy_initial import BASE

from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import SmallInteger
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from datetime import datetime


class Note(BASE):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key = True)
    note_type = Column(SmallInteger, nullable = False)
    title = Column(Text)
    description = Column(Text)
    intensity = Column(SmallInteger)
    note_date = Column(DateTime(), default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    #user: fake field holding the user object who make the annotation
    
    
    def __init__(self, title, desc = ""):
        self.title = title
        self.note_type = 1
        self.description = desc
    
