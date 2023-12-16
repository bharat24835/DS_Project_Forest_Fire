from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        requirements = file_obj.readlines()
        ## remove /n from requirements.txt
        requirements = [req.replace("\n" , "") for req in requirements]
        return requirements


setup(
    name='Forest_Fire_Prediction',
      version='0.0.1',
      description='Python Distribution Utilities',
      author='Bharat',
      author_email='bharat24835@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      install_requires =get_requirements('requirements.txt'), 
      packages=find_packages()
    )
