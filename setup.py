#!/usr/bin/env python

import os

from codecs import open

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


packages = ['aioinflux']

requires = [
    'aiohttp>=2.2.5',
]


with open('LICENSE', 'r', 'utf-8') as f:
    license_text = f.read()

setup(
    name='aioinflux',
    version='0.1',
    description='Asynchronous helpers for writing data to influx db',
    long_description='Asynchronous helpers for writing data to influx db',
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    url='https://github.com/Melevir/aioinflux',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'aioinflux': 'aioinflux'},
    include_package_data=True,
    install_requires=requires,
    license=license_text,
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)
