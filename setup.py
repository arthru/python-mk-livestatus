#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup

import mk_livestatus


def read(filename):
    filepath = join(dirname(__file__), filename)
    with open(filepath) as f:
        return f.read()


setup(
    name='python-mk-livestatus',
    version=mk_livestatus.__version__,
    description='Helps to query MK livestatus and get results',
    long_description=read('README.rst'),
    author='Michael Fladischer',
    author_email='michael@fladi.at',
    url='https://github.com/arthru/python-mk-livestatus',
    download_url='http://pypi.python.org/pypi/python-mk-livestatus',
    packages=['mk_livestatus'],
    license='BSD',
    test_requires=['tox', 'mock', 'pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring',
    ],
)
