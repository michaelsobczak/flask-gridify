from flask import Flask
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Text, create_engine, Table, Boolean, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from flask_gridify import FlaskGridify

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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()
db = SQLAlchemy(app)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    email = Column(String(120))
    verified = Column(Boolean)
    notes = relationship('Note')

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))

grid = FlaskGridify(app, flask_sqlalchemy_db=db, root_url_prefix='/grids')

@app.before_first_request
def init_app():
    if not os.path.exists(get_db_path()):
        Base.metadata.create_all(bind=db.engine)
    grid.gridify(User)
    grid.gridify(Note)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)