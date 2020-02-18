# flask-gridify
flask extension for making editable grids from sqlalchemy models. In the `example` directory of the repo you can find a mimimal flask app demonstrating features and usage of the extension. The code snippets below are all from the example.

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

### Using FlaskGridify in Templates

The extension also exposes Jinja template macros you can use to embed the editable grids for models in your pages. In the `example/templates/index.html.jinja` template file we create grids for the User and Note model classes like so:

```
    <div id="user-grid"></div>
    <div id="note-grid"></div>
    {{ macros.create_grid("user-grid", "user", GRID_REGISTRY["user"]) }}
    {{ macros.create_grid("note-grid", "note", GRID_REGISTRY["note"]) }}
```

## TODO
* Add Enum field support
* Add relationship field support
	* many to one
	* many to many
* Clean up the exposed macros to avoid reference to `GRID_REGISTRY`

## Dependencies
* Server side
	* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
	* [Flask-Restless](https://flask-restless.readthedocs.io/en/stable/)
* Client side
	* [jsgrid](http://js-grid.com/)


