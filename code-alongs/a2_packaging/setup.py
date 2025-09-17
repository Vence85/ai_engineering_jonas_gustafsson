from setuptools import setup, find_packages

print(find_packages())

setup(
    name="cool_package",
    version="0.0.1",
    description="this package is a template for",
    author="Jonas Gustafsson",
    author_email="jonas.gustafsson@gmail.com",
    packages=find_packages(),
)