# flask-gridify
flask extension for making editable grids from sqlalchemy models

## Usage

Like other flask extensions, you'll initialize it with the app. Below is from the "example" application in the repo.

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_gridify import FlaskGridify

app = Flask(__name__)
db = SQLAlchemy(app)

# initialize the FlaskGridify extension
grid = FlaskGridify(app, flask_sqlalchemy_db=db, root_url_prefix='/grids')
```

Then for each model class you want grids for you'll call the `gridify` function of the `grid` object above and pass in the SQLAlchemy model **class**

```
from .models import User, Note
grid.gridify(User)
grid.gridify(Note)
```

When you run the app, you'll have the following URL routes:

* /
	* This route demonstrates useage of the Jinja macros that allow for creation of grids inside of your application templates
* /grids/note
	* This is the grid page created for the Note model
* /grids/user
	* This is the grid page created for the User model

Additionally, the extension will create and use a REST API for each gridified model class that can be used by your application. It uses the [FlaskRestless](https://flask-restless.readthedocs.io/en/stable/) extension so information on the formatting and URLs can be found there