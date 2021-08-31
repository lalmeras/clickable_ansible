#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup_requirements = [
]

test_requirements = [
]

setup(
    name='clickable_ansible',
    version="1.0.dev0",
    description=("Ansible helpers for clickable."),
    long_description=readme + '\n\n' + history,
    author="Laurent Almeras",
    author_email='lalmeras@gmail.com',
    url='https://github.com/lalmeras/clickable_ansible',
    packages=find_packages(include=['clickable_ansible', 'clickable_ansible.*']),
    entry_points={
        'console_scripts': [
        ]
    },
    include_package_data=True,
    install_requires=[
        "clickable @ git+https://github.com/lalmeras/clickable@v1.0#egg=clickable"
    ],
    python_requires='>=3.6',
    license="BSD license",
    zip_safe=False,
    keywords='clickable',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
