from setuptools import setup, find_packages

setup(
    name="pymaxheap",
    version="1.0.0",
    author="Diksha Wagh",
    author_email="waghdiksha935@gmail.com",
    description="A simple Python library for Max Heap operations built on heapq",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Diksha-3905/Maxheap_for_myself",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
