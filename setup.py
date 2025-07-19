from setuptools import setup, find_packages

def get_requirements(file_path):
    """
    Reads the requirements from a file and returns a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    # Remove any whitespace characters like `\n` at the end of each line
    return [req.strip() for req in requirements if req.strip()]

setup(
    name='ml_project',
    version='0.1.0',
    author='Akshat Raj Vansh',
    author_email='rajvanshakshat@gmail.com',
    description='A machine learning project for predicting house prices',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)