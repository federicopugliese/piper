from setuptools import setup, find_packages
import os


# Read requirements
requirements_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
with open(requirements_file, "r") as f:
    requirements = f.read().splitlines()


# Package configuration
_NAME = "{{package_name}}"
setup(
    name=_NAME,
    version="0.0.0",
    description="{{description}}",
    packages=find_packages(),
    install_requires=requirements
)
