Installing
==========

This is the repository is meant to be used for installing the {{cookiecutter.package_name}} package. 
A wheel dstribution of this package is present in the [`dist`](../master/dist) folder and may be 
installed within your virtual enviroonment. Just download this directly into your folder and install 
like any other pip package as:

`pip3 install {{cookiecutter.package_name}}-<version>-py3-none-any.whl`

Git alternatively allows you to install packages directly from Github. Consider doing the following:

`pip3 install git+https://github.com/sankhaMukherjee/{{cookiecutter.package_name}}.git`

This has been built upon a Unix system. If you use this for other systems, you 
may wish to consider building this library from source.  If this is a 
provate repo, or you use ssh, remember to use the following instead:

`pip3 install git+ssh://git@github.com/sankhaMukherjee/{{cookiecutter.package_name}}.git`

Package Building
----------------

You may wish to make customize this package for your own use. For that, you need to build the system:

 - Clone this repo to your computer
 - Install a virtual enviromnent, and istall the required packages
 - Buid the system

 A `Makefile` has been provided for aiding with this process. The following commands should allow you do do the following

  - `make grantPermission`: grants execute permission to all shell scripts in the `bin` folder
  - `make clean`: clean unwanted and temporary files that are generated
  - `make build`: This will allow you to build Wheel packages for your system

