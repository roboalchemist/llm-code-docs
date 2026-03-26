# Overview

docs

 [https://readthedocs.org/projects/pytest-cov/]

tests

 [https://github.com/pytest-dev/pytest-cov/actions]

package

 [https://pypi.org/project/pytest-cov]  [https://anaconda.org/conda-forge/pytest-cov]  [https://pypi.org/project/pytest-cov]  [https://pypi.org/project/pytest-cov]  [https://pypi.org/project/pytest-cov]  [https://github.com/pytest-dev/pytest-cov/compare/v7.1.0...master]

This plugin provides coverage functionality as a pytest plugin. Compared to just using `coverage run` this plugin does some extras:

-

Automatic erasing and combination of .coverage files and default reporting.

-

Support for detailed coverage contexts (add `--cov-context=test` to have the full test name including parametrization as the context).

-

Xdist support: you can use all of pytest-xdist’s features including remote interpreters and still get coverage.

-

Consistent pytest behavior. If you run `coverage run -m pytest` you will have slightly different `sys.path` (CWD will be
in it, unlike when running `pytest`).

All features offered by the coverage package should work, either through pytest-cov’s command line options or
through coverage’s config file.

-

Free software: MIT license

## Installation

Install with pip:

```
pip install pytest-cov

```
