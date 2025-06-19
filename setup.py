from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this will return list of requiremnets
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML_01',
    version='0.01',
    author='Himanshu',
    author_email='himanshuk.iitp@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirement.txt')
     


)