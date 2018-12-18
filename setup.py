#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for folder_monitor.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys


from pkg_resources import require, VersionConflict
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

setup_requirements = [  # setup_requires package requirements
    "pytest-runner"
]

install_requirements = [  # install_requires install requirements
    # TODO: put install requirements here
]

test_requirements = [  # tests_require test requirements
    "pytest", "pytest-cov"
]


if __name__ == "__main__":
    setup(
        setup_requires=setup_requirements,
        tests_require=test_requirements
    )
