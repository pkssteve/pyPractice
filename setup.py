from setuptools import setup, find_packages

setup(
    name='pyquibase',
    version='1.0',
    description='Python wrapper for liquibase',
    author='Eun Woo Song',
    author_email='songew@gmail.com',
    url='https://github.com/rampart81/pyquibase',
    download_url='',
    install_requires=[],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['python practice'],
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
