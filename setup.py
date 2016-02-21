"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sts',
    version='1.0.0',
    description='Stock Pattern Analysis',
    long_description=long_description,
    url='https://github.com/',
    author='Mike Preshman',
    author_email='mpresh@gmail.com',
    license='MIT',
    keywords='stock pattern analysis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "docopt",
        "requests",
        "beautifulsoup4",
        "xmltodict",
        "MySQL-python"
    ],
)
