# Source: https://docs.pytest.org/en/stable/explanation/goodpractices.html

[]

# Good Integration Practices[¶](#good-integration-practices "Link to this heading")

## Install package with pip[¶](#install-package-with-pip "Link to this heading")

For development, we recommend you use [[`venv`]](https://docs.python.org/3/library/venv.html#module-venv "(in Python v3.14)") for virtual environments and [pip](https://pip.pypa.io/en/stable/ "(in pip v25.3)") for installing your application and any dependencies, as well as the [`pytest`] package itself. This ensures your code and dependencies are isolated from your system Python installation.

Create a [`pyproject.toml`] file in the root of your repository as described in [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/ "(in Python Packaging User Guide)"). The first few lines should look like this:

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [project]
    name = "PACKAGENAME"
    version = "PACKAGEVERSION"

where [`PACKAGENAME`] and [`PACKAGEVERSION`] are the name and version of your package respectively.

You can then install your package in "editable" mode by running from the same directory:

    pip install -e .

which lets you change your source code (both tests and application) and rerun tests at will.

[][]

## Conventions for Python test discovery[¶](#conventions-for-python-test-discovery "Link to this heading")

[`pytest`] implements the following standard test discovery:

-   If no arguments are specified then collection starts from [[`testpaths`]](../reference/reference.html#confval-testpaths) (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.

-   Recurse into directories, unless they match [[`norecursedirs`]](../reference/reference.html#confval-norecursedirs).

-   In those directories, search for [`test_*.py`] or [`*_test.py`] files, imported by their [test package name](#test-package-name).

-   From those files, collect test items:

    -   [`test`] prefixed test functions or methods outside of class.

    -   [`test`] prefixed test functions or methods inside [`Test`] prefixed test classes (without an [`__init__`] method). Methods decorated with [`@staticmethod`] and [`@classmethods`] are also considered.

For examples of how to customize your test discovery [[Changing standard (Python) test discovery]](../example/pythoncollection.html).

Within Python modules, [`pytest`] also discovers tests using the standard [[unittest.TestCase]](../how-to/unittest.html#unittest-testcase) subclassing technique.

[]

## Choosing a test layout[¶](#choosing-a-test-layout "Link to this heading")

[`pytest`] supports two common test layouts:

### Tests outside application code[¶](#tests-outside-application-code "Link to this heading")

Putting tests into an extra directory outside your actual application code might be useful if you have many functional tests or for other reasons want to keep tests separate from actual application code (often a good idea):

    pyproject.toml
    src/
        mypkg/
            __init__.py
            app.py
            view.py
    tests/
        test_app.py
        test_view.py
        ...

This has the following benefits:

-   Your tests can run against an installed version after executing [`pip`]` `[`install`]` `[`.`].

-   Your tests can run against the local copy with an editable install after executing [`pip`]` `[`install`]` `[`--editable`]` `[`.`].

For new projects, we recommend to use [`importlib`] [[import mode]](pythonpath.html#import-modes) (see [which-import-mode](#which-import-mode) for a detailed explanation). To this end, add the following to your configuration file:

    # content of pytest.toml
    [pytest]
    addopts = ["--import-mode=importlib"]

Generally, but especially if you use the default import mode [`prepend`], it is **strongly** suggested to use a [`src`] layout. Here, your application root package resides in a sub-directory of your root, i.e. [`src/mypkg/`] instead of [`mypkg`].

This layout prevents a lot of common pitfalls and has many benefits, which are better explained in this excellent [blog post](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure%3E) by Ionel Cristian Mărieș.

Note

If you do not use an editable install and use the [`src`] layout as above you need to extend the Python's search path for module files to execute the tests against the local copy directly. You can do it in an ad-hoc manner by setting the [`PYTHONPATH`] environment variable:

    PYTHONPATH=src pytest

or in a permanent manner by using the [[`pythonpath`]](../reference/reference.html#confval-pythonpath) configuration variable and adding the following to your configuration file:

toml

    [pytest]
    pythonpath = ["src"]

ini

    [pytest]
    pythonpath = src

Note

If you do not use an editable install and not use the [`src`] layout ([`mypkg`] directly in the root directory) you can rely on the fact that Python by default puts the current directory in [`sys.path`] to import your package and run [`python`]` `[`-m`]` `[`pytest`] to execute the tests against the local copy directly.

See [[Invoking pytest versus python -m pytest]](pythonpath.html#pytest-vs-python-m-pytest) for more information about the difference between calling [`pytest`] and [`python`]` `[`-m`]` `[`pytest`].

### Tests as part of application code[¶](#tests-as-part-of-application-code "Link to this heading")

Inlining test directories into your application package is useful if you have direct relation between tests and application modules and want to distribute them along with your application:

    pyproject.toml
    [src/]mypkg/
        __init__.py
        app.py
        view.py
        tests/
            __init__.py
            test_app.py
            test_view.py
            ...

In this scheme, it is easy to run your tests using the [[`--pyargs`]](../reference/reference.html#cmdoption-pyargs) option:

    pytest --pyargs mypkg

[`pytest`] will discover where [`mypkg`] is installed and collect tests from there.

Note that this layout also works in conjunction with the [`src`] layout mentioned in the previous section.

Note

You can use namespace packages (PEP420) for your application but pytest will still perform [test package name](#test-package-name) discovery based on the presence of [`__init__.py`] files. If you use one of the two recommended file system layouts above but leave away the [`__init__.py`] files from your directories, it should just work. From "inlined tests", however, you will need to use absolute imports for getting at your application code.

Note

In [`prepend`] and [`append`] import-modes, if pytest finds a [`"a/b/test_module.py"`] test file while recursing into the filesystem it determines the import name as follows:

-   determine [`basedir`]: this is the first "upward" (towards the root) directory not containing an [`__init__.py`]. If e.g. both [`a`] and [`b`] contain an [`__init__.py`] file then the parent directory of [`a`] will become the [`basedir`].

-   perform [`sys.path.insert(0,`]` `[`basedir)`] to make the test module importable under the fully qualified import name.

-   [`import`]` `[`a.b.test_module`] where the path is determined by converting path separators [`/`] into "." characters. This means you must follow the convention of having directory and file names map directly to the import names.

The reason for this somewhat evolved importing technique is that in larger projects multiple test modules might import from each other and thus deriving a canonical import name helps to avoid surprises such as a test module getting imported twice.

With [[`--import-mode=importlib`]](../reference/reference.html#cmdoption-import-mode) things are less convoluted because pytest doesn't need to change [`sys.path`], making things much less surprising.

[]

### Choosing an import mode[¶](#choosing-an-import-mode "Link to this heading")

For historical reasons, pytest defaults to the [`prepend`] [[import mode]](pythonpath.html#import-modes) instead of the [`importlib`] import mode we recommend for new projects. The reason lies in the way the [`prepend`] mode works:

Since there are no packages to derive a full package name from, [`pytest`] will import your test files as *top-level* modules. The test files in the first example ([[src layout]](#src-layout)) would be imported as [`test_app`] and [`test_view`] top-level modules by adding [`tests/`] to [`sys.path`].

This results in a drawback compared to the import mode [`importlib`]: your test files must have **unique names**.

If you need to have test modules with the same name, as a workaround you might add [`__init__.py`] files to your [`tests`] folder and subfolders, changing them to packages:

    pyproject.toml
    mypkg/
        ...
    tests/
        __init__.py
        foo/
            __init__.py
            test_view.py
        bar/
            __init__.py
            test_view.py

Now pytest will load the modules as [`tests.foo.test_view`] and [`tests.bar.test_view`], allowing you to have modules with the same name. But now this introduces a subtle problem: in order to load the test modules from the [`tests`] directory, pytest prepends the root of the repository to [`sys.path`], which adds the side-effect that now [`mypkg`] is also importable.

This is problematic if you are using a tool like [tox](#tox) to test your package in a virtual environment, because you want to test the *installed* version of your package, not the local code from the repository.

The [`importlib`] import mode does not have any of the drawbacks above, because [`sys.path`] is not changed when importing test modules.

[]

## tox[¶](#tox "Link to this heading")

Once you are done with your work and want to make sure that your actual package passes all tests you may want to look into [[tox]](https://tox.wiki/en/stable/index.html "(in Project name not set v4.32)"), the virtualenv test automation tool. [`tox`] helps you to setup virtualenv environments with pre-defined dependencies and then executing a pre-configured test command with options. It will run tests against the installed package and not against your source code checkout, helping to detect packaging glitches.

## Do not run via setuptools[¶](#do-not-run-via-setuptools "Link to this heading")

Integration with setuptools is **not recommended**, i.e. you should not be using [`python`]` `[`setup.py`]` `[`test`] or [`pytest-runner`], and may stop working in the future.

This is deprecated since it depends on deprecated features of setuptools and relies on features that break security mechanisms in pip. For example 'setup_requires' and 'tests_require' bypass [`pip`]` `[`--require-hashes`]. For more information and migration instructions, see the [pytest-runner notice](https://github.com/pytest-dev/pytest-runner#deprecation-notice). See also [pypa/setuptools#1684](https://github.com/pypa/setuptools/issues/1684).

setuptools intends to [remove the test command](https://github.com/pypa/setuptools/issues/931).

## Checking with flake8-pytest-style[¶](#checking-with-flake8-pytest-style "Link to this heading")

In order to ensure that pytest is being used correctly in your project, it can be helpful to use the [flake8-pytest-style](https://github.com/m-burst/flake8-pytest-style) flake8 plugin.

flake8-pytest-style checks for common mistakes and coding style violations in pytest code, such as incorrect use of fixtures, test function names, and markers. By using this plugin, you can catch these errors early in the development process and ensure that your pytest code is consistent and easy to maintain.

A list of the lints detected by flake8-pytest-style can be found on its [PyPI page](https://pypi.org/project/flake8-pytest-style/).

Note

flake8-pytest-style is not an official pytest project. Some of the rules enforce certain style choices, such as using [`@pytest.fixture()`] over [`@pytest.fixture`], but you can configure the plugin to fit your preferred style.

[]

## Using pytest's strict mode[¶](#using-pytest-s-strict-mode "Link to this heading")

[Added in version 9.0.]

Pytest contains a set of configuration options that make it more strict. The options are off by default for compatibility or other reasons, but you should enable them if you can.

You can enable all of the strictness options at once by setting the [[`strict`]](../reference/reference.html#confval-strict) configuration option:

toml

    [pytest]
    strict = true

ini

    [pytest]
    strict = true

See the [[`strict`]](../reference/reference.html#confval-strict) documentation for the options it enables and their effect.

If pytest adds new strictness options in the future, they will also be enabled in strict mode. Therefore, you should only enable strict mode if you use a pinned/locked version of pytest, or if you want to proactively adopt new strictness options as they are added. If you don't want to automatically pick up new options, you can enable options individually:

toml

    [pytest]
    strict_config = true
    strict_markers = true
    strict_parametrization_ids = true
    strict_xfail = true

ini

    [pytest]
    strict_config = true
    strict_markers = true
    strict_parametrization_ids = true
    strict_xfail = true

If you want to use strict mode but having trouble with a specific option, you can turn it off individually:

toml

    [pytest]
    strict = true
    strict_parametrization_ids = false

ini

    [pytest]
    strict = true
    strict_parametrization_ids = false