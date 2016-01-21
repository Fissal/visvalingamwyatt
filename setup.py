#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of visvalingamwyatt.
# https://github.com/fitnr/visvalingamwyatt

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, fitnr <contact@fakeisthenewreal.org>

from setuptools import setup, find_packages

setup(
    name='visvalingamwyatt',

    version='0.1.0',

    description='Simplify geometries with the Visvalingam-Wyatt algorithm',

    long_description='Simplify geometries with the Visvalingam-Wyatt algorithm',

    keywords='gis',

    author='fitnr',

    author_email='contact@fakeisthenewreal.org',

    url='https://github.com/fitnr/visvalingamwyatt',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],

    packages=find_packages(),

    include_package_data=False,

    install_requires=[
        'numpy>=1.8,<2'
    ],

    extras_require={
        'cli': ['Fiona>=1.6.2,<2'],
    },

    entry_points={
        'console_scripts': [
            'vwsimplify=visvalingamwyatt.cli:main',
        ],
    },

    test_suite='tests',

    use_2to3=True,
)
