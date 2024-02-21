from setuptools import setup, find_packages

# Read requirements.txt and store its contents in a list
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='idgen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,  # Use the list created from requirements.txt
    entry_points={
        'console_scripts': [
            'id-gen=my_package.main:main',  # "idgen" command will call main() in my_package/main.py
        ],
    },
)
