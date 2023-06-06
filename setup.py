from setuptools import setup, find_packages
# it lets you create the packages
# find packages automatically finds the packages inside the src(__init__.py)

setup(
    name='insurance',
    version="0.1",
    description="package for insurance premium prediction",
    author="Prajwal",
    packages=find_packages(),
    license="MIT"
)

# to run
# pip install -e .
# pip freeze

# make tar file 
# python setup.py sdist bdist_wheels