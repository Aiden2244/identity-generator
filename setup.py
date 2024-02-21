'''
setup.py
'''

from setuptools import setup, find_packages

# Read requirements.txt and store its contents in a list
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='id_gen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    package_data={
        'id_gen': ['attributes/*.txt'],
    },  
    entry_points={
        'console_scripts': [
            'id_gen=id_gen.main:main',  
        ],
    },
    include_package_data=True
)

