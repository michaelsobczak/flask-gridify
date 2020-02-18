
from dataclasses import dataclass
from sqlalchemy import inspect, Table
from sqlalchemy.orm import class_mapper, ColumnProperty, RelationshipProperty
from sqlalchemy.sql.sqltypes import Integer, Boolean, String, Enum, Float, Text
import enum
from typing import List
class FlaskGridifyException(BaseException):
    pass

class FlaskGridifyDatatypes(enum.Enum):
    INTEGER = 'integer'
    FLOAT = 'float'
    TEXT = 'text'
    BOOL = 'bool'
    RELATIONSHIP = 'relationship'
    ENUM = 'enum'


_SQL_GRIDIFY_TYPE_MAP = {
    String: FlaskGridifyDatatypes.TEXT,
    Integer: FlaskGridifyDatatypes.INTEGER,
    Boolean: FlaskGridifyDatatypes.BOOL,
    Enum: FlaskGridifyDatatypes.ENUM,
    Float: FlaskGridifyDatatypes.FLOAT,
    Text: FlaskGridifyDatatypes.TEXT
}

@dataclass
class ModelAttribute:
    name: str
    datatype: FlaskGridifyDatatypes
    target: Table = None

def get_attributes(sqlalchemy_model_class) -> List[ModelAttribute]:
    mapper = class_mapper(sqlalchemy_model_class)
    
    attributes = []
    for p in mapper.iterate_properties:
        column_name = p.key
        if isinstance(p, ColumnProperty):
            if len(p.columns) != 1:
                print(f'WARNING: Unable to process {p} since it has number of columns other than 1: {p.columns}')
                continue
            datatype = None
            sql_datatype = type(p.columns[0].type)
            if sql_datatype not in _SQL_GRIDIFY_TYPE_MAP:
                print(f'WARNING: Unsupported type {sql_datatype} for column {column_name}')
                continue
            else:
                datatype = _SQL_GRIDIFY_TYPE_MAP[sql_datatype]
            if datatype:
                attributes.append(
                    ModelAttribute(column_name, datatype)
                )
            else:
                print(f'WARNING: Unable to find datatype for column {column_name}')
                continue
        elif isinstance(p, RelationshipProperty):
            attributes.append(
                ModelAttribute(column_name, FlaskGridifyDatatypes.RELATIONSHIP, p.target)
            )
        else:
            print(f'WARNING: Unable to process {p} with type {type(p)}')
            continue

    return attributes
    # class_name = sqlalchemy_model_class.__name__
    # if not hasattr(sqlalchemy_model_class, '__table__'):
    #     raise FlaskGridifyException(f'Class {class_name} has to attribute __table__ but FlaskGridify expects a subclass of SQLAlchemy declarative base class')
    # t = sqlalchemy_model_class.__table__
    # columns = t.columns
    # foreign_keys = t.foreign_keys
    # return [ModelAttribute(name=c.name, datatype='VARCHAR' if 'VARCHAR' in str(c.type) else c.type) for c in columns]