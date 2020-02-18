from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Text, create_engine, Table, Boolean, String, Float, Enum
from sqlalchemy.orm import relationship
import os
import enum

Base = declarative_base()

class UserRole(enum.Enum):
    GUEST = 'guest'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    email = Column(String(120))
    description = Column(Text)
    rating = Column(Float)
    verified = Column(Boolean)
    role = Column(Enum(UserRole))
    notes = relationship('Note')

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))


def get_db_path():
    db_dir = os.path.join(
        os.environ['HOME'],
        '.local', 'share',
        'flask-gridify-example'
    )
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    db_url = os.path.join(db_dir, 'db.sqlite')
    return db_url

def get_db_url():
    return f'sqlite:///{get_db_path()}'

def get_engine():
    return create_engine(get_db_url)