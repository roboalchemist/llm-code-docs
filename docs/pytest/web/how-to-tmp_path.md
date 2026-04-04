# Source: https://docs.pytest.org/en/stable/how-to/tmp_path.html

[][]

# How to use temporary directories and files in tests[¶](#how-to-use-temporary-directories-and-files-in-tests "Link to this heading")

## The [`tmp_path`] fixture[¶](#the-tmp-path-fixture "Link to this heading")

You can use the [`tmp_path`] fixture which will provide a temporary directory unique to each test function.

[`tmp_path`] is a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") object. Here is an example test usage:

    # content of test_tmp_path.py
    CONTENT = "content"

    def test_create_file(tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text(CONTENT, encoding="utf-8")
        assert p.read_text(encoding="utf-8") == CONTENT
        assert len(list(tmp_path.iterdir())) == 1
        assert 0

Running this would result in a passed test except for the last [`assert`]` `[`0`] line which we use to look at values:

    $ pytest test_tmp_path.py
    =========================== test session starts ============================
    platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
    rootdir: /home/sweet/project
    collected 1 item

    test_tmp_path.py F                                                   [100%]

    ================================= FAILURES =================================
    _____________________________ test_create_file _____________________________

    tmp_path = PosixPath('PYTEST_TMPDIR/test_create_file0')

        def test_create_file(tmp_path):
            d = tmp_path / "sub"
            d.mkdir()
            p = d / "hello.txt"
            p.write_text(CONTENT, encoding="utf-8")
            assert p.read_text(encoding="utf-8") == CONTENT
            assert len(list(tmp_path.iterdir())) == 1
    >       assert 0
    E       assert 0

    test_tmp_path.py:11: AssertionError
    ========================= short test summary info ==========================
    FAILED test_tmp_path.py::test_create_file - assert 0
    ============================ 1 failed in 0.12s =============================

By default, [`pytest`] retains the temporary directory for the last 3 [`pytest`] invocations. Concurrent invocations of the same test function are supported by configuring the base temporary directory to be unique for each concurrent run. See [temporary directory location and retention](#temporary-directory-location-and-retention) for details.

[]

## The [`tmp_path_factory`] fixture[¶](#the-tmp-path-factory-fixture "Link to this heading")

The [`tmp_path_factory`] is a session-scoped fixture which can be used to create arbitrary temporary directories from any other fixture or test.

For example, suppose your test suite needs a large image on disk, which is generated procedurally. Instead of computing the same image for each test that uses it into its own [`tmp_path`], you can generate it once per-session to save time:

    # contents of conftest.py
    import pytest

    @pytest.fixture(scope="session")
    def image_file(tmp_path_factory):
        img = compute_expensive_image()
        fn = tmp_path_factory.mktemp("data") / "img.png"
        img.save(fn)
        return fn

    # contents of test_image.py
    def test_histogram(image_file):
        img = load_image(image_file)
        # compute and test histogram

See [[tmp_path_factory API]](../reference/reference.html#tmp-path-factory-factory-api) for details.

[][]

## The [`tmpdir`] and [`tmpdir_factory`] fixtures[¶](#the-tmpdir-and-tmpdir-factory-fixtures "Link to this heading")

The [`tmpdir`] and [`tmpdir_factory`] fixtures are similar to [`tmp_path`] and [`tmp_path_factory`], but use/return legacy [py.path.local](https://py.readthedocs.io/en/latest/path.html) objects rather than standard [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") objects.

Note

These days, it is preferred to use [`tmp_path`] and [`tmp_path_factory`].

In order to help modernize old code bases, one can run pytest with the legacypath plugin disabled:

    pytest -p no:legacypath

This will trigger errors on tests using the legacy paths. It can also be permanently set as part of the [[`addopts`]](../reference/reference.html#confval-addopts) parameter in the config file.

See [[`tmpdir`]](../reference/reference.html#std-fixture-tmpdir) [[`tmpdir_factory`]](../reference/reference.html#std-fixture-tmpdir_factory) API for details.

[]

## Temporary directory location and retention[¶](#temporary-directory-location-and-retention "Link to this heading")

The temporary directories, as returned by the [[`tmp_path`]](../reference/reference.html#std-fixture-tmp_path) and (now deprecated) [[`tmpdir`]](../reference/reference.html#std-fixture-tmpdir) fixtures, are automatically created under a base temporary directory, in a structure that depends on the [[`--basetemp`]](../reference/reference.html#cmdoption-basetemp) option:

-   By default (when the [[`--basetemp`]](../reference/reference.html#cmdoption-basetemp) option is not set), the temporary directories will follow this template:

    ::: 
    ::: highlight
        /pytest-of-/pytest-//
    :::
    :::

    where:

    -   [``] is the system temporary directory as determined by [[`tempfile.gettempdir()`]](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir "(in Python v3.14)"). It can be overridden by the [][[`PYTEST_DEBUG_TEMPROOT`]](../reference/reference.html#envvar-PYTEST_DEBUG_TEMPROOT) environment variable.

    -   [``] is the user name running the tests,

    -   [``] is a number that is incremented with each test suite run

    -   [``] is a sanitized version of [[`the`]` `[`name`]` `[`of`]` `[`the`]` `[`current`]` `[`test`]](../reference/reference.html#pytest.nodes.Node.name "_pytest.nodes.Node.name").

    The auto-incrementing [``] placeholder provides a basic retention feature and avoids that existing results of previous test runs are blindly removed. By default, the last 3 temporary directories are kept, but this behavior can be configured with [[`tmp_path_retention_count`]](../reference/reference.html#confval-tmp_path_retention_count) and [[`tmp_path_retention_policy`]](../reference/reference.html#confval-tmp_path_retention_policy).

-   When the [[`--basetemp`]](../reference/reference.html#cmdoption-basetemp) option is used (e.g. [`pytest`]` `[`--basetemp=mydir`]), it will be used directly as base temporary directory:

    ::: 
    ::: highlight
        //
    :::
    :::

    Note that there is no retention feature in this case: only the results of the most recent run will be kept.

    ::: 
    Warning

    The directory given to [[`--basetemp`]](../reference/reference.html#cmdoption-basetemp) will be cleared blindly before each test run, so make sure to use a directory for that purpose only.
    :::

When distributing tests on the local machine using [`pytest-xdist`], care is taken to automatically configure a [`basetemp`] directory for the sub processes such that all temporary data lands below a single per-test run temporary directory.