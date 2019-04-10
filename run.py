from app.database.sqlalchemy_initial import ENGINE
from app.database.sqlalchemy_initial import BASE

from app.database.models.user import User
from app.database.models.note import Note


BASE.metadata.create_all(ENGINE)

print('Database setup successfuly....')
