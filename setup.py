# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='eventhor',
    version='0.0.1',
    description='Simple event driven framework for Python',
    long_description=readme,
    author='Makito Ishikura',
    author_email='tilt.silvie@gmail.com',
    url='https://github.com/tilt-silvie/eventhor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

