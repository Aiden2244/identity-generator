'''
setup.py
'''

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='new-alias',
    version='1.1.0',
    packages=find_packages(),
    install_requires=requirements,
    package_data={
        'new_alias': ['attributes/*.txt'],
    },  
    entry_points={
        'console_scripts': [
            'new_alias=new_alias.main:main',  
        ],
    },
    include_package_data=True,
    
    author='Aiden R. McCormack',
    author_email='aidenm2244@proton.me',
    description='An alias generator for online privacy protection',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Aiden2244/identity-generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

