import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read()

setup(
    name="Janus Backend Server",
    version="0.0.0",
    author="Gerben Aaltink",
    author_email="yuraaltink@hotmail.com",
    description=(
        "An demonstration of how to create, document, and publish "
        "an hardcore scaling server."
    ),
    license="BSD",
    keywords="cvs versions backend microservice",
    url="https://github.com/prikkeldraad/janus",
    packages=["vb"],
    install_requires=requirements,
    # long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
