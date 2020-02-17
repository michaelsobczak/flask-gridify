"""
flask-gridify
-------------

This extension creates editable grids from sqlalchemy models
"""
from setuptools import setup


setup(
    name='flask-gridify',
    version='1.0',
    url='https://github.com/michaelsobczak/flask-gridify',
    license='BSD',
    author='Michael Sobczak',
    author_email='mikesobczak.code@gmail.com',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_gridify'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
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