#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
setup_requirements = ['pytest-runner', ]


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Simple html report for pytest',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'html report', 'pytest report'
    ],
    name='pytest-simple-report',
    packages=find_packages(include=['pytest_simple_report']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-simple-report',
    version='0.1.0',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner'
        'jinja2'
    ],
    entry_points={
        'pytest11': [
            'pytest-simple-report = pytest_simple_report.plugin',
        ]
    }
)
