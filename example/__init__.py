import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_gridify import FlaskGridify

from .models import User, Note, get_db_url, get_db_path

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()
db = SQLAlchemy(app)

# initialize the FlaskGridify extension
#   the created pages will be /grids/<model_name> due to root_url_prefix
grid = FlaskGridify(app, flask_sqlalchemy_db=db, root_url_prefix='/grids')

if not os.path.exists(get_db_path()):
    Base.metadata.create_all(bind=db.engine)

grid.gridify(User)
grid.gridify(Note)
from . import views, models