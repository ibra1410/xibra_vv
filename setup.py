# setup.py

from setuptools import setup, find_packages

setup(
    name='xibra_v',  # Name of the library
    version='0.1',
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # If there are any external dependencies, list them here
    description='A simple encryption library for text and files with customizable layers of encryption.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ibrahim',
    author_email='ibraus34@gmail.com',
    url='https://github.com/ibra1410/xibra_vv',  # URL of the GitHub repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Supported Python versions
)
