#from distutils.core import setup
from setuptools import setup

setup(
    name='moesearch',
    version='0.1.1',
    author='alfateam123',
    author_email='alfateam123@gmail.com',
    packages=['moesearch'],
    scripts=['bin/index', 'bin/post_details', 'bin/thread_details', 'bin/search'],
    url='http://github.com/alfateam123/moesearch',
    #license='LICENSE.txt',
    description='archive.moe Search REST API Library',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.3.0"
    ],
)
