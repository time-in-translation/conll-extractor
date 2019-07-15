from setuptools import setup, find_packages

setup(
    name='conll_extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=['click', 'pyconll'],
    entry_points={
        'console_scripts': ['conll-extract=conll_extractor.cli:cli'],
    },
)
