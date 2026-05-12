#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='5.12.6',
      description="Singer.io utility library",
      author="Stitch",
      python_requires=">=3.7.0",
      classifiers=[
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
      ],
      url="http://singer.io",
      install_requires=[
          'pytz>=2018.4',
          'jsonschema>=2.6.0',
          'simplejson>=3.11.1',
          'python-dateutil>=2.6.0',
          'backoff>=2.2.1',
          'pycryptodome',
          'pycryptodomex',
          'ciso8601',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'pytest',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
