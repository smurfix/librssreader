#!/usr/bin/env python
from setuptools import setup, find_packages
import librssreader

setup(
    name             = 'librssreader',
    version          = librssreader.__version__,
    description      = 'Library for working with the Google Reader Like API',
    long_description = open('README.md').read() + '\n\n' + open('HISTORY.md').read(),

    author           = librssreader.__author__,
    author_email     = 'zigler.zhang@gmail.com',
    url              = 'https://github.com/fireinice/librssreader',
    license          = open("LICENSE.txt").read(),

    install_requires = ['requests>=1.0',],

    packages         = ['librssreader'],
    test_suite       = 'tests',

    classifiers      = (
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
