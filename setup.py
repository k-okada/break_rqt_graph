#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

import os


description = """
break_rqt_graph
"""


setup(
    name='break_rqt_graph',
    version='0.0.1',
    packages=find_packages(),
    author='Kei Okada',
    author_email='kei.okada@gmail.com',
    license='MIT',
    description=description,
    install_requires=open('requirements.txt').readlines()
)
