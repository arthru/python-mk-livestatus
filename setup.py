#!/usr/bin/env python
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='python-mk-livestatus',
      version='0.1',
      description='access MK livestatus query results either as lists or dictionaries',
      long_description=read('README.rst'),
      author='Michael Fladischer',
      author_email='michael@fladi.at',
      url='http://git.fladi.at/python-mk-livestatus.git/',
      download_url='http://pypi.python.org/pypi/python-mk-livestatus',
      packages=['mk_livestatus'],
      license='BSD',
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Office/Business :: Financial :: Accounting',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Monitoring',
      ],
)
