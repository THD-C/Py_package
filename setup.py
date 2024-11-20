from setuptools import setup, find_packages

setup(
    name="Py_package",
    version="0.1.0",
    packages=find_packages(),
    author="THDC",
    author_email="thdc.p.lodz@outlook.com",
    description="A brief description of your module",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/THD-C/Protocol.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)