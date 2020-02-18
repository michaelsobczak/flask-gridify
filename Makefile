clean:
	rm -rf dist build flask_gridify.egg-info

build: clean
	python dev/convert_readme.py
	python dev/populate_setup.py
	python setup.py sdist

upload: build
	twine upload dist/*
	python dev/depopulate_setup.py
	rm README.rst

run:
	FLASK_APP=example FLASK_DEBUG=true flask run --host=0.0.0.0