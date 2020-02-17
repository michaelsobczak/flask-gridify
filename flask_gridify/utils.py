
from dataclasses import dataclass
from sqlalchemy import inspect
import enum
from typing import List
class FlaskGridifyException(BaseException):
    pass

class FlaskGridifyDatatypes(enum.Enum):
    INTEGER = 'integer'
    TEXT = 'text'
    BOOL = 'bool'

@dataclass
class ModelAttribute:
    name: str
    datatype: FlaskGridifyDatatypes

def get_attributes(sqlalchemy_model_class) -> List[ModelAttribute]:
    class_name = sqlalchemy_model_class.__name__
    if not hasattr(sqlalchemy_model_class, '__table__'):
        raise FlaskGridifyException(f'Class {class_name} has to attribute __table__ but FlaskGridify expects a subclass of SQLAlchemy declarative base class')
    t = sqlalchemy_model_class.__table__
    columns = t.columns
    foreign_keys = t.foreign_keys
    return [ModelAttribute(name=c.name, datatype=c.type) for c in columns]