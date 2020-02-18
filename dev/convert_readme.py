import pypandoc
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
_README_PATH = os.path.join(_REPO_ROOT, 'README.md')

def conv(fn):
    return pypandoc.convert_file(fn, 'rst')

def main():
    rst = None
    try:
        rst = conv(_README_PATH)
    except OSError:
        print('pandoc installation not found, installing it and trying again...')
        from pypandoc.pandoc_download import download_pandoc
        download_pandoc()
        rst = conv(_README_PATH)

    if not rst:
        print(f'Unable to convert {_README_PATH} to restructured text, exiting')
        return 1
    else:
        with open(_README_PATH.replace('.md', '.rst'), 'w') as rst_file:
            rst_file.write(rst)
        return 0

if __name__ == '__main__':
    sys.exit(main())