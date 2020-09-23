from setuptools import setup, find_packages

try:
    with open("Readme.md", "r") as fh:
        long_description = fh.read()
except:
    # When using tox, this is no longer going
    # to work properly. For this, just add a
    # dummy description ...
    long_description = "some long description"

setup(
    name='{{cookiecutter.package_name}}',
    version='0.0.1',
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description='Say Hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sankhaMukherjee/{{cookiecutter.package_name}}",
    packages=find_packages(),
    entry_points ={ 
            'console_scripts': [ 
                '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.{{cookiecutter.package_name}}:main'
            ]}, 
    package_data={'':['**/*.json']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    python_requires='>=3.6',
)

