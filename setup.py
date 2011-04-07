# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.json'
version = '0.1'
readme = open(join('src', 'dolmen', 'json', "README.txt")).read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.browser',
    'cromlech.io',
    'setuptools',
    ]

setup(name = name,
      version = version,
      description = 'JSON helpers for the Dolmen project',
      long_description = readme + '\n\n' + history,
      keywords = 'Cromlech Grok Dolmen Json',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = '',
      license = 'ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['dolmen'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires = install_requires,
      extras_require = {
          'test': ['zope.interface'],
          'cjson': ['python-cjson'],
          },
      classifiers = [
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
      )
