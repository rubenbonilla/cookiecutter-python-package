#!/usr/bin/env python
import os
from setuptools import setup, find_packages

try:  # From pip version < 10.0.0
    from pip.req import parse_requirements
    from pip.download import PipSession
except Exception:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession


def read(fname):
    """Read a file and return its content."""
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


def requirements(filename):
    """Parse requirements files."""
    return [f'{req.name}{req.specifier}'
            for req in parse_requirements(filename=filename, session=PipSession())]


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.description }}',
    long_description=read('README.md'),
    packages=find_packages(exclude=['tests']),
    install_requires=requirements('./requirements/requirements.txt'),
    extras_require={
        'dev': requirements('./requirements/requirements-dev.txt'),
        'test': requirements('./requirements/requirements-test.txt')
        },
    setup_requires=['pytest-runner'],
    tests_require=requirements('./requirements/requirements-test.txt'),
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}:main']
        }
)
