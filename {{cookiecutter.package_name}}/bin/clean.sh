#!/bin/bash

find . -name __pycache__ | xargs rm -rf
rm -rf build
rm -rf src/{{cookiecutter.package_name}}.egg-info
rm -rf .pytest_cache