# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import oh_backend
version = oh_backend.__version__

setup(
    name='Open Hospital backend',
    version=version,
    author='',
    author_email='fmarella@inventati.org',
    packages=[
        'oh_backend',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['oh_backend/manage.py'],
)