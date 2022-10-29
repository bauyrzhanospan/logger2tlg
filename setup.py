#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import codecs

from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))

def read(filename):
    with codecs.open(os.path.join(cwd, filename), 'rb', 'utf-8') as h:
        return h.read()

metadata = read(os.path.join(cwd, 'logger2telegram', '__init__.py'))

def extract_metaitem(meta):
    # swiped from https://hynek.me 's attr package
    meta_match = re.search(r"""^__{meta}__\s+=\s+['\"]([^'\"]*)['\"]""".format(meta=meta),
                           metadata, re.MULTILINE)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))

setup(
    name='logger2telegram',
    version="1.0.1",
    author='Bauyrzhan Ospan, CEO "Cleverest Technologies LLP"',
    author_email="main@cleverest.tech",
    url="https://github.com/bauyrzhanospan/telegram_logger",
    description="Telegram bot logger that sends strings to telegram chat",
    license="MIT",
    packages=find_packages(exclude=['tests', 'docs']),
    platforms=['Any'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)