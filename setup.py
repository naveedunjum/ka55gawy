from distutils.core import setup
from setuptools import find_packages

setup(name='ka55gawy',
    version='0.1',
    author="DSSS",
    author_email="naveed.unjum@fau.de",
    packages=find_packages(),
    install_requires=['numpy', 'Pillow', 'ipywidgets'])