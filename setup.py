from setuptools import setup, find_packages

# Read requirements.txt and store its contents in a list
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='idgen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,  
    entry_points={
        'console_scripts': [
            'id_gen=id_gen.main:main',  
        ],
    },
)
