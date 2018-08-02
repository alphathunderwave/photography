import re

from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as f:
    requirements = f.read().splitlines()

with open('README.md', 'rt') as f:
    readme = f.read()

try:
    with open('app/__init__.py', 'rt') as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            f.read(), re.MULTILINE).group(1)
except (AttributeError, FileNotFoundError):
    raise RuntimeError('version is not set')

if not version:
    raise RuntimeError('version is not set')

setup(
    name='photo',
    author='alphathunderwave',
    author_email='alphathunderwave@gmail.com',
    url='http://github.com/alphathunderwave/photography',
    version=version,
    packages=find_packages(),
    license='MIT',
    description='Photo hosting website',
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
    setup_requires=[
        'flake8',
        'pep8-naming',
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: photography',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Photo'
    ]
)
