# Source: https://docs.pytest.org/en/stable/changelog.html

[]

# Changelog[¶](#changelog "Link to this heading")

Versions follow [Semantic Versioning](https://semver.org/) ([`<major>.<minor>.<patch>`]).

Backward incompatible (breaking) changes will only be introduced in major versions with advance notice in the **Deprecations** section of releases.

## pytest 9.0.2 (2025-12-06)[¶](#pytest-9-0-2-2025-12-06 "Link to this heading")

### Bug fixes[¶](#bug-fixes "Link to this heading")

-   [#13896](https://github.com/pytest-dev/pytest/issues/13896): The terminal progress feature added in pytest 9.0.0 has been disabled by default, except on Windows, due to compatibility issues with some terminal emulators.

    You may enable it again by passing [`-p`]` `[`terminalprogress`]. We may enable it by default again once compatibility improves in the future.

    Additionally, when the environment variable [`TERM`] is [`dumb`], the escape codes are no longer emitted, even if the plugin is enabled.

-   [#13904](https://github.com/pytest-dev/pytest/issues/13904): Fixed the TOML type of the [[`tmp_path_retention_count`]](reference/reference.html#confval-tmp_path_retention_count) settings in the API reference from number to string.

-   [#13946](https://github.com/pytest-dev/pytest/issues/13946): The private [`config.inicfg`] attribute was changed in a breaking manner in pytest 9.0.0. Due to its usage in the ecosystem, it is now restored to working order using a compatibility shim. It will be deprecated in pytest 9.1 and removed in pytest 10.

-   [#13965](https://github.com/pytest-dev/pytest/issues/13965): Fixed quadratic-time behavior when handling [`unittest`] subtests in Python 3.10.

### Improved documentation[¶](#improved-documentation "Link to this heading")

-   [#4492](https://github.com/pytest-dev/pytest/issues/4492): The API Reference now contains cross-reference-able documentation of [[pytest's command-line flags]](reference/reference.html#command-line-flags).

## pytest 9.0.1 (2025-11-12)[¶](#pytest-9-0-1-2025-11-12 "Link to this heading")

### Bug fixes[¶](#id7 "Link to this heading")

-   [#13895](https://github.com/pytest-dev/pytest/issues/13895): Restore support for skipping tests via [`raise`]` `[`unittest.SkipTest`].

-   [#13896](https://github.com/pytest-dev/pytest/issues/13896): The terminal progress plugin added in pytest 9.0 is now automatically disabled when iTerm2 is detected, it generated desktop notifications instead of the desired functionality.

-   [#13904](https://github.com/pytest-dev/pytest/issues/13904): Fixed the TOML type of the verbosity settings in the API reference from number to string.

-   [#13910](https://github.com/pytest-dev/pytest/issues/13910): Fixed [`UserWarning:`]` `[`Do`]` `[`not`]` `[`expect`]` `[`file_or_dir`] on some earlier Python 3.12 and 3.13 point versions.

### Packaging updates and notes for downstreams[¶](#packaging-updates-and-notes-for-downstreams "Link to this heading")

-   [#13933](https://github.com/pytest-dev/pytest/issues/13933): The tox configuration has been adjusted to make sure the desired version string can be passed into its [[package_env]](https://tox.wiki/en/stable/config.html#package_env "(in Project name not set v4.32)") through the [`SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYTEST`] environment variable as a part of the release process -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

### Contributor-facing changes[¶](#contributor-facing-changes "Link to this heading")

-   [#13891](https://github.com/pytest-dev/pytest/issues/13891), [#13942](https://github.com/pytest-dev/pytest/issues/13942): The CI/CD part of the release automation is now capable of creating GitHub Releases without having a Git checkout on disk -- by [\@bluetech](https://github.com/sponsors/bluetech) and [\@webknjaz](https://github.com/sponsors/webknjaz).

-   [#13933](https://github.com/pytest-dev/pytest/issues/13933): The tox configuration has been adjusted to make sure the desired version string can be passed into its [[package_env]](https://tox.wiki/en/stable/config.html#package_env "(in Project name not set v4.32)") through the [`SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYTEST`] environment variable as a part of the release process -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

## pytest 9.0.0 (2025-11-05)[¶](#pytest-9-0-0-2025-11-05 "Link to this heading")

### New features[¶](#new-features "Link to this heading")

-   [#1367](https://github.com/pytest-dev/pytest/issues/1367): **Support for subtests** has been added.

    [[subtests]](how-to/subtests.html#subtests) are an alternative to parametrization, useful in situations where the parametrization values are not all known at collection time.

    Example:

    ::: 
    ::: highlight
        def contains_docstring(p: Path) -> bool:
            """Return True if the given Python file contains a top-level docstring."""
            ...

        def test_py_files_contain_docstring(subtests: pytest.Subtests) -> None:
            for path in Path.cwd().glob("*.py"):
                with subtests.test(path=str(path)):
                    assert contains_docstring(path)
    :::
    :::

    Each assert failure or error is caught by the context manager and reported individually, giving a clear picture of all files that are missing a docstring.

    In addition, [[`unittest.TestCase.subTest()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "(in Python v3.14)") is now also supported.

    This feature was originally implemented as a separate plugin in [pytest-subtests](https://github.com/pytest-dev/pytest-subtests), but since then has been merged into the core.

    ::: 
    Note

    This feature is experimental and will likely evolve in future releases. By that we mean that we might change how subtests are reported on failure, but the functionality and how to use it are stable.
    :::

-   [#13743](https://github.com/pytest-dev/pytest/issues/13743): Added support for **native TOML configuration files**.

    While pytest, since version 6, supports configuration in [`pyproject.toml`] files under [`[tool.pytest.ini_options]`], it does so in an "INI compatibility mode", where all configuration values are treated as strings or list of strings. Now, pytest supports the native TOML data model.

    In [`pyproject.toml`], the native TOML configuration is under the [`[tool.pytest]`] table.

    ::: 
    ::: highlight
        # pyproject.toml
        [tool.pytest]
        minversion = "9.0"
        addopts = ["-ra", "-q"]
        testpaths = [
            "tests",
            "integration",
        ]
    :::
    :::

    The [`[tool.pytest.ini_options]`] table remains supported, but both tables cannot be used at the same time.

    If you prefer to use a separate configuration file, or don't use [`pyproject.toml`], you can use [`pytest.toml`] or [`.pytest.toml`]:

    ::: 
    ::: highlight
        # pytest.toml or .pytest.toml
        [pytest]
        minversion = "9.0"
        addopts = ["-ra", "-q"]
        testpaths = [
            "tests",
            "integration",
        ]
    :::
    :::

    The documentation now (sometimes) shows configuration snippets in both TOML and INI formats, in a tabbed interface.

    See [[Configuration file formats]](reference/customize.html#config-file-formats) for full details.

-   [#13823](https://github.com/pytest-dev/pytest/issues/13823): Added a **"strict mode"** enabled by the [[`strict`]](reference/reference.html#confval-strict) configuration option.

    When set to [`true`], the [[`strict`]](reference/reference.html#confval-strict) option currently enables

    -   [[`strict_config`]](reference/reference.html#confval-strict_config)

    -   [[`strict_markers`]](reference/reference.html#confval-strict_markers)

    -   [[`strict_parametrization_ids`]](reference/reference.html#confval-strict_parametrization_ids)

    -   [[`strict_xfail`]](reference/reference.html#confval-strict_xfail)

    The individual strictness options can be explicitly set to override the global [[`strict`]](reference/reference.html#confval-strict) setting.

    The previously-deprecated [`--strict`] command-line flag now enables strict mode.

    If pytest adds new strictness options in the future, they will also be enabled in strict mode. Therefore, you should only enable strict mode if you use a pinned/locked version of pytest, or if you want to proactively adopt new strictness options as they are added.

    See [[Using pytest's strict mode]](explanation/goodpractices.html#strict-mode) for more details.

-   [#13737](https://github.com/pytest-dev/pytest/issues/13737): Added the [[`strict_parametrization_ids`]](reference/reference.html#confval-strict_parametrization_ids) configuration option.

    When set, pytest emits an error if it detects non-unique parameter set IDs, rather than automatically making the IDs unique by adding [`0`], [`1`], ... to them. This can be particularly useful for catching unintended duplicates.

-   [#13072](https://github.com/pytest-dev/pytest/issues/13072): Added support for displaying test session **progress in the terminal tab** using the [OSC 9;4;](https://conemu.github.io/en/AnsiEscapeCodes.html#ConEmu_specific_OSC) ANSI sequence.

    **Note**: *This feature has been disabled by default in version 9.0.2, except on Windows, due to compatibility issues with some terminal emulators. You may enable it again by passing* [`-p`]` `[`terminalprogress`]. *We may enable it by default again once compatibility improves in the future.*

    When pytest runs in a supported terminal emulator like ConEmu, Gnome Terminal, Ptyxis, Windows Terminal, Kitty or Ghostty, you'll see the progress in the terminal tab or window, allowing you to monitor pytest's progress at a glance.

    This feature is automatically enabled when running in a TTY. It is implemented as an internal plugin. If needed, it can be disabled as follows: - On a user level, using [`-p`]` `[`no:terminalprogress`] on the command line or via an environment variable [`PYTEST_ADDOPTS='-p`]` `[`no:terminalprogress'`]. - On a project configuration level, using [`addopts`]` `[`=`]` `[`"-p`]` `[`no:terminalprogress"`].

-   [#478](https://github.com/pytest-dev/pytest/issues/478): Support PEP420 (implicit namespace packages) as [`--pyargs`] target when [[`consider_namespace_packages`]](reference/reference.html#confval-consider_namespace_packages) is [`true`] in the config.

    Previously, this option only impacted package imports, now it also impacts tests discovery.

-   [#13678](https://github.com/pytest-dev/pytest/issues/13678): Added a new [[`faulthandler_exit_on_timeout`]](reference/reference.html#confval-faulthandler_exit_on_timeout) configuration option set to "false" by default to let [`faulthandler`] interrupt the [`pytest`] process after a timeout in case of deadlock.

    Previously, a [`faulthandler`] timeout would only dump the traceback of all threads to stderr, but would not interrupt the [`pytest`] process.

    -- by [\@ogrisel](https://github.com/sponsors/ogrisel).

-   [#13829](https://github.com/pytest-dev/pytest/issues/13829): Added support for configuration option aliases via the [`aliases`] parameter in [[`Parser.addini()`]](reference/reference.html#pytest.Parser.addini "pytest.Parser.addini").

    Plugins can now register alternative names for configuration options, allowing for more flexibility in configuration naming and supporting backward compatibility when renaming options. The canonical name always takes precedence if both the canonical name and an alias are specified in the configuration file.

### Improvements in existing functionality[¶](#improvements-in-existing-functionality "Link to this heading")

-   [#13330](https://github.com/pytest-dev/pytest/issues/13330): Having pytest configuration spread over more than one file (for example having both a [`pytest.ini`] file and [`pyproject.toml`] with a [`[tool.pytest.ini_options]`] table) will now print a warning to make it clearer to the user that only one of them is actually used.

    -- by [\@sgaist](https://github.com/sponsors/sgaist)

-   [#13574](https://github.com/pytest-dev/pytest/issues/13574): The single argument [`--version`] no longer loads the entire plugin infrastructure, making it faster and more reliable when displaying only the pytest version.

    Passing [`--version`] twice (e.g., [`pytest`]` `[`--version`]` `[`--version`]) retains the original behavior, showing both the pytest version and plugin information.

    ::: 
    Note

    Since [`--version`] is now processed early, it only takes effect when passed directly via the command line. It will not work if set through other mechanisms, such as [][[`PYTEST_ADDOPTS`]](reference/reference.html#envvar-PYTEST_ADDOPTS) or [[`addopts`]](reference/reference.html#confval-addopts).
    :::

-   [#13823](https://github.com/pytest-dev/pytest/issues/13823): Added [[`strict_xfail`]](reference/reference.html#confval-strict_xfail) as an alias to the [`xfail_strict`] option, [[`strict_config`]](reference/reference.html#confval-strict_config) as an alias to the [`--strict-config`] flag, and [[`strict_markers`]](reference/reference.html#confval-strict_markers) as an alias to the [`--strict-markers`] flag. This makes all strictness options consistently have configuration options with the prefix [`strict_`].

-   [#13700](https://github.com/pytest-dev/pytest/issues/13700): [`--junitxml`] no longer prints the [`generated`]` `[`xml`]` `[`file`] summary at the end of the pytest session when [`--quiet`] is given.

-   [#13732](https://github.com/pytest-dev/pytest/issues/13732): Previously, when filtering warnings, pytest would fail if the filter referenced a class that could not be imported. Now, this only outputs a message indicating the problem.

-   [#13859](https://github.com/pytest-dev/pytest/issues/13859): Clarify the error message for [`pytest.raises()`] when a regex [`match`] fails.

-   [#13861](https://github.com/pytest-dev/pytest/issues/13861): Better sentence structure in a test's expected error message. Previously, the error message would be "expected exception must be \<expected\>, but got \<actual\>". Now, it is "Expected \<expected\>, but got \<actual\>".

### Removals and backward incompatible breaking changes[¶](#removals-and-backward-incompatible-breaking-changes "Link to this heading")

-   [#12083](https://github.com/pytest-dev/pytest/issues/12083): Fixed a bug where an invocation such as [`pytest`]` `[`a/`]` `[`a/b`] would cause only tests from [`a/b`] to run, and not other tests under [`a/`].

    The fix entails a few breaking changes to how such overlapping arguments and duplicates are handled:

    1.  [`pytest`]` `[`a/b`]` `[`a/`] or [`pytest`]` `[`a/`]` `[`a/b`] are equivalent to [`pytest`]` `[`a`]; if an argument overlaps another arguments, only the prefix remains.

    2.  [`pytest`]` `[`x.py`]` `[`x.py`] is equivalent to [`pytest`]` `[`x.py`]; previously such an invocation was taken as an explicit request to run the tests from the file twice.

    If you rely on these behaviors, consider using [[--keep-duplicates]](example/pythoncollection.html#duplicate-paths), which retains its existing behavior (including the bug).

-   [#13719](https://github.com/pytest-dev/pytest/issues/13719): Support for Python 3.9 is dropped following its end of life.

-   [#13766](https://github.com/pytest-dev/pytest/issues/13766): Previously, pytest would assume it was running in a CI/CD environment if either of the environment variables [`$CI`] or [`$BUILD_NUMBER`] was defined; now, CI mode is only activated if at least one of those variables is defined and set to a *non-empty* value.

-   The non-public [`config.args`] attribute used to be able to contain [`pathlib.Path`] instances; now it can only contain strings.

-   [#13779](https://github.com/pytest-dev/pytest/issues/13779): **PytestRemovedIn9Warning deprecation warnings are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`PytestRemovedIn9Warning`] now generate errors instead of warning messages by default.

    **The affected features will be effectively removed in pytest 9.1**, so please consult the [[Deprecations and Removals]](deprecations.html#deprecations) section in the docs for directions on how to update existing code.

    In the pytest [`9.0.X`] series, it is possible to change the errors back into warnings as a stopgap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.PytestRemovedIn9Warning
    :::
    :::

    But this will stop working when pytest [`9.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#13779](https://github.com/pytest-dev/pytest/issues/13779).

### Deprecations (removal in next major release)[¶](#deprecations-removal-in-next-major-release "Link to this heading")

-   [#13807](https://github.com/pytest-dev/pytest/issues/13807): [[`monkeypatch.syspath_prepend()`]](reference/reference.html#pytest.MonkeyPatch.syspath_prepend "pytest.MonkeyPatch.syspath_prepend") now issues a deprecation warning when the prepended path contains legacy namespace packages (those using [`pkg_resources.declare_namespace()`]). Users should migrate to native namespace packages ([][**PEP 420**](https://peps.python.org/pep-0420/)). See [[monkeypatch.syspath_prepend with legacy namespace packages]](deprecations.html#monkeypatch-fixup-namespace-packages) for details.

### Bug fixes[¶](#id36 "Link to this heading")

-   [#13445](https://github.com/pytest-dev/pytest/issues/13445): Made the type annotations of [[`pytest.skip()`]](reference/reference.html#pytest.skip "pytest.skip") and friends more spec-complaint to have them work across more type checkers.

-   [#13537](https://github.com/pytest-dev/pytest/issues/13537): Fixed a bug in which [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)") with only [`Skipped`] exceptions in teardown was not handled correctly and showed as error.

-   [#13598](https://github.com/pytest-dev/pytest/issues/13598): Fixed possible collection confusion on Windows when short paths and symlinks are involved.

-   [#13716](https://github.com/pytest-dev/pytest/issues/13716): Fixed a bug where a nonsensical invocation like [`pytest`]` `[`x.py[a]`] (a file cannot be parametrized) was silently treated as [`pytest`]` `[`x.py`]. This is now a usage error.

-   [#13722](https://github.com/pytest-dev/pytest/issues/13722): Fixed a misleading assertion failure message when using [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") on mappings with differing lengths.

-   [#13773](https://github.com/pytest-dev/pytest/issues/13773): Fixed the static fixture closure calculation to properly consider transitive dependencies requested by overridden fixtures.

-   [#13816](https://github.com/pytest-dev/pytest/issues/13816): Fixed [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") which now returns a clearer error message when comparing mappings with different keys.

-   [#13849](https://github.com/pytest-dev/pytest/issues/13849): Hidden [`.pytest.ini`] files are now picked up as the config file even if empty. This was an inconsistency with non-hidden [`pytest.ini`].

-   [#13865](https://github.com/pytest-dev/pytest/issues/13865): Fixed [`--show-capture`] with [`--tb=line`].

-   [#13522](https://github.com/pytest-dev/pytest/issues/13522): Fixed [[`pytester`]](reference/reference.html#std-fixture-pytester) in subprocess mode ignored all [[`pytester.plugins`]](reference/reference.html#pytest.Pytester.plugins "pytest.Pytester.plugins") except the first.

    Fixed [[`pytester`]](reference/reference.html#std-fixture-pytester) in subprocess mode silently ignored non-str [[`pytester.plugins`]](reference/reference.html#pytest.Pytester.plugins "pytest.Pytester.plugins"). Now it errors instead. If you are affected by this, specify the plugin by name, or switch the affected tests to use [[`pytester.runpytest_inprocess`]](reference/reference.html#pytest.Pytester.runpytest_inprocess "pytest.Pytester.runpytest_inprocess") explicitly instead.

### Packaging updates and notes for downstreams[¶](#id47 "Link to this heading")

-   [#13791](https://github.com/pytest-dev/pytest/issues/13791): Minimum requirements on [`iniconfig`] and [`packaging`] were bumped to [`1.0.1`] and [`22.0.0`], respectively.

### Contributor-facing changes[¶](#id49 "Link to this heading")

-   [#12244](https://github.com/pytest-dev/pytest/issues/12244): Fixed self-test failures when [`TERM=dumb`].

-   [#12474](https://github.com/pytest-dev/pytest/issues/12474): Added scheduled GitHub Action Workflow to run Sphinx linkchecks in repo documentation.

-   [#13621](https://github.com/pytest-dev/pytest/issues/13621): pytest's own testsuite now handles the [`lsof`] command hanging (e.g. due to unreachable network filesystems), with the affected selftests being skipped after 10 seconds.

-   [#13638](https://github.com/pytest-dev/pytest/issues/13638): Fixed deprecated **gh pr new** command in [`scripts/prepare-release-pr.py`]. The script now uses **gh pr create** which is compatible with GitHub CLI v2.0+.

-   [#13695](https://github.com/pytest-dev/pytest/issues/13695): Flush [`stdout`] and [`stderr`] in [`Pytester.run`] to avoid truncated outputs in [`test_faulthandler.py::test_timeout`] on CI -- by [\@ogrisel](https://github.com/sponsors/ogrisel).

-   [#13771](https://github.com/pytest-dev/pytest/issues/13771): Skip [`test_do_not_collect_symlink_siblings`] on Windows environments without symlink support to avoid false negatives.

-   [#13841](https://github.com/pytest-dev/pytest/issues/13841): [`tox>=4`] is now required when contributing to pytest.

-   [#13625](https://github.com/pytest-dev/pytest/issues/13625): Added missing docstrings to [`pytest_addoption()`], [`pytest_configure()`], and [`cacheshow()`] functions in [`cacheprovider.py`].

### Miscellaneous internal changes[¶](#miscellaneous-internal-changes "Link to this heading")

-   [#13830](https://github.com/pytest-dev/pytest/issues/13830): Configuration overrides ([`-o`]/[`--override-ini`]) are now processed during startup rather than during [[`config.getini()`]](reference/reference.html#pytest.Config.getini "pytest.Config.getini").

## pytest 8.4.2 (2025-09-03)[¶](#pytest-8-4-2-2025-09-03 "Link to this heading")

### Bug fixes[¶](#id59 "Link to this heading")

-   [#13478](https://github.com/pytest-dev/pytest/issues/13478): Fixed a crash when using [[`console_output_style`]](reference/reference.html#confval-console_output_style) with [`times`] and a module is skipped.

-   [#13530](https://github.com/pytest-dev/pytest/issues/13530): Fixed a crash when using [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") and [[`decimal.Decimal`]](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") instances with the [[`decimal.FloatOperation`]](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "(in Python v3.14)") trap set.

-   [#13549](https://github.com/pytest-dev/pytest/issues/13549): No longer evaluate type annotations in Python [`3.14`] when inspecting function signatures.

    This prevents crashes during module collection when modules do not explicitly use [`from`]` `[`__future__`]` `[`import`]` `[`annotations`] and import types for annotations within a [`if`]` `[`TYPE_CHECKING:`] block.

-   [#13559](https://github.com/pytest-dev/pytest/issues/13559): Added missing [`int`] and [`float`] variants to the [`Literal`] type annotation of the [`type`] parameter in [[`pytest.Parser.addini()`]](reference/reference.html#pytest.Parser.addini "pytest.Parser.addini").

-   [#13563](https://github.com/pytest-dev/pytest/issues/13563): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now only imports [`numpy`] if NumPy is already in [`sys.modules`]. This fixes unconditional import behavior introduced in [`8.4.0`].

### Improved documentation[¶](#id65 "Link to this heading")

-   [#13577](https://github.com/pytest-dev/pytest/issues/13577): Clarify that [`pytest_generate_tests`] is discovered in test modules/classes; other hooks must be in [`conftest.py`] or plugins.

### Contributor-facing changes[¶](#id67 "Link to this heading")

-   [#13480](https://github.com/pytest-dev/pytest/issues/13480): Self-testing: fixed a few test failures when run with [`-Wdefault`] or a similar override.

-   [#13547](https://github.com/pytest-dev/pytest/issues/13547): Self-testing: corrected expected message for [`test_doctest_unexpected_exception`] in Python [`3.14`].

-   [#13684](https://github.com/pytest-dev/pytest/issues/13684): Make pytest's own testsuite insensitive to the presence of the [`CI`] environment variable -- by [\@ogrisel](https://github.com/sponsors/ogrisel).

## pytest 8.4.1 (2025-06-17)[¶](#pytest-8-4-1-2025-06-17 "Link to this heading")

### Bug fixes[¶](#id71 "Link to this heading")

-   [#13461](https://github.com/pytest-dev/pytest/issues/13461): Corrected [`_pytest.terminal.TerminalReporter.isatty`] to support being called as a method. Before it was just a boolean which could break correct code when using [`-o`]` `[`log_cli=true`]).

-   [#13477](https://github.com/pytest-dev/pytest/issues/13477): Reintroduced [[`pytest.PytestReturnNotNoneWarning`]](reference/reference.html#pytest.PytestReturnNotNoneWarning "pytest.PytestReturnNotNoneWarning") which was removed by accident in pytest [`8.4`].

    This warning is raised when a test functions returns a value other than [`None`], which is often a mistake made by beginners.

    See [[Returning non-None value in test functions]](how-to/assert.html#return-not-none) for more information.

-   [#13497](https://github.com/pytest-dev/pytest/issues/13497): Fixed compatibility with [`Twisted`]` `[`25+`].

### Improved documentation[¶](#id75 "Link to this heading")

-   [#13492](https://github.com/pytest-dev/pytest/issues/13492): Fixed outdated warning about [`faulthandler`] not working on Windows.

## pytest 8.4.0 (2025-06-02)[¶](#pytest-8-4-0-2025-06-02 "Link to this heading")

### Removals and backward incompatible breaking changes[¶](#id77 "Link to this heading")

-   [#11372](https://github.com/pytest-dev/pytest/issues/11372): Async tests will now fail, instead of warning+skipping, if you don't have any suitable plugin installed.

-   [#12346](https://github.com/pytest-dev/pytest/issues/12346): Tests will now fail, instead of raising a warning, if they return any value other than None.

-   [#12874](https://github.com/pytest-dev/pytest/issues/12874): We dropped support for Python 3.8 following its end of life (2024-10-07).

-   [#12960](https://github.com/pytest-dev/pytest/issues/12960): Test functions containing a yield now cause an explicit error. They have not been run since pytest 4.0, and were previously marked as an expected failure and deprecation warning.

    See [[the docs]](deprecations.html#yield-tests-deprecated) for more information.

### Deprecations (removal in next major release)[¶](#id82 "Link to this heading")

-   [#10839](https://github.com/pytest-dev/pytest/issues/10839): Requesting an asynchronous fixture without a [`pytest_fixture_setup`] hook that resolves it will now give a DeprecationWarning. This most commonly happens if a sync test requests an async fixture. This should have no effect on a majority of users with async tests or fixtures using async pytest plugins, but may affect non-standard hook setups or [`autouse=True`]. For guidance on how to work around this warning see [[sync test depending on async fixture]](deprecations.html#sync-test-async-fixture).

### New features[¶](#id84 "Link to this heading")

-   [#11538](https://github.com/pytest-dev/pytest/issues/11538): Added [[`pytest.RaisesGroup`]](reference/reference.html#pytest.RaisesGroup "pytest.RaisesGroup") as an equivalent to [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") for expecting [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)"). Also adds [[`pytest.RaisesExc`]](reference/reference.html#pytest.RaisesExc "pytest.RaisesExc") which is now the logic behind [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") and used as parameter to [[`pytest.RaisesGroup`]](reference/reference.html#pytest.RaisesGroup "pytest.RaisesGroup"). [`RaisesGroup`] includes the ability to specify multiple different expected exceptions, the structure of nested exception groups, and flags for emulating [[except\*]](https://docs.python.org/3/reference/compound_stmts.html#except-star "(in Python v3.14)"). See [[Assertions about expected exception groups]](how-to/assert.html#assert-matching-exception-groups) and docstrings for more information.

-   [#12081](https://github.com/pytest-dev/pytest/issues/12081): Added [[`capteesys`]](reference/reference.html#std-fixture-capteesys) to capture AND pass output to next handler set by [`--capture=`].

-   [#12504](https://github.com/pytest-dev/pytest/issues/12504): [[`pytest.mark.xfail()`]](reference/reference.html#pytest.mark.xfail "pytest.mark.xfail") now accepts [[`pytest.RaisesGroup`]](reference/reference.html#pytest.RaisesGroup "pytest.RaisesGroup") for the [`raises`] parameter when you expect an exception group. You can also pass a [[`pytest.RaisesExc`]](reference/reference.html#pytest.RaisesExc "pytest.RaisesExc") if you e.g. want to make use of the [`check`] parameter.

-   [#12713](https://github.com/pytest-dev/pytest/issues/12713): New [`--force-short-summary`] option to force condensed summary output regardless of verbosity level.

    This lets users still see condensed summary output of failures for quick reference in log files from job outputs, being especially useful if non-condensed output is very verbose.

-   [#12749](https://github.com/pytest-dev/pytest/issues/12749): pytest traditionally collects classes/functions in the test module namespace even if they are imported from another file.

    For example:

    ::: 
    ::: highlight
        # contents of src/domain.py
        class Testament: ...

        # contents of tests/test_testament.py
        from domain import Testament

        def test_testament(): ...
    :::
    :::

    In this scenario with the default options, pytest will collect the class [`Testament`] from [`tests/test_testament.py`] because it starts with [`Test`], even though in this case it is a production class being imported in the test module namespace.

    This behavior can now be prevented by setting the new [[`collect_imported_tests`]](reference/reference.html#confval-collect_imported_tests) configuration option to [`false`], which will make pytest collect classes/functions from test files **only** if they are defined in that file.

    -- by [\@FreerGit](https://github.com/sponsors/FreerGit)

-   [#12765](https://github.com/pytest-dev/pytest/issues/12765): Thresholds to trigger snippet truncation can now be set with [[`truncation_limit_lines`]](reference/reference.html#confval-truncation_limit_lines) and [[`truncation_limit_chars`]](reference/reference.html#confval-truncation_limit_chars).

    See [[Modifying truncation limits]](how-to/output.html#truncation-params) for more information.

-   [#13125](https://github.com/pytest-dev/pytest/issues/13125): [[`console_output_style`]](reference/reference.html#confval-console_output_style) now supports [`times`] to show execution time of each test.

-   [#13192](https://github.com/pytest-dev/pytest/issues/13192): [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") will now raise a warning when passing an empty string to [`match`], as this will match against any value. Use [`match="^$"`] if you want to check that an exception has no message.

-   [#13192](https://github.com/pytest-dev/pytest/issues/13192): [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") will now print a helpful string diff if matching fails and the match parameter has [`^`] and [`$`] and is otherwise escaped.

-   [#13192](https://github.com/pytest-dev/pytest/issues/13192): You can now pass [[`with`]` `[`pytest.raises(check=fn):`]](reference/reference.html#pytest.raises "pytest.raises"), where [`fn`] is a function which takes a raised exception and returns a boolean. The [`raises`] fails if no exception was raised (as usual), passes if an exception is raised and [`fn`] returns [`True`] (as well as [`match`] and the type matching, if specified, which are checked before), and propagates the exception if [`fn`] returns [`False`] (which likely also fails the test).

-   [#13228](https://github.com/pytest-dev/pytest/issues/13228): [[pytest.HIDDEN_PARAM]](reference/reference.html#hidden-param) can now be used in [`id`] of [[`pytest.param()`]](reference/reference.html#pytest.param "pytest.param") or in [`ids`] of [[`Metafunc.parametrize`]](reference/reference.html#pytest.Metafunc.parametrize "pytest.Metafunc.parametrize"). It hides the parameter set from the test name.

-   [#13253](https://github.com/pytest-dev/pytest/issues/13253): New flag: [[--disable-plugin-autoload]](how-to/plugins.html#disable-plugin-autoload) which works as an alternative to [][[`PYTEST_DISABLE_PLUGIN_AUTOLOAD`]](reference/reference.html#envvar-PYTEST_DISABLE_PLUGIN_AUTOLOAD) when setting environment variables is inconvenient; and allows setting it in config files with [[`addopts`]](reference/reference.html#confval-addopts).

### Improvements in existing functionality[¶](#id97 "Link to this heading")

-   [#10224](https://github.com/pytest-dev/pytest/issues/10224): pytest's [`short`] and [`long`] traceback styles ([[Modifying Python traceback printing]](how-to/output.html#how-to-modifying-python-tb-printing)) now have partial [][**PEP 657**](https://peps.python.org/pep-0657/) support and will show specific code segments in the traceback.

    ::: 
    ::: highlight
        ================================= FAILURES =================================
        _______________________ test_gets_correct_tracebacks _______________________

        test_tracebacks.py:12: in test_gets_correct_tracebacks
            assert manhattan_distance(p1, p2) == 1
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
        test_tracebacks.py:6: in manhattan_distance
            return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)
                                   ^^^^^^^^^
        E   AttributeError: 'NoneType' object has no attribute 'x'
    :::
    :::

    -- by [\@ammaraskar](https://github.com/sponsors/ammaraskar)

-   [#11118](https://github.com/pytest-dev/pytest/issues/11118): Now [[`pythonpath`]](reference/reference.html#confval-pythonpath) configures [`$PYTHONPATH`] earlier than before during the initialization process, which now also affects plugins loaded via the [`-p`] command-line option.

    -- by [\@millerdev](https://github.com/sponsors/millerdev)

-   [#11381](https://github.com/pytest-dev/pytest/issues/11381): The [`type`] parameter of the [`parser.addini`] method now accepts [`"int"`] and [`"float"`] parameters, facilitating the parsing of configuration values in the configuration file.

    Example:

    ::: 
    ::: highlight
        def pytest_addoption(parser):
            parser.addini("int_value", type="int", default=2, help="my int value")
            parser.addini("float_value", type="float", default=4.2, help="my float value")
    :::
    :::

    The [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        int_value = 3
        float_value = 5.4
    :::
    :::

-   [#11525](https://github.com/pytest-dev/pytest/issues/11525): Fixtures are now clearly represented in the output as a "fixture object", not as a normal function as before, making it easy for beginners to catch mistakes such as referencing a fixture declared in the same module but not requested in the test function.

    -- by [\@the-compiler](https://github.com/sponsors/the-compiler) and [\@glyphack](https://github.com/sponsors/glyphack)

-   [#12426](https://github.com/pytest-dev/pytest/issues/12426): A warning is now issued when [[pytest.mark.usefixtures]](reference/reference.html#pytest-mark-usefixtures-ref) is used without specifying any fixtures. Previously, empty usefixtures markers were silently ignored.

-   [#12707](https://github.com/pytest-dev/pytest/issues/12707): Exception chains can be navigated when dropped into Pdb in Python 3.13+.

-   [#12736](https://github.com/pytest-dev/pytest/issues/12736): Added a new attribute [`name`] with the fixed value [`"pytest`]` `[`tests"`] to the root tag [`testsuites`] of the junit-xml generated by pytest.

    This attribute is part of many junit-xml specifications and is even part of the [`junit-10.xsd`] specification that pytest's implementation is based on.

-   [#12943](https://github.com/pytest-dev/pytest/issues/12943): If a test fails with an exceptiongroup with a single exception, the contained exception will now be displayed in the short test summary info.

-   [#12958](https://github.com/pytest-dev/pytest/issues/12958): A number of [[unraisable]](how-to/failures.html#unraisable) enhancements:

    -   Set the unraisable hook as early as possible and unset it as late as possible, to collect the most possible number of unraisable exceptions.

    -   Call the garbage collector just before unsetting the unraisable hook, to collect any straggling exceptions.

    -   Collect multiple unraisable exceptions per test phase.

    -   Report the [[`tracemalloc`]](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "(in Python v3.14)") allocation traceback (if available).

    -   Avoid using a generator based hook to allow handling [[`StopIteration`]](https://docs.python.org/3/library/exceptions.html#StopIteration "(in Python v3.14)") in test failures.

    -   Report the unraisable exception as the cause of the [[`pytest.PytestUnraisableExceptionWarning`]](reference/reference.html#pytest.PytestUnraisableExceptionWarning "pytest.PytestUnraisableExceptionWarning") exception if raised.

    -   Compute the [`repr`] of the unraisable object in the unraisable hook so you get the latest information if available, and should help with resurrection of the object.

-   [#13010](https://github.com/pytest-dev/pytest/issues/13010): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now can compare collections that contain numbers and non-numbers mixed.

-   [#13016](https://github.com/pytest-dev/pytest/issues/13016): A number of [[threadexception]](how-to/failures.html#unraisable) enhancements:

    -   Set the excepthook as early as possible and unset it as late as possible, to collect the most possible number of unhandled exceptions from threads.

    -   Collect multiple thread exceptions per test phase.

    -   Report the [[`tracemalloc`]](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "(in Python v3.14)") allocation traceback (if available).

    -   Avoid using a generator based hook to allow handling [[`StopIteration`]](https://docs.python.org/3/library/exceptions.html#StopIteration "(in Python v3.14)") in test failures.

    -   Report the thread exception as the cause of the [[`pytest.PytestUnhandledThreadExceptionWarning`]](reference/reference.html#pytest.PytestUnhandledThreadExceptionWarning "pytest.PytestUnhandledThreadExceptionWarning") exception if raised.

    -   Extract the [`name`] of the thread object in the excepthook which should help with resurrection of the thread.

-   [#13031](https://github.com/pytest-dev/pytest/issues/13031): An empty parameter set as in [`pytest.mark.parametrize([],`]` `[`ids=idfunc)`] will no longer trigger a call to [`idfunc`] with internal objects.

-   [#13115](https://github.com/pytest-dev/pytest/issues/13115): Allows supplying [`ExceptionGroup[Exception]`] and [`BaseExceptionGroup[BaseException]`] to [`pytest.raises`] to keep full typing on [[`ExceptionInfo`]](reference/reference.html#pytest.ExceptionInfo "pytest.ExceptionInfo"):

    ::: 
    ::: highlight
        with pytest.raises(ExceptionGroup[Exception]) as exc_info:
            some_function()
    :::
    :::

    Parametrizing with other exception types remains an error - we do not check the types of child exceptions and thus do not permit code that might look like we do.

-   [#13122](https://github.com/pytest-dev/pytest/issues/13122): The [`--stepwise`] mode received a number of improvements:

    -   It no longer forgets the last failed test in case pytest is executed later without the flag.

        This enables the following workflow:

        1.  Execute pytest with [`--stepwise`], pytest then stops at the first failing test;

        2.  Iteratively update the code and run the test in isolation, without the [`--stepwise`] flag (for example in an IDE), until it is fixed.

        3.  Execute pytest with [`--stepwise`] again and pytest will continue from the previously failed test, and if it passes, continue on to the next tests.

        Previously, at step 3, pytest would start from the beginning, forgetting the previously failed test.

        This change however might cause issues if the [`--stepwise`] mode is used far apart in time, as the state might get stale, so the internal state will be reset automatically in case the test suite changes (for now only the number of tests are considered for this, we might change/improve this on the future).

    -   New [`--stepwise-reset`]/[`--sw-reset`] flag, allowing the user to explicitly reset the stepwise state and restart the workflow from the beginning.

-   [#13308](https://github.com/pytest-dev/pytest/issues/13308): Added official support for Python 3.14.

-   [#13380](https://github.com/pytest-dev/pytest/issues/13380): Fix [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)") traceback filtering to exclude pytest internals.

-   [#13415](https://github.com/pytest-dev/pytest/issues/13415): The author metadata of the BibTex example is now correctly formatted with last names following first names. An example of BibLaTex has been added. BibTex and BibLaTex examples now clearly indicate that what is cited is software.

    -- by [\@willynilly](https://github.com/sponsors/willynilly)

-   [#13420](https://github.com/pytest-dev/pytest/issues/13420): Improved test collection performance by optimizing path resolution used in [`FSCollector`].

-   [#13457](https://github.com/pytest-dev/pytest/issues/13457): The error message about duplicate parametrization no longer displays an internal stack trace.

-   [#4112](https://github.com/pytest-dev/pytest/issues/4112): Using [[pytest.mark.usefixtures]](reference/reference.html#pytest-mark-usefixtures-ref) on [[`pytest.param()`]](reference/reference.html#pytest.param "pytest.param") now produces an error instead of silently doing nothing.

-   [#5473](https://github.com/pytest-dev/pytest/issues/5473): Replace [`:`] with [`;`] in the assertion rewrite warning message so it can be filtered using standard Python warning filters before calling [[`pytest.main()`]](reference/reference.html#pytest.main "pytest.main").

-   

    [#6985](https://github.com/pytest-dev/pytest/issues/6985): Improved [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") to enhance the readability of value ranges and tolerances between 0.001 and 1000.

    :   -   The [`repr`] method now provides clearer output for values within those ranges, making it easier to interpret the results.

        -   Previously, the output for those ranges of values and tolerances was displayed in scientific notation (e.g., [`42`]` `[`±`]` `[`1.0e+00`]). The updated method now presents the tolerance as a decimal for better readability (e.g., [`42`]` `[`±`]` `[`1`]).

            Example:

            **Previous Output:**

            ::: 
            ::: highlight
                >>> pytest.approx(42, abs=1)
                42 ± 1.0e+00
            :::
            :::

            **Current Output:**

            ::: 
            ::: highlight
                >>> pytest.approx(42, abs=1)
                42 ± 1
            :::
            :::

        -- by [\@fazeelghafoor](https://github.com/sponsors/fazeelghafoor)

-   [#7683](https://github.com/pytest-dev/pytest/issues/7683): The formerly optional [`pygments`] dependency is now required, causing output always to be source-highlighted (unless disabled via the [`--code-highlight=no`] CLI option).

### Bug fixes[¶](#id121 "Link to this heading")

-   [#10404](https://github.com/pytest-dev/pytest/issues/10404): Apply filterwarnings from config/cli as soon as possible, and revert them as late as possible so that warnings as errors are collected throughout the pytest run and before the unraisable and threadexcept hooks are removed.

    This allows very late warnings and unraisable/threadexcept exceptions to fail the test suite.

    This also changes the warning that the lsof plugin issues from PytestWarning to the new warning PytestFDWarning so it can be more easily filtered.

-   [#11067](https://github.com/pytest-dev/pytest/issues/11067): The test report is now consistent regardless if the test xfailed via [[pytest.mark.xfail]](reference/reference.html#pytest-mark-xfail-ref) or [[`pytest.fail()`]](reference/reference.html#pytest.fail "pytest.fail").

    Previously, *xfailed* tests via the marker would have the string [`"reason:`]` `[`"`] prefixed to the message, while those *xfailed* via the function did not. The prefix has been removed.

-   [#12008](https://github.com/pytest-dev/pytest/issues/12008): In [#11220](https://github.com/pytest-dev/pytest/pull/11220), an unintended change in reordering was introduced by changing the way indices were assigned to direct params. More specifically, before that change, the indices of direct params to metafunc's callspecs were assigned after all parametrizations took place. Now, that change is reverted.

-   [#12863](https://github.com/pytest-dev/pytest/issues/12863): Fix applying markers, including [[pytest.mark.parametrize]](reference/reference.html#pytest-mark-parametrize-ref) when placed above [`@staticmethod`] or [`@classmethod`].

-   [#12929](https://github.com/pytest-dev/pytest/issues/12929): Handle StopIteration from test cases, setup and teardown correctly.

-   [#12938](https://github.com/pytest-dev/pytest/issues/12938): Fixed [`--durations-min`] argument not respected if [`-vv`] is used.

-   [#12946](https://github.com/pytest-dev/pytest/issues/12946): Fixed missing help for [[`pdb`]](https://docs.python.org/3/library/pdb.html#module-pdb "(in Python v3.14)") commands wrapped by pytest -- by [\@adamchainz](https://github.com/sponsors/adamchainz).

-   [#12981](https://github.com/pytest-dev/pytest/issues/12981): Prevent exceptions in [[`pytest.Config.add_cleanup()`]](reference/reference.html#pytest.Config.add_cleanup "pytest.Config.add_cleanup") callbacks preventing further cleanups.

-   [#13047](https://github.com/pytest-dev/pytest/issues/13047): Restore [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") handling of equality checks between [`bool`] and [`numpy.bool_`] types.

    Comparing [`bool`] and [`numpy.bool_`] using [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") accidentally changed in version [`8.3.4`] and [`8.3.5`] to no longer match:

    ::: 
    ::: highlight
        >>> import numpy as np
        >>> from pytest import approx
        >>> [np.True_, np.True_] == pytest.approx([True, True])
        False
    :::
    :::

    This has now been fixed:

    ::: 
    ::: highlight
        >>> [np.True_, np.True_] == pytest.approx([True, True])
        True
    :::
    :::

-   [#13119](https://github.com/pytest-dev/pytest/issues/13119): Improved handling of invalid regex patterns for filter warnings by providing a clear error message.

-   [#13175](https://github.com/pytest-dev/pytest/issues/13175): The diff is now also highlighted correctly when comparing two strings.

-   [#13248](https://github.com/pytest-dev/pytest/issues/13248): Fixed an issue where passing a [`scope`] in [[`Metafunc.parametrize`]](reference/reference.html#pytest.Metafunc.parametrize "pytest.Metafunc.parametrize") with [`indirect=True`] could result in other fixtures being unable to depend on the parametrized fixture.

-   [#13291](https://github.com/pytest-dev/pytest/issues/13291): Fixed [`repr`] of [`attrs`] objects in assertion failure messages when using [`attrs>=25.2`].

-   [#13312](https://github.com/pytest-dev/pytest/issues/13312): Fixed a possible [`KeyError`] crash on PyPy during collection of tests involving higher-scoped parameters.

-   [#13345](https://github.com/pytest-dev/pytest/issues/13345): Fix type hints for [[`pytest.TestReport.when`]](reference/reference.html#pytest.TestReport.when "pytest.TestReport.when") and [[`pytest.TestReport.location`]](reference/reference.html#pytest.TestReport.location "pytest.TestReport.location").

-   [#13377](https://github.com/pytest-dev/pytest/issues/13377): Fixed handling of test methods with positional-only parameter syntax.

    Now, methods are supported that formally define [`self`] as positional-only and/or fixture parameters as keyword-only, e.g.:

    ::: 
    ::: highlight
        class TestClass:

            def test_method(self, /, *, fixture): ...
    :::
    :::

    Before, this caused an internal error in pytest.

-   [#13384](https://github.com/pytest-dev/pytest/issues/13384): Fixed an issue where pytest could report negative durations.

-   [#13420](https://github.com/pytest-dev/pytest/issues/13420): Added [`lru_cache`] to [`nodes._check_initialpaths_for_relpath`].

-   [#9037](https://github.com/pytest-dev/pytest/issues/9037): Honor [[`disable_test_id_escaping_and_forfeit_all_rights_to_community_support`]](reference/reference.html#confval-disable_test_id_escaping_and_forfeit_all_rights_to_community_support) when escaping ids in parametrized tests.

### Improved documentation[¶](#id141 "Link to this heading")

-   [#12535](https://github.com/pytest-dev/pytest/issues/12535): [`This`]` `[`` example`<https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures> ``]` `[`showed`]` `[``` ``print` ```] statements that do not exactly reflect what the different branches actually do. The fix makes the example more precise.

-   [#13218](https://github.com/pytest-dev/pytest/issues/13218): Pointed out in the [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") documentation that it considers booleans unequal to numeric zero or one.

-   [#13221](https://github.com/pytest-dev/pytest/issues/13221): Improved grouping of CLI options in the [`--help`] output.

-   [#6649](https://github.com/pytest-dev/pytest/issues/6649): Added [[`TerminalReporter`]](reference/reference.html#pytest.TerminalReporter "pytest.TerminalReporter") to the [[API Reference]](reference/reference.html#api-reference) documentation page.

-   [#8612](https://github.com/pytest-dev/pytest/issues/8612): Add a recipe for handling abstract test classes in the documentation.

    A new example has been added to the documentation to demonstrate how to use a mixin class to handle abstract test classes without manually setting the [`__test__`] attribute for subclasses. This ensures that subclasses of abstract test classes are automatically collected by pytest.

### Packaging updates and notes for downstreams[¶](#id147 "Link to this heading")

-   [#13317](https://github.com/pytest-dev/pytest/issues/13317): Specified minimum allowed versions of [`colorama`], [`iniconfig`], and [`packaging`]; and bumped the minimum allowed version of [`exceptiongroup`] for [`python_version<'3.11'`] from a release candidate to a full release.

### Contributor-facing changes[¶](#id149 "Link to this heading")

-   [#12017](https://github.com/pytest-dev/pytest/issues/12017): Mixed internal improvements:

    -   Migrate formatting to f-strings in some tests.

    -   Use type-safe constructs in JUnitXML tests.

    -   Moved\`\` MockTiming\`\` into [`_pytest.timing`].

    -- by [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt)

-   [#12647](https://github.com/pytest-dev/pytest/issues/12647): Fixed running the test suite with the [`hypothesis`] pytest plugin.

### Miscellaneous internal changes[¶](#id152 "Link to this heading")

-   [#6649](https://github.com/pytest-dev/pytest/issues/6649): Added [[`TerminalReporter`]](reference/reference.html#pytest.TerminalReporter "pytest.TerminalReporter") to the public pytest API, as it is part of the signature of the [[`pytest_terminal_summary`]](reference/reference.html#std-hook-pytest_terminal_summary) hook.

## pytest 8.3.5 (2025-03-02)[¶](#pytest-8-3-5-2025-03-02 "Link to this heading")

### Bug fixes[¶](#id154 "Link to this heading")

-   [#11777](https://github.com/pytest-dev/pytest/issues/11777): Fixed issue where sequences were still being shortened even with [`-vv`] verbosity.

-   [#12888](https://github.com/pytest-dev/pytest/issues/12888): Fixed broken input when using Python 3.13+ and a [`libedit`] build of Python, such as on macOS or with uv-managed Python binaries from the [`python-build-standalone`] project. This could manifest e.g. by a broken prompt when using [`Pdb`], or seeing empty inputs with manual usage of [`input()`] and suspended capturing.

-   [#13026](https://github.com/pytest-dev/pytest/issues/13026): Fixed [[`AttributeError`]](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)") crash when using [`--import-mode=importlib`] when top-level directory same name as another module of the standard library.

-   [#13053](https://github.com/pytest-dev/pytest/issues/13053): Fixed a regression in pytest 8.3.4 where, when using [`--import-mode=importlib`], a directory containing py file with the same name would cause an [`ImportError`]

-   [#13083](https://github.com/pytest-dev/pytest/issues/13083): Fixed issue where pytest could crash if one of the collected directories got removed during collection.

### Improved documentation[¶](#id160 "Link to this heading")

-   [#12842](https://github.com/pytest-dev/pytest/issues/12842): Added dedicated page about using types with pytest.

    See [[Typing in pytest]](explanation/types.html#types) for detailed usage.

### Contributor-facing changes[¶](#id162 "Link to this heading")

-   [#13112](https://github.com/pytest-dev/pytest/issues/13112): Fixed selftest failures in [`test_terminal.py`] with Pygments \>= 2.19.0

-   [#13256](https://github.com/pytest-dev/pytest/issues/13256): Support for Towncrier versions released in 2024 has been re-enabled when building Sphinx docs -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

## pytest 8.3.4 (2024-12-01)[¶](#pytest-8-3-4-2024-12-01 "Link to this heading")

### Bug fixes[¶](#id165 "Link to this heading")

-   [#12592](https://github.com/pytest-dev/pytest/issues/12592): Fixed [[`KeyError`]](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") crash when using [`--import-mode=importlib`] in a directory layout where a directory contains a child directory with the same name.

-   [#12818](https://github.com/pytest-dev/pytest/issues/12818): Assertion rewriting now preserves the source ranges of the original instructions, making it play well with tools that deal with the [`AST`], like [executing](https://github.com/alexmojaki/executing).

-   [#12849](https://github.com/pytest-dev/pytest/issues/12849): ANSI escape codes for colored output now handled correctly in [[`pytest.fail()`]](reference/reference.html#pytest.fail "pytest.fail") with [`pytrace=False`].

-   [#9353](https://github.com/pytest-dev/pytest/issues/9353): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now uses strict equality when given booleans.

### Improved documentation[¶](#id170 "Link to this heading")

-   [#10558](https://github.com/pytest-dev/pytest/issues/10558): Fix ambiguous docstring of [[`pytest.Config.getoption()`]](reference/reference.html#pytest.Config.getoption "pytest.Config.getoption").

-   [#10829](https://github.com/pytest-dev/pytest/issues/10829): Improve documentation on the current handling of the [`--basetemp`] option and its lack of retention functionality ([[Temporary directory location and retention]](how-to/tmp_path.html#temporary-directory-location-and-retention)).

-   [#12866](https://github.com/pytest-dev/pytest/issues/12866): Improved cross-references concerning the [[`recwarn`]](reference/reference.html#std-fixture-recwarn) fixture.

-   [#12966](https://github.com/pytest-dev/pytest/issues/12966): Clarify [[\@pytest.mark.filterwarnings]](how-to/capture-warnings.html#filterwarnings) docs on filter precedence/order when using multiple [[\@pytest.mark.filterwarnings]](reference/reference.html#pytest-mark-filterwarnings-ref) marks.

### Contributor-facing changes[¶](#id175 "Link to this heading")

-   [#12497](https://github.com/pytest-dev/pytest/issues/12497): Fixed two failing pdb-related tests on Python 3.13.

## pytest 8.3.3 (2024-09-09)[¶](#pytest-8-3-3-2024-09-09 "Link to this heading")

### Bug fixes[¶](#id177 "Link to this heading")

-   [#12446](https://github.com/pytest-dev/pytest/issues/12446): Avoid calling [`@property`] (and other instance descriptors) during fixture discovery -- by [\@asottile](https://github.com/sponsors/asottile)

-   [#12659](https://github.com/pytest-dev/pytest/issues/12659): Fixed the issue of not displaying assertion failure differences when using the parameter [`--import-mode=importlib`] in pytest\>=8.1.

-   [#12667](https://github.com/pytest-dev/pytest/issues/12667): Fixed a regression where type change in [`ExceptionInfo.errisinstance`] caused [`mypy`] to fail.

-   [#12744](https://github.com/pytest-dev/pytest/issues/12744): Fixed typing compatibility with Python 3.9 or less -- replaced [`typing.Self`] with [`typing_extensions.Self`] -- by [\@Avasam](https://github.com/sponsors/Avasam)

-   [#12745](https://github.com/pytest-dev/pytest/issues/12745): Fixed an issue with backslashes being incorrectly converted in nodeid paths on Windows, ensuring consistent path handling across environments.

-   [#6682](https://github.com/pytest-dev/pytest/issues/6682): Fixed bug where the verbosity levels where not being respected when printing the "msg" part of failed assertion (as in [`assert`]` `[`condition,`]` `[`msg`]).

-   [#9422](https://github.com/pytest-dev/pytest/issues/9422): Fix bug where disabling the terminal plugin via [`-p`]` `[`no:terminal`] would cause crashes related to missing the [`verbose`] option.

    -- by [\@GTowers1](https://github.com/sponsors/GTowers1)

### Improved documentation[¶](#id185 "Link to this heading")

-   [#12663](https://github.com/pytest-dev/pytest/issues/12663): Clarify that the [`pytest_deselected`] hook should be called from [`pytest_collection_modifyitems`] hook implementations when items are deselected.

-   [#12678](https://github.com/pytest-dev/pytest/issues/12678): Remove erroneous quotes from [`tmp_path_retention_policy`] example in docs.

### Miscellaneous internal changes[¶](#id188 "Link to this heading")

-   [#12769](https://github.com/pytest-dev/pytest/issues/12769): Fix typos discovered by codespell and add codespell to pre-commit hooks.

## pytest 8.3.2 (2024-07-24)[¶](#pytest-8-3-2-2024-07-24 "Link to this heading")

### Bug fixes[¶](#id190 "Link to this heading")

-   [#12652](https://github.com/pytest-dev/pytest/issues/12652): Resolve regression [`conda`] environments where no longer being automatically detected.

    -- by [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt)

## pytest 8.3.1 (2024-07-20)[¶](#pytest-8-3-1-2024-07-20 "Link to this heading")

The 8.3.0 release failed to include the change notes and docs for the release. This patch release remedies this. There are no other changes.

## pytest 8.3.0 (2024-07-20)[¶](#pytest-8-3-0-2024-07-20 "Link to this heading")

### New features[¶](#id192 "Link to this heading")

-   [#12231](https://github.com/pytest-dev/pytest/issues/12231): Added [`--xfail-tb`] flag, which turns on traceback output for XFAIL results.

    -   If the [`--xfail-tb`] flag is not given, tracebacks for XFAIL results are NOT shown.

    -   The style of traceback for XFAIL is set with [`--tb`], and can be [`auto|long|short|line|native|no`].

    -   Note: Even if you have [`--xfail-tb`] set, you won't see them if [`--tb=no`].

    Some history:

    With pytest 8.0, [`-rx`] or [`-ra`] would not only turn on summary reports for xfail, but also report the tracebacks for xfail results. This caused issues with some projects that utilize xfail, but don't want to see all of the xfail tracebacks.

    This change detaches xfail tracebacks from [`-rx`], and now we turn on xfail tracebacks with [`--xfail-tb`]. With this, the default [`-rx`]/ [`-ra`] behavior is identical to pre-8.0 with respect to xfail tracebacks. While this is a behavior change, it brings default behavior back to pre-8.0.0 behavior, which ultimately was considered the better course of action.

    -- by [\@okken](https://github.com/sponsors/okken)

-   [#12281](https://github.com/pytest-dev/pytest/issues/12281): Added support for keyword matching in marker expressions.

    Now tests can be selected by marker keyword arguments. Supported values are [[`int`]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), (unescaped) [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [[`bool`]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") & [[`None`]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)").

    See [[marker examples]](example/markers.html#marker-keyword-expression-example) for more information.

    -- by [\@lovetheguitar](https://github.com/sponsors/lovetheguitar)

-   [#12567](https://github.com/pytest-dev/pytest/issues/12567): Added [`--no-fold-skipped`] command line option.

    If this option is set, then skipped tests in short summary are no longer grouped by reason but all tests are printed individually with their nodeid in the same way as other statuses.

    -- by [\@pbrezina](https://github.com/sponsors/pbrezina)

### Improvements in existing functionality[¶](#id196 "Link to this heading")

-   [#12469](https://github.com/pytest-dev/pytest/issues/12469): The console output now uses the "third-party plugins" terminology, replacing the previously established but confusing and outdated reference to [[setuptools]](https://setuptools.pypa.io/en/stable/index.html "(in setuptools v80.9.0.post20250527)") -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

-   [#12544](https://github.com/pytest-dev/pytest/issues/12544), [#12545](https://github.com/pytest-dev/pytest/issues/12545): Python virtual environment detection was improved by checking for a [`pyvenv.cfg`] file, ensuring reliable detection on various platforms -- by [\@zachsnickers](https://github.com/sponsors/zachsnickers).

-   [#2871](https://github.com/pytest-dev/pytest/issues/2871): Do not truncate arguments to functions in output when running with [`-vvv`].

-   [#389](https://github.com/pytest-dev/pytest/issues/389): The readability of assertion introspection of bound methods has been enhanced -- by [\@farbodahm](https://github.com/sponsors/farbodahm), [\@webknjaz](https://github.com/sponsors/webknjaz), [\@obestwalter](https://github.com/sponsors/obestwalter), [\@flub](https://github.com/sponsors/flub) and [\@glyphack](https://github.com/sponsors/glyphack).

    Earlier, it was like:

    ::: 
    ::: highlight
        =================================== FAILURES ===================================
        _____________________________________ test _____________________________________

            def test():
        >       assert Help().fun() == 2
        E       assert 1 == 2
        E        +  where 1 = <bound method Help.fun of <example.Help instance at 0x256a830>>()
        E        +    where <bound method Help.fun of <example.Help instance at 0x256a830>> = <example.Help instance at 0x256a830>.fun
        E        +      where <example.Help instance at 0x256a830> = Help()

        example.py:7: AssertionError
        =========================== 1 failed in 0.03 seconds ===========================
    :::
    :::

    And now it's like:

    ::: 
    ::: highlight
        =================================== FAILURES ===================================
        _____________________________________ test _____________________________________

            def test():
        >       assert Help().fun() == 2
        E       assert 1 == 2
        E        +  where 1 = fun()
        E        +    where fun = <test_local.Help object at 0x1074be230>.fun
        E        +      where <test_local.Help object at 0x1074be230> = Help()

        test_local.py:13: AssertionError
        =========================== 1 failed in 0.03 seconds ===========================
    :::
    :::

-   [#7662](https://github.com/pytest-dev/pytest/issues/7662): Added timezone information to the testsuite timestamp in the JUnit XML report.

### Bug fixes[¶](#id203 "Link to this heading")

-   [#11706](https://github.com/pytest-dev/pytest/issues/11706): Fixed reporting of teardown errors in higher-scoped fixtures when using [`--maxfail`] or [`--stepwise`].

    Originally added in pytest 8.0.0, but reverted in 8.0.2 due to a regression in pytest-xdist. This regression was fixed in pytest-xdist 3.6.1.

-   [#11797](https://github.com/pytest-dev/pytest/issues/11797): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now correctly handles [[`Sequence`]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")-like objects.

-   [#12204](https://github.com/pytest-dev/pytest/issues/12204), [#12264](https://github.com/pytest-dev/pytest/issues/12264): Fixed a regression in pytest 8.0 where tracebacks get longer and longer when multiple tests fail due to a shared higher-scope fixture which raised -- by [\@bluetech](https://github.com/sponsors/bluetech).

    Also fixed a similar regression in pytest 5.4 for collectors which raise during setup.

    The fix necessitated internal changes which may affect some plugins:

    -   [`FixtureDef.cached_result[2]`] is now a tuple [`(exc,`]` `[`tb)`] instead of [`exc`].

    -   [`SetupState.stack`] failures are now a tuple [`(exc,`]` `[`tb)`] instead of [`exc`].

-   [#12275](https://github.com/pytest-dev/pytest/issues/12275): Fixed collection error upon encountering an [[`abstract`]](https://docs.python.org/3/library/abc.html#module-abc "(in Python v3.14)") class, including abstract [`unittest.TestCase`] subclasses.

-   [#12328](https://github.com/pytest-dev/pytest/issues/12328): Fixed a regression in pytest 8.0.0 where package-scoped parameterized items were not correctly reordered to minimize setups/teardowns in some cases.

-   [#12424](https://github.com/pytest-dev/pytest/issues/12424): Fixed crash with [`assert`]` `[`testcase`]` `[`is`]` `[`not`]` `[`None`] assertion failure when re-running unittest tests using plugins like pytest-rerunfailures. Regressed in 8.2.2.

-   [#12472](https://github.com/pytest-dev/pytest/issues/12472): Fixed a crash when returning category [`"error"`] or [`"failed"`] with a custom test status from [[`pytest_report_teststatus`]](reference/reference.html#std-hook-pytest_report_teststatus) hook -- [\@pbrezina](https://github.com/sponsors/pbrezina).

-   [#12505](https://github.com/pytest-dev/pytest/issues/12505): Improved handling of invalid regex patterns in [[`pytest.raises(match=r'...')`]](reference/reference.html#pytest.raises "pytest.raises") by providing a clear error message.

-   [#12580](https://github.com/pytest-dev/pytest/issues/12580): Fixed a crash when using the cache class on Windows and the cache directory was created concurrently.

-   [#6962](https://github.com/pytest-dev/pytest/issues/6962): Parametrization parameters are now compared using [`==`] instead of [`is`] ([`is`] is still used as a fallback if the parameter does not support [`==`]). This fixes use of parameters such as lists, which have a different [`id`] but compare equal, causing fixtures to be re-computed instead of being cached.

-   [#7166](https://github.com/pytest-dev/pytest/issues/7166): Fixed progress percentages (the [`[`]` `[`87%]`] at the edge of the screen) sometimes not aligning correctly when running with pytest-xdist [`-n`].

### Improved documentation[¶](#id216 "Link to this heading")

-   [#12153](https://github.com/pytest-dev/pytest/issues/12153): Documented using [][[`PYTEST_VERSION`]](reference/reference.html#envvar-PYTEST_VERSION) to detect if code is running from within a pytest run.

-   [#12469](https://github.com/pytest-dev/pytest/issues/12469): The external plugin mentions in the documentation now avoid mentioning [[setuptools entry-points]](https://setuptools.pypa.io/en/stable/index.html "(in setuptools v80.9.0.post20250527)") as the concept is much more generic nowadays. Instead, the terminology of "external", "installed", or "third-party" plugins (or packages) replaces that.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12577](https://github.com/pytest-dev/pytest/issues/12577): [`CI`] and [`BUILD_NUMBER`] environment variables role is described in the reference doc. They now also appear when doing [`pytest`]` `[`-h`] -- by [\@MarcBresson](https://github.com/sponsors/MarcBresson).

### Contributor-facing changes[¶](#id220 "Link to this heading")

-   [#12467](https://github.com/pytest-dev/pytest/issues/12467): Migrated all internal type-annotations to the python3.10+ style by using the [`annotations`] future import.

    -- by [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt)

-   [#11771](https://github.com/pytest-dev/pytest/issues/11771), [#12557](https://github.com/pytest-dev/pytest/issues/12557): The PyPy runtime version has been updated to 3.9 from 3.8 that introduced a flaky bug at the garbage collector which was not expected to fix there as the 3.8 is EoL.

    -- by [\@x612skm](https://github.com/sponsors/x612skm)

-   [#12493](https://github.com/pytest-dev/pytest/issues/12493): The change log draft preview integration has been refactored to use a third party extension [`sphinxcontib-towncrier`]. The previous in-repo script was putting the change log preview file at [`doc/en/_changelog_towncrier_draft.rst`]. Said file is no longer ignored in Git and might show up among untracked files in the development environments of the contributors. To address that, the contributors can run the following command that will clean it up:

    ::: 
    ::: highlight
        $ git clean -x -i -- doc/en/_changelog_towncrier_draft.rst
    :::
    :::

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12498](https://github.com/pytest-dev/pytest/issues/12498): All the undocumented [`tox`] environments now have descriptions. They can be listed in one's development environment by invoking [`tox`]` `[`-av`] in a terminal.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12501](https://github.com/pytest-dev/pytest/issues/12501): The changelog configuration has been updated to introduce more accurate audience-tailored categories. Previously, there was a [`trivial`] change log fragment type with an unclear and broad meaning. It was removed and we now have [`contrib`], [`misc`] and [`packaging`] in place of it.

    The new change note types target the readers who are downstream packagers and project contributors. Additionally, the miscellaneous section is kept for unspecified updates that do not fit anywhere else.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12502](https://github.com/pytest-dev/pytest/issues/12502): The UX of the GitHub automation making pull requests to update the plugin list has been updated. Previously, the maintainers had to close the automatically created pull requests and re-open them to trigger the CI runs. From now on, they only need to click the [`Ready`]` `[`for`]` `[`review`] button instead.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12522](https://github.com/pytest-dev/pytest/issues/12522): The [`:pull:`] RST role has been replaced with a shorter [`:pr:`] due to starting to use the implementation from the third-party [sphinx-issues](https://pypi.org/project/sphinx-issues) Sphinx extension -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

-   [#12531](https://github.com/pytest-dev/pytest/issues/12531): The coverage reporting configuration has been updated to exclude pytest's own tests marked as expected to fail from the coverage report. This has an effect of reducing the influence of flaky tests on the resulting number.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12533](https://github.com/pytest-dev/pytest/issues/12533): The [`extlinks`] Sphinx extension is no longer enabled. The [`:bpo:`] role it used to declare has been removed with that. BPO itself has migrated to GitHub some years ago and it is possible to link the respective issues by using their GitHub issue numbers and the [`:issue:`] role that the [`sphinx-issues`] extension implements.

    -- by [\@webknjaz](https://github.com/sponsors/webknjaz)

-   [#12562](https://github.com/pytest-dev/pytest/issues/12562): Possible typos in using the [`:user:`] RST role is now being linted through the pre-commit tool integration -- by [\@webknjaz](https://github.com/sponsors/webknjaz).

## pytest 8.2.2 (2024-06-04)[¶](#pytest-8-2-2-2024-06-04 "Link to this heading")

### Bug Fixes[¶](#id232 "Link to this heading")

-   [#12355](https://github.com/pytest-dev/pytest/issues/12355): Fix possible catastrophic performance slowdown on a certain parametrization pattern involving many higher-scoped parameters.

-   [#12367](https://github.com/pytest-dev/pytest/issues/12367): Fix a regression in pytest 8.2.0 where unittest class instances (a fresh one is created for each test) were not released promptly on test teardown but only on session teardown.

-   [#12381](https://github.com/pytest-dev/pytest/issues/12381): Fix possible "Directory not empty" crashes arising from concurrent cache dir ([`.pytest_cache`]) creation. Regressed in pytest 8.2.0.

### Improved Documentation[¶](#id236 "Link to this heading")

-   [#12290](https://github.com/pytest-dev/pytest/issues/12290): Updated Sphinx theme to use Furo instead of Flask, enabling Dark mode theme.

-   [#12356](https://github.com/pytest-dev/pytest/issues/12356): Added a subsection to the documentation for debugging flaky tests to mention lack of thread safety in pytest as a possible source of flakiness.

-   [#12363](https://github.com/pytest-dev/pytest/issues/12363): The documentation webpages now links to a canonical version to reduce outdated documentation in search engine results.

## pytest 8.2.1 (2024-05-19)[¶](#pytest-8-2-1-2024-05-19 "Link to this heading")

### Improvements[¶](#improvements "Link to this heading")

-   [#12334](https://github.com/pytest-dev/pytest/issues/12334): Support for Python 3.13 (beta1 at the time of writing).

### Bug Fixes[¶](#id241 "Link to this heading")

-   [#12120](https://github.com/pytest-dev/pytest/issues/12120): Fix [`PermissionError`] crashes arising from directories which are not selected on the command-line.

-   [#12191](https://github.com/pytest-dev/pytest/issues/12191): Keyboard interrupts and system exits are now properly handled during the test collection.

-   [#12300](https://github.com/pytest-dev/pytest/issues/12300): Fixed handling of 'Function not implemented' error under squashfuse_ll, which is a different way to say that the mountpoint is read-only.

-   [#12308](https://github.com/pytest-dev/pytest/issues/12308): Fix a regression in pytest 8.2.0 where the permissions of automatically-created [`.pytest_cache`] directories became [`rwx------`] instead of the expected [`rwxr-xr-x`].

### Trivial/Internal Changes[¶](#trivial-internal-changes "Link to this heading")

-   [#12333](https://github.com/pytest-dev/pytest/issues/12333): pytest releases are now attested using the recent [Artifact Attestation](https://github.blog/2024-05-02-introducing-artifact-attestations-now-in-public-beta/) support from GitHub, allowing users to verify the provenance of pytest's sdist and wheel artifacts.

## pytest 8.2.0 (2024-04-27)[¶](#pytest-8-2-0-2024-04-27 "Link to this heading")

### Breaking Changes[¶](#breaking-changes "Link to this heading")

-   [#12089](https://github.com/pytest-dev/pytest/pull/12089): pytest now requires that [[`unittest.TestCase`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.14)") subclasses can be instantiated freely using [`MyTestCase('runTest')`].

    If the class doesn't allow this, you may see an error during collection such as [`AttributeError:`]` `[`'MyTestCase'`]` `[`object`]` `[`has`]` `[`no`]` `[`attribute`]` `[`'runTest'`].

    Classes which do not override [`__init__`], or do not access the test method in [`__init__`] using [`getattr`] or similar, are unaffected.

    Classes which do should take care to not crash when [`"runTest"`] is given, as is shown in [unittest.TestCases's implementation](https://github.com/python/cpython/blob/51aefc5bf907ddffaaf083ded0de773adcdf08c8/Lib/unittest/case.py#L419-L426). Alternatively, consider using [[`setUp`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "(in Python v3.14)") instead of [`__init__`].

    If you run into this issue using [`tornado.AsyncTestCase`], please see [issue 12263](https://github.com/pytest-dev/pytest/issues/12263).

    If you run into this issue using an abstract [`TestCase`] subclass, please see [issue 12275](https://github.com/pytest-dev/pytest/issues/12275).

    Historical note: the effect of this change on custom TestCase implementations was not properly considered initially, this is why it was done in a minor release. We apologize for the inconvenience.

### Deprecations[¶](#deprecations "Link to this heading")

-   [#12069](https://github.com/pytest-dev/pytest/issues/12069): A deprecation warning is now raised when implementations of one of the following hooks request a deprecated [`py.path.local`] parameter instead of the [`pathlib.Path`] parameter which replaced it:

    -   [[`pytest_ignore_collect`]](reference/reference.html#std-hook-pytest_ignore_collect) - the [`path`] parameter - use [`collection_path`] instead.

    -   [[`pytest_collect_file`]](reference/reference.html#std-hook-pytest_collect_file) - the [`path`] parameter - use [`file_path`] instead.

    -   [[`pytest_pycollect_makemodule`]](reference/reference.html#std-hook-pytest_pycollect_makemodule) - the [`path`] parameter - use [`module_path`] instead.

    -   [[`pytest_report_header`]](reference/reference.html#std-hook-pytest_report_header) - the [`startdir`] parameter - use [`start_path`] instead.

    -   [[`pytest_report_collectionfinish`]](reference/reference.html#std-hook-pytest_report_collectionfinish) - the [`startdir`] parameter - use [`start_path`] instead.

    The replacement parameters are available since pytest 7.0.0. The old parameters will be removed in pytest 9.0.0.

    See [[py.path.local arguments for hooks replaced with pathlib.Path]](deprecations.html#legacy-path-hooks-deprecated) for more details.

### Features[¶](#features "Link to this heading")

-   [#11871](https://github.com/pytest-dev/pytest/issues/11871): Added support for reading command line arguments from a file using the prefix character [`@`], like e.g.: [`pytest`]` `[`@tests.txt`]. The file must have one argument per line.

    See [[Read arguments from file]](how-to/usage.html#args-from-file) for details.

### Improvements[¶](#id250 "Link to this heading")

-   [#11523](https://github.com/pytest-dev/pytest/issues/11523): [[`pytest.importorskip()`]](reference/reference.html#pytest.importorskip "pytest.importorskip") will now issue a warning if the module could be found, but raised [[`ImportError`]](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)") instead of [[`ModuleNotFoundError`]](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "(in Python v3.14)").

    The warning can be suppressed by passing [`exc_type=ImportError`] to [[`pytest.importorskip()`]](reference/reference.html#pytest.importorskip "pytest.importorskip").

    See [[pytest.importorskip default behavior regarding ImportError]](deprecations.html#import-or-skip-import-error) for details.

-   [#11728](https://github.com/pytest-dev/pytest/issues/11728): For [`unittest`]-based tests, exceptions during class cleanup (as raised by functions registered with [[`TestCase.addClassCleanup`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "(in Python v3.14)")) are now reported instead of silently failing.

-   [#11777](https://github.com/pytest-dev/pytest/issues/11777): Text is no longer truncated in the [`short`]` `[`test`]` `[`summary`]` `[`info`] section when [`-vv`] is given.

-   [#12112](https://github.com/pytest-dev/pytest/issues/12112): Improved namespace packages detection when [[`consider_namespace_packages`]](reference/reference.html#confval-consider_namespace_packages) is enabled, covering more situations (like editable installs).

-   [#9502](https://github.com/pytest-dev/pytest/issues/9502): Added [][[`PYTEST_VERSION`]](reference/reference.html#envvar-PYTEST_VERSION) environment variable which is defined at the start of the pytest session and undefined afterwards. It contains the value of [`pytest.__version__`], and among other things can be used to easily check if code is running from within a pytest run.

### Bug Fixes[¶](#id256 "Link to this heading")

-   [#12065](https://github.com/pytest-dev/pytest/issues/12065): Fixed a regression in pytest 8.0.0 where test classes containing [`setup_method`] and tests using [`@staticmethod`] or [`@classmethod`] would crash with [`AttributeError:`]` `[`'NoneType'`]` `[`object`]` `[`has`]` `[`no`]` `[`attribute`]` `[`'setup_method'`].

    Now the [[`request.instance`]](reference/reference.html#pytest.FixtureRequest.instance "pytest.FixtureRequest.instance") attribute of tests using [`@staticmethod`] and [`@classmethod`] is no longer [`None`], but a fresh instance of the class, like in non-static methods. Previously it was [`None`], and all fixtures of such tests would share a single [`self`].

-   [#12135](https://github.com/pytest-dev/pytest/issues/12135): Fixed issue where fixtures adding their finalizer multiple times to fixtures they request would cause unreliable and non-intuitive teardown ordering in some instances.

-   [#12194](https://github.com/pytest-dev/pytest/issues/12194): Fixed a bug with [`--importmode=importlib`] and [`--doctest-modules`] where child modules did not appear as attributes in parent modules.

-   [#1489](https://github.com/pytest-dev/pytest/issues/1489): Fixed some instances where teardown of higher-scoped fixtures was not happening in the reverse order they were initialized in.

### Trivial/Internal Changes[¶](#id261 "Link to this heading")

-   [#12069](https://github.com/pytest-dev/pytest/issues/12069): [`pluggy>=1.5.0`] is now required.

-   [#12167](https://github.com/pytest-dev/pytest/issues/12167): [[cache]](how-to/cache.html#cache): create supporting files ([`CACHEDIR.TAG`], [`.gitignore`], etc.) in a temporary directory to provide atomic semantics.

## pytest 8.1.2 (2024-04-26)[¶](#pytest-8-1-2-2024-04-26 "Link to this heading")

### Bug Fixes[¶](#id264 "Link to this heading")

-   [#12114](https://github.com/pytest-dev/pytest/issues/12114): Fixed error in [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") when used with [`numpy`] arrays and comparing with other types.

## pytest 8.1.1 (2024-03-08)[¶](#pytest-8-1-1-2024-03-08 "Link to this heading")

Note

This release is not a usual bug fix release -- it contains features and improvements, being a follow up to [`8.1.0`], which has been yanked from PyPI.

### Features[¶](#id266 "Link to this heading")

-   [#11475](https://github.com/pytest-dev/pytest/issues/11475): Added the new [[`consider_namespace_packages`]](reference/reference.html#confval-consider_namespace_packages) configuration option, defaulting to [`False`].

    If set to [`True`], pytest will attempt to identify modules that are part of [namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages) when importing modules.

-   [#11653](https://github.com/pytest-dev/pytest/issues/11653): Added the new [[`verbosity_test_cases`]](reference/reference.html#confval-verbosity_test_cases) configuration option for fine-grained control of test execution verbosity. See [[Fine-grained verbosity]](how-to/output.html#pytest-fine-grained-verbosity) for more details.

### Improvements[¶](#id269 "Link to this heading")

-   [#10865](https://github.com/pytest-dev/pytest/issues/10865): [[`pytest.warns()`]](reference/reference.html#pytest.warns "pytest.warns") now validates that [[`warnings.warn()`]](https://docs.python.org/3/library/warnings.html#warnings.warn "(in Python v3.14)") was called with a [`str`] or a [`Warning`]. Currently in Python it is possible to use other types, however this causes an exception when [[`warnings.filterwarnings()`]](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "(in Python v3.14)") is used to filter those warnings (see [CPython #103577](https://github.com/python/cpython/issues/103577) for a discussion). While this can be considered a bug in CPython, we decided to put guards in pytest as the error message produced without this check in place is confusing.

-   [#11311](https://github.com/pytest-dev/pytest/issues/11311): When using [`--override-ini`] for paths in invocations without a configuration file defined, the current working directory is used as the relative directory.

    Previously this would raise an [[`AssertionError`]](https://docs.python.org/3/library/exceptions.html#AssertionError "(in Python v3.14)").

-   [#11475](https://github.com/pytest-dev/pytest/issues/11475): [[--import-mode=importlib]](explanation/pythonpath.html#import-mode-importlib) now tries to import modules using the standard import mechanism (but still without changing [[`sys.path`]](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.14)")), falling back to importing modules directly only if that fails.

    This means that installed packages will be imported under their canonical name if possible first, for example [`app.core.models`], instead of having the module name always be derived from their path (for example [`.env310.lib.site_packages.app.core.models`]).

-   [#11801](https://github.com/pytest-dev/pytest/issues/11801): Added the [[`iter_parents()`]](reference/reference.html#pytest.nodes.Node.iter_parents "_pytest.nodes.Node.iter_parents") helper method on nodes. It is similar to [[`listchain`]](reference/reference.html#pytest.nodes.Node.listchain "_pytest.nodes.Node.listchain"), but goes from bottom to top, and returns an iterator, not a list.

-   [#11850](https://github.com/pytest-dev/pytest/issues/11850): Added support for [[`sys.last_exc`]](https://docs.python.org/3/library/sys.html#sys.last_exc "(in Python v3.14)") for post-mortem debugging on Python\>=3.12.

-   [#11962](https://github.com/pytest-dev/pytest/issues/11962): In case no other suitable candidates for configuration file are found, a [`pyproject.toml`] (even without a [`[tool.pytest.ini_options]`] table) will be considered as the configuration file and define the [`rootdir`].

-   [#11978](https://github.com/pytest-dev/pytest/issues/11978): Add [`--log-file-mode`] option to the logging plugin, enabling appending to log-files. This option accepts either [`"w"`] or [`"a"`] and defaults to [`"w"`].

    Previously, the mode was hard-coded to be [`"w"`] which truncates the file before logging.

-   [#12047](https://github.com/pytest-dev/pytest/issues/12047): When multiple finalizers of a fixture raise an exception, now all exceptions are reported as an exception group. Previously, only the first exception was reported.

### Bug Fixes[¶](#id278 "Link to this heading")

-   [#11475](https://github.com/pytest-dev/pytest/issues/11475): Fixed regression where [`--importmode=importlib`] would import non-test modules more than once.

-   [#11904](https://github.com/pytest-dev/pytest/issues/11904): Fixed a regression in pytest 8.0.0 that would cause test collection to fail due to permission errors when using [`--pyargs`].

    This change improves the collection tree for tests specified using [`--pyargs`], see [#12043](https://github.com/pytest-dev/pytest/pull/12043) for a comparison with pytest 8.0 and \<8.

-   [#12011](https://github.com/pytest-dev/pytest/issues/12011): Fixed a regression in 8.0.1 whereby [`setup_module`] xunit-style fixtures are not executed when [`--doctest-modules`] is passed.

-   [#12014](https://github.com/pytest-dev/pytest/issues/12014): Fix the [`stacklevel`] used when warning about marks used on fixtures.

-   [#12039](https://github.com/pytest-dev/pytest/issues/12039): Fixed a regression in [`8.0.2`] where tests created using [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) have been collected multiple times in CI under Windows.

### Improved Documentation[¶](#id284 "Link to this heading")

-   [#11790](https://github.com/pytest-dev/pytest/issues/11790): Documented the retention of temporary directories created using the [`tmp_path`] fixture in more detail.

### Trivial/Internal Changes[¶](#id286 "Link to this heading")

-   [#11785](https://github.com/pytest-dev/pytest/issues/11785): Some changes were made to private functions which may affect plugins which access them:

    -   [`FixtureManager._getautousenames()`] now takes a [`Node`] itself instead of the nodeid.

    -   [`FixtureManager.getfixturedefs()`] now takes the [`Node`] itself instead of the nodeid.

    -   The [`_pytest.nodes.iterparentnodeids()`] function is removed without replacement. Prefer to traverse the node hierarchy itself instead. If you really need to, copy the function from the previous pytest release.

-   [#12069](https://github.com/pytest-dev/pytest/issues/12069): Delayed the deprecation of the following features to [`9.0.0`]:

    -   [[fspath argument for Node constructors replaced with pathlib.Path]](deprecations.html#node-ctor-fspath-deprecation).

    -   [[py.path.local arguments for hooks replaced with pathlib.Path]](deprecations.html#legacy-path-hooks-deprecated).

    It was discovered after [`8.1.0`] was released that the warnings about the impeding removal were not being displayed, so the team decided to revert the removal.

    This is the reason for [`8.1.0`] being yanked.

## pytest 8.1.0 (YANKED)[¶](#pytest-8-1-0-yanked "Link to this heading")

Note

This release has been **yanked**: it broke some plugins without the proper warning period, due to some warnings not showing up as expected.

See [#12069](https://github.com/pytest-dev/pytest/issues/12069).

## pytest 8.0.2 (2024-02-24)[¶](#pytest-8-0-2-2024-02-24 "Link to this heading")

### Bug Fixes[¶](#id289 "Link to this heading")

-   [#11895](https://github.com/pytest-dev/pytest/issues/11895): Fix collection on Windows where initial paths contain the short version of a path (for example [`c:\PROGRA~1\tests`]).

-   [#11953](https://github.com/pytest-dev/pytest/issues/11953): Fix an [`IndexError`] crash raising from [`getstatementrange_ast`].

-   [#12021](https://github.com/pytest-dev/pytest/issues/12021): Reverted a fix to [`--maxfail`] handling in pytest 8.0.0 because it caused a regression in pytest-xdist whereby session fixture teardowns may get executed multiple times when the max-fails is reached.

## pytest 8.0.1 (2024-02-16)[¶](#pytest-8-0-1-2024-02-16 "Link to this heading")

### Bug Fixes[¶](#id293 "Link to this heading")

-   [#11875](https://github.com/pytest-dev/pytest/issues/11875): Correctly handle errors from [[`getpass.getuser()`]](https://docs.python.org/3/library/getpass.html#getpass.getuser "(in Python v3.14)") in Python 3.13.

-   [#11879](https://github.com/pytest-dev/pytest/issues/11879): Fix an edge case where [`ExceptionInfo._stringify_exception`] could crash [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises").

-   [#11906](https://github.com/pytest-dev/pytest/issues/11906): Fix regression with [[`pytest.warns()`]](reference/reference.html#pytest.warns "pytest.warns") using custom warning subclasses which have more than one parameter in their [`__init__`].

-   [#11907](https://github.com/pytest-dev/pytest/issues/11907): Fix a regression in pytest 8.0.0 whereby calling [[`pytest.skip()`]](reference/reference.html#pytest.skip "pytest.skip") and similar control-flow exceptions within a [[`pytest.warns()`]](reference/reference.html#pytest.warns "pytest.warns") block would get suppressed instead of propagating.

-   [#11929](https://github.com/pytest-dev/pytest/issues/11929): Fix a regression in pytest 8.0.0 whereby autouse fixtures defined in a module get ignored by the doctests in the module.

-   [#11937](https://github.com/pytest-dev/pytest/issues/11937): Fix a regression in pytest 8.0.0 whereby items would be collected in reverse order in some circumstances.

## pytest 8.0.0 (2024-01-27)[¶](#pytest-8-0-0-2024-01-27 "Link to this heading")

### Bug Fixes[¶](#id300 "Link to this heading")

-   [#11842](https://github.com/pytest-dev/pytest/issues/11842): Properly escape the [`reason`] of a [[skip]](reference/reference.html#pytest-mark-skip-ref) mark when writing JUnit XML files.

-   [#11861](https://github.com/pytest-dev/pytest/issues/11861): Avoid microsecond exceeds [`1_000_000`] when using [`log-date-format`] with [`%f`] specifier, which might cause the test suite to crash.

## pytest 8.0.0rc2 (2024-01-17)[¶](#pytest-8-0-0rc2-2024-01-17 "Link to this heading")

### Improvements[¶](#id303 "Link to this heading")

-   [#11233](https://github.com/pytest-dev/pytest/issues/11233): Improvements to [`-r`] for xfailures and xpasses:

    -   Report tracebacks for xfailures when [`-rx`] is set.

    -   Report captured output for xpasses when [`-rX`] is set.

    -   For xpasses, add [`-`] in summary between test name and reason, to match how xfail is displayed.

-   [#11825](https://github.com/pytest-dev/pytest/issues/11825): The [[`pytest_plugin_registered`]](reference/reference.html#std-hook-pytest_plugin_registered) hook has a new [`plugin_name`] parameter containing the name by which [`plugin`] is registered.

### Bug Fixes[¶](#id306 "Link to this heading")

-   [#11706](https://github.com/pytest-dev/pytest/issues/11706): Fix reporting of teardown errors in higher-scoped fixtures when using [`--maxfail`] or [`--stepwise`].

    NOTE: This change was reverted in pytest 8.0.2 to fix a [regression](https://github.com/pytest-dev/pytest-xdist/issues/1024) it caused in pytest-xdist.

-   [#11758](https://github.com/pytest-dev/pytest/issues/11758): Fixed [`IndexError:`]` `[`string`]` `[`index`]` `[`out`]` `[`of`]` `[`range`] crash in [`if`]` `[`highlighted[-1]`]` `[`==`]` `[`"\n"`]` `[`and`]` `[`source[-1]`]` `[`!=`]` `[`"\n"`]. This bug was introduced in pytest 8.0.0rc1.

-   [#9765](https://github.com/pytest-dev/pytest/issues/9765), [#11816](https://github.com/pytest-dev/pytest/issues/11816): Fixed a frustrating bug that afflicted some users with the only error being [`assert`]` `[`mod`]` `[`not`]` `[`in`]` `[`mods`]. The issue was caused by the fact that [`str(Path(mod))`] and [`mod.__file__`] don't necessarily produce the same string, and was being erroneously used interchangeably in some places in the code.

    This fix also broke the internal API of [`PytestPluginManager.consider_conftest`] by introducing a new parameter -- we mention this in case it is being used by external code, even if marked as *private*.

## pytest 8.0.0rc1 (2023-12-30)[¶](#pytest-8-0-0rc1-2023-12-30 "Link to this heading")

### Breaking Changes[¶](#id311 "Link to this heading")

#### Old Deprecations Are Now Errors[¶](#old-deprecations-are-now-errors "Link to this heading")

-   [#7363](https://github.com/pytest-dev/pytest/issues/7363): **PytestRemovedIn8Warning deprecation warnings are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`PytestRemovedIn8Warning`] now generate errors instead of warning messages by default.

    **The affected features will be effectively removed in pytest 8.1**, so please consult the [[Deprecations and Removals]](deprecations.html#deprecations) section in the docs for directions on how to update existing code.

    In the pytest [`8.0.X`] series, it is possible to change the errors back into warnings as a stopgap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.PytestRemovedIn8Warning
    :::
    :::

    But this will stop working when pytest [`8.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#7363](https://github.com/pytest-dev/pytest/issues/7363).

#### Version Compatibility[¶](#version-compatibility "Link to this heading")

-   [#11151](https://github.com/pytest-dev/pytest/issues/11151): Dropped support for Python 3.7, which [reached end-of-life on 2023-06-27](https://devguide.python.org/versions/).

-   [`pluggy>=1.3.0`] is now required.

#### Collection Changes[¶](#collection-changes "Link to this heading")

In this version we've made several breaking changes to pytest's collection phase, particularly around how filesystem directories and Python packages are collected, fixing deficiencies and allowing for cleanups and improvements to pytest's internals. A deprecation period for these changes was not possible.

-   [#7777](https://github.com/pytest-dev/pytest/issues/7777): Files and directories are now collected in alphabetical order jointly, unless changed by a plugin. Previously, files were collected before directories. See below for an example.

-   [#8976](https://github.com/pytest-dev/pytest/issues/8976): Running [`pytest`]` `[`pkg/__init__.py`] now collects the [`pkg/__init__.py`] file (module) only. Previously, it collected the entire [`pkg`] package, including other test files in the directory, but excluding tests in the [`__init__.py`] file itself (unless [[`python_files`]](reference/reference.html#confval-python_files) was changed to allow [`__init__.py`] file).

    To collect the entire package, specify just the directory: [`pytest`]` `[`pkg`].

-   [#11137](https://github.com/pytest-dev/pytest/issues/11137): [[`pytest.Package`]](reference/reference.html#pytest.Package "pytest.Package") is no longer a [[`pytest.Module`]](reference/reference.html#pytest.Module "pytest.Module") or [[`pytest.File`]](reference/reference.html#pytest.File "pytest.File").

    The [`Package`] collector node designates a Python package, that is, a directory with an [`__init__.py`] file. Previously [`Package`] was a subtype of [`pytest.Module`] (which represents a single Python module), the module being the [`__init__.py`] file. This has been deemed a design mistake (see [#11137](https://github.com/pytest-dev/pytest/issues/11137) and [#7777](https://github.com/pytest-dev/pytest/issues/7777) for details).

    The [`path`] property of [`Package`] nodes now points to the package directory instead of the [`__init__.py`] file.

    Note that a [`Module`] node for [`__init__.py`] (which is not a [`Package`]) may still exist, if it is picked up during collection (e.g. if you configured [[`python_files`]](reference/reference.html#confval-python_files) to include [`__init__.py`] files).

-   [#7777](https://github.com/pytest-dev/pytest/issues/7777): Added a new [[`pytest.Directory`]](reference/reference.html#pytest.Directory "pytest.Directory") base collection node, which all collector nodes for filesystem directories are expected to subclass. This is analogous to the existing [[`pytest.File`]](reference/reference.html#pytest.File "pytest.File") for file nodes.

    Changed [[`pytest.Package`]](reference/reference.html#pytest.Package "pytest.Package") to be a subclass of [[`pytest.Directory`]](reference/reference.html#pytest.Directory "pytest.Directory"). A [`Package`] represents a filesystem directory which is a Python package, i.e. contains an [`__init__.py`] file.

    [[`pytest.Package`]](reference/reference.html#pytest.Package "pytest.Package") now only collects files in its own directory; previously it collected recursively. Sub-directories are collected as their own collector nodes, which then collect themselves, thus creating a collection tree which mirrors the filesystem hierarchy.

    Added a new [[`pytest.Dir`]](reference/reference.html#pytest.Dir "pytest.Dir") concrete collection node, a subclass of [[`pytest.Directory`]](reference/reference.html#pytest.Directory "pytest.Directory"). This node represents a filesystem directory, which is not a [[`pytest.Package`]](reference/reference.html#pytest.Package "pytest.Package"), that is, does not contain an [`__init__.py`] file. Similarly to [`Package`], it only collects the files in its own directory.

    [[`pytest.Session`]](reference/reference.html#pytest.Session "pytest.Session") now only collects the initial arguments, without recursing into directories. This work is now done by the [[`recursive`]` `[`expansion`]` `[`process`]](reference/reference.html#pytest.Collector.collect "pytest.Collector.collect") of directory collector nodes.

    [[`session.name`]](reference/reference.html#pytest.Session.name "pytest.Session.name") is now [`""`]; previously it was the rootdir directory name. This matches [[`session.nodeid`]](reference/reference.html#pytest.nodes.Node.nodeid "_pytest.nodes.Node.nodeid") which has always been [`""`].

    The collection tree now contains directories/packages up to the [[rootdir]](reference/customize.html#rootdir), for initial arguments that are found within the rootdir. For files outside the rootdir, only the immediate directory/package is collected -- note however that collecting from outside the rootdir is discouraged.

    As an example, given the following filesystem tree:

    ::: 
    ::: highlight
        myroot/
            pytest.ini
            top/
            ├── aaa
            │   └── test_aaa.py
            ├── test_a.py
            ├── test_b
            │   ├── __init__.py
            │   └── test_b.py
            ├── test_c.py
            └── zzz
                ├── __init__.py
                └── test_zzz.py
    :::
    :::

    the collection tree, as shown by [`pytest`]` `[`--collect-only`]` `[`top/`] but with the otherwise-hidden [[`Session`]](reference/reference.html#pytest.Session "pytest.Session") node added for clarity, is now the following:

    ::: 
    ::: highlight
        <Session>
          <Dir myroot>
            <Dir top>
              <Dir aaa>
                <Module test_aaa.py>
                  <Function test_it>
              <Module test_a.py>
                <Function test_it>
              <Package test_b>
                <Module test_b.py>
                  <Function test_it>
              <Module test_c.py>
                <Function test_it>
              <Package zzz>
                <Module test_zzz.py>
                  <Function test_it>
    :::
    :::

    Previously, it was:

    ::: 
    ::: highlight
        <Session>
          <Module top/test_a.py>
            <Function test_it>
          <Module top/test_c.py>
            <Function test_it>
          <Module top/aaa/test_aaa.py>
            <Function test_it>
          <Package test_b>
            <Module test_b.py>
              <Function test_it>
          <Package zzz>
            <Module test_zzz.py>
              <Function test_it>
    :::
    :::

    Code/plugins which rely on a specific shape of the collection tree might need to update.

-   [#11676](https://github.com/pytest-dev/pytest/issues/11676): The classes [[`Node`]](reference/reference.html#pytest.nodes.Node "_pytest.nodes.Node"), [[`Collector`]](reference/reference.html#pytest.Collector "pytest.Collector"), [[`Item`]](reference/reference.html#pytest.Item "pytest.Item"), [[`File`]](reference/reference.html#pytest.File "pytest.File"), [[`FSCollector`]](reference/reference.html#pytest.nodes.FSCollector "_pytest.nodes.FSCollector") are now marked abstract (see [[`abc`]](https://docs.python.org/3/library/abc.html#module-abc "(in Python v3.14)")).

    We do not expect this change to affect users and plugin authors, it will only cause errors when the code is already wrong or problematic.

#### Other breaking changes[¶](#other-breaking-changes "Link to this heading")

These are breaking changes where deprecation was not possible.

-   [#11282](https://github.com/pytest-dev/pytest/issues/11282): Sanitized the handling of the [`default`] parameter when defining configuration options.

    Previously if [`default`] was not supplied for [[`parser.addini`]](reference/reference.html#pytest.Parser.addini "pytest.Parser.addini") and the configuration option value was not defined in a test session, then calls to [[`config.getini`]](reference/reference.html#pytest.Config.getini "pytest.Config.getini") returned an *empty list* or an *empty string* depending on whether [`type`] was supplied or not respectively, which is clearly incorrect. Also, [`None`] was not honored even if [`default=None`] was used explicitly while defining the option.

    Now the behavior of [[`parser.addini`]](reference/reference.html#pytest.Parser.addini "pytest.Parser.addini") is as follows:

    -   If [`default`] is NOT passed but [`type`] is provided, then a type-specific default will be returned. For example [`type=bool`] will return [`False`], [`type=str`] will return [`""`], etc.

    -   If [`default=None`] is passed and the option is not defined in a test session, then [`None`] will be returned, regardless of the [`type`].

    -   If neither [`default`] nor [`type`] are provided, assume [`type=str`] and return [`""`] as default (this is as per previous behavior).

    The team decided to not introduce a deprecation period for this change, as doing so would be complicated both in terms of communicating this to the community as well as implementing it, and also because the team believes this change should not break existing plugins except in rare cases.

-   [#11667](https://github.com/pytest-dev/pytest/issues/11667): pytest's [`setup.py`] file is removed. If you relied on this file, e.g. to install pytest using [`setup.py`]` `[`install`], please see [Why you shouldn't invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html#summary) for alternatives.

-   [#9288](https://github.com/pytest-dev/pytest/issues/9288): [[`warns()`]](reference/reference.html#pytest.warns "pytest.warns") now re-emits unmatched warnings when the context closes -- previously it would consume all warnings, hiding those that were not matched by the function.

    While this is a new feature, we announce it as a breaking change because many test suites are configured to error-out on warnings, and will therefore fail on the newly-re-emitted warnings.

-   The internal [`FixtureManager.getfixtureclosure`] method has changed. Plugins which use this method or which subclass [`FixtureManager`] and overwrite that method will need to adapt to the change.

### Deprecations[¶](#id322 "Link to this heading")

-   [#10465](https://github.com/pytest-dev/pytest/issues/10465): Test functions returning a value other than [`None`] will now issue a [[`pytest.PytestWarning`]](reference/reference.html#pytest.PytestWarning "pytest.PytestWarning") instead of [`pytest.PytestRemovedIn8Warning`], meaning this will stay a warning instead of becoming an error in the future.

-   [#3664](https://github.com/pytest-dev/pytest/issues/3664): Applying a mark to a fixture function now issues a warning: marks in fixtures never had any effect, but it is a common user error to apply a mark to a fixture (for example [`usefixtures`]) and expect it to work.

    This will become an error in pytest 9.0.

### Features and Improvements[¶](#features-and-improvements "Link to this heading")

#### Improved Diffs[¶](#improved-diffs "Link to this heading")

These changes improve the diffs that pytest prints when an assertion fails. Note that syntax highlighting requires the [`pygments`] package.

-   [#11520](https://github.com/pytest-dev/pytest/issues/11520): The very verbose ([`-vv`]) diff output is now colored as a diff instead of a big chunk of red.

    Python code in error reports is now syntax-highlighted as Python.

    The sections in the error reports are now better separated.

-   [#1531](https://github.com/pytest-dev/pytest/issues/1531): The very verbose diff ([`-vv`]) for every standard library container type is improved. The indentation is now consistent and the markers are on their own separate lines, which should reduce the diffs shown to users.

    Previously, the standard Python pretty printer was used to generate the output, which puts opening and closing markers on the same line as the first/last entry, in addition to not having consistent indentation.

-   [#10617](https://github.com/pytest-dev/pytest/issues/10617): Added more comprehensive set assertion rewrites for comparisons other than equality [`==`], with the following operations now providing better failure messages: [`!=`], [`<=`], [`>=`], [`<`], and [`>`].

#### Separate Control For Assertion Verbosity[¶](#separate-control-for-assertion-verbosity "Link to this heading")

-   [#11387](https://github.com/pytest-dev/pytest/issues/11387): Added the new [[`verbosity_assertions`]](reference/reference.html#confval-verbosity_assertions) configuration option for fine-grained control of failed assertions verbosity.

    If you've ever wished that pytest always show you full diffs, but without making everything else verbose, this is for you.

    See [[Fine-grained verbosity]](how-to/output.html#pytest-fine-grained-verbosity) for more details.

    For plugin authors, [[`config.get_verbosity`]](reference/reference.html#pytest.Config.get_verbosity "pytest.Config.get_verbosity") can be used to retrieve the verbosity level for a specific verbosity type.

#### Additional Support For Exception Groups and [`__notes__`][¶](#additional-support-for-exception-groups-and-notes "Link to this heading")

These changes improve pytest's support for exception groups.

-   [#10441](https://github.com/pytest-dev/pytest/issues/10441): Added [[`ExceptionInfo.group_contains()`]](reference/reference.html#pytest.ExceptionInfo.group_contains "pytest.ExceptionInfo.group_contains"), an assertion helper that tests if an [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)") contains a matching exception.

    See [[Assertions about expected exception groups]](how-to/assert.html#assert-matching-exception-groups) for an example.

-   [#11227](https://github.com/pytest-dev/pytest/issues/11227): Allow [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") [`match`] argument to match against [`PEP-678`]` `[`<https://peps.python.org/pep-0678/>`] [`__notes__`].

#### Custom Directory collectors[¶](#custom-directory-collectors "Link to this heading")

-   [#7777](https://github.com/pytest-dev/pytest/issues/7777): Added a new hook [[`pytest_collect_directory`]](reference/reference.html#std-hook-pytest_collect_directory), which is called by filesystem-traversing collector nodes, such as [[`pytest.Session`]](reference/reference.html#pytest.Session "pytest.Session"), [[`pytest.Dir`]](reference/reference.html#pytest.Dir "pytest.Dir") and [[`pytest.Package`]](reference/reference.html#pytest.Package "pytest.Package"), to create a collector node for a sub-directory. It is expected to return a subclass of [[`pytest.Directory`]](reference/reference.html#pytest.Directory "pytest.Directory"). This hook allows plugins to [[customize the collection of directories]](example/customdirectory.html#custom-directory-collectors).

#### "New-style" Hook Wrappers[¶](#new-style-hook-wrappers "Link to this heading")

-   [#11122](https://github.com/pytest-dev/pytest/issues/11122): pytest now uses "new-style" hook wrappers internally, available since pluggy 1.2.0. See [pluggy's 1.2.0 changelog](https://pluggy.readthedocs.io/en/latest/changelog.html#pluggy-1-2-0-2023-06-21) and the [[updated docs]](how-to/writing_hook_functions.html#hookwrapper) for details.

    Plugins which want to use new-style wrappers can do so if they require [`pytest>=8`].

#### Other Improvements[¶](#other-improvements "Link to this heading")

-   [#11216](https://github.com/pytest-dev/pytest/issues/11216): If a test is skipped from inside an [[xunit setup fixture]](how-to/xunit_setup.html#classic-xunit), the test summary now shows the test location instead of the fixture location.

-   [#11314](https://github.com/pytest-dev/pytest/issues/11314): Logging to a file using the [`--log-file`] option will use [`--log-level`], [`--log-format`] and [`--log-date-format`] as fallback if [`--log-file-level`], [`--log-file-format`] and [`--log-file-date-format`] are not provided respectively.

-   [#11610](https://github.com/pytest-dev/pytest/issues/11610): Added the [[`LogCaptureFixture.filtering()`]](reference/reference.html#pytest.LogCaptureFixture.filtering "pytest.LogCaptureFixture.filtering") context manager which adds a given [[`logging.Filter`]](https://docs.python.org/3/library/logging.html#logging.Filter "(in Python v3.14)") object to the [[`caplog`]](reference/reference.html#std-fixture-caplog) fixture.

-   [#11447](https://github.com/pytest-dev/pytest/issues/11447): [[`pytest.deprecated_call()`]](reference/reference.html#pytest.deprecated_call "pytest.deprecated_call") now also considers warnings of type [[`FutureWarning`]](https://docs.python.org/3/library/exceptions.html#FutureWarning "(in Python v3.14)").

-   [#11600](https://github.com/pytest-dev/pytest/issues/11600): Improved the documentation and type signature for [[`pytest.mark.xfail`]](reference/reference.html#pytest.mark.xfail "pytest.mark.xfail")'s [`condition`] param to use [`False`] as the default value.

-   [#7469](https://github.com/pytest-dev/pytest/issues/7469): [[`FixtureDef`]](reference/reference.html#pytest.FixtureDef "pytest.FixtureDef") is now exported as [`pytest.FixtureDef`] for typing purposes.

-   [#11353](https://github.com/pytest-dev/pytest/issues/11353): Added typing to [[`PytestPluginManager`]](reference/reference.html#pytest.PytestPluginManager "pytest.PytestPluginManager").

### Bug Fixes[¶](#id340 "Link to this heading")

-   [#10701](https://github.com/pytest-dev/pytest/issues/10701): [[`pytest.WarningsRecorder.pop()`]](reference/reference.html#pytest.WarningsRecorder.pop "pytest.WarningsRecorder.pop") will return the most-closely-matched warning in the list, rather than the first warning which is an instance of the requested type.

-   [#11255](https://github.com/pytest-dev/pytest/issues/11255): Fixed crash on [`parametrize(...,`]` `[`scope="package")`] without a package present.

-   [#11277](https://github.com/pytest-dev/pytest/issues/11277): Fixed a bug that when there are multiple fixtures for an indirect parameter, the scope of the highest-scope fixture is picked for the parameter set, instead of that of the one with the narrowest scope.

-   [#11456](https://github.com/pytest-dev/pytest/issues/11456): Parametrized tests now *really do* ensure that the ids given to each input are unique - for example, [`a,`]` `[`a,`]` `[`a0`] now results in [`a1,`]` `[`a2,`]` `[`a0`] instead of the previous (buggy) [`a0,`]` `[`a1,`]` `[`a0`]. This necessarily means changing nodeids where these were previously colliding, and for readability adds an underscore when non-unique ids end in a number.

-   [#11563](https://github.com/pytest-dev/pytest/issues/11563): Fixed a crash when using an empty string for the same parametrized value more than once.

-   [#11712](https://github.com/pytest-dev/pytest/issues/11712): Fixed handling [`NO_COLOR`] and [`FORCE_COLOR`] to ignore an empty value.

-   [#9036](https://github.com/pytest-dev/pytest/issues/9036): [`pytest.warns`] and similar functions now capture warnings when an exception is raised inside a [`with`] block.

### Improved Documentation[¶](#id348 "Link to this heading")

-   [#11011](https://github.com/pytest-dev/pytest/issues/11011): Added a warning about modifying the root logger during tests when using [`caplog`].

-   [#11065](https://github.com/pytest-dev/pytest/issues/11065): Use [`pytestconfig`] instead of [`request.config`] in cache example to be consistent with the API documentation.

### Trivial/Internal Changes[¶](#id351 "Link to this heading")

-   [#11208](https://github.com/pytest-dev/pytest/issues/11208): The (internal) [`FixtureDef.cached_result`] type has changed. Now the third item [`cached_result[2]`], when set, is an exception instance instead of an exception triplet.

-   [#11218](https://github.com/pytest-dev/pytest/issues/11218): (This entry is meant to assist plugins which access private pytest internals to instantiate [`FixtureRequest`] objects.)

    [[`FixtureRequest`]](reference/reference.html#pytest.FixtureRequest "pytest.FixtureRequest") is now an abstract class which can't be instantiated directly. A new concrete [`TopRequest`] subclass of [`FixtureRequest`] has been added for the [`request`] fixture in test functions, as counterpart to the existing [`SubRequest`] subclass for the [`request`] fixture in fixture functions.

-   [#11315](https://github.com/pytest-dev/pytest/issues/11315): The [[`pytester`]](reference/reference.html#std-fixture-pytester) fixture now uses the [[`monkeypatch`]](reference/reference.html#std-fixture-monkeypatch) fixture to manage the current working directory. If you use [`pytester`] in combination with [[`monkeypatch.undo()`]](reference/reference.html#pytest.MonkeyPatch.undo "pytest.MonkeyPatch.undo"), the CWD might get restored. Use [[`monkeypatch.context()`]](reference/reference.html#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context") instead.

-   [#11333](https://github.com/pytest-dev/pytest/issues/11333): Corrected the spelling of [`Config.ArgsSource.INVOCATION_DIR`]. The previous spelling [`INCOVATION_DIR`] remains as an alias.

-   [#11638](https://github.com/pytest-dev/pytest/issues/11638): Fixed the selftests to pass correctly if [`FORCE_COLOR`], [`NO_COLOR`] or [`PY_COLORS`] is set in the calling environment.

## pytest 7.4.4 (2023-12-31)[¶](#pytest-7-4-4-2023-12-31 "Link to this heading")

### Bug Fixes[¶](#id357 "Link to this heading")

-   [#11140](https://github.com/pytest-dev/pytest/issues/11140): Fix non-string constants at the top of file being detected as docstrings on Python\>=3.8.

-   [#11572](https://github.com/pytest-dev/pytest/issues/11572): Handle an edge case where [[`sys.stderr`]](https://docs.python.org/3/library/sys.html#sys.stderr "(in Python v3.14)") and [[`sys.__stderr__`]](https://docs.python.org/3/library/sys.html#sys.__stderr__ "(in Python v3.14)") might already be closed when [[Fault Handler]](how-to/failures.html#faulthandler) is tearing down.

-   [#11710](https://github.com/pytest-dev/pytest/issues/11710): Fixed tracebacks from collection errors not getting pruned.

-   [#7966](https://github.com/pytest-dev/pytest/issues/7966): Removed unhelpful error message from assertion rewrite mechanism when exceptions are raised in [`__iter__`] methods. Now they are treated un-iterable instead.

### Improved Documentation[¶](#id362 "Link to this heading")

-   [#11091](https://github.com/pytest-dev/pytest/issues/11091): Updated documentation to refer to hyphenated options: replaced [`--junitxml`] with [`--junit-xml`] and [`--collectonly`] with [`--collect-only`].

## pytest 7.4.3 (2023-10-24)[¶](#pytest-7-4-3-2023-10-24 "Link to this heading")

### Bug Fixes[¶](#id364 "Link to this heading")

-   [#10447](https://github.com/pytest-dev/pytest/issues/10447): Markers are now considered in the reverse mro order to ensure base class markers are considered first -- this resolves a regression.

-   [#11239](https://github.com/pytest-dev/pytest/issues/11239): Fixed [`:=`] in asserts impacting unrelated test cases.

-   [#11439](https://github.com/pytest-dev/pytest/issues/11439): Handled an edge case where [[`sys.stderr`]](https://docs.python.org/3/library/sys.html#sys.stderr "(in Python v3.14)") might already be closed when [[Fault Handler]](how-to/failures.html#faulthandler) is tearing down.

## pytest 7.4.2 (2023-09-07)[¶](#pytest-7-4-2-2023-09-07 "Link to this heading")

### Bug Fixes[¶](#id368 "Link to this heading")

-   [#11237](https://github.com/pytest-dev/pytest/issues/11237): Fix doctest collection of [`functools.cached_property`] objects.

-   [#11306](https://github.com/pytest-dev/pytest/issues/11306): Fixed bug using [`--importmode=importlib`] which would cause package [`__init__.py`] files to be imported more than once in some cases.

-   [#11367](https://github.com/pytest-dev/pytest/issues/11367): Fixed bug where [`user_properties`] where not being saved in the JUnit XML file if a fixture failed during teardown.

-   [#11394](https://github.com/pytest-dev/pytest/issues/11394): Fixed crash when parsing long command line arguments that might be interpreted as files.

### Improved Documentation[¶](#id373 "Link to this heading")

-   [#11391](https://github.com/pytest-dev/pytest/issues/11391): Improved disclaimer on pytest plugin reference page to better indicate this is an automated, non-curated listing.

## pytest 7.4.1 (2023-09-02)[¶](#pytest-7-4-1-2023-09-02 "Link to this heading")

### Bug Fixes[¶](#id375 "Link to this heading")

-   [#10337](https://github.com/pytest-dev/pytest/issues/10337): Fixed bug where fake intermediate modules generated by [`--import-mode=importlib`] would not include the child modules as attributes of the parent modules.

-   [#10702](https://github.com/pytest-dev/pytest/issues/10702): Fixed error assertion handling in [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") when [`None`] is an expected or received value when comparing dictionaries.

-   [#10811](https://github.com/pytest-dev/pytest/issues/10811): Fixed issue when using [`--import-mode=importlib`] together with [`--doctest-modules`] that caused modules to be imported more than once, causing problems with modules that have import side effects.

## pytest 7.4.0 (2023-06-23)[¶](#pytest-7-4-0-2023-06-23 "Link to this heading")

### Features[¶](#id379 "Link to this heading")

-   [#10901](https://github.com/pytest-dev/pytest/issues/10901): Added [[`ExceptionInfo.from_exception()`]](reference/reference.html#pytest.ExceptionInfo.from_exception "pytest.ExceptionInfo.from_exception"), a simpler way to create an [[`ExceptionInfo`]](reference/reference.html#pytest.ExceptionInfo "pytest.ExceptionInfo") from an exception. This can replace [[`ExceptionInfo.from_exc_info()`]](reference/reference.html#pytest.ExceptionInfo.from_exc_info "pytest.ExceptionInfo.from_exc_info") for most uses.

### Improvements[¶](#id381 "Link to this heading")

-   [#10872](https://github.com/pytest-dev/pytest/issues/10872): Update test log report annotation to named tuple and fixed inconsistency in docs for [[`pytest_report_teststatus`]](reference/reference.html#std-hook-pytest_report_teststatus) hook.

-   [#10907](https://github.com/pytest-dev/pytest/issues/10907): When an exception traceback to be displayed is completely filtered out (by mechanisms such as [`__tracebackhide__`], internal frames, and similar), now only the exception string and the following message are shown:

    "All traceback entries are hidden. Pass [`--full-trace`] to see hidden and internal frames.".

    Previously, the last frame of the traceback was shown, even though it was hidden.

-   [#10940](https://github.com/pytest-dev/pytest/issues/10940): Improved verbose output ([`-vv`]) of [`skip`] and [`xfail`] reasons by performing text wrapping while leaving a clear margin for progress output.

    Added [`TerminalReporter.wrap_write()`] as a helper for that.

-   [#10991](https://github.com/pytest-dev/pytest/issues/10991): Added handling of [`%f`] directive to print microseconds in log format options, such as [`log-date-format`].

-   [#11005](https://github.com/pytest-dev/pytest/issues/11005): Added the underlying exception to the cache provider's path creation and write warning messages.

-   [#11013](https://github.com/pytest-dev/pytest/issues/11013): Added warning when [[`testpaths`]](reference/reference.html#confval-testpaths) is set, but paths are not found by glob. In this case, pytest will fall back to searching from the current directory.

-   [#11043](https://github.com/pytest-dev/pytest/issues/11043): When [`--confcutdir`] is not specified, and there is no config file present, the conftest cutoff directory ([`--confcutdir`]) is now set to the [[rootdir]](reference/customize.html#rootdir). Previously in such cases, [`conftest.py`] files would be probed all the way to the root directory of the filesystem. If you are badly affected by this change, consider adding an empty config file to your desired cutoff directory, or explicitly set [`--confcutdir`].

-   [#11081](https://github.com/pytest-dev/pytest/issues/11081): The [[`norecursedirs`]](reference/reference.html#confval-norecursedirs) check is now performed in a [[`pytest_ignore_collect`]](reference/reference.html#std-hook-pytest_ignore_collect) implementation, so plugins can affect it.

    If after updating to this version you see that your [`norecursedirs`] setting is not being respected, it means that a conftest or a plugin you use has a bad [`pytest_ignore_collect`] implementation. Most likely, your hook returns [`False`] for paths it does not want to ignore, which ends the processing and doesn't allow other plugins, including pytest itself, to ignore the path. The fix is to return [`None`] instead of [`False`] for paths your hook doesn't want to ignore.

-   [#8711](https://github.com/pytest-dev/pytest/issues/8711): [[`caplog.set_level()`]](reference/reference.html#pytest.LogCaptureFixture.set_level "pytest.LogCaptureFixture.set_level") and [[`caplog.at_level()`]](reference/reference.html#pytest.LogCaptureFixture.at_level "pytest.LogCaptureFixture.at_level") will temporarily enable the requested [`level`] if [`level`] was disabled globally via [`logging.disable(LEVEL)`].

### Bug Fixes[¶](#id391 "Link to this heading")

-   [#10831](https://github.com/pytest-dev/pytest/issues/10831): Terminal Reporting: Fixed bug when running in [`--tb=line`] mode where [`pytest.fail(pytrace=False)`] tests report [`None`].

-   [#11068](https://github.com/pytest-dev/pytest/issues/11068): Fixed the [`--last-failed`] whole-file skipping functionality ("skipped N files") for [[non-python test files]](example/nonpython.html#non-python-tests).

-   [#11104](https://github.com/pytest-dev/pytest/issues/11104): Fixed a regression in pytest 7.3.2 which caused to [[`testpaths`]](reference/reference.html#confval-testpaths) to be considered for loading initial conftests, even when it was not utilized (e.g. when explicit paths were given on the command line). Now the [`testpaths`] are only considered when they are in use.

-   [#1904](https://github.com/pytest-dev/pytest/issues/1904): Fixed traceback entries hidden with [`__tracebackhide__`]` `[`=`]` `[`True`] still being shown for chained exceptions (parts after "... the above exception ..." message).

-   [#7781](https://github.com/pytest-dev/pytest/issues/7781): Fix writing non-encodable text to log file when using [`--debug`].

### Improved Documentation[¶](#id397 "Link to this heading")

-   [#9146](https://github.com/pytest-dev/pytest/issues/9146): Improved documentation for [[`caplog.set_level()`]](reference/reference.html#pytest.LogCaptureFixture.set_level "pytest.LogCaptureFixture.set_level").

### Trivial/Internal Changes[¶](#id399 "Link to this heading")

-   [#11031](https://github.com/pytest-dev/pytest/issues/11031): Enhanced the CLI flag for [`-c`] to now include [`--config-file`] to make it clear that this flag applies to the usage of a custom config file.

## pytest 7.3.2 (2023-06-10)[¶](#pytest-7-3-2-2023-06-10 "Link to this heading")

### Bug Fixes[¶](#id401 "Link to this heading")

-   [#10169](https://github.com/pytest-dev/pytest/issues/10169): Fix bug where very long option names could cause pytest to break with [`OSError:`]` `[`[Errno`]` `[`36]`]` `[`File`]` `[`name`]` `[`too`]` `[`long`] on some systems.

-   [#10894](https://github.com/pytest-dev/pytest/issues/10894): Support for Python 3.12 (beta at the time of writing).

-   [#10987](https://github.com/pytest-dev/pytest/issues/10987): [[`testpaths`]](reference/reference.html#confval-testpaths) is now honored to load root [`conftests`].

-   [#10999](https://github.com/pytest-dev/pytest/issues/10999): The [`monkeypatch`] [`setitem`]/[`delitem`] type annotations now allow [`TypedDict`] arguments.

-   [#11028](https://github.com/pytest-dev/pytest/issues/11028): Fixed bug in assertion rewriting where a variable assigned with the walrus operator could not be used later in a function call.

-   [#11054](https://github.com/pytest-dev/pytest/issues/11054): Fixed [`--last-failed`]'s "(skipped N files)" functionality for files inside of packages (directories with [`__init__.py`] files).

## pytest 7.3.1 (2023-04-14)[¶](#pytest-7-3-1-2023-04-14 "Link to this heading")

### Improvements[¶](#id408 "Link to this heading")

-   [#10875](https://github.com/pytest-dev/pytest/issues/10875): Python 3.12 support: fixed [`RuntimeError:`]` `[`TestResult`]` `[`has`]` `[`no`]` `[`addDuration`]` `[`method`] when running [`unittest`] tests.

-   [#10890](https://github.com/pytest-dev/pytest/issues/10890): Python 3.12 support: fixed [`shutil.rmtree(onerror=...)`] deprecation warning when using [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path).

### Bug Fixes[¶](#id411 "Link to this heading")

-   [#10896](https://github.com/pytest-dev/pytest/issues/10896): Fixed performance regression related to [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) and the new [[`tmp_path_retention_policy`]](reference/reference.html#confval-tmp_path_retention_policy) option.

-   [#10903](https://github.com/pytest-dev/pytest/issues/10903): Fix crash [`INTERNALERROR`]` `[`IndexError:`]` `[`list`]` `[`index`]` `[`out`]` `[`of`]` `[`range`] which happens when displaying an exception where all entries are hidden. This reverts the change "Correctly handle [`__tracebackhide__`] for chained exceptions." introduced in version 7.3.0.

## pytest 7.3.0 (2023-04-08)[¶](#pytest-7-3-0-2023-04-08 "Link to this heading")

### Features[¶](#id414 "Link to this heading")

-   [#10525](https://github.com/pytest-dev/pytest/issues/10525): Test methods decorated with [`@classmethod`] can now be discovered as tests, following the same rules as normal methods. This fills the gap that static methods were discoverable as tests but not class methods.

-   [#10755](https://github.com/pytest-dev/pytest/issues/10755): [[`console_output_style`]](reference/reference.html#confval-console_output_style) now supports [`progress-even-when-capture-no`] to force the use of the progress output even when capture is disabled. This is useful in large test suites where capture may have significant performance impact.

-   [#7431](https://github.com/pytest-dev/pytest/issues/7431): [`--log-disable`] CLI option added to disable individual loggers.

-   [#8141](https://github.com/pytest-dev/pytest/issues/8141): Added [[`tmp_path_retention_count`]](reference/reference.html#confval-tmp_path_retention_count) and [[`tmp_path_retention_policy`]](reference/reference.html#confval-tmp_path_retention_policy) configuration options to control how directories created by the [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) fixture are kept.

### Improvements[¶](#id419 "Link to this heading")

-   [#10226](https://github.com/pytest-dev/pytest/issues/10226): If multiple errors are raised in teardown, we now re-raise an [`ExceptionGroup`] of them instead of discarding all but the last.

-   [#10658](https://github.com/pytest-dev/pytest/issues/10658): Allow [`-p`] arguments to include spaces (eg: [`-p`]` `[`no:logging`] instead of [`-pno:logging`]). Mostly useful in the [`addopts`] section of the configuration file.

-   [#10710](https://github.com/pytest-dev/pytest/issues/10710): Added [`start`] and [`stop`] timestamps to [`TestReport`] objects.

-   [#10727](https://github.com/pytest-dev/pytest/issues/10727): Split the report header for [`rootdir`], [`config`]` `[`file`] and [`testpaths`] so each has its own line.

-   [#10840](https://github.com/pytest-dev/pytest/issues/10840): pytest should no longer crash on AST with pathological position attributes, for example testing AST produced by [`Hylang`]` `[`<https://github.com/hylang/hy>__`].

-   [#6267](https://github.com/pytest-dev/pytest/issues/6267): The full output of a test is no longer truncated if the truncation message would be longer than the hidden text. The line number shown has also been fixed.

### Bug Fixes[¶](#id426 "Link to this heading")

-   [#10743](https://github.com/pytest-dev/pytest/issues/10743): The assertion rewriting mechanism now works correctly when assertion expressions contain the walrus operator.

-   [#10765](https://github.com/pytest-dev/pytest/issues/10765): Fixed [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) fixture always raising [[`OSError`]](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.14)") on [`emscripten`] platform due to missing [[`os.getuid()`]](https://docs.python.org/3/library/os.html#os.getuid "(in Python v3.14)").

-   [#1904](https://github.com/pytest-dev/pytest/issues/1904): Correctly handle [`__tracebackhide__`] for chained exceptions. NOTE: This change was reverted in version 7.3.1.

### Improved Documentation[¶](#id430 "Link to this heading")

-   [#10782](https://github.com/pytest-dev/pytest/issues/10782): Fixed the minimal example in [[Good Integration Practices]](explanation/goodpractices.html#goodpractices): [`pip`]` `[`install`]` `[`-e`]` `[`.`] requires a [`version`] entry in [`pyproject.toml`] to run successfully.

### Trivial/Internal Changes[¶](#id432 "Link to this heading")

-   [#10669](https://github.com/pytest-dev/pytest/issues/10669): pytest no longer directly depends on the [attrs](https://www.attrs.org/en/stable/) package. While we at pytest all love the package dearly and would like to thank the [`attrs`] team for many years of cooperation and support, it makes sense for [`pytest`] to have as little external dependencies as possible, as this helps downstream projects. With that in mind, we have replaced the pytest's limited internal usage to use the standard library's [`dataclasses`] instead.

    Nice diffs for [`attrs`] classes are still supported though.

## pytest 7.2.2 (2023-03-03)[¶](#pytest-7-2-2-2023-03-03 "Link to this heading")

### Bug Fixes[¶](#id434 "Link to this heading")

-   [#10533](https://github.com/pytest-dev/pytest/issues/10533): Fixed [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") handling of dictionaries containing one or more values of [`0.0`].

-   [#10592](https://github.com/pytest-dev/pytest/issues/10592): Fixed crash if [`--cache-show`] and [`--help`] are passed at the same time.

-   [#10597](https://github.com/pytest-dev/pytest/issues/10597): Fixed bug where a fixture method named [`teardown`] would be called as part of [`nose`] teardown stage.

-   [#10626](https://github.com/pytest-dev/pytest/issues/10626): Fixed crash if [`--fixtures`] and [`--help`] are passed at the same time.

-   [#10660](https://github.com/pytest-dev/pytest/issues/10660): Fixed [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") to return a 'ContextManager' so that type-checkers could narrow [`pytest.raises(...)`]` `[`if`]` `[`...`]` `[`else`]` `[`nullcontext()`] down to 'ContextManager' rather than 'object'.

### Improved Documentation[¶](#id440 "Link to this heading")

-   [#10690](https://github.com/pytest-dev/pytest/issues/10690): Added [`CI`] and [`BUILD_NUMBER`] environment variables to the documentation.

-   [#10721](https://github.com/pytest-dev/pytest/issues/10721): Fixed entry-points declaration in the documentation example using Hatch.

-   [#10753](https://github.com/pytest-dev/pytest/issues/10753): Changed wording of the module level skip to be very explicit about not collecting tests and not executing the rest of the module.

## pytest 7.2.1 (2023-01-13)[¶](#pytest-7-2-1-2023-01-13 "Link to this heading")

### Bug Fixes[¶](#id444 "Link to this heading")

-   [#10452](https://github.com/pytest-dev/pytest/issues/10452): Fix 'importlib.abc.TraversableResources' deprecation warning in Python 3.12.

-   [#10457](https://github.com/pytest-dev/pytest/issues/10457): If a test is skipped from inside a fixture, the test summary now shows the test location instead of the fixture location.

-   [#10506](https://github.com/pytest-dev/pytest/issues/10506): Fix bug where sometimes pytest would use the file system root directory as [[rootdir]](reference/customize.html#rootdir) on Windows.

-   [#10607](https://github.com/pytest-dev/pytest/issues/10607): Fix a race condition when creating junitxml reports, which could occur when multiple instances of pytest execute in parallel.

-   [#10641](https://github.com/pytest-dev/pytest/issues/10641): Fix a race condition when creating or updating the stepwise plugin's cache, which could occur when multiple xdist worker nodes try to simultaneously update the stepwise plugin's cache.

## pytest 7.2.0 (2022-10-23)[¶](#pytest-7-2-0-2022-10-23 "Link to this heading")

### Deprecations[¶](#id450 "Link to this heading")

-   [#10012](https://github.com/pytest-dev/pytest/issues/10012): Update [`pytest.PytestUnhandledCoroutineWarning`] to a deprecation; it will raise an error in pytest 8.

-   [#10396](https://github.com/pytest-dev/pytest/issues/10396): pytest no longer depends on the [`py`] library. [`pytest`] provides a vendored copy of [`py.error`] and [`py.path`] modules but will use the [`py`] library if it is installed. If you need other [`py.*`] modules, continue to install the deprecated [`py`] library separately, otherwise it can usually be removed as a dependency.

-   [#4562](https://github.com/pytest-dev/pytest/issues/4562): Deprecate configuring hook specs/impls using attributes/marks.

    Instead use [[`pytest.hookimpl()`]](reference/reference.html#pytest.hookimpl "pytest.hookimpl") and [[`pytest.hookspec()`]](reference/reference.html#pytest.hookspec "pytest.hookspec"). For more details, see the [[docs]](deprecations.html#legacy-path-hooks-deprecated).

-   [#9886](https://github.com/pytest-dev/pytest/issues/9886): The functionality for running tests written for [`nose`] has been officially deprecated.

    This includes:

    -   Plain [`setup`] and [`teardown`] functions and methods: this might catch users by surprise, as [`setup()`] and [`teardown()`] are not pytest idioms, but part of the [`nose`] support.

    -   Setup/teardown using the [\@with_setup](with-setup-nose) decorator.

    For more details, consult the [[deprecation docs]](deprecations.html#nose-deprecation).

-   [#7337](https://github.com/pytest-dev/pytest/issues/7337): A deprecation warning is now emitted if a test function returns something other than [`None`]. This prevents a common mistake among beginners that expect that returning a [`bool`] (for example [`return`]` `[`foo(a,`]` `[`b)`]` `[`==`]` `[`result`]) would cause a test to pass or fail, instead of using [`assert`]. The plan is to make returning non-[`None`] from tests an error in the future.

### Features[¶](#id456 "Link to this heading")

-   [#9897](https://github.com/pytest-dev/pytest/issues/9897): Added shell-style wildcard support to [`testpaths`].

### Improvements[¶](#id458 "Link to this heading")

-   [#10218](https://github.com/pytest-dev/pytest/issues/10218): [`@pytest.mark.parametrize()`] (and similar functions) now accepts any [`Sequence[str]`] for the argument names, instead of just [`list[str]`] and [`tuple[str,`]` `[`...]`].

    (Note that [`str`], which is itself a [`Sequence[str]`], is still treated as a comma-delimited name list, as before).

-   [#10381](https://github.com/pytest-dev/pytest/issues/10381): The [`--no-showlocals`] flag has been added. This can be passed directly to tests to override [`--showlocals`] declared through [`addopts`].

-   [#3426](https://github.com/pytest-dev/pytest/issues/3426): Assertion failures with strings in NFC and NFD forms that normalize to the same string now have a dedicated error message detailing the issue, and their utf-8 representation is expressed instead.

-   [#8508](https://github.com/pytest-dev/pytest/issues/8508): Introduce multiline display for warning matching via [[`pytest.warns()`]](reference/reference.html#pytest.warns "pytest.warns") and enhance match comparison for [[`pytest.ExceptionInfo.match()`]](reference/reference.html#pytest.ExceptionInfo.match "pytest.ExceptionInfo.match") as returned by [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises").

-   [#8646](https://github.com/pytest-dev/pytest/issues/8646): Improve [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises"). Previously passing an empty tuple would give a confusing error. We now raise immediately with a more helpful message.

-   [#9741](https://github.com/pytest-dev/pytest/issues/9741): On Python 3.11, use the standard library's [[`tomllib`]](https://docs.python.org/3/library/tomllib.html#module-tomllib "(in Python v3.14)") to parse TOML.

    [`tomli`] is no longer a dependency on Python 3.11.

-   [#9742](https://github.com/pytest-dev/pytest/issues/9742): Display assertion message without escaped newline characters with [`-vv`].

-   [#9823](https://github.com/pytest-dev/pytest/issues/9823): Improved error message that is shown when no collector is found for a given file.

-   [#9873](https://github.com/pytest-dev/pytest/issues/9873): Some coloring has been added to the short test summary.

-   [#9883](https://github.com/pytest-dev/pytest/issues/9883): Normalize the help description of all command-line options.

-   [#9920](https://github.com/pytest-dev/pytest/issues/9920): Display full crash messages in [`short`]` `[`test`]` `[`summary`]` `[`info`], when running in a CI environment.

-   [#9987](https://github.com/pytest-dev/pytest/issues/9987): Added support for hidden configuration file by allowing [`.pytest.ini`] as an alternative to [`pytest.ini`].

### Bug Fixes[¶](#id471 "Link to this heading")

-   [#10150](https://github.com/pytest-dev/pytest/issues/10150): [[`sys.stdin`]](https://docs.python.org/3/library/sys.html#sys.stdin "(in Python v3.14)") now contains all expected methods of a file-like object when capture is enabled.

-   [#10382](https://github.com/pytest-dev/pytest/issues/10382): Do not break into pdb when [`raise`]` `[`unittest.SkipTest()`] appears top-level in a file.

-   [#7792](https://github.com/pytest-dev/pytest/issues/7792): Marks are now inherited according to the full MRO in test classes. Previously, if a test class inherited from two or more classes, only marks from the first super-class would apply.

    When inheriting marks from super-classes, marks from the sub-classes are now ordered before marks from the super-classes, in MRO order. Previously it was the reverse.

    When inheriting marks from super-classes, the [`pytestmark`] attribute of the sub-class now only contains the marks directly applied to it. Previously, it also contained marks from its super-classes. Please note that this attribute should not normally be accessed directly; use [[`Node.iter_markers`]](reference/reference.html#pytest.nodes.Node.iter_markers "_pytest.nodes.Node.iter_markers") instead.

-   [#9159](https://github.com/pytest-dev/pytest/issues/9159): Showing inner exceptions by forcing native display in [`ExceptionGroups`] even when using display options other than [`--tb=native`]. A temporary step before full implementation of pytest-native display for inner exceptions in [`ExceptionGroups`].

-   [#9877](https://github.com/pytest-dev/pytest/issues/9877): Ensure [`caplog.get_records(when)`] returns current/correct data after invoking [`caplog.clear()`].

### Improved Documentation[¶](#id477 "Link to this heading")

-   [#10344](https://github.com/pytest-dev/pytest/issues/10344): Update information on writing plugins to use [`pyproject.toml`] instead of [`setup.py`].

-   [#9248](https://github.com/pytest-dev/pytest/issues/9248): The documentation is now built using Sphinx 5.x (up from 3.x previously).

-   [#9291](https://github.com/pytest-dev/pytest/issues/9291): Update documentation on how [[`pytest.warns()`]](reference/reference.html#pytest.warns "pytest.warns") affects [[`DeprecationWarning`]](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)").

### Trivial/Internal Changes[¶](#id481 "Link to this heading")

-   [#10313](https://github.com/pytest-dev/pytest/issues/10313): Made [`_pytest.doctest.DoctestItem`] export [`pytest.DoctestItem`] for type check and runtime purposes. Made [`_pytest.doctest`] use internal APIs to avoid circular imports.

-   [#9906](https://github.com/pytest-dev/pytest/issues/9906): Made [`_pytest.compat`] re-export [`importlib_metadata`] in the eyes of type checkers.

-   [#9910](https://github.com/pytest-dev/pytest/issues/9910): Fix default encoding warning ([`EncodingWarning`]) in [`cacheprovider`]

-   [#9984](https://github.com/pytest-dev/pytest/issues/9984): Improve the error message when we attempt to access a fixture that has been torn down. Add an additional sentence to the docstring explaining when it's not a good idea to call [`getfixturevalue`].

## pytest 7.1.3 (2022-08-31)[¶](#pytest-7-1-3-2022-08-31 "Link to this heading")

### Bug Fixes[¶](#id486 "Link to this heading")

-   [#10060](https://github.com/pytest-dev/pytest/issues/10060): When running with [`--pdb`], [`TestCase.tearDown`] is no longer called for tests when the *class* has been skipped via [`unittest.skip`] or [`pytest.mark.skip`].

-   [#10190](https://github.com/pytest-dev/pytest/issues/10190): Invalid XML characters in setup or teardown error messages are now properly escaped for JUnit XML reports.

-   [#10230](https://github.com/pytest-dev/pytest/issues/10230): Ignore [`.py`] files created by [`pyproject.toml`]-based editable builds introduced in [pip 21.3](https://pip.pypa.io/en/stable/news/#v21-3).

-   [#3396](https://github.com/pytest-dev/pytest/issues/3396): Doctests now respect the [`--import-mode`] flag.

-   [#9514](https://github.com/pytest-dev/pytest/issues/9514): Type-annotate [`FixtureRequest.param`] as [`Any`] as a stop gap measure until [#8073](https://github.com/pytest-dev/pytest/issues/8073) is fixed.

-   [#9791](https://github.com/pytest-dev/pytest/issues/9791): Fixed a path handling code in [`rewrite.py`] that seems to work fine, but was incorrect and fails in some systems.

-   [#9917](https://github.com/pytest-dev/pytest/issues/9917): Fixed string representation for [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") when used to compare tuples.

### Improved Documentation[¶](#id494 "Link to this heading")

-   [#9937](https://github.com/pytest-dev/pytest/issues/9937): Explicit note that [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir) fixture is discouraged in favour of [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path).

### Trivial/Internal Changes[¶](#id496 "Link to this heading")

-   [#10114](https://github.com/pytest-dev/pytest/issues/10114): Replace [atomicwrites](https://github.com/untitaker/python-atomicwrites) dependency on windows with [`os.replace`].

## pytest 7.1.2 (2022-04-23)[¶](#pytest-7-1-2-2022-04-23 "Link to this heading")

### Bug Fixes[¶](#id498 "Link to this heading")

-   [#9726](https://github.com/pytest-dev/pytest/issues/9726): An unnecessary [`numpy`] import inside [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") was removed.

-   [#9820](https://github.com/pytest-dev/pytest/issues/9820): Fix comparison of [`dataclasses`] with [`InitVar`].

-   [#9869](https://github.com/pytest-dev/pytest/issues/9869): Increase [`stacklevel`] for the [`NODE_CTOR_FSPATH_ARG`] deprecation to point to the user's code, not pytest.

-   [#9871](https://github.com/pytest-dev/pytest/issues/9871): Fix a bizarre (and fortunately rare) bug where the [`temp_path`] fixture could raise an internal error while attempting to get the current user's username.

## pytest 7.1.1 (2022-03-17)[¶](#pytest-7-1-1-2022-03-17 "Link to this heading")

### Bug Fixes[¶](#id503 "Link to this heading")

-   [#9767](https://github.com/pytest-dev/pytest/issues/9767): Fixed a regression in pytest 7.1.0 where some conftest.py files outside of the source tree (e.g. in the [`site-packages`] directory) were not picked up.

## pytest 7.1.0 (2022-03-13)[¶](#pytest-7-1-0-2022-03-13 "Link to this heading")

### Breaking Changes[¶](#id505 "Link to this heading")

-   [#8838](https://github.com/pytest-dev/pytest/issues/8838): As per our policy, the following features have been deprecated in the 6.X series and are now removed:

    -   [`pytest._fillfuncargs`] function.

    -   [`pytest_warning_captured`] hook - use [`pytest_warning_recorded`] instead.

    -   [`-k`]` `[`-foobar`] syntax - use [`-k`]` `[`'not`]` `[`foobar'`] instead.

    -   [`-k`]` `[`foobar:`] syntax.

    -   [`pytest.collect`] module - import from [`pytest`] directly.

    For more information consult [Deprecations and Removals](https://docs.pytest.org/en/latest/deprecations.html) in the docs.

-   [#9437](https://github.com/pytest-dev/pytest/issues/9437): Dropped support for Python 3.6, which reached [end-of-life](https://devguide.python.org/#status-of-python-branches) at 2021-12-23.

### Improvements[¶](#id508 "Link to this heading")

-   [#5192](https://github.com/pytest-dev/pytest/issues/5192): Fixed test output for some data types where [`-v`] would show less information.

    Also, when showing diffs for sequences, [`-q`] would produce full diffs instead of the expected diff.

-   [#9362](https://github.com/pytest-dev/pytest/issues/9362): pytest now avoids specialized assert formatting when it is detected that the default [`__eq__`] is overridden in [`attrs`] or [`dataclasses`].

-   [#9536](https://github.com/pytest-dev/pytest/issues/9536): When [`-vv`] is given on command line, show skipping and xfail reasons in full instead of truncating them to fit the terminal width.

-   [#9644](https://github.com/pytest-dev/pytest/issues/9644): More information about the location of resources that led Python to raise [[`ResourceWarning`]](https://docs.python.org/3/library/exceptions.html#ResourceWarning "(in Python v3.14)") can now be obtained by enabling [[`tracemalloc`]](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "(in Python v3.14)").

    See [[Resource Warnings]](how-to/capture-warnings.html#resource-warnings) for more information.

-   [#9678](https://github.com/pytest-dev/pytest/issues/9678): More types are now accepted in the [`ids`] argument to [`@pytest.mark.parametrize`]. Previously only [`str`], [`float`], [`int`] and [`bool`] were accepted; now [`bytes`], [`complex`], [`re.Pattern`], [`Enum`] and anything with a [`__name__`] are also accepted.

-   [#9692](https://github.com/pytest-dev/pytest/issues/9692): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now raises a [[`TypeError`]](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)") when given an unordered sequence (such as [[`set`]](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")).

    Note that this implies that custom classes which only implement [`__iter__`] and [`__len__`] are no longer supported as they don't guarantee order.

### Bug Fixes[¶](#id515 "Link to this heading")

-   [#8242](https://github.com/pytest-dev/pytest/issues/8242): The deprecation of raising [[`unittest.SkipTest`]](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "(in Python v3.14)") to skip collection of tests during the pytest collection phase is reverted - this is now a supported feature again.

-   [#9493](https://github.com/pytest-dev/pytest/issues/9493): Symbolic link components are no longer resolved in conftest paths. This means that if a conftest appears twice in collection tree, using symlinks, it will be executed twice. For example, given

    > <div>
    >
    > tests/real/conftest.py tests/real/test_it.py tests/link -\> tests/real
    >
    > </div>

    running [`pytest`]` `[`tests`] now imports the conftest twice, once as [`tests/real/conftest.py`] and once as [`tests/link/conftest.py`]. This is a fix to match a similar change made to test collection itself in pytest 6.0 (see [#6523](https://github.com/pytest-dev/pytest/pull/6523) for details).

-   [#9626](https://github.com/pytest-dev/pytest/issues/9626): Fixed count of selected tests on terminal collection summary when there were errors or skipped modules.

    If there were errors or skipped modules on collection, pytest would mistakenly subtract those from the selected count.

-   [#9645](https://github.com/pytest-dev/pytest/issues/9645): Fixed regression where [`--import-mode=importlib`] used together with [][[`PYTHONPATH`]](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH "(in Python v3.14)") or [[`pythonpath`]](reference/reference.html#confval-pythonpath) would cause import errors in test suites.

-   [#9708](https://github.com/pytest-dev/pytest/issues/9708): [[`pytester`]](reference/reference.html#std-fixture-pytester) now requests a [[`monkeypatch`]](reference/reference.html#std-fixture-monkeypatch) fixture instead of creating one internally. This solves some issues with tests that involve pytest environment variables.

-   [#9730](https://github.com/pytest-dev/pytest/issues/9730): Malformed [`pyproject.toml`] files now produce a clearer error message.

## pytest 7.0.1 (2022-02-11)[¶](#pytest-7-0-1-2022-02-11 "Link to this heading")

### Bug Fixes[¶](#id522 "Link to this heading")

-   [#9608](https://github.com/pytest-dev/pytest/issues/9608): Fix invalid importing of [`importlib.readers`] in Python 3.9.

-   [#9610](https://github.com/pytest-dev/pytest/issues/9610): Restore [`UnitTestFunction.obj`] to return unbound rather than bound method. Fixes a crash during a failed teardown in unittest TestCases with non-default [`__init__`]. Regressed in pytest 7.0.0.

-   [#9636](https://github.com/pytest-dev/pytest/issues/9636): The [`pythonpath`] plugin was renamed to [`python_path`]. This avoids a conflict with the [`pytest-pythonpath`] plugin.

-   [#9642](https://github.com/pytest-dev/pytest/issues/9642): Fix running tests by id with [`::`] in the parametrize portion.

-   [#9643](https://github.com/pytest-dev/pytest/issues/9643): Delay issuing a [[`PytestWarning`]](reference/reference.html#pytest.PytestWarning "pytest.PytestWarning") about diamond inheritance involving [[`Item`]](reference/reference.html#pytest.Item "pytest.Item") and [[`Collector`]](reference/reference.html#pytest.Collector "pytest.Collector") so it can be filtered using [[standard warning filters]](how-to/capture-warnings.html#warnings).

## pytest 7.0.0 (2022-02-03)[¶](#pytest-7-0-0-2022-02-03 "Link to this heading")

(**Please see the full set of changes for this release also in the 7.0.0rc1 notes below**)

### Deprecations[¶](#id528 "Link to this heading")

-   [#9488](https://github.com/pytest-dev/pytest/issues/9488): If custom subclasses of nodes like [[`pytest.Item`]](reference/reference.html#pytest.Item "pytest.Item") override the [`__init__`] method, they should take [`**kwargs`]. See [[Constructors of custom Node subclasses should take \*\*kwargs]](deprecations.html#uncooperative-constructors-deprecated) for details.

    Note that a deprecation warning is only emitted when there is a conflict in the arguments pytest expected to pass. This deprecation was already part of pytest 7.0.0rc1 but wasn't documented.

### Bug Fixes[¶](#id530 "Link to this heading")

-   [#9355](https://github.com/pytest-dev/pytest/issues/9355): Fixed error message prints function decorators when using assert in Python 3.8 and above.

-   [#9396](https://github.com/pytest-dev/pytest/issues/9396): Ensure [`pytest.Config.inifile`] is available during the [[`pytest_cmdline_main`]](reference/reference.html#std-hook-pytest_cmdline_main) hook (regression during [`7.0.0rc1`]).

### Improved Documentation[¶](#id533 "Link to this heading")

-   [#9404](https://github.com/pytest-dev/pytest/issues/9404): Added extra documentation on alternatives to common misuses of [`pytest.warns(None)`] ahead of its deprecation.

-   [#9505](https://github.com/pytest-dev/pytest/issues/9505): Clarify where the configuration files are located. To avoid confusions documentation mentions that configuration file is located in the root of the repository.

### Trivial/Internal Changes[¶](#id536 "Link to this heading")

-   [#9521](https://github.com/pytest-dev/pytest/issues/9521): Add test coverage to assertion rewrite path.

## pytest 7.0.0rc1 (2021-12-06)[¶](#pytest-7-0-0rc1-2021-12-06 "Link to this heading")

### Breaking Changes[¶](#id538 "Link to this heading")

-   [#7259](https://github.com/pytest-dev/pytest/issues/7259): The [[Node.reportinfo()]](example/nonpython.html#non-python-tests) function first return value type has been expanded from [`py.path.local`]` `[`|`]` `[`str`] to [`os.PathLike[str]`]` `[`|`]` `[`str`].

    Most plugins which refer to [`reportinfo()`] only define it as part of a custom [[`pytest.Item`]](reference/reference.html#pytest.Item "pytest.Item") implementation. Since [`py.path.local`] is an [`os.PathLike[str]`], these plugins are unaffected.

    Plugins and users which call [`reportinfo()`], use the first return value and interact with it as a [`py.path.local`], would need to adjust by calling [`py.path.local(fspath)`]. Although preferably, avoid the legacy [`py.path.local`] and use [`pathlib.Path`], or use [`item.location`] or [`item.path`], instead.

    Note: pytest was not able to provide a deprecation period for this change.

-   [#8246](https://github.com/pytest-dev/pytest/issues/8246): [`--version`] now writes version information to [`stdout`] rather than [`stderr`].

-   [#8733](https://github.com/pytest-dev/pytest/issues/8733): Drop a workaround for [pyreadline](https://github.com/pyreadline/pyreadline) that made it work with [`--pdb`].

    The workaround was introduced in [#1281](https://github.com/pytest-dev/pytest/pull/1281) in 2015, however since then [pyreadline seems to have gone unmaintained](https://github.com/pyreadline/pyreadline/issues/58), is [generating warnings](https://github.com/pytest-dev/pytest/issues/8847), and will stop working on Python 3.10.

-   [#9061](https://github.com/pytest-dev/pytest/issues/9061): Using [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") in a boolean context now raises an error hinting at the proper usage.

    It is apparently common for users to mistakenly use [`pytest.approx`] like this:

    ::: 
    ::: highlight
        assert pytest.approx(actual, expected)
    :::
    :::

    While the correct usage is:

    ::: 
    ::: highlight
        assert actual == pytest.approx(expected)
    :::
    :::

    The new error message helps catch those mistakes.

-   [#9277](https://github.com/pytest-dev/pytest/issues/9277): The [`pytest.Instance`] collector type has been removed. Importing [`pytest.Instance`] or [`_pytest.python.Instance`] returns a dummy type and emits a deprecation warning. See [[The pytest.Instance collector]](deprecations.html#instance-collector-deprecation) for details.

-   [#9308](https://github.com/pytest-dev/pytest/issues/9308): **PytestRemovedIn7Warning deprecation warnings are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`PytestRemovedIn7Warning`] now generate errors instead of warning messages by default.

    **The affected features will be effectively removed in pytest 7.1**, so please consult the [[Deprecations and Removals]](deprecations.html#deprecations) section in the docs for directions on how to update existing code.

    In the pytest [`7.0.X`] series, it is possible to change the errors back into warnings as a stopgap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.PytestRemovedIn7Warning
    :::
    :::

    But this will stop working when pytest [`7.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#9308](https://github.com/pytest-dev/pytest/issues/9308).

### Deprecations[¶](#id545 "Link to this heading")

-   [#7259](https://github.com/pytest-dev/pytest/issues/7259): [`py.path.local`] arguments for hooks have been deprecated. See [[the deprecation note]](deprecations.html#legacy-path-hooks-deprecated) for full details.

    [`py.path.local`] arguments to Node constructors have been deprecated. See [[the deprecation note]](deprecations.html#node-ctor-fspath-deprecation) for full details.

    ::: 
    Note

    The name of the [[`Node`]](reference/reference.html#pytest.nodes.Node "_pytest.nodes.Node") arguments and attributes (the new attribute being [`path`]) is **the opposite** of the situation for hooks (the old argument being [`path`]).

    This is an unfortunate artifact due to historical reasons, which should be resolved in future versions as we slowly get rid of the [py](https://pypi.org/project/py) dependency (see [#9283](https://github.com/pytest-dev/pytest/issues/9283) for a longer discussion).
    :::

-   [#7469](https://github.com/pytest-dev/pytest/issues/7469): Directly constructing the following classes is now deprecated:

    -   [`_pytest.mark.structures.Mark`]

    -   [`_pytest.mark.structures.MarkDecorator`]

    -   [`_pytest.mark.structures.MarkGenerator`]

    -   [`_pytest.python.Metafunc`]

    -   [`_pytest.runner.CallInfo`]

    -   [`_pytest._code.ExceptionInfo`]

    -   [`_pytest.config.argparsing.Parser`]

    -   [`_pytest.config.argparsing.OptionGroup`]

    -   [`_pytest.pytester.HookRecorder`]

    These constructors have always been considered private, but now issue a deprecation warning, which may become a hard error in pytest 8.

-   [#8242](https://github.com/pytest-dev/pytest/issues/8242): Raising [[`unittest.SkipTest`]](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "(in Python v3.14)") to skip collection of tests during the pytest collection phase is deprecated. Use [[`pytest.skip()`]](reference/reference.html#pytest.skip "pytest.skip") instead.

    Note: This deprecation only relates to using [[`unittest.SkipTest`]](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "(in Python v3.14)") during test collection. You are probably not doing that. Ordinary usage of [[`unittest.SkipTest`]](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "(in Python v3.14)") / [[`unittest.TestCase.skipTest()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "(in Python v3.14)") / [[`unittest.skip()`]](https://docs.python.org/3/library/unittest.html#unittest.skip "(in Python v3.14)") in unittest test cases is fully supported.

    ::: 
    Note

    This deprecation has been reverted in pytest 7.1.0.
    :::

-   [#8315](https://github.com/pytest-dev/pytest/issues/8315): Several behaviors of [[`Parser.addoption`]](reference/reference.html#pytest.Parser.addoption "pytest.Parser.addoption") are now scheduled for removal in pytest 8 (deprecated since pytest 2.4.0):

    -   [`parser.addoption(...,`]` `[`help="..`]` `[`%default`]` `[`..")`] - use [`%(default)s`] instead.

    -   [`parser.addoption(...,`]` `[`type="int/string/float/complex")`] - use [`type=int`] etc. instead.

-   [#8447](https://github.com/pytest-dev/pytest/issues/8447): Defining a custom pytest node type which is both an [[`Item`]](reference/reference.html#pytest.Item "pytest.Item") and a [[`Collector`]](reference/reference.html#pytest.Collector "pytest.Collector") (e.g. [[`File`]](reference/reference.html#pytest.File "pytest.File")) now issues a warning. It was never sanely supported and triggers hard to debug errors.

    See [[the deprecation note]](deprecations.html#diamond-inheritance-deprecated) for full details.

-   [#8592](https://github.com/pytest-dev/pytest/issues/8592): [`pytest_cmdline_preparse`] has been officially deprecated. It will be removed in a future release. Use [[`pytest_load_initial_conftests`]](reference/reference.html#std-hook-pytest_load_initial_conftests) instead.

    See [[the deprecation note]](deprecations.html#cmdline-preparse-deprecated) for full details.

-   [#8645](https://github.com/pytest-dev/pytest/issues/8645): [[`pytest.warns(None)`]](reference/reference.html#pytest.warns "pytest.warns") is now deprecated because many people used it to mean "this code does not emit warnings", but it actually had the effect of checking that the code emits at least one warning of any type - like [`pytest.warns()`] or [`pytest.warns(Warning)`].

-   [#8948](https://github.com/pytest-dev/pytest/issues/8948): [[`pytest.skip(msg=...)`]](reference/reference.html#pytest.skip "pytest.skip"), [[`pytest.fail(msg=...)`]](reference/reference.html#pytest.fail "pytest.fail") and [[`pytest.exit(msg=...)`]](reference/reference.html#pytest.exit "pytest.exit") signatures now accept a [`reason`] argument instead of [`msg`]. Using [`msg`] still works, but is deprecated and will be removed in a future release.

    This was changed for consistency with [[`pytest.mark.skip`]](reference/reference.html#pytest.mark.skip "pytest.mark.skip") and [[`pytest.mark.xfail`]](reference/reference.html#pytest.mark.xfail "pytest.mark.xfail") which both accept [`reason`] as an argument.

-   [#8174](https://github.com/pytest-dev/pytest/issues/8174): The following changes have been made to types reachable through [[`pytest.ExceptionInfo.traceback`]](reference/reference.html#pytest.ExceptionInfo.traceback "pytest.ExceptionInfo.traceback"):

    -   The [`path`] property of [`_pytest.code.Code`] returns [`Path`] instead of [`py.path.local`].

    -   The [`path`] property of [`_pytest.code.TracebackEntry`] returns [`Path`] instead of [`py.path.local`].

    There was no deprecation period for this change (sorry!).

### Features[¶](#id555 "Link to this heading")

-   [#5196](https://github.com/pytest-dev/pytest/issues/5196): Tests are now ordered by definition order in more cases.

    In a class hierarchy, tests from base classes are now consistently ordered before tests defined on their subclasses (reverse MRO order).

-   [#7132](https://github.com/pytest-dev/pytest/issues/7132): Added two environment variables [][[`PYTEST_THEME`]](reference/reference.html#envvar-PYTEST_THEME) and [][[`PYTEST_THEME_MODE`]](reference/reference.html#envvar-PYTEST_THEME_MODE) to let the users customize the pygments theme used.

-   [#7259](https://github.com/pytest-dev/pytest/issues/7259): Added [[`cache.mkdir()`]](reference/reference.html#pytest.Cache.mkdir "pytest.Cache.mkdir"), which is similar to the existing [`cache.makedir()`], but returns a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") instead of a legacy [`py.path.local`].

    Added a [`paths`] type to [[`parser.addini()`]](reference/reference.html#pytest.Parser.addini "pytest.Parser.addini"), as in [`parser.addini("mypaths",`]` `[`"my`]` `[`paths",`]` `[`type="paths")`], which is similar to the existing [`pathlist`], but returns a list of [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") instead of legacy [`py.path.local`].

-   [#7469](https://github.com/pytest-dev/pytest/issues/7469): The types of objects used in pytest's API are now exported so they may be used in type annotations.

    The newly-exported types are:

    -   [`pytest.Config`] for [[`Config`]](reference/reference.html#pytest.Config "pytest.Config").

    -   [`pytest.Mark`] for [[`marks`]](reference/reference.html#pytest.Mark "pytest.Mark").

    -   [`pytest.MarkDecorator`] for [[`mark`]` `[`decorators`]](reference/reference.html#pytest.MarkDecorator "pytest.MarkDecorator").

    -   [`pytest.MarkGenerator`] for the [[`pytest.mark`]](reference/reference.html#pytest.MarkGenerator "pytest.MarkGenerator") singleton.

    -   [`pytest.Metafunc`] for the [[`metafunc`]](reference/reference.html#pytest.MarkGenerator "pytest.MarkGenerator") argument to the [[`pytest_generate_tests`]](reference/reference.html#std-hook-pytest_generate_tests) hook.

    -   [`pytest.CallInfo`] for the [[`CallInfo`]](reference/reference.html#pytest.CallInfo "pytest.CallInfo") type passed to various hooks.

    -   [`pytest.PytestPluginManager`] for [[`PytestPluginManager`]](reference/reference.html#pytest.PytestPluginManager "pytest.PytestPluginManager").

    -   [`pytest.ExceptionInfo`] for the [[`ExceptionInfo`]](reference/reference.html#pytest.ExceptionInfo "pytest.ExceptionInfo") type returned from [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") and passed to various hooks.

    -   [`pytest.Parser`] for the [[`Parser`]](reference/reference.html#pytest.Parser "pytest.Parser") type passed to the [[`pytest_addoption`]](reference/reference.html#std-hook-pytest_addoption) hook.

    -   [`pytest.OptionGroup`] for the [[`OptionGroup`]](reference/reference.html#pytest.OptionGroup "pytest.OptionGroup") type returned from the [[`parser.addgroup`]](reference/reference.html#pytest.Parser.getgroup "pytest.Parser.getgroup") method.

    -   [`pytest.HookRecorder`] for the [[`HookRecorder`]](reference/reference.html#pytest.HookRecorder "pytest.HookRecorder") type returned from [[`Pytester`]](reference/reference.html#pytest.Pytester "pytest.Pytester").

    -   [`pytest.RecordedHookCall`] for the [[`RecordedHookCall`]](reference/reference.html#pytest.HookRecorder "pytest.HookRecorder") type returned from [[`HookRecorder`]](reference/reference.html#pytest.HookRecorder "pytest.HookRecorder").

    -   [`pytest.RunResult`] for the [[`RunResult`]](reference/reference.html#pytest.RunResult "pytest.RunResult") type returned from [[`Pytester`]](reference/reference.html#pytest.Pytester "pytest.Pytester").

    -   [`pytest.LineMatcher`] for the [[`LineMatcher`]](reference/reference.html#pytest.LineMatcher "pytest.LineMatcher") type used in [[`RunResult`]](reference/reference.html#pytest.RunResult "pytest.RunResult") and others.

    -   [`pytest.TestReport`] for the [[`TestReport`]](reference/reference.html#pytest.TestReport "pytest.TestReport") type used in various hooks.

    -   [`pytest.CollectReport`] for the [[`CollectReport`]](reference/reference.html#pytest.CollectReport "pytest.CollectReport") type used in various hooks.

    Constructing most of them directly is not supported; they are only meant for use in type annotations. Doing so will emit a deprecation warning, and may become a hard-error in pytest 8.0.

    Subclassing them is also not supported. This is not currently enforced at runtime, but is detected by type-checkers such as mypy.

-   [#7856](https://github.com/pytest-dev/pytest/issues/7856): [[--import-mode=importlib]](explanation/pythonpath.html#import-modes) now works with features that depend on modules being on [[`sys.modules`]](https://docs.python.org/3/library/sys.html#sys.modules "(in Python v3.14)"), such as [[`pickle`]](https://docs.python.org/3/library/pickle.html#module-pickle "(in Python v3.14)") and [[`dataclasses`]](https://docs.python.org/3/library/dataclasses.html#module-dataclasses "(in Python v3.14)").

-   [#8144](https://github.com/pytest-dev/pytest/issues/8144): The following hooks now receive an additional [`pathlib.Path`] argument, equivalent to an existing [`py.path.local`] argument:

    -   [[`pytest_ignore_collect`]](reference/reference.html#std-hook-pytest_ignore_collect) - The [`collection_path`] parameter (equivalent to existing [`path`] parameter).

    -   [[`pytest_collect_file`]](reference/reference.html#std-hook-pytest_collect_file) - The [`file_path`] parameter (equivalent to existing [`path`] parameter).

    -   [[`pytest_pycollect_makemodule`]](reference/reference.html#std-hook-pytest_pycollect_makemodule) - The [`module_path`] parameter (equivalent to existing [`path`] parameter).

    -   [[`pytest_report_header`]](reference/reference.html#std-hook-pytest_report_header) - The [`start_path`] parameter (equivalent to existing [`startdir`] parameter).

    -   [[`pytest_report_collectionfinish`]](reference/reference.html#std-hook-pytest_report_collectionfinish) - The [`start_path`] parameter (equivalent to existing [`startdir`] parameter).

    ::: 
    Note

    The name of the [[`Node`]](reference/reference.html#pytest.nodes.Node "_pytest.nodes.Node") arguments and attributes (the new attribute being [`path`]) is **the opposite** of the situation for hooks (the old argument being [`path`]).

    This is an unfortunate artifact due to historical reasons, which should be resolved in future versions as we slowly get rid of the [py](https://pypi.org/project/py) dependency (see [#9283](https://github.com/pytest-dev/pytest/issues/9283) for a longer discussion).
    :::

-   [#8251](https://github.com/pytest-dev/pytest/issues/8251): Implement [`Node.path`] as a [`pathlib.Path`]. Both the old [`fspath`] and this new attribute gets set no matter whether [`path`] or [`fspath`] (deprecated) is passed to the constructor. It is a replacement for the [`fspath`] attribute (which represents the same path as [`py.path.local`]). While [`fspath`] is not deprecated yet due to the ongoing migration of methods like [[`reportinfo()`]](reference/reference.html#pytest.Item.reportinfo "pytest.Item.reportinfo"), we expect to deprecate it in a future release.

    ::: 
    Note

    The name of the [[`Node`]](reference/reference.html#pytest.nodes.Node "_pytest.nodes.Node") arguments and attributes (the new attribute being [`path`]) is **the opposite** of the situation for hooks (the old argument being [`path`]).

    This is an unfortunate artifact due to historical reasons, which should be resolved in future versions as we slowly get rid of the [py](https://pypi.org/project/py) dependency (see [#9283](https://github.com/pytest-dev/pytest/issues/9283) for a longer discussion).
    :::

-   [#8421](https://github.com/pytest-dev/pytest/issues/8421): [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") now works on [[`Decimal`]](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") within mappings/dicts and sequences/lists.

-   [#8606](https://github.com/pytest-dev/pytest/issues/8606): pytest invocations with [`--fixtures-per-test`] and [`--fixtures`] have been enriched with:

    -   Fixture location path printed with the fixture name.

    -   First section of the fixture's docstring printed under the fixture name.

    -   Whole of fixture's docstring printed under the fixture name using [`--verbose`] option.

-   [#8761](https://github.com/pytest-dev/pytest/issues/8761): New [[pytest.version_tuple]](reference/reference.html#version-tuple) attribute, which makes it simpler for users to do something depending on the pytest version (such as declaring hooks which are introduced in later versions).

-   [#8789](https://github.com/pytest-dev/pytest/issues/8789): Switch TOML parser from [`toml`] to [`tomli`] for TOML v1.0.0 support in [`pyproject.toml`].

-   [#8920](https://github.com/pytest-dev/pytest/issues/8920): Added [[`pytest.Stash`]](reference/reference.html#pytest.Stash "pytest.Stash"), a facility for plugins to store their data on [[`Config`]](reference/reference.html#pytest.Config "pytest.Config") and [[`Node`]](reference/reference.html#pytest.nodes.Node "_pytest.nodes.Node")s in a type-safe and conflict-free manner. See [[Storing data on items across hook functions]](how-to/writing_hook_functions.html#plugin-stash) for details.

-   [#8953](https://github.com/pytest-dev/pytest/issues/8953): [[`RunResult`]](reference/reference.html#pytest.RunResult "pytest.RunResult") method [[`assert_outcomes()`]](reference/reference.html#pytest.RunResult.assert_outcomes "pytest.RunResult.assert_outcomes") now accepts a [`warnings`] argument to assert the total number of warnings captured.

-   [#8954](https://github.com/pytest-dev/pytest/issues/8954): [`--debug`] flag now accepts a [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") file to route debug logs into, remains defaulted to [`pytestdebug.log`].

-   [#9023](https://github.com/pytest-dev/pytest/issues/9023): Full diffs are now always shown for equality assertions of iterables when [`CI`] or [`BUILD_NUMBER`] is found in the environment, even when [`-v`] isn't used.

-   [#9113](https://github.com/pytest-dev/pytest/issues/9113): [[`RunResult`]](reference/reference.html#pytest.RunResult "pytest.RunResult") method [[`assert_outcomes()`]](reference/reference.html#pytest.RunResult.assert_outcomes "pytest.RunResult.assert_outcomes") now accepts a [`deselected`] argument to assert the total number of deselected tests.

-   [#9114](https://github.com/pytest-dev/pytest/issues/9114): Added [[`pythonpath`]](reference/reference.html#confval-pythonpath) setting that adds listed paths to [[`sys.path`]](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.14)") for the duration of the test session. If you currently use the pytest-pythonpath or pytest-srcpaths plugins, you should be able to replace them with built-in [`pythonpath`] setting.

### Improvements[¶](#id573 "Link to this heading")

-   [#7480](https://github.com/pytest-dev/pytest/issues/7480): A deprecation scheduled to be removed in a major version X (e.g. pytest 7, 8, 9, ...) now uses warning category [`PytestRemovedInXWarning`], a subclass of [[`PytestDeprecationWarning`]](reference/reference.html#pytest.PytestDeprecationWarning "pytest.PytestDeprecationWarning"), instead of [[`PytestDeprecationWarning`]](reference/reference.html#pytest.PytestDeprecationWarning "pytest.PytestDeprecationWarning") directly.

    See [[Backwards Compatibility Policy]](backwards-compatibility.html#backwards-compatibility) for more details.

-   [#7864](https://github.com/pytest-dev/pytest/issues/7864): Improved error messages when parsing warning filters.

    Previously pytest would show an internal traceback, which besides being ugly sometimes would hide the cause of the problem (for example an [`ImportError`] while importing a specific warning type).

-   [#8335](https://github.com/pytest-dev/pytest/issues/8335): Improved [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") assertion messages for sequences of numbers.

    The assertion messages now dumps a table with the index and the error of each diff. Example:

    ::: 
    ::: highlight
        >       assert [1, 2, 3, 4] == pytest.approx([1, 3, 3, 5])
        E       assert comparison failed for 2 values:
        E         Index | Obtained | Expected
        E         1     | 2        | 3 +- 3.0e-06
        E         3     | 4        | 5 +- 5.0e-06
    :::
    :::

-   [#8403](https://github.com/pytest-dev/pytest/issues/8403): By default, pytest will truncate long strings in assert errors so they don't clutter the output too much, currently at [`240`] characters by default.

    However, in some cases the longer output helps, or is even crucial, to diagnose a failure. Using [`-v`] will now increase the truncation threshold to [`2400`] characters, and [`-vv`] or higher will disable truncation entirely.

-   [#8509](https://github.com/pytest-dev/pytest/issues/8509): Fixed issue where [[`unittest.TestCase.setUpClass()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "(in Python v3.14)") is not called when a test has [`/`] in its name since pytest 6.2.0.

    This refers to the path part in pytest node IDs, e.g. [`TestClass::test_it`] in the node ID [`tests/test_file.py::TestClass::test_it`].

    Now, instead of assuming that the test name does not contain [`/`], it is assumed that test path does not contain [`::`]. We plan to hopefully make both of these work in the future.

-   [#8803](https://github.com/pytest-dev/pytest/issues/8803): It is now possible to add colors to custom log levels on cli log.

    By using [`add_color_level`] from a [[`pytest_configure`]](reference/reference.html#std-hook-pytest_configure) hook, colors can be added:

    ::: 
    ::: highlight
        logging_plugin = config.pluginmanager.get_plugin('logging-plugin')
        logging_plugin.log_cli_handler.formatter.add_color_level(logging.INFO, 'cyan')
        logging_plugin.log_cli_handler.formatter.add_color_level(logging.SPAM, 'blue')
    :::
    :::

    See [[Customizing Colors]](how-to/logging.html#log-colors) for more information.

-   [#8822](https://github.com/pytest-dev/pytest/issues/8822): When showing fixture paths in [`--fixtures`] or [`--fixtures-by-test`], fixtures coming from pytest itself now display an elided path, rather than the full path to the file in the [`site-packages`] directory.

-   [#8898](https://github.com/pytest-dev/pytest/issues/8898): Complex numbers are now treated like floats and integers when generating parameterization IDs.

-   [#9062](https://github.com/pytest-dev/pytest/issues/9062): [`--stepwise-skip`] now implicitly enables [`--stepwise`] and can be used on its own.

-   [#9205](https://github.com/pytest-dev/pytest/issues/9205): [[`pytest.Cache.set()`]](reference/reference.html#pytest.Cache.set "pytest.Cache.set") now preserves key order when saving dicts.

### Bug Fixes[¶](#id584 "Link to this heading")

-   [#7124](https://github.com/pytest-dev/pytest/issues/7124): Fixed an issue where [`__main__.py`] would raise an [`ImportError`] when [`--doctest-modules`] was provided.

-   [#8061](https://github.com/pytest-dev/pytest/issues/8061): Fixed failing [`staticmethod`] test cases if they are inherited from a parent test class.

-   [#8192](https://github.com/pytest-dev/pytest/issues/8192): [`testdir.makefile`] now silently accepts values which don't start with [`.`] to maintain backward compatibility with older pytest versions.

    [`pytester.makefile`] now issues a clearer error if the [`.`] is missing in the [`ext`] argument.

-   [#8258](https://github.com/pytest-dev/pytest/issues/8258): Fixed issue where pytest's [`faulthandler`] support would not dump traceback on crashes if the [[`faulthandler`]](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "(in Python v3.14)") module was already enabled during pytest startup (using [`python`]` `[`-X`]` `[`dev`]` `[`-m`]` `[`pytest`] for example).

-   [#8317](https://github.com/pytest-dev/pytest/issues/8317): Fixed an issue where illegal directory characters derived from [`getpass.getuser()`] raised an [`OSError`].

-   [#8367](https://github.com/pytest-dev/pytest/issues/8367): Fix [`Class.from_parent`] so it forwards extra keyword arguments to the constructor.

-   [#8377](https://github.com/pytest-dev/pytest/issues/8377): The test selection options [`pytest`]` `[`-k`] and [`pytest`]` `[`-m`] now support matching names containing forward slash ([`/`]) characters.

-   [#8384](https://github.com/pytest-dev/pytest/issues/8384): The [`@pytest.mark.skip`] decorator now correctly handles its arguments. When the [`reason`] argument is accidentally given both positional and as a keyword (e.g. because it was confused with [`skipif`]), a [`TypeError`] now occurs. Before, such tests were silently skipped, and the positional argument ignored. Additionally, [`reason`] is now documented correctly as positional or keyword (rather than keyword-only).

-   [#8394](https://github.com/pytest-dev/pytest/issues/8394): Use private names for internal fixtures that handle classic setup/teardown so that they don't show up with the default [`--fixtures`] invocation (but they still show up with [`--fixtures`]` `[`-v`]).

-   [#8456](https://github.com/pytest-dev/pytest/issues/8456): The [[`required_plugins`]](reference/reference.html#confval-required_plugins) config option now works correctly when pre-releases of plugins are installed, rather than falsely claiming that those plugins aren't installed at all.

-   [#8464](https://github.com/pytest-dev/pytest/issues/8464): [`-c`]` `[`<config`]` `[`file>`] now also properly defines [`rootdir`] as the directory that contains [`<config`]` `[`file>`].

-   [#8503](https://github.com/pytest-dev/pytest/issues/8503): [[`pytest.MonkeyPatch.syspath_prepend()`]](reference/reference.html#pytest.MonkeyPatch.syspath_prepend "pytest.MonkeyPatch.syspath_prepend") no longer fails when [`setuptools`] is not installed. It now only calls [`pkg_resources.fixup_namespace_packages`] if [`pkg_resources`] was previously imported, because it is not needed otherwise.

-   [#8548](https://github.com/pytest-dev/pytest/issues/8548): Introduce fix to handle precision width in [`log-cli-format`] in turn to fix output coloring for certain formats.

-   [#8796](https://github.com/pytest-dev/pytest/issues/8796): Fixed internal error when skipping doctests.

-   [#8983](https://github.com/pytest-dev/pytest/issues/8983): The test selection options [`pytest`]` `[`-k`] and [`pytest`]` `[`-m`] now support matching names containing backslash ([`\`]) characters. Backslashes are treated literally, not as escape characters (the values being matched against are already escaped).

-   [#8990](https://github.com/pytest-dev/pytest/issues/8990): Fix [`pytest`]` `[`-vv`] crashing with an internal exception [`AttributeError:`]` `[`'str'`]` `[`object`]` `[`has`]` `[`no`]` `[`attribute`]` `[`'relative_to'`] in some cases.

-   [#9077](https://github.com/pytest-dev/pytest/issues/9077): Fixed confusing error message when [`request.fspath`] / [`request.path`] was accessed from a session-scoped fixture.

-   [#9131](https://github.com/pytest-dev/pytest/issues/9131): Fixed the URL used by [`--pastebin`] to use [bpa.st](http://bpa.st).

-   [#9163](https://github.com/pytest-dev/pytest/issues/9163): The end line number and end column offset are now properly set for rewritten assert statements.

-   [#9169](https://github.com/pytest-dev/pytest/issues/9169): Support for the [`files`] API from [`importlib.resources`] within rewritten files.

-   [#9272](https://github.com/pytest-dev/pytest/issues/9272): The nose compatibility module-level fixtures [`setup()`] and [`teardown()`] are now only called once per module, instead of for each test function. They are now called even if object-level [`setup`]/[`teardown`] is defined.

### Improved Documentation[¶](#id606 "Link to this heading")

-   [#4320](https://github.com/pytest-dev/pytest/issues/4320): Improved docs for [`pytester.copy_example`].

-   [#5105](https://github.com/pytest-dev/pytest/issues/5105): Add automatically generated [[Pytest Plugin List]](reference/plugin_list.html#plugin-list). The list is updated on a periodic schedule.

-   [#8337](https://github.com/pytest-dev/pytest/issues/8337): Recommend [numpy.testing](https://numpy.org/doc/stable/reference/routines.testing.html) module on [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") documentation.

-   [#8655](https://github.com/pytest-dev/pytest/issues/8655): Help text for [`--pdbcls`] more accurately reflects the option's behavior.

-   [#9210](https://github.com/pytest-dev/pytest/issues/9210): Remove incorrect docs about [`confcutdir`] being a configuration option: it can only be set through the [`--confcutdir`] command-line option.

-   [#9242](https://github.com/pytest-dev/pytest/issues/9242): Upgrade readthedocs configuration to use a [`newer`]` `[`Ubuntu`]` `[`version`]` `[`` <https://blog.readthedocs.com/new-build-specification/>`__ ``] with better unicode support for PDF docs.

-   [#9341](https://github.com/pytest-dev/pytest/issues/9341): Various methods commonly used for [[Working with non-python tests]](example/nonpython.html#non-python-tests) are now correctly documented in the reference docs. They were undocumented previously.

### Trivial/Internal Changes[¶](#id614 "Link to this heading")

-   [#8133](https://github.com/pytest-dev/pytest/issues/8133): Migrate to [`setuptools_scm`] 6.x to use [`SETUPTOOLS_SCM_PRETEND_VERSION_FOR_PYTEST`] for more robust release tooling.

-   [#8174](https://github.com/pytest-dev/pytest/issues/8174): The following changes have been made to internal pytest types/functions:

    -   The [`_pytest.code.getfslineno()`] function returns [`Path`] instead of [`py.path.local`].

    -   The [`_pytest.python.path_matches_patterns()`] function takes [`Path`] instead of [`py.path.local`].

    -   The [`_pytest._code.Traceback.cut()`] function accepts any [`os.PathLike[str]`], not just [`py.path.local`].

-   [#8248](https://github.com/pytest-dev/pytest/issues/8248): Internal Restructure: let [`python.PyObjMixin`] inherit from [`nodes.Node`] to carry over typing information.

-   [#8432](https://github.com/pytest-dev/pytest/issues/8432): Improve error message when [[`pytest.skip()`]](reference/reference.html#pytest.skip "pytest.skip") is used at module level without passing [`allow_module_level=True`].

-   [#8818](https://github.com/pytest-dev/pytest/issues/8818): Ensure [`regendoc`] opts out of [`TOX_ENV`] cachedir selection to ensure independent example test runs.

-   [#8913](https://github.com/pytest-dev/pytest/issues/8913): The private [`CallSpec2._arg2scopenum`] attribute has been removed after an internal refactoring.

-   [#8967](https://github.com/pytest-dev/pytest/issues/8967): [[`pytest_assertion_pass`]](reference/reference.html#std-hook-pytest_assertion_pass) is no longer considered experimental and future changes to it will be considered more carefully.

-   [#9202](https://github.com/pytest-dev/pytest/issues/9202): Add github action to upload coverage report to codecov instead of bash uploader.

-   [#9225](https://github.com/pytest-dev/pytest/issues/9225): Changed the command used to create sdist and wheel artifacts: using the build package instead of setup.py.

-   [#9351](https://github.com/pytest-dev/pytest/issues/9351): Correct minor typos in doc/en/example/special.rst.

## pytest 6.2.5 (2021-08-29)[¶](#pytest-6-2-5-2021-08-29 "Link to this heading")

### Trivial/Internal Changes[¶](#id625 "Link to this heading")

-   [#8494](https://github.com/pytest-dev/pytest/issues/8494): Python 3.10 is now supported.

-   [#9040](https://github.com/pytest-dev/pytest/issues/9040): Enable compatibility with [`pluggy`]` `[`1.0`] or later.

## pytest 6.2.4 (2021-05-04)[¶](#pytest-6-2-4-2021-05-04 "Link to this heading")

### Bug Fixes[¶](#id626 "Link to this heading")

-   [#8539](https://github.com/pytest-dev/pytest/issues/8539): Fixed assertion rewriting on Python 3.10.

## pytest 6.2.3 (2021-04-03)[¶](#pytest-6-2-3-2021-04-03 "Link to this heading")

### Bug Fixes[¶](#id627 "Link to this heading")

-   [#8414](https://github.com/pytest-dev/pytest/issues/8414): pytest used to create directories under [`/tmp`] with world-readable permissions. This means that any user in the system was able to read information written by tests in temporary directories (such as those created by the [`tmp_path`]/[`tmpdir`] fixture). Now the directories are created with private permissions.

    pytest used to silently use a preexisting [`/tmp/pytest-of-<username>`] directory, even if owned by another user. This means another user could pre-create such a directory and gain control of another user's temporary directory. Now such a condition results in an error.

## pytest 6.2.2 (2021-01-25)[¶](#pytest-6-2-2-2021-01-25 "Link to this heading")

### Bug Fixes[¶](#id628 "Link to this heading")

-   [#8152](https://github.com/pytest-dev/pytest/issues/8152): Fixed "(\<Skipped instance\>)" being shown as a skip reason in the verbose test summary line when the reason is empty.

-   [#8249](https://github.com/pytest-dev/pytest/issues/8249): Fix the [`faulthandler`] plugin for occasions when running with [`twisted.logger`] and using [`pytest`]` `[`--capture=no`].

## pytest 6.2.1 (2020-12-15)[¶](#pytest-6-2-1-2020-12-15 "Link to this heading")

### Bug Fixes[¶](#id629 "Link to this heading")

-   [#7678](https://github.com/pytest-dev/pytest/issues/7678): Fixed bug where [`ImportPathMismatchError`] would be raised for files compiled in the host and loaded later from an UNC mounted path (Windows).

-   [#8132](https://github.com/pytest-dev/pytest/issues/8132): Fixed regression in [`approx`]: in 6.2.0 [`approx`] no longer raises [`TypeError`] when dealing with non-numeric types, falling back to normal comparison. Before 6.2.0, array types like tf.DeviceArray fell through to the scalar case, and happened to compare correctly to a scalar if they had only one element. After 6.2.0, these types began failing, because they inherited neither from standard Python number hierarchy nor from [`numpy.ndarray`].

    [`approx`] now converts arguments to [`numpy.ndarray`] if they expose the array protocol and are not scalars. This treats array-like objects like numpy arrays, regardless of size.

## pytest 6.2.0 (2020-12-12)[¶](#pytest-6-2-0-2020-12-12 "Link to this heading")

### Breaking Changes[¶](#id630 "Link to this heading")

-   [#7808](https://github.com/pytest-dev/pytest/issues/7808): pytest now supports python3.6+ only.

### Deprecations[¶](#id631 "Link to this heading")

-   [#7469](https://github.com/pytest-dev/pytest/issues/7469): Directly constructing/calling the following classes/functions is now deprecated:

    -   [`_pytest.cacheprovider.Cache`]

    -   [`_pytest.cacheprovider.Cache.for_config()`]

    -   [`_pytest.cacheprovider.Cache.clear_cache()`]

    -   [`_pytest.cacheprovider.Cache.cache_dir_from_config()`]

    -   [`_pytest.capture.CaptureFixture`]

    -   [`_pytest.fixtures.FixtureRequest`]

    -   [`_pytest.fixtures.SubRequest`]

    -   [`_pytest.logging.LogCaptureFixture`]

    -   [`_pytest.pytester.Pytester`]

    -   [`_pytest.pytester.Testdir`]

    -   [`_pytest.recwarn.WarningsRecorder`]

    -   [`_pytest.recwarn.WarningsChecker`]

    -   [`_pytest.tmpdir.TempPathFactory`]

    -   [`_pytest.tmpdir.TempdirFactory`]

    These have always been considered private, but now issue a deprecation warning, which may become a hard error in pytest 8.0.0.

-   [#7530](https://github.com/pytest-dev/pytest/issues/7530): The [`--strict`] command-line option has been deprecated, use [`--strict-markers`] instead.

    We have plans to maybe in the future to reintroduce [`--strict`] and make it an encompassing flag for all strictness related options ([`--strict-markers`] and [`--strict-config`] at the moment, more might be introduced in the future).

-   [#7988](https://github.com/pytest-dev/pytest/issues/7988): The [`@pytest.yield_fixture`] decorator/function is now deprecated. Use [[`pytest.fixture()`]](reference/reference.html#pytest.fixture "pytest.fixture") instead.

    [`yield_fixture`] has been an alias for [`fixture`] for a very long time, so can be search/replaced safely.

### Features[¶](#id632 "Link to this heading")

-   [#5299](https://github.com/pytest-dev/pytest/issues/5299): pytest now warns about unraisable exceptions and unhandled thread exceptions that occur in tests on Python\>=3.8. See [[Warning about unraisable exceptions and unhandled thread exceptions]](how-to/failures.html#unraisable) for more information.

-   [#7425](https://github.com/pytest-dev/pytest/issues/7425): New [[`pytester`]](reference/reference.html#std-fixture-pytester) fixture, which is identical to [[`testdir`]](reference/reference.html#std-fixture-testdir) but its methods return [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") when appropriate instead of [`py.path.local`].

    This is part of the movement to use [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") objects internally, in order to remove the dependency to [`py`] in the future.

    Internally, the old [`pytest.Testdir`] is now a thin wrapper around [[`Pytester`]](reference/reference.html#pytest.Pytester "pytest.Pytester"), preserving the old interface.

-   [#7695](https://github.com/pytest-dev/pytest/issues/7695): A new hook was added, [`pytest_markeval_namespace`] which should return a dictionary. This dictionary will be used to augment the "global" variables available to evaluate skipif/xfail/xpass markers.

    Pseudo example

    [`conftest.py`]:

    ::: 
    ::: highlight
        def pytest_markeval_namespace():
            return 
    :::
    :::

    [`test_func.py`]:

    ::: 
    ::: highlight
        @pytest.mark.skipif("color == 'blue'", reason="Color is not red")
        def test_func():
            assert False
    :::
    :::

-   [#8006](https://github.com/pytest-dev/pytest/issues/8006): It is now possible to construct a [[`MonkeyPatch`]](reference/reference.html#pytest.MonkeyPatch "pytest.MonkeyPatch") object directly as [`pytest.MonkeyPatch()`], in cases when the [[`monkeypatch`]](reference/reference.html#std-fixture-monkeypatch) fixture cannot be used. Previously some users imported it from the private [`_pytest.monkeypatch.MonkeyPatch`] namespace.

    Additionally, [[`MonkeyPatch.context`]](reference/reference.html#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context") is now a classmethod, and can be used as [`with`]` `[`MonkeyPatch.context()`]` `[`as`]` `[`mp:`]` `[`...`]. This is the recommended way to use [`MonkeyPatch`] directly, since unlike the [`monkeypatch`] fixture, an instance created directly is not [`undo()`]-ed automatically.

### Improvements[¶](#id633 "Link to this heading")

-   [#1265](https://github.com/pytest-dev/pytest/issues/1265): Added an [`__str__`] implementation to the [[`LineMatcher`]](reference/reference.html#pytest.LineMatcher "pytest.LineMatcher") class which is returned from [`pytester.run_pytest().stdout`] and similar. It returns the entire output, like the existing [`str()`] method.

-   [#2044](https://github.com/pytest-dev/pytest/issues/2044): Verbose mode now shows the reason that a test was skipped in the test's terminal line after the "SKIPPED", "XFAIL" or "XPASS".

-   [#7469](https://github.com/pytest-dev/pytest/issues/7469) The types of builtin pytest fixtures are now exported so they may be used in type annotations of test functions. The newly-exported types are:

    -   [`pytest.FixtureRequest`] for the [[`request`]](reference/reference.html#std-fixture-request) fixture.

    -   [`pytest.Cache`] for the [[`cache`]](reference/reference.html#std-fixture-cache) fixture.

    -   [`pytest.CaptureFixture[str]`] for the [[`capfd`]](reference/reference.html#std-fixture-capfd) and [[`capsys`]](reference/reference.html#std-fixture-capsys) fixtures.

    -   [`pytest.CaptureFixture[bytes]`] for the [[`capfdbinary`]](reference/reference.html#std-fixture-capfdbinary) and [[`capsysbinary`]](reference/reference.html#std-fixture-capsysbinary) fixtures.

    -   [`pytest.LogCaptureFixture`] for the [[`caplog`]](reference/reference.html#std-fixture-caplog) fixture.

    -   [`pytest.Pytester`] for the [[`pytester`]](reference/reference.html#std-fixture-pytester) fixture.

    -   [`pytest.Testdir`] for the [[`testdir`]](reference/reference.html#std-fixture-testdir) fixture.

    -   [`pytest.TempdirFactory`] for the [[`tmpdir_factory`]](reference/reference.html#std-fixture-tmpdir_factory) fixture.

    -   [`pytest.TempPathFactory`] for the [[`tmp_path_factory`]](reference/reference.html#std-fixture-tmp_path_factory) fixture.

    -   [`pytest.MonkeyPatch`] for the [[`monkeypatch`]](reference/reference.html#std-fixture-monkeypatch) fixture.

    -   [`pytest.WarningsRecorder`] for the [[`recwarn`]](reference/reference.html#std-fixture-recwarn) fixture.

    Constructing them is not supported (except for [`MonkeyPatch`]); they are only meant for use in type annotations. Doing so will emit a deprecation warning, and may become a hard-error in pytest 8.0.

    Subclassing them is also not supported. This is not currently enforced at runtime, but is detected by type-checkers such as mypy.

-   [#7527](https://github.com/pytest-dev/pytest/issues/7527): When a comparison between [[`namedtuple`]](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.14)") instances of the same type fails, pytest now shows the differing field names (possibly nested) instead of their indexes.

-   [#7615](https://github.com/pytest-dev/pytest/issues/7615): [[`Node.warn`]](reference/reference.html#pytest.nodes.Node.warn "_pytest.nodes.Node.warn") now permits any subclass of [[`Warning`]](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)"), not just [[`PytestWarning`]](reference/reference.html#pytest.PytestWarning "pytest.PytestWarning").

-   [#7701](https://github.com/pytest-dev/pytest/issues/7701): Improved reporting when using [`--collected-only`]. It will now show the number of collected tests in the summary stats.

-   [#7710](https://github.com/pytest-dev/pytest/issues/7710): Use strict equality comparison for non-numeric types in [[`pytest.approx()`]](reference/reference.html#pytest.approx "pytest.approx") instead of raising [[`TypeError`]](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)").

    This was the undocumented behavior before 3.7, but is now officially a supported feature.

-   [#7938](https://github.com/pytest-dev/pytest/issues/7938): New [`--sw-skip`] argument which is a shorthand for [`--stepwise-skip`].

-   [#8023](https://github.com/pytest-dev/pytest/issues/8023): Added [`'node_modules'`] to default value for [[`norecursedirs`]](reference/reference.html#confval-norecursedirs).

-   [#8032](https://github.com/pytest-dev/pytest/issues/8032): [[`doClassCleanups`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doClassCleanups "(in Python v3.14)") (introduced in [[`unittest`]](https://docs.python.org/3/library/unittest.html#module-unittest "(in Python v3.14)") in Python and 3.8) is now called appropriately.

### Bug Fixes[¶](#id634 "Link to this heading")

-   [#4824](https://github.com/pytest-dev/pytest/issues/4824): Fixed quadratic behavior and improved performance of collection of items using autouse fixtures and xunit fixtures.

-   [#7758](https://github.com/pytest-dev/pytest/issues/7758): Fixed an issue where some files in packages are getting lost from [`--lf`] even though they contain tests that failed. Regressed in pytest 5.4.0.

-   [#7911](https://github.com/pytest-dev/pytest/issues/7911): Directories created by by [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) and [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir) are now considered stale after 3 days without modification (previous value was 3 hours) to avoid deleting directories still in use in long running test suites.

-   [#7913](https://github.com/pytest-dev/pytest/issues/7913): Fixed a crash or hang in [[`pytester.spawn`]](reference/reference.html#pytest.Pytester.spawn "pytest.Pytester.spawn") when the [[`readline`]](https://docs.python.org/3/library/readline.html#module-readline "(in Python v3.14)") module is involved.

-   [#7951](https://github.com/pytest-dev/pytest/issues/7951): Fixed handling of recursive symlinks when collecting tests.

-   [#7981](https://github.com/pytest-dev/pytest/issues/7981): Fixed symlinked directories not being followed during collection. Regressed in pytest 6.1.0.

-   [#8016](https://github.com/pytest-dev/pytest/issues/8016): Fixed only one doctest being collected when using [`pytest`]` `[`--doctest-modules`]` `[`path/to/an/__init__.py`].

### Improved Documentation[¶](#id635 "Link to this heading")

-   [#7429](https://github.com/pytest-dev/pytest/issues/7429): Add more information and use cases about skipping doctests.

-   [#7780](https://github.com/pytest-dev/pytest/issues/7780): Classes which should not be inherited from are now marked [`final`]` `[`class`] in the API reference.

-   [#7872](https://github.com/pytest-dev/pytest/issues/7872): [`_pytest.config.argparsing.Parser.addini()`] accepts explicit [`None`] and [`"string"`].

-   [#7878](https://github.com/pytest-dev/pytest/issues/7878): In pull request section, ask to commit after editing changelog and authors file.

### Trivial/Internal Changes[¶](#id636 "Link to this heading")

-   [#7802](https://github.com/pytest-dev/pytest/issues/7802): The [`attrs`] dependency requirement is now \>=19.2.0 instead of \>=17.4.0.

-   [#8014](https://github.com/pytest-dev/pytest/issues/8014): [`.pyc`] files created by pytest's assertion rewriting now conform to the newer [][**PEP 552**](https://peps.python.org/pep-0552/) format on Python\>=3.7. (These files are internal and only interpreted by pytest itself.)

## pytest 6.1.2 (2020-10-28)[¶](#pytest-6-1-2-2020-10-28 "Link to this heading")

### Bug Fixes[¶](#id637 "Link to this heading")

-   [#7758](https://github.com/pytest-dev/pytest/issues/7758): Fixed an issue where some files in packages are getting lost from [`--lf`] even though they contain tests that failed. Regressed in pytest 5.4.0.

-   [#7911](https://github.com/pytest-dev/pytest/issues/7911): Directories created by [`tmpdir`] are now considered stale after 3 days without modification (previous value was 3 hours) to avoid deleting directories still in use in long running test suites.

### Improved Documentation[¶](#id638 "Link to this heading")

-   [#7815](https://github.com/pytest-dev/pytest/issues/7815): Improve deprecation warning message for [`pytest._fillfuncargs()`].

## pytest 6.1.1 (2020-10-03)[¶](#pytest-6-1-1-2020-10-03 "Link to this heading")

### Bug Fixes[¶](#id639 "Link to this heading")

-   [#7807](https://github.com/pytest-dev/pytest/issues/7807): Fixed regression in pytest 6.1.0 causing incorrect rootdir to be determined in some non-trivial cases where parent directories have config files as well.

-   [#7814](https://github.com/pytest-dev/pytest/issues/7814): Fixed crash in header reporting when [[`testpaths`]](reference/reference.html#confval-testpaths) is used and contains absolute paths (regression in 6.1.0).

## pytest 6.1.0 (2020-09-26)[¶](#pytest-6-1-0-2020-09-26 "Link to this heading")

### Breaking Changes[¶](#id640 "Link to this heading")

-   [#5585](https://github.com/pytest-dev/pytest/issues/5585): As per our policy, the following features which have been deprecated in the 5.X series are now removed:

    -   The [`funcargnames`] read-only property of [`FixtureRequest`], [`Metafunc`], and [`Function`] classes. Use [`fixturenames`] attribute.

    -   [`@pytest.fixture`] no longer supports positional arguments, pass all arguments by keyword instead.

    -   Direct construction of [`Node`] subclasses now raise an error, use [`from_parent`] instead.

    -   The default value for [`junit_family`] has changed to [`xunit2`]. If you require the old format, add [`junit_family=xunit1`] to your configuration file.

    -   The [`TerminalReporter`] no longer has a [`writer`] attribute. Plugin authors may use the public functions of the [`TerminalReporter`] instead of accessing the [`TerminalWriter`] object directly.

    -   The [`--result-log`] option has been removed. Users are recommended to use the [pytest-reportlog](https://github.com/pytest-dev/pytest-reportlog) plugin instead.

    For more information consult [[Deprecations and Removals]](deprecations.html) in the docs.

### Deprecations[¶](#id641 "Link to this heading")

-   [#6981](https://github.com/pytest-dev/pytest/issues/6981): The [`pytest.collect`] module is deprecated: all its names can be imported from [`pytest`] directly.

-   [#7097](https://github.com/pytest-dev/pytest/issues/7097): The [`pytest._fillfuncargs`] function is deprecated. This function was kept for backward compatibility with an older plugin.

    It's functionality is not meant to be used directly, but if you must replace it, use [`function._request._fillfixtures()`] instead, though note this is not a public API and may break in the future.

-   [#7210](https://github.com/pytest-dev/pytest/issues/7210): The special [`-k`]` `[`'-expr'`] syntax to [`-k`] is deprecated. Use [`-k`]` `[`'not`]` `[`expr'`] instead.

    The special [`-k`]` `[`'expr:'`] syntax to [`-k`] is deprecated. Please open an issue if you use this and want a replacement.

-   [#7255](https://github.com/pytest-dev/pytest/issues/7255): The [`pytest_warning_captured`] hook is deprecated in favor of [[`pytest_warning_recorded`]](reference/reference.html#std-hook-pytest_warning_recorded), and will be removed in a future version.

-   [#7648](https://github.com/pytest-dev/pytest/issues/7648): The [`gethookproxy()`] and [`isinitpath()`] methods of [`FSCollector`] and [`Package`] are deprecated; use [`self.session.gethookproxy()`] and [`self.session.isinitpath()`] instead. This should work on all pytest versions.

### Features[¶](#id642 "Link to this heading")

-   [#7667](https://github.com/pytest-dev/pytest/issues/7667): New [`--durations-min`] command-line flag controls the minimal duration for inclusion in the slowest list of tests shown by [`--durations`]. Previously this was hard-coded to [`0.005s`].

### Improvements[¶](#id643 "Link to this heading")

-   [#6681](https://github.com/pytest-dev/pytest/issues/6681): Internal pytest warnings issued during the early stages of initialization are now properly handled and can filtered through [[`filterwarnings`]](reference/reference.html#confval-filterwarnings) or [`--pythonwarnings/-W`].

    This also fixes a number of long standing issues: [#2891](https://github.com/pytest-dev/pytest/issues/2891), [#7620](https://github.com/pytest-dev/pytest/issues/7620), [#7426](https://github.com/pytest-dev/pytest/issues/7426).

-   [#7572](https://github.com/pytest-dev/pytest/issues/7572): When a plugin listed in [`required_plugins`] is missing or an unknown config key is used with [`--strict-config`], a simple error message is now shown instead of a stacktrace.

-   [#7685](https://github.com/pytest-dev/pytest/issues/7685): Added two new attributes [[`rootpath`]](reference/reference.html#pytest.Config.rootpath "pytest.Config.rootpath") and [[`inipath`]](reference/reference.html#pytest.Config.inipath "pytest.Config.inipath") to [[`Config`]](reference/reference.html#pytest.Config "pytest.Config"). These attributes are [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") versions of the existing [`rootdir`] and [`inifile`] attributes, and should be preferred over them when possible.

-   [#7780](https://github.com/pytest-dev/pytest/issues/7780): Public classes which are not designed to be inherited from are now marked [[`@final`]](https://docs.python.org/3/library/typing.html#typing.final "(in Python v3.14)"). Code which inherits from these classes will trigger a type-checking (e.g. mypy) error, but will still work in runtime. Currently the [`final`] designation does not appear in the API Reference but hopefully will in the future.

### Bug Fixes[¶](#id644 "Link to this heading")

-   [#1953](https://github.com/pytest-dev/pytest/issues/1953): Fixed error when overwriting a parametrized fixture, while also reusing the super fixture value.

    ::: 
    ::: highlight
        # conftest.py
        import pytest

        @pytest.fixture(params=[1, 2])
        def foo(request):
            return request.param

        # test_foo.py
        import pytest

        @pytest.fixture
        def foo(foo):
            return foo * 2
    :::
    :::

-   [#4984](https://github.com/pytest-dev/pytest/issues/4984): Fixed an internal error crash with [`IndexError:`]` `[`list`]` `[`index`]` `[`out`]` `[`of`]` `[`range`] when collecting a module which starts with a decorated function, the decorator raises, and assertion rewriting is enabled.

-   [#7591](https://github.com/pytest-dev/pytest/issues/7591): pylint shouldn't complain anymore about unimplemented abstract methods when inheriting from [[File]](example/nonpython.html#non-python-tests).

-   [#7628](https://github.com/pytest-dev/pytest/issues/7628): Fixed test collection when a full path without a drive letter was passed to pytest on Windows (for example [`\projects\tests\test.py`] instead of [`c:\projects\tests\pytest.py`]).

-   [#7638](https://github.com/pytest-dev/pytest/issues/7638): Fix handling of command-line options that appear as paths but trigger an OS-level syntax error on Windows, such as the options used internally by [`pytest-xdist`].

-   [#7742](https://github.com/pytest-dev/pytest/issues/7742): Fixed INTERNALERROR when accessing locals / globals with faulty [`exec`].

### Improved Documentation[¶](#id645 "Link to this heading")

-   [#1477](https://github.com/pytest-dev/pytest/issues/1477): Removed faq.rst and its reference in contents.rst.

### Trivial/Internal Changes[¶](#id646 "Link to this heading")

-   [#7536](https://github.com/pytest-dev/pytest/issues/7536): The internal [`junitxml`] plugin has rewritten to use [`xml.etree.ElementTree`]. The order of attributes in XML elements might differ. Some unneeded escaping is no longer performed.

-   [#7587](https://github.com/pytest-dev/pytest/issues/7587): The dependency on the [`more-itertools`] package has been removed.

-   [#7631](https://github.com/pytest-dev/pytest/issues/7631): The result type of [[`capfd.readouterr()`]](reference/reference.html#pytest.CaptureFixture.readouterr "pytest.CaptureFixture.readouterr") (and similar) is no longer a namedtuple, but should behave like one in all respects. This was done for technical reasons.

-   [#7671](https://github.com/pytest-dev/pytest/issues/7671): When collecting tests, pytest finds test classes and functions by examining the attributes of python objects (modules, classes and instances). To speed up this process, pytest now ignores builtin attributes (like [`__class__`], [`__delattr__`] and [`__new__`]) without consulting the [[`python_classes`]](reference/reference.html#confval-python_classes) and [[`python_functions`]](reference/reference.html#confval-python_functions) configuration options and without passing them to plugins using the [[`pytest_pycollect_makeitem`]](reference/reference.html#std-hook-pytest_pycollect_makeitem) hook.

## pytest 6.0.2 (2020-09-04)[¶](#pytest-6-0-2-2020-09-04 "Link to this heading")

### Bug Fixes[¶](#id647 "Link to this heading")

-   [#7148](https://github.com/pytest-dev/pytest/issues/7148): Fixed [`--log-cli`] potentially causing unrelated [`print`] output to be swallowed.

-   [#7672](https://github.com/pytest-dev/pytest/issues/7672): Fixed log-capturing level restored incorrectly if [`caplog.set_level`] is called more than once.

-   [#7686](https://github.com/pytest-dev/pytest/issues/7686): Fixed [`NotSetType.token`] being used as the parameter ID when the parametrization list is empty. Regressed in pytest 6.0.0.

-   [#7707](https://github.com/pytest-dev/pytest/issues/7707): Fix internal error when handling some exceptions that contain multiple lines or the style uses multiple lines ([`--tb=line`] for example).

## pytest 6.0.1 (2020-07-30)[¶](#pytest-6-0-1-2020-07-30 "Link to this heading")

### Bug Fixes[¶](#id648 "Link to this heading")

-   [#7394](https://github.com/pytest-dev/pytest/issues/7394): Passing an empty [`help`] value to [`Parser.add_option`] is now accepted instead of crashing when running [`pytest`]` `[`--help`]. Passing [`None`] raises a more informative [`TypeError`].

-   [#7558](https://github.com/pytest-dev/pytest/issues/7558): Fix pylint [`not-callable`] lint on [`pytest.mark.parametrize()`] and the other builtin marks: [`skip`], [`skipif`], [`xfail`], [`usefixtures`], [`filterwarnings`].

-   [#7559](https://github.com/pytest-dev/pytest/issues/7559): Fix regression in plugins using [`TestReport.longreprtext`] (such as [`pytest-html`]) when [`TestReport.longrepr`] is not a string.

-   [#7569](https://github.com/pytest-dev/pytest/issues/7569): Fix logging capture handler's level not reset on teardown after a call to [`caplog.set_level()`].

## pytest 6.0.0 (2020-07-28)[¶](#pytest-6-0-0-2020-07-28 "Link to this heading")

(**Please see the full set of changes for this release also in the 6.0.0rc1 notes below**)

### Breaking Changes[¶](#id649 "Link to this heading")

-   [#5584](https://github.com/pytest-dev/pytest/issues/5584): **PytestDeprecationWarning are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`PytestDeprecationWarning`] now generate errors instead of warning messages.

    **The affected features will be effectively removed in pytest 6.1**, so please consult the [[Deprecations and Removals]](deprecations.html) section in the docs for directions on how to update existing code.

    In the pytest [`6.0.X`] series, it is possible to change the errors back into warnings as a stopgap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.PytestDeprecationWarning
    :::
    :::

    But this will stop working when pytest [`6.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#5584](https://github.com/pytest-dev/pytest/issues/5584).

-   [#7472](https://github.com/pytest-dev/pytest/issues/7472): The [`exec_()`] and [`is_true()`] methods of [`_pytest._code.Frame`] have been removed.

### Features[¶](#id650 "Link to this heading")

-   [#7464](https://github.com/pytest-dev/pytest/issues/7464): Added support for [][[`NO_COLOR`]](reference/reference.html#envvar-NO_COLOR) and [][[`FORCE_COLOR`]](reference/reference.html#envvar-FORCE_COLOR) environment variables to control colored output.

### Improvements[¶](#id651 "Link to this heading")

-   [#7467](https://github.com/pytest-dev/pytest/issues/7467): [`--log-file`] CLI option and [`log_file`] ini marker now create subdirectories if needed.

-   [#7489](https://github.com/pytest-dev/pytest/issues/7489): The [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") function has a clearer error message when [`match`] equals the obtained string but is not a regex match. In this case it is suggested to escape the regex.

### Bug Fixes[¶](#id652 "Link to this heading")

-   [#7392](https://github.com/pytest-dev/pytest/issues/7392): Fix the reported location of tests skipped with [`@pytest.mark.skip`] when [`--runxfail`] is used.

-   [#7491](https://github.com/pytest-dev/pytest/issues/7491): [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir) and [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) no longer raise an error if the lock to check for stale temporary directories is not accessible.

-   [#7517](https://github.com/pytest-dev/pytest/issues/7517): Preserve line endings when captured via [`capfd`].

-   [#7534](https://github.com/pytest-dev/pytest/issues/7534): Restored the previous formatting of [`TracebackEntry.__str__`] which was changed by accident.

### Improved Documentation[¶](#id653 "Link to this heading")

-   [#7422](https://github.com/pytest-dev/pytest/issues/7422): Clarified when the [`usefixtures`] mark can apply fixtures to test.

-   [#7441](https://github.com/pytest-dev/pytest/issues/7441): Add a note about [`-q`] option used in getting started guide.

### Trivial/Internal Changes[¶](#id654 "Link to this heading")

-   [#7389](https://github.com/pytest-dev/pytest/issues/7389): Fixture scope [`package`] is no longer considered experimental.

## pytest 6.0.0rc1 (2020-07-08)[¶](#pytest-6-0-0rc1-2020-07-08 "Link to this heading")

### Breaking Changes[¶](#id655 "Link to this heading")

-   [#1316](https://github.com/pytest-dev/pytest/issues/1316): [`TestReport.longrepr`] is now always an instance of [`ReprExceptionInfo`]. Previously it was a [`str`] when a test failed with [`pytest.fail(...,`]` `[`pytrace=False)`].

-   [#5965](https://github.com/pytest-dev/pytest/issues/5965): symlinks are no longer resolved during collection and matching [`conftest.py`] files with test file paths.

    Resolving symlinks for the current directory and during collection was introduced as a bugfix in 3.9.0, but it actually is a new feature which had unfortunate consequences in Windows and surprising results in other platforms.

    The team decided to step back on resolving symlinks at all, planning to review this in the future with a more solid solution (see discussion in [#6523](https://github.com/pytest-dev/pytest/pull/6523) for details).

    This might break test suites which made use of this feature; the fix is to create a symlink for the entire test tree, and not only to partial files/tress as it was possible previously.

-   [#6505](https://github.com/pytest-dev/pytest/issues/6505): [`Testdir.run().parseoutcomes()`] now always returns the parsed nouns in plural form.

    Originally [`parseoutcomes()`] would always returns the nouns in plural form, but a change meant to improve the terminal summary by using singular form single items ([`1`]` `[`warning`] or [`1`]` `[`error`]) caused an unintended regression by changing the keys returned by [`parseoutcomes()`].

    Now the API guarantees to always return the plural form, so calls like this:

    ::: 
    ::: highlight
        result = testdir.runpytest()
        result.assert_outcomes(error=1)
    :::
    :::

    Need to be changed to:

    ::: 
    ::: highlight
        result = testdir.runpytest()
        result.assert_outcomes(errors=1)
    :::
    :::

-   [#6903](https://github.com/pytest-dev/pytest/issues/6903): The [`os.dup()`] function is now assumed to exist. We are not aware of any supported Python 3 implementations which do not provide it.

-   [#7040](https://github.com/pytest-dev/pytest/issues/7040): [`-k`] no longer matches against the names of the directories outside the test session root.

    Also, [`pytest.Package.name`] is now just the name of the directory containing the package's [`__init__.py`] file, instead of the full path. This is consistent with how the other nodes are named, and also one of the reasons why [`-k`] would match against any directory containing the test suite.

-   [#7122](https://github.com/pytest-dev/pytest/issues/7122): Expressions given to the [`-m`] and [`-k`] options are no longer evaluated using Python's [[`eval()`]](https://docs.python.org/3/library/functions.html#eval "(in Python v3.14)"). The format supports [`or`], [`and`], [`not`], parenthesis and general identifiers to match against. Python constants, keywords or other operators are no longer evaluated differently.

-   [#7135](https://github.com/pytest-dev/pytest/issues/7135): Pytest now uses its own [`TerminalWriter`] class instead of using the one from the [`py`] library. Plugins generally access this class through [`TerminalReporter.writer`], [`TerminalReporter.write()`] (and similar methods), or [`_pytest.config.create_terminal_writer()`].

    The following breaking changes were made:

    -   Output ([`write()`] method and others) no longer flush implicitly; the flushing behavior of the underlying file is respected. To flush explicitly (for example, if you want output to be shown before an end-of-line is printed), use [`write(flush=True)`] or [`terminal_writer.flush()`].

    -   Explicit Windows console support was removed, delegated to the colorama library.

    -   Support for writing [`bytes`] was removed.

    -   The [`reline`] method and [`chars_on_current_line`] property were removed.

    -   The [`stringio`] and [`encoding`] arguments was removed.

    -   Support for passing a callable instead of a file was removed.

-   [#7224](https://github.com/pytest-dev/pytest/issues/7224): The [`item.catch_log_handler`] and [`item.catch_log_handlers`] attributes, set by the logging plugin and never meant to be public, are no longer available.

    The deprecated [`--no-print-logs`] option and [`log_print`] ini option are removed. Use [`--show-capture`] instead.

-   [#7226](https://github.com/pytest-dev/pytest/issues/7226): Removed the unused [`args`] parameter from [`pytest.Function.__init__`].

-   [#7418](https://github.com/pytest-dev/pytest/issues/7418): Removed the [`pytest_doctest_prepare_content`] hook specification. This hook hasn't been triggered by pytest for at least 10 years.

-   [#7438](https://github.com/pytest-dev/pytest/issues/7438): Some changes were made to the internal [`_pytest._code.source`], listed here for the benefit of plugin authors who may be using it:

    -   The [`deindent`] argument to [`Source()`] has been removed, now it is always true.

    -   Support for zero or multiple arguments to [`Source()`] has been removed.

    -   Support for comparing [`Source`] with an [`str`] has been removed.

    -   The methods [`Source.isparseable()`] and [`Source.putaround()`] have been removed.

    -   The method [`Source.compile()`] and function [`_pytest._code.compile()`] have been removed; use plain [`compile()`] instead.

    -   The function [`_pytest._code.source.getsource()`] has been removed; use [`Source()`] directly instead.

### Deprecations[¶](#id656 "Link to this heading")

-   [#7210](https://github.com/pytest-dev/pytest/issues/7210): The special [`-k`]` `[`'-expr'`] syntax to [`-k`] is deprecated. Use [`-k`]` `[`'not`]` `[`expr'`] instead.

    The special [`-k`]` `[`'expr:'`] syntax to [`-k`] is deprecated. Please open an issue if you use this and want a replacement.

-   [#4049](https://github.com/pytest-dev/pytest/issues/4049): [`pytest_warning_captured`] is deprecated in favor of the [`pytest_warning_recorded`] hook.

### Features[¶](#id657 "Link to this heading")

-   [#1556](https://github.com/pytest-dev/pytest/issues/1556): pytest now supports [`pyproject.toml`] files for configuration.

    The configuration options is similar to the one available in other formats, but must be defined in a [`[tool.pytest.ini_options]`] table to be picked up by pytest:

    ::: 
    ::: highlight
        # pyproject.toml
        [tool.pytest.ini_options]
        minversion = "6.0"
        addopts = "-ra -q"
        testpaths = [
            "tests",
            "integration",
        ]
    :::
    :::

    More information can be found [[in the docs]](reference/customize.html#config-file-formats).

-   [#3342](https://github.com/pytest-dev/pytest/issues/3342): pytest now includes inline type annotations and exposes them to user programs. Most of the user-facing API is covered, as well as internal code.

    If you are running a type checker such as mypy on your tests, you may start noticing type errors indicating incorrect usage. If you run into an error that you believe to be incorrect, please let us know in an issue.

    The types were developed against mypy version 0.780. Versions before 0.750 are known not to work. We recommend using the latest version. Other type checkers may work as well, but they are not officially verified to work by pytest yet.

-   [#4049](https://github.com/pytest-dev/pytest/issues/4049): Introduced a new hook named [`pytest_warning_recorded`] to convey information about warnings captured by the internal [`pytest`] warnings plugin.

    This hook is meant to replace [`pytest_warning_captured`], which is deprecated and will be removed in a future release.

-   [#6471](https://github.com/pytest-dev/pytest/issues/6471): New command-line flags:

    -   [`--no-header`]: disables the initial header, including platform, version, and plugins.

    -   [`--no-summary`]: disables the final test summary, including warnings.

-   [#6856](https://github.com/pytest-dev/pytest/issues/6856): A warning is now shown when an unknown key is read from a config INI file.

    The [`--strict-config`] flag has been added to treat these warnings as errors.

-   [#6906](https://github.com/pytest-dev/pytest/issues/6906): Added [`--code-highlight`] command line option to enable/disable code highlighting in terminal output.

-   [#7245](https://github.com/pytest-dev/pytest/issues/7245): New [`--import-mode=importlib`] option that uses [[`importlib`]](https://docs.python.org/3/library/importlib.html#module-importlib "(in Python v3.14)") to import test modules.

    Traditionally pytest used [`__import__`] while changing [`sys.path`] to import test modules (which also changes [`sys.modules`] as a side-effect), which works but has a number of drawbacks, like requiring test modules that don't live in packages to have unique names (as they need to reside under a unique name in [`sys.modules`]).

    [`--import-mode=importlib`] uses more fine-grained import mechanisms from [`importlib`] which don't require pytest to change [`sys.path`] or [`sys.modules`] at all, eliminating much of the drawbacks of the previous mode.

    We intend to make [`--import-mode=importlib`] the default in future versions, so users are encouraged to try the new mode and provide feedback (both positive or negative) in issue [#7245](https://github.com/pytest-dev/pytest/issues/7245).

    You can read more about this option in [[the documentation]](explanation/pythonpath.html#import-modes).

-   [#7305](https://github.com/pytest-dev/pytest/issues/7305): New [`required_plugins`] configuration option allows the user to specify a list of plugins, including version information, that are required for pytest to run. An error is raised if any required plugins are not found when running pytest.

### Improvements[¶](#id658 "Link to this heading")

-   [#4375](https://github.com/pytest-dev/pytest/issues/4375): The [`pytest`] command now suppresses the [`BrokenPipeError`] error message that is printed to stderr when the output of [`pytest`] is piped and the pipe is closed by the piped-to program (common examples are [`less`] and [`head`]).

-   [#4391](https://github.com/pytest-dev/pytest/issues/4391): Improved precision of test durations measurement. [`CallInfo`] items now have a new [`<CallInfo>.duration`] attribute, created using [`time.perf_counter()`]. This attribute is used to fill the [`<TestReport>.duration`] attribute, which is more accurate than the previous [`<CallInfo>.stop`]` `[`-`]` `[`<CallInfo>.start`] (as these are based on [`time.time()`]).

-   [#4675](https://github.com/pytest-dev/pytest/issues/4675): Rich comparison for dataclasses and [`attrs`]-classes is now recursive.

-   [#6285](https://github.com/pytest-dev/pytest/issues/6285): Exposed the [`pytest.FixtureLookupError`] exception which is raised by [`request.getfixturevalue()`] (where [`request`] is a [`FixtureRequest`] fixture) when a fixture with the given name cannot be returned.

-   [#6433](https://github.com/pytest-dev/pytest/issues/6433): If an error is encountered while formatting the message in a logging call, for example [`logging.warning("oh`]` `[`no!:`]` `[`%s:`]` `[`%s",`]` `[`"first")`] (a second argument is missing), pytest now propagates the error, likely causing the test to fail.

    Previously, such a mistake would cause an error to be printed to stderr, which is not displayed by default for passing tests. This change makes the mistake visible during testing.

    You may suppress this behavior temporarily or permanently by setting [`logging.raiseExceptions`]` `[`=`]` `[`False`].

-   [#6817](https://github.com/pytest-dev/pytest/issues/6817): Explicit new-lines in help texts of command-line options are preserved, allowing plugins better control of the help displayed to users.

-   [#6940](https://github.com/pytest-dev/pytest/issues/6940): When using the [`--duration`] option, the terminal message output is now more precise about the number and duration of hidden items.

-   [#6991](https://github.com/pytest-dev/pytest/issues/6991): Collected files are displayed after any reports from hooks, e.g. the status from [`--lf`].

-   [#7091](https://github.com/pytest-dev/pytest/issues/7091): When [`fd`] capturing is used, through [`--capture=fd`] or the [`capfd`] and [`capfdbinary`] fixtures, and the file descriptor (0, 1, 2) cannot be duplicated, FD capturing is still performed. Previously, direct writes to the file descriptors would fail or be lost in this case.

-   [#7119](https://github.com/pytest-dev/pytest/issues/7119): Exit with an error if the [`--basetemp`] argument is empty, is the current working directory or is one of the parent directories. This is done to protect against accidental data loss, as any directory passed to this argument is cleared.

-   [#7128](https://github.com/pytest-dev/pytest/issues/7128): [`pytest`]` `[`--version`] now displays just the pytest version, while [`pytest`]` `[`--version`]` `[`--version`] displays more verbose information including plugins. This is more consistent with how other tools show [`--version`].

-   [#7133](https://github.com/pytest-dev/pytest/issues/7133): [[`caplog.set_level()`]](reference/reference.html#pytest.LogCaptureFixture.set_level "pytest.LogCaptureFixture.set_level") will now override any [[`log_level`]](reference/reference.html#confval-log_level) set via the CLI or configuration file.

-   [#7159](https://github.com/pytest-dev/pytest/issues/7159): [[`caplog.set_level()`]](reference/reference.html#pytest.LogCaptureFixture.set_level "pytest.LogCaptureFixture.set_level") and [[`caplog.at_level()`]](reference/reference.html#pytest.LogCaptureFixture.at_level "pytest.LogCaptureFixture.at_level") no longer affect the level of logs that are shown in the *Captured log report* report section.

-   [#7348](https://github.com/pytest-dev/pytest/issues/7348): Improve recursive diff report for comparison asserts on dataclasses / attrs.

-   [#7385](https://github.com/pytest-dev/pytest/issues/7385): [`--junitxml`] now includes the exception cause in the [`message`] XML attribute for failures during setup and teardown.

    Previously:

    ::: 
    ::: highlight
        <error message="test setup failure">
    :::
    :::

    Now:

    ::: 
    ::: highlight
        <error message="failed on setup with &quot;ValueError: Some error during setup&quot;">
    :::
    :::

### Bug Fixes[¶](#id659 "Link to this heading")

-   [#1120](https://github.com/pytest-dev/pytest/issues/1120): Fix issue where directories from [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir) are not removed properly when multiple instances of pytest are running in parallel.

-   [#4583](https://github.com/pytest-dev/pytest/issues/4583): Prevent crashing and provide a user-friendly error when a marker expression ([`-m`]) invoking of [[`eval()`]](https://docs.python.org/3/library/functions.html#eval "(in Python v3.14)") raises any exception.

-   [#4677](https://github.com/pytest-dev/pytest/issues/4677): The path shown in the summary report for SKIPPED tests is now always relative. Previously it was sometimes absolute.

-   [#5456](https://github.com/pytest-dev/pytest/issues/5456): Fix a possible race condition when trying to remove lock files used to control access to folders created by [[`tmp_path`]](reference/reference.html#std-fixture-tmp_path) and [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir).

-   [#6240](https://github.com/pytest-dev/pytest/issues/6240): Fixes an issue where logging during collection step caused duplication of log messages to stderr.

-   [#6428](https://github.com/pytest-dev/pytest/issues/6428): Paths appearing in error messages are now correct in case the current working directory has changed since the start of the session.

-   [#6755](https://github.com/pytest-dev/pytest/issues/6755): Support deleting paths longer than 260 characters on windows created inside [[`tmpdir`]](reference/reference.html#std-fixture-tmpdir).

-   [#6871](https://github.com/pytest-dev/pytest/issues/6871): Fix crash with captured output when using [[`capsysbinary`]](reference/reference.html#std-fixture-capsysbinary).

-   [#6909](https://github.com/pytest-dev/pytest/issues/6909): Revert the change introduced by [#6330](https://github.com/pytest-dev/pytest/pull/6330), which required all arguments to [`@pytest.mark.parametrize`] to be explicitly defined in the function signature.

    The intention of the original change was to remove what was expected to be an unintended/surprising behavior, but it turns out many people relied on it, so the restriction has been reverted.

-   [#6910](https://github.com/pytest-dev/pytest/issues/6910): Fix crash when plugins return an unknown stats while using the [`--reportlog`] option.

-   [#6924](https://github.com/pytest-dev/pytest/issues/6924): Ensure a [`unittest.IsolatedAsyncioTestCase`] is actually awaited.

-   [#6925](https://github.com/pytest-dev/pytest/issues/6925): Fix [`TerminalRepr`] instances to be hashable again.

-   [#6947](https://github.com/pytest-dev/pytest/issues/6947): Fix regression where functions registered with [[`unittest.TestCase.addCleanup()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "(in Python v3.14)") were not being called on test failures.

-   [#6951](https://github.com/pytest-dev/pytest/issues/6951): Allow users to still set the deprecated [`TerminalReporter.writer`] attribute.

-   [#6956](https://github.com/pytest-dev/pytest/issues/6956): Prevent pytest from printing [`ConftestImportFailure`] traceback to stdout.

-   [#6991](https://github.com/pytest-dev/pytest/issues/6991): Fix regressions with [`--lf`] filtering too much since pytest 5.4.

-   [#6992](https://github.com/pytest-dev/pytest/issues/6992): Revert "tmpdir: clean up indirection via config for factories" [#6767](https://github.com/pytest-dev/pytest/issues/6767) as it breaks pytest-xdist.

-   [#7061](https://github.com/pytest-dev/pytest/issues/7061): When a yielding fixture fails to yield a value, report a test setup error instead of crashing.

-   [#7076](https://github.com/pytest-dev/pytest/issues/7076): The path of file skipped by [`@pytest.mark.skip`] in the SKIPPED report is now relative to invocation directory. Previously it was relative to root directory.

-   [#7110](https://github.com/pytest-dev/pytest/issues/7110): Fixed regression: [`asyncbase.TestCase`] tests are executed correctly again.

-   [#7126](https://github.com/pytest-dev/pytest/issues/7126): [`--setup-show`] now doesn't raise an error when a bytes value is used as a [`parametrize`] parameter when Python is called with the [`-bb`] flag.

-   [#7143](https://github.com/pytest-dev/pytest/issues/7143): Fix [[`pytest.File.from_parent`]](reference/reference.html#pytest.nodes.Node.from_parent "_pytest.nodes.Node.from_parent") so it forwards extra keyword arguments to the constructor.

-   [#7145](https://github.com/pytest-dev/pytest/issues/7145): Classes with broken [`__getattribute__`] methods are displayed correctly during failures.

-   [#7150](https://github.com/pytest-dev/pytest/issues/7150): Prevent hiding the underlying exception when [`ConfTestImportFailure`] is raised.

-   [#7180](https://github.com/pytest-dev/pytest/issues/7180): Fix [`_is_setup_py`] for files encoded differently than locale.

-   [#7215](https://github.com/pytest-dev/pytest/issues/7215): Fix regression where running with [`--pdb`] would call [[`unittest.TestCase.tearDown()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "(in Python v3.14)") for skipped tests.

-   [#7253](https://github.com/pytest-dev/pytest/issues/7253): When using [`pytest.fixture`] on a function directly, as in [`pytest.fixture(func)`], if the [`autouse`] or [`params`] arguments are also passed, the function is no longer ignored, but is marked as a fixture.

-   [#7360](https://github.com/pytest-dev/pytest/issues/7360): Fix possibly incorrect evaluation of string expressions passed to [`pytest.mark.skipif`] and [`pytest.mark.xfail`], in rare circumstances where the exact same string is used but refers to different global values.

-   [#7383](https://github.com/pytest-dev/pytest/issues/7383): Fixed exception causes all over the codebase, i.e. use [`raise`]` `[`new_exception`]` `[`from`]` `[`old_exception`] when wrapping an exception.

### Improved Documentation[¶](#id660 "Link to this heading")

-   [#7202](https://github.com/pytest-dev/pytest/issues/7202): The development guide now links to the contributing section of the docs and [`RELEASING.rst`] on GitHub.

-   [#7233](https://github.com/pytest-dev/pytest/issues/7233): Add a note about [`--strict`] and [`--strict-markers`] and the preference for the latter one.

-   [#7345](https://github.com/pytest-dev/pytest/issues/7345): Explain indirect parametrization and markers for fixtures.

### Trivial/Internal Changes[¶](#id661 "Link to this heading")

-   [#7035](https://github.com/pytest-dev/pytest/issues/7035): The [`originalname`] attribute of [`_pytest.python.Function`] now defaults to [`name`] if not provided explicitly, and is always set.

-   [#7264](https://github.com/pytest-dev/pytest/issues/7264): The dependency on the [`wcwidth`] package has been removed.

-   [#7291](https://github.com/pytest-dev/pytest/issues/7291): Replaced [`py.iniconfig`] with [iniconfig](https://pypi.org/project/iniconfig).

-   [#7295](https://github.com/pytest-dev/pytest/issues/7295): [`src/_pytest/config/__init__.py`] now uses the [`warnings`] module to report warnings instead of [`sys.stderr.write`].

-   [#7356](https://github.com/pytest-dev/pytest/issues/7356): Remove last internal uses of deprecated *slave* term from old [`pytest-xdist`].

-   [#7357](https://github.com/pytest-dev/pytest/issues/7357): [`py`]\>=1.8.2 is now required.

## pytest 5.4.3 (2020-06-02)[¶](#pytest-5-4-3-2020-06-02 "Link to this heading")

### Bug Fixes[¶](#id662 "Link to this heading")

-   [#6428](https://github.com/pytest-dev/pytest/issues/6428): Paths appearing in error messages are now correct in case the current working directory has changed since the start of the session.

-   [#6755](https://github.com/pytest-dev/pytest/issues/6755): Support deleting paths longer than 260 characters on windows created inside tmpdir.

-   [#6956](https://github.com/pytest-dev/pytest/issues/6956): Prevent pytest from printing ConftestImportFailure traceback to stdout.

-   [#7150](https://github.com/pytest-dev/pytest/issues/7150): Prevent hiding the underlying exception when [`ConfTestImportFailure`] is raised.

-   [#7215](https://github.com/pytest-dev/pytest/issues/7215): Fix regression where running with [`--pdb`] would call the [`tearDown`] methods of [`unittest.TestCase`] subclasses for skipped tests.

## pytest 5.4.2 (2020-05-08)[¶](#pytest-5-4-2-2020-05-08 "Link to this heading")

### Bug Fixes[¶](#id663 "Link to this heading")

-   [#6871](https://github.com/pytest-dev/pytest/issues/6871): Fix crash with captured output when using the [[`capsysbinary`]` `[`fixture`]](reference/reference.html#std-fixture-capsysbinary).

-   [#6924](https://github.com/pytest-dev/pytest/issues/6924): Ensure a [`unittest.IsolatedAsyncioTestCase`] is actually awaited.

-   [#6925](https://github.com/pytest-dev/pytest/issues/6925): Fix TerminalRepr instances to be hashable again.

-   [#6947](https://github.com/pytest-dev/pytest/issues/6947): Fix regression where functions registered with [`TestCase.addCleanup`] were not being called on test failures.

-   [#6951](https://github.com/pytest-dev/pytest/issues/6951): Allow users to still set the deprecated [`TerminalReporter.writer`] attribute.

-   [#6992](https://github.com/pytest-dev/pytest/issues/6992): Revert "tmpdir: clean up indirection via config for factories" #6767 as it breaks pytest-xdist.

-   [#7110](https://github.com/pytest-dev/pytest/issues/7110): Fixed regression: [`asyncbase.TestCase`] tests are executed correctly again.

-   [#7143](https://github.com/pytest-dev/pytest/issues/7143): Fix [`File.from_parent`] so it forwards extra keyword arguments to the constructor.

-   [#7145](https://github.com/pytest-dev/pytest/issues/7145): Classes with broken [`__getattribute__`] methods are displayed correctly during failures.

-   [#7180](https://github.com/pytest-dev/pytest/issues/7180): Fix [`_is_setup_py`] for files encoded differently than locale.

## pytest 5.4.1 (2020-03-13)[¶](#pytest-5-4-1-2020-03-13 "Link to this heading")

### Bug Fixes[¶](#id664 "Link to this heading")

-   [#6909](https://github.com/pytest-dev/pytest/issues/6909): Revert the change introduced by [#6330](https://github.com/pytest-dev/pytest/pull/6330), which required all arguments to [`@pytest.mark.parametrize`] to be explicitly defined in the function signature.

    The intention of the original change was to remove what was expected to be an unintended/surprising behavior, but it turns out many people relied on it, so the restriction has been reverted.

-   [#6910](https://github.com/pytest-dev/pytest/issues/6910): Fix crash when plugins return an unknown stats while using the [`--reportlog`] option.

## pytest 5.4.0 (2020-03-12)[¶](#pytest-5-4-0-2020-03-12 "Link to this heading")

### Breaking Changes[¶](#id665 "Link to this heading")

-   [#6316](https://github.com/pytest-dev/pytest/issues/6316): Matching of [`-k`]` `[`EXPRESSION`] to test names is now case-insensitive.

-   [#6443](https://github.com/pytest-dev/pytest/issues/6443): Plugins specified with [`-p`] are now loaded after internal plugins, which results in their hooks being called *before* the internal ones.

    This makes the [`-p`] behavior consistent with [`PYTEST_PLUGINS`].

-   [#6637](https://github.com/pytest-dev/pytest/issues/6637): Removed the long-deprecated [`pytest_itemstart`] hook.

    This hook has been marked as deprecated and not been even called by pytest for over 10 years now.

-   [#6673](https://github.com/pytest-dev/pytest/issues/6673): Reversed / fix meaning of "+/-" in error diffs. "-" means that something expected is missing in the result and "+" means that there are unexpected extras in the result.

-   [#6737](https://github.com/pytest-dev/pytest/issues/6737): The [`cached_result`] attribute of [`FixtureDef`] is now set to [`None`] when the result is unavailable, instead of being deleted.

    If your plugin performs checks like [`hasattr(fixturedef,`]` `[`'cached_result')`], for example in a [`pytest_fixture_post_finalizer`] hook implementation, replace it with [`fixturedef.cached_result`]` `[`is`]` `[`not`]` `[`None`]. If you [`del`] the attribute, set it to [`None`] instead.

### Deprecations[¶](#id666 "Link to this heading")

-   [#3238](https://github.com/pytest-dev/pytest/issues/3238): Option [`--no-print-logs`] is deprecated and meant to be removed in a future release. If you use [`--no-print-logs`], please try out [`--show-capture`] and provide feedback.

    [`--show-capture`] command-line option was added in [`pytest`]` `[`3.5.0`] and allows to specify how to display captured output when tests fail: [`no`], [`stdout`], [`stderr`], [`log`] or [`all`] (the default).

-   [#571](https://github.com/pytest-dev/pytest/issues/571): Deprecate the unused/broken [`pytest_collect_directory`] hook. It was misaligned since the removal of the [`Directory`] collector in 2010 and incorrect/unusable as soon as collection was split from test execution.

-   [#5975](https://github.com/pytest-dev/pytest/issues/5975): Deprecate using direct constructors for [`Nodes`].

    Instead they are now constructed via [`Node.from_parent`].

    This transitional mechanism enables us to untangle the very intensely entangled [`Node`] relationships by enforcing more controlled creation/configuration patterns.

    As part of this change, session/config are already disallowed parameters and as we work on the details we might need disallow a few more as well.

    Subclasses are expected to use [`super().from_parent`] if they intend to expand the creation of [`Nodes`].

-   [#6779](https://github.com/pytest-dev/pytest/issues/6779): The [`TerminalReporter.writer`] attribute has been deprecated and should no longer be used. This was inadvertently exposed as part of the public API of that plugin and ties it too much with [`py.io.TerminalWriter`].

### Features[¶](#id667 "Link to this heading")

-   [#4597](https://github.com/pytest-dev/pytest/issues/4597): New [[--capture=tee-sys]](how-to/capture-stdout-stderr.html#capture-method) option to allow both live printing and capturing of test output.

-   [#5712](https://github.com/pytest-dev/pytest/issues/5712): Now all arguments to [`@pytest.mark.parametrize`] need to be explicitly declared in the function signature or via [`indirect`]. Previously it was possible to omit an argument if a fixture with the same name existed, which was just an accident of implementation and was not meant to be a part of the API.

-   [#6454](https://github.com/pytest-dev/pytest/issues/6454): Changed default for [`-r`] to [`fE`], which displays failures and errors in the [[short test summary]](how-to/output.html#pytest-detailed-failed-tests-usage). [`-rN`] can be used to disable it (the old behavior).

-   [#6469](https://github.com/pytest-dev/pytest/issues/6469): New options have been added to the [[`junit_logging`]](reference/reference.html#confval-junit_logging) option: [`log`], [`out-err`], and [`all`].

-   [#6834](https://github.com/pytest-dev/pytest/issues/6834): Excess warning summaries are now collapsed per file to ensure readable display of warning summaries.

### Improvements[¶](#id668 "Link to this heading")

-   [#1857](https://github.com/pytest-dev/pytest/issues/1857): [`pytest.mark.parametrize`] accepts integers for [`ids`] again, converting it to strings.

-   [#449](https://github.com/pytest-dev/pytest/issues/449): Use "yellow" main color with any XPASSED tests.

-   [#4639](https://github.com/pytest-dev/pytest/issues/4639): Revert "A warning is now issued when assertions are made for [`None`]".

    The warning proved to be less useful than initially expected and had quite a few false positive cases.

-   [#5686](https://github.com/pytest-dev/pytest/issues/5686): [`tmpdir_factory.mktemp`] now fails when given absolute and non-normalized paths.

-   [#5984](https://github.com/pytest-dev/pytest/issues/5984): The [`pytest_warning_captured`] hook now receives a [`location`] parameter with the code location that generated the warning.

-   [#6213](https://github.com/pytest-dev/pytest/issues/6213): pytester: the [`testdir`] fixture respects environment settings from the [`monkeypatch`] fixture for inner runs.

-   [#6247](https://github.com/pytest-dev/pytest/issues/6247): [`--fulltrace`] is honored with collection errors.

-   [#6384](https://github.com/pytest-dev/pytest/issues/6384): Make [`--showlocals`] work also with [`--tb=short`].

-   [#6653](https://github.com/pytest-dev/pytest/issues/6653): Add support for matching lines consecutively with [[`LineMatcher`]](reference/reference.html#pytest.LineMatcher "pytest.LineMatcher")'s [[`fnmatch_lines()`]](reference/reference.html#pytest.LineMatcher.fnmatch_lines "pytest.LineMatcher.fnmatch_lines") and [[`re_match_lines()`]](reference/reference.html#pytest.LineMatcher.re_match_lines "pytest.LineMatcher.re_match_lines").

-   [#6658](https://github.com/pytest-dev/pytest/issues/6658): Code is now highlighted in tracebacks when [`pygments`] is installed.

    Users are encouraged to install [`pygments`] into their environment and provide feedback, because the plan is to make [`pygments`] a regular dependency in the future.

-   [#6795](https://github.com/pytest-dev/pytest/issues/6795): Import usage error message with invalid [`-o`] option.

-   [#759](https://github.com/pytest-dev/pytest/issues/759): [`pytest.mark.parametrize`] supports iterators and generators for [`ids`].

### Bug Fixes[¶](#id669 "Link to this heading")

-   [#310](https://github.com/pytest-dev/pytest/issues/310): Add support for calling [`pytest.xfail()`] and [`pytest.importorskip()`] with doctests.

-   [#3823](https://github.com/pytest-dev/pytest/issues/3823): [`--trace`] now works with unittests.

-   [#4445](https://github.com/pytest-dev/pytest/issues/4445): Fixed some warning reports produced by pytest to point to the correct location of the warning in the user's code.

-   [#5301](https://github.com/pytest-dev/pytest/issues/5301): Fix [`--last-failed`] to collect new tests from files with known failures.

-   [#5928](https://github.com/pytest-dev/pytest/issues/5928): Report [`PytestUnknownMarkWarning`] at the level of the user's code, not [`pytest`]'s.

-   [#5991](https://github.com/pytest-dev/pytest/issues/5991): Fix interaction with [`--pdb`] and unittests: do not use unittest's [`TestCase.debug()`].

-   [#6334](https://github.com/pytest-dev/pytest/issues/6334): Fix summary entries appearing twice when [`f/F`] and [`s/S`] report chars were used at the same time in the [`-r`] command-line option (for example [`-rFf`]).

    The upper case variants were never documented and the preferred form should be the lower case.

-   [#6409](https://github.com/pytest-dev/pytest/issues/6409): Fallback to green (instead of yellow) for non-last items without previous passes with colored terminal progress indicator.

-   [#6454](https://github.com/pytest-dev/pytest/issues/6454): [`--disable-warnings`] is honored with [`-ra`] and [`-rA`].

-   [#6497](https://github.com/pytest-dev/pytest/issues/6497): Fix bug in the comparison of request key with cached key in fixture.

    A construct [`if`]` `[`key`]` `[`==`]` `[`cached_key:`] can fail either because [`==`] is explicitly disallowed, or for, e.g., NumPy arrays, where the result of [`a`]` `[`==`]` `[`b`] cannot generally be converted to [[`bool`]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"). The implemented fix replaces [`==`] with [`is`].

-   [#6557](https://github.com/pytest-dev/pytest/issues/6557): Make capture output streams [`.write()`] method return the same return value from original streams.

-   [#6566](https://github.com/pytest-dev/pytest/issues/6566): Fix [`EncodedFile.writelines`] to call the underlying buffer's [`writelines`] method.

-   [#6575](https://github.com/pytest-dev/pytest/issues/6575): Fix internal crash when [`faulthandler`] starts initialized (for example with [`PYTHONFAULTHANDLER=1`] environment variable set) and [`faulthandler_timeout`] defined in the configuration file.

-   [#6597](https://github.com/pytest-dev/pytest/issues/6597): Fix node ids which contain a parametrized empty-string variable.

-   [#6646](https://github.com/pytest-dev/pytest/issues/6646): Assertion rewriting hooks are (re)stored for the current item, which fixes them being still used after e.g. pytester's [`testdir.runpytest`] etc.

-   [#6660](https://github.com/pytest-dev/pytest/issues/6660): [[`pytest.exit()`]](reference/reference.html#pytest.exit "pytest.exit") is handled when emitted from the [[`pytest_sessionfinish`]](reference/reference.html#std-hook-pytest_sessionfinish) hook. This includes quitting from a debugger.

-   [#6752](https://github.com/pytest-dev/pytest/issues/6752): When [[`pytest.raises()`]](reference/reference.html#pytest.raises "pytest.raises") is used as a function (as opposed to a context manager), a [`match`] keyword argument is now passed through to the tested function. Previously it was swallowed and ignored (regression in pytest 5.1.0).

-   [#6801](https://github.com/pytest-dev/pytest/issues/6801): Do not display empty lines in between traceback for unexpected exceptions with doctests.

-   [#6802](https://github.com/pytest-dev/pytest/issues/6802): The [[`testdir`]` `[`fixture`]](reference/reference.html#std-fixture-testdir) works within doctests now.

### Improved Documentation[¶](#id670 "Link to this heading")

-   [#6696](https://github.com/pytest-dev/pytest/issues/6696): Add list of fixtures to start of fixture chapter.

-   [#6742](https://github.com/pytest-dev/pytest/issues/6742): Expand first sentence on fixtures into a paragraph.

### Trivial/Internal Changes[¶](#id671 "Link to this heading")

-   [#6404](https://github.com/pytest-dev/pytest/issues/6404): Remove usage of [`parser`] module, deprecated in Python 3.9.

## pytest 5.3.5 (2020-01-29)[¶](#pytest-5-3-5-2020-01-29 "Link to this heading")

### Bug Fixes[¶](#id672 "Link to this heading")

-   [#6517](https://github.com/pytest-dev/pytest/issues/6517): Fix regression in pytest 5.3.4 causing an INTERNALERROR due to a wrong assertion.

## pytest 5.3.4 (2020-01-20)[¶](#pytest-5-3-4-2020-01-20 "Link to this heading")

### Bug Fixes[¶](#id673 "Link to this heading")

-   [#6496](https://github.com/pytest-dev/pytest/issues/6496): Revert [#6436](https://github.com/pytest-dev/pytest/issues/6436): unfortunately this change has caused a number of regressions in many suites, so the team decided to revert this change and make a new release while we continue to look for a solution.

## pytest 5.3.3 (2020-01-16)[¶](#pytest-5-3-3-2020-01-16 "Link to this heading")

### Bug Fixes[¶](#id674 "Link to this heading")

-   [#2780](https://github.com/pytest-dev/pytest/issues/2780): Captured output during teardown is shown with [`-rP`].

-   [#5971](https://github.com/pytest-dev/pytest/issues/5971): Fix a [`pytest-xdist`] crash when dealing with exceptions raised in subprocesses created by the [`multiprocessing`] module.

-   [#6436](https://github.com/pytest-dev/pytest/issues/6436): [[`FixtureDef`]](reference/reference.html#pytest.FixtureDef "pytest.FixtureDef") objects now properly register their finalizers with autouse and parameterized fixtures that execute before them in the fixture stack so they are torn down at the right times, and in the right order.

-   [#6532](https://github.com/pytest-dev/pytest/issues/6532): Fix parsing of outcomes containing multiple errors with [`testdir`] results (regression in 5.3.0).

### Trivial/Internal Changes[¶](#id675 "Link to this heading")

-   [#6350](https://github.com/pytest-dev/pytest/issues/6350): Optimized automatic renaming of test parameter IDs.

## pytest 5.3.2 (2019-12-13)[¶](#pytest-5-3-2-2019-12-13 "Link to this heading")

### Improvements[¶](#id676 "Link to this heading")

-   [#4639](https://github.com/pytest-dev/pytest/issues/4639): Revert "A warning is now issued when assertions are made for [`None`]".

    The warning proved to be less useful than initially expected and had quite a few false positive cases.

### Bug Fixes[¶](#id677 "Link to this heading")

-   [#5430](https://github.com/pytest-dev/pytest/issues/5430): junitxml: Logs for failed test are now passed to junit report in case the test fails during call phase.

-   [#6290](https://github.com/pytest-dev/pytest/issues/6290): The supporting files in the [`.pytest_cache`] directory are kept with [`--cache-clear`], which only clears cached values now.

-   [#6301](https://github.com/pytest-dev/pytest/issues/6301): Fix assertion rewriting for egg-based distributions and [`editable`] installs ([`pip`]` `[`install`]` `[`--editable`]).

## pytest 5.3.1 (2019-11-25)[¶](#pytest-5-3-1-2019-11-25 "Link to this heading")

### Improvements[¶](#id678 "Link to this heading")

-   [#6231](https://github.com/pytest-dev/pytest/issues/6231): Improve check for misspelling of [[pytest.mark.parametrize]](reference/reference.html#pytest-mark-parametrize-ref).

-   [#6257](https://github.com/pytest-dev/pytest/issues/6257): Handle [[`pytest.exit()`]](reference/reference.html#pytest.exit "pytest.exit") being used via [[`pytest_internalerror`]](reference/reference.html#std-hook-pytest_internalerror), e.g. when quitting pdb from post mortem.

### Bug Fixes[¶](#id679 "Link to this heading")

-   [#5914](https://github.com/pytest-dev/pytest/issues/5914): pytester: fix [[`no_fnmatch_line()`]](reference/reference.html#pytest.LineMatcher.no_fnmatch_line "pytest.LineMatcher.no_fnmatch_line") when used after positive matching.

-   [#6082](https://github.com/pytest-dev/pytest/issues/6082): Fix line detection for doctest samples inside [[`property`]](https://docs.python.org/3/library/functions.html#property "(in Python v3.14)") docstrings, as a workaround to [python/cpython#61648](https://github.com/python/cpython/issues/61648).

-   [#6254](https://github.com/pytest-dev/pytest/issues/6254): Fix compatibility with pytest-parallel (regression in pytest 5.3.0).

-   [#6255](https://github.com/pytest-dev/pytest/issues/6255): Clear the [[`sys.last_traceback`]](https://docs.python.org/3/library/sys.html#sys.last_traceback "(in Python v3.14)"), [[`sys.last_type`]](https://docs.python.org/3/library/sys.html#sys.last_type "(in Python v3.14)") and [[`sys.last_value`]](https://docs.python.org/3/library/sys.html#sys.last_value "(in Python v3.14)") attributes by deleting them instead of setting them to [`None`]. This better matches the behaviour of the Python standard library.

## pytest 5.3.0 (2019-11-19)[¶](#pytest-5-3-0-2019-11-19 "Link to this heading")

### Deprecations[¶](#id680 "Link to this heading")

-   [#6179](https://github.com/pytest-dev/pytest/issues/6179): The default value of [[`junit_family`]](reference/reference.html#confval-junit_family) option will change to [`"xunit2"`] in pytest 6.0, given that this is the version supported by default in modern tools that manipulate this type of file.

    In order to smooth the transition, pytest will issue a warning in case the [`--junitxml`] option is given in the command line but [[`junit_family`]](reference/reference.html#confval-junit_family) is not explicitly configured in [`pytest.ini`].

    For more information, [[see the docs]](deprecations.html#junit-family-changed-default-value).

### Features[¶](#id681 "Link to this heading")

-   [#4488](https://github.com/pytest-dev/pytest/issues/4488): The pytest team has created the [pytest-reportlog](https://github.com/pytest-dev/pytest-reportlog) plugin, which provides a new [`--report-log=FILE`] option that writes *report logs* into a file as the test session executes.

    Each line of the report log contains a self contained JSON object corresponding to a testing event, such as a collection or a test result report. The file is guaranteed to be flushed after writing each line, so systems can read and process events in real-time.

    The plugin is meant to replace the [`--resultlog`] option, which is deprecated and meant to be removed in a future release. If you use [`--resultlog`], please try out [`pytest-reportlog`] and provide feedback.

-   [#4730](https://github.com/pytest-dev/pytest/issues/4730): When [[`sys.pycache_prefix`]](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "(in Python v3.14)") (Python 3.8+) is set, it will be used by pytest to cache test files changed by the assertion rewriting mechanism.

    This makes it easier to benefit of cached [`.pyc`] files even on file systems without permissions.

-   [#5515](https://github.com/pytest-dev/pytest/issues/5515): Allow selective auto-indentation of multiline log messages.

    Adds command line option [`--log-auto-indent`], config option [[`log_auto_indent`]](reference/reference.html#confval-log_auto_indent) and support for per-entry configuration of indentation behavior on calls to [[`logging.log()`]](https://docs.python.org/3/library/logging.html#logging.log "(in Python v3.14)").

    Alters the default for auto-indention from [`"on"`] to [`"off"`]. This restores the older behavior that existed prior to v4.6.0. This reversion to earlier behavior was done because it is better to activate new features that may lead to broken tests explicitly rather than implicitly.

-   [#5914](https://github.com/pytest-dev/pytest/issues/5914): [[`testdir`]](reference/reference.html#std-fixture-testdir) learned two new functions, [[`no_fnmatch_line()`]](reference/reference.html#pytest.LineMatcher.no_fnmatch_line "pytest.LineMatcher.no_fnmatch_line") and [[`no_re_match_line()`]](reference/reference.html#pytest.LineMatcher.no_re_match_line "pytest.LineMatcher.no_re_match_line").

    The functions are used to ensure the captured text *does not* match the given pattern.

    The previous idiom was to use [[`re.match()`]](https://docs.python.org/3/library/re.html#re.match "(in Python v3.14)"):

    ::: 
    ::: highlight
        result = testdir.runpytest()
        assert re.match(pat, result.stdout.str()) is None
    :::
    :::

    Or the [`in`] operator:

    ::: 
    ::: highlight
        result = testdir.runpytest()
        assert text in result.stdout.str()
    :::
    :::

    But the new functions produce best output on failure.

-   [#6057](https://github.com/pytest-dev/pytest/issues/6057): Added tolerances to complex values when printing [`pytest.approx`].

    For example, [`repr(pytest.approx(3+4j))`] returns [`(3+4j)`]` `[`±`]` `[`5e-06`]` `[`∠`]` `[`±180°`]. This is polar notation indicating a circle around the expected value, with a radius of 5e-06. For [`approx`] comparisons to return [`True`], the actual value should fall within this circle.

-   [#6061](https://github.com/pytest-dev/pytest/issues/6061): Added the pluginmanager as an argument to [`pytest_addoption`] so that hooks can be invoked when setting up command line options. This is useful for having one plugin communicate things to another plugin, such as default values or which set of command line options to add.

### Improvements[¶](#id682 "Link to this heading")

-   [#5061](https://github.com/pytest-dev/pytest/issues/5061): Use multiple colors with terminal summary statistics.

-   [#5630](https://github.com/pytest-dev/pytest/issues/5630): Quitting from debuggers is now properly handled in [`doctest`] items.

-   [#5924](https://github.com/pytest-dev/pytest/issues/5924): Improved verbose diff output with sequences.

    Before:

    ::: 
    ::: highlight
        E   AssertionError: assert ['version', '...version_info'] == ['version', '...version', ...]
        E     Right contains 3 more items, first extra item: ' '
        E     Full diff:
        E     - ['version', 'version_info', 'sys.version', 'sys.version_info']
        E     + ['version',
        E     +  'version_info',
        E     +  'sys.version',
        E     +  'sys.version_info',
        E     +  ' ',
        E     +  'sys.version',
        E     +  'sys.version_info']
    :::
    :::

    After:

    ::: 
    ::: highlight
        E   AssertionError: assert ['version', '...version_info'] == ['version', '...version', ...]
        E     Right contains 3 more items, first extra item: ' '
        E     Full diff:
        E       [
        E        'version',
        E        'version_info',
        E        'sys.version',
        E        'sys.version_info',
        E     +  ' ',
        E     +  'sys.version',
        E     +  'sys.version_info',
        E       ]
    :::
    :::

-   [#5934](https://github.com/pytest-dev/pytest/issues/5934): [`repr`] of [`ExceptionInfo`] objects has been improved to honor the [`__repr__`] method of the underlying exception.

-   [#5936](https://github.com/pytest-dev/pytest/issues/5936): Display untruncated assertion message with [`-vv`].

-   [#5990](https://github.com/pytest-dev/pytest/issues/5990): Fixed plurality mismatch in test summary (e.g. display "1 error" instead of "1 errors").

-   [#6008](https://github.com/pytest-dev/pytest/issues/6008): [`Config.InvocationParams.args`] is now always a [`tuple`] to better convey that it should be immutable and avoid accidental modifications.

-   [#6023](https://github.com/pytest-dev/pytest/issues/6023): [`pytest.main`] returns a [`pytest.ExitCode`] instance now, except for when custom exit codes are used (where it returns [`int`] then still).

-   [#6026](https://github.com/pytest-dev/pytest/issues/6026): Align prefixes in output of pytester's [`LineMatcher`].

-   [#6059](https://github.com/pytest-dev/pytest/issues/6059): Collection errors are reported as errors (and not failures like before) in the terminal's short test summary.

-   [#6069](https://github.com/pytest-dev/pytest/issues/6069): [`pytester.spawn`] does not skip/xfail tests on FreeBSD anymore unconditionally.

-   [#6097](https://github.com/pytest-dev/pytest/issues/6097): The "\[...%\]" indicator in the test summary is now colored according to the final (new) multi-colored line's main color.

-   [#6116](https://github.com/pytest-dev/pytest/issues/6116): Added [`--co`] as a synonym to [`--collect-only`].

-   [#6148](https://github.com/pytest-dev/pytest/issues/6148): [`atomicwrites`] is now only used on Windows, fixing a performance regression with assertion rewriting on Unix.

-   [#6152](https://github.com/pytest-dev/pytest/issues/6152): Now parametrization will use the [`__name__`] attribute of any object for the id, if present. Previously it would only use [`__name__`] for functions and classes.

-   [#6176](https://github.com/pytest-dev/pytest/issues/6176): Improved failure reporting with pytester's [`Hookrecorder.assertoutcome`].

-   [#6181](https://github.com/pytest-dev/pytest/issues/6181): The reason for a stopped session, e.g. with [`--maxfail`] / [`-x`], now gets reported in the test summary.

-   [#6206](https://github.com/pytest-dev/pytest/issues/6206): Improved [`cache.set`] robustness and performance.

### Bug Fixes[¶](#id683 "Link to this heading")

-   [#2049](https://github.com/pytest-dev/pytest/issues/2049): Fixed [`--setup-plan`] showing inaccurate information about fixture lifetimes.

-   [#2548](https://github.com/pytest-dev/pytest/issues/2548): Fixed line offset mismatch of skipped tests in terminal summary.

-   [#6039](https://github.com/pytest-dev/pytest/issues/6039): The [`PytestDoctestRunner`] is now properly invalidated when unconfiguring the doctest plugin.

    This is important when used with [`pytester`]'s [`runpytest_inprocess`].

-   [#6047](https://github.com/pytest-dev/pytest/issues/6047): BaseExceptions are now handled in [`saferepr`], which includes [`pytest.fail.Exception`] etc.

-   [#6074](https://github.com/pytest-dev/pytest/issues/6074): pytester: fixed order of arguments in [`rm_rf`] warning when cleaning up temporary directories, and do not emit warnings for errors with [`os.open`].

-   [#6189](https://github.com/pytest-dev/pytest/issues/6189): Fixed result of [`getmodpath`] method.

### Trivial/Internal Changes[¶](#id684 "Link to this heading")

-   [#4901](https://github.com/pytest-dev/pytest/issues/4901): [`RunResult`] from [`pytester`] now displays the mnemonic of the [`ret`] attribute when it is a valid [`pytest.ExitCode`] value.

## pytest 5.2.4 (2019-11-15)[¶](#pytest-5-2-4-2019-11-15 "Link to this heading")

### Bug Fixes[¶](#id685 "Link to this heading")

-   [#6194](https://github.com/pytest-dev/pytest/issues/6194): Fix incorrect discovery of non-test [`__init__.py`] files.

-   [#6197](https://github.com/pytest-dev/pytest/issues/6197): Revert "The first test in a package ([`__init__.py`]) marked with [`@pytest.mark.skip`] is now correctly skipped.".

## pytest 5.2.3 (2019-11-14)[¶](#pytest-5-2-3-2019-11-14 "Link to this heading")

### Bug Fixes[¶](#id686 "Link to this heading")

-   [#5830](https://github.com/pytest-dev/pytest/issues/5830): The first test in a package ([`__init__.py`]) marked with [`@pytest.mark.skip`] is now correctly skipped.

-   [#6099](https://github.com/pytest-dev/pytest/issues/6099): Fix [`--trace`] when used with parametrized functions.

-   [#6183](https://github.com/pytest-dev/pytest/issues/6183): Using [`request`] as a parameter name in [`@pytest.mark.parametrize`] now produces a more user-friendly error.

## pytest 5.2.2 (2019-10-24)[¶](#pytest-5-2-2-2019-10-24 "Link to this heading")

### Bug Fixes[¶](#id687 "Link to this heading")

-   [#5206](https://github.com/pytest-dev/pytest/issues/5206): Fix [`--nf`] to not forget about known nodeids with partial test selection.

-   [#5906](https://github.com/pytest-dev/pytest/issues/5906): Fix crash with [`KeyboardInterrupt`] during [`--setup-show`].

-   [#5946](https://github.com/pytest-dev/pytest/issues/5946): Fixed issue when parametrizing fixtures with numpy arrays (and possibly other sequence-like types).

-   [#6044](https://github.com/pytest-dev/pytest/issues/6044): Properly ignore [`FileNotFoundError`] exceptions when trying to remove old temporary directories, for instance when multiple processes try to remove the same directory (common with [`pytest-xdist`] for example).

## pytest 5.2.1 (2019-10-06)[¶](#pytest-5-2-1-2019-10-06 "Link to this heading")

### Bug Fixes[¶](#id688 "Link to this heading")

-   [#5902](https://github.com/pytest-dev/pytest/issues/5902): Fix warnings about deprecated [`cmp`] attribute in [`attrs>=19.2`].

## pytest 5.2.0 (2019-09-28)[¶](#pytest-5-2-0-2019-09-28 "Link to this heading")

### Deprecations[¶](#id689 "Link to this heading")

-   [#1682](https://github.com/pytest-dev/pytest/issues/1682): Passing arguments to pytest.fixture() as positional arguments is deprecated - pass them as a keyword argument instead.

### Features[¶](#id690 "Link to this heading")

-   [#1682](https://github.com/pytest-dev/pytest/issues/1682): The [`scope`] parameter of [`@pytest.fixture`] can now be a callable that receives the fixture name and the [`config`] object as keyword-only parameters. See [[the docs]](how-to/fixtures.html#dynamic-scope) for more information.

-   [#5764](https://github.com/pytest-dev/pytest/issues/5764): New behavior of the [`--pastebin`] option: failures to connect to the pastebin server are reported, without failing the pytest run

### Bug Fixes[¶](#id691 "Link to this heading")

-   [#5806](https://github.com/pytest-dev/pytest/issues/5806): Fix "lexer" being used when uploading to bpaste.net from [`--pastebin`] to "text".

-   [#5884](https://github.com/pytest-dev/pytest/issues/5884): Fix [`--setup-only`] and [`--setup-show`] for custom pytest items.

### Trivial/Internal Changes[¶](#id692 "Link to this heading")

-   [#5056](https://github.com/pytest-dev/pytest/issues/5056): The HelpFormatter uses [`py.io.get_terminal_width`] for better width detection.

## pytest 5.1.3 (2019-09-18)[¶](#pytest-5-1-3-2019-09-18 "Link to this heading")

### Bug Fixes[¶](#id693 "Link to this heading")

-   [#5807](https://github.com/pytest-dev/pytest/issues/5807): Fix pypy3.6 (nightly) on windows.

-   [#5811](https://github.com/pytest-dev/pytest/issues/5811): Handle [`--fulltrace`] correctly with [`pytest.raises`].

-   [#5819](https://github.com/pytest-dev/pytest/issues/5819): Windows: Fix regression with conftest whose qualified name contains uppercase characters (introduced by #5792).

## pytest 5.1.2 (2019-08-30)[¶](#pytest-5-1-2-2019-08-30 "Link to this heading")

### Bug Fixes[¶](#id694 "Link to this heading")

-   [#2270](https://github.com/pytest-dev/pytest/issues/2270): Fixed [`self`] reference in function-scoped fixtures defined plugin classes: previously [`self`] would be a reference to a *test* class, not the *plugin* class.

-   [#570](https://github.com/pytest-dev/pytest/issues/570): Fixed long standing issue where fixture scope was not respected when indirect fixtures were used during parametrization.

-   [#5782](https://github.com/pytest-dev/pytest/issues/5782): Fix decoding error when printing an error response from [`--pastebin`].

-   [#5786](https://github.com/pytest-dev/pytest/issues/5786): Chained exceptions in test and collection reports are now correctly serialized, allowing plugins like [`pytest-xdist`] to display them properly.

-   [#5792](https://github.com/pytest-dev/pytest/issues/5792): Windows: Fix error that occurs in certain circumstances when loading [`conftest.py`] from a working directory that has casing other than the one stored in the filesystem (e.g., [`c:\test`] instead of [`C:\test`]).

## pytest 5.1.1 (2019-08-20)[¶](#pytest-5-1-1-2019-08-20 "Link to this heading")

### Bug Fixes[¶](#id695 "Link to this heading")

-   [#5751](https://github.com/pytest-dev/pytest/issues/5751): Fixed [`TypeError`] when importing pytest on Python 3.5.0 and 3.5.1.

## pytest 5.1.0 (2019-08-15)[¶](#pytest-5-1-0-2019-08-15 "Link to this heading")

### Removals[¶](#removals "Link to this heading")

-   [#5180](https://github.com/pytest-dev/pytest/issues/5180): As per our policy, the following features have been deprecated in the 4.X series and are now removed:

    -   [`Request.getfuncargvalue`]: use [`Request.getfixturevalue`] instead.

    -   [`pytest.raises`] and [`pytest.warns`] no longer support strings as the second argument.

    -   [`message`] parameter of [`pytest.raises`].

    -   [`pytest.raises`], [`pytest.warns`] and [`ParameterSet.param`] now use native keyword-only syntax. This might change the exception message from previous versions, but they still raise [`TypeError`] on unknown keyword arguments as before.

    -   [`pytest.config`] global variable.

    -   [`tmpdir_factory.ensuretemp`] method.

    -   [`pytest_logwarning`] hook.

    -   [`RemovedInPytest4Warning`] warning type.

    -   [`request`] is now a reserved name for fixtures.

    For more information consult [[Deprecations and Removals]](deprecations.html) in the docs.

-   [#5565](https://github.com/pytest-dev/pytest/issues/5565): Removed unused support code for [unittest2](https://pypi.org/project/unittest2).

    The [`unittest2`] backport module is no longer necessary since Python 3.3+, and the small amount of code in pytest to support it also doesn't seem to be used: after removed, all tests still pass unchanged.

    Although our policy is to introduce a deprecation period before removing any features or support for third party libraries, because this code is apparently not used at all (even if [`unittest2`] is used by a test suite executed by pytest), it was decided to remove it in this release.

    If you experience a regression because of this, please [file an issue](https://github.com/pytest-dev/pytest/issues/new).

-   [#5615](https://github.com/pytest-dev/pytest/issues/5615): [`pytest.fail`], [`pytest.xfail`] and [`pytest.skip`] no longer support bytes for the message argument.

    This was supported for Python 2 where it was tempting to use [`"message"`] instead of [`u"message"`].

    Python 3 code is unlikely to pass [`bytes`] to these functions. If you do, please decode it to an [`str`] beforehand.

### Features[¶](#id696 "Link to this heading")

-   [#5564](https://github.com/pytest-dev/pytest/issues/5564): New [`Config.invocation_args`] attribute containing the unchanged arguments passed to [`pytest.main()`].

-   [#5576](https://github.com/pytest-dev/pytest/issues/5576): New [[NUMBER]](how-to/doctest.html#using-doctest-options) option for doctests to ignore irrelevant differences in floating-point numbers. Inspired by Sébastien Boisgérault's [numtest](https://github.com/boisgera/numtest) extension for doctest.

### Improvements[¶](#id697 "Link to this heading")

-   [#5471](https://github.com/pytest-dev/pytest/issues/5471): JUnit XML now includes a timestamp and hostname in the testsuite tag.

-   [#5707](https://github.com/pytest-dev/pytest/issues/5707): Time taken to run the test suite now includes a human-readable representation when it takes over 60 seconds, for example:

    ::: 
    ::: highlight
        ===== 2 failed in 102.70s (0:01:42) =====
    :::
    :::

### Bug Fixes[¶](#id698 "Link to this heading")

-   [#4344](https://github.com/pytest-dev/pytest/issues/4344): Fix RuntimeError/StopIteration when trying to collect package with "\_\_init\_\_.py" only.

-   [#5115](https://github.com/pytest-dev/pytest/issues/5115): Warnings issued during [`pytest_configure`] are explicitly not treated as errors, even if configured as such, because it otherwise completely breaks pytest.

-   [#5477](https://github.com/pytest-dev/pytest/issues/5477): The XML file produced by [`--junitxml`] now correctly contain a [`<testsuites>`] root element.

-   [#5524](https://github.com/pytest-dev/pytest/issues/5524): Fix issue where [`tmp_path`] and [`tmpdir`] would not remove directories containing files marked as read-only, which could lead to pytest crashing when executed a second time with the [`--basetemp`] option.

-   [#5537](https://github.com/pytest-dev/pytest/issues/5537): Replace [`importlib_metadata`] backport with [`importlib.metadata`] from the standard library on Python 3.8+.

-   [#5578](https://github.com/pytest-dev/pytest/issues/5578): Improve type checking for some exception-raising functions ([`pytest.xfail`], [`pytest.skip`], etc) so they provide better error messages when users meant to use marks (for example [`@pytest.xfail`] instead of [`@pytest.mark.xfail`]).

-   [#5606](https://github.com/pytest-dev/pytest/issues/5606): Fixed internal error when test functions were patched with objects that cannot be compared for truth values against others, like [`numpy`] arrays.

-   [#5634](https://github.com/pytest-dev/pytest/issues/5634): [`pytest.exit`] is now correctly handled in [`unittest`] cases. This makes [`unittest`] cases handle [`quit`] from pytest's pdb correctly.

-   [#5650](https://github.com/pytest-dev/pytest/issues/5650): Improved output when parsing an ini configuration file fails.

-   [#5701](https://github.com/pytest-dev/pytest/issues/5701): Fix collection of [`staticmethod`] objects defined with [`functools.partial`].

-   [#5734](https://github.com/pytest-dev/pytest/issues/5734): Skip async generator test functions, and update the warning message to refer to [`async`]` `[`def`] functions.

### Improved Documentation[¶](#id699 "Link to this heading")

-   [#5669](https://github.com/pytest-dev/pytest/issues/5669): Add docstring for [`Testdir.copy_example`].

### Trivial/Internal Changes[¶](#id700 "Link to this heading")

-   [#5095](https://github.com/pytest-dev/pytest/issues/5095): XML files of the [`xunit2`] family are now validated against the schema by pytest's own test suite to avoid future regressions.

-   [#5516](https://github.com/pytest-dev/pytest/issues/5516): Cache node splitting function which can improve collection performance in very large test suites.

-   [#5603](https://github.com/pytest-dev/pytest/issues/5603): Simplified internal [`SafeRepr`] class and removed some dead code.

-   [#5664](https://github.com/pytest-dev/pytest/issues/5664): When invoking pytest's own testsuite with [`PYTHONDONTWRITEBYTECODE=1`], the [`test_xfail_handling`] test no longer fails.

-   [#5684](https://github.com/pytest-dev/pytest/issues/5684): Replace manual handling of [`OSError.errno`] in the codebase by new [`OSError`] subclasses ([`PermissionError`], [`FileNotFoundError`], etc.).

## pytest 5.0.1 (2019-07-04)[¶](#pytest-5-0-1-2019-07-04 "Link to this heading")

### Bug Fixes[¶](#id701 "Link to this heading")

-   [#5479](https://github.com/pytest-dev/pytest/issues/5479): Improve quoting in [`raises`] match failure message.

-   [#5523](https://github.com/pytest-dev/pytest/issues/5523): Fixed using multiple short options together in the command-line (for example [`-vs`]) in Python 3.8+.

-   [#5547](https://github.com/pytest-dev/pytest/issues/5547): [`--step-wise`] now handles [`xfail(strict=True)`] markers properly.

### Improved Documentation[¶](#id702 "Link to this heading")

-   [#5517](https://github.com/pytest-dev/pytest/issues/5517): Improve "Declaring new hooks" section in chapter "Writing Plugins"

## pytest 5.0.0 (2019-06-28)[¶](#pytest-5-0-0-2019-06-28 "Link to this heading")

### Important[¶](#important "Link to this heading")

This release is a Python3.5+ only release.

For more details, see our [Python 2.7 and 3.4 support plan](https://docs.pytest.org/en/7.0.x/py27-py34-deprecation.html).

### Removals[¶](#id703 "Link to this heading")

-   [#1149](https://github.com/pytest-dev/pytest/issues/1149): Pytest no longer accepts prefixes of command-line arguments, for example typing [`pytest`]` `[`--doctest-mod`] inplace of [`--doctest-modules`]. This was previously allowed where the [`ArgumentParser`] thought it was unambiguous, but this could be incorrect due to delayed parsing of options for plugins. See for example issues [#1149](https://github.com/pytest-dev/pytest/issues/1149), [#3413](https://github.com/pytest-dev/pytest/issues/3413), and [#4009](https://github.com/pytest-dev/pytest/issues/4009).

-   [#5402](https://github.com/pytest-dev/pytest/issues/5402): **PytestDeprecationWarning are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`PytestDeprecationWarning`] now generate errors instead of warning messages.

    **The affected features will be effectively removed in pytest 5.1**, so please consult the [[Deprecations and Removals]](deprecations.html) section in the docs for directions on how to update existing code.

    In the pytest [`5.0.X`] series, it is possible to change the errors back into warnings as a stop gap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.PytestDeprecationWarning
    :::
    :::

    But this will stop working when pytest [`5.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#5402](https://github.com/pytest-dev/pytest/issues/5402).

-   [#5412](https://github.com/pytest-dev/pytest/issues/5412): [`ExceptionInfo`] objects (returned by [`pytest.raises`]) now have the same [`str`] representation as [`repr`], which avoids some confusion when users use [`print(e)`] to inspect the object.

    This means code like:

    ::: 
    ::: highlight
        with pytest.raises(SomeException) as e:
            ...
        assert "some message" in str(e)
    :::
    :::

    Needs to be changed to:

    ::: 
    ::: highlight
        with pytest.raises(SomeException) as e:
            ...
        assert "some message" in str(e.value)
    :::
    :::

### Deprecations[¶](#id704 "Link to this heading")

-   [#4488](https://github.com/pytest-dev/pytest/issues/4488): The removal of the [`--result-log`] option and module has been postponed to (tentatively) pytest 6.0 as the team has not yet got around to implement a good alternative for it.

-   [#466](https://github.com/pytest-dev/pytest/issues/466): The [`funcargnames`] attribute has been an alias for [`fixturenames`] since pytest 2.3, and is now deprecated in code too.

### Features[¶](#id705 "Link to this heading")

-   [#3457](https://github.com/pytest-dev/pytest/issues/3457): New [[`pytest_assertion_pass`]](reference/reference.html#std-hook-pytest_assertion_pass) hook, called with context information when an assertion *passes*.

    This hook is still **experimental** so use it with caution.

-   [#5440](https://github.com/pytest-dev/pytest/issues/5440): The [[`faulthandler`]](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "(in Python v3.14)") standard library module is now enabled by default to help users diagnose crashes in C modules.

    This functionality was provided by integrating the external [pytest-faulthandler](https://github.com/pytest-dev/pytest-faulthandler) plugin into the core, so users should remove that plugin from their requirements if used.

    For more information see the docs: [[Fault Handler]](how-to/failures.html#faulthandler).

-   [#5452](https://github.com/pytest-dev/pytest/issues/5452): When warnings are configured as errors, pytest warnings now appear as originating from [`pytest.`] instead of the internal [`_pytest.warning_types.`] module.

-   [#5125](https://github.com/pytest-dev/pytest/issues/5125): [`Session.exitcode`] values are now coded in [`pytest.ExitCode`], an [`IntEnum`]. This makes the exit code available for consumer code and are more explicit other than just documentation. User defined exit codes are still valid, but should be used with caution.

    The team doesn't expect this change to break test suites or plugins in general, except in esoteric/specific scenarios.

    **pytest-xdist** users should upgrade to [`1.29.0`] or later, as [`pytest-xdist`] required a compatibility fix because of this change.

### Bug Fixes[¶](#id706 "Link to this heading")

-   [#1403](https://github.com/pytest-dev/pytest/issues/1403): Switch from [`imp`] to [`importlib`].

-   [#1671](https://github.com/pytest-dev/pytest/issues/1671): The name of the [`.pyc`] files cached by the assertion writer now includes the pytest version to avoid stale caches.

-   [#2761](https://github.com/pytest-dev/pytest/issues/2761): Honor [][**PEP 235**](https://peps.python.org/pep-0235/) on case-insensitive file systems.

-   [#5078](https://github.com/pytest-dev/pytest/issues/5078): Test module is no longer double-imported when using [`--pyargs`].

-   [#5260](https://github.com/pytest-dev/pytest/issues/5260): Improved comparison of byte strings.

    When comparing bytes, the assertion message used to show the byte numeric value when showing the differences:

    ::: 
    ::: highlight
            def test():
        >       assert b'spam' == b'eggs'
        E       AssertionError: assert b'spam' == b'eggs'
        E         At index 0 diff: 115 != 101
        E         Use -v to get the full diff
    :::
    :::

    It now shows the actual ascii representation instead, which is often more useful:

    ::: 
    ::: highlight
            def test():
        >       assert b'spam' == b'eggs'
        E       AssertionError: assert b'spam' == b'eggs'
        E         At index 0 diff: b's' != b'e'
        E         Use -v to get the full diff
    :::
    :::

-   [#5335](https://github.com/pytest-dev/pytest/issues/5335): Colorize level names when the level in the logging format is formatted using '%(levelname).Xs' (truncated fixed width alignment), where X is an integer.

-   [#5354](https://github.com/pytest-dev/pytest/issues/5354): Fix [`pytest.mark.parametrize`] when the argvalues is an iterator.

-   [#5370](https://github.com/pytest-dev/pytest/issues/5370): Revert unrolling of [`all()`] to fix [`NameError`] on nested comprehensions.

-   [#5371](https://github.com/pytest-dev/pytest/issues/5371): Revert unrolling of [`all()`] to fix incorrect handling of generators with [`if`].

-   [#5372](https://github.com/pytest-dev/pytest/issues/5372): Revert unrolling of [`all()`] to fix incorrect assertion when using [`all()`] in an expression.

-   [#5383](https://github.com/pytest-dev/pytest/issues/5383): [`-q`] has again an impact on the style of the collected items ([`--collect-only`]) when [`--log-cli-level`] is used.

-   [#5389](https://github.com/pytest-dev/pytest/issues/5389): Fix regressions of [#5063](https://github.com/pytest-dev/pytest/pull/5063) for [`importlib_metadata.PathDistribution`] which have their [`files`] attribute being [`None`].

-   [#5390](https://github.com/pytest-dev/pytest/issues/5390): Fix regression where the [`obj`] attribute of [`TestCase`] items was no longer bound to methods.

-   [#5404](https://github.com/pytest-dev/pytest/issues/5404): Emit a warning when attempting to unwrap a broken object raises an exception, for easier debugging ([#5080](https://github.com/pytest-dev/pytest/issues/5080)).

-   [#5432](https://github.com/pytest-dev/pytest/issues/5432): Prevent "already imported" warnings from assertion rewriter when invoking pytest in-process multiple times.

-   [#5433](https://github.com/pytest-dev/pytest/issues/5433): Fix assertion rewriting in packages ([`__init__.py`]).

-   [#5444](https://github.com/pytest-dev/pytest/issues/5444): Fix [`--stepwise`] mode when the first file passed on the command-line fails to collect.

-   [#5482](https://github.com/pytest-dev/pytest/issues/5482): Fix bug introduced in 4.6.0 causing collection errors when passing more than 2 positional arguments to [`pytest.mark.parametrize`].

-   [#5505](https://github.com/pytest-dev/pytest/issues/5505): Fix crash when discovery fails while using [`-p`]` `[`no:terminal`].

### Improved Documentation[¶](#id707 "Link to this heading")

-   [#5315](https://github.com/pytest-dev/pytest/issues/5315): Expand docs on mocking classes and dictionaries with [`monkeypatch`].

-   [#5416](https://github.com/pytest-dev/pytest/issues/5416): Fix PytestUnknownMarkWarning in run/skip example.

## pytest 4.6.11 (2020-06-04)[¶](#pytest-4-6-11-2020-06-04 "Link to this heading")

### Bug Fixes[¶](#id708 "Link to this heading")

-   [#6334](https://github.com/pytest-dev/pytest/issues/6334): Fix summary entries appearing twice when [`f/F`] and [`s/S`] report chars were used at the same time in the [`-r`] command-line option (for example [`-rFf`]).

    The upper case variants were never documented and the preferred form should be the lower case.

-   [#7310](https://github.com/pytest-dev/pytest/issues/7310): Fix [`UnboundLocalError:`]` `[`local`]` `[`variable`]` `[`'letter'`]` `[`referenced`]` `[`before`]` `[`assignment`] in [`_pytest.terminal.pytest_report_teststatus()`] when plugins return report objects in an unconventional state.

    This was making [`pytest_report_teststatus()`] skip entering if-block branches that declare the [`letter`] variable.

    The fix was to set the initial value of the [`letter`] before the if-block cascade so that it always has a value.

## pytest 4.6.10 (2020-05-08)[¶](#pytest-4-6-10-2020-05-08 "Link to this heading")

### Features[¶](#id709 "Link to this heading")

-   [#6870](https://github.com/pytest-dev/pytest/issues/6870): New [`Config.invocation_args`] attribute containing the unchanged arguments passed to [`pytest.main()`].

    Remark: while this is technically a new feature and according to our [policy](https://docs.pytest.org/en/7.0.x/py27-py34-deprecation.html#what-goes-into-4-6-x-releases) it should not have been backported, we have opened an exception in this particular case because it fixes a serious interaction with [`pytest-xdist`], so it can also be considered a bugfix.

### Trivial/Internal Changes[¶](#id710 "Link to this heading")

-   [#6404](https://github.com/pytest-dev/pytest/issues/6404): Remove usage of [`parser`] module, deprecated in Python 3.9.

## pytest 4.6.9 (2020-01-04)[¶](#pytest-4-6-9-2020-01-04 "Link to this heading")

### Bug Fixes[¶](#id711 "Link to this heading")

-   [#6301](https://github.com/pytest-dev/pytest/issues/6301): Fix assertion rewriting for egg-based distributions and [`editable`] installs ([`pip`]` `[`install`]` `[`--editable`]).

## pytest 4.6.8 (2019-12-19)[¶](#pytest-4-6-8-2019-12-19 "Link to this heading")

### Features[¶](#id712 "Link to this heading")

-   [#5471](https://github.com/pytest-dev/pytest/issues/5471): JUnit XML now includes a timestamp and hostname in the testsuite tag.

### Bug Fixes[¶](#id713 "Link to this heading")

-   [#5430](https://github.com/pytest-dev/pytest/issues/5430): junitxml: Logs for failed test are now passed to junit report in case the test fails during call phase.

### Trivial/Internal Changes[¶](#id714 "Link to this heading")

-   [#6345](https://github.com/pytest-dev/pytest/issues/6345): Pin [`colorama`] to [`0.4.1`] only for Python 3.4 so newer Python versions can still receive colorama updates.

## pytest 4.6.7 (2019-12-05)[¶](#pytest-4-6-7-2019-12-05 "Link to this heading")

### Bug Fixes[¶](#id715 "Link to this heading")

-   [#5477](https://github.com/pytest-dev/pytest/issues/5477): The XML file produced by [`--junitxml`] now correctly contain a [`<testsuites>`] root element.

-   [#6044](https://github.com/pytest-dev/pytest/issues/6044): Properly ignore [`FileNotFoundError`] ([`OSError.errno`]` `[`==`]` `[`NOENT`] in Python 2) exceptions when trying to remove old temporary directories, for instance when multiple processes try to remove the same directory (common with [`pytest-xdist`] for example).

## pytest 4.6.6 (2019-10-11)[¶](#pytest-4-6-6-2019-10-11 "Link to this heading")

### Bug Fixes[¶](#id716 "Link to this heading")

-   [#5523](https://github.com/pytest-dev/pytest/issues/5523): Fixed using multiple short options together in the command-line (for example [`-vs`]) in Python 3.8+.

-   [#5537](https://github.com/pytest-dev/pytest/issues/5537): Replace [`importlib_metadata`] backport with [`importlib.metadata`] from the standard library on Python 3.8+.

-   [#5806](https://github.com/pytest-dev/pytest/issues/5806): Fix "lexer" being used when uploading to bpaste.net from [`--pastebin`] to "text".

-   [#5902](https://github.com/pytest-dev/pytest/issues/5902): Fix warnings about deprecated [`cmp`] attribute in [`attrs>=19.2`].

### Trivial/Internal Changes[¶](#id717 "Link to this heading")

-   [#5801](https://github.com/pytest-dev/pytest/issues/5801): Fixes python version checks (detected by [`flake8-2020`]) in case python4 becomes a thing.

## pytest 4.6.5 (2019-08-05)[¶](#pytest-4-6-5-2019-08-05 "Link to this heading")

### Bug Fixes[¶](#id718 "Link to this heading")

-   [#4344](https://github.com/pytest-dev/pytest/issues/4344): Fix RuntimeError/StopIteration when trying to collect package with "\_\_init\_\_.py" only.

-   [#5478](https://github.com/pytest-dev/pytest/issues/5478): Fix encode error when using unicode strings in exceptions with [`pytest.raises`].

-   [#5524](https://github.com/pytest-dev/pytest/issues/5524): Fix issue where [`tmp_path`] and [`tmpdir`] would not remove directories containing files marked as read-only, which could lead to pytest crashing when executed a second time with the [`--basetemp`] option.

-   [#5547](https://github.com/pytest-dev/pytest/issues/5547): [`--step-wise`] now handles [`xfail(strict=True)`] markers properly.

-   [#5650](https://github.com/pytest-dev/pytest/issues/5650): Improved output when parsing an ini configuration file fails.

## pytest 4.6.4 (2019-06-28)[¶](#pytest-4-6-4-2019-06-28 "Link to this heading")

### Bug Fixes[¶](#id719 "Link to this heading")

-   [#5404](https://github.com/pytest-dev/pytest/issues/5404): Emit a warning when attempting to unwrap a broken object raises an exception, for easier debugging ([#5080](https://github.com/pytest-dev/pytest/issues/5080)).

-   [#5444](https://github.com/pytest-dev/pytest/issues/5444): Fix [`--stepwise`] mode when the first file passed on the command-line fails to collect.

-   [#5482](https://github.com/pytest-dev/pytest/issues/5482): Fix bug introduced in 4.6.0 causing collection errors when passing more than 2 positional arguments to [`pytest.mark.parametrize`].

-   [#5505](https://github.com/pytest-dev/pytest/issues/5505): Fix crash when discovery fails while using [`-p`]` `[`no:terminal`].

## pytest 4.6.3 (2019-06-11)[¶](#pytest-4-6-3-2019-06-11 "Link to this heading")

### Bug Fixes[¶](#id720 "Link to this heading")

-   [#5383](https://github.com/pytest-dev/pytest/issues/5383): [`-q`] has again an impact on the style of the collected items ([`--collect-only`]) when [`--log-cli-level`] is used.

-   [#5389](https://github.com/pytest-dev/pytest/issues/5389): Fix regressions of [#5063](https://github.com/pytest-dev/pytest/pull/5063) for [`importlib_metadata.PathDistribution`] which have their [`files`] attribute being [`None`].

-   [#5390](https://github.com/pytest-dev/pytest/issues/5390): Fix regression where the [`obj`] attribute of [`TestCase`] items was no longer bound to methods.

## pytest 4.6.2 (2019-06-03)[¶](#pytest-4-6-2-2019-06-03 "Link to this heading")

### Bug Fixes[¶](#id721 "Link to this heading")

-   [#5370](https://github.com/pytest-dev/pytest/issues/5370): Revert unrolling of [`all()`] to fix [`NameError`] on nested comprehensions.

-   [#5371](https://github.com/pytest-dev/pytest/issues/5371): Revert unrolling of [`all()`] to fix incorrect handling of generators with [`if`].

-   [#5372](https://github.com/pytest-dev/pytest/issues/5372): Revert unrolling of [`all()`] to fix incorrect assertion when using [`all()`] in an expression.

## pytest 4.6.1 (2019-06-02)[¶](#pytest-4-6-1-2019-06-02 "Link to this heading")

### Bug Fixes[¶](#id722 "Link to this heading")

-   [#5354](https://github.com/pytest-dev/pytest/issues/5354): Fix [`pytest.mark.parametrize`] when the argvalues is an iterator.

-   [#5358](https://github.com/pytest-dev/pytest/issues/5358): Fix assertion rewriting of [`all()`] calls to deal with non-generators.

## pytest 4.6.0 (2019-05-31)[¶](#pytest-4-6-0-2019-05-31 "Link to this heading")

### Important[¶](#id723 "Link to this heading")

The [`4.6.X`] series will be the last series to support **Python 2 and Python 3.4**.

For more details, see our [Python 2.7 and 3.4 support plan](https://docs.pytest.org/en/7.0.x/py27-py34-deprecation.html).

### Features[¶](#id725 "Link to this heading")

-   [#4559](https://github.com/pytest-dev/pytest/issues/4559): Added the [`junit_log_passing_tests`] ini value which can be used to enable or disable logging of passing test output in the Junit XML file.

-   [#4956](https://github.com/pytest-dev/pytest/issues/4956): pytester's [`testdir.spawn`] uses [`tmpdir`] as HOME/USERPROFILE directory.

-   [#5062](https://github.com/pytest-dev/pytest/issues/5062): Unroll calls to [`all`] to full for-loops with assertion rewriting for better failure messages, especially when using Generator Expressions.

-   [#5063](https://github.com/pytest-dev/pytest/issues/5063): Switch from [`pkg_resources`] to [`importlib-metadata`] for entrypoint detection for improved performance and import time.

-   [#5091](https://github.com/pytest-dev/pytest/issues/5091): The output for ini options in [`--help`] has been improved.

-   [#5269](https://github.com/pytest-dev/pytest/issues/5269): [`pytest.importorskip`] includes the [`ImportError`] now in the default [`reason`].

-   [#5311](https://github.com/pytest-dev/pytest/issues/5311): Captured logs that are output for each failing test are formatted using the ColoredLevelFormatter.

-   [#5312](https://github.com/pytest-dev/pytest/issues/5312): Improved formatting of multiline log messages in Python 3.

### Bug Fixes[¶](#id726 "Link to this heading")

-   [#2064](https://github.com/pytest-dev/pytest/issues/2064): The debugging plugin imports the wrapped [`Pdb`] class ([`--pdbcls`]) on-demand now.

-   [#4908](https://github.com/pytest-dev/pytest/issues/4908): The [`pytest_enter_pdb`] hook gets called with post-mortem ([`--pdb`]).

-   [#5036](https://github.com/pytest-dev/pytest/issues/5036): Fix issue where fixtures dependent on other parametrized fixtures would be erroneously parametrized.

-   [#5256](https://github.com/pytest-dev/pytest/issues/5256): Handle internal error due to a lone surrogate unicode character not being representable in Jython.

-   [#5257](https://github.com/pytest-dev/pytest/issues/5257): Ensure that [`sys.stdout.mode`] does not include [`'b'`] as it is a text stream.

-   [#5278](https://github.com/pytest-dev/pytest/issues/5278): Pytest's internal python plugin can be disabled using [`-p`]` `[`no:python`] again.

-   [#5286](https://github.com/pytest-dev/pytest/issues/5286): Fix issue with [`disable_test_id_escaping_and_forfeit_all_rights_to_community_support`] option not working when using a list of test IDs in parametrized tests.

-   [#5330](https://github.com/pytest-dev/pytest/issues/5330): Show the test module being collected when emitting [`PytestCollectionWarning`] messages for test classes with [`__init__`] and [`__new__`] methods to make it easier to pin down the problem.

-   [#5333](https://github.com/pytest-dev/pytest/issues/5333): Fix regression in 4.5.0 with [`--lf`] not re-running all tests with known failures from non-selected tests.

### Improved Documentation[¶](#id727 "Link to this heading")

-   [#5250](https://github.com/pytest-dev/pytest/issues/5250): Expand docs on use of [`setenv`] and [`delenv`] with [`monkeypatch`].

## pytest 4.5.0 (2019-05-11)[¶](#pytest-4-5-0-2019-05-11 "Link to this heading")

### Features[¶](#id728 "Link to this heading")

-   [#4826](https://github.com/pytest-dev/pytest/issues/4826): A warning is now emitted when unknown marks are used as a decorator. This is often due to a typo, which can lead to silently broken tests.

-   [#4907](https://github.com/pytest-dev/pytest/issues/4907): Show XFail reason as part of JUnitXML message field.

-   [#5013](https://github.com/pytest-dev/pytest/issues/5013): Messages from crash reports are displayed within test summaries now, truncated to the terminal width.

-   [#5023](https://github.com/pytest-dev/pytest/issues/5023): New flag [`--strict-markers`] that triggers an error when unknown markers (e.g. those not registered using the [[`markers`]](reference/reference.html#confval-markers) option in the configuration file) are used in the test suite.

    The existing [`--strict`] option has the same behavior currently, but can be augmented in the future for additional checks.

-   [#5026](https://github.com/pytest-dev/pytest/issues/5026): Assertion failure messages for sequences and dicts contain the number of different items now.

-   [#5034](https://github.com/pytest-dev/pytest/issues/5034): Improve reporting with [`--lf`] and [`--ff`] (run-last-failure).

-   [#5035](https://github.com/pytest-dev/pytest/issues/5035): The [`--cache-show`] option/action accepts an optional glob to show only matching cache entries.

-   [#5059](https://github.com/pytest-dev/pytest/issues/5059): Standard input (stdin) can be given to pytester's [`Testdir.run()`] and [`Testdir.popen()`].

-   [#5068](https://github.com/pytest-dev/pytest/issues/5068): The [`-r`] option learnt about [`A`] to display all reports (including passed ones) in the short test summary.

-   [#5108](https://github.com/pytest-dev/pytest/issues/5108): The short test summary is displayed after passes with output ([`-rP`]).

-   [#5172](https://github.com/pytest-dev/pytest/issues/5172): The [`--last-failed`] ([`--lf`]) option got smarter and will now skip entire files if all tests of that test file have passed in previous runs, greatly speeding up collection.

-   [#5177](https://github.com/pytest-dev/pytest/issues/5177): Introduce new specific warning [`PytestWarning`] subclasses to make it easier to filter warnings based on the class, rather than on the message. The new subclasses are:

    -   [`PytestAssertRewriteWarning`]

    -   [`PytestCacheWarning`]

    -   [`PytestCollectionWarning`]

    -   [`PytestConfigWarning`]

    -   [`PytestUnhandledCoroutineWarning`]

    -   [`PytestUnknownMarkWarning`]

-   [#5202](https://github.com/pytest-dev/pytest/issues/5202): New [`record_testsuite_property`] session-scoped fixture allows users to log [`<property>`] tags at the [`testsuite`] level with the [`junitxml`] plugin.

    The generated XML is compatible with the latest xunit standard, contrary to the properties recorded by [`record_property`] and [`record_xml_attribute`].

-   [#5214](https://github.com/pytest-dev/pytest/issues/5214): The default logging format has been changed to improve readability. Here is an example of a previous logging message:

    ::: 
    ::: highlight
        test_log_cli_enabled_disabled.py    3 CRITICAL critical message logged by test
    :::
    :::

    This has now become:

    ::: 
    ::: highlight
        CRITICAL root:test_log_cli_enabled_disabled.py:3 critical message logged by test
    :::
    :::

    The formatting can be changed through the [[`log_format`]](reference/reference.html#confval-log_format) configuration option.

-   [#5220](https://github.com/pytest-dev/pytest/issues/5220): [`--fixtures`] now also shows fixture scope for scopes other than [`"function"`].

### Bug Fixes[¶](#id729 "Link to this heading")

-   [#5113](https://github.com/pytest-dev/pytest/issues/5113): Deselected items from plugins using [`pytest_collect_modifyitems`] as a hookwrapper are correctly reported now.

-   [#5144](https://github.com/pytest-dev/pytest/issues/5144): With usage errors [`exitstatus`] is set to [`EXIT_USAGEERROR`] in the [`pytest_sessionfinish`] hook now as expected.

-   [#5235](https://github.com/pytest-dev/pytest/issues/5235): [`outcome.exit`] is not used with [`EOF`] in the pdb wrapper anymore, but only with [`quit`].

### Improved Documentation[¶](#id730 "Link to this heading")

-   [#4935](https://github.com/pytest-dev/pytest/issues/4935): Expand docs on registering marks and the effect of [`--strict`].

### Trivial/Internal Changes[¶](#id731 "Link to this heading")

-   [#4942](https://github.com/pytest-dev/pytest/issues/4942): [`logging.raiseExceptions`] is not set to [`False`] anymore.

-   [#5013](https://github.com/pytest-dev/pytest/issues/5013): pytest now depends on [wcwidth](https://pypi.org/project/wcwidth) to properly track unicode character sizes for more precise terminal output.

-   [#5059](https://github.com/pytest-dev/pytest/issues/5059): pytester's [`Testdir.popen()`] uses [`stdout`] and [`stderr`] via keyword arguments with defaults now ([`subprocess.PIPE`]).

-   [#5069](https://github.com/pytest-dev/pytest/issues/5069): The code for the short test summary in the terminal was moved to the terminal plugin.

-   [#5082](https://github.com/pytest-dev/pytest/issues/5082): Improved validation of kwargs for various methods in the pytester plugin.

-   [#5202](https://github.com/pytest-dev/pytest/issues/5202): [`record_property`] now emits a [`PytestWarning`] when used with [`junit_family=xunit2`]: the fixture generates [`property`] tags as children of [`testcase`], which is not permitted according to the most [recent schema](https://github.com/jenkinsci/xunit-plugin/blob/master/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd).

-   [#5239](https://github.com/pytest-dev/pytest/issues/5239): Pin [`pluggy`] to [`<`]` `[`1.0`] so we don't update to [`1.0`] automatically when it gets released: there are planned breaking changes, and we want to ensure pytest properly supports [`pluggy`]` `[`1.0`].

## pytest 4.4.2 (2019-05-08)[¶](#pytest-4-4-2-2019-05-08 "Link to this heading")

### Bug Fixes[¶](#id732 "Link to this heading")

-   [#5089](https://github.com/pytest-dev/pytest/issues/5089): Fix crash caused by error in [`__repr__`] function with both [`showlocals`] and verbose output enabled.

-   [#5139](https://github.com/pytest-dev/pytest/issues/5139): Eliminate core dependency on 'terminal' plugin.

-   [#5229](https://github.com/pytest-dev/pytest/issues/5229): Require [`pluggy>=0.11.0`] which reverts a dependency to [`importlib-metadata`] added in [`0.10.0`]. The [`importlib-metadata`] package cannot be imported when installed as an egg and causes issues when relying on [`setup.py`] to install test dependencies.

### Improved Documentation[¶](#id733 "Link to this heading")

-   [#5171](https://github.com/pytest-dev/pytest/issues/5171): Doc: [`pytest_ignore_collect`], [`pytest_collect_directory`], [`pytest_collect_file`] and [`pytest_pycollect_makemodule`] hooks's 'path' parameter documented type is now [`py.path.local`]

-   [#5188](https://github.com/pytest-dev/pytest/issues/5188): Improve help for [`--runxfail`] flag.

### Trivial/Internal Changes[¶](#id734 "Link to this heading")

-   [#5182](https://github.com/pytest-dev/pytest/issues/5182): Removed internal and unused [`_pytest.deprecated.MARK_INFO_ATTRIBUTE`].

## pytest 4.4.1 (2019-04-15)[¶](#pytest-4-4-1-2019-04-15 "Link to this heading")

### Bug Fixes[¶](#id735 "Link to this heading")

-   [#5031](https://github.com/pytest-dev/pytest/issues/5031): Environment variables are properly restored when using pytester's [`testdir`] fixture.

-   [#5039](https://github.com/pytest-dev/pytest/issues/5039): Fix regression with [`--pdbcls`], which stopped working with local modules in 4.0.0.

-   [#5092](https://github.com/pytest-dev/pytest/issues/5092): Produce a warning when unknown keywords are passed to [`pytest.param(...)`].

-   [#5098](https://github.com/pytest-dev/pytest/issues/5098): Invalidate import caches with [`monkeypatch.syspath_prepend`], which is required with namespace packages being used.

## pytest 4.4.0 (2019-03-29)[¶](#pytest-4-4-0-2019-03-29 "Link to this heading")

### Features[¶](#id736 "Link to this heading")

-   [#2224](https://github.com/pytest-dev/pytest/issues/2224): [`async`] test functions are skipped and a warning is emitted when a suitable async plugin is not installed (such as [`pytest-asyncio`] or [`pytest-trio`]).

    Previously [`async`] functions would not execute at all but still be marked as "passed".

-   [#2482](https://github.com/pytest-dev/pytest/issues/2482): Include new [`disable_test_id_escaping_and_forfeit_all_rights_to_community_support`] option to disable ascii-escaping in parametrized values. This may cause a series of problems and as the name makes clear, use at your own risk.

-   [#4718](https://github.com/pytest-dev/pytest/issues/4718): The [`-p`] option can now be used to early-load plugins also by entry-point name, instead of just by module name.

    This makes it possible to early load external plugins like [`pytest-cov`] in the command-line:

    ::: 
    ::: highlight
        pytest -p pytest_cov
    :::
    :::

-   [#4855](https://github.com/pytest-dev/pytest/issues/4855): The [`--pdbcls`] option handles classes via module attributes now (e.g. [`pdb:pdb.Pdb`] with [pdbpp](https://pypi.org/project/pdbpp)), and its validation was improved.

-   [#4875](https://github.com/pytest-dev/pytest/issues/4875): The [[`testpaths`]](reference/reference.html#confval-testpaths) configuration option is now displayed next to the [`rootdir`] and [`inifile`] lines in the pytest header if the option is in effect, i.e., directories or file names were not explicitly passed in the command line.

    Also, [`inifile`] is only displayed if there's a configuration file, instead of an empty [`inifile:`] string.

-   [#4911](https://github.com/pytest-dev/pytest/issues/4911): Doctests can be skipped now dynamically using [`pytest.skip()`].

-   [#4920](https://github.com/pytest-dev/pytest/issues/4920): Internal refactorings have been made in order to make the implementation of the [pytest-subtests](https://github.com/pytest-dev/pytest-subtests) plugin possible, which adds unittest sub-test support and a new [`subtests`] fixture as discussed in [#1367](https://github.com/pytest-dev/pytest/issues/1367).

    For details on the internal refactorings, please see the details on the related PR.

-   [#4931](https://github.com/pytest-dev/pytest/issues/4931): pytester's [`LineMatcher`] asserts that the passed lines are a sequence.

-   [#4936](https://github.com/pytest-dev/pytest/issues/4936): Handle [`-p`]` `[`plug`] after [`-p`]` `[`no:plug`].

    This can be used to override a blocked plugin (e.g. in "addopts") from the command line etc.

-   [#4951](https://github.com/pytest-dev/pytest/issues/4951): Output capturing is handled correctly when only capturing via fixtures (capsys, capfs) with [`pdb.set_trace()`].

-   [#4956](https://github.com/pytest-dev/pytest/issues/4956): [`pytester`] sets [`$HOME`] and [`$USERPROFILE`] to the temporary directory during test runs.

    This ensures to not load configuration files from the real user's home directory.

-   [#4980](https://github.com/pytest-dev/pytest/issues/4980): Namespace packages are handled better with [`monkeypatch.syspath_prepend`] and [`testdir.syspathinsert`] (via [`pkg_resources.fixup_namespace_packages`]).

-   [#4993](https://github.com/pytest-dev/pytest/issues/4993): The stepwise plugin reports status information now.

-   [#5008](https://github.com/pytest-dev/pytest/issues/5008): If a [`setup.cfg`] file contains [`[tool:pytest]`] and also the no longer supported [`[pytest]`] section, pytest will use [`[tool:pytest]`] ignoring [`[pytest]`]. Previously it would unconditionally error out.

    This makes it simpler for plugins to support old pytest versions.

### Bug Fixes[¶](#id737 "Link to this heading")

-   [#1895](https://github.com/pytest-dev/pytest/issues/1895): Fix bug where fixtures requested dynamically via [`request.getfixturevalue()`] might be teardown before the requesting fixture.

-   [#4851](https://github.com/pytest-dev/pytest/issues/4851): pytester unsets [`PYTEST_ADDOPTS`] now to not use outer options with [`testdir.runpytest()`].

-   [#4903](https://github.com/pytest-dev/pytest/issues/4903): Use the correct modified time for years after 2038 in rewritten [`.pyc`] files.

-   [#4928](https://github.com/pytest-dev/pytest/issues/4928): Fix line offsets with [`ScopeMismatch`] errors.

-   [#4957](https://github.com/pytest-dev/pytest/issues/4957): [`-p`]` `[`no:plugin`] is handled correctly for default (internal) plugins now, e.g. with [`-p`]` `[`no:capture`].

    Previously they were loaded (imported) always, making e.g. the [`capfd`] fixture available.

-   [#4968](https://github.com/pytest-dev/pytest/issues/4968): The pdb [`quit`] command is handled properly when used after the [`debug`] command with [pdbpp](https://pypi.org/project/pdbpp).

-   [#4975](https://github.com/pytest-dev/pytest/issues/4975): Fix the interpretation of [`-qq`] option where it was being considered as [`-v`] instead.

-   [#4978](https://github.com/pytest-dev/pytest/issues/4978): [`outcomes.Exit`] is not swallowed in [`assertrepr_compare`] anymore.

-   [#4988](https://github.com/pytest-dev/pytest/issues/4988): Close logging's file handler explicitly when the session finishes.

-   [#5003](https://github.com/pytest-dev/pytest/issues/5003): Fix line offset with mark collection error (off by one).

### Improved Documentation[¶](#id738 "Link to this heading")

-   [#4974](https://github.com/pytest-dev/pytest/issues/4974): Update docs for [`pytest_cmdline_parse`] hook to note availability limitations

### Trivial/Internal Changes[¶](#id739 "Link to this heading")

-   [#4718](https://github.com/pytest-dev/pytest/issues/4718): [`pluggy>=0.9`] is now required.

-   [#4815](https://github.com/pytest-dev/pytest/issues/4815): [`funcsigs>=1.0`] is now required for Python 2.7.

-   [#4829](https://github.com/pytest-dev/pytest/issues/4829): Some left-over internal code related to [`yield`] tests has been removed.

-   [#4890](https://github.com/pytest-dev/pytest/issues/4890): Remove internally unused [`anypython`] fixture from the pytester plugin.

-   [#4912](https://github.com/pytest-dev/pytest/issues/4912): Remove deprecated Sphinx directive, [`add_description_unit()`], pin sphinx-removed-in to \>= 0.2.0 to support Sphinx 2.0.

-   [#4913](https://github.com/pytest-dev/pytest/issues/4913): Fix pytest tests invocation with custom [`PYTHONPATH`].

-   [#4965](https://github.com/pytest-dev/pytest/issues/4965): New [`pytest_report_to_serializable`] and [`pytest_report_from_serializable`] **experimental** hooks.

    These hooks will be used by [`pytest-xdist`], [`pytest-subtests`], and the replacement for resultlog to serialize and customize reports.

    They are experimental, meaning that their details might change or even be removed completely in future patch releases without warning.

    Feedback is welcome from plugin authors and users alike.

-   [#4987](https://github.com/pytest-dev/pytest/issues/4987): [`Collector.repr_failure`] respects the [`--tb`] option, but only defaults to [`short`] now (with [`auto`]).

## pytest 4.3.1 (2019-03-11)[¶](#pytest-4-3-1-2019-03-11 "Link to this heading")

### Bug Fixes[¶](#id740 "Link to this heading")

-   [#4810](https://github.com/pytest-dev/pytest/issues/4810): Logging messages inside [`pytest_runtest_logreport()`] are now properly captured and displayed.

-   [#4861](https://github.com/pytest-dev/pytest/issues/4861): Improve validation of contents written to captured output so it behaves the same as when capture is disabled.

-   [#4898](https://github.com/pytest-dev/pytest/issues/4898): Fix [`AttributeError:`]` `[`FixtureRequest`]` `[`has`]` `[`no`]` `[`'confg'`]` `[`attribute`] bug in [`testdir.copy_example`].

### Trivial/Internal Changes[¶](#id741 "Link to this heading")

-   [#4768](https://github.com/pytest-dev/pytest/issues/4768): Avoid pkg_resources import at the top-level.

## pytest 4.3.0 (2019-02-16)[¶](#pytest-4-3-0-2019-02-16 "Link to this heading")

### Deprecations[¶](#id742 "Link to this heading")

-   [#4724](https://github.com/pytest-dev/pytest/issues/4724): [`pytest.warns()`] now emits a warning when it receives unknown keyword arguments.

    This will be changed into an error in the future.

### Features[¶](#id743 "Link to this heading")

-   [#2753](https://github.com/pytest-dev/pytest/issues/2753): Usage errors from argparse are mapped to pytest's [`UsageError`].

-   [#3711](https://github.com/pytest-dev/pytest/issues/3711): Add the [`--ignore-glob`] parameter to exclude test-modules with Unix shell-style wildcards. Add the [[`collect_ignore_glob`]](reference/reference.html#globalvar-collect_ignore_glob) for [`conftest.py`] to exclude test-modules with Unix shell-style wildcards.

-   [#4698](https://github.com/pytest-dev/pytest/issues/4698): The warning about Python 2.7 and 3.4 not being supported in pytest 5.0 has been removed.

    In the end it was considered to be more of a nuisance than actual utility and users of those Python versions shouldn't have problems as [`pip`] will not install pytest 5.0 on those interpreters.

-   [#4707](https://github.com/pytest-dev/pytest/issues/4707): With the help of new [`set_log_path()`] method there is a way to set [`log_file`] paths from hooks.

### Bug Fixes[¶](#id744 "Link to this heading")

-   [#4651](https://github.com/pytest-dev/pytest/issues/4651): [`--help`] and [`--version`] are handled with [`UsageError`].

-   [#4782](https://github.com/pytest-dev/pytest/issues/4782): Fix [`AssertionError`] with collection of broken symlinks with packages.

## pytest 4.2.1 (2019-02-12)[¶](#pytest-4-2-1-2019-02-12 "Link to this heading")

### Bug Fixes[¶](#id745 "Link to this heading")

-   [#2895](https://github.com/pytest-dev/pytest/issues/2895): The [`pytest_report_collectionfinish`] hook now is also called with [`--collect-only`].

-   [#3899](https://github.com/pytest-dev/pytest/issues/3899): Do not raise [`UsageError`] when an imported package has a [`pytest_plugins.py`] child module.

-   [#4347](https://github.com/pytest-dev/pytest/issues/4347): Fix output capturing when using pdb++ with recursive debugging.

-   [#4592](https://github.com/pytest-dev/pytest/issues/4592): Fix handling of [`collect_ignore`] via parent [`conftest.py`].

-   [#4700](https://github.com/pytest-dev/pytest/issues/4700): Fix regression where [`setUpClass`] would always be called in subclasses even if all tests were skipped by a [`unittest.skip()`] decorator applied in the subclass.

-   [#4739](https://github.com/pytest-dev/pytest/issues/4739): Fix [`parametrize(...`]` `[`ids=<function>)`] when the function returns non-strings.

-   [#4745](https://github.com/pytest-dev/pytest/issues/4745): Fix/improve collection of args when passing in [`__init__.py`] and a test file.

-   [#4770](https://github.com/pytest-dev/pytest/issues/4770): [`more_itertools`] is now constrained to \<6.0.0 when required for Python 2.7 compatibility.

-   [#526](https://github.com/pytest-dev/pytest/issues/526): Fix "ValueError: Plugin already registered" exceptions when running in build directories that symlink to actual source.

### Improved Documentation[¶](#id746 "Link to this heading")

-   [#3899](https://github.com/pytest-dev/pytest/issues/3899): Add note to [`plugins.rst`] that [`pytest_plugins`] should not be used as a name for a user module containing plugins.

-   [#4324](https://github.com/pytest-dev/pytest/issues/4324): Document how to use [`raises`] and [`does_not_raise`] to write parametrized tests with conditional raises.

-   [#4709](https://github.com/pytest-dev/pytest/issues/4709): Document how to customize test failure messages when using [`pytest.warns`].

### Trivial/Internal Changes[¶](#id747 "Link to this heading")

-   [#4741](https://github.com/pytest-dev/pytest/issues/4741): Some verbosity related attributes of the TerminalReporter plugin are now read only properties.

## pytest 4.2.0 (2019-01-30)[¶](#pytest-4-2-0-2019-01-30 "Link to this heading")

### Features[¶](#id748 "Link to this heading")

-   [#3094](https://github.com/pytest-dev/pytest/issues/3094): [[Classic xunit-style]](how-to/xunit_setup.html) functions and methods now obey the scope of *autouse* fixtures.

    This fixes a number of surprising issues like [`setup_method`] being called before session-scoped autouse fixtures (see [#517](https://github.com/pytest-dev/pytest/issues/517) for an example).

-   [#4627](https://github.com/pytest-dev/pytest/issues/4627): Display a message at the end of the test session when running under Python 2.7 and 3.4 that pytest 5.0 will no longer support those Python versions.

-   [#4660](https://github.com/pytest-dev/pytest/issues/4660): The number of *selected* tests now are also displayed when the [`-k`] or [`-m`] flags are used.

-   [#4688](https://github.com/pytest-dev/pytest/issues/4688): [`pytest_report_teststatus`] hook now can also receive a [`config`] parameter.

-   [#4691](https://github.com/pytest-dev/pytest/issues/4691): [`pytest_terminal_summary`] hook now can also receive a [`config`] parameter.

### Bug Fixes[¶](#id749 "Link to this heading")

-   [#3547](https://github.com/pytest-dev/pytest/issues/3547): [`--junitxml`] can emit XML compatible with Jenkins xUnit. [`junit_family`] INI option accepts [`legacy|xunit1`], which produces old style output, and [`xunit2`] that conforms more strictly to [https://github.com/jenkinsci/xunit-plugin/blob/xunit-2.3.2/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd](https://github.com/jenkinsci/xunit-plugin/blob/xunit-2.3.2/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd)

-   [#4280](https://github.com/pytest-dev/pytest/issues/4280): Improve quitting from pdb, especially with [`--trace`].

    Using [`q[quit]`] after [`pdb.set_trace()`] will quit pytest also.

-   [#4402](https://github.com/pytest-dev/pytest/issues/4402): Warning summary now groups warnings by message instead of by test id.

    This makes the output more compact and better conveys the general idea of how much code is actually generating warnings, instead of how many tests call that code.

-   [#4536](https://github.com/pytest-dev/pytest/issues/4536): [`monkeypatch.delattr`] handles class descriptors like [`staticmethod`]/[`classmethod`].

-   [#4649](https://github.com/pytest-dev/pytest/issues/4649): Restore marks being considered keywords for keyword expressions.

-   [#4653](https://github.com/pytest-dev/pytest/issues/4653): [`tmp_path`] fixture and other related ones provides resolved path (a.k.a real path)

-   [#4667](https://github.com/pytest-dev/pytest/issues/4667): [`pytest_terminal_summary`] uses result from [`pytest_report_teststatus`] hook, rather than hardcoded strings.

-   [#4669](https://github.com/pytest-dev/pytest/issues/4669): Correctly handle [`unittest.SkipTest`] exception containing non-ascii characters on Python 2.

-   [#4680](https://github.com/pytest-dev/pytest/issues/4680): Ensure the [`tmpdir`] and the [`tmp_path`] fixtures are the same folder.

-   [#4681](https://github.com/pytest-dev/pytest/issues/4681): Ensure [`tmp_path`] is always a real path.

### Trivial/Internal Changes[¶](#id750 "Link to this heading")

-   [#4643](https://github.com/pytest-dev/pytest/issues/4643): Use [`a.item()`] instead of the deprecated [`np.asscalar(a)`] in [`pytest.approx`].

    [`np.asscalar`] has been [[deprecated]](https://numpy.org/doc/stable/release/1.16.0-notes.html "(in NumPy v2.3)") in [`numpy`]` `[`1.16.`].

-   [#4657](https://github.com/pytest-dev/pytest/issues/4657): Copy saferepr from pylib

-   [#4668](https://github.com/pytest-dev/pytest/issues/4668): The verbose word for expected failures in the teststatus report changes from [`xfail`] to [`XFAIL`] to be consistent with other test outcomes.

## pytest 4.1.1 (2019-01-12)[¶](#pytest-4-1-1-2019-01-12 "Link to this heading")

### Bug Fixes[¶](#id751 "Link to this heading")

-   [#2256](https://github.com/pytest-dev/pytest/issues/2256): Show full repr with [`assert`]` `[`a==b`] and [`-vv`].

-   [#3456](https://github.com/pytest-dev/pytest/issues/3456): Extend Doctest-modules to ignore mock objects.

-   [#4617](https://github.com/pytest-dev/pytest/issues/4617): Fixed [`pytest.warns`] bug when context manager is reused (e.g. multiple parametrization).

-   [#4631](https://github.com/pytest-dev/pytest/issues/4631): Don't rewrite assertion when [`__getattr__`] is broken

### Improved Documentation[¶](#id752 "Link to this heading")

-   [#3375](https://github.com/pytest-dev/pytest/issues/3375): Document that using [`setup.cfg`] may crash other tools or cause hard to track down problems because it uses a different parser than [`pytest.ini`] or [`tox.ini`] files.

### Trivial/Internal Changes[¶](#id753 "Link to this heading")

-   [#4602](https://github.com/pytest-dev/pytest/issues/4602): Uninstall [`hypothesis`] in regen tox env.

## pytest 4.1.0 (2019-01-05)[¶](#pytest-4-1-0-2019-01-05 "Link to this heading")

### Removals[¶](#id754 "Link to this heading")

-   [#2169](https://github.com/pytest-dev/pytest/issues/2169): [`pytest.mark.parametrize`]: in previous versions, errors raised by id functions were suppressed and changed into warnings. Now the exceptions are propagated, along with a pytest message informing the node, parameter value and index where the exception occurred.

-   [#3078](https://github.com/pytest-dev/pytest/issues/3078): Remove legacy internal warnings system: [`config.warn`], [`Node.warn`]. The [`pytest_logwarning`] now issues a warning when implemented.

    See our [[docs]](deprecations.html#config-warn-and-node-warn-deprecated) on information on how to update your code.

-   [#3079](https://github.com/pytest-dev/pytest/issues/3079): Removed support for yield tests - they are fundamentally broken because they don't support fixtures properly since collection and test execution were separated.

    See our [[docs]](deprecations.html#yield-tests-deprecated) on information on how to update your code.

-   [#3082](https://github.com/pytest-dev/pytest/issues/3082): Removed support for applying marks directly to values in [`@pytest.mark.parametrize`]. Use [`pytest.param`] instead.

    See our [[docs]](deprecations.html#marks-in-pytest-parametrize-deprecated) on information on how to update your code.

-   [#3083](https://github.com/pytest-dev/pytest/issues/3083): Removed [`Metafunc.addcall`]. This was the predecessor mechanism to [`@pytest.mark.parametrize`].

    See our [[docs]](deprecations.html#metafunc-addcall-deprecated) on information on how to update your code.

-   [#3085](https://github.com/pytest-dev/pytest/issues/3085): Removed support for passing strings to [`pytest.main`]. Now, always pass a list of strings instead.

    See our [[docs]](deprecations.html#passing-command-line-string-to-pytest-main-deprecated) on information on how to update your code.

-   [#3086](https://github.com/pytest-dev/pytest/issues/3086): [`[pytest]`] section in **setup.cfg** files is no longer supported, use [`[tool:pytest]`] instead. [`setup.cfg`] files are meant for use with [`distutils`], and a section named [`pytest`] has notoriously been a source of conflicts and bugs.

    Note that for **pytest.ini** and **tox.ini** files the section remains [`[pytest]`].

-   [#3616](https://github.com/pytest-dev/pytest/issues/3616): Removed the deprecated compat properties for [`node.Class/Function/Module`] - use [`pytest.Class/Function/Module`] now.

    See our [[docs]](deprecations.html#internal-classes-accessed-through-node-deprecated) on information on how to update your code.

-   [#4421](https://github.com/pytest-dev/pytest/issues/4421): Removed the implementation of the [`pytest_namespace`] hook.

    See our [[docs]](deprecations.html#pytest-namespace-deprecated) on information on how to update your code.

-   [#4489](https://github.com/pytest-dev/pytest/issues/4489): Removed [`request.cached_setup`]. This was the predecessor mechanism to modern fixtures.

    See our [[docs]](deprecations.html#cached-setup-deprecated) on information on how to update your code.

-   [#4535](https://github.com/pytest-dev/pytest/issues/4535): Removed the deprecated [`PyCollector.makeitem`] method. This method was made public by mistake a long time ago.

-   [#4543](https://github.com/pytest-dev/pytest/issues/4543): Removed support to define fixtures using the [`pytest_funcarg__`] prefix. Use the [`@pytest.fixture`] decorator instead.

    See our [[docs]](deprecations.html#pytest-funcarg-prefix-deprecated) on information on how to update your code.

-   [#4545](https://github.com/pytest-dev/pytest/issues/4545): Calling fixtures directly is now always an error instead of a warning.

    See our [[docs]](deprecations.html#calling-fixtures-directly-deprecated) on information on how to update your code.

-   [#4546](https://github.com/pytest-dev/pytest/issues/4546): Remove [`Node.get_marker(name)`] the return value was not usable for more than an existence check.

    Use [`Node.get_closest_marker(name)`] as a replacement.

-   [#4547](https://github.com/pytest-dev/pytest/issues/4547): The deprecated [`record_xml_property`] fixture has been removed, use the more generic [`record_property`] instead.

    See our [[docs]](deprecations.html#record-xml-property-deprecated) for more information.

-   [#4548](https://github.com/pytest-dev/pytest/issues/4548): An error is now raised if the [`pytest_plugins`] variable is defined in a non-top-level [`conftest.py`] file (i.e., not residing in the [`rootdir`]).

    See our [[docs]](deprecations.html#pytest-plugins-in-non-top-level-conftest-files-deprecated) for more information.

-   [#891](https://github.com/pytest-dev/pytest/issues/891): Remove [`testfunction.markername`] attributes - use [`Node.iter_markers(name=None)`] to iterate them.

### Deprecations[¶](#id755 "Link to this heading")

-   [#3050](https://github.com/pytest-dev/pytest/issues/3050): Deprecated the [`pytest.config`] global.

    See [[pytest.config global]](deprecations.html#pytest-config-global-deprecated) for rationale.

-   [#3974](https://github.com/pytest-dev/pytest/issues/3974): Passing the [`message`] parameter of [`pytest.raises`] now issues a [`DeprecationWarning`].

    It is a common mistake to think this parameter will match the exception message, while in fact it only serves to provide a custom message in case the [`pytest.raises`] check fails. To avoid this mistake and because it is believed to be little used, pytest is deprecating it without providing an alternative for the moment.

    If you have concerns about this, please comment on [#3974](https://github.com/pytest-dev/pytest/issues/3974).

-   [#4435](https://github.com/pytest-dev/pytest/issues/4435): Deprecated [`raises(...,`]` `[`'code(as_a_string)')`] and [`warns(...,`]` `[`'code(as_a_string)')`].

    See [[raises / warns with a string as the second argument]](deprecations.html#raises-warns-exec) for rationale and examples.

### Features[¶](#id756 "Link to this heading")

-   [#3191](https://github.com/pytest-dev/pytest/issues/3191): A warning is now issued when assertions are made for [`None`].

    This is a common source of confusion among new users, which write:

    ::: 
    ::: highlight
        assert mocked_object.assert_called_with(3, 4, 5, key="value")
    :::
    :::

    When they should write:

    ::: 
    ::: highlight
        mocked_object.assert_called_with(3, 4, 5, key="value")
    :::
    :::

    Because the [`assert_called_with`] method of mock objects already executes an assertion.

    This warning will not be issued when [`None`] is explicitly checked. An assertion like:

    ::: 
    ::: highlight
        assert variable is None
    :::
    :::

    will not issue the warning.

-   [#3632](https://github.com/pytest-dev/pytest/issues/3632): Richer equality comparison introspection on [`AssertionError`] for objects created using [attrs](https://www.attrs.org/en/stable/) or [[`dataclasses`]](https://docs.python.org/3/library/dataclasses.html#module-dataclasses "(in Python v3.14)") (Python 3.7+, [backported to 3.6](https://pypi.org/project/dataclasses)).

-   [#4278](https://github.com/pytest-dev/pytest/issues/4278): [`CACHEDIR.TAG`] files are now created inside cache directories.

    Those files are part of the [Cache Directory Tagging Standard](https://bford.info/cachedir/spec.html), and can be used by backup or synchronization programs to identify pytest's cache directory as such.

-   [#4292](https://github.com/pytest-dev/pytest/issues/4292): [`pytest.outcomes.Exit`] is derived from [`SystemExit`] instead of [`KeyboardInterrupt`]. This allows us to better handle [`pdb`] exiting.

-   [#4371](https://github.com/pytest-dev/pytest/issues/4371): Updated the [`--collect-only`] option to display test descriptions when ran using [`--verbose`].

-   [#4386](https://github.com/pytest-dev/pytest/issues/4386): Restructured [`ExceptionInfo`] object construction and ensure incomplete instances have a [`repr`]/[`str`].

-   [#4416](https://github.com/pytest-dev/pytest/issues/4416): pdb: added support for keyword arguments with [`pdb.set_trace`].

    It handles [`header`] similar to Python 3.7 does it, and forwards any other keyword arguments to the [`Pdb`] constructor.

    This allows for [`__import__("pdb").set_trace(skip=["foo.*"])`].

-   [#4483](https://github.com/pytest-dev/pytest/issues/4483): Added ini parameter [`junit_duration_report`] to optionally report test call durations, excluding setup and teardown times.

    The JUnit XML specification and the default pytest behavior is to include setup and teardown times in the test duration report. You can include just the call durations instead (excluding setup and teardown) by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        junit_duration_report = call
    :::
    :::

-   [#4532](https://github.com/pytest-dev/pytest/issues/4532): [`-ra`] now will show errors and failures last, instead of as the first items in the summary.

    This makes it easier to obtain a list of errors and failures to run tests selectively.

-   [#4599](https://github.com/pytest-dev/pytest/issues/4599): [`pytest.importorskip`] now supports a [`reason`] parameter, which will be shown when the requested module cannot be imported.

### Bug Fixes[¶](#id757 "Link to this heading")

-   [#3532](https://github.com/pytest-dev/pytest/issues/3532): [`-p`] now accepts its argument without a space between the value, for example [`-pmyplugin`].

-   [#4327](https://github.com/pytest-dev/pytest/issues/4327): [`approx`] again works with more generic containers, more precisely instances of [`Iterable`] and [`Sized`] instead of more restrictive [`Sequence`].

-   [#4397](https://github.com/pytest-dev/pytest/issues/4397): Ensure that node ids are printable.

-   [#4435](https://github.com/pytest-dev/pytest/issues/4435): Fixed [`raises(...,`]` `[`'code(string)')`] frame filename.

-   [#4458](https://github.com/pytest-dev/pytest/issues/4458): Display actual test ids in [`--collect-only`].

### Improved Documentation[¶](#id758 "Link to this heading")

-   [#4557](https://github.com/pytest-dev/pytest/issues/4557): Markers example documentation page updated to support latest pytest version.

-   [#4558](https://github.com/pytest-dev/pytest/issues/4558): Update cache documentation example to correctly show cache hit and miss.

-   [#4580](https://github.com/pytest-dev/pytest/issues/4580): Improved detailed summary report documentation.

### Trivial/Internal Changes[¶](#id759 "Link to this heading")

-   [#4447](https://github.com/pytest-dev/pytest/issues/4447): Changed the deprecation type of [`--result-log`] to [`PytestDeprecationWarning`].

    It was decided to remove this feature at the next major revision.

## pytest 4.0.2 (2018-12-13)[¶](#pytest-4-0-2-2018-12-13 "Link to this heading")

### Bug Fixes[¶](#id760 "Link to this heading")

-   [#4265](https://github.com/pytest-dev/pytest/issues/4265): Validate arguments from the [`PYTEST_ADDOPTS`] environment variable and the [`addopts`] ini option separately.

-   [#4435](https://github.com/pytest-dev/pytest/issues/4435): Fix [`raises(...,`]` `[`'code(string)')`] frame filename.

-   [#4500](https://github.com/pytest-dev/pytest/issues/4500): When a fixture yields and a log call is made after the test runs, and, if the test is interrupted, capture attributes are [`None`].

-   [#4538](https://github.com/pytest-dev/pytest/issues/4538): Raise [`TypeError`] for [`with`]` `[`raises(...,`]` `[`match=<non-None`]` `[`falsey`]` `[`value>)`].

### Improved Documentation[¶](#id761 "Link to this heading")

-   [#1495](https://github.com/pytest-dev/pytest/issues/1495): Document common doctest fixture directory tree structure pitfalls

## pytest 4.0.1 (2018-11-23)[¶](#pytest-4-0-1-2018-11-23 "Link to this heading")

### Bug Fixes[¶](#id762 "Link to this heading")

-   [#3952](https://github.com/pytest-dev/pytest/issues/3952): Display warnings before "short test summary info" again, but still later warnings in the end.

-   [#4386](https://github.com/pytest-dev/pytest/issues/4386): Handle uninitialized exceptioninfo in repr/str.

-   [#4393](https://github.com/pytest-dev/pytest/issues/4393): Do not create [`.gitignore`]/[`README.md`] files in existing cache directories.

-   [#4400](https://github.com/pytest-dev/pytest/issues/4400): Rearrange warning handling for the yield test errors so the opt-out in 4.0.x correctly works.

-   [#4405](https://github.com/pytest-dev/pytest/issues/4405): Fix collection of testpaths with [`--pyargs`].

-   [#4412](https://github.com/pytest-dev/pytest/issues/4412): Fix assertion rewriting involving [`Starred`] + side-effects.

-   [#4425](https://github.com/pytest-dev/pytest/issues/4425): Ensure we resolve the absolute path when the given [`--basetemp`] is a relative path.

### Trivial/Internal Changes[¶](#id763 "Link to this heading")

-   [#4315](https://github.com/pytest-dev/pytest/issues/4315): Use [`pkg_resources.parse_version`] instead of [`LooseVersion`] in minversion check.

-   [#4440](https://github.com/pytest-dev/pytest/issues/4440): Adjust the stack level of some internal pytest warnings.

## pytest 4.0.0 (2018-11-13)[¶](#pytest-4-0-0-2018-11-13 "Link to this heading")

### Removals[¶](#id764 "Link to this heading")

-   [#3737](https://github.com/pytest-dev/pytest/issues/3737): **RemovedInPytest4Warnings are now errors by default.**

    Following our plan to remove deprecated features with as little disruption as possible, all warnings of type [`RemovedInPytest4Warnings`] now generate errors instead of warning messages.

    **The affected features will be effectively removed in pytest 4.1**, so please consult the [[Deprecations and Removals]](deprecations.html) section in the docs for directions on how to update existing code.

    In the pytest [`4.0.X`] series, it is possible to change the errors back into warnings as a stop gap measure by adding this to your [`pytest.ini`] file:

    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            ignore::pytest.RemovedInPytest4Warning
    :::
    :::

    But this will stop working when pytest [`4.1`] is released.

    **If you have concerns** about the removal of a specific feature, please add a comment to [#4348](https://github.com/pytest-dev/pytest/issues/4348).

-   [#4358](https://github.com/pytest-dev/pytest/issues/4358): Remove the [`::()`] notation to denote a test class instance in node ids.

    Previously, node ids that contain test instances would use [`::()`] to denote the instance like this:

    ::: 
    ::: highlight
        test_foo.py::Test::()::test_bar
    :::
    :::

    The extra [`::()`] was puzzling to most users and has been removed, so that the test id becomes now:

    ::: 
    ::: highlight
        test_foo.py::Test::test_bar
    :::
    :::

    This change could not accompany a deprecation period as is usual when user-facing functionality changes because it was not really possible to detect when the functionality was being used explicitly.

    The extra [`::()`] might have been removed in some places internally already, which then led to confusion in places where it was expected, e.g. with [`--deselect`] ([#4127](https://github.com/pytest-dev/pytest/issues/4127)).

    Test class instances are also not listed with [`--collect-only`] anymore.

### Features[¶](#id765 "Link to this heading")

-   [#4270](https://github.com/pytest-dev/pytest/issues/4270): The [`cache_dir`] option uses [`$TOX_ENV_DIR`] as prefix (if set in the environment).

    This uses a different cache per tox environment by default.

### Bug Fixes[¶](#id766 "Link to this heading")

-   [#3554](https://github.com/pytest-dev/pytest/issues/3554): Fix [`CallInfo.__repr__`] for when the call is not finished yet.

## pytest 3.10.1 (2018-11-11)[¶](#pytest-3-10-1-2018-11-11 "Link to this heading")

### Bug Fixes[¶](#id767 "Link to this heading")

-   [#4287](https://github.com/pytest-dev/pytest/issues/4287): Fix nested usage of debugging plugin (pdb), e.g. with pytester's [`testdir.runpytest`].

-   [#4304](https://github.com/pytest-dev/pytest/issues/4304): Block the [`stepwise`] plugin if [`cacheprovider`] is also blocked, as one depends on the other.

-   [#4306](https://github.com/pytest-dev/pytest/issues/4306): Parse [`minversion`] as an actual version and not as dot-separated strings.

-   [#4310](https://github.com/pytest-dev/pytest/issues/4310): Fix duplicate collection due to multiple args matching the same packages.

-   [#4321](https://github.com/pytest-dev/pytest/issues/4321): Fix [`item.nodeid`] with resolved symlinks.

-   [#4325](https://github.com/pytest-dev/pytest/issues/4325): Fix collection of direct symlinked files, where the target does not match [`python_files`].

-   [#4329](https://github.com/pytest-dev/pytest/issues/4329): Fix TypeError in report_collect with \_collect_report_last_write.

### Trivial/Internal Changes[¶](#id768 "Link to this heading")

-   [#4305](https://github.com/pytest-dev/pytest/issues/4305): Replace byte/unicode helpers in test_capture with python level syntax.

## pytest 3.10.0 (2018-11-03)[¶](#pytest-3-10-0-2018-11-03 "Link to this heading")

### Features[¶](#id769 "Link to this heading")

-   [#2619](https://github.com/pytest-dev/pytest/issues/2619): Resume capturing output after [`continue`] with [`__import__("pdb").set_trace()`].

    This also adds a new [`pytest_leave_pdb`] hook, and passes in [`pdb`] to the existing [`pytest_enter_pdb`] hook.

-   [#4147](https://github.com/pytest-dev/pytest/issues/4147): Add [`--sw`], [`--stepwise`] as an alternative to [`--lf`]` `[`-x`] for stopping at the first failure, but starting the next test invocation from that test. See [[the documentation]](how-to/cache.html#cache-stepwise) for more info.

-   [#4188](https://github.com/pytest-dev/pytest/issues/4188): Make [`--color`] emit colorful dots when not running in verbose mode. Earlier, it would only colorize the test-by-test output if [`--verbose`] was also passed.

-   [#4225](https://github.com/pytest-dev/pytest/issues/4225): Improve performance with collection reporting in non-quiet mode with terminals.

    The "collecting ..." message is only printed/updated every 0.5s.

### Bug Fixes[¶](#id770 "Link to this heading")

-   [#2701](https://github.com/pytest-dev/pytest/issues/2701): Fix false [`RemovedInPytest4Warning:`]` `[`usage`]` `[`of`]` `[`Session...`]` `[`is`]` `[`deprecated,`]` `[`please`]` `[`use`]` `[`pytest`] warnings.

-   [#4046](https://github.com/pytest-dev/pytest/issues/4046): Fix problems with running tests in package [`__init__.py`] files.

-   [#4260](https://github.com/pytest-dev/pytest/issues/4260): Swallow warnings during anonymous compilation of source.

-   [#4262](https://github.com/pytest-dev/pytest/issues/4262): Fix access denied error when deleting stale directories created by [`tmpdir`] / [`tmp_path`].

-   [#611](https://github.com/pytest-dev/pytest/issues/611): Naming a fixture [`request`] will now raise a warning: the [`request`] fixture is internal and should not be overwritten as it will lead to internal errors.

-   [#4266](https://github.com/pytest-dev/pytest/issues/4266): Handle (ignore) exceptions raised during collection, e.g. with Django's LazySettings proxy class.

### Improved Documentation[¶](#id771 "Link to this heading")

-   [#4255](https://github.com/pytest-dev/pytest/issues/4255): Added missing documentation about the fact that module names passed to filter warnings are not regex-escaped.

### Trivial/Internal Changes[¶](#id772 "Link to this heading")

-   [#4272](https://github.com/pytest-dev/pytest/issues/4272): Display cachedir also in non-verbose mode if non-default.

-   [#4277](https://github.com/pytest-dev/pytest/issues/4277): pdb: improve message about output capturing with [`set_trace`].

    Do not display "IO-capturing turned off/on" when [`-s`] is used to avoid confusion.

-   [#4279](https://github.com/pytest-dev/pytest/issues/4279): Improve message and stack level of warnings issued by [`monkeypatch.setenv`] when the value of the environment variable is not a [`str`].

## pytest 3.9.3 (2018-10-27)[¶](#pytest-3-9-3-2018-10-27 "Link to this heading")

### Bug Fixes[¶](#id773 "Link to this heading")

-   [#4174](https://github.com/pytest-dev/pytest/issues/4174): Fix "ValueError: Plugin already registered" with conftest plugins via symlink.

-   [#4181](https://github.com/pytest-dev/pytest/issues/4181): Handle race condition between creation and deletion of temporary folders.

-   [#4221](https://github.com/pytest-dev/pytest/issues/4221): Fix bug where the warning summary at the end of the test session was not showing the test where the warning was originated.

-   [#4243](https://github.com/pytest-dev/pytest/issues/4243): Fix regression when [`stacklevel`] for warnings was passed as positional argument on python2.

### Improved Documentation[¶](#id774 "Link to this heading")

-   [#3851](https://github.com/pytest-dev/pytest/issues/3851): Add reference to [`empty_parameter_set_mark`] ini option in documentation of [`@pytest.mark.parametrize`]

### Trivial/Internal Changes[¶](#id775 "Link to this heading")

-   [#4028](https://github.com/pytest-dev/pytest/issues/4028): Revert patching of [`sys.breakpointhook`] since it appears to do nothing.

-   [#4233](https://github.com/pytest-dev/pytest/issues/4233): Apply an import sorter ([`reorder-python-imports`]) to the codebase.

-   [#4248](https://github.com/pytest-dev/pytest/issues/4248): Remove use of unnecessary compat shim, six.binary_type

## pytest 3.9.2 (2018-10-22)[¶](#pytest-3-9-2-2018-10-22 "Link to this heading")

### Bug Fixes[¶](#id776 "Link to this heading")

-   [#2909](https://github.com/pytest-dev/pytest/issues/2909): Improve error message when a recursive dependency between fixtures is detected.

-   [#3340](https://github.com/pytest-dev/pytest/issues/3340): Fix logging messages not shown in hooks [`pytest_sessionstart()`] and [`pytest_sessionfinish()`].

-   [#3533](https://github.com/pytest-dev/pytest/issues/3533): Fix unescaped XML raw objects in JUnit report for skipped tests

-   [#3691](https://github.com/pytest-dev/pytest/issues/3691): Python 2: safely format warning message about passing unicode strings to [`warnings.warn`], which may cause surprising [`MemoryError`] exception when monkey patching [`warnings.warn`] itself.

-   [#4026](https://github.com/pytest-dev/pytest/issues/4026): Improve error message when it is not possible to determine a function's signature.

-   [#4177](https://github.com/pytest-dev/pytest/issues/4177): Pin [`setuptools>=40.0`] to support [`py_modules`] in [`setup.cfg`]

-   [#4179](https://github.com/pytest-dev/pytest/issues/4179): Restore the tmpdir behaviour of symlinking the current test run.

-   [#4192](https://github.com/pytest-dev/pytest/issues/4192): Fix filename reported by [`warnings.warn`] when using [`recwarn`] under python2.

## pytest 3.9.1 (2018-10-16)[¶](#pytest-3-9-1-2018-10-16 "Link to this heading")

### Features[¶](#id777 "Link to this heading")

-   [#4159](https://github.com/pytest-dev/pytest/issues/4159): For test-suites containing test classes, the information about the subclassed module is now output only if a higher verbosity level is specified (at least "-vv").

## pytest 3.9.0 (2018-10-15 - not published due to a release automation bug)[¶](#pytest-3-9-0-2018-10-15-not-published-due-to-a-release-automation-bug "Link to this heading")

### Deprecations[¶](#id778 "Link to this heading")

-   [#3616](https://github.com/pytest-dev/pytest/issues/3616): The following accesses have been documented as deprecated for years, but are now actually emitting deprecation warnings.

    -   Access of [`Module`], [`Function`], [`Class`], [`Instance`], [`File`] and [`Item`] through [`Node`] instances. Now users will this warning:

        ::: 
        ::: highlight
            usage of Function.Module is deprecated, please use pytest.Module instead
        :::
        :::

        Users should just [`import`]` `[`pytest`] and access those objects using the [`pytest`] module.

    -   [`request.cached_setup`], this was the precursor of the setup/teardown mechanism available to fixtures. You can consult [[funcarg comparison section in the docs]](funcarg_compare.html).

    -   Using objects named [`"Class"`] as a way to customize the type of nodes that are collected in [`Collector`] subclasses has been deprecated. Users instead should use [`pytest_collect_make_item`] to customize node types during collection.

        This issue should affect only advanced plugins who create new collection types, so if you see this warning message please contact the authors so they can change the code.

    -   The warning that produces the message below has changed to [`RemovedInPytest4Warning`]:

        ::: 
        ::: highlight
            getfuncargvalue is deprecated, use getfixturevalue
        :::
        :::

-   [#3988](https://github.com/pytest-dev/pytest/issues/3988): Add a Deprecation warning for pytest.ensuretemp as it was deprecated since a while.

### Features[¶](#id779 "Link to this heading")

-   [#2293](https://github.com/pytest-dev/pytest/issues/2293): Improve usage errors messages by hiding internal details which can be distracting and noisy.

    This has the side effect that some error conditions that previously raised generic errors (such as [`ValueError`] for unregistered marks) are now raising [`Failed`] exceptions.

-   [#3332](https://github.com/pytest-dev/pytest/issues/3332): Improve the error displayed when a [`conftest.py`] file could not be imported.

    In order to implement this, a new [`chain`] parameter was added to [`ExceptionInfo.getrepr`] to show or hide chained tracebacks in Python 3 (defaults to [`True`]).

-   [#3849](https://github.com/pytest-dev/pytest/issues/3849): Add [`empty_parameter_set_mark=fail_at_collect`] ini option for raising an exception when parametrize collects an empty set.

-   [#3964](https://github.com/pytest-dev/pytest/issues/3964): Log messages generated in the collection phase are shown when live-logging is enabled and/or when they are logged to a file.

-   [#3985](https://github.com/pytest-dev/pytest/issues/3985): Introduce [`tmp_path`] as a fixture providing a Path object. Also introduce [`tmp_path_factory`] as a session-scoped fixture for creating arbitrary temporary directories from any other fixture or test.

-   [#4013](https://github.com/pytest-dev/pytest/issues/4013): Deprecation warnings are now shown even if you customize the warnings filters yourself. In the previous version any customization would override pytest's filters and deprecation warnings would fall back to being hidden by default.

-   [#4073](https://github.com/pytest-dev/pytest/issues/4073): Allow specification of timeout for [`Testdir.runpytest_subprocess()`] and [`Testdir.run()`].

-   [#4098](https://github.com/pytest-dev/pytest/issues/4098): Add returncode argument to pytest.exit() to exit pytest with a specific return code.

-   [#4102](https://github.com/pytest-dev/pytest/issues/4102): Reimplement [`pytest.deprecated_call`] using [`pytest.warns`] so it supports the [`match='...'`] keyword argument.

    This has the side effect that [`pytest.deprecated_call`] now raises [`pytest.fail.Exception`] instead of [`AssertionError`].

-   [#4149](https://github.com/pytest-dev/pytest/issues/4149): Require setuptools\>=30.3 and move most of the metadata to [`setup.cfg`].

### Bug Fixes[¶](#id780 "Link to this heading")

-   [#2535](https://github.com/pytest-dev/pytest/issues/2535): Improve error message when test functions of [`unittest.TestCase`] subclasses use a parametrized fixture.

-   [#3057](https://github.com/pytest-dev/pytest/issues/3057): [`request.fixturenames`] now correctly returns the name of fixtures created by [`request.getfixturevalue()`].

-   [#3946](https://github.com/pytest-dev/pytest/issues/3946): Warning filters passed as command line options using [`-W`] now take precedence over filters defined in [`ini`] configuration files.

-   [#4066](https://github.com/pytest-dev/pytest/issues/4066): Fix source reindenting by using [`textwrap.dedent`] directly.

-   [#4102](https://github.com/pytest-dev/pytest/issues/4102): [`pytest.warn`] will capture previously-warned warnings in Python 2. Previously they were never raised.

-   [#4108](https://github.com/pytest-dev/pytest/issues/4108): Resolve symbolic links for args.

    This fixes running [`pytest`]` `[`tests/test_foo.py::test_bar`], where [`tests`] is a symlink to [`project/app/tests`]: previously [`project/app/conftest.py`] would be ignored for fixtures then.

-   [#4132](https://github.com/pytest-dev/pytest/issues/4132): Fix duplicate printing of internal errors when using [`--pdb`].

-   [#4135](https://github.com/pytest-dev/pytest/issues/4135): pathlib based tmpdir cleanup now correctly handles symlinks in the folder.

-   [#4152](https://github.com/pytest-dev/pytest/issues/4152): Display the filename when encountering [`SyntaxWarning`].

### Improved Documentation[¶](#id781 "Link to this heading")

-   [#3713](https://github.com/pytest-dev/pytest/issues/3713): Update usefixtures documentation to clarify that it can't be used with fixture functions.

-   [#4058](https://github.com/pytest-dev/pytest/issues/4058): Update fixture documentation to specify that a fixture can be invoked twice in the scope it's defined for.

-   [#4064](https://github.com/pytest-dev/pytest/issues/4064): According to unittest.rst, setUpModule and tearDownModule were not implemented, but it turns out they are. So updated the documentation for unittest.

-   [#4151](https://github.com/pytest-dev/pytest/issues/4151): Add tempir testing example to CONTRIBUTING.rst guide

### Trivial/Internal Changes[¶](#id782 "Link to this heading")

-   [#2293](https://github.com/pytest-dev/pytest/issues/2293): The internal [`MarkerError`] exception has been removed.

-   [#3988](https://github.com/pytest-dev/pytest/issues/3988): Port the implementation of tmpdir to pathlib.

-   [#4063](https://github.com/pytest-dev/pytest/issues/4063): Exclude 0.00 second entries from [`--duration`] output unless [`-vv`] is passed on the command-line.

-   [#4093](https://github.com/pytest-dev/pytest/issues/4093): Fixed formatting of string literals in internal tests.

## pytest 3.8.2 (2018-10-02)[¶](#pytest-3-8-2-2018-10-02 "Link to this heading")

### Deprecations and Removals[¶](#deprecations-and-removals "Link to this heading")

-   [#4036](https://github.com/pytest-dev/pytest/issues/4036): The [`item`] parameter of [`pytest_warning_captured`] hook is now documented as deprecated. We realized only after the [`3.8`] release that this parameter is incompatible with [`pytest-xdist`].

    Our policy is to not deprecate features during bug-fix releases, but in this case we believe it makes sense as we are only documenting it as deprecated, without issuing warnings which might potentially break test suites. This will get the word out that hook implementers should not use this parameter at all.

    In a future release [`item`] will always be [`None`] and will emit a proper warning when a hook implementation makes use of it.

### Bug Fixes[¶](#id783 "Link to this heading")

-   [#3539](https://github.com/pytest-dev/pytest/issues/3539): Fix reload on assertion rewritten modules.

-   [#4034](https://github.com/pytest-dev/pytest/issues/4034): The [`.user_properties`] attribute of [`TestReport`] objects is a list of (name, value) tuples, but could sometimes be instantiated as a tuple of tuples. It is now always a list.

-   [#4039](https://github.com/pytest-dev/pytest/issues/4039): No longer issue warnings about using [`pytest_plugins`] in non-top-level directories when using [`--pyargs`]: the current [`--pyargs`] mechanism is not reliable and might give false negatives.

-   [#4040](https://github.com/pytest-dev/pytest/issues/4040): Exclude empty reports for passed tests when [`-rP`] option is used.

-   [#4051](https://github.com/pytest-dev/pytest/issues/4051): Improve error message when an invalid Python expression is passed to the [`-m`] option.

-   [#4056](https://github.com/pytest-dev/pytest/issues/4056): [`MonkeyPatch.setenv`] and [`MonkeyPatch.delenv`] issue a warning if the environment variable name is not [`str`] on Python 2.

    In Python 2, adding [`unicode`] keys to [`os.environ`] causes problems with [`subprocess`] (and possible other modules), making this a subtle bug specially susceptible when used with [`from`]` `[`__future__`]` `[`import`]` `[`unicode_literals`].

### Improved Documentation[¶](#id784 "Link to this heading")

-   [#3928](https://github.com/pytest-dev/pytest/issues/3928): Add possible values for fixture scope to docs.

## pytest 3.8.1 (2018-09-22)[¶](#pytest-3-8-1-2018-09-22 "Link to this heading")

### Bug Fixes[¶](#id785 "Link to this heading")

-   [#3286](https://github.com/pytest-dev/pytest/issues/3286): [`.pytest_cache`] directory is now automatically ignored by Git. Users who would like to contribute a solution for other SCMs please consult/comment on this issue.

-   [#3749](https://github.com/pytest-dev/pytest/issues/3749): Fix the following error during collection of tests inside packages:

    ::: 
    ::: highlight
        TypeError: object of type 'Package' has no len()
    :::
    :::

-   [#3941](https://github.com/pytest-dev/pytest/issues/3941): Fix bug where indirect parametrization would consider the scope of all fixtures used by the test function to determine the parametrization scope, and not only the scope of the fixtures being parametrized.

-   [#3973](https://github.com/pytest-dev/pytest/issues/3973): Fix crash of the assertion rewriter if a test changed the current working directory without restoring it afterwards.

-   [#3998](https://github.com/pytest-dev/pytest/issues/3998): Fix issue that prevented some caplog properties (for example [`record_tuples`]) from being available when entering the debugger with [`--pdb`].

-   [#3999](https://github.com/pytest-dev/pytest/issues/3999): Fix [`UnicodeDecodeError`] in python2.x when a class returns a non-ascii binary [`__repr__`] in an assertion which also contains non-ascii text.

### Improved Documentation[¶](#id786 "Link to this heading")

-   [#3996](https://github.com/pytest-dev/pytest/issues/3996): New [[Deprecations and Removals]](deprecations.html) page shows all currently deprecated features, the rationale to do so, and alternatives to update your code. It also list features removed from pytest in past major releases to help those with ancient pytest versions to upgrade.

### Trivial/Internal Changes[¶](#id787 "Link to this heading")

-   [#3955](https://github.com/pytest-dev/pytest/issues/3955): Improve pre-commit detection for changelog filenames

-   [#3975](https://github.com/pytest-dev/pytest/issues/3975): Remove legacy code around im_func as that was python2 only

## pytest 3.8.0 (2018-09-05)[¶](#pytest-3-8-0-2018-09-05 "Link to this heading")

### Deprecations and Removals[¶](#id788 "Link to this heading")

-   [#2452](https://github.com/pytest-dev/pytest/issues/2452): [`Config.warn`] and [`Node.warn`] have been deprecated, see [[Config.warn and Node.warn]](deprecations.html#config-warn-and-node-warn-deprecated) for rationale and examples.

-   [#3936](https://github.com/pytest-dev/pytest/issues/3936): [`@pytest.mark.filterwarnings`] second parameter is no longer regex-escaped, making it possible to actually use regular expressions to check the warning message.

    **Note**: regex-escaping the match string was an implementation oversight that might break test suites which depend on the old behavior.

### Features[¶](#id789 "Link to this heading")

-   [#2452](https://github.com/pytest-dev/pytest/issues/2452): Internal pytest warnings are now issued using the standard [`warnings`] module, making it possible to use the standard warnings filters to manage those warnings. This introduces [`PytestWarning`], [`PytestDeprecationWarning`] and [`RemovedInPytest4Warning`] warning types as part of the public API.

    Consult [[the documentation]](how-to/capture-warnings.html#internal-warnings) for more info.

-   [#2908](https://github.com/pytest-dev/pytest/issues/2908): [`DeprecationWarning`] and [`PendingDeprecationWarning`] are now shown by default if no other warning filter is configured. This makes pytest more compliant with [][**PEP 506#recommended-filter-settings-for-test-runners**](https://peps.python.org/pep-0506/#recommended-filter-settings-for-test-runners). See [[the docs]](how-to/capture-warnings.html#deprecation-warnings) for more info.

-   [#3251](https://github.com/pytest-dev/pytest/issues/3251): Warnings are now captured and displayed during test collection.

-   [#3784](https://github.com/pytest-dev/pytest/issues/3784): [`PYTEST_DISABLE_PLUGIN_AUTOLOAD`] environment variable disables plugin auto-loading when set.

-   [#3829](https://github.com/pytest-dev/pytest/issues/3829): Added the [`count`] option to [`console_output_style`] to enable displaying the progress as a count instead of a percentage.

-   [#3837](https://github.com/pytest-dev/pytest/issues/3837): Added support for 'xfailed' and 'xpassed' outcomes to the [`pytester.RunResult.assert_outcomes`] signature.

### Bug Fixes[¶](#id790 "Link to this heading")

-   [#3911](https://github.com/pytest-dev/pytest/issues/3911): Terminal writer now takes into account unicode character width when writing out progress.

-   [#3913](https://github.com/pytest-dev/pytest/issues/3913): Pytest now returns with correct exit code (EXIT_USAGEERROR, 4) when called with unknown arguments.

-   [#3918](https://github.com/pytest-dev/pytest/issues/3918): Improve performance of assertion rewriting.

### Improved Documentation[¶](#id791 "Link to this heading")

-   [#3566](https://github.com/pytest-dev/pytest/issues/3566): Added a blurb in usage.rst for the usage of -r flag which is used to show an extra test summary info.

-   [#3907](https://github.com/pytest-dev/pytest/issues/3907): Corrected type of the exceptions collection passed to [`xfail`]: [`raises`] argument accepts a [`tuple`] instead of [`list`].

### Trivial/Internal Changes[¶](#id792 "Link to this heading")

-   [#3853](https://github.com/pytest-dev/pytest/issues/3853): Removed [`"run`]` `[`all`]` `[`(no`]` `[`recorded`]` `[`failures)"`] message printed with [`--failed-first`] and [`--last-failed`] when there are no failed tests.

## pytest 3.7.4 (2018-08-29)[¶](#pytest-3-7-4-2018-08-29 "Link to this heading")

### Bug Fixes[¶](#id793 "Link to this heading")

-   [#3506](https://github.com/pytest-dev/pytest/issues/3506): Fix possible infinite recursion when writing [`.pyc`] files.

-   [#3853](https://github.com/pytest-dev/pytest/issues/3853): Cache plugin now obeys the [`-q`] flag when [`--last-failed`] and [`--failed-first`] flags are used.

-   [#3883](https://github.com/pytest-dev/pytest/issues/3883): Fix bad console output when using [`console_output_style=classic`].

-   [#3888](https://github.com/pytest-dev/pytest/issues/3888): Fix macOS specific code using [`capturemanager`] plugin in doctests.

### Improved Documentation[¶](#id794 "Link to this heading")

-   [#3902](https://github.com/pytest-dev/pytest/issues/3902): Fix pytest.org links

## pytest 3.7.3 (2018-08-26)[¶](#pytest-3-7-3-2018-08-26 "Link to this heading")

### Bug Fixes[¶](#id795 "Link to this heading")

-   [#3033](https://github.com/pytest-dev/pytest/issues/3033): Fixtures during teardown can again use [`capsys`] and [`capfd`] to inspect output captured during tests.

-   [#3773](https://github.com/pytest-dev/pytest/issues/3773): Fix collection of tests from [`__init__.py`] files if they match the [`python_files`] configuration option.

-   [#3796](https://github.com/pytest-dev/pytest/issues/3796): Fix issue where teardown of fixtures of consecutive sub-packages were executed once, at the end of the outer package.

-   [#3816](https://github.com/pytest-dev/pytest/issues/3816): Fix bug where [`--show-capture=no`] option would still show logs printed during fixture teardown.

-   [#3819](https://github.com/pytest-dev/pytest/issues/3819): Fix [`stdout/stderr`] not getting captured when real-time cli logging is active.

-   [#3843](https://github.com/pytest-dev/pytest/issues/3843): Fix collection error when specifying test functions directly in the command line using [`test.py::test`] syntax together with [`--doctest-modules`].

-   [#3848](https://github.com/pytest-dev/pytest/issues/3848): Fix bugs where unicode arguments could not be passed to [`testdir.runpytest`] on Python 2.

-   [#3854](https://github.com/pytest-dev/pytest/issues/3854): Fix double collection of tests within packages when the filename starts with a capital letter.

### Improved Documentation[¶](#id796 "Link to this heading")

-   [#3824](https://github.com/pytest-dev/pytest/issues/3824): Added example for multiple glob pattern matches in [`python_files`].

-   [#3833](https://github.com/pytest-dev/pytest/issues/3833): Added missing docs for [`pytester.Testdir`].

-   [#3870](https://github.com/pytest-dev/pytest/issues/3870): Correct documentation for setuptools integration.

### Trivial/Internal Changes[¶](#id797 "Link to this heading")

-   [#3826](https://github.com/pytest-dev/pytest/issues/3826): Replace broken type annotations with type comments.

-   [#3845](https://github.com/pytest-dev/pytest/issues/3845): Remove a reference to issue [#568](https://github.com/pytest-dev/pytest/issues/568) from the documentation, which has since been fixed.

## pytest 3.7.2 (2018-08-16)[¶](#pytest-3-7-2-2018-08-16 "Link to this heading")

### Bug Fixes[¶](#id798 "Link to this heading")

-   [#3671](https://github.com/pytest-dev/pytest/issues/3671): Fix [`filterwarnings`] not being registered as a builtin mark.

-   [#3768](https://github.com/pytest-dev/pytest/issues/3768), [#3789](https://github.com/pytest-dev/pytest/issues/3789): Fix test collection from packages mixed with normal directories.

-   [#3771](https://github.com/pytest-dev/pytest/issues/3771): Fix infinite recursion during collection if a [`pytest_ignore_collect`] hook returns [`False`] instead of [`None`].

-   [#3774](https://github.com/pytest-dev/pytest/issues/3774): Fix bug where decorated fixtures would lose functionality (for example [`@mock.patch`]).

-   [#3775](https://github.com/pytest-dev/pytest/issues/3775): Fix bug where importing modules or other objects with prefix [`pytest_`] prefix would raise a [`PluginValidationError`].

-   [#3788](https://github.com/pytest-dev/pytest/issues/3788): Fix [`AttributeError`] during teardown of [`TestCase`] subclasses which raise an exception during [`__init__`].

-   [#3804](https://github.com/pytest-dev/pytest/issues/3804): Fix traceback reporting for exceptions with [`__cause__`] cycles.

### Improved Documentation[¶](#id799 "Link to this heading")

-   [#3746](https://github.com/pytest-dev/pytest/issues/3746): Add documentation for [`metafunc.config`] that had been mistakenly hidden.

## pytest 3.7.1 (2018-08-02)[¶](#pytest-3-7-1-2018-08-02 "Link to this heading")

### Bug Fixes[¶](#id800 "Link to this heading")

-   [#3473](https://github.com/pytest-dev/pytest/issues/3473): Raise immediately if [`approx()`] is given an expected value of a type it doesn't understand (e.g. strings, nested dicts, etc.).

-   [#3712](https://github.com/pytest-dev/pytest/issues/3712): Correctly represent the dimensions of a numpy array when calling [`repr()`] on [`approx()`].

-   [#3742](https://github.com/pytest-dev/pytest/issues/3742): Fix incompatibility with third party plugins during collection, which produced the error [`object`]` `[`has`]` `[`no`]` `[`attribute`]` `[`'_collectfile'`].

-   [#3745](https://github.com/pytest-dev/pytest/issues/3745): Display the absolute path if [`cache_dir`] is not relative to the [`rootdir`] instead of failing.

-   [#3747](https://github.com/pytest-dev/pytest/issues/3747): Fix compatibility problem with plugins and the warning code issued by fixture functions when they are called directly.

-   [#3748](https://github.com/pytest-dev/pytest/issues/3748): Fix infinite recursion in [`pytest.approx`] with arrays in [`numpy<1.13`].

-   [#3757](https://github.com/pytest-dev/pytest/issues/3757): Pin pathlib2 to [`>=2.2.0`] as we require [`__fspath__`] support.

-   [#3763](https://github.com/pytest-dev/pytest/issues/3763): Fix [`TypeError`] when the assertion message is [`bytes`] in python 3.

## pytest 3.7.0 (2018-07-30)[¶](#pytest-3-7-0-2018-07-30 "Link to this heading")

### Deprecations and Removals[¶](#id801 "Link to this heading")

-   [#2639](https://github.com/pytest-dev/pytest/issues/2639): [`pytest_namespace`] has been [[deprecated]](deprecations.html#pytest-namespace-deprecated).

-   [#3661](https://github.com/pytest-dev/pytest/issues/3661): Calling a fixture function directly, as opposed to request them in a test function, now issues a [`RemovedInPytest4Warning`]. See [[the documentation for rationale and examples]](deprecations.html#calling-fixtures-directly-deprecated).

### Features[¶](#id802 "Link to this heading")

-   [#2283](https://github.com/pytest-dev/pytest/issues/2283): New [`package`] fixture scope: fixtures are finalized when the last test of a *package* finishes. This feature is considered **experimental**, so use it sparingly.

-   [#3576](https://github.com/pytest-dev/pytest/issues/3576): [`Node.add_marker`] now supports an [`append=True/False`] parameter to determine whether the mark comes last (default) or first.

-   [#3579](https://github.com/pytest-dev/pytest/issues/3579): Fixture [`caplog`] now has a [`messages`] property, providing convenient access to the format-interpolated log messages without the extra data provided by the formatter/handler.

-   [#3610](https://github.com/pytest-dev/pytest/issues/3610): New [`--trace`] option to enter the debugger at the start of a test.

-   [#3623](https://github.com/pytest-dev/pytest/issues/3623): Introduce [`pytester.copy_example`] as helper to do acceptance tests against examples from the project.

### Bug Fixes[¶](#id803 "Link to this heading")

-   [#2220](https://github.com/pytest-dev/pytest/issues/2220): Fix a bug where fixtures overridden by direct parameters (for example parametrization) were being instantiated even if they were not being used by a test.

-   [#3695](https://github.com/pytest-dev/pytest/issues/3695): Fix [`ApproxNumpy`] initialisation argument mixup, [`abs`] and [`rel`] tolerances were flipped causing strange comparison results. Add tests to check [`abs`] and [`rel`] tolerances for [`np.array`] and test for expecting [`nan`] with [`np.array()`]

-   [#980](https://github.com/pytest-dev/pytest/issues/980): Fix truncated locals output in verbose mode.

### Improved Documentation[¶](#id804 "Link to this heading")

-   [#3295](https://github.com/pytest-dev/pytest/issues/3295): Correct the usage documentation of [`--last-failed-no-failures`] by adding the missing [`--last-failed`] argument in the presented examples, because they are misleading and lead to think that the missing argument is not needed.

### Trivial/Internal Changes[¶](#id805 "Link to this heading")

-   [#3519](https://github.com/pytest-dev/pytest/issues/3519): Now a [`README.md`] file is created in [`.pytest_cache`] to make it clear why the directory exists.

## pytest 3.6.4 (2018-07-28)[¶](#pytest-3-6-4-2018-07-28 "Link to this heading")

### Bug Fixes[¶](#id806 "Link to this heading")

-   Invoke pytest using [`-mpytest`] so [`sys.path`] does not get polluted by packages installed in [`site-packages`]. ([#742](https://github.com/pytest-dev/pytest/issues/742))

### Improved Documentation[¶](#id807 "Link to this heading")

-   Use [`smtp_connection`] instead of [`smtp`] in fixtures documentation to avoid possible confusion. ([#3592](https://github.com/pytest-dev/pytest/issues/3592))

### Trivial/Internal Changes[¶](#id808 "Link to this heading")

-   Remove obsolete [`__future__`] imports. ([#2319](https://github.com/pytest-dev/pytest/issues/2319))

-   Add CITATION to provide information on how to formally cite pytest. ([#3402](https://github.com/pytest-dev/pytest/issues/3402))

-   Replace broken type annotations with type comments. ([#3635](https://github.com/pytest-dev/pytest/issues/3635))

-   Pin [`pluggy`] to [`<0.8`]. ([#3727](https://github.com/pytest-dev/pytest/issues/3727))

## pytest 3.6.3 (2018-07-04)[¶](#pytest-3-6-3-2018-07-04 "Link to this heading")

### Bug Fixes[¶](#id809 "Link to this heading")

-   Fix [`ImportWarning`] triggered by explicit relative imports in assertion-rewritten package modules. ([#3061](https://github.com/pytest-dev/pytest/issues/3061))

-   Fix error in [`pytest.approx`] when dealing with 0-dimension numpy arrays. ([#3593](https://github.com/pytest-dev/pytest/issues/3593))

-   No longer raise [`ValueError`] when using the [`get_marker`] API. ([#3605](https://github.com/pytest-dev/pytest/issues/3605))

-   Fix problem where log messages with non-ascii characters would not appear in the output log file. ([#3630](https://github.com/pytest-dev/pytest/issues/3630))

-   No longer raise [`AttributeError`] when legacy marks can't be stored in functions. ([#3631](https://github.com/pytest-dev/pytest/issues/3631))

### Improved Documentation[¶](#id810 "Link to this heading")

-   The description above the example for [`@pytest.mark.skipif`] now better matches the code. ([#3611](https://github.com/pytest-dev/pytest/issues/3611))

### Trivial/Internal Changes[¶](#id811 "Link to this heading")

-   Internal refactoring: removed unused [`CallSpec2tox`]` `[`._globalid_args`] attribute and [`metafunc`] parameter from [`CallSpec2.copy()`]. ([#3598](https://github.com/pytest-dev/pytest/issues/3598))

-   Silence usage of [`reduce`] warning in Python 2 ([#3609](https://github.com/pytest-dev/pytest/issues/3609))

-   Fix usage of [`attr.ib`] deprecated [`convert`] parameter. ([#3653](https://github.com/pytest-dev/pytest/issues/3653))

## pytest 3.6.2 (2018-06-20)[¶](#pytest-3-6-2-2018-06-20 "Link to this heading")

### Bug Fixes[¶](#id812 "Link to this heading")

-   Fix regression in [`Node.add_marker`] by extracting the mark object of a [`MarkDecorator`]. ([#3555](https://github.com/pytest-dev/pytest/issues/3555))

-   Warnings without [`location`] were reported as [`None`]. This is corrected to now report [`<undetermined`]` `[`location>`]. ([#3563](https://github.com/pytest-dev/pytest/issues/3563))

-   Continue to call finalizers in the stack when a finalizer in a former scope raises an exception. ([#3569](https://github.com/pytest-dev/pytest/issues/3569))

-   Fix encoding error with [`print`] statements in doctests ([#3583](https://github.com/pytest-dev/pytest/issues/3583))

### Improved Documentation[¶](#id813 "Link to this heading")

-   Add documentation for the [`--strict`] flag. ([#3549](https://github.com/pytest-dev/pytest/issues/3549))

### Trivial/Internal Changes[¶](#id814 "Link to this heading")

-   Update old quotation style to parens in fixture.rst documentation. ([#3525](https://github.com/pytest-dev/pytest/issues/3525))

-   Improve display of hint about [`--fulltrace`] with [`KeyboardInterrupt`]. ([#3545](https://github.com/pytest-dev/pytest/issues/3545))

-   pytest's testsuite is no longer runnable through [`python`]` `[`setup.py`]` `[`test`] -- instead invoke [`pytest`] or [`tox`] directly. ([#3552](https://github.com/pytest-dev/pytest/issues/3552))

-   Fix typo in documentation ([#3567](https://github.com/pytest-dev/pytest/issues/3567))

## pytest 3.6.1 (2018-06-05)[¶](#pytest-3-6-1-2018-06-05 "Link to this heading")

### Bug Fixes[¶](#id815 "Link to this heading")

-   Fixed a bug where stdout and stderr were logged twice by junitxml when a test was marked xfail. ([#3491](https://github.com/pytest-dev/pytest/issues/3491))

-   Fix [`usefixtures`] mark applied to unittest tests by correctly instantiating [`FixtureInfo`]. ([#3498](https://github.com/pytest-dev/pytest/issues/3498))

-   Fix assertion rewriter compatibility with libraries that monkey patch [`file`] objects. ([#3503](https://github.com/pytest-dev/pytest/issues/3503))

### Improved Documentation[¶](#id816 "Link to this heading")

-   Added a section on how to use fixtures as factories to the fixture documentation. ([#3461](https://github.com/pytest-dev/pytest/issues/3461))

### Trivial/Internal Changes[¶](#id817 "Link to this heading")

-   Enable caching for pip/pre-commit in order to reduce build time on travis/appveyor. ([#3502](https://github.com/pytest-dev/pytest/issues/3502))

-   Switch pytest to the src/ layout as we already suggested it for good practice - now we implement it as well. ([#3513](https://github.com/pytest-dev/pytest/issues/3513))

-   Fix if in tests to support 3.7.0b5, where a docstring handling in AST got reverted. ([#3530](https://github.com/pytest-dev/pytest/issues/3530))

-   Remove some python2.5 compatibility code. ([#3529](https://github.com/pytest-dev/pytest/issues/3529))

## pytest 3.6.0 (2018-05-23)[¶](#pytest-3-6-0-2018-05-23 "Link to this heading")

### Features[¶](#id818 "Link to this heading")

-   Revamp the internals of the [`pytest.mark`] implementation with correct per node handling which fixes a number of long standing bugs caused by the old design. This introduces new [`Node.iter_markers(name)`] and [`Node.get_closest_marker(name)`] APIs. Users are **strongly encouraged** to read the [[reasons for the revamp in the docs]](historical-notes.html#marker-revamp), or jump over to details about [[updating existing code to use the new APIs]](historical-notes.html#update-marker-code). ([#3317](https://github.com/pytest-dev/pytest/issues/3317))

-   Now when [`@pytest.fixture`] is applied more than once to the same function a [`ValueError`] is raised. This buggy behavior would cause surprising problems and if was working for a test suite it was mostly by accident. ([#2334](https://github.com/pytest-dev/pytest/issues/2334))

-   Support for Python 3.7's builtin [`breakpoint()`] method, see [[Using the builtin breakpoint function]](how-to/failures.html#breakpoint-builtin) for details. ([#3180](https://github.com/pytest-dev/pytest/issues/3180))

-   [`monkeypatch`] now supports a [`context()`] function which acts as a context manager which undoes all patching done within the [`with`] block. ([#3290](https://github.com/pytest-dev/pytest/issues/3290))

-   The [`--pdb`] option now causes KeyboardInterrupt to enter the debugger, instead of stopping the test session. On python 2.7, hitting CTRL+C again exits the debugger. On python 3.2 and higher, use CTRL+D. ([#3299](https://github.com/pytest-dev/pytest/issues/3299))

-   pytest no longer changes the log level of the root logger when the [`log-level`] parameter has greater numeric value than that of the level of the root logger, which makes it play better with custom logging configuration in user code. ([#3307](https://github.com/pytest-dev/pytest/issues/3307))

### Bug Fixes[¶](#id819 "Link to this heading")

-   A rare race-condition which might result in corrupted [`.pyc`] files on Windows has been hopefully solved. ([#3008](https://github.com/pytest-dev/pytest/issues/3008))

-   Also use iter_marker for discovering the marks applying for marker expressions from the cli to avoid the bad data from the legacy mark storage. ([#3441](https://github.com/pytest-dev/pytest/issues/3441))

-   When showing diffs of failed assertions where the contents contain only whitespace, escape them using [`repr()`] first to make it easy to spot the differences. ([#3443](https://github.com/pytest-dev/pytest/issues/3443))

### Improved Documentation[¶](#id820 "Link to this heading")

-   Change documentation copyright year to a range which auto-updates itself each time it is published. ([#3303](https://github.com/pytest-dev/pytest/issues/3303))

### Trivial/Internal Changes[¶](#id821 "Link to this heading")

-   [`pytest`] now depends on the [python-atomicwrites](https://github.com/untitaker/python-atomicwrites) library. ([#3008](https://github.com/pytest-dev/pytest/issues/3008))

-   Update all pypi.python.org URLs to pypi.org. ([#3431](https://github.com/pytest-dev/pytest/issues/3431))

-   Detect [`pytest_`] prefixed hooks using the internal plugin manager since [`pluggy`] is deprecating the [`implprefix`] argument to [`PluginManager`]. ([#3487](https://github.com/pytest-dev/pytest/issues/3487))

-   Import [`Mapping`] and [`Sequence`] from [`_pytest.compat`] instead of directly from [`collections`] in [`python_api.py::approx`]. Add [`Mapping`] to [`_pytest.compat`], import it from [`collections`] on python 2, but from [`collections.abc`] on Python 3 to avoid a [`DeprecationWarning`] on Python 3.7 or newer. ([#3497](https://github.com/pytest-dev/pytest/issues/3497))

## pytest 3.5.1 (2018-04-23)[¶](#pytest-3-5-1-2018-04-23 "Link to this heading")

### Bug Fixes[¶](#id822 "Link to this heading")

-   Reset [`sys.last_type`], [`sys.last_value`] and [`sys.last_traceback`] before each test executes. Those attributes are added by pytest during the test run to aid debugging, but were never reset so they would create a leaking reference to the last failing test's frame which in turn could never be reclaimed by the garbage collector. ([#2798](https://github.com/pytest-dev/pytest/issues/2798))

-   [`pytest.raises`] now raises [`TypeError`] when receiving an unknown keyword argument. ([#3348](https://github.com/pytest-dev/pytest/issues/3348))

-   [`pytest.raises`] now works with exception classes that look like iterables. ([#3372](https://github.com/pytest-dev/pytest/issues/3372))

### Improved Documentation[¶](#id823 "Link to this heading")

-   Fix typo in [`caplog`] fixture documentation, which incorrectly identified certain attributes as methods. ([#3406](https://github.com/pytest-dev/pytest/issues/3406))

### Trivial/Internal Changes[¶](#id824 "Link to this heading")

-   Added a more indicative error message when parametrizing a function whose argument takes a default value. ([#3221](https://github.com/pytest-dev/pytest/issues/3221))

-   Remove internal [`_pytest.terminal.flatten`] function in favor of [`more_itertools.collapse`]. ([#3330](https://github.com/pytest-dev/pytest/issues/3330))

-   Import some modules from [`collections.abc`] instead of [`collections`] as the former modules trigger [`DeprecationWarning`] in Python 3.7. ([#3339](https://github.com/pytest-dev/pytest/issues/3339))

-   record_property is no longer experimental, removing the warnings was forgotten. ([#3360](https://github.com/pytest-dev/pytest/issues/3360))

-   Mention in documentation and CLI help that fixtures with leading [`_`] are printed by [`pytest`]` `[`--fixtures`] only if the [`-v`] option is added. ([#3398](https://github.com/pytest-dev/pytest/issues/3398))

## pytest 3.5.0 (2018-03-21)[¶](#pytest-3-5-0-2018-03-21 "Link to this heading")

### Deprecations and Removals[¶](#id825 "Link to this heading")

-   [`record_xml_property`] fixture is now deprecated in favor of the more generic [`record_property`]. ([#2770](https://github.com/pytest-dev/pytest/issues/2770))

-   Defining [`pytest_plugins`] is now deprecated in non-top-level conftest.py files, because they "leak" to the entire directory tree. [[See the docs]](deprecations.html#pytest-plugins-in-non-top-level-conftest-files-deprecated) for the rationale behind this decision ([#3084](https://github.com/pytest-dev/pytest/issues/3084))

### Features[¶](#id826 "Link to this heading")

-   New [`--show-capture`] command-line option that allows to specify how to display captured output when tests fail: [`no`], [`stdout`], [`stderr`], [`log`] or [`all`] (the default). ([#1478](https://github.com/pytest-dev/pytest/issues/1478))

-   New [`--rootdir`] command-line option to override the rules for discovering the root directory. See [[customize]](reference/customize.html) in the documentation for details. ([#1642](https://github.com/pytest-dev/pytest/issues/1642))

-   Fixtures are now instantiated based on their scopes, with higher-scoped fixtures (such as [`session`]) being instantiated first than lower-scoped fixtures (such as [`function`]). The relative order of fixtures of the same scope is kept unchanged, based in their declaration order and their dependencies. ([#2405](https://github.com/pytest-dev/pytest/issues/2405))

-   [`record_xml_property`] renamed to [`record_property`] and is now compatible with xdist, markers and any reporter. [`record_xml_property`] name is now deprecated. ([#2770](https://github.com/pytest-dev/pytest/issues/2770))

-   New [`--nf`], [`--new-first`] options: run new tests first followed by the rest of the tests, in both cases tests are also sorted by the file modified time, with more recent files coming first. ([#3034](https://github.com/pytest-dev/pytest/issues/3034))

-   New [`--last-failed-no-failures`] command-line option that allows to specify the behavior of the cache plugin's [`` `--last-failed ``] feature when no tests failed in the last run (or no cache was found): [`none`] or [`all`] (the default). ([#3139](https://github.com/pytest-dev/pytest/issues/3139))

-   New [`--doctest-continue-on-failure`] command-line option to enable doctests to show multiple failures for each snippet, instead of stopping at the first failure. ([#3149](https://github.com/pytest-dev/pytest/issues/3149))

-   Captured log messages are added to the [`<system-out>`] tag in the generated junit xml file if the [`junit_logging`] ini option is set to [`system-out`]. If the value of this ini option is [`system-err`], the logs are written to [`<system-err>`]. The default value for [`junit_logging`] is [`no`], meaning captured logs are not written to the output file. ([#3156](https://github.com/pytest-dev/pytest/issues/3156))

-   Allow the logging plugin to handle [`pytest_runtest_logstart`] and [`pytest_runtest_logfinish`] hooks when live logs are enabled. ([#3189](https://github.com/pytest-dev/pytest/issues/3189))

-   Passing [`--log-cli-level`] in the command-line now automatically activates live logging. ([#3190](https://github.com/pytest-dev/pytest/issues/3190))

-   Add command line option [`--deselect`] to allow deselection of individual tests at collection time. ([#3198](https://github.com/pytest-dev/pytest/issues/3198))

-   Captured logs are printed before entering pdb. ([#3204](https://github.com/pytest-dev/pytest/issues/3204))

-   Deselected item count is now shown before tests are run, e.g. [`collected`]` `[`X`]` `[`items`]` `[`/`]` `[`Y`]` `[`deselected`]. ([#3213](https://github.com/pytest-dev/pytest/issues/3213))

-   The builtin module [`platform`] is now available for use in expressions in [`pytest.mark`]. ([#3236](https://github.com/pytest-dev/pytest/issues/3236))

-   The *short test summary info* section now is displayed after tracebacks and warnings in the terminal. ([#3255](https://github.com/pytest-dev/pytest/issues/3255))

-   New [`--verbosity`] flag to set verbosity level explicitly. ([#3296](https://github.com/pytest-dev/pytest/issues/3296))

-   [`pytest.approx`] now accepts comparing a numpy array with a scalar. ([#3312](https://github.com/pytest-dev/pytest/issues/3312))

### Bug Fixes[¶](#id827 "Link to this heading")

-   Suppress [`IOError`] when closing the temporary file used for capturing streams in Python 2.7. ([#2370](https://github.com/pytest-dev/pytest/issues/2370))

-   Fixed [`clear()`] method on [`caplog`] fixture which cleared [`records`], but not the [`text`] property. ([#3297](https://github.com/pytest-dev/pytest/issues/3297))

-   During test collection, when stdin is not allowed to be read, the [`DontReadFromStdin`] object still allow itself to be iterable and resolved to an iterator without crashing. ([#3314](https://github.com/pytest-dev/pytest/issues/3314))

### Improved Documentation[¶](#id828 "Link to this heading")

-   Added a [[reference]](reference/reference.html) page to the docs. ([#1713](https://github.com/pytest-dev/pytest/issues/1713))

### Trivial/Internal Changes[¶](#id829 "Link to this heading")

-   Change minimum requirement of [`attrs`] to [`17.4.0`]. ([#3228](https://github.com/pytest-dev/pytest/issues/3228))

-   Renamed example directories so all tests pass when ran from the base directory. ([#3245](https://github.com/pytest-dev/pytest/issues/3245))

-   Internal [`mark.py`] module has been turned into a package. ([#3250](https://github.com/pytest-dev/pytest/issues/3250))

-   [`pytest`] now depends on the [more-itertools](https://github.com/erikrose/more-itertools) package. ([#3265](https://github.com/pytest-dev/pytest/issues/3265))

-   Added warning when [`[pytest]`] section is used in a [`.cfg`] file passed with [`-c`] ([#3268](https://github.com/pytest-dev/pytest/issues/3268))

-   [`nodeids`] can now be passed explicitly to [`FSCollector`] and [`Node`] constructors. ([#3291](https://github.com/pytest-dev/pytest/issues/3291))

-   Internal refactoring of [`FormattedExcinfo`] to use [`attrs`] facilities and remove old support code for legacy Python versions. ([#3292](https://github.com/pytest-dev/pytest/issues/3292))

-   Refactoring to unify how verbosity is handled internally. ([#3296](https://github.com/pytest-dev/pytest/issues/3296))

-   Internal refactoring to better integrate with argparse. ([#3304](https://github.com/pytest-dev/pytest/issues/3304))

-   Fix a python example when calling a fixture in doc/en/usage.rst ([#3308](https://github.com/pytest-dev/pytest/issues/3308))

## pytest 3.4.2 (2018-03-04)[¶](#pytest-3-4-2-2018-03-04 "Link to this heading")

### Bug Fixes[¶](#id830 "Link to this heading")

-   Removed progress information when capture option is [`no`]. ([#3203](https://github.com/pytest-dev/pytest/issues/3203))

-   Refactor check of bindir from [`exists`] to [`isdir`]. ([#3241](https://github.com/pytest-dev/pytest/issues/3241))

-   Fix [`TypeError`] issue when using [`approx`] with a [`Decimal`] value. ([#3247](https://github.com/pytest-dev/pytest/issues/3247))

-   Fix reference cycle generated when using the [`request`] fixture. ([#3249](https://github.com/pytest-dev/pytest/issues/3249))

-   [`[tool:pytest]`] sections in [`*.cfg`] files passed by the [`-c`] option are now properly recognized. ([#3260](https://github.com/pytest-dev/pytest/issues/3260))

### Improved Documentation[¶](#id831 "Link to this heading")

-   Add logging plugin to plugins list. ([#3209](https://github.com/pytest-dev/pytest/issues/3209))

### Trivial/Internal Changes[¶](#id832 "Link to this heading")

-   Fix minor typo in fixture.rst ([#3259](https://github.com/pytest-dev/pytest/issues/3259))

## pytest 3.4.1 (2018-02-20)[¶](#pytest-3-4-1-2018-02-20 "Link to this heading")

### Bug Fixes[¶](#id833 "Link to this heading")

-   Move import of [`doctest.UnexpectedException`] to top-level to avoid possible errors when using [`--pdb`]. ([#1810](https://github.com/pytest-dev/pytest/issues/1810))

-   Added printing of captured stdout/stderr before entering pdb, and improved a test which was giving false negatives about output capturing. ([#3052](https://github.com/pytest-dev/pytest/issues/3052))

-   Fix ordering of tests using parametrized fixtures which can lead to fixtures being created more than necessary. ([#3161](https://github.com/pytest-dev/pytest/issues/3161))

-   Fix bug where logging happening at hooks outside of "test run" hooks would cause an internal error. ([#3184](https://github.com/pytest-dev/pytest/issues/3184))

-   Detect arguments injected by [`unittest.mock.patch`] decorator correctly when pypi [`mock.patch`] is installed and imported. ([#3206](https://github.com/pytest-dev/pytest/issues/3206))

-   Errors shown when a [`pytest.raises()`] with [`match=`] fails are now cleaner on what happened: When no exception was raised, the "matching '...'" part got removed as it falsely implies that an exception was raised but it didn't match. When a wrong exception was raised, it's now thrown (like [`pytest.raised()`] without [`match=`] would) instead of complaining about the unmatched text. ([#3222](https://github.com/pytest-dev/pytest/issues/3222))

-   Fixed output capture handling in doctests on macOS. ([#985](https://github.com/pytest-dev/pytest/issues/985))

### Improved Documentation[¶](#id834 "Link to this heading")

-   Add Sphinx parameter docs for [`match`] and [`message`] args to [`pytest.raises`]. ([#3202](https://github.com/pytest-dev/pytest/issues/3202))

### Trivial/Internal Changes[¶](#id835 "Link to this heading")

-   pytest has changed the publication procedure and is now being published to PyPI directly from Travis. ([#3060](https://github.com/pytest-dev/pytest/issues/3060))

-   Rename [`ParameterSet._for_parameterize()`] to [`_for_parametrize()`] in order to comply with the naming convention. ([#3166](https://github.com/pytest-dev/pytest/issues/3166))

-   Skip failing pdb/doctest test on mac. ([#985](https://github.com/pytest-dev/pytest/issues/985))

## pytest 3.4.0 (2018-01-30)[¶](#pytest-3-4-0-2018-01-30 "Link to this heading")

### Deprecations and Removals[¶](#id836 "Link to this heading")

-   All pytest classes now subclass [`object`] for better Python 2/3 compatibility. This should not affect user code except in very rare edge cases. ([#2147](https://github.com/pytest-dev/pytest/issues/2147))

### Features[¶](#id837 "Link to this heading")

-   Introduce [`empty_parameter_set_mark`] ini option to select which mark to apply when [`@pytest.mark.parametrize`] is given an empty set of parameters. Valid options are [`skip`] (default) and [`xfail`]. Note that it is planned to change the default to [`xfail`] in future releases as this is considered less error prone. ([#2527](https://github.com/pytest-dev/pytest/issues/2527))

-   **Incompatible change**: after community feedback the [[logging]](how-to/logging.html) functionality has undergone some changes. Please consult the [[logging documentation]](how-to/logging.html#log-changes-3-4) for details. ([#3013](https://github.com/pytest-dev/pytest/issues/3013))

-   Console output falls back to "classic" mode when capturing is disabled ([`-s`]), otherwise the output gets garbled to the point of being useless. ([#3038](https://github.com/pytest-dev/pytest/issues/3038))

-   New [[`pytest_runtest_logfinish`]](reference/reference.html#std-hook-pytest_runtest_logfinish) hook which is called when a test item has finished executing, analogous to [[`pytest_runtest_logstart`]](reference/reference.html#std-hook-pytest_runtest_logstart). ([#3101](https://github.com/pytest-dev/pytest/issues/3101))

-   Improve performance when collecting tests using many fixtures. ([#3107](https://github.com/pytest-dev/pytest/issues/3107))

-   New [`caplog.get_records(when)`] method which provides access to the captured records for the [`"setup"`], [`"call"`] and [`"teardown"`] testing stages. ([#3117](https://github.com/pytest-dev/pytest/issues/3117))

-   New fixture [`record_xml_attribute`] that allows modifying and inserting attributes on the [`<testcase>`] xml node in JUnit reports. ([#3130](https://github.com/pytest-dev/pytest/issues/3130))

-   The default cache directory has been renamed from [`.cache`] to [`.pytest_cache`] after community feedback that the name [`.cache`] did not make it clear that it was used by pytest. ([#3138](https://github.com/pytest-dev/pytest/issues/3138))

-   Colorize the levelname column in the live-log output. ([#3142](https://github.com/pytest-dev/pytest/issues/3142))

### Bug Fixes[¶](#id838 "Link to this heading")

-   Fix hanging pexpect test on macOS by using flush() instead of wait(). ([#2022](https://github.com/pytest-dev/pytest/issues/2022))

-   Fix restoring Python state after in-process pytest runs with the [`pytester`] plugin; this may break tests using multiple inprocess pytest runs if later ones depend on earlier ones leaking global interpreter changes. ([#3016](https://github.com/pytest-dev/pytest/issues/3016))

-   Fix skipping plugin reporting hook when test aborted before plugin setup hook. ([#3074](https://github.com/pytest-dev/pytest/issues/3074))

-   Fix progress percentage reported when tests fail during teardown. ([#3088](https://github.com/pytest-dev/pytest/issues/3088))

-   **Incompatible change**: [`-o/--override`] option no longer eats all the remaining options, which can lead to surprising behavior: for example, [`pytest`]` `[`-o`]` `[`foo=1`]` `[`/path/to/test.py`] would fail because [`/path/to/test.py`] would be considered as part of the [`-o`] command-line argument. One consequence of this is that now multiple configuration overrides need multiple [`-o`] flags: [`pytest`]` `[`-o`]` `[`foo=1`]` `[`-o`]` `[`bar=2`]. ([#3103](https://github.com/pytest-dev/pytest/issues/3103))

### Improved Documentation[¶](#id839 "Link to this heading")

-   Document hooks (defined with [`historic=True`]) which cannot be used with [`hookwrapper=True`]. ([#2423](https://github.com/pytest-dev/pytest/issues/2423))

-   Clarify that warning capturing doesn't change the warning filter by default. ([#2457](https://github.com/pytest-dev/pytest/issues/2457))

-   Clarify a possible confusion when using pytest_fixture_setup with fixture functions that return None. ([#2698](https://github.com/pytest-dev/pytest/issues/2698))

-   Fix the wording of a sentence on doctest flags used in pytest. ([#3076](https://github.com/pytest-dev/pytest/issues/3076))

-   Prefer [`https://*.readthedocs.io`] over [`http://*.rtfd.org`] for links in the documentation. ([#3092](https://github.com/pytest-dev/pytest/issues/3092))

-   Improve readability (wording, grammar) of Getting Started guide ([#3131](https://github.com/pytest-dev/pytest/issues/3131))

-   Added note that calling pytest.main multiple times from the same process is not recommended because of import caching. ([#3143](https://github.com/pytest-dev/pytest/issues/3143))

### Trivial/Internal Changes[¶](#id840 "Link to this heading")

-   Show a simple and easy error when keyword expressions trigger a syntax error (for example, [`"-k`]` `[`foo`]` `[`and`]` `[`import"`] will show an error that you cannot use the [`import`] keyword in expressions). ([#2953](https://github.com/pytest-dev/pytest/issues/2953))

-   Change parametrized automatic test id generation to use the [`__name__`] attribute of functions instead of the fallback argument name plus counter. ([#2976](https://github.com/pytest-dev/pytest/issues/2976))

-   Replace py.std with stdlib imports. ([#3067](https://github.com/pytest-dev/pytest/issues/3067))

-   Corrected 'you' to 'your' in logging docs. ([#3129](https://github.com/pytest-dev/pytest/issues/3129))

## pytest 3.3.2 (2017-12-25)[¶](#pytest-3-3-2-2017-12-25 "Link to this heading")

### Bug Fixes[¶](#id841 "Link to this heading")

-   pytester: ignore files used to obtain current user metadata in the fd leak detector. ([#2784](https://github.com/pytest-dev/pytest/issues/2784))

-   Fix **memory leak** where objects returned by fixtures were never destructed by the garbage collector. ([#2981](https://github.com/pytest-dev/pytest/issues/2981))

-   Fix conversion of pyargs to filename to not convert symlinks on Python 2. ([#2985](https://github.com/pytest-dev/pytest/issues/2985))

-   [`PYTEST_DONT_REWRITE`] is now checked for plugins too rather than only for test modules. ([#2995](https://github.com/pytest-dev/pytest/issues/2995))

### Improved Documentation[¶](#id842 "Link to this heading")

-   Add clarifying note about behavior of multiple parametrized arguments ([#3001](https://github.com/pytest-dev/pytest/issues/3001))

### Trivial/Internal Changes[¶](#id843 "Link to this heading")

-   Code cleanup. ([#3015](https://github.com/pytest-dev/pytest/issues/3015), [#3021](https://github.com/pytest-dev/pytest/issues/3021))

-   Clean up code by replacing imports and references of [`_ast`] to [`ast`]. ([#3018](https://github.com/pytest-dev/pytest/issues/3018))

## pytest 3.3.1 (2017-12-05)[¶](#pytest-3-3-1-2017-12-05 "Link to this heading")

### Bug Fixes[¶](#id844 "Link to this heading")

-   Fix issue about [`-p`]` `[`no:<plugin>`] having no effect. ([#2920](https://github.com/pytest-dev/pytest/issues/2920))

-   Fix regression with warnings that contained non-strings in their arguments in Python 2. ([#2956](https://github.com/pytest-dev/pytest/issues/2956))

-   Always escape null bytes when setting [`PYTEST_CURRENT_TEST`]. ([#2957](https://github.com/pytest-dev/pytest/issues/2957))

-   Fix [`ZeroDivisionError`] when using the [`testmon`] plugin when no tests were actually collected. ([#2971](https://github.com/pytest-dev/pytest/issues/2971))

-   Bring back [`TerminalReporter.writer`] as an alias to [`TerminalReporter._tw`]. This alias was removed by accident in the [`3.3.0`] release. ([#2984](https://github.com/pytest-dev/pytest/issues/2984))

-   The [`pytest-capturelog`] plugin is now also blacklisted, avoiding errors when running pytest with it still installed. ([#3004](https://github.com/pytest-dev/pytest/issues/3004))

### Improved Documentation[¶](#id845 "Link to this heading")

-   Fix broken link to plugin [`pytest-localserver`]. ([#2963](https://github.com/pytest-dev/pytest/issues/2963))

### Trivial/Internal Changes[¶](#id846 "Link to this heading")

-   Update github "bugs" link in [`CONTRIBUTING.rst`] ([#2949](https://github.com/pytest-dev/pytest/issues/2949))

## pytest 3.3.0 (2017-11-23)[¶](#pytest-3-3-0-2017-11-23 "Link to this heading")

### Deprecations and Removals[¶](#id847 "Link to this heading")

-   pytest no longer supports Python **2.6** and **3.3**. Those Python versions are EOL for some time now and incur maintenance and compatibility costs on the pytest core team, and following up with the rest of the community we decided that they will no longer be supported starting on this version. Users which still require those versions should pin pytest to [`<3.3`]. ([#2812](https://github.com/pytest-dev/pytest/issues/2812))

-   Remove internal [`_preloadplugins()`] function. This removal is part of the [`pytest_namespace()`] hook deprecation. ([#2636](https://github.com/pytest-dev/pytest/issues/2636))

-   Internally change [`CallSpec2`] to have a list of marks instead of a broken mapping of keywords. This removes the keywords attribute of the internal [`CallSpec2`] class. ([#2672](https://github.com/pytest-dev/pytest/issues/2672))

-   Remove ParameterSet.deprecated_arg_dict - its not a public api and the lack of the underscore was a naming error. ([#2675](https://github.com/pytest-dev/pytest/issues/2675))

-   Remove the internal multi-typed attribute [`Node._evalskip`] and replace it with the boolean [`Node._skipped_by_mark`]. ([#2767](https://github.com/pytest-dev/pytest/issues/2767))

-   The [`params`] list passed to [`pytest.fixture`] is now for all effects considered immutable and frozen at the moment of the [`pytest.fixture`] call. Previously the list could be changed before the first invocation of the fixture allowing for a form of dynamic parametrization (for example, updated from command-line options), but this was an unwanted implementation detail which complicated the internals and prevented some internal cleanup. See issue [#2959](https://github.com/pytest-dev/pytest/issues/2959) for details and a recommended workaround.

### Features[¶](#id848 "Link to this heading")

-   [`pytest_fixture_post_finalizer`] hook can now receive a [`request`] argument. ([#2124](https://github.com/pytest-dev/pytest/issues/2124))

-   Replace the old introspection code in compat.py that determines the available arguments of fixtures with inspect.signature on Python 3 and funcsigs.signature on Python 2. This should respect [`__signature__`] declarations on functions. ([#2267](https://github.com/pytest-dev/pytest/issues/2267))

-   Report tests with global [`pytestmark`] variable only once. ([#2549](https://github.com/pytest-dev/pytest/issues/2549))

-   Now pytest displays the total progress percentage while running tests. The previous output style can be set by configuring the [`console_output_style`] setting to [`classic`]. ([#2657](https://github.com/pytest-dev/pytest/issues/2657))

-   Match [`warns`] signature to [`raises`] by adding [`match`] keyword. ([#2708](https://github.com/pytest-dev/pytest/issues/2708))

-   pytest now captures and displays output from the standard [`logging`] module. The user can control the logging level to be captured by specifying options in [`pytest.ini`], the command line and also during individual tests using markers. Also, a [`caplog`] fixture is available that enables users to test the captured log during specific tests (similar to [`capsys`] for example). For more information, please see the [[logging docs]](how-to/logging.html). This feature was introduced by merging the popular [pytest-catchlog](https://pypi.org/project/pytest-catchlog) plugin, thanks to [\@thisch](https://github.com/sponsors/thisch). Be advised that during the merging the backward compatibility interface with the defunct [`pytest-capturelog`] has been dropped. ([#2794](https://github.com/pytest-dev/pytest/issues/2794))

-   Add [`allow_module_level`] kwarg to [`pytest.skip()`], enabling to skip the whole module. ([#2808](https://github.com/pytest-dev/pytest/issues/2808))

-   Allow setting [`file_or_dir`], [`-c`], and [`-o`] in PYTEST_ADDOPTS. ([#2824](https://github.com/pytest-dev/pytest/issues/2824))

-   Return stdout/stderr capture results as a [`namedtuple`], so [`out`] and [`err`] can be accessed by attribute. ([#2879](https://github.com/pytest-dev/pytest/issues/2879))

-   Add [`capfdbinary`], a version of [`capfd`] which returns bytes from [`readouterr()`]. ([#2923](https://github.com/pytest-dev/pytest/issues/2923))

-   Add [`capsysbinary`] a version of [`capsys`] which returns bytes from [`readouterr()`]. ([#2934](https://github.com/pytest-dev/pytest/issues/2934))

-   Implement feature to skip [`setup.py`] files when run with [`--doctest-modules`]. ([#502](https://github.com/pytest-dev/pytest/issues/502))

### Bug Fixes[¶](#id849 "Link to this heading")

-   Resume output capturing after [`capsys/capfd.disabled()`] context manager. ([#1993](https://github.com/pytest-dev/pytest/issues/1993))

-   [`pytest_fixture_setup`] and [`pytest_fixture_post_finalizer`] hooks are now called for all [`conftest.py`] files. ([#2124](https://github.com/pytest-dev/pytest/issues/2124))

-   If an exception happens while loading a plugin, pytest no longer hides the original traceback. In Python 2 it will show the original traceback with a new message that explains in which plugin. In Python 3 it will show 2 canonized exceptions, the original exception while loading the plugin in addition to an exception that pytest throws about loading a plugin. ([#2491](https://github.com/pytest-dev/pytest/issues/2491))

-   [`capsys`] and [`capfd`] can now be used by other fixtures. ([#2709](https://github.com/pytest-dev/pytest/issues/2709))

-   Internal [`pytester`] plugin properly encodes [`bytes`] arguments to [`utf-8`]. ([#2738](https://github.com/pytest-dev/pytest/issues/2738))

-   [`testdir`] now uses use the same method used by [`tmpdir`] to create its temporary directory. This changes the final structure of the [`testdir`] directory slightly, but should not affect usage in normal scenarios and avoids a number of potential problems. ([#2751](https://github.com/pytest-dev/pytest/issues/2751))

-   pytest no longer complains about warnings with unicode messages being non-ascii compatible even for ascii-compatible messages. As a result of this, warnings with unicode messages are converted first to an ascii representation for safety. ([#2809](https://github.com/pytest-dev/pytest/issues/2809))

-   Change return value of pytest command when [`--maxfail`] is reached from [`2`] (interrupted) to [`1`] (failed). ([#2845](https://github.com/pytest-dev/pytest/issues/2845))

-   Fix issue in assertion rewriting which could lead it to rewrite modules which should not be rewritten. ([#2939](https://github.com/pytest-dev/pytest/issues/2939))

-   Handle marks without description in [`pytest.ini`]. ([#2942](https://github.com/pytest-dev/pytest/issues/2942))

### Trivial/Internal Changes[¶](#id850 "Link to this heading")

-   pytest now depends on [attrs](https://pypi.org/project/attrs) for internal structures to ease code maintainability. ([#2641](https://github.com/pytest-dev/pytest/issues/2641))

-   Refactored internal Python 2/3 compatibility code to use [`six`]. ([#2642](https://github.com/pytest-dev/pytest/issues/2642))

-   Stop vendoring [`pluggy`] - we're missing out on its latest changes for not much benefit ([#2719](https://github.com/pytest-dev/pytest/issues/2719))

-   Internal refactor: simplify ascii string escaping by using the backslashreplace error handler in newer Python 3 versions. ([#2734](https://github.com/pytest-dev/pytest/issues/2734))

-   Remove unnecessary mark evaluator in unittest plugin ([#2767](https://github.com/pytest-dev/pytest/issues/2767))

-   Calls to [`Metafunc.addcall`] now emit a deprecation warning. This function is scheduled to be removed in [`pytest-4.0`]. ([#2876](https://github.com/pytest-dev/pytest/issues/2876))

-   Internal move of the parameterset extraction to a more maintainable place. ([#2877](https://github.com/pytest-dev/pytest/issues/2877))

-   Internal refactoring to simplify scope node lookup. ([#2910](https://github.com/pytest-dev/pytest/issues/2910))

-   Configure [`pytest`] to prevent pip from installing pytest in unsupported Python versions. ([#2922](https://github.com/pytest-dev/pytest/issues/2922))

## pytest 3.2.5 (2017-11-15)[¶](#pytest-3-2-5-2017-11-15 "Link to this heading")

### Bug Fixes[¶](#id851 "Link to this heading")

-   Remove [`py<1.5`] restriction from [`pytest`] as this can cause version conflicts in some installations. ([#2926](https://github.com/pytest-dev/pytest/issues/2926))

## pytest 3.2.4 (2017-11-13)[¶](#pytest-3-2-4-2017-11-13 "Link to this heading")

### Bug Fixes[¶](#id852 "Link to this heading")

-   Fix the bug where running with [`--pyargs`] will result in items with empty [`parent.nodeid`] if run from a different root directory. ([#2775](https://github.com/pytest-dev/pytest/issues/2775))

-   Fix issue with [`@pytest.parametrize`] if argnames was specified as keyword arguments. ([#2819](https://github.com/pytest-dev/pytest/issues/2819))

-   Strip whitespace from marker names when reading them from INI config. ([#2856](https://github.com/pytest-dev/pytest/issues/2856))

-   Show full context of doctest source in the pytest output, if the line number of failed example in the docstring is \< 9. ([#2882](https://github.com/pytest-dev/pytest/issues/2882))

-   Match fixture paths against actual path segments in order to avoid matching folders which share a prefix. ([#2836](https://github.com/pytest-dev/pytest/issues/2836))

### Improved Documentation[¶](#id853 "Link to this heading")

-   Introduce a dedicated section about conftest.py. ([#1505](https://github.com/pytest-dev/pytest/issues/1505))

-   Explicitly mention [`xpass`] in the documentation of [`xfail`]. ([#1997](https://github.com/pytest-dev/pytest/issues/1997))

-   Append example for pytest.param in the example/parametrize document. ([#2658](https://github.com/pytest-dev/pytest/issues/2658))

-   Clarify language of proposal for fixtures parameters ([#2893](https://github.com/pytest-dev/pytest/issues/2893))

-   List python 3.6 in the documented supported versions in the getting started document. ([#2903](https://github.com/pytest-dev/pytest/issues/2903))

-   Clarify the documentation of available fixture scopes. ([#538](https://github.com/pytest-dev/pytest/issues/538))

-   Add documentation about the [`python`]` `[`-m`]` `[`pytest`] invocation adding the current directory to sys.path. ([#911](https://github.com/pytest-dev/pytest/issues/911))

## pytest 3.2.3 (2017-10-03)[¶](#pytest-3-2-3-2017-10-03 "Link to this heading")

### Bug Fixes[¶](#id854 "Link to this heading")

-   Fix crash in tab completion when no prefix is given. ([#2748](https://github.com/pytest-dev/pytest/issues/2748))

-   The equality checking function ([`__eq__`]) of [`MarkDecorator`] returns [`False`] if one object is not an instance of [`MarkDecorator`]. ([#2758](https://github.com/pytest-dev/pytest/issues/2758))

-   When running [`pytest`]` `[`--fixtures-per-test`]: don't crash if an item has no \_fixtureinfo attribute (e.g. doctests) ([#2788](https://github.com/pytest-dev/pytest/issues/2788))

### Improved Documentation[¶](#id855 "Link to this heading")

-   In help text of [`-k`] option, add example of using [`not`] to not select certain tests whose names match the provided expression. ([#1442](https://github.com/pytest-dev/pytest/issues/1442))

-   Add note in [`parametrize.rst`] about calling [`metafunc.parametrize`] multiple times. ([#1548](https://github.com/pytest-dev/pytest/issues/1548))

### Trivial/Internal Changes[¶](#id856 "Link to this heading")

-   Set [`xfail_strict=True`] in pytest's own test suite to catch expected failures as soon as they start to pass. ([#2722](https://github.com/pytest-dev/pytest/issues/2722))

-   Fix typo in example of passing a callable to markers (in example/markers.rst) ([#2765](https://github.com/pytest-dev/pytest/issues/2765))

## pytest 3.2.2 (2017-09-06)[¶](#pytest-3-2-2-2017-09-06 "Link to this heading")

### Bug Fixes[¶](#id857 "Link to this heading")

-   Calling the deprecated [`request.getfuncargvalue()`] now shows the source of the call. ([#2681](https://github.com/pytest-dev/pytest/issues/2681))

-   Allow tests declared as [`@staticmethod`] to use fixtures. ([#2699](https://github.com/pytest-dev/pytest/issues/2699))

-   Fixed edge-case during collection: attributes which raised [`pytest.fail`] when accessed would abort the entire collection. ([#2707](https://github.com/pytest-dev/pytest/issues/2707))

-   Fix [`ReprFuncArgs`] with mixed unicode and UTF-8 args. ([#2731](https://github.com/pytest-dev/pytest/issues/2731))

### Improved Documentation[¶](#id858 "Link to this heading")

-   In examples on working with custom markers, add examples demonstrating the usage of [`pytest.mark.MARKER_NAME.with_args`] in comparison with [`pytest.mark.MARKER_NAME.__call__`] ([#2604](https://github.com/pytest-dev/pytest/issues/2604))

-   In one of the simple examples, use [`pytest_collection_modifyitems()`] to skip tests based on a command-line option, allowing its sharing while preventing a user error when accessing [`pytest.config`] before the argument parsing. ([#2653](https://github.com/pytest-dev/pytest/issues/2653))

### Trivial/Internal Changes[¶](#id859 "Link to this heading")

-   Fixed minor error in 'Good Practices/Manual Integration' code snippet. ([#2691](https://github.com/pytest-dev/pytest/issues/2691))

-   Fixed typo in goodpractices.rst. ([#2721](https://github.com/pytest-dev/pytest/issues/2721))

-   Improve user guidance regarding [`--resultlog`] deprecation. ([#2739](https://github.com/pytest-dev/pytest/issues/2739))

## pytest 3.2.1 (2017-08-08)[¶](#pytest-3-2-1-2017-08-08 "Link to this heading")

### Bug Fixes[¶](#id860 "Link to this heading")

-   Fixed small terminal glitch when collecting a single test item. ([#2579](https://github.com/pytest-dev/pytest/issues/2579))

-   Correctly consider [`/`] as the file separator to automatically mark plugin files for rewrite on Windows. ([#2591](https://github.com/pytest-dev/pytest/issues/2591))

-   Properly escape test names when setting [`PYTEST_CURRENT_TEST`] environment variable. ([#2644](https://github.com/pytest-dev/pytest/issues/2644))

-   Fix error on Windows and Python 3.6+ when [`sys.stdout`] has been replaced with a stream-like object which does not implement the full [`io`] module buffer protocol. In particular this affects [`pytest-xdist`] users on the aforementioned platform. ([#2666](https://github.com/pytest-dev/pytest/issues/2666))

### Improved Documentation[¶](#id861 "Link to this heading")

-   Explicitly document which pytest features work with [`unittest`]. ([#2626](https://github.com/pytest-dev/pytest/issues/2626))

## pytest 3.2.0 (2017-07-30)[¶](#pytest-3-2-0-2017-07-30 "Link to this heading")

### Deprecations and Removals[¶](#id862 "Link to this heading")

-   [`pytest.approx`] no longer supports [`>`], [`>=`], [`<`] and [`<=`] operators to avoid surprising/inconsistent behavior. See the [[`approx()`]](reference/reference.html#pytest.approx "pytest.approx") docs for more information. ([#2003](https://github.com/pytest-dev/pytest/issues/2003))

-   All old-style specific behavior in current classes in the pytest's API is considered deprecated at this point and will be removed in a future release. This affects Python 2 users only and in rare situations. ([#2147](https://github.com/pytest-dev/pytest/issues/2147))

-   A deprecation warning is now raised when using marks for parameters in [`pytest.mark.parametrize`]. Use [`pytest.param`] to apply marks to parameters instead. ([#2427](https://github.com/pytest-dev/pytest/issues/2427))

### Features[¶](#id863 "Link to this heading")

-   Add support for numpy arrays (and dicts) to approx. ([#1994](https://github.com/pytest-dev/pytest/issues/1994))

-   Now test function objects have a [`pytestmark`] attribute containing a list of marks applied directly to the test function, as opposed to marks inherited from parent classes or modules. ([#2516](https://github.com/pytest-dev/pytest/issues/2516))

-   Collection ignores local virtualenvs by default; [`--collect-in-virtualenv`] overrides this behavior. ([#2518](https://github.com/pytest-dev/pytest/issues/2518))

-   Allow class methods decorated as [`@staticmethod`] to be candidates for collection as a test function. (Only for Python 2.7 and above. Python 2.6 will still ignore static methods.) ([#2528](https://github.com/pytest-dev/pytest/issues/2528))

-   Introduce [`mark.with_args`] in order to allow passing functions/classes as sole argument to marks. ([#2540](https://github.com/pytest-dev/pytest/issues/2540))

-   New [`cache_dir`] ini option: sets the directory where the contents of the cache plugin are stored. Directory may be relative or absolute path: if relative path, then directory is created relative to [`rootdir`], otherwise it is used as is. Additionally path may contain environment variables which are expanded during runtime. ([#2543](https://github.com/pytest-dev/pytest/issues/2543))

-   Introduce the [`PYTEST_CURRENT_TEST`] environment variable that is set with the [`nodeid`] and stage ([`setup`], [`call`] and [`teardown`]) of the test being currently executed. See the [[documentation]](example/simple.html#pytest-current-test-env) for more info. ([#2583](https://github.com/pytest-dev/pytest/issues/2583))

-   Introduced [`@pytest.mark.filterwarnings`] mark which allows overwriting the warnings filter on a per test, class or module level. See the [[docs]](how-to/capture-warnings.html#filterwarnings) for more information. ([#2598](https://github.com/pytest-dev/pytest/issues/2598))

-   [`--last-failed`] now remembers forever when a test has failed and only forgets it if it passes again. This makes it easy to fix a test suite by selectively running files and fixing tests incrementally. ([#2621](https://github.com/pytest-dev/pytest/issues/2621))

-   New [`pytest_report_collectionfinish`] hook which allows plugins to add messages to the terminal reporting after collection has been finished successfully. ([#2622](https://github.com/pytest-dev/pytest/issues/2622))

-   Added support for [][**PEP 415**](https://peps.python.org/pep-0415/)\'s [`Exception.__suppress_context__`]. Now if a [`raise`]` `[`exception`]` `[`from`]` `[`None`] is caught by pytest, pytest will no longer chain the context in the test report. The behavior now matches Python's traceback behavior. ([#2631](https://github.com/pytest-dev/pytest/issues/2631))

-   Exceptions raised by [`pytest.fail`], [`pytest.skip`] and [`pytest.xfail`] now subclass BaseException, making them harder to be caught unintentionally by normal code. ([#580](https://github.com/pytest-dev/pytest/issues/580))

### Bug Fixes[¶](#id864 "Link to this heading")

-   Set [`stdin`] to a closed [`PIPE`] in [`pytester.py.Testdir.popen()`] for avoid unwanted interactive [`pdb`] ([#2023](https://github.com/pytest-dev/pytest/issues/2023))

-   Add missing [`encoding`] attribute to [`sys.std*`] streams when using [`capsys`] capture mode. ([#2375](https://github.com/pytest-dev/pytest/issues/2375))

-   Fix terminal color changing to black on Windows if [`colorama`] is imported in a [`conftest.py`] file. ([#2510](https://github.com/pytest-dev/pytest/issues/2510))

-   Fix line number when reporting summary of skipped tests. ([#2548](https://github.com/pytest-dev/pytest/issues/2548))

-   capture: ensure that EncodedFile.name is a string. ([#2555](https://github.com/pytest-dev/pytest/issues/2555))

-   The options [`--fixtures`] and [`--fixtures-per-test`] will now keep indentation within docstrings. ([#2574](https://github.com/pytest-dev/pytest/issues/2574))

-   doctests line numbers are now reported correctly, fixing [pytest-sugar#122](https://github.com/Frozenball/pytest-sugar/issues/122). ([#2610](https://github.com/pytest-dev/pytest/issues/2610))

-   Fix non-determinism in order of fixture collection. Adds new dependency (ordereddict) for Python 2.6. ([#920](https://github.com/pytest-dev/pytest/issues/920))

### Improved Documentation[¶](#id865 "Link to this heading")

-   Clarify [`pytest_configure`] hook call order. ([#2539](https://github.com/pytest-dev/pytest/issues/2539))

-   Extend documentation for testing plugin code with the [`pytester`] plugin. ([#971](https://github.com/pytest-dev/pytest/issues/971))

### Trivial/Internal Changes[¶](#id866 "Link to this heading")

-   Update help message for [`--strict`] to make it clear it only deals with unregistered markers, not warnings. ([#2444](https://github.com/pytest-dev/pytest/issues/2444))

-   Internal code move: move code for pytest.approx/pytest.raises to own files in order to cut down the size of python.py ([#2489](https://github.com/pytest-dev/pytest/issues/2489))

-   Renamed the utility function [`_pytest.compat._escape_strings`] to [`_ascii_escaped`] to better communicate the function's purpose. ([#2533](https://github.com/pytest-dev/pytest/issues/2533))

-   Improve error message for CollectError with skip/skipif. ([#2546](https://github.com/pytest-dev/pytest/issues/2546))

-   Emit warning about [`yield`] tests being deprecated only once per generator. ([#2562](https://github.com/pytest-dev/pytest/issues/2562))

-   Ensure final collected line doesn't include artifacts of previous write. ([#2571](https://github.com/pytest-dev/pytest/issues/2571))

-   Fixed all flake8 errors and warnings. ([#2581](https://github.com/pytest-dev/pytest/issues/2581))

-   Added [`fix-lint`] tox environment to run automatic pep8 fixes on the code. ([#2582](https://github.com/pytest-dev/pytest/issues/2582))

-   Turn warnings into errors in pytest's own test suite in order to catch regressions due to deprecations more promptly. ([#2588](https://github.com/pytest-dev/pytest/issues/2588))

-   Show multiple issue links in CHANGELOG entries. ([#2620](https://github.com/pytest-dev/pytest/issues/2620))

## pytest 3.1.3 (2017-07-03)[¶](#pytest-3-1-3-2017-07-03 "Link to this heading")

### Bug Fixes[¶](#id867 "Link to this heading")

-   Fix decode error in Python 2 for doctests in docstrings. ([#2434](https://github.com/pytest-dev/pytest/issues/2434))

-   Exceptions raised during teardown by finalizers are now suppressed until all finalizers are called, with the initial exception reraised. ([#2440](https://github.com/pytest-dev/pytest/issues/2440))

-   Fix incorrect "collected items" report when specifying tests on the command- line. ([#2464](https://github.com/pytest-dev/pytest/issues/2464))

-   [`deprecated_call`] in context-manager form now captures deprecation warnings even if the same warning has already been raised. Also, [`deprecated_call`] will always produce the same error message (previously it would produce different messages in context-manager vs. function-call mode). ([#2469](https://github.com/pytest-dev/pytest/issues/2469))

-   Fix issue where paths collected by pytest could have triple leading [`/`] characters. ([#2475](https://github.com/pytest-dev/pytest/issues/2475))

-   Fix internal error when trying to detect the start of a recursive traceback. ([#2486](https://github.com/pytest-dev/pytest/issues/2486))

### Improved Documentation[¶](#id868 "Link to this heading")

-   Explicitly state for which hooks the calls stop after the first non-None result. ([#2493](https://github.com/pytest-dev/pytest/issues/2493))

### Trivial/Internal Changes[¶](#id869 "Link to this heading")

-   Create invoke tasks for updating the vendored packages. ([#2474](https://github.com/pytest-dev/pytest/issues/2474))

-   Update copyright dates in LICENSE, README.rst and in the documentation. ([#2499](https://github.com/pytest-dev/pytest/issues/2499))

## pytest 3.1.2 (2017-06-08)[¶](#pytest-3-1-2-2017-06-08 "Link to this heading")

### Bug Fixes[¶](#id870 "Link to this heading")

-   Required options added via [`pytest_addoption`] will no longer prevent using --help without passing them. (#1999)

-   Respect [`python_files`] in assertion rewriting. (#2121)

-   Fix recursion error detection when frames in the traceback contain objects that can't be compared (like [`numpy`] arrays). (#2459)

-   [`UnicodeWarning`] is issued from the internal pytest warnings plugin only when the message contains non-ascii unicode (Python 2 only). (#2463)

-   Added a workaround for Python 3.6 [`WindowsConsoleIO`] breaking due to Pytests's [`FDCapture`]. Other code using console handles might still be affected by the very same issue and might require further workarounds/fixes, i.e. [`colorama`]. (#2467)

### Improved Documentation[¶](#id871 "Link to this heading")

-   Fix internal API links to [`pluggy`] objects. (#2331)

-   Make it clear that [`pytest.xfail`] stops test execution at the calling point and improve overall flow of the [`skipping`] docs. (#810)

## pytest 3.1.1 (2017-05-30)[¶](#pytest-3-1-1-2017-05-30 "Link to this heading")

### Bug Fixes[¶](#id872 "Link to this heading")

-   pytest warning capture no longer overrides existing warning filters. The previous behaviour would override all filters and caused regressions in test suites which configure warning filters to match their needs. Note that as a side-effect of this is that [`DeprecationWarning`] and [`PendingDeprecationWarning`] are no longer shown by default. (#2430)

-   Fix issue with non-ascii contents in doctest text files. (#2434)

-   Fix encoding errors for unicode warnings in Python 2. (#2436)

-   [`pytest.deprecated_call`] now captures [`PendingDeprecationWarning`] in context manager form. (#2441)

### Improved Documentation[¶](#id873 "Link to this heading")

-   Addition of towncrier for changelog management. (#2390)

## 3.1.0 (2017-05-22)[¶](#id874 "Link to this heading")

### New Features[¶](#id875 "Link to this heading")

-   The [`pytest-warnings`] plugin has been integrated into the core and now [`pytest`] automatically captures and displays warnings at the end of the test session.

    ::: 
    Warning

    This feature may disrupt test suites which apply and treat warnings themselves, and can be disabled in your [`pytest.ini`]:

    ::: 
    ::: highlight
        [pytest]
        addopts = -p no:warnings
    :::
    :::

    See the [[warnings documentation page]](how-to/capture-warnings.html) for more information.
    :::

    Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Added [`junit_suite_name`] ini option to specify root [`<testsuite>`] name for JUnit XML reports ([#533](https://github.com/pytest-dev/pytest/issues/533)).

-   Added an ini option [`doctest_encoding`] to specify which encoding to use for doctest files. Thanks [\@wheerd](https://github.com/sponsors/wheerd) for the PR ([#2101](https://github.com/pytest-dev/pytest/pull/2101)).

-   [`pytest.warns`] now checks for subclass relationship rather than class equality. Thanks [\@lesteve](https://github.com/sponsors/lesteve) for the PR ([#2166](https://github.com/pytest-dev/pytest/pull/2166))

-   [`pytest.raises`] now asserts that the error message matches a text or regex with the [`match`] keyword argument. Thanks [\@Kriechi](https://github.com/sponsors/Kriechi) for the PR.

-   [`pytest.param`] can be used to declare test parameter sets with marks and test ids. Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

### Changes[¶](#changes "Link to this heading")

-   remove all internal uses of pytest_namespace hooks, this is to prepare the removal of preloadconfig in pytest 4.0 Thanks to [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

-   pytest now warns when a callable ids raises in a parametrized test. Thanks [\@fogo](https://github.com/sponsors/fogo) for the PR.

-   It is now possible to skip test classes from being collected by setting a [`__test__`] attribute to [`False`] in the class body ([#2007](https://github.com/pytest-dev/pytest/issues/2007)). Thanks to [\@syre](https://github.com/sponsors/syre) for the report and [\@lwm](https://github.com/sponsors/lwm) for the PR.

-   Change junitxml.py to produce reports that comply with Junitxml schema. If the same test fails with failure in call and then errors in teardown we split testcase element into two, one containing the error and the other the failure. ([#2228](https://github.com/pytest-dev/pytest/issues/2228)) Thanks to [\@kkoukiou](https://github.com/sponsors/kkoukiou) for the PR.

-   Testcase reports with a [`url`] attribute will now properly write this to junitxml. Thanks [\@fushi](https://github.com/sponsors/fushi) for the PR ([#1874](https://github.com/pytest-dev/pytest/pull/1874)).

-   Remove common items from dict comparison output when verbosity=1. Also update the truncation message to make it clearer that pytest truncates all assertion messages if verbosity \< 2 ([#1512](https://github.com/pytest-dev/pytest/issues/1512)). Thanks [\@mattduck](https://github.com/sponsors/mattduck) for the PR

-   [`--pdbcls`] no longer implies [`--pdb`]. This makes it possible to use [`addopts=--pdbcls=module.SomeClass`] on [`pytest.ini`]. Thanks [\@davidszotten](https://github.com/sponsors/davidszotten) for the PR ([#1952](https://github.com/pytest-dev/pytest/pull/1952)).

-   fix [#2013](https://github.com/pytest-dev/pytest/issues/2013): turn RecordedWarning into [`namedtuple`], to give it a comprehensible repr while preventing unwarranted modification.

-   fix [#2208](https://github.com/pytest-dev/pytest/issues/2208): ensure an iteration limit for [`_pytest.compat.get_real_func`]. Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the report and PR.

-   Hooks are now verified after collection is complete, rather than right after loading installed plugins. This makes it easy to write hooks for plugins which will be loaded during collection, for example using the [`pytest_plugins`] special variable ([#1821](https://github.com/pytest-dev/pytest/issues/1821)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Modify [`pytest_make_parametrize_id()`] hook to accept [`argname`] as an additional parameter. Thanks [\@unsignedint](https://github.com/sponsors/unsignedint) for the PR.

-   Add [`venv`] to the default [`norecursedirs`] setting. Thanks [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the PR.

-   [`PluginManager.import_plugin`] now accepts unicode plugin names in Python 2. Thanks [\@reutsharabani](https://github.com/sponsors/reutsharabani) for the PR.

-   fix [#2308](https://github.com/pytest-dev/pytest/issues/2308): When using both [`--lf`] and [`--ff`], only the last failed tests are run. Thanks [\@ojii](https://github.com/sponsors/ojii) for the PR.

-   Replace minor/patch level version numbers in the documentation with placeholders. This significantly reduces change-noise as different contributors regenerate the documentation on different platforms. Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

-   fix [#2391](https://github.com/pytest-dev/pytest/issues/2391): consider pytest_plugins on all plugin modules Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

### Bug Fixes[¶](#id876 "Link to this heading")

-   Fix [`AttributeError`] on [`sys.stdout.buffer`] / [`sys.stderr.buffer`] while using [`capsys`] fixture in python 3. ([#1407](https://github.com/pytest-dev/pytest/issues/1407)). Thanks to [\@asottile](https://github.com/sponsors/asottile).

-   Change capture.py's [`DontReadFromInput`] class to throw [`io.UnsupportedOperation`] errors rather than ValueErrors in the [`fileno`] method ([#2276](https://github.com/pytest-dev/pytest/issues/2276)). Thanks [\@metasyn](https://github.com/sponsors/metasyn) and [\@vlad-dragos](https://github.com/sponsors/vlad-dragos) for the PR.

-   Fix exception formatting while importing modules when the exception message contains non-ascii characters ([#2336](https://github.com/pytest-dev/pytest/issues/2336)). Thanks [\@fabioz](https://github.com/sponsors/fabioz) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Added documentation related to issue ([#1937](https://github.com/pytest-dev/pytest/issues/1937)) Thanks [\@skylarjhdownes](https://github.com/sponsors/skylarjhdownes) for the PR.

-   Allow collecting files with any file extension as Python modules ([#2369](https://github.com/pytest-dev/pytest/issues/2369)). Thanks [\@Kodiologist](https://github.com/sponsors/Kodiologist) for the PR.

-   Show the correct error message when collect "parametrize" func with wrong args ([#2383](https://github.com/pytest-dev/pytest/issues/2383)). Thanks [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the report and [\@robin0371](https://github.com/sponsors/robin0371) for the PR.

## 3.0.7 (2017-03-14)[¶](#id877 "Link to this heading")

-   Fix issue in assertion rewriting breaking due to modules silently discarding other modules when importing fails Notably, importing the [`anydbm`] module is fixed. ([#2248](https://github.com/pytest-dev/pytest/issues/2248)). Thanks [\@pfhayes](https://github.com/sponsors/pfhayes) for the PR.

-   junitxml: Fix problematic case where system-out tag occurred twice per testcase element in the XML report. Thanks [\@kkoukiou](https://github.com/sponsors/kkoukiou) for the PR.

-   Fix regression, pytest now skips unittest correctly if run with [`--pdb`] ([#2137](https://github.com/pytest-dev/pytest/issues/2137)). Thanks to [\@gst](https://github.com/sponsors/gst) for the report and [\@mbyt](https://github.com/sponsors/mbyt) for the PR.

-   Ignore exceptions raised from descriptors (e.g. properties) during Python test collection ([#2234](https://github.com/pytest-dev/pytest/issues/2234)). Thanks to [\@bluetech](https://github.com/sponsors/bluetech).

-   [`--override-ini`] now correctly overrides some fundamental options like [`python_files`] ([#2238](https://github.com/pytest-dev/pytest/issues/2238)). Thanks [\@sirex](https://github.com/sponsors/sirex) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Replace [`raise`]` `[`StopIteration`] usages in the code by simple [`returns`] to finish generators, in accordance to [][**PEP 479**](https://peps.python.org/pep-0479/) ([#2160](https://github.com/pytest-dev/pytest/issues/2160)). Thanks to [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix internal errors when an unprintable [`AssertionError`] is raised inside a test. Thanks [\@omerhadari](https://github.com/sponsors/omerhadari) for the PR.

-   Skipping plugin now also works with test items generated by custom collectors ([#2231](https://github.com/pytest-dev/pytest/issues/2231)). Thanks to [\@vidartf](https://github.com/sponsors/vidartf).

-   Fix trailing whitespace in console output if no .ini file presented ([#2281](https://github.com/pytest-dev/pytest/issues/2281)). Thanks [\@fbjorn](https://github.com/sponsors/fbjorn) for the PR.

-   Conditionless [`xfail`] markers no longer rely on the underlying test item being an instance of [`PyobjMixin`], and can therefore apply to tests not collected by the built-in python test collector. Thanks [\@barneygale](https://github.com/sponsors/barneygale) for the PR.

## 3.0.6 (2017-01-22)[¶](#id878 "Link to this heading")

-   pytest no longer generates [`PendingDeprecationWarning`] from its own operations, which was introduced by mistake in version [`3.0.5`] ([#2118](https://github.com/pytest-dev/pytest/issues/2118)). Thanks to [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the report and [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

-   pytest no longer recognizes coroutine functions as yield tests ([#2129](https://github.com/pytest-dev/pytest/issues/2129)). Thanks to [\@malinoff](https://github.com/sponsors/malinoff) for the PR.

-   Plugins loaded by the [`PYTEST_PLUGINS`] environment variable are now automatically considered for assertion rewriting ([#2185](https://github.com/pytest-dev/pytest/issues/2185)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Improve error message when pytest.warns fails ([#2150](https://github.com/pytest-dev/pytest/issues/2150)). The type(s) of the expected warnings and the list of caught warnings is added to the error message. Thanks [\@lesteve](https://github.com/sponsors/lesteve) for the PR.

-   Fix [`pytester`] internal plugin to work correctly with latest versions of [`zope.interface`] ([#1989](https://github.com/pytest-dev/pytest/issues/1989)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Assert statements of the [`pytester`] plugin again benefit from assertion rewriting ([#1920](https://github.com/pytest-dev/pytest/issues/1920)). Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Specifying tests with colons like [`test_foo.py::test_bar`] for tests in subdirectories with ini configuration files now uses the correct ini file ([#2148](https://github.com/pytest-dev/pytest/issues/2148)). Thanks [\@pelme](https://github.com/sponsors/pelme).

-   Fail [`testdir.runpytest().assert_outcomes()`] explicitly if the pytest terminal output it relies on is missing. Thanks to [\@eli-b](https://github.com/sponsors/eli-b) for the PR.

## 3.0.5 (2016-12-05)[¶](#id879 "Link to this heading")

-   Add warning when not passing [`option=value`] correctly to [`-o/--override-ini`] ([#2105](https://github.com/pytest-dev/pytest/issues/2105)). Also improved the help documentation. Thanks to [\@mbukatov](https://github.com/sponsors/mbukatov) for the report and [\@lwm](https://github.com/sponsors/lwm) for the PR.

-   Now [`--confcutdir`] and [`--junit-xml`] are properly validated if they are directories and filenames, respectively ([#2089](https://github.com/pytest-dev/pytest/issues/2089) and [#2078](https://github.com/pytest-dev/pytest/issues/2078)). Thanks to [\@lwm](https://github.com/sponsors/lwm) for the PR.

-   Add hint to error message hinting possible missing [`__init__.py`] ([#478](https://github.com/pytest-dev/pytest/issues/478)). Thanks [\@DuncanBetts](https://github.com/sponsors/DuncanBetts).

-   More accurately describe when fixture finalization occurs in documentation ([#687](https://github.com/pytest-dev/pytest/issues/687)). Thanks [\@DuncanBetts](https://github.com/sponsors/DuncanBetts).

-   Provide [`:ref:`] targets for [`recwarn.rst`] so we can use intersphinx referencing. Thanks to [\@dupuy](https://github.com/sponsors/dupuy) for the report and [\@lwm](https://github.com/sponsors/lwm) for the PR.

-   In Python 2, use a simple [`+-`] ASCII string in the string representation of [`pytest.approx`] (for example [`"4`]` `[`+-`]` `[`4.0e-06"`]) because it is brittle to handle that in different contexts and representations internally in pytest which can result in bugs such as [#2111](https://github.com/pytest-dev/pytest/issues/2111). In Python 3, the representation still uses [`±`] (for example [`4`]` `[`±`]` `[`4.0e-06`]). Thanks [\@kerrick-lyft](https://github.com/sponsors/kerrick-lyft) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Using [`item.Function`], [`item.Module`], etc., is now issuing deprecation warnings, prefer [`pytest.Function`], [`pytest.Module`], etc., instead ([#2034](https://github.com/pytest-dev/pytest/issues/2034)). Thanks [\@nmundar](https://github.com/sponsors/nmundar) for the PR.

-   Fix error message using [`approx`] with complex numbers ([#2082](https://github.com/pytest-dev/pytest/issues/2082)). Thanks [\@adler-j](https://github.com/sponsors/adler-j) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fixed false-positives warnings from assertion rewrite hook for modules imported more than once by the [`pytest_plugins`] mechanism. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Remove an internal cache which could cause hooks from [`conftest.py`] files in sub-directories to be called in other directories incorrectly ([#2016](https://github.com/pytest-dev/pytest/issues/2016)). Thanks [\@d-b-w](https://github.com/sponsors/d-b-w) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Remove internal code meant to support earlier Python 3 versions that produced the side effect of leaving [`None`] in [`sys.modules`] when expressions were evaluated by pytest (for example passing a condition as a string to [`pytest.mark.skipif`])([#2103](https://github.com/pytest-dev/pytest/issues/2103)). Thanks [\@jaraco](https://github.com/sponsors/jaraco) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Cope gracefully with a .pyc file with no matching .py file ([#2038](https://github.com/pytest-dev/pytest/issues/2038)). Thanks [\@nedbat](https://github.com/sponsors/nedbat).

## 3.0.4 (2016-11-09)[¶](#id880 "Link to this heading")

-   Import errors when collecting test modules now display the full traceback ([#1976](https://github.com/pytest-dev/pytest/issues/1976)). Thanks [\@cwitty](https://github.com/sponsors/cwitty) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix confusing command-line help message for custom options with two or more [`metavar`] properties ([#2004](https://github.com/pytest-dev/pytest/issues/2004)). Thanks [\@okulynyak](https://github.com/sponsors/okulynyak) and [\@davehunt](https://github.com/sponsors/davehunt) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   When loading plugins, import errors which contain non-ascii messages are now properly handled in Python 2 ([#1998](https://github.com/pytest-dev/pytest/issues/1998)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fixed cyclic reference when [`pytest.raises`] is used in context-manager form ([#1965](https://github.com/pytest-dev/pytest/issues/1965)). Also as a result of this fix, [`sys.exc_info()`] is left empty in both context-manager and function call usages. Previously, [`sys.exc_info`] would contain the exception caught by the context manager, even when the expected exception occurred. Thanks [\@MSeifert04](https://github.com/sponsors/MSeifert04) for the report and the PR.

-   Fixed false-positives warnings from assertion rewrite hook for modules that were rewritten but were later marked explicitly by [`pytest.register_assert_rewrite`] or implicitly as a plugin ([#2005](https://github.com/pytest-dev/pytest/issues/2005)). Thanks [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Report teardown output on test failure ([#442](https://github.com/pytest-dev/pytest/issues/442)). Thanks [\@matclab](https://github.com/sponsors/matclab) for the PR.

-   Fix teardown error message in generated xUnit XML. Thanks [\@gdyuldin](https://github.com/sponsors/gdyuldin) for the PR.

-   Properly handle exceptions in [`multiprocessing`] tasks ([#1984](https://github.com/pytest-dev/pytest/issues/1984)). Thanks [\@adborden](https://github.com/sponsors/adborden) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Clean up unittest TestCase objects after tests are complete ([#1649](https://github.com/pytest-dev/pytest/issues/1649)). Thanks [\@d-b-w](https://github.com/sponsors/d-b-w) for the report and PR.

## 3.0.3 (2016-09-28)[¶](#id881 "Link to this heading")

-   The [`ids`] argument to [`parametrize`] again accepts [`unicode`] strings in Python 2 ([#1905](https://github.com/pytest-dev/pytest/issues/1905)). Thanks [\@philpep](https://github.com/sponsors/philpep) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Assertions are now being rewritten for plugins in development mode ([`pip`]` `[`install`]` `[`-e`]) ([#1934](https://github.com/pytest-dev/pytest/issues/1934)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix pkg_resources import error in Jython projects ([#1853](https://github.com/pytest-dev/pytest/issues/1853)). Thanks [\@raquelalegre](https://github.com/sponsors/raquelalegre) for the PR.

-   Got rid of [`AttributeError:`]` `[`'Module'`]` `[`object`]` `[`has`]` `[`no`]` `[`attribute`]` `[`'_obj'`] exception in Python 3 ([#1944](https://github.com/pytest-dev/pytest/issues/1944)). Thanks [\@axil](https://github.com/sponsors/axil) for the PR.

-   Explain a bad scope value passed to [`@fixture`] declarations or a [`MetaFunc.parametrize()`] call.

-   This version includes [`pluggy-0.4.0`], which correctly handles [`VersionConflict`] errors in plugins ([#704](https://github.com/pytest-dev/pytest/issues/704)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

## 3.0.2 (2016-09-01)[¶](#id882 "Link to this heading")

-   Improve error message when passing non-string ids to [`pytest.mark.parametrize`] ([#1857](https://github.com/pytest-dev/pytest/issues/1857)). Thanks [\@okken](https://github.com/sponsors/okken) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Add [`buffer`] attribute to stdin stub class [`pytest.capture.DontReadFromInput`] Thanks [\@joguSD](https://github.com/sponsors/joguSD) for the PR.

-   Fix [`UnicodeEncodeError`] when string comparison with unicode has failed. ([#1864](https://github.com/pytest-dev/pytest/issues/1864)) Thanks [\@AiOO](https://github.com/sponsors/AiOO) for the PR.

-   [`pytest_plugins`] is now handled correctly if defined as a string (as opposed as a sequence of strings) when modules are considered for assertion rewriting. Due to this bug, much more modules were being rewritten than necessary if a test suite uses [`pytest_plugins`] to load internal plugins ([#1888](https://github.com/pytest-dev/pytest/issues/1888)). Thanks [\@jaraco](https://github.com/sponsors/jaraco) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR ([#1891](https://github.com/pytest-dev/pytest/pull/1891)).

-   Do not call tearDown and cleanups when running tests from [`unittest.TestCase`] subclasses with [`--pdb`] enabled. This allows proper post mortem debugging for all applications which have significant logic in their tearDown machinery ([#1890](https://github.com/pytest-dev/pytest/issues/1890)). Thanks [\@mbyt](https://github.com/sponsors/mbyt) for the PR.

-   Fix use of deprecated [`getfuncargvalue`] method in the internal doctest plugin. Thanks [\@ViviCoder](https://github.com/sponsors/ViviCoder) for the report ([#1898](https://github.com/pytest-dev/pytest/issues/1898)).

## 3.0.1 (2016-08-23)[¶](#id883 "Link to this heading")

-   Fix regression when [`importorskip`] is used at module level ([#1822](https://github.com/pytest-dev/pytest/issues/1822)). Thanks [\@jaraco](https://github.com/sponsors/jaraco) and [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix parametrization scope when session fixtures are used in conjunction with normal parameters in the same call ([#1832](https://github.com/pytest-dev/pytest/issues/1832)). Thanks [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the report, [\@Kingdread](https://github.com/sponsors/Kingdread) and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix internal error when parametrizing tests or fixtures using an empty [`ids`] argument ([#1849](https://github.com/pytest-dev/pytest/issues/1849)). Thanks [\@OPpuolitaival](https://github.com/sponsors/OPpuolitaival) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix loader error when running [`pytest`] embedded in a zipfile. Thanks [\@mbachry](https://github.com/sponsors/mbachry) for the PR.

[]

## 3.0.0 (2016-08-18)[¶](#release-3-0-0 "Link to this heading")

**Incompatible changes**

A number of incompatible changes were made in this release, with the intent of removing features deprecated for a long time or change existing behaviors in order to make them less surprising/more useful.

-   Reinterpretation mode has now been removed. Only plain and rewrite mode are available, consequently the [`--assert=reinterp`] option is no longer available. This also means files imported from plugins or [`conftest.py`] will not benefit from improved assertions by default, you should use [`pytest.register_assert_rewrite()`] to explicitly turn on assertion rewriting for those files. Thanks [\@flub](https://github.com/sponsors/flub) for the PR.

-   The following deprecated commandline options were removed:

    -   [`--genscript`]: no longer supported;

    -   [`--no-assert`]: use [`--assert=plain`] instead;

    -   [`--nomagic`]: use [`--assert=plain`] instead;

    -   [`--report`]: use [`-r`] instead;

    Thanks to [\@RedBeardCode](https://github.com/sponsors/RedBeardCode) for the PR ([#1664](https://github.com/pytest-dev/pytest/pull/1664)).

-   ImportErrors in plugins now are a fatal error instead of issuing a pytest warning ([#1479](https://github.com/pytest-dev/pytest/issues/1479)). Thanks to [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the PR.

-   Removed support code for Python 3 versions \< 3.3 ([#1627](https://github.com/pytest-dev/pytest/pull/1627)).

-   Removed all [`py.test-X*`] entry points. The versioned, suffixed entry points were never documented and a leftover from a pre-virtualenv era. These entry points also created broken entry points in wheels, so removing them also removes a source of confusion for users ([#1632](https://github.com/pytest-dev/pytest/issues/1632)). Thanks [\@obestwalter](https://github.com/sponsors/obestwalter) for the PR.

-   [`pytest.skip()`] now raises an error when used to decorate a test function, as opposed to its original intent (to imperatively skip a test inside a test function). Previously this usage would cause the entire module to be skipped ([#607](https://github.com/pytest-dev/pytest/issues/607)). Thanks [\@omarkohl](https://github.com/sponsors/omarkohl) for the complete PR ([#1519](https://github.com/pytest-dev/pytest/pull/1519)).

-   Exit tests if a collection error occurs. A poll indicated most users will hit CTRL-C anyway as soon as they see collection errors, so pytest might as well make that the default behavior ([#1421](https://github.com/pytest-dev/pytest/issues/1421)). A [`--continue-on-collection-errors`] option has been added to restore the previous behaviour. Thanks [\@olegpidsadnyi](https://github.com/sponsors/olegpidsadnyi) and [\@omarkohl](https://github.com/sponsors/omarkohl) for the complete PR ([#1628](https://github.com/pytest-dev/pytest/pull/1628)).

-   Renamed the pytest [`pdb`] module (plugin) into [`debugging`] to avoid clashes with the builtin [`pdb`] module.

-   Raise a helpful failure message when requesting a parametrized fixture at runtime, e.g. with [`request.getfixturevalue`]. Previously these parameters were simply never defined, so a fixture decorated like [`@pytest.fixture(params=[0,`]` `[`1,`]` `[`2])`] only ran once ([#460](https://github.com/pytest-dev/pytest/pull/460)). Thanks to [\@nikratio](https://github.com/sponsors/nikratio) for the bug report, [\@RedBeardCode](https://github.com/sponsors/RedBeardCode) and [\@tomviner](https://github.com/sponsors/tomviner) for the PR.

-   [`_pytest.monkeypatch.monkeypatch`] class has been renamed to [`_pytest.monkeypatch.MonkeyPatch`] so it doesn't conflict with the [`monkeypatch`] fixture.

-   [`--exitfirst`]` `[`/`]` `[`-x`] can now be overridden by a following [`--maxfail=N`] and is just a synonym for [`--maxfail=1`].

**New Features**

-   Support nose-style [`__test__`] attribute on methods of classes, including unittest-style Classes. If set to [`False`], the test will not be collected.

-   New [`doctest_namespace`] fixture for injecting names into the namespace in which doctests run. Thanks [\@milliams](https://github.com/sponsors/milliams) for the complete PR ([#1428](https://github.com/pytest-dev/pytest/pull/1428)).

-   New [`--doctest-report`] option available to change the output format of diffs when running (failing) doctests (implements [#1749](https://github.com/pytest-dev/pytest/issues/1749)). Thanks [\@hartym](https://github.com/sponsors/hartym) for the PR.

-   New [`name`] argument to [`pytest.fixture`] decorator which allows a custom name for a fixture (to solve the funcarg-shadowing-fixture problem). Thanks [\@novas0x2a](https://github.com/sponsors/novas0x2a) for the complete PR ([#1444](https://github.com/pytest-dev/pytest/pull/1444)).

-   New [`approx()`] function for easily comparing floating-point numbers in tests. Thanks [\@kalekundert](https://github.com/sponsors/kalekundert) for the complete PR ([#1441](https://github.com/pytest-dev/pytest/pull/1441)).

-   Ability to add global properties in the final xunit output file by accessing the internal [`junitxml`] plugin (experimental). Thanks [\@tareqalayan](https://github.com/sponsors/tareqalayan) for the complete PR [#1454](https://github.com/pytest-dev/pytest/pull/1454)).

-   New [`ExceptionInfo.match()`] method to match a regular expression on the string representation of an exception ([#372](https://github.com/pytest-dev/pytest/issues/372)). Thanks [\@omarkohl](https://github.com/sponsors/omarkohl) for the complete PR ([#1502](https://github.com/pytest-dev/pytest/pull/1502)).

-   [`__tracebackhide__`] can now also be set to a callable which then can decide whether to filter the traceback based on the [`ExceptionInfo`] object passed to it. Thanks [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the complete PR ([#1526](https://github.com/pytest-dev/pytest/pull/1526)).

-   New [`pytest_make_parametrize_id(config,`]` `[`val)`] hook which can be used by plugins to provide friendly strings for custom types. Thanks [\@palaviv](https://github.com/sponsors/palaviv) for the PR.

-   [`capsys`] and [`capfd`] now have a [`disabled()`] context-manager method, which can be used to temporarily disable capture within a test. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   New cli flag [`--fixtures-per-test`]: shows which fixtures are being used for each selected test item. Features doc strings of fixtures by default. Can also show where fixtures are defined if combined with [`-v`]. Thanks [\@hackebrot](https://github.com/sponsors/hackebrot) for the PR.

-   Introduce [`pytest`] command as recommended entry point. Note that [`py.test`] still works and is not scheduled for removal. Closes proposal [#1629](https://github.com/pytest-dev/pytest/issues/1629). Thanks [\@obestwalter](https://github.com/sponsors/obestwalter) and [\@davehunt](https://github.com/sponsors/davehunt) for the complete PR ([#1633](https://github.com/pytest-dev/pytest/pull/1633)).

-   New cli flags:

    -   [`--setup-plan`]: performs normal collection and reports the potential setup and teardown and does not execute any fixtures and tests;

    -   [`--setup-only`]: performs normal collection, executes setup and teardown of fixtures and reports them;

    -   [`--setup-show`]: performs normal test execution and additionally shows setup and teardown of fixtures;

    -   [`--keep-duplicates`]: py.test now ignores duplicated paths given in the command line. To retain the previous behavior where the same test could be run multiple times by specifying it in the command-line multiple times, pass the [`--keep-duplicates`] argument ([#1609](https://github.com/pytest-dev/pytest/issues/1609));

    Thanks [\@d6e](https://github.com/sponsors/d6e), [\@kvas-it](https://github.com/sponsors/kvas-it), [\@sallner](https://github.com/sponsors/sallner), [\@ioggstream](https://github.com/sponsors/ioggstream) and [\@omarkohl](https://github.com/sponsors/omarkohl) for the PRs.

-   New CLI flag [`--override-ini`]/[`-o`]: overrides values from the ini file. For example: [`"-o`]` `[`xfail_strict=True"`]'. Thanks [\@blueyed](https://github.com/sponsors/blueyed) and [\@fengxx](https://github.com/sponsors/fengxx) for the PR.

-   New hooks:

    -   [`pytest_fixture_setup(fixturedef,`]` `[`request)`]: executes fixture setup;

    -   [`pytest_fixture_post_finalizer(fixturedef)`]: called after the fixture's finalizer and has access to the fixture's result cache.

    Thanks [\@d6e](https://github.com/sponsors/d6e), [\@sallner](https://github.com/sponsors/sallner).

-   Issue warnings for asserts whose test is a tuple literal. Such asserts will never fail because tuples are always truthy and are usually a mistake (see [#1562](https://github.com/pytest-dev/pytest/issues/1562)). Thanks [\@kvas-it](https://github.com/sponsors/kvas-it), for the PR.

-   Allow passing a custom debugger class (e.g. [`--pdbcls=IPython.core.debugger:Pdb`]). Thanks to [\@anntzer](https://github.com/sponsors/anntzer) for the PR.

**Changes**

-   Plugins now benefit from assertion rewriting. Thanks [\@sober7](https://github.com/sponsors/sober7), [\@nicoddemus](https://github.com/sponsors/nicoddemus) and [\@flub](https://github.com/sponsors/flub) for the PR.

-   Change [`report.outcome`] for [`xpassed`] tests to [`"passed"`] in non-strict mode and [`"failed"`] in strict mode. Thanks to [\@hackebrot](https://github.com/sponsors/hackebrot) for the PR ([#1795](https://github.com/pytest-dev/pytest/pull/1795)) and [\@gprasad84](https://github.com/sponsors/gprasad84) for report ([#1546](https://github.com/pytest-dev/pytest/issues/1546)).

-   Tests marked with [`xfail(strict=False)`] (the default) now appear in JUnitXML reports as passing tests instead of skipped. Thanks to [\@hackebrot](https://github.com/sponsors/hackebrot) for the PR ([#1795](https://github.com/pytest-dev/pytest/pull/1795)).

-   Highlight path of the file location in the error report to make it easier to copy/paste. Thanks [\@suzaku](https://github.com/sponsors/suzaku) for the PR ([#1778](https://github.com/pytest-dev/pytest/pull/1778)).

-   Fixtures marked with [`@pytest.fixture`] can now use [`yield`] statements exactly like those marked with the [`@pytest.yield_fixture`] decorator. This change renders [`@pytest.yield_fixture`] deprecated and makes [`@pytest.fixture`] with [`yield`] statements the preferred way to write teardown code ([#1461](https://github.com/pytest-dev/pytest/pull/1461)). Thanks [\@csaftoiu](https://github.com/sponsors/csaftoiu) for bringing this to attention and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Explicitly passed parametrize ids do not get escaped to ascii ([#1351](https://github.com/pytest-dev/pytest/issues/1351)). Thanks [\@ceridwen](https://github.com/sponsors/ceridwen) for the PR.

-   Fixtures are now sorted in the error message displayed when an unknown fixture is declared in a test function. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   [`pytest_terminal_summary`] hook now receives the [`exitstatus`] of the test session as argument. Thanks [\@blueyed](https://github.com/sponsors/blueyed) for the PR ([#1809](https://github.com/pytest-dev/pytest/pull/1809)).

-   Parametrize ids can accept [`None`] as specific test id, in which case the automatically generated id for that argument will be used. Thanks [\@palaviv](https://github.com/sponsors/palaviv) for the complete PR ([#1468](https://github.com/pytest-dev/pytest/pull/1468)).

-   The parameter to xunit-style setup/teardown methods ([`setup_method`], [`setup_module`], etc.) is now optional and may be omitted. Thanks [\@okken](https://github.com/sponsors/okken) for bringing this to attention and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Improved automatic id generation selection in case of duplicate ids in parametrize. Thanks [\@palaviv](https://github.com/sponsors/palaviv) for the complete PR ([#1474](https://github.com/pytest-dev/pytest/pull/1474)).

-   Now pytest warnings summary is shown up by default. Added a new flag [`--disable-pytest-warnings`] to explicitly disable the warnings summary ([#1668](https://github.com/pytest-dev/pytest/issues/1668)).

-   Make ImportError during collection more explicit by reminding the user to check the name of the test module/package(s) ([#1426](https://github.com/pytest-dev/pytest/issues/1426)). Thanks [\@omarkohl](https://github.com/sponsors/omarkohl) for the complete PR ([#1520](https://github.com/pytest-dev/pytest/pull/1520)).

-   Add [`build/`] and [`dist/`] to the default [`--norecursedirs`] list. Thanks [\@mikofski](https://github.com/sponsors/mikofski) for the report and [\@tomviner](https://github.com/sponsors/tomviner) for the PR ([#1544](https://github.com/pytest-dev/pytest/issues/1544)).

-   [`pytest.raises`] in the context manager form accepts a custom [`message`] to raise when no exception occurred. Thanks [\@palaviv](https://github.com/sponsors/palaviv) for the complete PR ([#1616](https://github.com/pytest-dev/pytest/pull/1616)).

-   [`conftest.py`] files now benefit from assertion rewriting; previously it was only available for test modules. Thanks [\@flub](https://github.com/sponsors/flub), [\@sober7](https://github.com/sponsors/sober7) and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR ([#1619](https://github.com/pytest-dev/pytest/issues/1619)).

-   Text documents without any doctests no longer appear as "skipped". Thanks [\@graingert](https://github.com/sponsors/graingert) for reporting and providing a full PR ([#1580](https://github.com/pytest-dev/pytest/pull/1580)).

-   Ensure that a module within a namespace package can be found when it is specified on the command line together with the [`--pyargs`] option. Thanks to [\@taschini](https://github.com/sponsors/taschini) for the PR ([#1597](https://github.com/pytest-dev/pytest/pull/1597)).

-   Always include full assertion explanation during assertion rewriting. The previous behaviour was hiding sub-expressions that happened to be [`False`], assuming this was redundant information. Thanks [\@bagerard](https://github.com/sponsors/bagerard) for reporting ([#1503](https://github.com/pytest-dev/pytest/issues/1503)). Thanks to [\@davehunt](https://github.com/sponsors/davehunt) and [\@tomviner](https://github.com/sponsors/tomviner) for the PR.

-   [`OptionGroup.addoption()`] now checks if option names were already added before, to make it easier to track down issues like [#1618](https://github.com/pytest-dev/pytest/issues/1618). Before, you only got exceptions later from [`argparse`] library, giving no clue about the actual reason for double-added options.

-   [`yield`]-based tests are considered deprecated and will be removed in pytest-4.0. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   [`[pytest]`] sections in [`setup.cfg`] files should now be named [`[tool:pytest]`] to avoid conflicts with other distutils commands (see [#567](https://github.com/pytest-dev/pytest/pull/567)). [`[pytest]`] sections in [`pytest.ini`] or [`tox.ini`] files are supported and unchanged. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Using [`pytest_funcarg__`] prefix to declare fixtures is considered deprecated and will be removed in pytest-4.0 ([#1684](https://github.com/pytest-dev/pytest/pull/1684)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Passing a command-line string to [`pytest.main()`] is considered deprecated and scheduled for removal in pytest-4.0. It is recommended to pass a list of arguments instead ([#1723](https://github.com/pytest-dev/pytest/pull/1723)).

-   Rename [`getfuncargvalue`] to [`getfixturevalue`]. [`getfuncargvalue`] is still present but is now considered deprecated. Thanks to [\@RedBeardCode](https://github.com/sponsors/RedBeardCode) and [\@tomviner](https://github.com/sponsors/tomviner) for the PR ([#1626](https://github.com/pytest-dev/pytest/pull/1626)).

-   [`optparse`] type usage now triggers DeprecationWarnings ([#1740](https://github.com/pytest-dev/pytest/issues/1740)).

-   [`optparse`] backward compatibility supports float/complex types ([#457](https://github.com/pytest-dev/pytest/issues/457)).

-   Refined logic for determining the [`rootdir`], considering only valid paths which fixes a number of issues: [#1594](https://github.com/pytest-dev/pytest/issues/1594), [#1435](https://github.com/pytest-dev/pytest/issues/1435) and [#1471](https://github.com/pytest-dev/pytest/issues/1471). Updated the documentation according to current behavior. Thanks to [\@blueyed](https://github.com/sponsors/blueyed), [\@davehunt](https://github.com/sponsors/davehunt) and [\@matthiasha](https://github.com/sponsors/matthiasha) for the PR.

-   Always include full assertion explanation. The previous behaviour was hiding sub-expressions that happened to be False, assuming this was redundant information. Thanks [\@bagerard](https://github.com/sponsors/bagerard) for reporting ([#1503](https://github.com/pytest-dev/pytest/issues/1503)). Thanks to [\@davehunt](https://github.com/sponsors/davehunt) and [\@tomviner](https://github.com/sponsors/tomviner) for PR.

-   Better message in case of not using parametrized variable (see [#1539](https://github.com/pytest-dev/pytest/issues/1539)). Thanks to [\@tramwaj29](https://github.com/sponsors/tramwaj29) for the PR.

-   Updated docstrings with a more uniform style.

-   Add stderr write for [`pytest.exit(msg)`] during startup. Previously the message was never shown. Thanks [\@BeyondEvil](https://github.com/sponsors/BeyondEvil) for reporting [#1210](https://github.com/pytest-dev/pytest/issues/1210). Thanks to \@jgsonesen and [\@tomviner](https://github.com/sponsors/tomviner) for the PR.

-   No longer display the incorrect test deselection reason ([#1372](https://github.com/pytest-dev/pytest/issues/1372)). Thanks [\@ronnypfannschmidt](https://github.com/sponsors/ronnypfannschmidt) for the PR.

-   The [`--resultlog`] command line option has been deprecated: it is little used and there are more modern and better alternatives (see [#830](https://github.com/pytest-dev/pytest/issues/830)). Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Improve error message with fixture lookup errors: add an 'E' to the first line and '\>' to the rest. Fixes [#717](https://github.com/pytest-dev/pytest/issues/717). Thanks [\@blueyed](https://github.com/sponsors/blueyed) for reporting and a PR, [\@eolo999](https://github.com/sponsors/eolo999) for the initial PR and [\@tomviner](https://github.com/sponsors/tomviner) for his guidance during EuroPython2016 sprint.

**Bug Fixes**

-   Parametrize now correctly handles duplicated test ids.

-   Fix internal error issue when the [`method`] argument is missing for [`teardown_method()`] ([#1605](https://github.com/pytest-dev/pytest/issues/1605)).

-   Fix exception visualization in case the current working directory (CWD) gets deleted during testing ([#1235](https://github.com/pytest-dev/pytest/issues/1235)). Thanks [\@bukzor](https://github.com/sponsors/bukzor) for reporting. PR by [\@marscher](https://github.com/sponsors/marscher).

-   Improve test output for logical expression with brackets ([#925](https://github.com/pytest-dev/pytest/issues/925)). Thanks [\@DRMacIver](https://github.com/sponsors/DRMacIver) for reporting and [\@RedBeardCode](https://github.com/sponsors/RedBeardCode) for the PR.

-   Create correct diff for strings ending with newlines ([#1553](https://github.com/pytest-dev/pytest/issues/1553)). Thanks [\@Vogtinator](https://github.com/sponsors/Vogtinator) for reporting and [\@RedBeardCode](https://github.com/sponsors/RedBeardCode) and [\@tomviner](https://github.com/sponsors/tomviner) for the PR.

-   [`ConftestImportFailure`] now shows the traceback making it easier to identify bugs in [`conftest.py`] files ([#1516](https://github.com/pytest-dev/pytest/pull/1516)). Thanks [\@txomon](https://github.com/sponsors/txomon) for the PR.

-   Text documents without any doctests no longer appear as "skipped". Thanks [\@graingert](https://github.com/sponsors/graingert) for reporting and providing a full PR ([#1580](https://github.com/pytest-dev/pytest/pull/1580)).

-   Fixed collection of classes with custom [`__new__`] method. Fixes [#1579](https://github.com/pytest-dev/pytest/issues/1579). Thanks to [\@Stranger6667](https://github.com/sponsors/Stranger6667) for the PR.

-   Fixed scope overriding inside metafunc.parametrize ([#634](https://github.com/pytest-dev/pytest/issues/634)). Thanks to [\@Stranger6667](https://github.com/sponsors/Stranger6667) for the PR.

-   Fixed the total tests tally in junit xml output ([#1798](https://github.com/pytest-dev/pytest/pull/1798)). Thanks to [\@cboelsen](https://github.com/sponsors/cboelsen) for the PR.

-   Fixed off-by-one error with lines from [`request.node.warn`]. Thanks to [\@blueyed](https://github.com/sponsors/blueyed) for the PR.

## 2.9.2 (2016-05-31)[¶](#id885 "Link to this heading")

**Bug Fixes**

-   fix [#510](https://github.com/pytest-dev/pytest/issues/510): skip tests where one parameterize dimension was empty thanks Alex Stapleton for the Report and [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR

-   Fix Xfail does not work with condition keyword argument. Thanks [\@astraw38](https://github.com/sponsors/astraw38) for reporting the issue ([#1496](https://github.com/pytest-dev/pytest/issues/1496)) and [\@tomviner](https://github.com/sponsors/tomviner) for PR the ([#1524](https://github.com/pytest-dev/pytest/pull/1524)).

-   Fix win32 path issue when putting custom config file with absolute path in [`pytest.main("-c`]` `[`your_absolute_path")`].

-   Fix maximum recursion depth detection when raised error class is not aware of unicode/encoded bytes. Thanks [\@prusse-martin](https://github.com/sponsors/prusse-martin) for the PR ([#1506](https://github.com/pytest-dev/pytest/pull/1506)).

-   Fix [`pytest.mark.skip`] mark when used in strict mode. Thanks [\@pquentin](https://github.com/sponsors/pquentin) for the PR and [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for showing how to fix the bug.

-   Minor improvements and fixes to the documentation. Thanks [\@omarkohl](https://github.com/sponsors/omarkohl) for the PR.

-   Fix [`--fixtures`] to show all fixture definitions as opposed to just one per fixture name. Thanks to [\@hackebrot](https://github.com/sponsors/hackebrot) for the PR.

## 2.9.1 (2016-03-17)[¶](#id886 "Link to this heading")

**Bug Fixes**

-   Improve error message when a plugin fails to load. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix ([#1178](https://github.com/pytest-dev/pytest/issues/1178)): [`pytest.fail`] with non-ascii characters raises an internal pytest error. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix ([#469](https://github.com/pytest-dev/pytest/issues/469)): junit parses report.nodeid incorrectly, when params IDs contain [`::`]. Thanks [\@tomviner](https://github.com/sponsors/tomviner) for the PR ([#1431](https://github.com/pytest-dev/pytest/pull/1431)).

-   Fix ([#578](https://github.com/pytest-dev/pytest/issues/578)): SyntaxErrors containing non-ascii lines at the point of failure generated an internal py.test error. Thanks [\@asottile](https://github.com/sponsors/asottile) for the report and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Fix ([#1437](https://github.com/pytest-dev/pytest/issues/1437)): When passing in a bytestring regex pattern to parameterize attempt to decode it as utf-8 ignoring errors.

-   Fix ([#649](https://github.com/pytest-dev/pytest/issues/649)): parametrized test nodes cannot be specified to run on the command line.

-   Fix ([#138](https://github.com/pytest-dev/pytest/issues/138)): better reporting for python 3.3+ chained exceptions

## 2.9.0 (2016-02-29)[¶](#id887 "Link to this heading")

**New Features**

-   New [`pytest.mark.skip`] mark, which unconditionally skips marked tests. Thanks [\@MichaelAquilina](https://github.com/sponsors/MichaelAquilina) for the complete PR ([#1040](https://github.com/pytest-dev/pytest/pull/1040)).

-   [`--doctest-glob`] may now be passed multiple times in the command-line. Thanks [\@jab](https://github.com/sponsors/jab) and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   New [`-rp`] and [`-rP`] reporting options give the summary and full output of passing tests, respectively. Thanks to [\@codewarrior0](https://github.com/sponsors/codewarrior0) for the PR.

-   [`pytest.mark.xfail`] now has a [`strict`] option, which makes [`XPASS`] tests to fail the test suite (defaulting to [`False`]). There's also a [`xfail_strict`] ini option that can be used to configure it project-wise. Thanks [\@rabbbit](https://github.com/sponsors/rabbbit) for the request and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR ([#1355](https://github.com/pytest-dev/pytest/pull/1355)).

-   [`Parser.addini`] now supports options of type [`bool`]. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   New [`ALLOW_BYTES`] doctest option. This strips [`b`] prefixes from byte strings in doctest output (similar to [`ALLOW_UNICODE`]). Thanks [\@jaraco](https://github.com/sponsors/jaraco) for the request and [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR ([#1287](https://github.com/pytest-dev/pytest/pull/1287)).

-   Give a hint on [`KeyboardInterrupt`] to use the [`--fulltrace`] option to show the errors. Fixes [#1366](https://github.com/pytest-dev/pytest/issues/1366). Thanks to [\@hpk42](https://github.com/sponsors/hpk42) for the report and [\@RonnyPfannschmidt](https://github.com/sponsors/RonnyPfannschmidt) for the PR.

-   Catch [`IndexError`] exceptions when getting exception source location. Fixes a pytest internal error for dynamically generated code (fixtures and tests) where source lines are fake by intention.

**Changes**

-   **Important**: [py.code](https://pylib.readthedocs.io/en/stable/code.html) has been merged into the [`pytest`] repository as [`pytest._code`]. This decision was made because [`py.code`] had very few uses outside [`pytest`] and the fact that it was in a different repository made it difficult to fix bugs on its code in a timely manner. The team hopes with this to be able to better refactor out and improve that code. This change shouldn't affect users, but it is useful to let users aware if they encounter any strange behavior.

    Keep in mind that the code for [`pytest._code`] is **private** and **experimental**, so you definitely should not import it explicitly!

    Please note that the original [`py.code`] is still available in [pylib](https://pylib.readthedocs.io).

-   [`pytest_enter_pdb`] now optionally receives the pytest config object. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR.

-   Removed code and documentation for Python 2.5 or lower versions, including removal of the obsolete [`_pytest.assertion.oldinterpret`] module. Thanks [\@nicoddemus](https://github.com/sponsors/nicoddemus) for the PR ([#1226](https://github.com/pytest-dev/pytest/pull/1226)).

-   Comparisons now always show up in full when [`CI`] or [`BUILD_NUMBER`] is found in the environment, even when [`-vv`] isn't used. Thanks [\@The-Compiler](https://github.com/sponsors/The-Compiler) for the PR.

-   [`--lf`] and [`--ff`] now support long names: [`--last-failed`] and [`--failed-first`] respectively. Thanks [\@MichaelAquilina](https://github.com/sponsors/MichaelAquilina) for the PR.

-   Added expected exceptions to [`pytest.raises`] fail message.

-   Collection only displays progress ("collecting X items") when in a terminal. This avoids cluttering the output when using [`--color=yes`] to obtain colors in CI integrations systems ([#1397](https://github.com/pytest-dev/pytest/issues/1397)).

**Bug Fixes**

-   The [`-s`] and [`-c`] options should now work under [`xdist`]; [`Config.fromdictargs`] now represents its input much more faithfully. Thanks to [\@bukzor](https://github.com/sponsors/bukzor) for the complete PR ([#680](https://github.com/pytest-dev/pytest/issues/680)).

-   Fix ([#1290](https://github.com/pytest-dev/pytest/issues/1290)): support Python 3.5's [`@`] operator in assertion rewriting. Thanks [\@Shinkenjoe](https://github.com/sponsors/Shinkenjoe) for report with test case and [\@tomviner](https://github.com/sponsors/tomviner) for the PR.

-   Fix formatting utf-8 explanation messages ([#1379](https://github.com/pytest-dev/pytest/issues/1379)). Thanks [\@biern](https://github.com/sponsors/biern) for the PR.

-   Fix [[traceback style docs]](how-to/output.html#how-to-modifying-python-tb-printing) to describe all of the available options (auto/long/short/line/native/no), with [`auto`] being the default since v2.6. Thanks [\@hackebrot](https://github.com/sponsors/hackebrot) for the PR.

-   Fix ([#1422](https://github.com/pytest-dev/pytest/issues/1422)): junit record_xml_property doesn't allow multiple records with same name.

## 2.8.7 (2016-01-24)[¶](#id888 "Link to this heading")

-   fix #1338: use predictable object resolution for monkeypatch

## 2.8.6 (2016-01-21)[¶](#id889 "Link to this heading")

-   fix #1259: allow for double nodeids in junitxml, this was a regression failing plugins combinations like pytest-pep8 + pytest-flakes

-   Workaround for exception that occurs in pyreadline when using [`--pdb`] with standard I/O capture enabled. Thanks Erik M. Bray for the PR.

-   fix #900: Better error message in case the target of a [`monkeypatch`] call raises an [`ImportError`].

-   fix #1292: monkeypatch calls (setattr, setenv, etc.) are now O(1). Thanks David R. MacIver for the report and Bruno Oliveira for the PR.

-   fix #1223: captured stdout and stderr are now properly displayed before entering pdb when [`--pdb`] is used instead of being thrown away. Thanks Cal Leeming for the PR.

-   fix #1305: pytest warnings emitted during [`pytest_terminal_summary`] are now properly displayed. Thanks Ionel Maries Cristian for the report and Bruno Oliveira for the PR.

-   fix #628: fixed internal UnicodeDecodeError when doctests contain unicode. Thanks Jason R. Coombs for the report and Bruno Oliveira for the PR.

-   fix #1334: Add captured stdout to jUnit XML report on setup error. Thanks Georgy Dyuldin for the PR.

## 2.8.5 (2015-12-11)[¶](#id890 "Link to this heading")

-   fix #1243: fixed issue where class attributes injected during collection could break pytest. PR by Alexei Kozlenok, thanks Ronny Pfannschmidt and Bruno Oliveira for the review and help.

-   fix #1074: precompute junitxml chunks instead of storing the whole tree in objects Thanks Bruno Oliveira for the report and Ronny Pfannschmidt for the PR

-   fix #1238: fix [`pytest.deprecated_call()`] receiving multiple arguments (Regression introduced in 2.8.4). Thanks Alex Gaynor for the report and Bruno Oliveira for the PR.

## 2.8.4 (2015-12-06)[¶](#id891 "Link to this heading")

-   fix #1190: [`deprecated_call()`] now works when the deprecated function has been already called by another test in the same module. Thanks Mikhail Chernykh for the report and Bruno Oliveira for the PR.

-   fix #1198: [`--pastebin`] option now works on Python 3. Thanks Mehdy Khoshnoody for the PR.

-   fix #1219: [`--pastebin`] now works correctly when captured output contains non-ascii characters. Thanks Bruno Oliveira for the PR.

-   fix #1204: another error when collecting with a nasty \_\_getattr\_\_(). Thanks Florian Bruhin for the PR.

-   fix the summary printed when no tests did run. Thanks Florian Bruhin for the PR.

-   fix #1185 - ensure MANIFEST.in exactly matches what should go to a sdist

-   a number of documentation modernizations wrt good practices. Thanks Bruno Oliveira for the PR.

## 2.8.3 (2015-11-18)[¶](#id892 "Link to this heading")

-   fix #1169: add \_\_name\_\_ attribute to testcases in TestCaseFunction to support the \@unittest.skip decorator on functions and methods. Thanks Lee Kamentsky for the PR.

-   fix #1035: collecting tests if test module level obj has \_\_getattr\_\_(). Thanks Suor for the report and Bruno Oliveira / Tom Viner for the PR.

-   fix #331: don't collect tests if their failure cannot be reported correctly e.g. they are a callable instance of a class.

-   fix #1133: fixed internal error when filtering tracebacks where one entry belongs to a file which is no longer available. Thanks Bruno Oliveira for the PR.

-   enhancement made to highlight in red the name of the failing tests so they stand out in the output. Thanks Gabriel Reis for the PR.

-   add more talks to the documentation

-   extend documentation on the --ignore cli option

-   use pytest-runner for setuptools integration

-   minor fixes for interaction with OS X El Capitan system integrity protection (thanks Florian)

## 2.8.2 (2015-10-07)[¶](#id893 "Link to this heading")

-   fix #1085: proper handling of encoding errors when passing encoded byte strings to pytest.parametrize in Python 2. Thanks Themanwithoutaplan for the report and Bruno Oliveira for the PR.

-   fix #1087: handling SystemError when passing empty byte strings to pytest.parametrize in Python 3. Thanks Paul Kehrer for the report and Bruno Oliveira for the PR.

-   fix #995: fixed internal error when filtering tracebacks where one entry was generated by an exec() statement. Thanks Daniel Hahler, Ashley C Straw, Philippe Gauthier and Pavel Savchenko for contributing and Bruno Oliveira for the PR.

-   fix #1100 and #1057: errors when using autouse fixtures and doctest modules. Thanks Sergey B Kirpichev and Vital Kudzelka for contributing and Bruno Oliveira for the PR.

## 2.8.1 (2015-09-29)[¶](#id894 "Link to this heading")

-   fix #1034: Add missing nodeid on pytest_logwarning call in addhook. Thanks Simon Gomizelj for the PR.

-   'deprecated_call' is now only satisfied with a DeprecationWarning or PendingDeprecationWarning. Before 2.8.0, it accepted any warning, and 2.8.0 made it accept only DeprecationWarning (but not PendingDeprecationWarning). Thanks Alex Gaynor for the issue and Eric Hunsberger for the PR.

-   fix issue #1073: avoid calling \_\_getattr\_\_ on potential plugin objects. This fixes an incompatibility with pytest-django. Thanks Andreas Pelme, Bruno Oliveira and Ronny Pfannschmidt for contributing and Holger Krekel for the fix.

-   Fix issue #704: handle versionconflict during plugin loading more gracefully. Thanks Bruno Oliveira for the PR.

-   Fix issue #1064: ""--junitxml" regression when used with the "pytest-xdist" plugin, with test reports being assigned to the wrong tests. Thanks Daniel Grunwald for the report and Bruno Oliveira for the PR.

-   (experimental) adapt more SEMVER style versioning and change meaning of master branch in git repo: "master" branch now keeps the bug fixes, changes aimed for micro releases. "features" branch will only be released with minor or major pytest releases.

-   Fix issue #766 by removing documentation references to distutils. Thanks Russel Winder.

-   Fix issue #1030: now byte-strings are escaped to produce item node ids to make them always serializable. Thanks Andy Freeland for the report and Bruno Oliveira for the PR.

-   Python 2: if unicode parametrized values are convertible to ascii, their ascii representation is used for the node id.

-   Fix issue #411: Add \_\_eq\_\_ method to assertion comparison example. Thanks Ben Webb.

-   Fix issue #653: deprecated_call can be used as context manager.

-   fix issue 877: properly handle assertion explanations with non-ascii repr Thanks Mathieu Agopian for the report and Ronny Pfannschmidt for the PR.

-   fix issue 1029: transform errors when writing cache values into pytest-warnings

## 2.8.0 (2015-09-18)[¶](#id895 "Link to this heading")

-   new [`--lf`] and [`-ff`] options to run only the last failing tests or "failing tests first" from the last run. This functionality is provided through porting the formerly external pytest-cache plugin into pytest core. BACKWARD INCOMPAT: if you used pytest-cache's functionality to persist data between test runs be aware that we don't serialize sets anymore. Thanks Ronny Pfannschmidt for most of the merging work.

-   "-r" option now accepts "a" to include all possible reports, similar to passing "fEsxXw" explicitly (issue960). Thanks Abhijeet Kasurde for the PR.

-   avoid python3.5 deprecation warnings by introducing version specific inspection helpers, thanks Michael Droettboom.

-   fix issue562: \@nose.tools.istest now fully respected.

-   fix issue934: when string comparison fails and a diff is too large to display without passing -vv, still show a few lines of the diff. Thanks Florian Bruhin for the report and Bruno Oliveira for the PR.

-   fix issue736: Fix a bug where fixture params would be discarded when combined with parametrization markers. Thanks to Markus Unterwaditzer for the PR.

-   fix issue710: introduce ALLOW_UNICODE doctest option: when enabled, the [`u`] prefix is stripped from unicode strings in expected doctest output. This allows doctests which use unicode to run in Python 2 and 3 unchanged. Thanks Jason R. Coombs for the report and Bruno Oliveira for the PR.

-   parametrize now also generates meaningful test IDs for enum, regex and class objects (as opposed to class instances). Thanks to Florian Bruhin for the PR.

-   Add 'warns' to assert that warnings are thrown (like 'raises'). Thanks to Eric Hunsberger for the PR.

-   Fix issue683: Do not apply an already applied mark. Thanks ojake for the PR.

-   Deal with capturing failures better so fewer exceptions get lost to /dev/null. Thanks David Szotten for the PR.

-   fix issue730: deprecate and warn about the --genscript option. Thanks Ronny Pfannschmidt for the report and Christian Pommranz for the PR.

-   fix issue751: multiple parametrize with ids bug if it parametrizes class with two or more test methods. Thanks Sergey Chipiga for reporting and Jan Bednarik for PR.

-   fix issue82: avoid loading conftest files from setup.cfg/pytest.ini/tox.ini files and upwards by default (--confcutdir can still be set to override this). Thanks Bruno Oliveira for the PR.

-   fix issue768: docstrings found in python modules were not setting up session fixtures. Thanks Jason R. Coombs for reporting and Bruno Oliveira for the PR.

-   added [`tmpdir_factory`], a session-scoped fixture that can be used to create directories under the base temporary directory. Previously this object was installed as a [`_tmpdirhandler`] attribute of the [`config`] object, but now it is part of the official API and using [`config._tmpdirhandler`] is deprecated. Thanks Bruno Oliveira for the PR.

-   fix issue808: pytest's internal assertion rewrite hook now implements the optional [][**PEP 302**](https://peps.python.org/pep-0302/) get_data API so tests can access data files next to them. Thanks xmo-odoo for request and example and Bruno Oliveira for the PR.

-   rootdir and inifile are now displayed during usage errors to help users diagnose problems such as unexpected ini files which add unknown options being picked up by pytest. Thanks to Pavel Savchenko for bringing the problem to attention in #821 and Bruno Oliveira for the PR.

-   Summary bar now is colored yellow for warning situations such as: all tests either were skipped or xpass/xfailed, or no tests were run at all (this is a partial fix for issue500).

-   fix issue812: pytest now exits with status code 5 in situations where no tests were run at all, such as the directory given in the command line does not contain any tests or as result of a command line option filters all out all tests (-k for example). Thanks Eric Siegerman (issue812) and Bruno Oliveira for the PR.

-   Summary bar now is colored yellow for warning situations such as: all tests either were skipped or xpass/xfailed, or no tests were run at all (related to issue500). Thanks Eric Siegerman.

-   New [`testpaths`] ini option: list of directories to search for tests when executing pytest from the root directory. This can be used to speed up test collection when a project has well specified directories for tests, being usually more practical than configuring norecursedirs for all directories that do not contain tests. Thanks to Adrian for idea (#694) and Bruno Oliveira for the PR.

-   fix issue713: JUnit XML reports for doctest failures. Thanks Punyashloka Biswal.

-   fix issue970: internal pytest warnings now appear as "pytest-warnings" in the terminal instead of "warnings", so it is clear for users that those warnings are from pytest and not from the builtin "warnings" module. Thanks Bruno Oliveira.

-   Include setup and teardown in junitxml test durations. Thanks Janne Vanhala.

-   fix issue735: assertion failures on debug versions of Python 3.4+

-   new option [`--import-mode`] to allow to change test module importing behaviour to append to sys.path instead of prepending. This better allows to run test modules against installed versions of a package even if the package under test has the same import root. In this example:

    ::: 
    ::: highlight
        testing/__init__.py
        testing/test_pkg_under_test.py
        pkg_under_test/
    :::
    :::

    the tests will run against the installed version of pkg_under_test when [`--import-mode=append`] is used whereas by default they would always pick up the local version. Thanks Holger Krekel.

-   pytester: add method [`TmpTestdir.delete_loaded_modules()`], and call it from [`inline_run()`] to allow temporary modules to be reloaded. Thanks Eduardo Schettino.

-   internally refactor pluginmanager API and code so that there is a clear distinction between a pytest-agnostic rather simple pluginmanager and the PytestPluginManager which adds a lot of behaviour, among it handling of the local conftest files. In terms of documented methods this is a backward compatible change but it might still break 3rd party plugins which relied on details like especially the pluginmanager.add_shutdown() API. Thanks Holger Krekel.

-   pluginmanagement: introduce [`pytest.hookimpl`] and [`pytest.hookspec`] decorators for setting impl/spec specific parameters. This substitutes the previous now deprecated use of [`pytest.mark`] which is meant to contain markers for test functions only.

-   write/refine docs for "writing plugins" which now have their own page and are separate from the "using/installing plugins\`\` page.

-   fix issue732: properly unregister plugins from any hook calling sites allowing to have temporary plugins during test execution.

-   deprecate and warn about [`__multicall__`] argument in hook implementations. Use the [`hookwrapper`] mechanism instead already introduced with pytest-2.7.

-   speed up pytest's own test suite considerably by using inprocess tests by default (testrun can be modified with --runpytest=subprocess to create subprocesses in many places instead). The main APIs to run pytest in a test is "runpytest()" or "runpytest_subprocess" and "runpytest_inprocess" if you need a particular way of running the test. In all cases you get back a RunResult but the inprocess one will also have a "reprec" attribute with the recorded events/reports.

-   fix monkeypatch.setattr("x.y", raising=False) to actually not raise if "y" is not a preexisting attribute. Thanks Florian Bruhin.

-   fix issue741: make running output from testdir.run copy/pasteable Thanks Bruno Oliveira.

-   add a new [`--noconftest`] argument which ignores all [`conftest.py`] files.

-   add [`file`] and [`line`] attributes to JUnit-XML output.

-   fix issue890: changed extension of all documentation files from [`txt`] to [`rst`]. Thanks to Abhijeet for the PR.

-   fix issue714: add ability to apply indirect=True parameter on particular argnames. Thanks Elizaveta239.

-   fix issue890: changed extension of all documentation files from [`txt`] to [`rst`]. Thanks to Abhijeet for the PR.

-   fix issue957: "# doctest: SKIP" option will now register doctests as SKIPPED rather than PASSED. Thanks Thomas Grainger for the report and Bruno Oliveira for the PR.

-   issue951: add new record_xml_property fixture, that supports logging additional information on xml output. Thanks David Diaz for the PR.

-   issue949: paths after normal options (for example [`-s`], [`-v`], etc) are now properly used to discover [`rootdir`] and [`ini`] files. Thanks Peter Lauri for the report and Bruno Oliveira for the PR.

## 2.7.3 (2015-09-15)[¶](#id896 "Link to this heading")

-   Allow 'dev', 'rc', or other non-integer version strings in [`importorskip`]. Thanks to Eric Hunsberger for the PR.

-   fix issue856: consider --color parameter in all outputs (for example --fixtures). Thanks Barney Gale for the report and Bruno Oliveira for the PR.

-   fix issue855: passing str objects as [`plugins`] argument to pytest.main is now interpreted as a module name to be imported and registered as a plugin, instead of silently having no effect. Thanks xmo-odoo for the report and Bruno Oliveira for the PR.

-   fix issue744: fix for ast.Call changes in Python 3.5+. Thanks Guido van Rossum, Matthias Bussonnier, Stefan Zimmermann and Thomas Kluyver.

-   fix issue842: applying markers in classes no longer propagate this markers to superclasses which also have markers. Thanks xmo-odoo for the report and Bruno Oliveira for the PR.

-   preserve warning functions after call to pytest.deprecated_call. Thanks Pieter Mulder for PR.

-   fix issue854: autouse yield_fixtures defined as class members of unittest.TestCase subclasses now work as expected. Thanks xmo-odoo for the report and Bruno Oliveira for the PR.

-   fix issue833: --fixtures now shows all fixtures of collected test files, instead of just the fixtures declared on the first one. Thanks Florian Bruhin for reporting and Bruno Oliveira for the PR.

-   fix issue863: skipped tests now report the correct reason when a skip/xfail condition is met when using multiple markers. Thanks Raphael Pierzina for reporting and Bruno Oliveira for the PR.

-   optimized tmpdir fixture initialization, which should make test sessions faster (specially when using pytest-xdist). The only visible effect is that now pytest uses a subdirectory in the \$TEMP directory for all directories created by this fixture (defaults to \$TEMP/pytest-\$USER). Thanks Bruno Oliveira for the PR.

## 2.7.2 (2015-06-23)[¶](#id897 "Link to this heading")

-   fix issue767: pytest.raises value attribute does not contain the exception instance on Python 2.6. Thanks Eric Siegerman for providing the test case and Bruno Oliveira for PR.

-   Automatically create directory for junitxml and results log. Thanks Aron Curzon.

-   fix issue713: JUnit XML reports for doctest failures. Thanks Punyashloka Biswal.

-   fix issue735: assertion failures on debug versions of Python 3.4+ Thanks Benjamin Peterson.

-   fix issue114: skipif marker reports to internal skipping plugin; Thanks Floris Bruynooghe for reporting and Bruno Oliveira for the PR.

-   fix issue748: unittest.SkipTest reports to internal pytest unittest plugin. Thanks Thomas De Schampheleire for reporting and Bruno Oliveira for the PR.

-   fix issue718: failed to create representation of sets containing unsortable elements in python 2. Thanks Edison Gustavo Muenz.

-   fix issue756, fix issue752 (and similar issues): depend on py-1.4.29 which has a refined algorithm for traceback generation.

## 2.7.1 (2015-05-19)[¶](#id898 "Link to this heading")

-   fix issue731: do not get confused by the braces which may be present and unbalanced in an object's repr while collapsing False explanations. Thanks Carl Meyer for the report and test case.

-   fix issue553: properly handling inspect.getsourcelines failures in FixtureLookupError which would lead to an internal error, obfuscating the original problem. Thanks talljosh for initial diagnose/patch and Bruno Oliveira for final patch.

-   fix issue660: properly report scope-mismatch-access errors independently from ordering of fixture arguments. Also avoid the pytest internal traceback which does not provide information to the user. Thanks Holger Krekel.

-   streamlined and documented release process. Also all versions (in setup.py and documentation generation) are now read from \_pytest/\_\_init\_\_.py. Thanks Holger Krekel.

-   fixed docs to remove the notion that yield-fixtures are experimental. They are here to stay :) Thanks Bruno Oliveira.

-   Support building wheels by using environment markers for the requirements. Thanks Ionel Maries Cristian.

-   fixed regression to 2.6.4 which surfaced e.g. in lost stdout capture printing when tests raised SystemExit. Thanks Holger Krekel.

-   reintroduced \_pytest fixture of the pytester plugin which is used at least by pytest-xdist.

## 2.7.0 (2015-03-26)[¶](#id899 "Link to this heading")

-   fix issue435: make reload() work when assert rewriting is active. Thanks Daniel Hahler.

-   fix issue616: conftest.py files and their contained fixtures are now properly considered for visibility, independently from the exact current working directory and test arguments that are used. Many thanks to Eric Siegerman and his PR235 which contains systematic tests for conftest visibility and now passes. This change also introduces the concept of a [`rootdir`] which is printed as a new pytest header and documented in the pytest customize web page.

-   change reporting of "diverted" tests, i.e. tests that are collected in one file but actually come from another (e.g. when tests in a test class come from a base class in a different file). We now show the nodeid and indicate via a postfix the other file.

-   add ability to set command line options by environment variable PYTEST_ADDOPTS.

-   added documentation on the new pytest-dev teams on bitbucket and github. See [https://pytest.org/en/stable/contributing.html](https://pytest.org/en/stable/contributing.html) . Thanks to Anatoly for pushing and initial work on this.

-   fix issue650: new option [`--doctest-ignore-import-errors`] which will turn import errors in doctests into skips. Thanks Charles Cloud for the complete PR.

-   fix issue655: work around different ways that cause python2/3 to leak sys.exc_info into fixtures/tests causing failures in 3rd party code

-   fix issue615: assertion rewriting did not correctly escape % signs when formatting boolean operations, which tripped over mixing booleans with modulo operators. Thanks to Tom Viner for the report, triaging and fix.

-   implement issue351: add ability to specify parametrize ids as a callable to generate custom test ids. Thanks Brianna Laugher for the idea and implementation.

-   introduce and document new hookwrapper mechanism useful for plugins which want to wrap the execution of certain hooks for their purposes. This supersedes the undocumented [`__multicall__`] protocol which pytest itself and some external plugins use. Note that pytest-2.8 is scheduled to drop supporting the old [`__multicall__`] and only support the hookwrapper protocol.

-   majorly speed up invocation of plugin hooks

-   use hookwrapper mechanism in builtin pytest plugins.

-   add a doctest ini option for doctest flags, thanks Holger Peters.

-   add note to docs that if you want to mark a parameter and the parameter is a callable, you also need to pass in a reason to disambiguate it from the "decorator" case. Thanks Tom Viner.

-   "python_classes" and "python_functions" options now support glob-patterns for test discovery, as discussed in issue600. Thanks Ldiary Translations.

-   allow to override parametrized fixtures with non-parametrized ones and vice versa (bubenkoff).

-   fix issue463: raise specific error for 'parameterize' misspelling (pfctdayelise).

-   On failure, the [`sys.last_value`], [`sys.last_type`] and [`sys.last_traceback`] are set, so that a user can inspect the error via postmortem debugging (almarklein).

## 2.6.4 (2014-10-24)[¶](#id900 "Link to this heading")

-   Improve assertion failure reporting on iterables, by using ndiff and pprint.

-   removed outdated japanese docs from source tree.

-   docs for "pytest_addhooks" hook. Thanks Bruno Oliveira.

-   updated plugin index docs. Thanks Bruno Oliveira.

-   fix issue557: with "-k" we only allow the old style "-" for negation at the beginning of strings and even that is deprecated. Use "not" instead. This should allow to pick parametrized tests where "-" appeared in the parameter.

-   fix issue604: Escape % character in the assertion message.

-   fix issue620: add explanation in the --genscript target about what the binary blob means. Thanks Dinu Gherman.

-   fix issue614: fixed pastebin support.

-   fix issue620: add explanation in the --genscript target about what the binary blob means. Thanks Dinu Gherman.

-   fix issue614: fixed pastebin support.

## 2.6.3 (2014-09-24)[¶](#id901 "Link to this heading")

-   fix issue575: xunit-xml was reporting collection errors as failures instead of errors, thanks Oleg Sinyavskiy.

-   fix issue582: fix setuptools example, thanks Laszlo Papp and Ronny Pfannschmidt.

-   Fix infinite recursion bug when pickling capture.EncodedFile, thanks Uwe Schmitt.

-   fix issue589: fix bad interaction with numpy and others when showing exceptions. Check for precise "maximum recursion depth exceed" exception instead of presuming any RuntimeError is that one (implemented in py dep). Thanks Charles Cloud for analysing the issue.

-   fix conftest related fixture visibility issue: when running with a CWD outside of a test package pytest would get fixture discovery wrong. Thanks to Wolfgang Schnerring for figuring out a reproducible example.

-   Introduce pytest_enter_pdb hook (needed e.g. by pytest_timeout to cancel the timeout when interactively entering pdb). Thanks Wolfgang Schnerring.

-   check xfail/skip also with non-python function test items. Thanks Floris Bruynooghe.

## 2.6.2 (2014-09-05)[¶](#id902 "Link to this heading")

-   Added function pytest.freeze_includes(), which makes it easy to embed pytest into executables using tools like cx_freeze. See docs for examples and rationale. Thanks Bruno Oliveira.

-   Improve assertion rewriting cache invalidation precision.

-   fixed issue561: adapt autouse fixture example for python3.

-   fixed issue453: assertion rewriting issue with \_\_repr\_\_ containing "n" and "n\~".

-   fix issue560: correctly display code if an "else:" or "finally:" is followed by statements on the same line.

-   Fix example in monkeypatch documentation, thanks t-8ch.

-   fix issue572: correct tmpdir doc example for python3.

-   Do not mark as universal wheel because Python 2.6 is different from other builds due to the extra argparse dependency. Fixes issue566. Thanks sontek.

-   Implement issue549: user-provided assertion messages now no longer replace the py.test introspection message but are shown in addition to them.

## 2.6.1 (2014-08-07)[¶](#id903 "Link to this heading")

-   No longer show line numbers in the --verbose output, the output is now purely the nodeid. The line number is still shown in failure reports. Thanks Floris Bruynooghe.

-   fix issue437 where assertion rewriting could cause pytest-xdist worker nodes to collect different tests. Thanks Bruno Oliveira.

-   fix issue555: add "errors" attribute to capture-streams to satisfy some distutils and possibly other code accessing sys.stdout.errors.

-   fix issue547 capsys/capfd also work when output capturing ("-s") is disabled.

-   address issue170: allow pytest.mark.xfail(...) to specify expected exceptions via an optional "raises=EXC" argument where EXC can be a single exception or a tuple of exception classes. Thanks David Mohr for the complete PR.

-   fix integration of pytest with unittest.mock.patch decorator when it uses the "new" argument. Thanks Nicolas Delaby for test and PR.

-   fix issue with detecting conftest files if the arguments contain "::" node id specifications (copy pasted from "-v" output)

-   fix issue544 by only removing "@NUM" at the end of "::" separated parts and if the part has a ".py" extension

-   don't use py.std import helper, rather import things directly. Thanks Bruno Oliveira.

## 2.6[¶](#id904 "Link to this heading")

-   Cache exceptions from fixtures according to their scope (issue 467).

-   fix issue537: Avoid importing old assertion reinterpretation code by default.

-   fix issue364: shorten and enhance tracebacks representation by default. The new "--tb=auto" option (default) will only display long tracebacks for the first and last entry. You can get the old behaviour of printing all entries as long entries with "--tb=long". Also short entries by default are now printed very similarly to "--tb=native" ones.

-   fix issue514: teach assertion reinterpretation about private class attributes

-   change -v output to include full node IDs of tests. Users can copy a node ID from a test run, including line number, and use it as a positional argument in order to run only a single test.

-   fix issue 475: fail early and comprehensible if calling pytest.raises with wrong exception type.

-   fix issue516: tell in getting-started about current dependencies.

-   cleanup setup.py a bit and specify supported versions. Thanks Jurko Gospodnetic for the PR.

-   change XPASS colour to yellow rather than red when tests are run with -v.

-   fix issue473: work around mock putting an unbound method into a class dict when double-patching.

-   fix issue498: if a fixture finalizer fails, make sure that the fixture is still invalidated.

-   fix issue453: the result of the pytest_assertrepr_compare hook now gets it's newlines escaped so that format_exception does not blow up.

-   internal new warning system: pytest will now produce warnings when it detects oddities in your test collection or execution. Warnings are ultimately sent to a new pytest_logwarning hook which is currently only implemented by the terminal plugin which displays warnings in the summary line and shows more details when -rw (report on warnings) is specified.

-   change skips into warnings for test classes with an \_\_init\_\_ and callables in test modules which look like a test but are not functions.

-   fix issue436: improved finding of initial conftest files from command line arguments by using the result of parse_known_args rather than the previous flaky heuristics. Thanks Marc Abramowitz for tests and initial fixing approaches in this area.

-   fix issue #479: properly handle nose/unittest(2) SkipTest exceptions during collection/loading of test modules. Thanks to Marc Schlaich for the complete PR.

-   fix issue490: include pytest_load_initial_conftests in documentation and improve docstring.

-   fix issue472: clarify that [`pytest.config.getvalue()`] cannot work if it's triggered ahead of command line parsing.

-   merge PR123: improved integration with mock.patch decorator on tests.

-   fix issue412: messing with stdout/stderr FD-level streams is now captured without crashes.

-   fix issue483: trial/py33 works now properly. Thanks Daniel Grana for PR.

-   improve example for pytest integration with "python setup.py test" which now has a generic "-a" or "--pytest-args" option where you can pass additional options as a quoted string. Thanks Trevor Bekolay.

-   simplified internal capturing mechanism and made it more robust against tests or setups changing FD1/FD2, also better integrated now with pytest.pdb() in single tests.

-   improvements to pytest's own test-suite leakage detection, courtesy of PRs from Marc Abramowitz

-   fix issue492: avoid leak in test_writeorg. Thanks Marc Abramowitz.

-   fix issue493: don't run tests in doc directory with [`python`]` `[`setup.py`]` `[`test`] (use tox -e doctesting for that)

-   fix issue486: better reporting and handling of early conftest loading failures

-   some cleanup and simplification of internal conftest handling.

-   work a bit harder to break reference cycles when catching exceptions. Thanks Jurko Gospodnetic.

-   fix issue443: fix skip examples to use proper comparison. Thanks Alex Groenholm.

-   support nose-style [`__test__`] attribute on modules, classes and functions, including unittest-style Classes. If set to False, the test will not be collected.

-   fix issue512: show "\<notset\>" for arguments which might not be set in monkeypatch plugin. Improves output in documentation.

## 2.5.2 (2014-01-29)[¶](#id905 "Link to this heading")

-   fix issue409 -- better interoperate with cx_freeze by not trying to import from collections.abc which causes problems for py27/cx_freeze. Thanks Wolfgang L. for reporting and tracking it down.

-   fixed docs and code to use "pytest" instead of "py.test" almost everywhere. Thanks Jurko Gospodnetic for the complete PR.

-   fix issue425: mention at end of "py.test -h" that --markers and --fixtures work according to specified test path (or current dir)

-   fix issue413: exceptions with unicode attributes are now printed correctly also on python2 and with pytest-xdist runs. (the fix requires py-1.4.20)

-   copy, cleanup and integrate py.io capture from pylib 1.4.20.dev2 (rev 13d9af95547e)

-   address issue416: clarify docs as to conftest.py loading semantics

-   fix issue429: comparing byte strings with non-ascii chars in assert expressions now work better. Thanks Floris Bruynooghe.

-   make capfd/capsys.capture private, its unused and shouldn't be exposed

## 2.5.1 (2013-12-17)[¶](#id906 "Link to this heading")

-   merge new documentation styling PR from Tobias Bieniek.

-   fix issue403: allow parametrize of multiple same-name functions within a collection node. Thanks Andreas Kloeckner and Alex Gaynor for reporting and analysis.

-   Allow parameterized fixtures to specify the ID of the parameters by adding an ids argument to pytest.fixture() and pytest.yield_fixture(). Thanks Floris Bruynooghe.

-   fix issue404 by always using the binary xml escape in the junitxml plugin. Thanks Ronny Pfannschmidt.

-   fix issue407: fix addoption docstring to point to argparse instead of optparse. Thanks Daniel D. Wright.

## 2.5.0 (2013-12-12)[¶](#id907 "Link to this heading")

-   dropped python2.5 from automated release testing of pytest itself which means it's probably going to break soon (but still works with this release we believe).

-   simplified and fixed implementation for calling finalizers when parametrized fixtures or function arguments are involved. finalization is now performed lazily at setup time instead of in the "teardown phase". While this might sound odd at first, it helps to ensure that we are correctly handling setup/teardown even in complex code. User-level code should not be affected unless it's implementing the pytest_runtest_teardown hook and expecting certain fixture instances are torn down within (very unlikely and would have been unreliable anyway).

-   PR90: add --color=yes\|no\|auto option to force terminal coloring mode ("auto" is default). Thanks Marc Abramowitz.

-   fix issue319 - correctly show unicode in assertion errors. Many thanks to Floris Bruynooghe for the complete PR. Also means we depend on py\>=1.4.19 now.

-   fix issue396 - correctly sort and finalize class-scoped parametrized tests independently from number of methods on the class.

-   refix issue323 in a better way -- parametrization should now never cause Runtime Recursion errors because the underlying algorithm for re-ordering tests per-scope/per-fixture is not recursive anymore (it was tail-call recursive before which could lead to problems for more than \>966 non-function scoped parameters).

-   fix issue290 - there is preliminary support now for parametrizing with repeated same values (sometimes useful to test if calling a second time works as with the first time).

-   close issue240 - document precisely how pytest module importing works, discuss the two common test directory layouts, and how it interacts with [][**PEP 420**](https://peps.python.org/pep-0420/)-namespace packages.

-   fix issue246 fix finalizer order to be LIFO on independent fixtures depending on a parametrized higher-than-function scoped fixture. (was quite some effort so please bear with the complexity of this sentence :) Thanks Ralph Schmitt for the precise failure example.

-   fix issue244 by implementing special index for parameters to only use indices for parametrized test ids

-   fix issue287 by running all finalizers but saving the exception from the first failing finalizer and re-raising it so teardown will still have failed. We reraise the first failing exception because it might be the cause for other finalizers to fail.

-   fix ordering when mock.patch or other standard decorator-wrappings are used with test methods. This fixes issue346 and should help with random "xdist" collection failures. Thanks to Ronny Pfannschmidt and Donald Stufft for helping to isolate it.

-   fix issue357 - special case "-k" expressions to allow for filtering with simple strings that are not valid python expressions. Examples: "-k 1.3" matches all tests parametrized with 1.3. "-k None" filters all tests that have "None" in their name and conversely "-k 'not None'". Previously these examples would raise syntax errors.

-   fix issue384 by removing the trial support code since the unittest compat enhancements allow trial to handle it on its own

-   don't hide an ImportError when importing a plugin produces one. fixes issue375.

-   fix issue275 - allow usefixtures and autouse fixtures for running doctest text files.

-   fix issue380 by making --resultlog only rely on longrepr instead of the "reprcrash" attribute which only exists sometimes.

-   address issue122: allow \@pytest.fixture(params=iterator) by exploding into a list early on.

-   fix pexpect-3.0 compatibility for pytest's own tests. (fixes issue386)

-   allow nested parametrize-value markers, thanks James Lan for the PR.

-   fix unicode handling with new monkeypatch.setattr(import_path, value) API. Thanks Rob Dennis. Fixes issue371.

-   fix unicode handling with junitxml, fixes issue368.

-   In assertion rewriting mode on Python 2, fix the detection of coding cookies. See issue #330.

-   make "--runxfail" turn imperative pytest.xfail calls into no ops (it already did neutralize pytest.mark.xfail markers)

-   refine pytest / pkg_resources interactions: The AssertionRewritingHook [][**PEP 302**](https://peps.python.org/pep-0302/) compliant loader now registers itself with setuptools/pkg_resources properly so that the pkg_resources.resource_stream method works properly. Fixes issue366. Thanks for the investigations and full PR to Jason R. Coombs.

-   pytestconfig fixture is now session-scoped as it is the same object during the whole test run. Fixes issue370.

-   avoid one surprising case of marker malfunction/confusion:

    ::: 
    ::: highlight
        @pytest.mark.some(lambda arg: ...)
        def test_function():
    :::
    :::

    would not work correctly because pytest assumes \@pytest.mark.some gets a function to be decorated already. We now at least detect if this arg is a lambda and thus the example will work. Thanks Alex Gaynor for bringing it up.

-   xfail a test on pypy that checks wrong encoding/ascii (pypy does not error out). fixes issue385.

-   internally make varnames() deal with classes's \_\_init\_\_, although it's not needed by pytest itself atm. Also fix caching. Fixes issue376.

-   fix issue221 - handle importing of namespace-package with no \_\_init\_\_.py properly.

-   refactor internal FixtureRequest handling to avoid monkeypatching. One of the positive user-facing effects is that the "request" object can now be used in closures.

-   fixed version comparison in pytest.importskip(modname, minverstring)

-   fix issue377 by clarifying in the nose-compat docs that pytest does not duplicate the unittest-API into the "plain" namespace.

-   fix verbose reporting for \@mock'd test functions

## 2.4.2 (2013-10-04)[¶](#id908 "Link to this heading")

-   on Windows require colorama and a newer py lib so that py.io.TerminalWriter() now uses colorama instead of its own ctypes hacks. (fixes issue365) thanks Paul Moore for bringing it up.

-   fix "-k" matching of tests where "repr" and "attr" and other names would cause wrong matches because of an internal implementation quirk (don't ask) which is now properly implemented. fixes issue345.

-   avoid tmpdir fixture to create too long filenames especially when parametrization is used (issue354)

-   fix pytest-pep8 and pytest-flakes / pytest interactions (collection names in mark plugin was assuming an item always has a function which is not true for those plugins etc.) Thanks Andi Zeidler.

-   introduce node.get_marker/node.add_marker API for plugins like pytest-pep8 and pytest-flakes to avoid the messy details of the node.keywords pseudo-dicts. Adapted docs.

-   remove attempt to "dup" stdout at startup as it's icky. the normal capturing should catch enough possibilities of tests messing up standard FDs.

-   add pluginmanager.do_configure(config) as a link to config.do_configure() for plugin-compatibility

## 2.4.1 (2013-10-02)[¶](#id909 "Link to this heading")

-   When using parser.addoption() unicode arguments to the "type" keyword should also be converted to the respective types. thanks Floris Bruynooghe, \@dnozay. (fixes issue360 and issue362)

-   fix dotted filename completion when using argcomplete thanks Anthon van der Neuth. (fixes issue361)

-   fix regression when a 1-tuple ("arg",) is used for specifying parametrization (the values of the parametrization were passed nested in a tuple). Thanks Donald Stufft.

-   merge doc typo fixes, thanks Andy Dirnberger

## 2.4[¶](#id910 "Link to this heading")

known incompatibilities:

-   if calling --genscript from python2.7 or above, you only get a standalone script which works on python2.7 or above. Use Python2.6 to also get a python2.5 compatible version.

-   all xunit-style teardown methods (nose-style, pytest-style, unittest-style) will not be called if the corresponding setup method failed, see issue322 below.

-   the pytest_plugin_unregister hook wasn't ever properly called and there is no known implementation of the hook - so it got removed.

-   pytest.fixture-decorated functions cannot be generators (i.e. use yield) anymore. This change might be reversed in 2.4.1 if it causes unforeseen real-life issues. However, you can always write and return an inner function/generator and change the fixture consumer to iterate over the returned generator. This change was done in lieu of the new [`pytest.yield_fixture`] decorator, see below.

new features:

-   experimentally introduce a new [`pytest.yield_fixture`] decorator which accepts exactly the same parameters as pytest.fixture but mandates a [`yield`] statement instead of a [`return`]` `[`statement`] from fixture functions. This allows direct integration with "with-style" context managers in fixture functions and generally avoids registering of finalization callbacks in favour of treating the "after-yield" as teardown code. Thanks Andreas Pelme, Vladimir Keleshev, Floris Bruynooghe, Ronny Pfannschmidt and many others for discussions.

-   allow boolean expression directly with skipif/xfail if a "reason" is also specified. Rework skipping documentation to recommend "condition as booleans" because it prevents surprises when importing markers between modules. Specifying conditions as strings will remain fully supported.

-   reporting: color the last line red or green depending if failures/errors occurred or everything passed. thanks Christian Theunert.

-   make "import pdb ; pdb.set_trace()" work natively wrt capturing (no "-s" needed anymore), making [`pytest.set_trace()`] a mere shortcut.

-   fix issue181: --pdb now also works on collect errors (and on internal errors) . This was implemented by a slight internal refactoring and the introduction of a new hook [`pytest_exception_interact`] hook (see next item).

-   fix issue341: introduce new experimental hook for IDEs/terminals to intercept debugging: [`pytest_exception_interact(node,`]` `[`call,`]` `[`report)`].

-   new monkeypatch.setattr() variant to provide a shorter invocation for patching out classes/functions from modules:

    > <div>
    >
    > monkeypatch.setattr("requests.get", myfunc)
    >
    > </div>

    will replace the "get" function of the "requests" module with [`myfunc`].

-   fix issue322: tearDownClass is not run if setUpClass failed. Thanks Mathieu Agopian for the initial fix. Also make all of pytest/nose finalizer mimic the same generic behaviour: if a setupX exists and fails, don't run teardownX. This internally introduces a new method "node.addfinalizer()" helper which can only be called during the setup phase of a node.

-   simplify pytest.mark.parametrize() signature: allow to pass a CSV-separated string to specify argnames. For example: [`pytest.mark.parametrize("input,expected",`]`  `[`[(1,2),`]` `[`(2,3)])`] works as well as the previous: [`pytest.mark.parametrize(("input",`]` `[`"expected"),`]` `[`...)`].

-   add support for setUpModule/tearDownModule detection, thanks Brian Okken.

-   integrate tab-completion on options through use of "argcomplete". Thanks Anthon van der Neut for the PR.

-   change option names to be hyphen-separated long options but keep the old spelling backward compatible. py.test -h will only show the hyphenated version, for example "--collect-only" but "--collectonly" will remain valid as well (for backward-compat reasons). Many thanks to Anthon van der Neut for the implementation and to Hynek Schlawack for pushing us.

-   fix issue 308 - allow to mark/xfail/skip individual parameter sets when parametrizing. Thanks Brianna Laugher.

-   call new experimental pytest_load_initial_conftests hook to allow 3rd party plugins to do something before a conftest is loaded.

Bug fixes:

-   fix issue358 - capturing options are now parsed more properly by using a new parser.parse_known_args method.

-   pytest now uses argparse instead of optparse (thanks Anthon) which means that "argparse" is added as a dependency if installing into python2.6 environments or below.

-   fix issue333: fix a case of bad unittest/pytest hook interaction.

-   PR27: correctly handle nose.SkipTest during collection. Thanks Antonio Cuni, Ronny Pfannschmidt.

-   fix issue355: junitxml puts name="pytest" attribute to testsuite tag.

-   fix issue336: autouse fixture in plugins should work again.

-   fix issue279: improve object comparisons on assertion failure for standard datatypes and recognise collections.abc. Thanks to Brianna Laugher and Mathieu Agopian.

-   fix issue317: assertion rewriter support for the is_package method

-   fix issue335: document py.code.ExceptionInfo() object returned from pytest.raises(), thanks Mathieu Agopian.

-   remove implicit distribute_setup support from setup.py.

-   fix issue305: ignore any problems when writing pyc files.

-   SO-17664702: call fixture finalizers even if the fixture function partially failed (finalizers would not always be called before)

-   fix issue320 - fix class scope for fixtures when mixed with module-level functions. Thanks Anatoly Bubenkoff.

-   you can specify "-q" or "-qq" to get different levels of "quieter" reporting (thanks Katarzyna Jachim)

-   fix issue300 - Fix order of conftest loading when starting py.test in a subdirectory.

-   fix issue323 - sorting of many module-scoped arg parametrizations

-   make sessionfinish hooks execute with the same cwd-context as at session start (helps fix plugin behaviour which write output files with relative path such as pytest-cov)

-   fix issue316 - properly reference collection hooks in docs

-   fix issue 306 - cleanup of -k/-m options to only match markers/test names/keywords respectively. Thanks Wouter van Ackooy.

-   improved doctest counting for doctests in python modules -- files without any doctest items will not show up anymore and doctest examples are counted as separate test items. thanks Danilo Bellini.

-   fix issue245 by depending on the released py-1.4.14 which fixes py.io.dupfile to work with files with no mode. Thanks Jason R. Coombs.

-   fix junitxml generation when test output contains control characters, addressing issue267, thanks Jaap Broekhuizen

-   fix issue338: honor --tb style for setup/teardown errors as well. Thanks Maho.

-   fix issue307 - use yaml.safe_load in example, thanks Mark Eichin.

-   better parametrize error messages, thanks Brianna Laugher

-   pytest_terminal_summary(terminalreporter) hooks can now use ".section(title)" and ".line(msg)" methods to print extra information at the end of a test run.

## 2.3.5 (2013-04-30)[¶](#id911 "Link to this heading")

-   fix issue169: respect --tb=style with setup/teardown errors as well.

-   never consider a fixture function for test function collection

-   allow re-running of test items / helps to fix pytest-reruntests plugin and also help to keep less fixture/resource references alive

-   put captured stdout/stderr into junitxml output even for passing tests (thanks Adam Goucher)

-   Issue 265 - integrate nose setup/teardown with setupstate so it doesn't try to teardown if it did not setup

-   issue 271 - don't write junitxml on worker nodes

-   Issue 274 - don't try to show full doctest example when doctest does not know the example location

-   issue 280 - disable assertion rewriting on buggy CPython 2.6.0

-   inject "getfixture()" helper to retrieve fixtures from doctests, thanks Andreas Zeidler

-   issue 259 - when assertion rewriting, be consistent with the default source encoding of ASCII on Python 2

-   issue 251 - report a skip instead of ignoring classes with init

-   issue250 unicode/str mixes in parametrization names and values now works

-   issue257, assertion-triggered compilation of source ending in a comment line doesn't blow up in python2.5 (fixed through py\>=1.4.13.dev6)

-   fix --genscript option to generate standalone scripts that also work with python3.3 (importer ordering)

-   issue171 - in assertion rewriting, show the repr of some global variables

-   fix option help for "-k"

-   move long description of distribution into README.rst

-   improve docstring for metafunc.parametrize()

-   fix bug where using capsys with pytest.set_trace() in a test function would break when looking at capsys.readouterr()

-   allow to specify prefixes starting with "\_" when customizing python_functions test discovery. (thanks Graham Horler)

-   improve PYTEST_DEBUG tracing output by putting extra data on a new lines with additional indent

-   ensure OutcomeExceptions like skip/fail have initialized exception attributes

-   issue 260 - don't use nose special setup on plain unittest cases

-   fix issue134 - print the collect errors that prevent running specified test items

-   fix issue266 - accept unicode in MarkEvaluator expressions

## 2.3.4 (2012-11-20)[¶](#id912 "Link to this heading")

-   yielded test functions will now have autouse-fixtures active but cannot accept fixtures as funcargs - it's anyway recommended to rather use the post-2.0 parametrize features instead of yield, see: [http://pytest.org/en/stable/example/how-to/parametrize.html](http://pytest.org/en/stable/example/how-to/parametrize.html)

-   fix autouse-issue where autouse-fixtures would not be discovered if defined in an a/conftest.py file and tests in a/tests/test_some.py

-   fix issue226 - LIFO ordering for fixture teardowns

-   fix issue224 - invocations with \>256 char arguments now work

-   fix issue91 - add/discuss package/directory level setups in example

-   allow to dynamically define markers via item.keywords\[...\]=assignment integrating with "-m" option

-   make "-k" accept an expressions the same as with "-m" so that one can write: -k "name1 or name2" etc. This is a slight incompatibility if you used special syntax like "TestClass.test_method" which you now need to write as -k "TestClass and test_method" to match a certain method in a certain test class.

## 2.3.3 (2012-11-06)[¶](#id913 "Link to this heading")

-   fix issue214 - parse modules that contain special objects like e. g. flask's request object which blows up on getattr access if no request is active. thanks Thomas Waldmann.

-   fix issue213 - allow to parametrize with values like numpy arrays that do not support an \_\_eq\_\_ operator

-   fix issue215 - split test_python.org into multiple files

-   fix issue148 - \@unittest.skip on classes is now recognized and avoids calling setUpClass/tearDownClass, thanks Pavel Repin

-   fix issue209 - reintroduce python2.4 support by depending on newer pylib which re-introduced statement-finding for pre-AST interpreters

-   nose support: only call setup if it's a callable, thanks Andrew Taumoefolau

-   fix issue219 - add py2.4-3.3 classifiers to TROVE list

-   in tracebacks *,\** arg values are now shown next to normal arguments (thanks Manuel Jacob)

-   fix issue217 - support mock.patch with pytest's fixtures - note that you need either mock-1.0.1 or the python3.3 builtin unittest.mock.

-   fix issue127 - improve documentation for pytest_addoption() and add a [`config.getoption(name)`] helper function for consistency.

## 2.3.2 (2012-10-25)[¶](#id914 "Link to this heading")

-   fix issue208 and fix issue29 use new py version to avoid long pauses when printing tracebacks in long modules

-   fix issue205 - conftests in subdirs customizing pytest_pycollect_makemodule and pytest_pycollect_makeitem now work properly

-   fix teardown-ordering for parametrized setups

-   fix issue127 - better documentation for pytest_addoption and related objects.

-   fix unittest behaviour: TestCase.runtest only called if there are test methods defined

-   improve trial support: don't collect its empty unittest.TestCase.runTest() method

-   "python setup.py test" now works with pytest itself

-   fix/improve internal/packaging related bits:

    -   exception message check of test_nose.py now passes on python33 as well

    -   issue206 - fix test_assertrewrite.py to work when a global PYTHONDONTWRITEBYTECODE=1 is present

    -   add tox.ini to pytest distribution so that ignore-dirs and others config bits are properly distributed for maintainers who run pytest-own tests

## 2.3.1 (2012-10-20)[¶](#id915 "Link to this heading")

-   fix issue202 - fix regression: using "self" from fixture functions now works as expected (it's the same "self" instance that a test method which uses the fixture sees)

-   skip pexpect using tests (test_pdb.py mostly) on freebsd\* systems due to pexpect not supporting it properly (hanging)

-   link to web pages from --markers output which provides help for pytest.mark.\* usage.

## 2.3.0 (2012-10-19)[¶](#id916 "Link to this heading")

-   fix issue202 - better automatic names for parametrized test functions

-   fix issue139 - introduce \@pytest.fixture which allows direct scoping and parametrization of funcarg factories.

-   fix issue198 - conftest fixtures were not found on windows32 in some circumstances with nested directory structures due to path manipulation issues

-   fix issue193 skip test functions with were parametrized with empty parameter sets

-   fix python3.3 compat, mostly reporting bits that previously depended on dict ordering

-   introduce re-ordering of tests by resource and parametrization setup which takes precedence to the usual file-ordering

-   fix issue185 monkeypatching time.time does not cause pytest to fail

-   fix issue172 duplicate call of pytest.fixture decoratored setup_module functions

-   fix junitxml=path construction so that if tests change the current working directory and the path is a relative path it is constructed correctly from the original current working dir.

-   fix "python setup.py test" example to cause a proper "errno" return

-   fix issue165 - fix broken doc links and mention stackoverflow for FAQ

-   catch unicode-issues when writing failure representations to terminal to prevent the whole session from crashing

-   fix xfail/skip confusion: a skip-mark or an imperative pytest.skip will now take precedence before xfail-markers because we can't determine xfail/xpass status in case of a skip. see also: [http://stackoverflow.com/questions/11105828/in-py-test-when-i-explicitly-skip-a-test-that-is-marked-as-xfail-how-can-i-get](http://stackoverflow.com/questions/11105828/in-py-test-when-i-explicitly-skip-a-test-that-is-marked-as-xfail-how-can-i-get)

-   always report installed 3rd party plugins in the header of a test run

-   fix issue160: a failing setup of an xfail-marked tests should be reported as xfail (not xpass)

-   fix issue128: show captured output when capsys/capfd are used

-   fix issue179: properly show the dependency chain of factories

-   pluginmanager.register(...) now raises ValueError if the plugin has been already registered or the name is taken

-   fix issue159: improve [https://docs.pytest.org/en/6.0.1/faq.html](https://docs.pytest.org/en/6.0.1/faq.html) especially with respect to the "magic" history, also mention pytest-django, trial and unittest integration.

-   make request.keywords and node.keywords writable. All descendant collection nodes will see keyword values. Keywords are dictionaries containing markers and other info.

-   fix issue 178: xml binary escapes are now wrapped in py.xml.raw

-   fix issue 176: correctly catch the builtin AssertionError even when we replaced AssertionError with a subclass on the python level

-   factory discovery no longer fails with magic global callables that provide no sane \_\_code\_\_ object (mock.call for example)

-   fix issue 182: testdir.inprocess_run now considers passed plugins

-   

    fix issue 188: ensure sys.exc_info is clear on python2

    :   before calling into a test

-   fix issue 191: add unittest TestCase runTest method support

-   fix issue 156: monkeypatch correctly handles class level descriptors

-   reporting refinements:

    -   pytest_report_header now receives a "startdir" so that you can use startdir.bestrelpath(yourpath) to show nice relative path

    -   allow plugins to implement both pytest_report_header and pytest_sessionstart (sessionstart is invoked first).

    -   don't show deselected reason line if there is none

    -   py.test -vv will show all of assert comparisons instead of truncating

## 2.2.4 (2012-05-22)[¶](#id917 "Link to this heading")

-   fix error message for rewritten assertions involving the % operator

-   fix issue 126: correctly match all invalid xml characters for junitxml binary escape

-   fix issue with unittest: now \@unittest.expectedFailure markers should be processed correctly (you can also use \@pytest.mark markers)

-   document integration with the extended distribute/setuptools test commands

-   fix issue 140: properly get the real functions of bound classmethods for setup/teardown_class

-   fix issue #141: switch from the deceased paste.pocoo.org to bpaste.net

-   fix issue #143: call unconfigure/sessionfinish always when configure/sessionstart where called

-   fix issue #144: better mangle test ids to junitxml classnames

-   upgrade distribute_setup.py to 0.6.27

## 2.2.3 (2012-02-05)[¶](#id918 "Link to this heading")

-   fix uploaded package to only include necessary files

## 2.2.2 (2012-02-05)[¶](#id919 "Link to this heading")

-   fix issue101: wrong args to unittest.TestCase test function now produce better output

-   fix issue102: report more useful errors and hints for when a test directory was renamed and some pyc/\_\_pycache\_\_ remain

-   fix issue106: allow parametrize to be applied multiple times e.g. from module, class and at function level.

-   fix issue107: actually perform session scope finalization

-   don't check in parametrize if indirect parameters are funcarg names

-   add chdir method to monkeypatch funcarg

-   fix crash resulting from calling monkeypatch undo a second time

-   fix issue115: make --collectonly robust against early failure (missing files/directories)

-   "-qq --collectonly" now shows only files and the number of tests in them

-   "-q --collectonly" now shows test ids

-   allow adding of attributes to test reports such that it also works with distributed testing (no upgrade of pytest-xdist needed)

## 2.2.1 (2011-12-16)[¶](#id920 "Link to this heading")

-   fix issue99 (in pytest and py) internallerrors with resultlog now produce better output - fixed by normalizing pytest_internalerror input arguments.

-   fix issue97 / traceback issues (in pytest and py) improve traceback output in conjunction with jinja2 and cython which hack tracebacks

-   fix issue93 (in pytest and pytest-xdist) avoid "delayed teardowns": the final test in a test node will now run its teardown directly instead of waiting for the end of the session. Thanks Dave Hunt for the good reporting and feedback. The pytest_runtest_protocol as well as the pytest_runtest_teardown hooks now have "nextitem" available which will be None indicating the end of the test run.

-   fix collection crash due to unknown-source collected items, thanks to Ralf Schmitt (fixed by depending on a more recent pylib)

## 2.2.0 (2011-11-18)[¶](#id921 "Link to this heading")

-   fix issue90: introduce eager tearing down of test items so that teardown function are called earlier.

-   add an all-powerful metafunc.parametrize function which allows to parametrize test function arguments in multiple steps and therefore from independent plugins and places.

-   add a \@pytest.mark.parametrize helper which allows to easily call a test function with different argument values

-   Add examples to the "parametrize" example page, including a quick port of Test scenarios and the new parametrize function and decorator.

-   introduce registration for "pytest.mark.\*" helpers via ini-files or through plugin hooks. Also introduce a "--strict" option which will treat unregistered markers as errors allowing to avoid typos and maintain a well described set of markers for your test suite. See examples at [http://pytest.org/en/stable/how-to/mark.html](http://pytest.org/en/stable/how-to/mark.html) and its links.

-   issue50: introduce "-m marker" option to select tests based on markers (this is a stricter and more predictable version of '-k' in that "-m" only matches complete markers and has more obvious rules for and/or semantics.

-   new feature to help optimizing the speed of your tests: --durations=N option for displaying N slowest test calls and setup/teardown methods.

-   fix issue87: --pastebin now works with python3

-   fix issue89: --pdb with unexpected exceptions in doctest work more sensibly

-   fix and cleanup pytest's own test suite to not leak FDs

-   fix issue83: link to generated funcarg list

-   fix issue74: pyarg module names are now checked against imp.find_module false positives

-   fix compatibility with twisted/trial-11.1.0 use cases

-   simplify Node.listchain

-   simplify junitxml output code by relying on py.xml

-   add support for skip properties on unittest classes and functions

## 2.1.3 (2011-10-18)[¶](#id922 "Link to this heading")

-   fix issue79: assertion rewriting failed on some comparisons in boolops

-   correctly handle zero length arguments (a la pytest '')

-   fix issue67 / junitxml now contains correct test durations, thanks ronny

-   fix issue75 / skipping test failure on jython

-   fix issue77 / Allow assertrepr_compare hook to apply to a subset of tests

## 2.1.2 (2011-09-24)[¶](#id923 "Link to this heading")

-   fix assertion rewriting on files with windows newlines on some Python versions

-   refine test discovery by package/module name (--pyargs), thanks Florian Mayer

-   fix issue69 / assertion rewriting fixed on some boolean operations

-   fix issue68 / packages now work with assertion rewriting

-   fix issue66: use different assertion rewriting caches when the -O option is passed

-   don't try assertion rewriting on Jython, use reinterp

## 2.1.1[¶](#id924 "Link to this heading")

-   fix issue64 / pytest.set_trace now works within pytest_generate_tests hooks

-   fix issue60 / fix error conditions involving the creation of \_\_pycache\_\_

-   fix issue63 / assertion rewriting on inserts involving strings containing '%'

-   fix assertion rewriting on calls with a \*\* arg

-   don't cache rewritten modules if bytecode generation is disabled

-   fix assertion rewriting in read-only directories

-   fix issue59: provide system-out/err tags for junitxml output

-   fix issue61: assertion rewriting on boolean operations with 3 or more operands

-   you can now build a man page with "cd doc ; make man"

## 2.1.0 (2011-07-09)[¶](#id925 "Link to this heading")

-   fix issue53 call nosestyle setup functions with correct ordering

-   fix issue58 and issue59: new assertion code fixes

-   merge Benjamin's assertionrewrite branch: now assertions for test modules on python 2.6 and above are done by rewriting the AST and saving the pyc file before the test module is imported. see doc/assert.txt for more info.

-   fix issue43: improve doctests with better traceback reporting on unexpected exceptions

-   fix issue47: timing output in junitxml for test cases is now correct

-   fix issue48: typo in MarkInfo repr leading to exception

-   fix issue49: avoid confusing error when initialization partially fails

-   fix issue44: env/username expansion for junitxml file path

-   show releaselevel information in test runs for pypy

-   reworked doc pages for better navigation and PDF generation

-   report KeyboardInterrupt even if interrupted during session startup

-   fix issue 35 - provide PDF doc version and download link from index page

## 2.0.3 (2011-05-11)[¶](#id926 "Link to this heading")

-   fix issue38: nicer tracebacks on calls to hooks, particularly early configure/sessionstart ones

-   fix missing skip reason/meta information in junitxml files, reported via [http://lists.idyll.org/pipermail/testing-in-python/2011-March/003928.html](http://lists.idyll.org/pipermail/testing-in-python/2011-March/003928.html)

-   fix issue34: avoid collection failure with "test" prefixed classes deriving from object.

-   don't require zlib (and other libs) for genscript plugin without --genscript actually being used.

-   speed up skips (by not doing a full traceback representation internally)

-   fix issue37: avoid invalid characters in junitxml's output

## 2.0.2 (2011-03-09)[¶](#id927 "Link to this heading")

-   tackle issue32 - speed up test runs of very quick test functions by reducing the relative overhead

-   fix issue30 - extended xfail/skipif handling and improved reporting. If you have a syntax error in your skip/xfail expressions you now get nice error reports.

    Also you can now access module globals from xfail/skipif expressions so that this for example works now:

    ::: 
    ::: highlight
        import pytest
        import mymodule
        @pytest.mark.skipif("mymodule.__version__[0] == "1")
        def test_function():
            pass
    :::
    :::

    This will not run the test function if the module's version string does not start with a "1". Note that specifying a string instead of a boolean expressions allows py.test to report meaningful information when summarizing a test run as to what conditions lead to skipping (or xfail-ing) tests.

-   fix issue28 - setup_method and pytest_generate_tests work together The setup_method fixture method now gets called also for test function invocations generated from the pytest_generate_tests hook.

-   fix issue27 - collectonly and keyword-selection (-k) now work together Also, if you do "py.test --collectonly -q" you now get a flat list of test ids that you can use to paste to the py.test commandline in order to execute a particular test.

-   fix issue25 avoid reported problems with --pdb and python3.2/encodings output

-   fix issue23 - tmpdir argument now works on Python3.2 and WindowsXP Starting with Python3.2 os.symlink may be supported. By requiring a newer py lib version the py.path.local() implementation acknowledges this.

-   fixed typos in the docs (thanks Victor Garcia, Brianna Laugher) and particular thanks to Laura Creighton who also reviewed parts of the documentation.

-   fix slightly wrong output of verbose progress reporting for classes (thanks Amaury)

-   more precise (avoiding of) deprecation warnings for node.Class\|Function accesses

-   avoid std unittest assertion helper code in tracebacks (thanks Ronny)

## 2.0.1 (2011-02-07)[¶](#id928 "Link to this heading")

-   refine and unify initial capturing so that it works nicely even if the logging module is used on an early-loaded conftest.py file or plugin.

-   allow to omit "()" in test ids to allow for uniform test ids as produced by Alfredo's nice pytest.vim plugin.

-   fix issue12 - show plugin versions with "--version" and "--traceconfig" and also document how to add extra information to reporting test header

-   fix issue17 (import-\* reporting issue on python3) by requiring py\>1.4.0 (1.4.1 is going to include it)

-   fix issue10 (numpy arrays truth checking) by refining assertion interpretation in py lib

-   fix issue15: make nose compatibility tests compatible with python3 (now that nose-1.0 supports python3)

-   remove somewhat surprising "same-conftest" detection because it ignores conftest.py when they appear in several subdirs.

-   improve assertions ("not in"), thanks Floris Bruynooghe

-   improve behaviour/warnings when running on top of "python -OO" (assertions and docstrings are turned off, leading to potential false positives)

-   introduce a pytest_cmdline_processargs(args) hook to allow dynamic computation of command line arguments. This fixes a regression because py.test prior to 2.0 allowed to set command line options from conftest.py files which so far pytest-2.0 only allowed from ini-files now.

-   fix issue7: assert failures in doctest modules. unexpected failures in doctests will not generally show nicer, i.e. within the doctest failing context.

-   fix issue9: setup/teardown functions for an xfail-marked test will report as xfail if they fail but report as normally passing (not xpassing) if they succeed. This only is true for "direct" setup/teardown invocations because teardown_class/ teardown_module cannot closely relate to a single test.

-   fix issue14: no logging errors at process exit

-   refinements to "collecting" output on non-ttys

-   refine internal plugin registration and --traceconfig output

-   introduce a mechanism to prevent/unregister plugins from the command line, see [http://pytest.org/en/stable/how-to/plugins.html#cmdunregister](http://pytest.org/en/stable/how-to/plugins.html#cmdunregister)

-   activate resultlog plugin by default

-   fix regression wrt yielded tests which due to the collection-before-running semantics were not setup as with pytest 1.3.4. Note, however, that the recommended and much cleaner way to do test parameterization remains the "pytest_generate_tests" mechanism, see the docs.

## 2.0.0 (2010-11-25)[¶](#id929 "Link to this heading")

-   pytest-2.0 is now its own package and depends on pylib-2.0

-   new ability: python -m pytest / python -m pytest.main ability

-   new python invocation: pytest.main(args, plugins) to load some custom plugins early.

-   try harder to run unittest test suites in a more compatible manner by deferring setup/teardown semantics to the unittest package. also work harder to run twisted/trial and Django tests which should now basically work by default.

-   introduce a new way to set config options via ini-style files, by default setup.cfg and tox.ini files are searched. The old ways (certain environment variables, dynamic conftest.py reading is removed).

-   add a new "-q" option which decreases verbosity and prints a more nose/unittest-style "dot" output.

-   fix issue135 - marks now work with unittest test cases as well

-   fix issue126 - introduce py.test.set_trace() to trace execution via PDB during the running of tests even if capturing is ongoing.

-   fix issue123 - new "python -m py.test" invocation for py.test (requires Python 2.5 or above)

-   fix issue124 - make reporting more resilient against tests opening files on filedescriptor 1 (stdout).

-   fix issue109 - sibling conftest.py files will not be loaded. (and Directory collectors cannot be customized anymore from a Directory's conftest.py - this needs to happen at least one level up).

-   introduce (customizable) assertion failure representations and enhance output on assertion failures for comparisons and other cases (Floris Bruynooghe)

-   nose-plugin: pass through type-signature failures in setup/teardown functions instead of not calling them (Ed Singleton)

-   remove py.test.collect.Directory (follows from a major refactoring and simplification of the collection process)

-   majorly reduce py.test core code, shift function/python testing to own plugin

-   fix issue88 (finding custom test nodes from command line arg)

-   refine 'tmpdir' creation, will now create basenames better associated with test names (thanks Ronny)

-   "xpass" (unexpected pass) tests don't cause exitcode!=0

-   fix issue131 / issue60 - importing doctests in \_\_init\_\_ files used as namespace packages

-   fix issue93 stdout/stderr is captured while importing conftest.py

-   fix bug: unittest collected functions now also can have "pytestmark" applied at class/module level

-   add ability to use "class" level for cached_setup helper

-   fix strangeness: mark.\* objects are now immutable, create new instances

## 1.3.4 (2010-09-14)[¶](#id930 "Link to this heading")

-   fix issue111: improve install documentation for windows

-   fix issue119: fix custom collectability of \_\_init\_\_.py as a module

-   fix issue116: --doctestmodules work with \_\_init\_\_.py files as well

-   fix issue115: unify internal exception passthrough/catching/GeneratorExit

-   fix issue118: new --tb=native for presenting cpython-standard exceptions

## 1.3.3 (2010-07-30)[¶](#id931 "Link to this heading")

-   fix issue113: assertion representation problem with triple-quoted strings (and possibly other cases)

-   make conftest loading detect that a conftest file with the same content was already loaded, avoids surprises in nested directory structures which can be produced e.g. by Hudson. It probably removes the need to use --confcutdir in most cases.

-   fix terminal coloring for win32 (thanks Michael Foord for reporting)

-   fix weirdness: make terminal width detection work on stdout instead of stdin (thanks Armin Ronacher for reporting)

-   remove trailing whitespace in all py/text distribution files

## 1.3.2 (2010-07-08)[¶](#id932 "Link to this heading")

**New features**

-   fix issue103: introduce py.test.raises as context manager, examples:

    ::: 
    ::: highlight
        with py.test.raises(ZeroDivisionError):
            x = 0
            1 / x

        with py.test.raises(RuntimeError) as excinfo:
            call_something()

        # you may do extra checks on excinfo.value|type|traceback here
    :::
    :::

    (thanks Ronny Pfannschmidt)

-   Funcarg factories can now dynamically apply a marker to a test invocation. This is for example useful if a factory provides parameters to a test which are expected-to-fail:

    ::: 
    ::: highlight
        def pytest_funcarg__arg(request):
            request.applymarker(py.test.mark.xfail(reason="flaky config"))
            ...

        def test_function(arg):
            ...
    :::
    :::

-   improved error reporting on collection and import errors. This makes use of a more general mechanism, namely that for custom test item/collect nodes [`node.repr_failure(excinfo)`] is now uniformly called so that you can override it to return a string error representation of your choice which is going to be reported as a (red) string.

-   introduce '--junitprefix=STR' option to prepend a prefix to all reports in the junitxml file.

**Bug fixes**

-   make tests and the [`pytest_recwarn`] plugin in particular fully compatible to Python2.7 (if you use the [`recwarn`] funcarg warnings will be enabled so that you can properly check for their existence in a cross-python manner).

-   refine --pdb: ignore xfailed tests, unify its TB-reporting and don't display failures again at the end.

-   fix assertion interpretation with the \*\* operator (thanks Benjamin Peterson)

-   fix issue105 assignment on the same line as a failing assertion (thanks Benjamin Peterson)

-   fix issue104 proper escaping for test names in junitxml plugin (thanks anonymous)

-   fix issue57 -f\|--looponfail to work with xpassing tests (thanks Ronny)

-   fix issue92 collectonly reporter and --pastebin (thanks Benjamin Peterson)

-   fix py.code.compile(source) to generate unique filenames

-   fix assertion re-interp problems on PyPy, by deferring code compilation to the (overridable) Frame.eval class. (thanks Amaury Forgeot)

-   fix py.path.local.pyimport() to work with directories

-   streamline py.path.local.mkdtemp implementation and usage

-   don't print empty lines when showing junitxml-filename

-   add optional boolean ignore_errors parameter to py.path.local.remove

-   fix terminal writing on win32/python2.4

-   py.process.cmdexec() now tries harder to return properly encoded unicode objects on all python versions

-   install plain py.test/py.which scripts also for Jython, this helps to get canonical script paths in virtualenv situations

-   make path.bestrelpath(path) return ".", note that when calling X.bestrelpath the assumption is that X is a directory.

-   make initial conftest discovery ignore "--" prefixed arguments

-   fix resultlog plugin when used in a multicpu/multihost xdist situation (thanks Jakub Gustak)

-   perform distributed testing related reporting in the xdist-plugin rather than having dist-related code in the generic py.test distribution

-   fix homedir detection on Windows

-   ship distribute_setup.py version 0.6.13

## 1.3.1 (2010-05-25)[¶](#id933 "Link to this heading")

**New features**

-   issue91: introduce new py.test.xfail(reason) helper to imperatively mark a test as expected to fail. Can be used from within setup and test functions. This is useful especially for parametrized tests when certain configurations are expected-to-fail. In this case the declarative approach with the \@py.test.mark.xfail cannot be used as it would mark all configurations as xfail.

-   issue102: introduce new --maxfail=NUM option to stop test runs after NUM failures. This is a generalization of the '-x' or '--exitfirst' option which is now equivalent to '--maxfail=1'. Both '-x' and '--maxfail' will now also print a line near the end indicating the Interruption.

-   issue89: allow py.test.mark decorators to be used on classes (class decorators were introduced with python2.6) and also allow to have multiple markers applied at class/module level by specifying a list.

-   improve and refine letter reporting in the progress bar: . pass f failed test s skipped tests (reminder: use for dependency/platform mismatch only) x xfailed test (test that was expected to fail) X xpassed test (test that was expected to fail but passed)

    You can use any combination of 'fsxX' with the '-r' extended reporting option. The xfail/xpass results will show up as skipped tests in the junitxml output - which also fixes issue99.

-   make py.test.cmdline.main() return the exitstatus instead of raising SystemExit and also allow it to be called multiple times. This of course requires that your application and tests are properly teared down and don't have global state.

**Bug Fixes**

-   improved traceback presentation: - improved and unified reporting for "--tb=short" option - Errors during test module imports are much shorter, (using --tb=short style) - raises shows shorter more relevant tracebacks - --fulltrace now more systematically makes traces longer / inhibits cutting

-   improve support for raises and other dynamically compiled code by manipulating python's linecache.cache instead of the previous rather hacky way of creating custom code objects. This makes it seamlessly work on Jython and PyPy where it previously didn't.

-   fix issue96: make capturing more resilient against Control-C interruptions (involved somewhat substantial refactoring to the underlying capturing functionality to avoid race conditions).

-   fix chaining of conditional skipif/xfail decorators - so it works now as expected to use multiple \@py.test.mark.skipif(condition) decorators, including specific reporting which of the conditions lead to skipping.

-   fix issue95: late-import zlib so that it's not required for general py.test startup.

-   fix issue94: make reporting more robust against bogus source code (and internally be more careful when presenting unexpected byte sequences)

## 1.3.0 (2010-05-05)[¶](#id934 "Link to this heading")

-   deprecate --report option in favour of a new shorter and easier to remember -r option: it takes a string argument consisting of any combination of 'xfsX' characters. They relate to the single chars you see during the dotted progress printing and will print an extra line per test at the end of the test run. This extra line indicates the exact position or test ID that you directly paste to the py.test cmdline in order to re-run a particular test.

-   allow external plugins to register new hooks via the new pytest_addhooks(pluginmanager) hook. The new release of the pytest-xdist plugin for distributed and looponfailing testing requires this feature.

-   add a new pytest_ignore_collect(path, config) hook to allow projects and plugins to define exclusion behaviour for their directory structure - for example you may define in a conftest.py this method:

    ::: 
    ::: highlight
        def pytest_ignore_collect(path):
            return path.check(link=1)
    :::
    :::

    to prevent even a collection try of any tests in symlinked dirs.

-   new pytest_pycollect_makemodule(path, parent) hook for allowing customization of the Module collection object for a matching test module.

-   extend and refine xfail mechanism: [`@py.test.mark.xfail(run=False)`] do not run the decorated test [`@py.test.mark.xfail(reason="...")`] prints the reason string in xfail summaries specifying [`--runxfail`] on command line virtually ignores xfail markers

-   expose (previously internal) commonly useful methods: py.io.get_terminal_with() -\> return terminal width py.io.ansi_print(...) -\> print colored/bold text on linux/win32 py.io.saferepr(obj) -\> return limited representation string

-   expose test outcome related exceptions as py.test.skip.Exception, py.test.raises.Exception etc., useful mostly for plugins doing special outcome interpretation/tweaking

-   (issue85) fix junitxml plugin to handle tests with non-ascii output

-   fix/refine python3 compatibility (thanks Benjamin Peterson)

-   fixes for making the jython/win32 combination work, note however: jython2.5.1/win32 does not provide a command line launcher, see [https://bugs.jython.org/issue1491](https://bugs.jython.org/issue1491) . See pylib install documentation for how to work around.

-   fixes for handling of unicode exception values and unprintable objects

-   (issue87) fix unboundlocal error in assertionold code

-   (issue86) improve documentation for looponfailing

-   refine IO capturing: stdin-redirect pseudo-file now has a NOP close() method

-   ship distribute_setup.py version 0.6.10

-   added links to the new capturelog and coverage plugins

## 1.2.0 (2010-01-18)[¶](#id935 "Link to this heading")

-   refined usage and options for "py.cleanup":

    ::: 
    ::: highlight
        py.cleanup     # remove "*.pyc" and "*$py.class" (jython) files
        py.cleanup -e .swp -e .cache # also remove files with these extensions
        py.cleanup -s  # remove "build" and "dist" directory next to setup.py files
        py.cleanup -d  # also remove empty directories
        py.cleanup -a  # synonym for "-s -d -e 'pip-log.txt'"
        py.cleanup -n  # dry run, only show what would be removed
    :::
    :::

-   add a new option "py.test --funcargs" which shows available funcargs and their help strings (docstrings on their respective factory function) for a given test path

-   display a short and concise traceback if a funcarg lookup fails

-   early-load "conftest.py" files in non-dot first-level sub directories. allows to conveniently keep and access test-related options in a [`test`] subdir and still add command line options.

-   fix issue67: new super-short traceback-printing option: "--tb=line" will print a single line for each failing (python) test indicating its filename, lineno and the failure value

-   fix issue78: always call python-level teardown functions even if the according setup failed. This includes refinements for calling setup_module/class functions which will now only be called once instead of the previous behaviour where they'd be called multiple times if they raise an exception (including a Skipped exception). Any exception will be re-corded and associated with all tests in the according module/class scope.

-   fix issue63: assume \<40 columns to be a bogus terminal width, default to 80

-   fix pdb debugging to be in the correct frame on raises-related errors

-   update apipkg.py to fix an issue where recursive imports might unnecessarily break importing

-   fix plugin links

## 1.1.1 (2009-11-24)[¶](#id936 "Link to this heading")

-   moved dist/looponfailing from py.test core into a new separately released pytest-xdist plugin.

-   new junitxml plugin: --junitxml=path will generate a junit style xml file which is processable e.g. by the Hudson CI system.

-   new option: --genscript=path will generate a standalone py.test script which will not need any libraries installed. thanks to Ralf Schmitt.

-   new option: --ignore will prevent specified path from collection. Can be specified multiple times.

-   new option: --confcutdir=dir will make py.test only consider conftest files that are relative to the specified dir.

-   new funcarg: "pytestconfig" is the pytest config object for access to command line args and can now be easily used in a test.

-   install [`py.test`] and [`py.which`] with a [`-$VERSION`] suffix to disambiguate between Python3, python2.X, Jython and PyPy installed versions.

-   new "pytestconfig" funcarg allows access to test config object

-   new "pytest_report_header" hook can return additional lines to be displayed at the header of a test run.

-   (experimental) allow "py.test path::name1::name2::..." for pointing to a test within a test collection directly. This might eventually evolve as a full substitute to "-k" specifications.

-   streamlined plugin loading: order is now as documented in customize.html: setuptools, ENV, commandline, conftest. also setuptools entry point names are turned to canonical names ("pytest\_\*")

-   automatically skip tests that need 'capfd' but have no os.dup

-   allow pytest_generate_tests to be defined in classes as well

-   deprecate usage of 'disabled' attribute in favour of pytestmark

-   deprecate definition of Directory, Module, Class and Function nodes in conftest.py files. Use pytest collect hooks instead.

-   collection/item node specific runtest/collect hooks are only called exactly on matching conftest.py files, i.e. ones which are exactly below the filesystem path of an item

-   change: the first pytest_collect_directory hook to return something will now prevent further hooks to be called.

-   change: figleaf plugin now requires --figleaf to run. Also change its long command line options to be a bit shorter (see py.test -h).

-   change: pytest doctest plugin is now enabled by default and has a new option --doctest-glob to set a pattern for file matches.

-   change: remove internal py.\_\* helper vars, only keep py.\_pydir

-   robustify capturing to survive if custom pytest_runtest_setup code failed and prevented the capturing setup code from running.

-   make py.test.\* helpers provided by default plugins visible early - works transparently both for pydoc and for interactive sessions which will regularly see e.g. py.test.mark and py.test.importorskip.

-   simplify internal plugin manager machinery

-   simplify internal collection tree by introducing a RootCollector node

-   fix assert reinterpreation that sees a call containing "keyword=..."

-   fix issue66: invoke pytest_sessionstart and pytest_sessionfinish hooks on worker nodes during dist-testing, report module/session teardown hooks correctly.

-   fix issue65: properly handle dist-testing if no execnet/py lib installed remotely.

-   skip some install-tests if no execnet is available

-   fix docs, fix internal bin/ script generation

## 1.1.0 (2009-11-05)[¶](#id937 "Link to this heading")

-   introduce automatic plugin registration via 'pytest11' entrypoints via setuptools' pkg_resources.iter_entry_points

-   fix py.test dist-testing to work with execnet \>= 1.0.0b4

-   re-introduce py.test.cmdline.main() for better backward compatibility

-   svn paths: fix a bug with path.check(versioned=True) for svn paths, allow '%' in svn paths, make svnwc.update() default to interactive mode like in 1.0.x and add svnwc.update(interactive=False) to inhibit interaction.

-   refine distributed tarball to contain test and no pyc files

-   try harder to have deprecation warnings for py.compat.\* accesses report a correct location

## 1.0.3[¶](#id938 "Link to this heading")

-   adjust and improve docs

-   remove py.rest tool and internal namespace - it was never really advertised and can still be used with the old release if needed. If there is interest it could be revived into its own tool i guess.

-   fix issue48 and issue59: raise an Error if the module from an imported test file does not seem to come from the filepath - avoids "same-name" confusion that has been reported repeatedly

-   merged Ronny's nose-compatibility hacks: now nose-style setup_module() and setup() functions are supported

-   introduce generalized py.test.mark function marking

-   reshuffle / refine command line grouping

-   deprecate parser.addgroup in favour of getgroup which creates option group

-   add --report command line option that allows to control showing of skipped/xfailed sections

-   generalized skipping: a new way to mark python functions with skipif or xfail at function, class and modules level based on platform or sys-module attributes.

-   extend py.test.mark decorator to allow for positional args

-   introduce and test "py.cleanup -d" to remove empty directories

-   fix issue #59 - robustify unittest test collection

-   make bpython/help interaction work by adding an \_\_all\_\_ attribute to ApiModule, cleanup initpkg

-   use MIT license for pylib, add some contributors

-   remove py.execnet code and substitute all usages with 'execnet' proper

-   fix issue50 - cached_setup now caches more to expectations for test functions with multiple arguments.

-   merge Jarko's fixes, issue #45 and #46

-   add the ability to specify a path for py.lookup to search in

-   fix a funcarg cached_setup bug probably only occurring in distributed testing and "module" scope with teardown.

-   many fixes and changes for making the code base python3 compatible, many thanks to Benjamin Peterson for helping with this.

-   consolidate builtins implementation to be compatible with \>=2.3, add helpers to ease keeping 2 and 3k compatible code

-   deprecate py.compat.doctest\|subprocess\|textwrap\|optparse

-   deprecate py.magic.autopath, remove py/magic directory

-   move pytest assertion handling to py/code and a pytest_assertion plugin, add "--no-assert" option, deprecate py.magic namespaces in favour of (less) py.code ones.

-   consolidate and cleanup py/code classes and files

-   cleanup py/misc, move tests to bin-for-dist

-   introduce delattr/delitem/delenv methods to py.test's monkeypatch funcarg

-   consolidate py.log implementation, remove old approach.

-   introduce py.io.TextIO and py.io.BytesIO for distinguishing between text/unicode and byte-streams (uses underlying standard lib io.\* if available)

-   make py.unittest_convert helper script available which converts "unittest.py" style files into the simpler assert/direct-test-classes py.test/nosetests style. The script was written by Laura Creighton.

-   simplified internal localpath implementation

## 1.0.2 (2009-08-27)[¶](#id939 "Link to this heading")

-   fixing packaging issues, triggered by fedora redhat packaging, also added doc, examples and contrib dirs to the tarball.

-   added a documentation link to the new django plugin.

## 1.0.1 (2009-08-19)[¶](#id940 "Link to this heading")

-   added a 'pytest_nose' plugin which handles nose.SkipTest, nose-style function/method/generator setup/teardown and tries to report functions correctly.

-   capturing of unicode writes or encoded strings to sys.stdout/err work better, also terminalwriting was adapted and somewhat unified between windows and linux.

-   improved documentation layout and content a lot

-   added a "--help-config" option to show conftest.py / ENV-var names for all longopt cmdline options, and some special conftest.py variables. renamed 'conf_capture' conftest setting to 'option_capture' accordingly.

-   fix issue #27: better reporting on non-collectable items given on commandline (e.g. pyc files)

-   fix issue #33: added --version flag (thanks Benjamin Peterson)

-   fix issue #32: adding support for "incomplete" paths to wcpath.status()

-   "Test" prefixed classes are *not* collected by default anymore if they have an \_\_init\_\_ method

-   monkeypatch setenv() now accepts a "prepend" parameter

-   improved reporting of collection error tracebacks

-   simplified multicall mechanism and plugin architecture, renamed some internal methods and argnames

## 1.0.0 (2009-08-04)[¶](#id941 "Link to this heading")

-   more terse reporting try to show filesystem path relatively to current dir

-   improve xfail output a bit

## 1.0.0b9 (2009-07-31)[¶](#b9-2009-07-31 "Link to this heading")

-   cleanly handle and report final teardown of test setup

-   fix svn-1.6 compat issue with py.path.svnwc().versioned() (thanks Wouter Vanden Hove)

-   setup/teardown or collection problems now show as ERRORs or with big "E"'s in the progress lines. they are reported and counted separately.

-   dist-testing: properly handle test items that get locally collected but cannot be collected on the remote side - often due to platform/dependency reasons

-   simplified py.test.mark API - see keyword plugin documentation

-   integrate better with logging: capturing now by default captures test functions and their immediate setup/teardown in a single stream

-   capsys and capfd funcargs now have a readouterr() and a close() method (underlyingly py.io.StdCapture/FD objects are used which grew a readouterr() method as well to return snapshots of captured out/err)

-   make assert-reinterpretation work better with comparisons not returning bools (reported with numpy from thanks maciej fijalkowski)

-   reworked per-test output capturing into the pytest_iocapture.py plugin and thus removed capturing code from config object

-   item.repr_failure(excinfo) instead of item.repr_failure(excinfo, outerr)

## 1.0.0b8 (2009-07-22)[¶](#b8-2009-07-22 "Link to this heading")

-   pytest_unittest-plugin is now enabled by default

-   introduced pytest_keyboardinterrupt hook and refined pytest_sessionfinish hooked, added tests.

-   workaround a buggy logging module interaction ("closing already closed files"). Thanks to Sridhar Ratnakumar for triggering.

-   if plugins use "py.test.importorskip" for importing a dependency only a warning will be issued instead of exiting the testing process.

-   many improvements to docs: - refined funcargs doc , use the term "factory" instead of "provider" - added a new talk/tutorial doc page - better download page - better plugin docstrings - added new plugins page and automatic doc generation script

-   fixed teardown problem related to partially failing funcarg setups (thanks MrTopf for reporting), "pytest_runtest_teardown" is now always invoked even if the "pytest_runtest_setup" failed.

-   tweaked doctest output for docstrings in py modules, thanks Radomir.

## 1.0.0b7[¶](#b7 "Link to this heading")

-   renamed py.test.xfail back to py.test.mark.xfail to avoid two ways to decorate for xfail

-   re-added py.test.mark decorator for setting keywords on functions (it was actually documented so removing it was not nice)

-   remove scope-argument from request.addfinalizer() because request.cached_setup has the scope arg. TOOWTDI.

-   perform setup finalization before reporting failures

-   apply modified patches from Andreas Kloeckner to allow test functions to have no func_code (#22) and to make "-k" and function keywords work (#20)

-   apply patch from Daniel Peolzleithner (issue #23)

-   resolve issue #18, multiprocessing.Manager() and redirection clash

-   make \_\_name\_\_ == "\_\_channelexec\_\_" for remote_exec code

## 1.0.0b3 (2009-06-19)[¶](#b3-2009-06-19 "Link to this heading")

-   plugin classes are removed: one now defines hooks directly in conftest.py or global pytest\_\*.py files.

-   added new pytest_namespace(config) hook that allows to inject helpers directly to the py.test.\* namespace.

-   documented and refined many hooks

-   added new style of generative tests via pytest_generate_tests hook that integrates well with function arguments.

## 1.0.0b1[¶](#b1 "Link to this heading")

-   introduced new "funcarg" setup method, see doc/test/funcarg.txt

-   introduced plugin architecture and many new py.test plugins, see doc/test/plugins.txt

-   teardown_method is now guaranteed to get called after a test method has run.

-   new method: py.test.importorskip(mod,minversion) will either import or call py.test.skip()

-   completely revised internal py.test architecture

-   new py.process.ForkedFunc object allowing to fork execution of a function to a sub process and getting a result back.

XXX lots of things missing here XXX

## 0.9.2[¶](#id942 "Link to this heading")

-   refined installation and metadata, created new setup.py, now based on setuptools/ez_setup (thanks to Ralf Schmitt for his support).

-   improved the way of making py.\* scripts available in windows environments, they are now added to the Scripts directory as ".cmd" files.

-   py.path.svnwc.status() now is more complete and uses xml output from the 'svn' command if available (Guido Wesdorp)

-   fix for py.path.svn\* to work with svn 1.5 (Chris Lamb)

-   fix path.relto(otherpath) method on windows to use normcase for checking if a path is relative.

-   py.test's traceback is better parseable from editors (follows the filenames:LINENO: MSG convention) (thanks to Osmo Salomaa)

-   fix to javascript-generation, "py.test --runbrowser" should work more reliably now

-   removed previously accidentally added py.test.broken and py.test.notimplemented helpers.

-   there now is a py.\_\_version\_\_ attribute

## 0.9.1[¶](#id943 "Link to this heading")

This is a fairly complete list of v0.9.1, which can serve as a reference for developers.

-   allowing + signs in py.path.svn urls \[39106\]

-   fixed support for Failed exceptions without excinfo in py.test \[39340\]

-   added support for killing processes for Windows (as well as platforms that support os.kill) in py.misc.killproc \[39655\]

-   added setup/teardown for generative tests to py.test \[40702\]

-   added detection of FAILED TO LOAD MODULE to py.test \[40703, 40738, 40739\]

-   fixed problem with calling .remove() on wcpaths of non-versioned files in py.path \[44248\]

-   fixed some import and inheritance issues in py.test \[41480, 44648, 44655\]

-   fail to run greenlet tests when pypy is available, but without stackless \[45294\]

-   small fixes in rsession tests \[45295\]

-   fixed issue with 2.5 type representations in py.test \[45483, 45484\]

-   made that internal reporting issues displaying is done atomically in py.test \[45518\]

-   made that non-existing files are ignored by the py.lookup script \[45519\]

-   improved exception name creation in py.test \[45535\]

-   made that less threads are used in execnet \[merge in 45539\]

-   removed lock required for atomic reporting issue displaying in py.test \[45545\]

-   removed globals from execnet \[45541, 45547\]

-   refactored cleanup mechanics, made that setDaemon is set to 1 to make atexit get called in 2.5 (py.execnet) \[45548\]

-   fixed bug in joining threads in py.execnet's servemain \[45549\]

-   refactored py.test.rsession tests to not rely on exact output format anymore \[45646\]

-   using repr() on test outcome \[45647\]

-   added 'Reason' classes for py.test.skip() \[45648, 45649\]

-   killed some unnecessary sanity check in py.test.collect \[45655\]

-   avoid using os.tmpfile() in py.io.fdcapture because on Windows it's only usable by Administrators \[45901\]

-   added support for locking and non-recursive commits to py.path.svnwc \[45994\]

-   locking files in py.execnet to prevent CPython from segfaulting \[46010\]

-   added export() method to py.path.svnurl

-   fixed -d -x in py.test \[47277\]

-   fixed argument concatenation problem in py.path.svnwc \[49423\]

-   restore py.test behaviour that it exits with code 1 when there are failures \[49974\]

-   don't fail on html files that don't have an accompanying .txt file \[50606\]

-   fixed 'utestconvert.py \< input' \[50645\]

-   small fix for code indentation in py.code.source \[50755\]

-   fix \_docgen.py documentation building \[51285\]

-   improved checks for source representation of code blocks in py.test \[51292\]

-   added support for passing authentication to py.path.svn\* objects \[52000, 52001\]

-   removed sorted() call for py.apigen tests in favour of \[\].sort() to support Python 2.3 \[52481\]