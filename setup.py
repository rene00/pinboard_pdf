# -*- coding: utf-8 -*-

from pinboard_pdf import metadata
from setuptools import find_packages, setup
import re

INSTALL_REQUIRES = list()
with open('requirements.txt') as requirements_file:
    for requirement in requirements_file:
        INSTALL_REQUIRES.append(requirement)
INSTALL_REQUIRES = list(set(INSTALL_REQUIRES))

setup(
    name='pinboard_pdf',
    version=metadata.__version__,
    description='pinboard pdf',
    maintainer='Rene Cunningham',
    maintainer_email='rene@compounddata.com',
    install_requires=INSTALL_REQUIRES,
    packages=['pinboard_pdf'],
    package_data={'': ['LICENSE', 'README.rst']},
    entry_points={
        'console_scripts': (
            'pinboard_pdf = pinboard_pdf.pinboard_pdf:pinboard_pdf',
        ),
    }
)
