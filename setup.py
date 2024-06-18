"""
Setup scripts to build/install the mypackage.

Inspired by:
    - https://github.com/scrapy/scrapy
    - https://github.com/scikit-learn/scikit-learn
"""
from pathlib import Path

from setuptools import find_packages, setup

version = (Path(__file__).parent / "mypackage/VERSION").read_text("ascii").strip()


install_requires = [
    "icecream",
    "numpy",
    "setuptools",
]
extras_require = dict()  # Some examples at https://github.com/scrapy/scrapy/blob/2.11/setup.py

# For setup arguments/keywords refer to: https://setuptools.pypa.io/en/latest/references/keywords.html
setup(
    name="MyPackage",
    version=version,
    url="https://mypackage.website.org",
    project_urls={
        "Documentation": "https://sinras-mypackage.readthedocs.io/en/latest/",
        "Source": "https://github.com/SinRas/pypi-plus-readthedocs",
        "Tracker": "https://github.com/SinRas/pypi-plus-readthedocs/issues",
    },
    description="A python package that builds for PyPI and connects to ReadthDocs, named mypackage",
    long_description=open("README.rst", encoding="utf-8").read(),
    author="Sina Rasouli (author)",
    author_email="rasoolibox193@gmail.com",
    maintainer="Sina Rasouli (maintainer)",
    maintainer_email="rasoolibox193@gmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: MyPackage",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],  # List of all possible classifiers: https://pypi.org/classifiers/
    python_requires=">=3.11",
    install_requires=install_requires,
    extras_require=extras_require,
)
