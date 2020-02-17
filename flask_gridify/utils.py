

from sqlalchemy import inspect

class FlaskGridifyException(BaseException):
    pass


def get_attributes(sqlalchemy_model_class):
    if not hasattr(sqlalchemy_model_class, '__table__'):
        raise FlaskGridifyException(f'Class {sqlalchemy_model_class.__name__} has to attribute __table__ but FlaskGridify expects a subclass of SQLAlchemy declarative base class')

    t = sqlalchemy_model_class.__table__
    columns = t.columns
    foreign_keys = t.foreign_keys