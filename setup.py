# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def get_requirements(fname):
    "Takes requirements from requirements.txt and returns a list."
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")
setuptools.setup(
    name="notion",
    version="0.0.28",
    author="Jamie Alexandre",
    author_email="jamalex+python@gmail.com",
    description="Unofficial Python API client for Notion.so",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mathix420/notion-py",
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
