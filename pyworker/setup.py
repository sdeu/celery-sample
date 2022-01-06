#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ 
    "redis==3.5.3", 
    "celery==5.2.2",
    "requests==2.23.0"
    ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Steffen Deubler",
    author_email='steffen.deubler@t-online.de',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Sample application for Celery chord.",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='celery chord',
    name='pyworker',
    packages=find_packages(include=['pyworker', 'pyworker.*']),
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    version='0.1.0',
    zip_safe=False,
)
