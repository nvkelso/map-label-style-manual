#!/usr/bin/env python

from distutils.core import setup
from StreetNames import __version__

setup(name='StreetNames',
      version=__version__,
      description='Utility functions for handling street names.',
      author='Michal Migurski',
      author_email='mike@stamen.com',
      url='https://github.com/nvkelso/map-label-style-manual',
      packages=['StreetNames'],
      license='BSD')
