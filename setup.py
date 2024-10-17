from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fx_python_sdk",
    version="0.1.0",
    author="FX",
    author_email="fx@fx.com",
    description="Interact with FX Port to share / retrieve AAS Submodel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_package_name",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyYAML>=6.0.2',
        'requests>=2.32.3',
    ],
)