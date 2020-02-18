from flask import current_app, _app_ctx_stack
import pkg_resources
from .utils import get_attributes
import os
from flask import Blueprint, render_template
from flask_restless import APIManager

class FlaskGridify(object):
    def __init__(self, app, flask_sqlalchemy_db, root_url_prefix):
        self.app = app
        if app is not None:
            self.init_app(app, flask_sqlalchemy_db, root_url_prefix)

    def init_app(self, app, flask_sqlalchemy_db, root_url_prefix):
        self.app = app
        self.url_prefix = root_url_prefix
        self.rest_api_manager = APIManager(self.app, flask_sqlalchemy_db=flask_sqlalchemy_db)
        self.app.config['GRID_REGISTRY'] = {}
        template_folder = pkg_resources.resource_filename('flask_gridify', 'templates')
        static_blueprint = Blueprint('flask-gridify', __name__, 
            static_folder=pkg_resources.resource_filename('flask_gridify', 'static'), static_url_path='/flask-gridify',
            template_folder=template_folder)
        self.app.register_blueprint(static_blueprint)

        def wrapper(a):
            app = a
            @app.context_processor
            def inject_attribute_map():
                return {
                    'GRID_REGISTRY': app.config['GRID_REGISTRY']
                }

        wrapper(self.app)
        

    def teardown(self, exception):
        pass

    def gridify(self, sqlalchemy_model_class):

        name = sqlalchemy_model_class.__name__.lower()
        model_url_prefix = f'{self.url_prefix}/{name}'
        model_blueprint = Blueprint(f'flask-gridify-{name}', __name__, 
            template_folder='templates',
            url_prefix=model_url_prefix)
        attributes = get_attributes(sqlalchemy_model_class)
        self.app.config['GRID_REGISTRY'][name] = attributes
        # create the REST API
        api_attributes_list = [ a.name for a in attributes ]
        api_blueprint = self.rest_api_manager.create_api_blueprint(sqlalchemy_model_class, methods=['GET', 'POST', 'PUT', 'DELETE'])

        def route_maker(attrs):
            attrs = list(attrs)
            # create the views
            @model_blueprint.route(f'/')
            def model_view():
                return render_template('gridify/grid.html.jinja', class_name=name, attributes=attrs)

        route_maker(attributes)
        self.app.register_blueprint(model_blueprint)
        self.app.register_blueprint(api_blueprint)



