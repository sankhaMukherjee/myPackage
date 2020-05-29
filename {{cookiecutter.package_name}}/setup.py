from setuptools import setup

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='{{cookiecutter.package_name}}',
    version='0.0.1',
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description='Say Hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sankhaMukherjee/{{cookiecutter.package_name}}",
    py_modules=['{{cookiecutter.package_name}}'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
