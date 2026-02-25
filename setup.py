#!/usr/bin/env python
"""
Setup script for Food Delivery Operations Analytics
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith('#')]

setup(
    name='food-delivery-analytics',
    version='1.0.0',
    author='Data Engineering Team',
    author_email='team@fooddeliveryanalytics.com',
    description=
    'A comprehensive data engineering and analytics platform for food delivery operations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/food-delivery-analytics',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'food-delivery-elt=src.etl.etl_pipeline:main',
            'food-delivery-dashboard=src.dashboard.app:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
