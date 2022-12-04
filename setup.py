from setuptools import setup, find_packages

NAME = 'proxier'

setup(
    name=NAME,
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'proxier = proxier.cli:main'
        ]
    },
    install_requires=['requests>=2.28.1']
)
