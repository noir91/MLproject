from setuptools import find_packages, setup
from typing import List

# creating a constant to monitor "-e ."
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    The function returns a list of requirements for the package.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Reading requirements.txt
        requirements = file_obj.readlines()

        # Removing \n spaces on next line 
        requirements = [req.replace('\n', '') for req in requirements]

        # Removing -e .
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

            
# setup method, details about the package        
setup(
    name= 'MLproject',
    author = 'Noorullah Y',
    author_email= 'noorpro92@gmail.com',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)