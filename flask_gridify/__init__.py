from flask import current_app, _app_ctx_stack

from .utils import get_attributes

class FlaskGridify(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass
        # app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        # app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        # if hasattr(ctx, 'sqlite3_db'):
        #     ctx.sqlite3_db.close()

    def gridify(self, sqlalchemy_model_class):
        attributes = get_attributes(sqlalchemy_model_class)
