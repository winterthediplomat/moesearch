#from distutils.core import setup
from setuptools import setup

setup(
    name='moesearch',
    version='0.1.0',
    author='alfateam123',
    author_email='alfateam123@gmail.com',
    packages=['moesearch'],
    #scripts=['bin/index', 'bin/post_details', 'bin/thread_details', 'bin/search'],
    #url='http://pypi.python.org/pypi/moesearch',
    #license='LICENSE.txt',
    description='archive.moe Search REST API Library',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.3.0"
    ],
)
