from setuptools import setup, find_packages,setup 
from pathlib import Path
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    if '-e.' in requirements:
        requirements.remove('-e.')
    return requirements



setup(
    name='Ml-projet',
    version='1.0.0',
    author='Ruhit',
    description='A machine learning project',
    packages=find_packages(),
    author_email="ruhittanvir14@gmail.com",
    install_requires=get_requirements('requirements.txt')
)