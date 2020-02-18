clean:
	rm -rf dist build flask_gridify.egg-info

build: clean
	python dev/convert_readme.py
	python dev/populate_setup.py
	python setup.py sdist

upload: build
	twine upload dist/*

run:
	FLASK_APP=example flask run --host=0.0.0.0