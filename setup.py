#!/usr/bin/env python

from __future__ import unicode_literals
from setuptools import setup
import io
import os


pkg_dir = os.path.dirname(__file__)
# importing __<vars>__ into the namespace
#https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
with open(os.path.join(pkg_dir, 'opentargets_urlzsource', 'version.py')) as fv:
    exec(fv.read())


long_description = ""
readme_path = os.path.join(pkg_dir, 'README.md')
with io.open(readme_path, encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(name=__pkgname__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8',
    author=__author__,
    author_email=__author_email__,
    url=__homepage__,
    packages=['opentargets_urlzsource'],
    license=__license__,
    download_url=__homepage__ + '/archive/' + __version__ + '.tar.gz',
    keywords=['opentargets', 'python2', 'python3'],
    platforms=['any'],
    #make sure this matches requirements.txt
    install_requires=['requests-file', 'future'],
    dependency_links=[],
    include_package_data=True,
    data_files=[],
    scripts=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    #make sure this matches requirements.dev.txt
    extras_require={'dev': ['pytest',
        'pytest-cov', 'pylint', 'tox', 'codecov', 'pipdeptree']}
)
