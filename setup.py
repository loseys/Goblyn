#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='goblyn',
    version=__import__('goblyn').__version__,
    description='...',
    author='Loseys',
    author_email='iphs2@outlook.com',
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/loseys/Goblyn',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'goblyn = goblyn.__main__:main'
        ]
    },
    keywords=['goblyn', 'pentesting', 'security'],
)
