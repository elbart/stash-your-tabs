#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='Stashthetab',
      version='0.1',
      description='Stash the tab',
      author='Tim Eggert',
      author_email='tim@elbart.com',
      url='http://elbart.com',
      package_dir={'' : 'src'},
      packages=['stashthetab'],
     )
