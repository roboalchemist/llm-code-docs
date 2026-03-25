# Source: https://docs.pytest.org/en/stable/how-to/mark.html

[]

# How to mark test functions with attributes[¶](#how-to-mark-test-functions-with-attributes "Link to this heading")

By using the [`pytest.mark`] helper you can easily set metadata on your test functions. You can find the full list of builtin markers in the [[API Reference]](../reference/reference.html#marks-ref). Or you can list all the markers, including builtin and custom, using the CLI - [`pytest`]` `[`--markers`].

Here are some of the builtin markers:

-   [[usefixtures]](fixtures.html#usefixtures) - use fixtures on a test function or class

-   [[filterwarnings]](capture-warnings.html#filterwarnings) - filter certain warnings of a test function

-   [[skip]](skipping.html#skip) - always skip a test function

-   [[skipif]](skipping.html#skipif) - skip a test function if a certain condition is met

-   [[xfail]](skipping.html#xfail) - produce an "expected failure" outcome if a certain condition is met

-   [[parametrize]](parametrize.html#parametrizemark) - perform multiple calls to the same test function.

It's easy to create custom markers or to apply markers to whole test classes or modules. Those markers can be used by plugins, and also are commonly used to [[select tests]](../example/markers.html#mark-run) on the command-line with the [[`-m`]](../reference/reference.html#cmdoption-m) option.

See [[Working with custom markers]](../example/markers.html#mark-examples) for examples which also serve as documentation.

Note

Marks can only be applied to tests, having no effect on [[fixtures]](../reference/fixtures.html#fixtures).

## Registering marks[¶](#registering-marks "Link to this heading")

You can register custom marks in your configuration file like this:

toml

    [pytest]
    markers = [
        "slow: marks tests as slow (deselect with '-m \"not slow\"')",
        "serial",
    ]

ini

    [pytest]
    markers =
        slow: marks tests as slow (deselect with '-m "not slow"')
        serial

Note that everything past the [`:`] after the mark name is an optional description.

Alternatively, you can register new markers programmatically in a [[pytest_configure]](../reference/reference.html#initialization-hooks) hook:

    def pytest_configure(config):
        config.addinivalue_line(
            "markers", "env(name): mark test to run only on named environment"
        )

Registered marks appear in pytest's help text and do not emit warnings (see the next section). It is recommended that third-party plugins always [[register their markers]](writing_plugins.html#registering-markers).

[]

## Raising errors on unknown marks[¶](#raising-errors-on-unknown-marks "Link to this heading")

Unregistered marks applied with the [`@pytest.mark.name_of_the_mark`] decorator will always emit a warning in order to avoid silently doing something surprising due to mistyped names. As described in the previous section, you can disable the warning for custom marks by registering them in your configuration file or using a custom [`pytest_configure`] hook.

When the [[`strict_markers`]](../reference/reference.html#confval-strict_markers) configuration option is set, any unknown marks applied with the [`@pytest.mark.name_of_the_mark`] decorator will trigger an error. You can enforce this validation in your project by setting [[`strict_markers`]](../reference/reference.html#confval-strict_markers) in your configuration:

toml

    [pytest]
    addopts = ["--strict-markers"]
    markers = [
        "slow: marks tests as slow (deselect with '-m \"not slow\"')",
        "serial",
    ]

ini

    [pytest]
    strict_markers = true
    markers =
        slow: marks tests as slow (deselect with '-m "not slow"')
        serial