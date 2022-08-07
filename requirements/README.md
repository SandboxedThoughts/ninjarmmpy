# Requirements

Used to retain versioning of python packages while organizing multiple environment setups.
Packages required in every environment will be added to the base requirements file. All envioronment-specific packages will be added as listed below.

## Install instructions 

To install necessary packages for your environment use the `-r` flag on `pip install` to specify a specific filepath.

#### Example

Install the local packages by entering the command,  `pip install -r requrirements/local.txt`

## base.txt

The file holding all python packages required in every environment. The base requirments are added by default to each envioronmnet and are installed when running `pip install`.


## environments

### testing.txt

For use with any testing environment - local or public. The testing packages are included in the local packages by default. However, live servers requiring the testing packages will need to be installed in a separate command.

### local.txt

For use on local environments only, this package installs the testing packages along with any additional packages required specifically for a local development environment.

#### python-decouple

This package will allow for a configuration file rather than storing necessary keys in environment variables. See the [pypi documents](https://pypi.org/project/python-decouple/) for reference matierial.

### live.txt

For use on live servers. This includes any staging servers, production servers, and testing servers not on a local environment.
