from setuptools import setup
from setuptools import find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description="EDSA example python package",
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/KiomeGM/mypackage',
    author='Rogers Mugambi',
    author_email='Rogerskiome.rk@gmail.com'
)

