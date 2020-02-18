"""
flask-gridify
-------------

This extension creates editable grids from sqlalchemy models
"""
from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith("-"))]

setup(
    name='flask-gridify',
    version='0.1.0',
    url='https://github.com/michaelsobczak/flask-gridify',
    license='BSD',
    author='Michael Sobczak',
    author_email='mikesobczak.code@gmail.com',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_gridify'],
    keywords=['Flask', 'FlaskSQLAlchemy', 'FlaskRestless', 'jsgrid', 'data table'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)