import os.path
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('version.py').read())

setup(name='tornado-skeleton',
    version=__version__,
    description='Boilerplate for a tornado based web application',
    long_description=read('README.md'),
    author='Uian Sol',
    author_email='sol.uian@gmail.com',
    url='https://github.com/uiansol/tornado-skeleton',
    include_package_data=True,
    classifiers=[],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'tornado==4.3',
    ])
