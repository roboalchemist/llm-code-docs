# Source: https://xlrd.readthedocs.io/en/latest/development.html

Title: Development — xlrd 2.0.1 documentation

URL Source: https://xlrd.readthedocs.io/en/latest/development.html

Markdown Content:
[xlrd](https://xlrd.readthedocs.io/en/latest/index.html)
If you wish to contribute to this project, then you should fork the repository found here:

[https://github.com/python-excel/xlrd](https://github.com/python-excel/xlrd)

Once that has been done and you have a checkout, you can follow these instructions to perform various development tasks:

Setting up a virtualenv[¶](https://xlrd.readthedocs.io/en/latest/development.html#setting-up-a-virtualenv "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

The recommended way to set up a development environment is to turn your checkout into a virtualenv and then install the package in editable form as follows:

$ virtualenv .
$ bin/pip install -e .[test]

Running the tests[¶](https://xlrd.readthedocs.io/en/latest/development.html#running-the-tests "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

Once you’ve set up a virtualenv, the tests can be run as follows:

$ source bin/activate
$ pytest

Building the documentation[¶](https://xlrd.readthedocs.io/en/latest/development.html#building-the-documentation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------

The Sphinx documentation is built by doing the following, having activated the virtualenv above, from the directory containing setup.py:

$ source bin/activate
$ cd docs
$ make html

To check that the description that will be used on PyPI renders properly, do the following:

$ python setup.py --long-description | rst2html.py > desc.html

Making a release[¶](https://xlrd.readthedocs.io/en/latest/development.html#making-a-release "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

To make a release, just update the version in `xlrd.info.__VERSION__`, update the change log and push to [https://github.com/python-excel/xlrd](https://github.com/python-excel/xlrd) and Carthorse should take care of the rest.
