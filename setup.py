#from distutils.core import setup
from setuptools import setup

setup(
    name='moesearch',
    version='0.1.2',
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
    classifiers=[
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards",
    "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
