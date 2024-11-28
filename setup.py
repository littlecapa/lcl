from setuptools import setup, find_packages

setup(
    name="my_lib",
    version="0.1.0",
    description="A Python library for basic functions",
    author="Littlecapa",
    author_email="littlecapa@googlemail.com",
    url="https://github.com/littlecapa/lcl",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
