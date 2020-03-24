from setuptools import setup, find_packages

setup(
    name='pyPractice',
    version='1.0',
    description='Python practice',
    author='ks steve',
    author_email='pkssteve@gmail.com',
    url='https://github.com/pkssteve/pyPractice',
    download_url='',
    install_requires=[],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['python practice'],
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
