# -*- coding: utf-8 -*-

# Learn more: https://github.com/sheldonrobinson/kaggle_python/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kaggle_python',
    version='0.1.0',
    description='Package of utility scripts extracted from Kaggle/docker-python',
    long_description=readme,
    author='Sheldon Robinson',
    author_email='sheldon_robinson@yahoo.co.uk',
    url='https://github.com/sheldonrobinson/kaggle_python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

