import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="slackpoint v2",
    version="2.1.0",
    url="https://github.com/nihar4276/slackpoint-v2",
    author="Nihar, Saksham, Manish, Palash, Shruti",
    author_email="nsrao@ncsu.edu",
    description="Sets up the project automatically.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("test",)),
    install_requires=[
        "flask==2.2.2",
        "slackclient==2.9.4",
        "python-dotenv==0.21.0",
        "slackeventsapi==3.0.1",
        "flask-sqlalchemy==3.0.0",
        "psycopg2==2.9.3",
        "pytest==7.1.3",
        "pytest-mock==3.10.0",
        "black==22.8.0",
        "pylint==2.15.3",
    ],
    dependency_links=[],
    setup_requires=["flask>=2.2.2", "pip>=20"],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 1 - Production",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
