# build application as a package

'''The setup.py file is at the heart of a Python project.
 It describes all the metadata about your project. There are quite a few
fields you can add to a project to give it a rich set of metadata describing the project. 
However, there are only three required fields: name, version, and packages.'''


from setuptools import find_packages,setup
from typing import List

Hypen_E_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' this func will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # it will read lines from requirements.txt but with next line character("\n").. exclude it
        requirements=[req.replace("\n","") for req in requirements]
        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
        return requirements
# metadata
setup(
    name="mlproject",
    version='0.0.1',
    author="umer",
    author_email="rafiqyatooumer@gmail.com",
    packages=find_packages(), #directs to __init__
    # install_requires=['pandas','numpy','seaborn'] #not feasible
    install_requires=get_requirements('requirements.txt')
)