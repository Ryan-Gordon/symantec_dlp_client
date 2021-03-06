# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="symantec_dlp_python_client",
    version="0.1.0",
    description="A python package used to interface with the Symantec DLP SOAP API",
    license="MIT",
    author="Ryan Gordon",
    url="https://github.com/Ryan-Gordon/symantec_dlp_client",
    packages=find_packages(),
    install_requires=[
        "zeep>=3.4.0",
        "requests" # Ideally this should be pinned to something, open for now.
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
