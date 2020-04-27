from setuptools import setup, find_packages

setup(
    name='BluePrism-json-to-xml-conversion',
    version='0.1',
    packages=find_packages(),
    license='',
    author='',
    author_email='',
    description='Blue Prism Json to Xml conversion',
    install_requires=['lxml'],
    extras_require={'test': ['pytest']}
)
