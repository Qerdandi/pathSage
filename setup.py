
from setuptools import find_packages, setup

setup(
    name='pathsage',
    packages=find_packages(include=['pathsage']),
    version='0.0.1',
    description='This library manages access paths, avoids format and path not found issues and is cross-platform.',
    author='CyberTorii',
    license='MIT',
    install_requires=['os','pathlib']
)
        