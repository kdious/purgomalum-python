from os import path
from setuptools import find_packages, setup
here = path.abspath(path.dirname(__file__))

version_num = "1.0.3"

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='PurgoMalum',
    version=version_num,
    description='A python client for the PurgoMalum profanity filter web service',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Kevin Dious',
    author_email='kdious@yahoo.com',
    url='https://github.com/kdious/purgomalum-python',
    download_url='https://github.com/kdious/purgomalum-python/tarball/{ver}'.format(
        ver=version_num),
    install_requires=['future==0.17.1', 'requests==2.22.0'],
    packages=find_packages(),
    keywords=['profanity', 'filter', 'PurgoMalum', 'purgomalum', 'purgo_malum', 'purgo-malum', 'Purgo Malum'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
