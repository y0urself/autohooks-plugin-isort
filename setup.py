# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pkg_resources import safe_version
from setuptools import setup, find_namespace_packages

VERSION = (1, 0, 1, 'alpha')


def get_version():
    str_version = '.'.join([str(v) for v in VERSION])
    return safe_version(str_version)


with open('README.md', 'r') as f:
    long_description = f.read()  # pylint: disable=invalid-name

setup(
    name='autohooks-plugin-isort',
    version=get_version(),
    author='Greenbone Networks GmbH',
    author_email='info@greenbone.net',
    description='Autohooks plugin for include sorting via isort',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/greenbone/autohooks-plugin-isort',
    packages=find_namespace_packages(include=['autohooks.*']),
    python_requires='>=3.5',
    install_requires=['autohooks>=1.1', 'isort'],
    classifiers=[
        # Full list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
    ],
)
