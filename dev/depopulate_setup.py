import pypandoc
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
_README_PATH = os.path.join(_REPO_ROOT, 'README.rst')
_SETUP_PATH = os.path.join(_REPO_ROOT, 'setup.py')

def main():
    with open(_SETUP_PATH, 'r') as setup_file:
        orig = setup_file.read()

    with open(_README_PATH, 'r') as readme_file:
        readme = readme_file.read()

    new = orig.replace(f'"""{readme}"""', "'{LONGDESCRIPTION}'")
    with open(_SETUP_PATH, 'w') as new_setup_file:
        new_setup_file.write(new)

if __name__ == '__main__':
    sys.exit(main())