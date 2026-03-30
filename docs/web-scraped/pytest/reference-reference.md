# Source: https://docs.pytest.org/en/stable/reference/reference.html

[]

# API Reference[¶](#api-reference "Link to this heading")

This page contains the full reference to pytest's API.

## Constants[¶](#constants "Link to this heading")

### pytest.\_\_version\_\_[¶](#pytest-version "Link to this heading")

The current pytest version, as a string:

    >>> import pytest
    >>> pytest.__version__
    '7.0.0'

[]

### pytest.HIDDEN_PARAM[¶](#pytest-hidden-param "Link to this heading")

[Added in version 8.4.]

Can be passed to [`ids`] of [[`Metafunc.parametrize`]](#pytest.Metafunc.parametrize "pytest.Metafunc.parametrize") or to [`id`] of [[`pytest.param()`]](#pytest.param "pytest.param") to hide a parameter set from the test name. Can only be used at most 1 time, as test names need to be unique.

[]

### pytest.version_tuple[¶](#pytest-version-tuple "Link to this heading")

[Added in version 7.0.]

The current pytest version, as a tuple:

    >>> import pytest
    >>> pytest.version_tuple
    (7, 0, 0)

For pre-releases, the last component will be a string with the prerelease version:

    >>> import pytest
    >>> pytest.version_tuple
    (7, 0, '0rc1')

## Functions[¶](#functions "Link to this heading")

### pytest.approx[¶](#pytest-approx "Link to this heading")

[[approx]][(]*[[expected]]*, *[[rel]][[=]][[None]]*, *[[abs]][[=]][[None]]*, *[[nan_ok]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/python_api.html#approx)[¶](#pytest.approx "Link to this definition")

:   Assert that two numbers (or two ordered sequences of numbers) are equal to each other within some tolerance.

    Due to the [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html "(in Python v3.14)"), numbers that we would intuitively expect to be equal are not always so:

    ::: 
    ::: highlight
        >>> 0.1 + 0.2 == 0.3
        False
    :::
    :::

    This problem is commonly encountered when writing tests, e.g. when making sure that floating-point values are what you expect them to be. One way to deal with this problem is to assert that two floating-point numbers are equal to within some appropriate tolerance:

    ::: 
    ::: highlight
        >>> abs((0.1 + 0.2) - 0.3) < 1e-6
        True
    :::
    :::

    However, comparisons like this are tedious to write and difficult to understand. Furthermore, absolute comparisons like the one above are usually discouraged because there's no tolerance that works well for all situations. [`1e-6`] is good for numbers around [`1`], but too small for very big numbers and too big for very small ones. It's better to express the tolerance as a fraction of the expected value, but relative comparisons like that are even more difficult to write correctly and concisely.

    The [`approx`] class performs floating-point comparisons using a syntax that's as intuitive as possible:

    ::: 
    ::: highlight
        >>> from pytest import approx
        >>> 0.1 + 0.2 == approx(0.3)
        True
    :::
    :::

    The same syntax also works for ordered sequences of numbers:

    ::: 
    ::: highlight
        >>> (0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6))
        True
    :::
    :::

    [`numpy`] arrays:

    ::: 
    ::: highlight
        >>> import numpy as np
        >>> np.array([0.1, 0.2]) + np.array([0.2, 0.4]) == approx(np.array([0.3, 0.6]))
        True
    :::
    :::

    And for a [`numpy`] array against a scalar:

    ::: 
    ::: highlight
        >>> import numpy as np
        >>> np.array([0.1, 0.2]) + np.array([0.2, 0.1]) == approx(0.3)
        True
    :::
    :::

    Only ordered sequences are supported, because [`approx`] needs to infer the relative position of the sequences without ambiguity. This means [`sets`] and other unordered sequences are not supported.

    Finally, dictionary *values* can also be compared:

    ::: 
    ::: highlight
        >>>  == approx()
        True
    :::
    :::

    The comparison will be true if both mappings have the same keys and their respective values match the expected tolerances.

    **Tolerances**

    By default, [`approx`] considers numbers within a relative tolerance of [`1e-6`] (i.e. one part in a million) of its expected value to be equal. This treatment would lead to surprising results if the expected value was [`0.0`], because nothing but [`0.0`] itself is relatively close to [`0.0`]. To handle this case less surprisingly, [`approx`] also considers numbers within an absolute tolerance of [`1e-12`] of its expected value to be equal. Infinity and NaN are special cases. Infinity is only considered equal to itself, regardless of the relative tolerance. NaN is not considered equal to anything by default, but you can make it be equal to itself by setting the [`nan_ok`] argument to True. (This is meant to facilitate comparing arrays that use NaN to mean "no data".)

    Both the relative and absolute tolerances can be changed by passing arguments to the [`approx`] constructor:

    ::: 
    ::: highlight
        >>> 1.0001 == approx(1)
        False
        >>> 1.0001 == approx(1, rel=1e-3)
        True
        >>> 1.0001 == approx(1, abs=1e-3)
        True
    :::
    :::

    If you specify [`abs`] but not [`rel`], the comparison will not consider the relative tolerance at all. In other words, two numbers that are within the default relative tolerance of [`1e-6`] will still be considered unequal if they exceed the specified absolute tolerance. If you specify both [`abs`] and [`rel`], the numbers will be considered equal if either tolerance is met:

    ::: 
    ::: highlight
        >>> 1 + 1e-8 == approx(1)
        True
        >>> 1 + 1e-8 == approx(1, abs=1e-12)
        False
        >>> 1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12)
        True
    :::
    :::

    **Non-numeric types**

    You can also use [`approx`] to compare non-numeric types, or dicts and sequences containing non-numeric types, in which case it falls back to strict equality. This can be useful for comparing dicts and sequences that can contain optional values:

    ::: 
    ::: highlight
        >>>  == approx()
        True
        >>> [None, 1.0000005] == approx([None,1])
        True
        >>> ["foo", 1.0000005] == approx([None,1])
        False
    :::
    :::

    If you're thinking about using [`approx`], then you might want to know how it compares to other good ways of comparing floating-point numbers. All of these algorithms are based on relative and absolute tolerances and should agree for the most part, but they do have meaningful differences:

    -   [`math.isclose(a,`]` `[`b,`]` `[`rel_tol=1e-9,`]` `[`abs_tol=0.0)`]: True if the relative tolerance is met w.r.t. either [`a`] or [`b`] or if the absolute tolerance is met. Because the relative tolerance is calculated w.r.t. both [`a`] and [`b`], this test is symmetric (i.e. neither [`a`] nor [`b`] is a "reference value"). You have to specify an absolute tolerance if you want to compare to [`0.0`] because there is no tolerance by default. More information: [[`math.isclose()`]](https://docs.python.org/3/library/math.html#math.isclose "(in Python v3.14)").

    -   [`numpy.isclose(a,`]` `[`b,`]` `[`rtol=1e-5,`]` `[`atol=1e-8)`]: True if the difference between [`a`] and [`b`] is less that the sum of the relative tolerance w.r.t. [`b`] and the absolute tolerance. Because the relative tolerance is only calculated w.r.t. [`b`], this test is asymmetric and you can think of [`b`] as the reference value. Support for comparing sequences is provided by [[`numpy.allclose()`]](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "(in NumPy v2.3)"). More information: [numpy.isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html "(in NumPy v2.3)").

    -   [`unittest.TestCase.assertAlmostEqual(a,`]` `[`b)`]: True if [`a`] and [`b`] are within an absolute tolerance of [`1e-7`]. No relative tolerance is considered , so this function is not appropriate for very large or very small numbers. Also, it's only available in subclasses of [`unittest.TestCase`] and it's ugly because it doesn't follow PEP8. More information: [[`unittest.TestCase.assertAlmostEqual()`]](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "(in Python v3.14)").

    -   [`a`]` `[`==`]` `[`pytest.approx(b,`]` `[`rel=1e-6,`]` `[`abs=1e-12)`]: True if the relative tolerance is met w.r.t. [`b`] or if the absolute tolerance is met. Because the relative tolerance is only calculated w.r.t. [`b`], this test is asymmetric and you can think of [`b`] as the reference value. In the special case that you explicitly specify an absolute tolerance but not a relative tolerance, only the absolute tolerance is considered.

    ::: 
    Note

    [`approx`] can handle numpy arrays, but we recommend the specialised test helpers in [Test support](https://numpy.org/doc/stable/reference/routines.testing.html "(in NumPy v2.3)") if you need support for comparisons, NaNs, or ULP-based tolerances.

    To match strings using regex, you can use [Matches](https://github.com/asottile/re-assert#re_assertmatchespattern-str-args-kwargs) from the [re_assert package](https://github.com/asottile/re-assert).
    :::

    ::: 
    Note

    Unlike built-in equality, this function considers booleans unequal to numeric zero or one. For example:

    ::: 
    ::: highlight
        >>> 1 == approx(True)
        False
    :::
    :::
    :::

    ::: 
    Warning

    ::: versionchanged
    [Changed in version 3.2.]
    :::

    In order to avoid inconsistent behavior, [[`TypeError`]](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)") is raised for [`>`], [`>=`], [`<`] and [`<=`] comparisons. The example below illustrates the problem:

    ::: 
    ::: highlight
        assert approx(0.1) > 0.1 + 1e-10  # calls approx(0.1).__gt__(0.1 + 1e-10)
        assert 0.1 + 1e-10 > approx(0.1)  # calls approx(0.1).__lt__(0.1 + 1e-10)
    :::
    :::

    In the second example one expects [`approx(0.1).__le__(0.1`]` `[`+`]` `[`1e-10)`] to be called. But instead, [`approx(0.1).__lt__(0.1`]` `[`+`]` `[`1e-10)`] is used to comparison. This is because the call hierarchy of rich comparisons follows a fixed behavior. More information: [[`object.__ge__()`]](https://docs.python.org/3/reference/datamodel.html#object.__ge__ "(in Python v3.14)")
    :::

    ::: versionchanged
    [Changed in version 3.7.1: ][`approx`] raises [`TypeError`] when it encounters a dict value or sequence element of non-numeric type.
    :::

    ::: versionchanged
    [Changed in version 6.1.0: ][`approx`] falls back to strict equality for non-numeric types instead of raising [`TypeError`].
    :::

### pytest.fail[¶](#pytest-fail "Link to this heading")

**Tutorial**: [[How to use skip and xfail to deal with tests that cannot succeed]](../how-to/skipping.html#skipping)

[[fail]][(]*[[reason]]*[\[], *[[pytrace=True]]*[\]][)][¶](#pytest.fail "Link to this definition")

:   Explicitly fail an executing test with the given message.

    Parameters[:]

    :   -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The message to show the user as reason for the failure.

        -   **pytrace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If False, msg represents the full failure information and no python traceback will be reported.

    Raises[:]

    :   [**pytest.fail.Exception**](#pytest.fail.Exception "pytest.fail.Exception") -- The exception that is raised.

```
<!-- -->
```

*[[class]][ ]*[[pytest.fail.]][[Exception]][¶](#pytest.fail.Exception "Link to this definition")

:   The exception raised by [[`pytest.fail()`]](#pytest.fail "pytest.fail").

### pytest.skip[¶](#pytest-skip "Link to this heading")

[[skip]][(]*[[reason]]*[\[], *[[allow_module_level=False]]*[\]][)][¶](#pytest.skip "Link to this definition")

:   Skip an executing test with the given message.

    This function should be called only during testing (setup, call or teardown) or during collection by using the [`allow_module_level`] flag. This function can be called in doctests as well.

    Parameters[:]

    :   -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The message to show the user as reason for the skip.

        -   **allow_module_level** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) --

            Allows this function to be called at module level. Raising the skip exception at module level will stop the execution of the module and prevent the collection of all tests in the module, even those defined before the [`skip`] call.

            Defaults to False.

    Raises[:]

    :   [**pytest.skip.Exception**](#pytest.skip.Exception "pytest.skip.Exception") -- The exception that is raised.

    ::: 
    Note

    It is better to use the [[pytest.mark.skipif]](#pytest-mark-skipif-ref) marker when possible to declare a test to be skipped under certain conditions like mismatching platforms or dependencies. Similarly, use the [`#`]` `[`doctest:`]` `[`+SKIP`] directive (see [[`doctest.SKIP`]](https://docs.python.org/3/library/doctest.html#doctest.SKIP "(in Python v3.14)")) to skip a doctest statically.
    :::

```
<!-- -->
```

*[[class]][ ]*[[pytest.skip.]][[Exception]][¶](#pytest.skip.Exception "Link to this definition")

:   The exception raised by [[`pytest.skip()`]](#pytest.skip "pytest.skip").

[]

### pytest.importorskip[¶](#pytest-importorskip "Link to this heading")

[[importorskip]][(]*[[modname]]*, *[[minversion]][[=]][[None]]*, *[[reason]][[=]][[None]]*, *[[\*]]*, *[[exc_type]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/outcomes.html#importorskip)[¶](#pytest.importorskip "Link to this definition")

:   Import and return the requested module [`modname`], or skip the current test if the module cannot be imported.

    Parameters[:]

    :   -   **modname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The name of the module to import.

        -   **minversion** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- If given, the imported module's [`__version__`] attribute must be at least this minimal version, otherwise the test is still skipped.

        -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- If given, this reason is shown as the message when the module cannot be imported.

        -   **exc_type** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[*[*ImportError*](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)")*\]* *\|* *None*) --

            The exception that should be captured in order to skip modules. Must be [[`ImportError`]](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)") or a subclass.

            If the module can be imported but raises [[`ImportError`]](https://docs.python.org/3/library/exceptions.html#ImportError "(in Python v3.14)"), pytest will issue a warning to the user, as often users expect the module not to be found (which would raise [[`ModuleNotFoundError`]](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "(in Python v3.14)") instead).

            This warning can be suppressed by passing [`exc_type=ImportError`] explicitly.

            See [[pytest.importorskip default behavior regarding ImportError]](../deprecations.html#import-or-skip-import-error) for details.

    Returns[:]

    :   The imported module. This should be assigned to its canonical name.

    Raises[:]

    :   [**pytest.skip.Exception**](#pytest.skip.Exception "pytest.skip.Exception") -- If the module cannot be imported.

    Return type[:]

    :   [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")

    Example:

    ::: 
    ::: highlight
        docutils = pytest.importorskip("docutils")
    :::
    :::

    ::: versionadded
    [Added in version 8.2: ]The [`exc_type`] parameter.
    :::

### pytest.xfail[¶](#pytest-xfail "Link to this heading")

[[xfail]][(]*[[reason]][[=]][[\'\']]*[)][¶](#pytest.xfail "Link to this definition")

:   Imperatively xfail an executing test or setup function with the given reason.

    This function should be called only during testing (setup, call or teardown).

    No other code is executed after using [`xfail()`] (it is implemented internally by raising an exception).

    Parameters[:]

    :   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The message to show the user as reason for the xfail.

    ::: 
    Note

    It is better to use the [[pytest.mark.xfail]](#pytest-mark-xfail-ref) marker when possible to declare a test to be xfailed under certain conditions like known bugs or missing features.
    :::

    Raises[:]

    :   [**pytest.xfail.Exception**](#pytest.xfail.Exception "pytest.xfail.Exception") -- The exception that is raised.

```
<!-- -->
```

*[[class]][ ]*[[pytest.xfail.]][[Exception]][¶](#pytest.xfail.Exception "Link to this definition")

:   The exception raised by [[`pytest.xfail()`]](#pytest.xfail "pytest.xfail").

### pytest.exit[¶](#pytest-exit "Link to this heading")

[[exit]][(]*[[reason]]*[\[], *[[returncode=None]]*[\]][)][¶](#pytest.exit "Link to this definition")

:   Exit testing process.

    Parameters[:]

    :   -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The message to show as the reason for exiting pytest. reason has a default value only because [`msg`] is deprecated.

        -   **returncode** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* *None*) -- Return code to be used when exiting pytest. None means the same as [`0`] (no error), same as [[`sys.exit()`]](https://docs.python.org/3/library/sys.html#sys.exit "(in Python v3.14)").

    Raises[:]

    :   [**pytest.exit.Exception**](#pytest.exit.Exception "pytest.exit.Exception") -- The exception that is raised.

```
<!-- -->
```

*[[class]][ ]*[[pytest.exit.]][[Exception]][¶](#pytest.exit.Exception "Link to this definition")

:   The exception raised by [[`pytest.exit()`]](#pytest.exit "pytest.exit").

### pytest.main[¶](#pytest-main "Link to this heading")

**Tutorial**: [[Calling pytest from Python code]](../how-to/usage.html#pytest-main-usage)

[[main]][(]*[[args]][[=]][[None]]*, *[[plugins]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#main)[¶](#pytest.main "Link to this definition")

:   Perform an in-process test run.

    Parameters[:]

    :   -   **args** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) -- List of command line arguments. If [`None`] or not given, defaults to reading arguments directly from the process command line ([[`sys.argv`]](https://docs.python.org/3/library/sys.html#sys.argv "(in Python v3.14)")).

        -   **plugins** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")*\]* *\|* *None*) -- List of plugin objects to be auto-registered during initialization.

    Returns[:]

    :   An exit code.

    Return type[:]

    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") \| [*ExitCode*](#pytest.ExitCode "pytest.ExitCode")

### pytest.param[¶](#pytest-param "Link to this heading")

[[param]][(]*[[\*values]]*[\[], *[[id]]*[\]][\[], *[[marks]]*[\]][)][[[\[source\]]]](../_modules/_pytest/mark.html#param)[¶](#pytest.param "Link to this definition")

:   Specify a parameter in [pytest.mark.parametrize](#pytest-mark-parametrize) calls or [[parametrized fixtures]](../how-to/fixtures.html#fixture-parametrize-marks).

    ::: 
    ::: highlight
        @pytest.mark.parametrize(
            "test_input,expected",
            [
                ("3+5", 8),
                pytest.param("6*9", 42, marks=pytest.mark.xfail),
            ],
        )
        def test_eval(test_input, expected):
            assert eval(test_input) == expected
    :::
    :::

    Parameters[:]

    :   -   **values** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- Variable args of the values of the parameter set, in order.

        -   **marks** ([*MarkDecorator*](#pytest.MarkDecorator "_pytest.mark.structures.MarkDecorator") *\|* [*Collection*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.14)")*\[*[*MarkDecorator*](#pytest.MarkDecorator "_pytest.mark.structures.MarkDecorator") *\|* [*Mark*](#pytest.Mark "_pytest.mark.structures.Mark")*\]*) --

            A single mark or a list of marks to be applied to this parameter set.

            [[pytest.mark.usefixtures]](#pytest-mark-usefixtures-ref) cannot be added via this parameter.

        -   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *Literal\[pytest.HIDDEN_PARAM\]* *\|* *None*) --

            The id to attribute to this parameter set.

            ::: versionadded
            [Added in version 8.4: ][[pytest.HIDDEN_PARAM]](#hidden-param) means to hide the parameter set from the test name. Can only be used at most 1 time, as test names need to be unique.
            :::

### pytest.raises[¶](#pytest-raises "Link to this heading")

**Tutorial**: [[Assertions about approximate equality]](../how-to/assert.html#assertraises)

*[with]* [[raises]][(]*[[expected_exception]][[:]][ ][[[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][E][[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][E][[\]]][[,]][ ][[\...]][[\]]]]*, *[[\*]]*, *[[match]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Pattern]](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[\...]]*, *[[check]][[:]][ ][[Callable][[\[]][[\[]][E][[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\...]]*[)] [[→] [[[RaisesExc]](#pytest.RaisesExc "pytest.RaisesExc")[[\[]][E][[\]]]]]*[ as] [excinfo]*[[[\[source\]]]](../_modules/_pytest/raises.html#raises)[¶](#pytest.raises "Link to this definition")\
*[with]* [[raises]][(]*[[\*]]*, *[[match]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Pattern]](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]*, *[[check]][[:]][ ][[Callable][[\[]][[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\...]]*[)] [[→] [[[RaisesExc]](#pytest.RaisesExc "_pytest.raises.RaisesExc")[[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]]]]*[ as] [excinfo]*\
*[with]* [[raises]][(]*[[\*]]*, *[[check]][[:]][ ][[Callable][[\[]][[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]]]*[)] [[→] [[[RaisesExc]](#pytest.RaisesExc "_pytest.raises.RaisesExc")[[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]]]]*[ as] [excinfo]*\
*[with]* [[raises]][(]*[[expected_exception]][[:]][ ][[[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][E][[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][E][[\]]][[,]][ ][[\...]][[\]]]]*, *[[func]][[:]][ ][[Callable][[\[]][[\...]][[,]][ ][Any][[\]]]]*, *[[\*]][[args]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[\*\*]][[kwargs]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*[)] [[→] [[[ExceptionInfo]](#pytest.ExceptionInfo "pytest.ExceptionInfo")[[\[]][E][[\]]]]]*[ as] [excinfo]*

:   Assert that a code block/function call raises an exception type, or one of its subclasses.

    Parameters[:]

    :   -   **expected_exception** --

            The expected exception type, or a tuple if one of multiple possible exception types are expected. Note that subclasses of the passed exceptions will also match.

            This is not a required parameter, you may opt to only use [`match`] and/or [`check`] for verifying the raised exception.

        -   **match** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*re.Pattern*](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) --

            If specified, a string containing a regular expression, or a regular expression object, that is tested against the string representation of the exception and its [][**PEP 678**](https://peps.python.org/pep-0678/) [`__notes__`] using [[`re.search()`]](https://docs.python.org/3/library/re.html#re.search "(in Python v3.14)").

            To match a literal string that may contain [[special characters]](https://docs.python.org/3/library/re.html#re-syntax "(in Python v3.14)"), the pattern can first be escaped with [[`re.escape()`]](https://docs.python.org/3/library/re.html#re.escape "(in Python v3.14)").

            (This is only used when [`pytest.raises`] is used as a context manager, and passed through to the function otherwise. When using [`pytest.raises`] as a function, you can use: [`pytest.raises(Exc,`]` `[`func,`]` `[`match="passed`]` `[`on").match("my`]` `[`pattern")`].)

        -   **check** (*Callable\[\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\],* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*\]*) --

            ::: versionadded
            [Added in version 8.4.]
            :::

            If specified, a callable that will be called with the exception as a parameter after checking the type and the match regex if specified. If it returns [`True`] it will be considered a match, if not it will be considered a failed match.

    Use [`pytest.raises`] as a context manager, which will capture the exception of the given type, or any of its subclasses:

    ::: 
    ::: highlight
        >>> import pytest
        >>> with pytest.raises(ZeroDivisionError):
        ...    1/0
    :::
    :::

    If the code block does not raise the expected exception ([[`ZeroDivisionError`]](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "(in Python v3.14)") in the example above), or no exception at all, the check will fail instead.

    You can also use the keyword argument [`match`] to assert that the exception matches a text or regex:

    ::: 
    ::: highlight
        >>> with pytest.raises(ValueError, match='must be 0 or None'):
        ...     raise ValueError("value must be 0 or None")

        >>> with pytest.raises(ValueError, match=r'must be \d+$'):
        ...     raise ValueError("value must be 42")
    :::
    :::

    The [`match`] argument searches the formatted exception string, which includes any [PEP-678](https://peps.python.org/pep-0678/) [`__notes__`]:

    ::: 
    ::: highlight
        >>> with pytest.raises(ValueError, match=r"had a note added"):
        ...     e = ValueError("value must be 42")
        ...     e.add_note("had a note added")
        ...     raise e
    :::
    :::

    The [`check`] argument, if provided, must return True when passed the raised exception for the match to be successful, otherwise an [[`AssertionError`]](https://docs.python.org/3/library/exceptions.html#AssertionError "(in Python v3.14)") is raised.

    ::: 
    ::: highlight
        >>> import errno
        >>> with pytest.raises(OSError, check=lambda e: e.errno == errno.EACCES):
        ...     raise OSError(errno.EACCES, "no permission to view")
    :::
    :::

    The context manager produces an [[`ExceptionInfo`]](#pytest.ExceptionInfo "pytest.ExceptionInfo") object which can be used to inspect the details of the captured exception:

    ::: 
    ::: highlight
        >>> with pytest.raises(ValueError) as exc_info:
        ...     raise ValueError("value must be 42")
        >>> assert exc_info.type is ValueError
        >>> assert exc_info.value.args[0] == "value must be 42"
    :::
    :::

    ::: 
    Warning

    Given that [`pytest.raises`] matches subclasses, be wary of using it to match [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") like this:

    ::: 
    ::: highlight
        # Careful, this will catch ANY exception raised.
        with pytest.raises(Exception):
            some_function()
    :::
    :::

    Because [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") is the base class of almost all exceptions, it is easy for this to hide real bugs, where the user wrote this expecting a specific exception, but some other exception is being raised due to a bug introduced during a refactoring.

    Avoid using [`pytest.raises`] to catch [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") unless certain that you really want to catch **any** exception raised.
    :::

    ::: 
    Note

    When using [`pytest.raises`] as a context manager, it's worthwhile to note that normal context manager rules apply and that the exception raised *must* be the final line in the scope of the context manager. Lines of code after that, within the scope of the context manager will not be executed. For example:

    ::: 
    ::: highlight
        >>> value = 15
        >>> with pytest.raises(ValueError) as exc_info:
        ...     if value > 10:
        ...         raise ValueError("value must be <= 10")
        ...     assert exc_info.type is ValueError  # This will not execute.
    :::
    :::

    Instead, the following approach must be taken (note the difference in scope):

    ::: 
    ::: highlight
        >>> with pytest.raises(ValueError) as exc_info:
        ...     if value > 10:
        ...         raise ValueError("value must be <= 10")
        ...
        >>> assert exc_info.type is ValueError
    :::
    :::
    :::

    **Expecting exception groups**

    When expecting exceptions wrapped in [[`BaseExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "(in Python v3.14)") or [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)"), you should instead use [[`pytest.RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup").

    **Using with** [`pytest.mark.parametrize`]

    When using [[pytest.mark.parametrize]](#pytest-mark-parametrize-ref) it is possible to parametrize tests such that some runs raise an exception and others do not.

    See [[Parametrizing conditional raising]](../example/parametrize.html#parametrizing-conditional-raising) for an example.

    ::: 
    See also

    [[Assertions about approximate equality]](../how-to/assert.html#assertraises) for more examples and detailed discussion.
    :::

    **Legacy form**

    It is possible to specify a callable by passing a to-be-called lambda:

    ::: 
    ::: highlight
        >>> raises(ZeroDivisionError, lambda: 1/0)
        <ExceptionInfo ...>
    :::
    :::

    or you can specify an arbitrary callable with arguments:

    ::: 
    ::: highlight
        >>> def f(x): return 1/x
        ...
        >>> raises(ZeroDivisionError, f, 0)
        <ExceptionInfo ...>
        >>> raises(ZeroDivisionError, f, x=0)
        <ExceptionInfo ...>
    :::
    :::

    The form above is fully supported but discouraged for new code because the context manager form is regarded as more readable and less error-prone.

    ::: 
    Note

    Similar to caught exception objects in Python, explicitly clearing local references to returned [`ExceptionInfo`] objects can help the Python interpreter speed up its garbage collection.

    Clearing those references breaks a reference cycle ([`ExceptionInfo`] --\> caught exception --\> frame stack raising the exception --\> current frame stack --\> local variables --\> [`ExceptionInfo`]) which makes Python keep all objects referenced from that cycle (including all local variables in the current frame) alive until the next cyclic garbage collection run. More detailed information can be found in the official Python documentation for [[the try statement]](https://docs.python.org/3/reference/compound_stmts.html#try "(in Python v3.14)").
    :::

### pytest.deprecated_call[¶](#pytest-deprecated-call "Link to this heading")

**Tutorial**: [[Ensuring code triggers a deprecation warning]](../how-to/capture-warnings.html#ensuring-function-triggers)

*[with]* [[deprecated_call]][(]*[[\*]]*, *[[match]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Pattern]](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[\...]]*[)] [[→] [[[WarningsRecorder]](#pytest.WarningsRecorder "_pytest.recwarn.WarningsRecorder")]][[[\[source\]]]](../_modules/_pytest/recwarn.html#deprecated_call)[¶](#pytest.deprecated_call "Link to this definition")\
*[with]* [[deprecated_call]][(]*[[func]][[:]][ ][[[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[\...]][[\]]][[,]][ ][T][[\]]]]*, *[[\*]][[args]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[\*\*]][[kwargs]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*[)] [[→] [[T]]]

:   Assert that code produces a [`DeprecationWarning`] or [`PendingDeprecationWarning`] or [`FutureWarning`].

    This function can be used as a context manager:

    ::: 
    ::: highlight
        >>> import warnings
        >>> def api_call_v2():
        ...     warnings.warn('use v3 of this api', DeprecationWarning)
        ...     return 200

        >>> import pytest
        >>> with pytest.deprecated_call():
        ...    assert api_call_v2() == 200
    :::
    :::

    It can also be used by passing a function and [`*args`] and [`**kwargs`], in which case it will ensure calling [`func(*args,`]` `[`**kwargs)`] produces one of the warnings types above. The return value is the return value of the function.

    In the context manager form you may use the keyword argument [`match`] to assert that the warning matches a text or regex.

    The context manager produces a list of [`warnings.WarningMessage`] objects, one for each warning raised.

### pytest.register_assert_rewrite[¶](#pytest-register-assert-rewrite "Link to this heading")

**Tutorial**: [[Assertion Rewriting]](../how-to/writing_plugins.html#assertion-rewriting)

[[register_assert_rewrite]][(]*[[\*]][[names]]*[)][[[\[source\]]]](../_modules/_pytest/assertion.html#register_assert_rewrite)[¶](#pytest.register_assert_rewrite "Link to this definition")

:   Register one or more module names to be rewritten on import.

    This function will make sure that this module or all modules inside the package will get their assert statements rewritten. Thus you should make sure to call this before the module is actually imported, usually in your \_\_init\_\_.py if you are a plugin using a package.

    Parameters[:]

    :   **names** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The module names to register.

### pytest.warns[¶](#pytest-warns "Link to this heading")

**Tutorial**: [[Asserting warnings with the warns function]](../how-to/capture-warnings.html#assertwarnings)

*[with]* [[warns]][(]*[expected_warning:] [type\[Warning\]] [\|] [tuple\[type\[Warning\],] [\...\]] [=] [\<class] [\'Warning\'\>,] [\*,] [match:] [str] [\|] [\~re.Pattern\[str\]] [\|] [None] [=] [None]*[)] [[→] [[WarningsChecker]]][[[\[source\]]]](../_modules/_pytest/recwarn.html#warns)[¶](#pytest.warns "Link to this definition")\
*[with]* [[warns]][(]*[[expected_warning]][[:]][ ][[[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][[Warning]](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)")[[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][[Warning]](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)")[[\]]][[,]][ ][[\...]][[\]]]]*, *[[func]][[:]][ ][[[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[\...]][[\]]][[,]][ ][T][[\]]]]*, *[[\*]][[args]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[\*\*]][[kwargs]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*[)] [[→] [[T]]]

:   Assert that code raises a particular class of warning.

    Specifically, the parameter [`expected_warning`] can be a warning class or tuple of warning classes, and the code inside the [`with`] block must issue at least one warning of that class or classes.

    This helper produces a list of [`warnings.WarningMessage`] objects, one for each warning emitted (regardless of whether it is an [`expected_warning`] or not). Since pytest 8.0, unmatched warnings are also re-emitted when the context closes.

    This function can be used as a context manager:

    ::: 
    ::: highlight
        >>> import pytest
        >>> with pytest.warns(RuntimeWarning):
        ...    warnings.warn("my warning", RuntimeWarning)
    :::
    :::

    In the context manager form you may use the keyword argument [`match`] to assert that the warning matches a text or regex:

    ::: 
    ::: highlight
        >>> with pytest.warns(UserWarning, match='must be 0 or None'):
        ...     warnings.warn("value must be 0 or None", UserWarning)

        >>> with pytest.warns(UserWarning, match=r'must be \d+$'):
        ...     warnings.warn("value must be 42", UserWarning)

        >>> with pytest.warns(UserWarning):  # catch re-emitted warning
        ...     with pytest.warns(UserWarning, match=r'must be \d+$'):
        ...         warnings.warn("this is not here", UserWarning)
        Traceback (most recent call last):
          ...
        Failed: DID NOT WARN. No warnings of type ...UserWarning... were emitted...
    :::
    :::

    **Using with** [`pytest.mark.parametrize`]

    When using [[pytest.mark.parametrize]](#pytest-mark-parametrize-ref) it is possible to parametrize tests such that some runs raise a warning and others do not.

    This could be achieved in the same way as with exceptions, see [[Parametrizing conditional raising]](../example/parametrize.html#parametrizing-conditional-raising) for an example.

### pytest.freeze_includes[¶](#pytest-freeze-includes "Link to this heading")

**Tutorial**: [[Freezing pytest]](../example/simple.html#freezing-pytest)

[[freeze_includes]][(][)][[[\[source\]]]](../_modules/_pytest/freeze_support.html#freeze_includes)[¶](#pytest.freeze_includes "Link to this definition")

:   Return a list of module names used by pytest that should be included by cx_freeze.

[]

## Marks[¶](#marks "Link to this heading")

Marks can be used to apply metadata to *test functions* (but not fixtures), which can then be accessed by fixtures or plugins.

[]

### pytest.mark.filterwarnings[¶](#pytest-mark-filterwarnings "Link to this heading")

**Tutorial**: [[\@pytest.mark.filterwarnings]](../how-to/capture-warnings.html#filterwarnings)

Add warning filters to marked test items.

[[pytest.mark.]][[filterwarnings]][(]*[[filter]]*[)][¶](#pytest.mark.filterwarnings "Link to this definition")

:   

    Parameters[:]

    :   **filter** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) --

        A *warning specification string*, which is composed of contents of the tuple [`(action,`]` `[`message,`]` `[`category,`]` `[`module,`]` `[`lineno)`] as specified in [The Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter "(in Python v3.14)") section of the Python documentation, separated by [`":"`]. Optional fields can be omitted. Module names passed for filtering are not regex-escaped.

        For example:

        ::: 
        ::: highlight
            @pytest.mark.filterwarnings("ignore:.*usage will be deprecated.*:DeprecationWarning")
            def test_foo(): ...
        :::
        :::

[]

### pytest.mark.parametrize[¶](#pytest-mark-parametrize "Link to this heading")

**Tutorial**: [[How to parametrize fixtures and test functions]](../how-to/parametrize.html#parametrize)

This mark has the same signature as [[`pytest.Metafunc.parametrize()`]](#pytest.Metafunc.parametrize "pytest.Metafunc.parametrize"); see there.

[]

### pytest.mark.skip[¶](#pytest-mark-skip "Link to this heading")

**Tutorial**: [[Skipping test functions]](../how-to/skipping.html#skip)

Unconditionally skip a test function.

[[pytest.mark.]][[skip]][(]*[[reason]][[=]][[None]]*[)][¶](#pytest.mark.skip "Link to this definition")

:   

    Parameters[:]

    :   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Reason why the test function is being skipped.

[]

### pytest.mark.skipif[¶](#pytest-mark-skipif "Link to this heading")

**Tutorial**: [[Skipping test functions]](../how-to/skipping.html#skipif)

Skip a test function if a condition is [`True`].

[[pytest.mark.]][[skipif]][(]*[[condition]]*, *[[\*]]*, *[[reason]][[=]][[None]]*[)][¶](#pytest.mark.skipif "Link to this definition")

:   

    Parameters[:]

    :   -   **condition** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *or* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- [`True/False`] if the condition should be skipped or a [[condition string]](../historical-notes.html#string-conditions).

        -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Reason why the test function is being skipped.

[]

### pytest.mark.usefixtures[¶](#pytest-mark-usefixtures "Link to this heading")

**Tutorial**: [[Use fixtures in classes and modules with usefixtures]](../how-to/fixtures.html#usefixtures)

Mark a test function as using the given fixture names.

[[pytest.mark.]][[usefixtures]][(]*[[\*]][[names]]*[)][¶](#pytest.mark.usefixtures "Link to this definition")

:   

    Parameters[:]

    :   **args** -- The names of the fixture to use, as strings.

Note

When using [`usefixtures`] in hooks, it can only load fixtures when applied to a test function before test setup (for example in the [`pytest_collection_modifyitems`] hook).

Also note that this mark has no effect when applied to **fixtures**.

[]

### pytest.mark.xfail[¶](#pytest-mark-xfail "Link to this heading")

**Tutorial**: [[XFail: mark test functions as expected to fail]](../how-to/skipping.html#xfail)

Marks a test function as *expected to fail*.

[[pytest.mark.]][[xfail]][(]*[[condition]][[=]][[False]]*, *[[\*]]*, *[[reason]][[=]][[None]]*, *[[raises]][[=]][[None]]*, *[[run]][[=]][[True]]*, *[[strict]][[=]][[strict_xfail]]*[)][¶](#pytest.mark.xfail "Link to this definition")

:   

    Parameters[:]

    :   -   **condition** (*Union\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- Condition for marking the test function as xfail ([`True/False`] or a [[condition string]](../historical-notes.html#string-conditions)). If a [`bool`], you also have to specify [`reason`] (see [[condition string]](../historical-notes.html#string-conditions)).

        -   **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Reason why the test function is marked as xfail.

        -   **raises** (Type\[[[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")\]) -- Exception class (or tuple of classes) expected to be raised by the test function; other exceptions will fail the test. Note that subclasses of the classes passed will also result in a match (similar to how the [`except`] statement works).

        -   **run** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether the test function should actually be executed. If [`False`], the function will always xfail and will not be executed (useful if a function is segfaulting).

        -   **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) --

            -   If [`False`] the function will be shown in the terminal output as [`xfailed`] if it fails and as [`xpass`] if it passes. In both cases this will not cause the test suite to fail as a whole. This is particularly useful to mark *flaky* tests (tests that fail at random) to be tackled later.

            -   If [`True`], the function will be shown in the terminal output as [`xfailed`] if it fails, but if it unexpectedly passes then it will **fail** the test suite. This is particularly useful to mark functions that are always failing and there should be a clear indication if they unexpectedly start to pass (for example a new release of a library fixes a known bug).

            Defaults to [[`strict_xfail`]](#confval-strict_xfail), which is [`False`] by default.

### Custom marks[¶](#custom-marks "Link to this heading")

Marks are created dynamically using the factory object [`pytest.mark`] and applied as a decorator.

For example:

    @pytest.mark.timeout(10, "slow", method="thread")
    def test_function(): ...

Will create and attach a [[`Mark`]](#pytest.Mark "pytest.Mark") object to the collected [[`Item`]](#pytest.Item "pytest.Item"), which can then be accessed by fixtures or hooks with [[`Node.iter_markers`]](#pytest.nodes.Node.iter_markers "_pytest.nodes.Node.iter_markers"). The [`mark`] object will have the following attributes:

    mark.args == (10, "slow")
    mark.kwargs == 

Example for using multiple custom markers:

    @pytest.mark.timeout(10, "slow", method="thread")
    @pytest.mark.slow
    def test_function(): ...

When [[`Node.iter_markers`]](#pytest.nodes.Node.iter_markers "_pytest.nodes.Node.iter_markers") or [[`Node.iter_markers_with_node`]](#pytest.nodes.Node.iter_markers_with_node "_pytest.nodes.Node.iter_markers_with_node") is used with multiple markers, the marker closest to the function will be iterated over first. The above example will result in [`@pytest.mark.slow`] followed by [`@pytest.mark.timeout(...)`].

[]

## Fixtures[¶](#fixtures "Link to this heading")

**Tutorial**: [[Fixtures reference]](fixtures.html#fixture)

Fixtures are requested by test functions or other fixtures by declaring them as argument names.

Example of a test requiring a fixture:

    def test_output(capsys):
        print("hello")
        out, err = capsys.readouterr()
        assert out == "hello\n"

Example of a fixture requiring another fixture:

    @pytest.fixture
    def db_session(tmp_path):
        fn = tmp_path / "db.file"
        return connect(fn)

For more details, consult the full [[fixtures docs]](fixtures.html#fixture).

[]

### \@pytest.fixture[¶](#pytest-fixture "Link to this heading")

[[@]][[fixture]][(]*[[fixture_function]][[:]][ ][[[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[\...]][[\]]][[,]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[scope]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]][ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Config]](#pytest.Config "_pytest.config.Config")[[\]]][[,]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]][[\]]]][ ][[=]][ ][[\'function\']]*, *[[params]][[:]][ ][[[Iterable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[\[]][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[autouse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[ids]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[,]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[FixtureFunctionDefinition]]][[[\[source\]]]](../_modules/_pytest/fixtures.html#fixture)[¶](#pytest.fixture "Link to this definition")\
[[@]][[fixture]][(]*[[fixture_function]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[scope]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]][ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Config]](#pytest.Config "_pytest.config.Config")[[\]]][[,]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]][[\]]]][ ][[=]][ ][[\'function\']]*, *[[params]][[:]][ ][[[Iterable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[\[]][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[autouse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[ids]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[\[]][[\[]][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][[,]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[FixtureFunctionMarker]]]

:   Decorator to mark a fixture factory function.

    This decorator can be used, with or without parameters, to define a fixture function.

    The name of the fixture function can later be referenced to cause its invocation ahead of running tests: test modules or classes can use the [`pytest.mark.usefixtures(fixturename)`] marker.

    Test functions can directly use fixture names as input arguments in which case the fixture instance returned from the fixture function will be injected.

    Fixtures can provide their values to test functions using [`return`] or [`yield`] statements. When using [`yield`] the code block after the [`yield`] statement is executed as teardown code regardless of the test outcome, and must yield exactly once.

    Parameters[:]

    :   -   **scope** --

            The scope for which this fixture is shared; one of [`"function"`] (default), [`"class"`], [`"module"`], [`"package"`] or [`"session"`].

            This parameter may also be a callable which receives [`(fixture_name,`]` `[`config)`] as parameters, and must return a [`str`] with one of the values mentioned above.

            See [[Dynamic scope]](../how-to/fixtures.html#dynamic-scope) in the docs for more information.

        -   **params** -- An optional list of parameters which will cause multiple invocations of the fixture function and all of the tests using it. The current parameter is available in [`request.param`].

        -   **autouse** -- If True, the fixture func is activated for all tests that can see it. If False (the default), an explicit reference is needed to activate the fixture.

        -   **ids** -- Sequence of ids each corresponding to the params so that they are part of the test id. If no ids are provided they will be generated automatically from the params.

        -   **name** -- The name of the fixture. This defaults to the name of the decorated function. If a fixture is used in the same module in which it is defined, the function name of the fixture will be shadowed by the function arg that requests the fixture; one way to resolve this is to name the decorated function [`fixture_<fixturename>`] and then use [`@pytest.fixture(name='<fixturename>')`].

[]

### capfd[¶](#capfd "Link to this heading")

**Tutorial**: [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures)

[[capfd]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#capfd)[¶](#pytest.capture.capfd "Link to this definition")

:   Enable text capturing of writes to file descriptors [`1`] and [`2`].

    The captured output is made available via [`capfd.readouterr()`] method calls, which return a [`(out,`]` `[`err)`] namedtuple. [`out`] and [`err`] will be [`text`] objects.

    Returns an instance of [[`CaptureFixture[str]`]](#pytest.CaptureFixture "pytest.CaptureFixture").

    Example:

    ::: 
    ::: highlight
        def test_system_echo(capfd):
            os.system('echo "hello"')
            captured = capfd.readouterr()
            assert captured.out == "hello\n"
    :::
    :::

[]

### capfdbinary[¶](#capfdbinary "Link to this heading")

**Tutorial**: [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures)

[[capfdbinary]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#capfdbinary)[¶](#pytest.capture.capfdbinary "Link to this definition")

:   Enable bytes capturing of writes to file descriptors [`1`] and [`2`].

    The captured output is made available via [`capfd.readouterr()`] method calls, which return a [`(out,`]` `[`err)`] namedtuple. [`out`] and [`err`] will be [`byte`] objects.

    Returns an instance of [[`CaptureFixture[bytes]`]](#pytest.CaptureFixture "pytest.CaptureFixture").

    Example:

    ::: 
    ::: highlight
        def test_system_echo(capfdbinary):
            os.system('echo "hello"')
            captured = capfdbinary.readouterr()
            assert captured.out == b"hello\n"
    :::
    :::

[]

### caplog[¶](#caplog "Link to this heading")

**Tutorial**: [[How to manage logging]](../how-to/logging.html#logging)

[[caplog]][(][)][[[\[source\]]]](../_modules/_pytest/logging.html#caplog)[¶](#pytest.logging.caplog "Link to this definition")

:   Access and control log capturing.

    Captured logs are available through the following properties/methods:

    ::: 
    ::: highlight
        * caplog.messages        -> list of format-interpolated log messages
        * caplog.text            -> string containing formatted log output
        * caplog.records         -> list of logging.LogRecord instances
        * caplog.record_tuples   -> list of (logger_name, level, message) tuples
        * caplog.clear()         -> clear captured records and formatted log output string
    :::
    :::

    Returns a [[`pytest.LogCaptureFixture`]](#pytest.LogCaptureFixture "pytest.LogCaptureFixture") instance.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[LogCaptureFixture]][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture)[¶](#pytest.LogCaptureFixture "Link to this definition")

:   Provides access and control of log capturing.

```
<!-- -->
```

*[[property]][ ]*[[handler]]*[[:]][ ][LogCaptureHandler]*[¶](#pytest.LogCaptureFixture.handler "Link to this definition")

:   Get the logging handler used by the fixture.

```
<!-- -->
```

[[get_records]][(]*[[when]]*[)][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture.get_records)[¶](#pytest.LogCaptureFixture.get_records "Link to this definition")

:   Get the logging records for one of the possible test phases.

    Parameters[:]

    :   **when** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")*\[\'setup\',* *\'call\',* *\'teardown\'\]*) -- Which test phase to obtain the records from. Valid values are: "setup", "call" and "teardown".

    Returns[:]

    :   The list of captured records at the given stage.

    Return type[:]

    :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[*LogRecord*](https://docs.python.org/3/library/logging.html#logging.LogRecord "(in Python v3.14)")\]

    ::: versionadded
    [Added in version 3.4.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[text]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.LogCaptureFixture.text "Link to this definition")

:   The formatted log text.

```
<!-- -->
```

*[[property]][ ]*[[records]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[LogRecord]](https://docs.python.org/3/library/logging.html#logging.LogRecord "(in Python v3.14)")[[\]]]*[¶](#pytest.LogCaptureFixture.records "Link to this definition")

:   The list of log records.

```
<!-- -->
```

*[[property]][ ]*[[record_tuples]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]]*[¶](#pytest.LogCaptureFixture.record_tuples "Link to this definition")

:   A list of a stripped down version of log records intended for use in assertion comparison.

    The format of the tuple is:

    > <div>
    >
    > (logger_name, log_level, message)
    >
    > </div>

```
<!-- -->
```

*[[property]][ ]*[[messages]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#pytest.LogCaptureFixture.messages "Link to this definition")

:   A list of format-interpolated log messages.

    Unlike 'records', which contains the format string and parameters for interpolation, log messages in this list are all interpolated.

    Unlike 'text', which contains the output from the handler, log messages in this list are unadorned with levels, timestamps, etc, making exact comparisons more reliable.

    Note that traceback or stack info (from [[`logging.exception()`]](https://docs.python.org/3/library/logging.html#logging.exception "(in Python v3.14)") or the [`exc_info`] or [`stack_info`] arguments to the logging functions) is not included, as this is added by the formatter in the handler.

    ::: versionadded
    [Added in version 3.7.]
    :::

```
<!-- -->
```

[[clear]][(][)][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture.clear)[¶](#pytest.LogCaptureFixture.clear "Link to this definition")

:   Reset the list of log records and the captured log text.

```
<!-- -->
```

[[set_level]][(]*[[level]]*, *[[logger]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture.set_level)[¶](#pytest.LogCaptureFixture.set_level "Link to this definition")

:   Set the threshold level of a logger for the duration of a test.

    Logging messages which are less severe than this level will not be captured.

    ::: versionchanged
    [Changed in version 3.4: ]The levels of the loggers changed by this function will be restored to their initial values at the end of the test.
    :::

    Will enable the requested logging level if it was disabled via [[`logging.disable()`]](https://docs.python.org/3/library/logging.html#logging.disable "(in Python v3.14)").

    Parameters[:]

    :   -   **level** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The level.

        -   **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- The logger to update. If not given, the root logger.

```
<!-- -->
```

*[with]* [[at_level]][(]*[[level]]*, *[[logger]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture.at_level)[¶](#pytest.LogCaptureFixture.at_level "Link to this definition")

:   Context manager that sets the level for capturing of logs. After the end of the 'with' statement the level is restored to its original value.

    Will enable the requested logging level if it was disabled via [[`logging.disable()`]](https://docs.python.org/3/library/logging.html#logging.disable "(in Python v3.14)").

    Parameters[:]

    :   -   **level** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The level.

        -   **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- The logger to update. If not given, the root logger.

```
<!-- -->
```

*[with]* [[filtering]][(]*[[filter\_]]*[)][[[\[source\]]]](../_modules/_pytest/logging.html#LogCaptureFixture.filtering)[¶](#pytest.LogCaptureFixture.filtering "Link to this definition")

:   Context manager that temporarily adds the given filter to the caplog's [[`handler()`]](#pytest.LogCaptureFixture.handler "pytest.LogCaptureFixture.handler") for the 'with' statement block, and removes that filter at the end of the block.

    Parameters[:]

    :   **filter** -- A custom [[`logging.Filter`]](https://docs.python.org/3/library/logging.html#logging.Filter "(in Python v3.14)") object.

    ::: versionadded
    [Added in version 7.5.]
    :::

[]

### capsys[¶](#capsys "Link to this heading")

**Tutorial**: [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures)

[[capsys]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#capsys)[¶](#pytest.capture.capsys "Link to this definition")

:   Enable text capturing of writes to [`sys.stdout`] and [`sys.stderr`].

    The captured output is made available via [`capsys.readouterr()`] method calls, which return a [`(out,`]` `[`err)`] namedtuple. [`out`] and [`err`] will be [`text`] objects.

    Returns an instance of [[`CaptureFixture[str]`]](#pytest.CaptureFixture "pytest.CaptureFixture").

    Example:

    ::: 
    ::: highlight
        def test_output(capsys):
            print("hello")
            captured = capsys.readouterr()
            assert captured.out == "hello\n"
    :::
    :::

```
<!-- -->
```

*[[class]][ ]*[[CaptureFixture]][[[\[source\]]]](../_modules/_pytest/capture.html#CaptureFixture)[¶](#pytest.CaptureFixture "Link to this definition")

:   Object returned by the [[`capsys`]](#std-fixture-capsys), [[`capsysbinary`]](#std-fixture-capsysbinary), [[`capfd`]](#std-fixture-capfd) and [[`capfdbinary`]](#std-fixture-capfdbinary) fixtures.

```
<!-- -->
```

[[readouterr]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#CaptureFixture.readouterr)[¶](#pytest.CaptureFixture.readouterr "Link to this definition")

:   Read and return the captured output so far, resetting the internal buffer.

    Returns[:]

    :   The captured content as a namedtuple with [`out`] and [`err`] string attributes.

    Return type[:]

    :   *CaptureResult*

```
<!-- -->
```

*[with]* [[disabled]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#CaptureFixture.disabled)[¶](#pytest.CaptureFixture.disabled "Link to this definition")

:   Temporarily disable capturing while inside the [`with`] block.

[]

### capteesys[¶](#capteesys "Link to this heading")

**Tutorial**: [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures)

[[capteesys]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#capteesys)[¶](#pytest.capture.capteesys "Link to this definition")

:   Enable simultaneous text capturing and pass-through of writes to [`sys.stdout`] and [`sys.stderr`] as defined by [`--capture=`].

    The captured output is made available via [`capteesys.readouterr()`] method calls, which return a [`(out,`]` `[`err)`] namedtuple. [`out`] and [`err`] will be [`text`] objects.

    The output is also passed-through, allowing it to be "live-printed", reported, or both as defined by [`--capture=`].

    Returns an instance of [[`CaptureFixture[str]`]](#pytest.CaptureFixture "pytest.CaptureFixture").

    Example:

    ::: 
    ::: highlight
        def test_output(capteesys):
            print("hello")
            captured = capteesys.readouterr()
            assert captured.out == "hello\n"
    :::
    :::

[]

### capsysbinary[¶](#capsysbinary "Link to this heading")

**Tutorial**: [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures)

[[capsysbinary]][(][)][[[\[source\]]]](../_modules/_pytest/capture.html#capsysbinary)[¶](#pytest.capture.capsysbinary "Link to this definition")

:   Enable bytes capturing of writes to [`sys.stdout`] and [`sys.stderr`].

    The captured output is made available via [`capsysbinary.readouterr()`] method calls, which return a [`(out,`]` `[`err)`] namedtuple. [`out`] and [`err`] will be [`bytes`] objects.

    Returns an instance of [[`CaptureFixture[bytes]`]](#pytest.CaptureFixture "pytest.CaptureFixture").

    Example:

    ::: 
    ::: highlight
        def test_output(capsysbinary):
            print("hello")
            captured = capsysbinary.readouterr()
            assert captured.out == b"hello\n"
    :::
    :::

[]

### config.cache[¶](#config-cache "Link to this heading")

**Tutorial**: [[How to re-run failed tests and maintain state between test runs]](../how-to/cache.html#cache)

The [`config.cache`] object allows other plugins and fixtures to store and retrieve values across test runs. To access it from fixtures request [`pytestconfig`] into your fixture and get it with [`pytestconfig.cache`].

Under the hood, the cache plugin uses the simple [`dumps`]/[`loads`] API of the [[`json`]](https://docs.python.org/3/library/json.html#module-json "(in Python v3.14)") stdlib module.

[`config.cache`] is an instance of [[`pytest.Cache`]](#pytest.Cache "pytest.Cache"):

*[[final]][ ][[class]][ ]*[[Cache]][[[\[source\]]]](../_modules/_pytest/cacheprovider.html#Cache)[¶](#pytest.Cache "Link to this definition")

:   Instance of the [`cache`] fixture.

```
<!-- -->
```

[[mkdir]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/cacheprovider.html#Cache.mkdir)[¶](#pytest.Cache.mkdir "Link to this definition")

:   Return a directory path object with the given name.

    If the directory does not yet exist, it will be created. You can use it to manage files to e.g. store/retrieve database dumps across test sessions.

    ::: versionadded
    [Added in version 7.0.]
    :::

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Must be a string not containing a [`/`] separator. Make sure the name contains your plugin or application identifiers to prevent clashes with other cache users.

```
<!-- -->
```

[[get]][(]*[[key]]*, *[[default]]*[)][[[\[source\]]]](../_modules/_pytest/cacheprovider.html#Cache.get)[¶](#pytest.Cache.get "Link to this definition")

:   Return the cached value for the given key.

    If no value was yet cached or the value cannot be read, the specified default is returned.

    Parameters[:]

    :   -   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Must be a [`/`] separated value. Usually the first name is the name of your plugin or your application.

        -   **default** -- The value to return in case of a cache-miss or invalid cache value.

```
<!-- -->
```

[[set]][(]*[[key]]*, *[[value]]*[)][[[\[source\]]]](../_modules/_pytest/cacheprovider.html#Cache.set)[¶](#pytest.Cache.set "Link to this definition")

:   Save value for the given key.

    Parameters[:]

    :   -   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Must be a [`/`] separated value. Usually the first name is the name of your plugin or your application.

        -   **value** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- Must be of any combination of basic python types, including nested types like lists of dictionaries.

[]

### doctest_namespace[¶](#doctest-namespace "Link to this heading")

**Tutorial**: [[How to run doctests]](../how-to/doctest.html#doctest)

[[doctest_namespace]][(][)][[[\[source\]]]](../_modules/_pytest/doctest.html#doctest_namespace)[¶](#pytest.doctest.doctest_namespace "Link to this definition")

:   Fixture that returns a [[`dict`]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") that will be injected into the namespace of doctests.

    Usually this fixture is used in conjunction with another [`autouse`] fixture:

    ::: 
    ::: highlight
        @pytest.fixture(autouse=True)
        def add_np(doctest_namespace):
            doctest_namespace["np"] = numpy
    :::
    :::

    For more details: [['doctest_namespace' fixture]](../how-to/doctest.html#doctest-namespace).

[]

### monkeypatch[¶](#monkeypatch "Link to this heading")

**Tutorial**: [[How to monkeypatch/mock modules and environments]](../how-to/monkeypatch.html#monkeypatching)

[[monkeypatch]][(][)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#monkeypatch)[¶](#pytest.monkeypatch.monkeypatch "Link to this definition")

:   A convenient fixture for monkey-patching.

    The fixture provides these methods to modify objects, dictionaries, or [[`os.environ`]](https://docs.python.org/3/library/os.html#os.environ "(in Python v3.14)"):

    -   [[`monkeypatch.setattr(obj,`]` `[`name,`]` `[`value,`]` `[`raising=True)`]](#pytest.MonkeyPatch.setattr "pytest.MonkeyPatch.setattr")

    -   [[`monkeypatch.delattr(obj,`]` `[`name,`]` `[`raising=True)`]](#pytest.MonkeyPatch.delattr "pytest.MonkeyPatch.delattr")

    -   [[`monkeypatch.setitem(mapping,`]` `[`name,`]` `[`value)`]](#pytest.MonkeyPatch.setitem "pytest.MonkeyPatch.setitem")

    -   [[`monkeypatch.delitem(obj,`]` `[`name,`]` `[`raising=True)`]](#pytest.MonkeyPatch.delitem "pytest.MonkeyPatch.delitem")

    -   [[`monkeypatch.setenv(name,`]` `[`value,`]` `[`prepend=None)`]](#pytest.MonkeyPatch.setenv "pytest.MonkeyPatch.setenv")

    -   [[`monkeypatch.delenv(name,`]` `[`raising=True)`]](#pytest.MonkeyPatch.delenv "pytest.MonkeyPatch.delenv")

    -   [[`monkeypatch.syspath_prepend(path)`]](#pytest.MonkeyPatch.syspath_prepend "pytest.MonkeyPatch.syspath_prepend")

    -   [[`monkeypatch.chdir(path)`]](#pytest.MonkeyPatch.chdir "pytest.MonkeyPatch.chdir")

    -   [[`monkeypatch.context()`]](#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context")

    All modifications will be undone after the requesting test function or fixture has finished. The [`raising`] parameter determines if a [[`KeyError`]](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") or [[`AttributeError`]](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)") will be raised if the set/deletion operation does not have the specified target.

    To undo modifications done by the fixture in a contained scope, use [[`context()`]](#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context").

    Returns a [[`MonkeyPatch`]](#pytest.MonkeyPatch "pytest.MonkeyPatch") instance.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[MonkeyPatch]][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch)[¶](#pytest.MonkeyPatch "Link to this definition")

:   Helper to conveniently monkeypatch attributes/items/environment variables/syspath.

    Returned by the [[`monkeypatch`]](#std-fixture-monkeypatch) fixture.

    ::: versionchanged
    [Changed in version 6.2: ]Can now also be used directly as [`pytest.MonkeyPatch()`], for when the fixture is not available. In this case, use [[`with`]` `[`MonkeyPatch.context()`]` `[`as`]` `[`mp:`]](#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context") or remember to call [[`undo()`]](#pytest.MonkeyPatch.undo "pytest.MonkeyPatch.undo") explicitly.
    :::

```
<!-- -->
```

*[classmethod] [with]* [[context]][(][)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.context)[¶](#pytest.MonkeyPatch.context "Link to this definition")

:   Context manager that returns a new [[`MonkeyPatch`]](#pytest.MonkeyPatch "pytest.MonkeyPatch") object which undoes any patching done inside the [`with`] block upon exit.

    Example:

    ::: 
    ::: highlight
        import functools

        def test_partial(monkeypatch):
            with monkeypatch.context() as m:
                m.setattr(functools, "partial", 3)
    :::
    :::

    Useful in situations where it is desired to undo some patches before the test ends, such as mocking [`stdlib`] functions that might break pytest itself if mocked (for examples of this see [#3290](https://github.com/pytest-dev/pytest/issues/3290)).

```
<!-- -->
```

[[setattr]][(]*[[target:] [str]]*, *[[name:] [object]]*, *[[value:] [\~\_pytest.monkeypatch.Notset] [=] [\<notset\>]]*, *[[raising:] [bool] [=] [True]]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.setattr)[¶](#pytest.MonkeyPatch.setattr "Link to this definition")\
[[setattr]][(]*[[target]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]*, *[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[value]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]*, *[[raising]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]]

:   Set attribute value on target, memorizing the old value.

    For example:

    ::: 
    ::: highlight
        import os

        monkeypatch.setattr(os, "getcwd", lambda: "/")
    :::
    :::

    The code above replaces the [[`os.getcwd()`]](https://docs.python.org/3/library/os.html#os.getcwd "(in Python v3.14)") function by a [`lambda`] which always returns [`"/"`].

    For convenience, you can specify a string as [`target`] which will be interpreted as a dotted import path, with the last part being the attribute name:

    ::: 
    ::: highlight
        monkeypatch.setattr("os.getcwd", lambda: "/")
    :::
    :::

    Raises [[`AttributeError`]](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)") if the attribute does not exist, unless [`raising`] is set to False.

    **Where to patch**

    [`monkeypatch.setattr`] works by (temporarily) changing the object that a name points to with another one. There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.

    See the section [[Where to patch]](https://docs.python.org/3/library/unittest.mock.html#where-to-patch "(in Python v3.14)") in the [[`unittest.mock`]](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock "(in Python v3.14)") docs for a complete explanation, which is meant for [[`unittest.mock.patch()`]](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "(in Python v3.14)") but applies to [`monkeypatch.setattr`] as well.

```
<!-- -->
```

[[delattr]][(]*[[target]]*, *[[name=\<notset\>]]*, *[[raising=True]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.delattr)[¶](#pytest.MonkeyPatch.delattr "Link to this definition")

:   Delete attribute [`name`] from [`target`].

    If no [`name`] is specified and [`target`] is a string it will be interpreted as a dotted import path with the last part being the attribute name.

    Raises AttributeError it the attribute does not exist, unless [`raising`] is set to False.

```
<!-- -->
```

[[setitem]][(]*[[dic]]*, *[[name]]*, *[[value]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.setitem)[¶](#pytest.MonkeyPatch.setitem "Link to this definition")

:   Set dictionary entry [`name`] to value.

```
<!-- -->
```

[[delitem]][(]*[[dic]]*, *[[name]]*, *[[raising]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.delitem)[¶](#pytest.MonkeyPatch.delitem "Link to this definition")

:   Delete [`name`] from dict.

    Raises [`KeyError`] if it doesn't exist, unless [`raising`] is set to False.

```
<!-- -->
```

[[setenv]][(]*[[name]]*, *[[value]]*, *[[prepend]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.setenv)[¶](#pytest.MonkeyPatch.setenv "Link to this definition")

:   Set environment variable [`name`] to [`value`].

    If [`prepend`] is a character, read the current environment variable value and prepend the [`value`] adjoined with the [`prepend`] character.

```
<!-- -->
```

[[delenv]][(]*[[name]]*, *[[raising]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.delenv)[¶](#pytest.MonkeyPatch.delenv "Link to this definition")

:   Delete [`name`] from the environment.

    Raises [`KeyError`] if it does not exist, unless [`raising`] is set to False.

```
<!-- -->
```

[[syspath_prepend]][(]*[[path]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.syspath_prepend)[¶](#pytest.MonkeyPatch.syspath_prepend "Link to this definition")

:   Prepend [`path`] to [`sys.path`] list of import locations.

```
<!-- -->
```

[[chdir]][(]*[[path]]*[)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.chdir)[¶](#pytest.MonkeyPatch.chdir "Link to this definition")

:   Change the current working directory to the specified path.

    Parameters[:]

    :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The path to change into.

```
<!-- -->
```

[[undo]][(][)][[[\[source\]]]](../_modules/_pytest/monkeypatch.html#MonkeyPatch.undo)[¶](#pytest.MonkeyPatch.undo "Link to this definition")

:   Undo previous changes.

    This call consumes the undo stack. Calling it a second time has no effect unless you do more monkeypatching after the undo call.

    There is generally no need to call [`undo()`], since it is called automatically during tear-down.

    ::: 
    Note

    The same [`monkeypatch`] fixture is used across a single test function invocation. If [`monkeypatch`] is used both by the test function itself and one of the test fixtures, calling [`undo()`] will undo all of the changes made in both functions.

    Prefer to use [[`context()`]](#pytest.MonkeyPatch.context "pytest.MonkeyPatch.context") instead.
    :::

[]

### pytestconfig[¶](#pytestconfig "Link to this heading")

[[pytestconfig]][(][)][[[\[source\]]]](../_modules/_pytest/fixtures.html#pytestconfig)[¶](#pytest.fixtures.pytestconfig "Link to this definition")

:   Session-scoped fixture that returns the session's [[`pytest.Config`]](#pytest.Config "pytest.Config") object.

    Example:

    ::: 
    ::: highlight
        def test_foo(pytestconfig):
            if pytestconfig.get_verbosity() > 0:
                ...
    :::
    :::

[]

### pytester[¶](#pytester "Link to this heading")

[Added in version 6.2.]

Provides a [[`Pytester`]](#pytest.Pytester "pytest.Pytester") instance that can be used to run and test pytest itself.

It provides an empty directory where pytest can be executed in isolation, and contains facilities to write tests, configuration files, and match against expected output.

To use it, include in your topmost [`conftest.py`] file:

    pytest_plugins = "pytester"

*[[final]][ ][[class]][ ]*[[Pytester]][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester)[¶](#pytest.Pytester "Link to this definition")

:   Facilities to write tests/configuration files, execute pytest in isolation, and match against expected output, perfect for black-box testing of pytest plugins.

    It attempts to isolate the test run from external factors as much as possible, modifying the current working directory to [[`path`]](#pytest.Pytester.path "pytest.Pytester.path") and environment variables during initialization.

```
<!-- -->
```

*[[exception]][ ]*[[TimeoutExpired]][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.TimeoutExpired)[¶](#pytest.Pytester.TimeoutExpired "Link to this definition")

:   

```
<!-- -->
```

[[plugins]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]]*[¶](#pytest.Pytester.plugins "Link to this definition")

:   A list of plugins to use with [[`parseconfig()`]](#pytest.Pytester.parseconfig "pytest.Pytester.parseconfig") and [[`runpytest()`]](#pytest.Pytester.runpytest "pytest.Pytester.runpytest"). Initially this is an empty list but plugins can be added to the list.

    When running in subprocess mode, specify plugins by name (str) - adding plugin objects directly is not supported.

```
<!-- -->
```

*[[property]][ ]*[[path]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Pytester.path "Link to this definition")

:   Temporary directory path used to create files/run tests from, etc.

```
<!-- -->
```

[[make_hook_recorder]][(]*[[pluginmanager]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.make_hook_recorder)[¶](#pytest.Pytester.make_hook_recorder "Link to this definition")

:   Create a new [[`HookRecorder`]](#pytest.HookRecorder "pytest.HookRecorder") for a [[`PytestPluginManager`]](#pytest.PytestPluginManager "pytest.PytestPluginManager").

```
<!-- -->
```

[[chdir]][(][)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.chdir)[¶](#pytest.Pytester.chdir "Link to this definition")

:   Cd into the temporary directory.

    This is done automatically upon instantiation.

```
<!-- -->
```

[[makefile]][(]*[[ext]]*, *[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.makefile)[¶](#pytest.Pytester.makefile "Link to this definition")

:   Create new text file(s) in the test directory.

    Parameters[:]

    :   -   **ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The extension the file(s) should use, including the dot, e.g. [`.py`].

        -   **args** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- All args are treated as strings and joined using newlines. The result is written as contents to the file. The name of the file is based on the test function requesting this fixture.

        -   **kwargs** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Each keyword is the name of a file, while the value of it will be written as contents of the file.

    Returns[:]

    :   The first created file.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

    Examples:

    ::: 
    ::: highlight
        pytester.makefile(".txt", "line1", "line2")

        pytester.makefile(".ini", pytest="[pytest]\naddopts=-rs\n")
    :::
    :::

    To create binary files, use [[`pathlib.Path.write_bytes()`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "(in Python v3.14)") directly:

    ::: 
    ::: highlight
        filename = pytester.path.joinpath("foo.bin")
        filename.write_bytes(b"...")
    :::
    :::

```
<!-- -->
```

[[makeconftest]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.makeconftest)[¶](#pytest.Pytester.makeconftest "Link to this definition")

:   Write a conftest.py file.

    Parameters[:]

    :   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The contents.

    Returns[:]

    :   The conftest.py file.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

```
<!-- -->
```

[[makeini]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.makeini)[¶](#pytest.Pytester.makeini "Link to this definition")

:   Write a tox.ini file.

    Parameters[:]

    :   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The contents.

    Returns[:]

    :   The tox.ini file.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

```
<!-- -->
```

[[maketoml]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.maketoml)[¶](#pytest.Pytester.maketoml "Link to this definition")

:   Write a pytest.toml file.

    Parameters[:]

    :   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The contents.

    Returns[:]

    :   The pytest.toml file.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

    ::: versionadded
    [Added in version 9.0.]
    :::

```
<!-- -->
```

[[getinicfg]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getinicfg)[¶](#pytest.Pytester.getinicfg "Link to this definition")

:   Return the pytest section from the tox.ini config file.

```
<!-- -->
```

[[makepyprojecttoml]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.makepyprojecttoml)[¶](#pytest.Pytester.makepyprojecttoml "Link to this definition")

:   Write a pyproject.toml file.

    Parameters[:]

    :   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The contents.

    Returns[:]

    :   The pyproject.ini file.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

    ::: versionadded
    [Added in version 6.0.]
    :::

```
<!-- -->
```

[[makepyfile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.makepyfile)[¶](#pytest.Pytester.makepyfile "Link to this definition")

:   Shortcut for .makefile() with a .py extension.

    Defaults to the test name with a '.py' extension, e.g test_foobar.py, overwriting existing files.

    Examples:

    ::: 
    ::: highlight
        def test_something(pytester):
            # Initial file is created test_something.py.
            pytester.makepyfile("foobar")
            # To create multiple files, pass kwargs accordingly.
            pytester.makepyfile(custom="foobar")
            # At this point, both 'test_something.py' & 'custom.py' exist in the test directory.
    :::
    :::

```
<!-- -->
```

[[maketxtfile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.maketxtfile)[¶](#pytest.Pytester.maketxtfile "Link to this definition")

:   Shortcut for .makefile() with a .txt extension.

    Defaults to the test name with a '.txt' extension, e.g test_foobar.txt, overwriting existing files.

    Examples:

    ::: 
    ::: highlight
        def test_something(pytester):
            # Initial file is created test_something.txt.
            pytester.maketxtfile("foobar")
            # To create multiple files, pass kwargs accordingly.
            pytester.maketxtfile(custom="foobar")
            # At this point, both 'test_something.txt' & 'custom.txt' exist in the test directory.
    :::
    :::

```
<!-- -->
```

[[syspathinsert]][(]*[[path]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.syspathinsert)[¶](#pytest.Pytester.syspathinsert "Link to this definition")

:   Prepend a directory to sys.path, defaults to [[`path`]](#pytest.Pytester.path "pytest.Pytester.path").

    This is undone automatically when this object dies at the end of each test.

    Parameters[:]

    :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) -- The path.

```
<!-- -->
```

[[mkdir]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.mkdir)[¶](#pytest.Pytester.mkdir "Link to this definition")

:   Create a new (sub)directory.

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The name of the directory, relative to the pytester path.

    Returns[:]

    :   The created directory.

    Return type[:]

    :   [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

```
<!-- -->
```

[[mkpydir]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.mkpydir)[¶](#pytest.Pytester.mkpydir "Link to this definition")

:   Create a new python package.

    This creates a (sub)directory with an empty [`__init__.py`] file so it gets recognised as a Python package.

```
<!-- -->
```

[[copy_example]][(]*[[name]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.copy_example)[¶](#pytest.Pytester.copy_example "Link to this definition")

:   Copy file from project's directory into the testdir.

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- The name of the file to copy.

    Returns[:]

    :   Path to the copied directory (inside [`self.path`]).

    Return type[:]

    :   [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

```
<!-- -->
```

[[getnode]][(]*[[config]]*, *[[arg]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getnode)[¶](#pytest.Pytester.getnode "Link to this definition")

:   Get the collection node of a file.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "_pytest.config.Config")) -- A pytest config. See [[`parseconfig()`]](#pytest.Pytester.parseconfig "pytest.Pytester.parseconfig") and [[`parseconfigure()`]](#pytest.Pytester.parseconfigure "pytest.Pytester.parseconfigure") for creating it.

        -   **arg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- Path to the file.

    Returns[:]

    :   The node.

    Return type[:]

    :   [*Collector*](#pytest.Collector "_pytest.nodes.Collector") \| [*Item*](#pytest.Item "_pytest.nodes.Item")

```
<!-- -->
```

[[getpathnode]][(]*[[path]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getpathnode)[¶](#pytest.Pytester.getpathnode "Link to this definition")

:   Return the collection node of a file.

    This is like [[`getnode()`]](#pytest.Pytester.getnode "pytest.Pytester.getnode") but uses [[`parseconfigure()`]](#pytest.Pytester.parseconfigure "pytest.Pytester.parseconfigure") to create the (configured) pytest Config instance.

    Parameters[:]

    :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- Path to the file.

    Returns[:]

    :   The node.

    Return type[:]

    :   [*Collector*](#pytest.Collector "_pytest.nodes.Collector") \| [*Item*](#pytest.Item "_pytest.nodes.Item")

```
<!-- -->
```

[[genitems]][(]*[[colitems]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.genitems)[¶](#pytest.Pytester.genitems "Link to this definition")

:   Generate all test items from a collection node.

    This recurses into the collection node and returns a list of all the test items contained within.

    Parameters[:]

    :   **colitems** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*Item*](#pytest.Item "_pytest.nodes.Item") *\|* [*Collector*](#pytest.Collector "_pytest.nodes.Collector")*\]*) -- The collection nodes.

    Returns[:]

    :   The collected items.

    Return type[:]

    :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[*Item*](#pytest.Item "_pytest.nodes.Item")\]

```
<!-- -->
```

[[runitem]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runitem)[¶](#pytest.Pytester.runitem "Link to this definition")

:   Run the "test_func" Item.

    The calling test instance (class containing the test method) must provide a [`.getrunner()`] method which should return a runner which can run the test protocol for a single item, e.g. [`_pytest.runner.runtestprotocol`].

```
<!-- -->
```

[[inline_runsource]][(]*[[source]]*, *[[\*]][[cmdlineargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.inline_runsource)[¶](#pytest.Pytester.inline_runsource "Link to this definition")

:   Run a test module in process using [`pytest.main()`].

    This run writes "source" into a temporary file and runs [`pytest.main()`] on it, returning a [[`HookRecorder`]](#pytest.HookRecorder "pytest.HookRecorder") instance for the result.

    Parameters[:]

    :   -   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The source code of the test module.

        -   **cmdlineargs** -- Any extra command line arguments to use.

```
<!-- -->
```

[[inline_genitems]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.inline_genitems)[¶](#pytest.Pytester.inline_genitems "Link to this definition")

:   Run [`pytest.main(['--collect-only'])`] in-process.

    Runs the [[`pytest.main()`]](#pytest.main "pytest.main") function to run all of pytest inside the test process itself like [[`inline_run()`]](#pytest.Pytester.inline_run "pytest.Pytester.inline_run"), but returns a tuple of the collected items and a [[`HookRecorder`]](#pytest.HookRecorder "pytest.HookRecorder") instance.

```
<!-- -->
```

[[inline_run]][(]*[[\*]][[args]]*, *[[plugins]][[=]][[()]]*, *[[no_reraise_ctrlc]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.inline_run)[¶](#pytest.Pytester.inline_run "Link to this definition")

:   Run [`pytest.main()`] in-process, returning a HookRecorder.

    Runs the [[`pytest.main()`]](#pytest.main "pytest.main") function to run all of pytest inside the test process itself. This means it can return a [[`HookRecorder`]](#pytest.HookRecorder "pytest.HookRecorder") instance which gives more detailed results from that run than can be done by matching stdout/stderr from [[`runpytest()`]](#pytest.Pytester.runpytest "pytest.Pytester.runpytest").

    Parameters[:]

    :   -   **args** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- Command line arguments to pass to [[`pytest.main()`]](#pytest.main "pytest.main").

        -   **plugins** -- Extra plugin instances the [`pytest.main()`] instance should use.

        -   **no_reraise_ctrlc** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Typically we reraise keyboard interrupts from the child run. If True, the KeyboardInterrupt exception is captured.

```
<!-- -->
```

[[runpytest_inprocess]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runpytest_inprocess)[¶](#pytest.Pytester.runpytest_inprocess "Link to this definition")

:   Return result of running pytest in-process, providing a similar interface to what self.runpytest() provides.

```
<!-- -->
```

[[runpytest]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runpytest)[¶](#pytest.Pytester.runpytest "Link to this definition")

:   Run pytest inline or in a subprocess, depending on the command line option "--runpytest" and return a [[`RunResult`]](#pytest.RunResult "pytest.RunResult").

```
<!-- -->
```

[[parseconfig]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.parseconfig)[¶](#pytest.Pytester.parseconfig "Link to this definition")

:   Return a new pytest [[`pytest.Config`]](#pytest.Config "pytest.Config") instance from given commandline args.

    This invokes the pytest bootstrapping code in \_pytest.config to create a new [[`pytest.PytestPluginManager`]](#pytest.PytestPluginManager "pytest.PytestPluginManager") and call the [[`pytest_cmdline_parse`]](#std-hook-pytest_cmdline_parse) hook to create a new [[`pytest.Config`]](#pytest.Config "pytest.Config") instance.

    If [[`plugins`]](#pytest.Pytester.plugins "pytest.Pytester.plugins") has been populated they should be plugin modules to be registered with the plugin manager.

```
<!-- -->
```

[[parseconfigure]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.parseconfigure)[¶](#pytest.Pytester.parseconfigure "Link to this definition")

:   Return a new pytest configured Config instance.

    Returns a new [[`pytest.Config`]](#pytest.Config "pytest.Config") instance like [[`parseconfig()`]](#pytest.Pytester.parseconfig "pytest.Pytester.parseconfig"), but also calls the [[`pytest_configure`]](#std-hook-pytest_configure) hook.

```
<!-- -->
```

[[getitem]][(]*[[source]]*, *[[funcname]][[=]][[\'test_func\']]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getitem)[¶](#pytest.Pytester.getitem "Link to this definition")

:   Return the test item for a test function.

    Writes the source to a python file and runs pytest's collection on the resulting module, returning the test item for the requested function name.

    Parameters[:]

    :   -   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The module source.

        -   **funcname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The name of the test function for which to return a test item.

    Returns[:]

    :   The test item.

    Return type[:]

    :   [*Item*](#pytest.Item "_pytest.nodes.Item")

```
<!-- -->
```

[[getitems]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getitems)[¶](#pytest.Pytester.getitems "Link to this definition")

:   Return all test items collected from the module.

    Writes the source to a Python file and runs pytest's collection on the resulting module, returning all test items contained within.

```
<!-- -->
```

[[getmodulecol]][(]*[[source]]*, *[[configargs]][[=]][[()]]*, *[[\*]]*, *[[withinit]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.getmodulecol)[¶](#pytest.Pytester.getmodulecol "Link to this definition")

:   Return the module collection node for [`source`].

    Writes [`source`] to a file using [[`makepyfile()`]](#pytest.Pytester.makepyfile "pytest.Pytester.makepyfile") and then runs the pytest collection on it, returning the collection node for the test module.

    Parameters[:]

    :   -   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The source code of the module to collect.

        -   **configargs** -- Any extra arguments to pass to [[`parseconfigure()`]](#pytest.Pytester.parseconfigure "pytest.Pytester.parseconfigure").

        -   **withinit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to also write an [`__init__.py`] file to the same directory to ensure it is a package.

```
<!-- -->
```

[[collect_by_name]][(]*[[modcol]]*, *[[name]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.collect_by_name)[¶](#pytest.Pytester.collect_by_name "Link to this definition")

:   Return the collection node for name from the module collection.

    Searches a module collection node for a collection node matching the given name.

    Parameters[:]

    :   -   **modcol** ([*Collector*](#pytest.Collector "_pytest.nodes.Collector")) -- A module collection node; see [[`getmodulecol()`]](#pytest.Pytester.getmodulecol "pytest.Pytester.getmodulecol").

        -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The name of the node to return.

```
<!-- -->
```

[[popen]][(]*[[cmdargs]]*, *[[stdout]][[=]][[-1]]*, *[[stderr]][[=]][[-1]]*, *[[stdin]][[=]][[NotSetType.token]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.popen)[¶](#pytest.Pytester.popen "Link to this definition")

:   Invoke [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)").

    Calls [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)") making sure the current working directory is in [`PYTHONPATH`].

    You probably want to use [[`run()`]](#pytest.Pytester.run "pytest.Pytester.run") instead.

```
<!-- -->
```

[[run]][(]*[[\*]][[cmdargs]]*, *[[timeout]][[=]][[None]]*, *[[stdin]][[=]][[NotSetType.token]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.run)[¶](#pytest.Pytester.run "Link to this definition")

:   Run a command with arguments.

    Run a process using [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)") saving the stdout and stderr.

    Parameters[:]

    :   -   **cmdargs** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The sequence of arguments to pass to [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)"), with path-like objects being converted to [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") automatically.

        -   **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *\|* *None*) -- The period in seconds after which to timeout and raise [[`Pytester.TimeoutExpired`]](#pytest.Pytester.TimeoutExpired "pytest.Pytester.TimeoutExpired").

        -   **stdin** (*\_pytest.compat.NotSetType* *\|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") *\|* *IO\[Any\]* *\|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) --

            Optional standard input.

            -   If it is [`CLOSE_STDIN`] (Default), then this method calls [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)") with [`stdin=subprocess.PIPE`], and the standard input is closed immediately after the new command is started.

            -   If it is of type [[`bytes`]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)"), these bytes are sent to the standard input of the command.

            -   Otherwise, it is passed through to [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)"). For further information in this case, consult the document of the [`stdin`] parameter in [[`subprocess.Popen`]](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "(in Python v3.14)").

    Returns[:]

    :   The result.

    Return type[:]

    :   [*RunResult*](#pytest.RunResult "_pytest.pytester.RunResult")

```
<!-- -->
```

[[runpython]][(]*[[script]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runpython)[¶](#pytest.Pytester.runpython "Link to this definition")

:   Run a python script using sys.executable as interpreter.

```
<!-- -->
```

[[runpython_c]][(]*[[command]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runpython_c)[¶](#pytest.Pytester.runpython_c "Link to this definition")

:   Run [`python`]` `[`-c`]` `[`"command"`].

```
<!-- -->
```

[[runpytest_subprocess]][(]*[[\*]][[args]]*, *[[timeout]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.runpytest_subprocess)[¶](#pytest.Pytester.runpytest_subprocess "Link to this definition")

:   Run pytest as a subprocess with given arguments.

    Any plugins added to the [[`plugins`]](#pytest.Pytester.plugins "pytest.Pytester.plugins") list will be added using the [`-p`] command line option. Additionally [`--basetemp`] is used to put any temporary files and directories in a numbered directory prefixed with "runpytest-" to not conflict with the normal numbered pytest location for temporary files and directories.

    Parameters[:]

    :   -   **args** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The sequence of arguments to pass to the pytest subprocess.

        -   **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *\|* *None*) -- The period in seconds after which to timeout and raise [[`Pytester.TimeoutExpired`]](#pytest.Pytester.TimeoutExpired "pytest.Pytester.TimeoutExpired").

    Returns[:]

    :   The result.

    Return type[:]

    :   [*RunResult*](#pytest.RunResult "_pytest.pytester.RunResult")

```
<!-- -->
```

[[spawn_pytest]][(]*[[string]]*, *[[expect_timeout]][[=]][[10.0]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.spawn_pytest)[¶](#pytest.Pytester.spawn_pytest "Link to this definition")

:   Run pytest using pexpect.

    This makes sure to use the right pytest and sets up the temporary directory locations.

    The pexpect child is returned.

```
<!-- -->
```

[[spawn]][(]*[[cmd]]*, *[[expect_timeout]][[=]][[10.0]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#Pytester.spawn)[¶](#pytest.Pytester.spawn "Link to this definition")

:   Run a command using pexpect.

    The pexpect child is returned.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[RunResult]][[[\[source\]]]](../_modules/_pytest/pytester.html#RunResult)[¶](#pytest.RunResult "Link to this definition")

:   The result of running a command from [[`Pytester`]](#pytest.Pytester "pytest.Pytester").

```
<!-- -->
```

[[ret]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[ExitCode]](#pytest.ExitCode "pytest.ExitCode")*[¶](#pytest.RunResult.ret "Link to this definition")

:   The return value.

```
<!-- -->
```

[[outlines]][¶](#pytest.RunResult.outlines "Link to this definition")

:   List of lines captured from stdout.

```
<!-- -->
```

[[errlines]][¶](#pytest.RunResult.errlines "Link to this definition")

:   List of lines captured from stderr.

```
<!-- -->
```

[[stdout]][¶](#pytest.RunResult.stdout "Link to this definition")

:   [[`LineMatcher`]](#pytest.LineMatcher "pytest.LineMatcher") of stdout.

    Use e.g. [[`str(stdout)`]](#pytest.LineMatcher.__str__ "pytest.LineMatcher.__str__") to reconstruct stdout, or the commonly used [[`stdout.fnmatch_lines()`]](#pytest.LineMatcher.fnmatch_lines "pytest.LineMatcher.fnmatch_lines") method.

```
<!-- -->
```

[[stderr]][¶](#pytest.RunResult.stderr "Link to this definition")

:   [[`LineMatcher`]](#pytest.LineMatcher "pytest.LineMatcher") of stderr.

```
<!-- -->
```

[[duration]][¶](#pytest.RunResult.duration "Link to this definition")

:   Duration in seconds.

```
<!-- -->
```

[[parseoutcomes]][(][)][[[\[source\]]]](../_modules/_pytest/pytester.html#RunResult.parseoutcomes)[¶](#pytest.RunResult.parseoutcomes "Link to this definition")

:   Return a dictionary of outcome noun -\> count from parsing the terminal output that the test process produced.

    The returned nouns will always be in plural form:

    ::: 
    ::: highlight
        ======= 1 failed, 1 passed, 1 warning, 1 error in 0.13s ====
    :::
    :::

    Will return [`]` `[`1,`]` `[`"passed":`]` `[`1,`]` `[`"warnings":`]` `[`1,`]` `[`"errors":`]` `[`1}`].

```
<!-- -->
```

*[classmethod]* [[parse_summary_nouns]][(]*[[lines]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#RunResult.parse_summary_nouns)[¶](#pytest.RunResult.parse_summary_nouns "Link to this definition")

:   Extract the nouns from a pytest terminal summary line.

    It always returns the plural noun for consistency:

    ::: 
    ::: highlight
        ======= 1 failed, 1 passed, 1 warning, 1 error in 0.13s ====
    :::
    :::

    Will return [`]` `[`1,`]` `[`"passed":`]` `[`1,`]` `[`"warnings":`]` `[`1,`]` `[`"errors":`]` `[`1}`].

```
<!-- -->
```

[[assert_outcomes]][(]*[[passed]][[=]][[0]]*, *[[skipped]][[=]][[0]]*, *[[failed]][[=]][[0]]*, *[[errors]][[=]][[0]]*, *[[xpassed]][[=]][[0]]*, *[[xfailed]][[=]][[0]]*, *[[warnings]][[=]][[None]]*, *[[deselected]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#RunResult.assert_outcomes)[¶](#pytest.RunResult.assert_outcomes "Link to this definition")

:   Assert that the specified outcomes appear with the respective numbers (0 means it didn't occur) in the text output from a test run.

    [`warnings`] and [`deselected`] are only checked if not None.

```
<!-- -->
```

*[[class]][ ]*[[LineMatcher]][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher)[¶](#pytest.LineMatcher "Link to this definition")

:   Flexible matching of text.

    This is a convenience class to test large texts like the output of commands.

    The constructor takes a list of lines without their trailing newlines, i.e. [`text.splitlines()`].

```
<!-- -->
```

[[\_\_str\_\_]][(][)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.__str__)[¶](#pytest.LineMatcher.__str__ "Link to this definition")

:   Return the entire original text.

    ::: versionadded
    [Added in version 6.2: ]You can use [[`str()`]](#pytest.LineMatcher.str "pytest.LineMatcher.str") in older versions.
    :::

```
<!-- -->
```

[[fnmatch_lines_random]][(]*[[lines2]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.fnmatch_lines_random)[¶](#pytest.LineMatcher.fnmatch_lines_random "Link to this definition")

:   Check lines exist in the output in any order (using [[`fnmatch.fnmatch()`]](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.14)")).

```
<!-- -->
```

[[re_match_lines_random]][(]*[[lines2]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.re_match_lines_random)[¶](#pytest.LineMatcher.re_match_lines_random "Link to this definition")

:   Check lines exist in the output in any order (using [[`re.match()`]](https://docs.python.org/3/library/re.html#re.match "(in Python v3.14)")).

```
<!-- -->
```

[[get_lines_after]][(]*[[fnline]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.get_lines_after)[¶](#pytest.LineMatcher.get_lines_after "Link to this definition")

:   Return all lines following the given line in the text.

    The given line can contain glob wildcards.

```
<!-- -->
```

[[fnmatch_lines]][(]*[[lines2]]*, *[[\*]]*, *[[consecutive]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.fnmatch_lines)[¶](#pytest.LineMatcher.fnmatch_lines "Link to this definition")

:   Check lines exist in the output (using [[`fnmatch.fnmatch()`]](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.14)")).

    The argument is a list of lines which have to match and can use glob wildcards. If they do not match a pytest.fail() is called. The matches and non-matches are also shown as part of the error message.

    Parameters[:]

    :   -   **lines2** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- String patterns to match.

        -   **consecutive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Match lines consecutively?

```
<!-- -->
```

[[re_match_lines]][(]*[[lines2]]*, *[[\*]]*, *[[consecutive]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.re_match_lines)[¶](#pytest.LineMatcher.re_match_lines "Link to this definition")

:   Check lines exist in the output (using [[`re.match()`]](https://docs.python.org/3/library/re.html#re.match "(in Python v3.14)")).

    The argument is a list of lines which have to match using [`re.match`]. If they do not match a pytest.fail() is called.

    The matches and non-matches are also shown as part of the error message.

    Parameters[:]

    :   -   **lines2** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- string patterns to match.

        -   **consecutive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- match lines consecutively?

```
<!-- -->
```

[[no_fnmatch_line]][(]*[[pat]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.no_fnmatch_line)[¶](#pytest.LineMatcher.no_fnmatch_line "Link to this definition")

:   Ensure captured lines do not match the given pattern, using [`fnmatch.fnmatch`].

    Parameters[:]

    :   **pat** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The pattern to match lines.

```
<!-- -->
```

[[no_re_match_line]][(]*[[pat]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.no_re_match_line)[¶](#pytest.LineMatcher.no_re_match_line "Link to this definition")

:   Ensure captured lines do not match the given pattern, using [`re.match`].

    Parameters[:]

    :   **pat** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The regular expression to match lines.

```
<!-- -->
```

[[str]][(][)][[[\[source\]]]](../_modules/_pytest/pytester.html#LineMatcher.str)[¶](#pytest.LineMatcher.str "Link to this definition")

:   Return the entire original text.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[HookRecorder]][[[\[source\]]]](../_modules/_pytest/pytester.html#HookRecorder)[¶](#pytest.HookRecorder "Link to this definition")

:   Record all hooks called in a plugin manager.

    Hook recorders are created by [[`Pytester`]](#pytest.Pytester "pytest.Pytester").

    This wraps all the hook calls in the plugin manager, recording each call before propagating the normal calls.

```
<!-- -->
```

[[getcalls]][(]*[[names]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#HookRecorder.getcalls)[¶](#pytest.HookRecorder.getcalls "Link to this definition")

:   Get all recorded calls to hooks with the given names (or name).

```
<!-- -->
```

[[matchreport]][(]*[[inamepart]][[=]][[\'\']]*, *[[names]][[=]][[(\'pytest_runtest_logreport\',] [\'pytest_collectreport\')]]*, *[[when]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/pytester.html#HookRecorder.matchreport)[¶](#pytest.HookRecorder.matchreport "Link to this definition")

:   Return a testreport whose dotted import path matches.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[RecordedHookCall]][[[\[source\]]]](../_modules/_pytest/pytester.html#RecordedHookCall)[¶](#pytest.RecordedHookCall "Link to this definition")

:   A recorded call to a hook.

    The arguments to the hook call are set as attributes. For example:

    ::: 
    ::: highlight
        calls = hook_recorder.getcalls("pytest_runtest_setup")
        # Suppose pytest_runtest_setup was called once with `item=an_item`.
        assert calls[0].item is an_item
    :::
    :::

[]

### record_property[¶](#record-property "Link to this heading")

**Tutorial**: [[record_property]](../how-to/output.html#record-property-example)

[[record_property]][(][)][[[\[source\]]]](../_modules/_pytest/junitxml.html#record_property)[¶](#pytest.junitxml.record_property "Link to this definition")

:   Add extra properties to the calling test.

    User properties become part of the test report and are available to the configured reporters, like JUnit XML.

    The fixture is callable with [`name,`]` `[`value`]. The value is automatically XML-encoded.

    Example:

    ::: 
    ::: highlight
        def test_function(record_property):
            record_property("example_key", 1)
    :::
    :::

[]

### record_testsuite_property[¶](#record-testsuite-property "Link to this heading")

**Tutorial**: [[record_testsuite_property]](../how-to/output.html#record-testsuite-property-example)

[[record_testsuite_property]][(][)][[[\[source\]]]](../_modules/_pytest/junitxml.html#record_testsuite_property)[¶](#pytest.junitxml.record_testsuite_property "Link to this definition")

:   Record a new [`<property>`] tag as child of the root [`<testsuite>`].

    This is suitable to writing global information regarding the entire test suite, and is compatible with [`xunit2`] JUnit family.

    This is a [`session`]-scoped fixture which is called with [`(name,`]` `[`value)`]. Example:

    ::: 
    ::: highlight
        def test_foo(record_testsuite_property):
            record_testsuite_property("ARCH", "PPC")
            record_testsuite_property("STORAGE_TYPE", "CEPH")
    :::
    :::

    Parameters[:]

    :   -   **name** -- The property name.

        -   **value** -- The property value. Will be converted to a string.

    ::: 
    Warning

    Currently this fixture **does not work** with the [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) plugin. See [#7767](https://github.com/pytest-dev/pytest/issues/7767) for details.
    :::

[]

### recwarn[¶](#recwarn "Link to this heading")

**Tutorial**: [[Recording warnings]](../how-to/capture-warnings.html#recwarn)

[[recwarn]][(][)][[[\[source\]]]](../_modules/_pytest/recwarn.html#recwarn)[¶](#pytest.recwarn.recwarn "Link to this definition")

:   Return a [[`WarningsRecorder`]](#pytest.WarningsRecorder "_pytest.recwarn.WarningsRecorder") instance that records all warnings emitted by test functions.

    See [[How to capture warnings]](../how-to/capture-warnings.html#warnings) for information on warning categories.

```
<!-- -->
```

*[[class]][ ]*[[WarningsRecorder]][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder)[¶](#pytest.WarningsRecorder "Link to this definition")

:   A context manager to record raised warnings.

    Each recorded warning is an instance of [`warnings.WarningMessage`].

    Adapted from [`warnings.catch_warnings`].

    ::: 
    Note

    [`DeprecationWarning`] and [`PendingDeprecationWarning`] are treated differently; see [[Ensuring code triggers a deprecation warning]](../how-to/capture-warnings.html#ensuring-function-triggers).
    :::

```
<!-- -->
```

*[[property]][ ]*[[list]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][WarningMessage][[\]]]*[¶](#pytest.WarningsRecorder.list "Link to this definition")

:   The list of recorded warnings.

```
<!-- -->
```

[[\_\_getitem\_\_]][(]*[[i]]*[)][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder.__getitem__)[¶](#pytest.WarningsRecorder.__getitem__ "Link to this definition")

:   Get a recorded warning by index.

```
<!-- -->
```

[[\_\_iter\_\_]][(][)][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder.__iter__)[¶](#pytest.WarningsRecorder.__iter__ "Link to this definition")

:   Iterate through the recorded warnings.

```
<!-- -->
```

[[\_\_len\_\_]][(][)][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder.__len__)[¶](#pytest.WarningsRecorder.__len__ "Link to this definition")

:   The number of recorded warnings.

```
<!-- -->
```

[[pop]][(]*[[cls=\<class] [\'Warning\'\>]]*[)][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder.pop)[¶](#pytest.WarningsRecorder.pop "Link to this definition")

:   Pop the first recorded warning which is an instance of [`cls`], but not an instance of a child class of any other match. Raises [`AssertionError`] if there is no match.

```
<!-- -->
```

[[clear]][(][)][[[\[source\]]]](../_modules/_pytest/recwarn.html#WarningsRecorder.clear)[¶](#pytest.WarningsRecorder.clear "Link to this definition")

:   Clear the list of recorded warnings.

[]

### request[¶](#request "Link to this heading")

**Example**: [[Pass different values to a test function, depending on command line options]](../example/simple.html#request-example)

The [`request`] fixture is a special fixture providing information of the requesting test function.

*[[class]][ ]*[[FixtureRequest]][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureRequest)[¶](#pytest.FixtureRequest "Link to this definition")

:   The type of the [`request`] fixture.

    A request object gives access to the requesting test context and has a [`param`] attribute in case the fixture is parametrized.

```
<!-- -->
```

[[fixturename]]*[[:]][ ][[Final]](https://docs.python.org/3/library/typing.html#typing.Final "(in Python v3.14)")*[¶](#pytest.FixtureRequest.fixturename "Link to this definition")

:   Fixture for which this request is being performed.

```
<!-- -->
```

*[[property]][ ]*[[scope]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]]*[¶](#pytest.FixtureRequest.scope "Link to this definition")

:   Scope string, one of "function", "class", "module", "package", "session".

```
<!-- -->
```

*[[property]][ ]*[[fixturenames]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#pytest.FixtureRequest.fixturenames "Link to this definition")

:   Names of all active fixtures in this request.

```
<!-- -->
```

*[[abstract]][ ][[property]][ ]*[[node]][¶](#pytest.FixtureRequest.node "Link to this definition")

:   Underlying collection node (depends on current request scope).

```
<!-- -->
```

*[[property]][ ]*[[config]]*[[:]][ ][[Config]](#pytest.Config "_pytest.config.Config")*[¶](#pytest.FixtureRequest.config "Link to this definition")

:   The pytest config object associated with this request.

```
<!-- -->
```

*[[property]][ ]*[[function]][¶](#pytest.FixtureRequest.function "Link to this definition")

:   Test function object if the request has a per-function scope.

```
<!-- -->
```

*[[property]][ ]*[[cls]][¶](#pytest.FixtureRequest.cls "Link to this definition")

:   Class (can be None) where the test function was collected.

```
<!-- -->
```

*[[property]][ ]*[[instance]][¶](#pytest.FixtureRequest.instance "Link to this definition")

:   Instance (can be None) on which test function was collected.

```
<!-- -->
```

*[[property]][ ]*[[module]][¶](#pytest.FixtureRequest.module "Link to this definition")

:   Python module object where the test function was collected.

```
<!-- -->
```

*[[property]][ ]*[[path]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.FixtureRequest.path "Link to this definition")

:   Path where the test function was collected.

```
<!-- -->
```

*[[property]][ ]*[[keywords]]*[[:]][ ][[MutableMapping]](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]*[¶](#pytest.FixtureRequest.keywords "Link to this definition")

:   Keywords/markers dictionary for the underlying node.

```
<!-- -->
```

*[[property]][ ]*[[session]]*[[:]][ ][[Session]](#pytest.Session "_pytest.main.Session")*[¶](#pytest.FixtureRequest.session "Link to this definition")

:   Pytest session object.

```
<!-- -->
```

*[abstractmethod]* [[addfinalizer]][(]*[[finalizer]]*[)][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureRequest.addfinalizer)[¶](#pytest.FixtureRequest.addfinalizer "Link to this definition")

:   Add finalizer/teardown function to be called without arguments after the last test within the requesting test context finished execution.

```
<!-- -->
```

[[applymarker]][(]*[[marker]]*[)][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureRequest.applymarker)[¶](#pytest.FixtureRequest.applymarker "Link to this definition")

:   Apply a marker to a single test function invocation.

    This method is useful if you don't want to have a keyword/marker on all function invocations.

    Parameters[:]

    :   **marker** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*MarkDecorator*](#pytest.MarkDecorator "_pytest.mark.structures.MarkDecorator")) -- An object created by a call to [`pytest.mark.NAME(...)`].

```
<!-- -->
```

[[raiseerror]][(]*[[msg]]*[)][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureRequest.raiseerror)[¶](#pytest.FixtureRequest.raiseerror "Link to this definition")

:   Raise a FixtureLookupError exception.

    Parameters[:]

    :   **msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- An optional custom error message.

```
<!-- -->
```

[[getfixturevalue]][(]*[[argname]]*[)][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureRequest.getfixturevalue)[¶](#pytest.FixtureRequest.getfixturevalue "Link to this definition")

:   Dynamically run a named fixture function.

    Declaring fixtures via function argument is recommended where possible. But if you can only decide whether to use another fixture at test setup time, you may use this function to retrieve it inside a fixture or test function body.

    This method can be used during the test setup phase or the test run phase, but during the test teardown phase a fixture's value may not be available.

    Parameters[:]

    :   **argname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The fixture name.

    Raises[:]

    :   [**pytest.FixtureLookupError**](#pytest.FixtureLookupError "pytest.FixtureLookupError") -- If the given fixture could not be found.

[]

### subtests[¶](#subtests "Link to this heading")

The [`subtests`] fixture enables declaring subtests inside test functions.

**Tutorial**: [[How to use subtests]](../how-to/subtests.html#subtests)

*[[class]][ ]*[[Subtests]][[[\[source\]]]](../_modules/_pytest/subtests.html#Subtests)[¶](#pytest.Subtests "Link to this definition")

:   Subtests fixture, enables declaring subtests inside test functions via the [[`test()`]](#pytest.Subtests.test "pytest.Subtests.test") method.

```
<!-- -->
```

[[test]][(]*[[msg]][[=]][[None]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/subtests.html#Subtests.test)[¶](#pytest.Subtests.test "Link to this definition")

:   Context manager for subtests, capturing exceptions raised inside the subtest scope and reporting assertion failures and errors individually.

    ::: 
    #### Usage[¶](#usage "Link to this heading")

    ::: 
    ::: highlight
        def test(subtests):
            for i in range(5):
                with subtests.test("custom message", i=i):
                    assert i % 2 == 0
    :::
    :::

    param msg[:]

    :   If given, the message will be shown in the test report in case of subtest failure.

    param kwargs[:]

    :   Arbitrary values that are also added to the subtest report.
    :::

[]

### testdir[¶](#testdir "Link to this heading")

Identical to [[`pytester`]](#std-fixture-pytester), but provides an instance whose methods return legacy [`py.path.local`] objects instead when applicable.

New code should avoid using [[`testdir`]](#std-fixture-testdir) in favor of [[`pytester`]](#std-fixture-pytester).

*[[final]][ ][[class]][ ]*[[Testdir]][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir)

:   Similar to [[`Pytester`]](#pytest.Pytester "pytest.Pytester"), but this class works with legacy legacy_path objects instead.

    All methods just forward to an internal [[`Pytester`]](#pytest.Pytester "pytest.Pytester") instance, converting results to [`legacy_path`] objects as necessary.

```
<!-- -->
```

*[[exception]][ ]*[[TimeoutExpired]]

:   

```
<!-- -->
```

*[[property]][ ]*[[tmpdir]]*[[:]][ ][LocalPath]*

:   Temporary directory where tests are executed.

```
<!-- -->
```

[[make_hook_recorder]][(]*[[pluginmanager]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.make_hook_recorder)

:   See [[`Pytester.make_hook_recorder()`]](#pytest.Pytester.make_hook_recorder "pytest.Pytester.make_hook_recorder").

```
<!-- -->
```

[[chdir]][(][)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.chdir)

:   See [[`Pytester.chdir()`]](#pytest.Pytester.chdir "pytest.Pytester.chdir").

```
<!-- -->
```

[[makefile]][(]*[[ext]]*, *[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.makefile)

:   See [[`Pytester.makefile()`]](#pytest.Pytester.makefile "pytest.Pytester.makefile").

```
<!-- -->
```

[[makeconftest]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.makeconftest)

:   See [[`Pytester.makeconftest()`]](#pytest.Pytester.makeconftest "pytest.Pytester.makeconftest").

```
<!-- -->
```

[[makeini]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.makeini)

:   See [[`Pytester.makeini()`]](#pytest.Pytester.makeini "pytest.Pytester.makeini").

```
<!-- -->
```

[[getinicfg]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getinicfg)

:   See [[`Pytester.getinicfg()`]](#pytest.Pytester.getinicfg "pytest.Pytester.getinicfg").

```
<!-- -->
```

[[makepyprojecttoml]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.makepyprojecttoml)

:   See [[`Pytester.makepyprojecttoml()`]](#pytest.Pytester.makepyprojecttoml "pytest.Pytester.makepyprojecttoml").

```
<!-- -->
```

[[makepyfile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.makepyfile)

:   See [[`Pytester.makepyfile()`]](#pytest.Pytester.makepyfile "pytest.Pytester.makepyfile").

```
<!-- -->
```

[[maketxtfile]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.maketxtfile)

:   See [[`Pytester.maketxtfile()`]](#pytest.Pytester.maketxtfile "pytest.Pytester.maketxtfile").

```
<!-- -->
```

[[syspathinsert]][(]*[[path]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.syspathinsert)

:   See [[`Pytester.syspathinsert()`]](#pytest.Pytester.syspathinsert "pytest.Pytester.syspathinsert").

```
<!-- -->
```

[[mkdir]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.mkdir)

:   See [[`Pytester.mkdir()`]](#pytest.Pytester.mkdir "pytest.Pytester.mkdir").

```
<!-- -->
```

[[mkpydir]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.mkpydir)

:   See [[`Pytester.mkpydir()`]](#pytest.Pytester.mkpydir "pytest.Pytester.mkpydir").

```
<!-- -->
```

[[copy_example]][(]*[[name]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.copy_example)

:   See [[`Pytester.copy_example()`]](#pytest.Pytester.copy_example "pytest.Pytester.copy_example").

```
<!-- -->
```

[[getnode]][(]*[[config]]*, *[[arg]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getnode)

:   See [[`Pytester.getnode()`]](#pytest.Pytester.getnode "pytest.Pytester.getnode").

```
<!-- -->
```

[[getpathnode]][(]*[[path]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getpathnode)

:   See [[`Pytester.getpathnode()`]](#pytest.Pytester.getpathnode "pytest.Pytester.getpathnode").

```
<!-- -->
```

[[genitems]][(]*[[colitems]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.genitems)

:   See [[`Pytester.genitems()`]](#pytest.Pytester.genitems "pytest.Pytester.genitems").

```
<!-- -->
```

[[runitem]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runitem)

:   See [[`Pytester.runitem()`]](#pytest.Pytester.runitem "pytest.Pytester.runitem").

```
<!-- -->
```

[[inline_runsource]][(]*[[source]]*, *[[\*]][[cmdlineargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.inline_runsource)

:   See [[`Pytester.inline_runsource()`]](#pytest.Pytester.inline_runsource "pytest.Pytester.inline_runsource").

```
<!-- -->
```

[[inline_genitems]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.inline_genitems)

:   See [[`Pytester.inline_genitems()`]](#pytest.Pytester.inline_genitems "pytest.Pytester.inline_genitems").

```
<!-- -->
```

[[inline_run]][(]*[[\*]][[args]]*, *[[plugins]][[=]][[()]]*, *[[no_reraise_ctrlc]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.inline_run)

:   See [[`Pytester.inline_run()`]](#pytest.Pytester.inline_run "pytest.Pytester.inline_run").

```
<!-- -->
```

[[runpytest_inprocess]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runpytest_inprocess)

:   See [[`Pytester.runpytest_inprocess()`]](#pytest.Pytester.runpytest_inprocess "pytest.Pytester.runpytest_inprocess").

```
<!-- -->
```

[[runpytest]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runpytest)

:   See [[`Pytester.runpytest()`]](#pytest.Pytester.runpytest "pytest.Pytester.runpytest").

```
<!-- -->
```

[[parseconfig]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.parseconfig)

:   See [[`Pytester.parseconfig()`]](#pytest.Pytester.parseconfig "pytest.Pytester.parseconfig").

```
<!-- -->
```

[[parseconfigure]][(]*[[\*]][[args]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.parseconfigure)

:   See [[`Pytester.parseconfigure()`]](#pytest.Pytester.parseconfigure "pytest.Pytester.parseconfigure").

```
<!-- -->
```

[[getitem]][(]*[[source]]*, *[[funcname]][[=]][[\'test_func\']]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getitem)

:   See [[`Pytester.getitem()`]](#pytest.Pytester.getitem "pytest.Pytester.getitem").

```
<!-- -->
```

[[getitems]][(]*[[source]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getitems)

:   See [[`Pytester.getitems()`]](#pytest.Pytester.getitems "pytest.Pytester.getitems").

```
<!-- -->
```

[[getmodulecol]][(]*[[source]]*, *[[configargs]][[=]][[()]]*, *[[withinit]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.getmodulecol)

:   See [[`Pytester.getmodulecol()`]](#pytest.Pytester.getmodulecol "pytest.Pytester.getmodulecol").

```
<!-- -->
```

[[collect_by_name]][(]*[[modcol]]*, *[[name]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.collect_by_name)

:   See [[`Pytester.collect_by_name()`]](#pytest.Pytester.collect_by_name "pytest.Pytester.collect_by_name").

```
<!-- -->
```

[[popen]][(]*[[cmdargs]]*, *[[stdout]][[=]][[-1]]*, *[[stderr]][[=]][[-1]]*, *[[stdin]][[=]][[NotSetType.token]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.popen)

:   See [[`Pytester.popen()`]](#pytest.Pytester.popen "pytest.Pytester.popen").

```
<!-- -->
```

[[run]][(]*[[\*]][[cmdargs]]*, *[[timeout]][[=]][[None]]*, *[[stdin]][[=]][[NotSetType.token]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.run)

:   See [[`Pytester.run()`]](#pytest.Pytester.run "pytest.Pytester.run").

```
<!-- -->
```

[[runpython]][(]*[[script]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runpython)

:   See [[`Pytester.runpython()`]](#pytest.Pytester.runpython "pytest.Pytester.runpython").

```
<!-- -->
```

[[runpython_c]][(]*[[command]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runpython_c)

:   See [[`Pytester.runpython_c()`]](#pytest.Pytester.runpython_c "pytest.Pytester.runpython_c").

```
<!-- -->
```

[[runpytest_subprocess]][(]*[[\*]][[args]]*, *[[timeout]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.runpytest_subprocess)

:   See [[`Pytester.runpytest_subprocess()`]](#pytest.Pytester.runpytest_subprocess "pytest.Pytester.runpytest_subprocess").

```
<!-- -->
```

[[spawn_pytest]][(]*[[string]]*, *[[expect_timeout]][[=]][[10.0]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.spawn_pytest)

:   See [[`Pytester.spawn_pytest()`]](#pytest.Pytester.spawn_pytest "pytest.Pytester.spawn_pytest").

```
<!-- -->
```

[[spawn]][(]*[[cmd]]*, *[[expect_timeout]][[=]][[10.0]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#Testdir.spawn)

:   See [[`Pytester.spawn()`]](#pytest.Pytester.spawn "pytest.Pytester.spawn").

[]

### tmp_path[¶](#tmp-path "Link to this heading")

**Tutorial**: [[How to use temporary directories and files in tests]](../how-to/tmp_path.html#tmp-path)

[[tmp_path]][(][)][[[\[source\]]]](../_modules/_pytest/tmpdir.html#tmp_path)[¶](#pytest.tmpdir.tmp_path "Link to this definition")

:   Return a temporary directory (as [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") object) which is unique to each test function invocation. The temporary directory is created as a subdirectory of the base temporary directory, with configurable retention, as discussed in [[Temporary directory location and retention]](../how-to/tmp_path.html#temporary-directory-location-and-retention).

[]

### tmp_path_factory[¶](#tmp-path-factory "Link to this heading")

**Tutorial**: [[The tmp_path_factory fixture]](../how-to/tmp_path.html#tmp-path-factory-example)

[`tmp_path_factory`] is an instance of [[`TempPathFactory`]](#pytest.TempPathFactory "pytest.TempPathFactory"):

*[[final]][ ][[class]][ ]*[[TempPathFactory]][[[\[source\]]]](../_modules/_pytest/tmpdir.html#TempPathFactory)[¶](#pytest.TempPathFactory "Link to this definition")

:   Factory for temporary directories under the common base temp directory, as discussed at [[Temporary directory location and retention]](../how-to/tmp_path.html#temporary-directory-location-and-retention).

```
<!-- -->
```

[[mktemp]][(]*[[basename]]*, *[[numbered]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/tmpdir.html#TempPathFactory.mktemp)[¶](#pytest.TempPathFactory.mktemp "Link to this definition")

:   Create a new temporary directory managed by the factory.

    Parameters[:]

    :   -   **basename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Directory base name, must be a relative path.

        -   **numbered** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`], ensure the directory is unique by adding a numbered suffix greater than any existing one: [`basename="foo-"`] and [`numbered=True`] means that this function will create directories named [`"foo-0"`], [`"foo-1"`], [`"foo-2"`] and so on.

    Returns[:]

    :   The path to the new directory.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

```
<!-- -->
```

[[getbasetemp]][(][)][[[\[source\]]]](../_modules/_pytest/tmpdir.html#TempPathFactory.getbasetemp)[¶](#pytest.TempPathFactory.getbasetemp "Link to this definition")

:   Return the base temporary directory, creating it if needed.

    Returns[:]

    :   The base temporary directory.

    Return type[:]

    :   [*Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

[]

### tmpdir[¶](#tmpdir "Link to this heading")

**Tutorial**: [[The tmpdir and tmpdir_factory fixtures]](../how-to/tmp_path.html#tmpdir-and-tmpdir-factory)

[[tmpdir]][(][)][¶](#pytest.legacypath.LegacyTmpdirPlugin.tmpdir "Link to this definition")

:   Return a temporary directory (as [legacy_path](https://py.readthedocs.io/en/latest/path.html) object) which is unique to each test function invocation. The temporary directory is created as a subdirectory of the base temporary directory, with configurable retention, as discussed in [[Temporary directory location and retention]](../how-to/tmp_path.html#temporary-directory-location-and-retention).

    ::: 
    Note

    These days, it is preferred to use [`tmp_path`].

    [[About the tmpdir and tmpdir_factory fixtures]](../how-to/tmp_path.html#tmpdir-and-tmpdir-factory).
    :::

[]

### tmpdir_factory[¶](#tmpdir-factory "Link to this heading")

**Tutorial**: [[The tmpdir and tmpdir_factory fixtures]](../how-to/tmp_path.html#tmpdir-and-tmpdir-factory)

[`tmpdir_factory`] is an instance of [[`TempdirFactory`]](#pytest.TempdirFactory "pytest.TempdirFactory"):

*[[final]][ ][[class]][ ]*[[TempdirFactory]][[[\[source\]]]](../_modules/_pytest/legacypath.html#TempdirFactory)[¶](#pytest.TempdirFactory "Link to this definition")

:   Backward compatibility wrapper that implements [`py.path.local`] for [[`TempPathFactory`]](#pytest.TempPathFactory "pytest.TempPathFactory").

    ::: 
    Note

    These days, it is preferred to use [`tmp_path_factory`].

    [[About the tmpdir and tmpdir_factory fixtures]](../how-to/tmp_path.html#tmpdir-and-tmpdir-factory).
    :::

```
<!-- -->
```

[[mktemp]][(]*[[basename]]*, *[[numbered]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/legacypath.html#TempdirFactory.mktemp)[¶](#pytest.TempdirFactory.mktemp "Link to this definition")

:   Same as [[`TempPathFactory.mktemp()`]](#pytest.TempPathFactory.mktemp "pytest.TempPathFactory.mktemp"), but returns a [`py.path.local`] object.

```
<!-- -->
```

[[getbasetemp]][(][)][[[\[source\]]]](../_modules/_pytest/legacypath.html#TempdirFactory.getbasetemp)[¶](#pytest.TempdirFactory.getbasetemp "Link to this definition")

:   Same as [[`TempPathFactory.getbasetemp()`]](#pytest.TempPathFactory.getbasetemp "pytest.TempPathFactory.getbasetemp"), but returns a [`py.path.local`] object.

[]

## Hooks[¶](#hooks "Link to this heading")

**Tutorial**: [[Writing plugins]](../how-to/writing_plugins.html#writing-plugins)

Reference to all hooks which can be implemented by [[conftest.py files]](../how-to/writing_plugins.html#localplugin) and [[plugins]](../how-to/writing_plugins.html#plugins).

### \@pytest.hookimpl[¶](#pytest-hookimpl "Link to this heading")

[[@]][[pytest.]][[hookimpl]][¶](#pytest.hookimpl "Link to this definition")

:   pytest's decorator for marking functions as hook implementations.

    See [[Writing hook functions]](../how-to/writing_hook_functions.html#writinghooks) and [[`pluggy.HookimplMarker()`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.HookimplMarker "(in pluggy v0.1)").

### \@pytest.hookspec[¶](#pytest-hookspec "Link to this heading")

[[@]][[pytest.]][[hookspec]][¶](#pytest.hookspec "Link to this definition")

:   pytest's decorator for marking functions as hook specifications.

    See [[Declaring new hooks]](../how-to/writing_hook_functions.html#declaringhooks) and [[`pluggy.HookspecMarker()`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.HookspecMarker "(in pluggy v0.1)").

### Bootstrapping hooks[¶](#bootstrapping-hooks "Link to this heading")

Bootstrapping hooks called for plugins registered early enough (internal and third-party plugins).

[[pytest_load_initial_conftests]][(]*[[early_config]]*, *[[parser]]*, *[[args]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_load_initial_conftests)[¶](#pytest.hookspec.pytest_load_initial_conftests "Link to this definition")

:   Called to implement the loading of [[initial conftest files]](../how-to/writing_plugins.html#pluginorder) ahead of command line option parsing.

    Parameters[:]

    :   -   **early_config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **args** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- Arguments passed on the command line.

        -   **parser** ([*Parser*](#pytest.Parser "pytest.Parser")) -- To add command line options.

    ::: 
    #### Use in conftest plugins[¶](#use-in-conftest-plugins "Link to this heading")

    This hook is not called for conftest files.
    :::

```
<!-- -->
```

[[pytest_cmdline_parse]][(]*[[pluginmanager]]*, *[[args]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_cmdline_parse)[¶](#pytest.hookspec.pytest_cmdline_parse "Link to this definition")

:   Return an initialized [[`Config`]](#pytest.Config "pytest.Config"), parsing the specified args.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    ::: 
    Note

    This hook is only called for plugin classes passed to the [`plugins`] arg when using [pytest.main](#pytest-main) to perform an in-process test run.
    :::

    Parameters[:]

    :   -   **pluginmanager** ([*PytestPluginManager*](#pytest.PytestPluginManager "pytest.PytestPluginManager")) -- The pytest plugin manager.

        -   **args** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- List of arguments passed on the command line.

    Returns[:]

    :   A pytest config object.

    Return type[:]

    :   [Config](#pytest.Config "pytest.Config") \| None

    ::: 
    #### Use in conftest plugins[¶](#id2 "Link to this heading")

    This hook is not called for conftest files.
    :::

```
<!-- -->
```

[[pytest_cmdline_main]][(]*[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_cmdline_main)[¶](#pytest.hookspec.pytest_cmdline_main "Link to this definition")

:   Called for performing the main command line action.

    The default implementation will invoke the configure hooks and [[`pytest_runtestloop`]](#std-hook-pytest_runtestloop).

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    Returns[:]

    :   The exit code.

    Return type[:]

    :   [ExitCode](#pytest.ExitCode "pytest.ExitCode") \| [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") \| None

    ::: 
    #### Use in conftest plugins[¶](#id3 "Link to this heading")

    This hook is only called for [[initial conftests]](../how-to/writing_plugins.html#pluginorder).
    :::

[]

### Initialization hooks[¶](#initialization-hooks "Link to this heading")

Initialization hooks called for plugins and [`conftest.py`] files.

[[pytest_addoption]][(]*[[parser]]*, *[[pluginmanager]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_addoption)[¶](#pytest.hookspec.pytest_addoption "Link to this definition")

:   Register argparse-style options and config-style config values, called once at the beginning of a test run.

    Parameters[:]

    :   -   **parser** ([*Parser*](#pytest.Parser "pytest.Parser")) -- To add command line options, call [[`parser.addoption(...)`]](#pytest.Parser.addoption "pytest.Parser.addoption"). To add config-file values call [[`parser.addini(...)`]](#pytest.Parser.addini "pytest.Parser.addini").

        -   **pluginmanager** ([*PytestPluginManager*](#pytest.PytestPluginManager "pytest.PytestPluginManager")) -- The pytest plugin manager, which can be used to install [[`hookspec()`]](#pytest.hookspec "pytest.hookspec")'s or [[`hookimpl()`]](#pytest.hookimpl "pytest.hookimpl")'s and allow one plugin to call another plugin's hooks to change how command line options are added.

    Options can later be accessed through the [[`config`]](#pytest.Config "pytest.Config") object, respectively:

    -   [[`config.getoption(name)`]](#pytest.Config.getoption "pytest.Config.getoption") to retrieve the value of a command line option.

    -   [[`config.getini(name)`]](#pytest.Config.getini "pytest.Config.getini") to retrieve a value read from a configuration file.

    The config object is passed around on many internal objects via the [`.config`] attribute or can be retrieved as the [`pytestconfig`] fixture.

    ::: 
    Note

    This hook is incompatible with hook wrappers.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id5 "Link to this heading")

    If a conftest plugin implements this hook, it will be called immediately when the conftest is registered.

    This hook is only called for [[initial conftests]](../how-to/writing_plugins.html#pluginorder).
    :::

```
<!-- -->
```

[[pytest_addhooks]][(]*[[pluginmanager]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_addhooks)[¶](#pytest.hookspec.pytest_addhooks "Link to this definition")

:   Called at plugin registration time to allow adding new hooks via a call to [[`pluginmanager.add_hookspecs(module_or_class,`]` `[`prefix)`]](#pytest.PytestPluginManager.add_hookspecs "pytest.PytestPluginManager.add_hookspecs").

    Parameters[:]

    :   **pluginmanager** ([*PytestPluginManager*](#pytest.PytestPluginManager "pytest.PytestPluginManager")) -- The pytest plugin manager.

    ::: 
    Note

    This hook is incompatible with hook wrappers.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id6 "Link to this heading")

    If a conftest plugin implements this hook, it will be called immediately when the conftest is registered.
    :::

```
<!-- -->
```

[[pytest_configure]][(]*[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_configure)[¶](#pytest.hookspec.pytest_configure "Link to this definition")

:   Allow plugins and conftest files to perform initial configuration.

    ::: 
    Note

    This hook is incompatible with hook wrappers.
    :::

    Parameters[:]

    :   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    ::: 
    #### Use in conftest plugins[¶](#id7 "Link to this heading")

    This hook is called for every [[initial conftest]](../how-to/writing_plugins.html#pluginorder) file after command line options have been parsed. After that, the hook is called for other conftest files as they are registered.
    :::

```
<!-- -->
```

[[pytest_unconfigure]][(]*[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_unconfigure)[¶](#pytest.hookspec.pytest_unconfigure "Link to this definition")

:   Called before test process is exited.

    Parameters[:]

    :   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    ::: 
    #### Use in conftest plugins[¶](#id8 "Link to this heading")

    Any conftest file can implement this hook.
    :::

```
<!-- -->
```

[[pytest_sessionstart]][(]*[[session]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_sessionstart)[¶](#pytest.hookspec.pytest_sessionstart "Link to this definition")

:   Called after the [`Session`] object has been created and before performing collection and entering the run test loop.

    Parameters[:]

    :   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

    ::: 
    #### Use in conftest plugins[¶](#id9 "Link to this heading")

    This hook is only called for [[initial conftests]](../how-to/writing_plugins.html#pluginorder).
    :::

```
<!-- -->
```

[[pytest_sessionfinish]][(]*[[session]]*, *[[exitstatus]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_sessionfinish)[¶](#pytest.hookspec.pytest_sessionfinish "Link to this definition")

:   Called after whole test run finished, right before returning the exit status to the system.

    Parameters[:]

    :   -   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

        -   **exitstatus** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* [*ExitCode*](#pytest.ExitCode "pytest.ExitCode")) -- The status which pytest will return to the system.

    ::: 
    #### Use in conftest plugins[¶](#id10 "Link to this heading")

    Any conftest file can implement this hook.
    :::

```
<!-- -->
```

[[pytest_plugin_registered]][(]*[[plugin]]*, *[[plugin_name]]*, *[[manager]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_plugin_registered)[¶](#pytest.hookspec.pytest_plugin_registered "Link to this definition")

:   A new pytest plugin got registered.

    Parameters[:]

    :   -   **plugin** (*\_PluggyPlugin*) -- The plugin module or instance.

        -   **plugin_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The name by which the plugin is registered.

        -   **manager** ([*PytestPluginManager*](#pytest.PytestPluginManager "pytest.PytestPluginManager")) -- The pytest plugin manager.

    ::: 
    Note

    This hook is incompatible with hook wrappers.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id11 "Link to this heading")

    If a conftest plugin implements this hook, it will be called immediately when the conftest is registered, once for each plugin registered thus far (including itself!), and for all plugins thereafter when they are registered.
    :::

### Collection hooks[¶](#collection-hooks "Link to this heading")

[`pytest`] calls the following hooks for collecting files and directories:

[[pytest_collection]][(]*[[session]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collection)[¶](#pytest.hookspec.pytest_collection "Link to this definition")

:   Perform the collection phase for the given session.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult). The return value is not used, but only stops further processing.

    The default collection phase is this (see individual hooks for full details):

    1.  Starting from [`session`] as the initial collector:

    > <div>
    >
    > 1.  [`pytest_collectstart(collector)`]
    >
    > 2.  [`report`]` `[`=`]` `[`pytest_make_collect_report(collector)`]
    >
    > 3.  [`pytest_exception_interact(collector,`]` `[`call,`]` `[`report)`] if an interactive exception occurred
    >
    > 4.  For each collected node:
    >
    > > <div>
    > >
    > > 1.  If an item, [`pytest_itemcollected(item)`]
    > >
    > > 2.  If a collector, recurse into it.
    > >
    > > </div>
    >
    > 5.  [`pytest_collectreport(report)`]
    >
    > </div>

    2.  [`pytest_collection_modifyitems(session,`]` `[`config,`]` `[`items)`]

    > <div>
    >
    > 1.  [`pytest_deselected(items)`] for any deselected items (may be called multiple times)
    >
    > </div>

    3.  [`pytest_collection_finish(session)`]

    4.  Set [`session.items`] to the list of collected items

    5.  Set [`session.testscollected`] to the number of collected items

    You can implement this hook to only perform some action before collection, for example the terminal plugin uses it to start displaying the collection counter (and returns [`None`]).

    Parameters[:]

    :   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

    ::: 
    #### Use in conftest plugins[¶](#id12 "Link to this heading")

    This hook is only called for [[initial conftests]](../how-to/writing_plugins.html#pluginorder).
    :::

```
<!-- -->
```

[[pytest_ignore_collect]][(]*[[collection_path]]*, *[[path]]*, *[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_ignore_collect)[¶](#pytest.hookspec.pytest_ignore_collect "Link to this definition")

:   Return [`True`] to ignore this path for collection.

    Return [`None`] to let other plugins ignore the path for collection.

    Returning [`False`] will forcefully *not* ignore this path for collection, without giving a chance for other plugins to ignore this path.

    This hook is consulted for all files and directories prior to calling more specific hooks.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   -   **collection_path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The path to analyze.

        -   **path** (*LEGACY_PATH*) -- The path to analyze (deprecated).

        -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    ::: versionchanged
    [Changed in version 7.0.0: ]The [`collection_path`] parameter was added as a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") equivalent of the [`path`] parameter. The [`path`] parameter has been deprecated.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id13 "Link to this heading")

    Any conftest file can implement this hook. For a given collection path, only conftest files in parent directories of the collection path are consulted (if the path is a directory, its own conftest file is *not* consulted - a directory cannot ignore itself!).
    :::

```
<!-- -->
```

[[pytest_collect_directory]][(]*[[path]]*, *[[parent]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collect_directory)[¶](#pytest.hookspec.pytest_collect_directory "Link to this definition")

:   Create a [[`Collector`]](#pytest.Collector "pytest.Collector") for the given directory, or None if not relevant.

    ::: versionadded
    [Added in version 8.0.]
    :::

    For best results, the returned collector should be a subclass of [[`Directory`]](#pytest.Directory "pytest.Directory"), but this is not required.

    The new node needs to have the specified [`parent`] as a parent.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   **path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The path to analyze.

    See [[Using a custom directory collector]](../example/customdirectory.html#custom-directory-collectors) for a simple example of use of this hook.

    ::: 
    #### Use in conftest plugins[¶](#id14 "Link to this heading")

    Any conftest file can implement this hook. For a given collection path, only conftest files in parent directories of the collection path are consulted (if the path is a directory, its own conftest file is *not* consulted - a directory cannot collect itself!).
    :::

```
<!-- -->
```

[[pytest_collect_file]][(]*[[file_path]]*, *[[path]]*, *[[parent]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collect_file)[¶](#pytest.hookspec.pytest_collect_file "Link to this definition")

:   Create a [[`Collector`]](#pytest.Collector "pytest.Collector") for the given path, or None if not relevant.

    For best results, the returned collector should be a subclass of [[`File`]](#pytest.File "pytest.File"), but this is not required.

    The new node needs to have the specified [`parent`] as a parent.

    Parameters[:]

    :   -   **file_path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The path to analyze.

        -   **path** (*LEGACY_PATH*) -- The path to collect (deprecated).

    ::: versionchanged
    [Changed in version 7.0.0: ]The [`file_path`] parameter was added as a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") equivalent of the [`path`] parameter. The [`path`] parameter has been deprecated.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id15 "Link to this heading")

    Any conftest file can implement this hook. For a given file path, only conftest files in parent directories of the file path are consulted.
    :::

```
<!-- -->
```

[[pytest_pycollect_makemodule]][(]*[[module_path]]*, *[[path]]*, *[[parent]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_pycollect_makemodule)[¶](#pytest.hookspec.pytest_pycollect_makemodule "Link to this definition")

:   Return a [[`pytest.Module`]](#pytest.Module "pytest.Module") collector or None for the given path.

    This hook will be called for each matching test module path. The [[`pytest_collect_file`]](#std-hook-pytest_collect_file) hook needs to be used if you want to create test modules for files that do not match as a test module.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   -   **module_path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The path of the module to collect.

        -   **path** (*LEGACY_PATH*) -- The path of the module to collect (deprecated).

    ::: versionchanged
    [Changed in version 7.0.0: ]The [`module_path`] parameter was added as a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") equivalent of the [`path`] parameter.

    The [`path`] parameter has been deprecated in favor of [`fspath`].
    :::

    ::: 
    #### Use in conftest plugins[¶](#id16 "Link to this heading")

    Any conftest file can implement this hook. For a given parent collector, only conftest files in the collector's directory and its parent directories are consulted.
    :::

For influencing the collection of objects in Python modules you can use the following hook:

[[pytest_pycollect_makeitem]][(]*[[collector]]*, *[[name]]*, *[[obj]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_pycollect_makeitem)[¶](#pytest.hookspec.pytest_pycollect_makeitem "Link to this definition")

:   Return a custom item/collector for a Python object in a module, or None.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   -   **collector** ([*Module*](#pytest.Module "pytest.Module") *\|* [*Class*](#pytest.Class "pytest.Class")) -- The module/class collector.

        -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The name of the object in the module/class.

        -   **obj** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- The object.

    Returns[:]

    :   The created items/collectors.

    Return type[:]

    :   None \| [Item](#pytest.Item "pytest.Item") \| [Collector](#pytest.Collector "pytest.Collector") \| [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[Item](#pytest.Item "pytest.Item") \| [Collector](#pytest.Collector "pytest.Collector")\]

    ::: 
    #### Use in conftest plugins[¶](#id17 "Link to this heading")

    Any conftest file can implement this hook. For a given collector, only conftest files in the collector's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_generate_tests]][(]*[[metafunc]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_generate_tests)[¶](#pytest.hookspec.pytest_generate_tests "Link to this definition")

:   Generate (multiple) parametrized calls to a test function.

    Parameters[:]

    :   **metafunc** ([*Metafunc*](#pytest.Metafunc "pytest.Metafunc")) -- The [[`Metafunc`]](#pytest.Metafunc "pytest.Metafunc") helper for the test function.

    ::: 
    #### Use in conftest plugins[¶](#id18 "Link to this heading")

    Any conftest file can implement this hook. For a given function definition, only conftest files in the functions's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_make_parametrize_id]][(]*[[config]]*, *[[val]]*, *[[argname]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_make_parametrize_id)[¶](#pytest.hookspec.pytest_make_parametrize_id "Link to this definition")

:   Return a user-friendly string representation of the given [`val`] that will be used by \@pytest.mark.parametrize calls, or None if the hook doesn't know about [`val`].

    The parameter name is available as [`argname`], if required.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **val** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- The parametrized value.

        -   **argname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The automatic parameter name produced by pytest.

    ::: 
    #### Use in conftest plugins[¶](#id19 "Link to this heading")

    Any conftest file can implement this hook.
    :::

Hooks for influencing test skipping:

[[pytest_markeval_namespace]][(]*[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_markeval_namespace)[¶](#pytest.hookspec.pytest_markeval_namespace "Link to this definition")

:   Called when constructing the globals dictionary used for evaluating string conditions in xfail/skipif markers.

    This is useful when the condition for a marker requires objects that are expensive or impossible to obtain during collection time, which is required by normal boolean conditions.

    ::: versionadded
    [Added in version 6.2.]
    :::

    Parameters[:]

    :   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    Returns[:]

    :   A dictionary of additional globals to add.

    Return type[:]

    :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), Any\]

    ::: 
    #### Use in conftest plugins[¶](#id20 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in parent directories of the item are consulted.
    :::

After collection is complete, you can modify the order of items, delete or otherwise amend the test items:

[[pytest_collection_modifyitems]][(]*[[session]]*, *[[config]]*, *[[items]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collection_modifyitems)[¶](#pytest.hookspec.pytest_collection_modifyitems "Link to this definition")

:   Called after collection has been performed. May filter or re-order the items in-place.

    When items are deselected (filtered out from [`items`]), the hook [[`pytest_deselected`]](#std-hook-pytest_deselected) must be called explicitly with the deselected items to properly notify other plugins, e.g. with [`config.hook.pytest_deselected(items=deselected_items)`].

    Parameters[:]

    :   -   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

        -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*\[*[*Item*](#pytest.Item "pytest.Item")*\]*) -- List of item objects.

    ::: 
    #### Use in conftest plugins[¶](#id21 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

Note

If this hook is implemented in [`conftest.py`] files, it always receives all collected items, not only those under the [`conftest.py`] where it is implemented.

[[pytest_collection_finish]][(]*[[session]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collection_finish)[¶](#pytest.hookspec.pytest_collection_finish "Link to this definition")

:   Called after collection has been performed and modified.

    Parameters[:]

    :   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

    ::: 
    #### Use in conftest plugins[¶](#id22 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

### Test running (runtest) hooks[¶](#test-running-runtest-hooks "Link to this heading")

All runtest related hooks receive a [[`pytest.Item`]](#pytest.Item "pytest.Item") object.

[[pytest_runtestloop]][(]*[[session]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtestloop)[¶](#pytest.hookspec.pytest_runtestloop "Link to this definition")

:   Perform the main runtest loop (after collection finished).

    The default hook implementation performs the runtest protocol for all items collected in the session ([`session.items`]), unless the collection failed or the [`collectonly`] pytest option is set.

    If at any point [[`pytest.exit()`]](#pytest.exit "pytest.exit") is called, the loop is terminated immediately.

    If at any point [`session.shouldfail`] or [`session.shouldstop`] are set, the loop is terminated after the runtest protocol for the current item is finished.

    Parameters[:]

    :   **session** ([*Session*](#pytest.Session "pytest.Session")) -- The pytest session object.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult). The return value is not used, but only stops further processing.

    ::: 
    #### Use in conftest plugins[¶](#id23 "Link to this heading")

    Any conftest file can implement this hook.
    :::

```
<!-- -->
```

[[pytest_runtest_protocol]][(]*[[item]]*, *[[nextitem]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_protocol)[¶](#pytest.hookspec.pytest_runtest_protocol "Link to this definition")

:   Perform the runtest protocol for a single test item.

    The default runtest protocol is this (see individual hooks for full details):

    -   [`pytest_runtest_logstart(nodeid,`]` `[`location)`]

    -   

        Setup phase:

        :   -   [`call`]` `[`=`]` `[`pytest_runtest_setup(item)`] (wrapped in [`CallInfo(when="setup")`])

            -   [`report`]` `[`=`]` `[`pytest_runtest_makereport(item,`]` `[`call)`]

            -   [`pytest_runtest_logreport(report)`]

            -   [`pytest_exception_interact(call,`]` `[`report)`] if an interactive exception occurred

    -   

        Call phase, if the setup passed and the [`setuponly`] pytest option is not set:

        :   -   [`call`]` `[`=`]` `[`pytest_runtest_call(item)`] (wrapped in [`CallInfo(when="call")`])

            -   [`report`]` `[`=`]` `[`pytest_runtest_makereport(item,`]` `[`call)`]

            -   [`pytest_runtest_logreport(report)`]

            -   [`pytest_exception_interact(call,`]` `[`report)`] if an interactive exception occurred

    -   

        Teardown phase:

        :   -   [`call`]` `[`=`]` `[`pytest_runtest_teardown(item,`]` `[`nextitem)`] (wrapped in [`CallInfo(when="teardown")`])

            -   [`report`]` `[`=`]` `[`pytest_runtest_makereport(item,`]` `[`call)`]

            -   [`pytest_runtest_logreport(report)`]

            -   [`pytest_exception_interact(call,`]` `[`report)`] if an interactive exception occurred

    -   [`pytest_runtest_logfinish(nodeid,`]` `[`location)`]

    Parameters[:]

    :   -   **item** ([*Item*](#pytest.Item "pytest.Item")) -- Test item for which the runtest protocol is performed.

        -   **nextitem** ([*Item*](#pytest.Item "pytest.Item") *\|* *None*) -- The scheduled-to-be-next test item (or None if this is the end my friend).

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult). The return value is not used, but only stops further processing.

    ::: 
    #### Use in conftest plugins[¶](#id24 "Link to this heading")

    Any conftest file can implement this hook.
    :::

```
<!-- -->
```

[[pytest_runtest_logstart]][(]*[[nodeid]]*, *[[location]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_logstart)[¶](#pytest.hookspec.pytest_runtest_logstart "Link to this definition")

:   Called at the start of running the runtest protocol for a single item.

    See [[`pytest_runtest_protocol`]](#std-hook-pytest_runtest_protocol) for a description of the runtest protocol.

    Parameters[:]

    :   -   **nodeid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Full node ID of the item.

        -   **location** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* *None,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- A tuple of [`(filename,`]` `[`lineno,`]` `[`testname)`] where [`filename`] is a file path relative to [`config.rootpath`] and [`lineno`] is 0-based.

    ::: 
    #### Use in conftest plugins[¶](#id25 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_runtest_logfinish]][(]*[[nodeid]]*, *[[location]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_logfinish)[¶](#pytest.hookspec.pytest_runtest_logfinish "Link to this definition")

:   Called at the end of running the runtest protocol for a single item.

    See [[`pytest_runtest_protocol`]](#std-hook-pytest_runtest_protocol) for a description of the runtest protocol.

    Parameters[:]

    :   -   **nodeid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Full node ID of the item.

        -   **location** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *\|* *None,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- A tuple of [`(filename,`]` `[`lineno,`]` `[`testname)`] where [`filename`] is a file path relative to [`config.rootpath`] and [`lineno`] is 0-based.

    ::: 
    #### Use in conftest plugins[¶](#id26 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_runtest_setup]][(]*[[item]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_setup)[¶](#pytest.hookspec.pytest_runtest_setup "Link to this definition")

:   Called to perform the setup phase for a test item.

    The default implementation runs [`setup()`] on [`item`] and all of its parents (which haven't been setup yet). This includes obtaining the values of fixtures required by the item (which haven't been obtained yet).

    Parameters[:]

    :   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

    ::: 
    #### Use in conftest plugins[¶](#id27 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_runtest_call]][(]*[[item]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_call)[¶](#pytest.hookspec.pytest_runtest_call "Link to this definition")

:   Called to run the test for test item (the call phase).

    The default implementation calls [`item.runtest()`].

    Parameters[:]

    :   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

    ::: 
    #### Use in conftest plugins[¶](#id28 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_runtest_teardown]][(]*[[item]]*, *[[nextitem]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_teardown)[¶](#pytest.hookspec.pytest_runtest_teardown "Link to this definition")

:   Called to perform the teardown phase for a test item.

    The default implementation runs the finalizers and calls [`teardown()`] on [`item`] and all of its parents (which need to be torn down). This includes running the teardown phase of fixtures required by the item (if they go out of scope).

    Parameters[:]

    :   -   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

        -   **nextitem** ([*Item*](#pytest.Item "pytest.Item") *\|* *None*) -- The scheduled-to-be-next test item (None if no further test item is scheduled). This argument is used to perform exact teardowns, i.e. calling just enough finalizers so that nextitem only needs to call setup functions.

    ::: 
    #### Use in conftest plugins[¶](#id29 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_runtest_makereport]][(]*[[item]]*, *[[call]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_makereport)[¶](#pytest.hookspec.pytest_runtest_makereport "Link to this definition")

:   Called to create a [[`TestReport`]](#pytest.TestReport "pytest.TestReport") for each of the setup, call and teardown runtest phases of a test item.

    See [[`pytest_runtest_protocol`]](#std-hook-pytest_runtest_protocol) for a description of the runtest protocol.

    Parameters[:]

    :   -   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

        -   **call** ([*CallInfo*](#pytest.CallInfo "pytest.CallInfo")*\[None\]*) -- The [[`CallInfo`]](#pytest.CallInfo "pytest.CallInfo") for the phase.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    ::: 
    #### Use in conftest plugins[¶](#id30 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

For deeper understanding you may look at the default implementation of these hooks in [`_pytest.runner`] and maybe also in [`_pytest.pdb`] which interacts with [`_pytest.capture`] and its input/output capturing in order to immediately drop into interactive debugging when a test failure occurs.

[[pytest_pyfunc_call]][(]*[[pyfuncitem]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_pyfunc_call)[¶](#pytest.hookspec.pytest_pyfunc_call "Link to this definition")

:   Call underlying test function.

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   **pyfuncitem** ([*Function*](#pytest.Function "pytest.Function")) -- The function item.

    ::: 
    #### Use in conftest plugins[¶](#id31 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

### Reporting hooks[¶](#reporting-hooks "Link to this heading")

Session related reporting hooks:

[[pytest_collectstart]][(]*[[collector]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collectstart)[¶](#pytest.hookspec.pytest_collectstart "Link to this definition")

:   Collector starts collecting.

    Parameters[:]

    :   **collector** ([*Collector*](#pytest.Collector "pytest.Collector")) -- The collector.

    ::: 
    #### Use in conftest plugins[¶](#id32 "Link to this heading")

    Any conftest file can implement this hook. For a given collector, only conftest files in the collector's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_make_collect_report]][(]*[[collector]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_make_collect_report)[¶](#pytest.hookspec.pytest_make_collect_report "Link to this definition")

:   Perform [[`collector.collect()`]](#pytest.Collector.collect "pytest.Collector.collect") and return a [[`CollectReport`]](#pytest.CollectReport "pytest.CollectReport").

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    Parameters[:]

    :   **collector** ([*Collector*](#pytest.Collector "pytest.Collector")) -- The collector.

    ::: 
    #### Use in conftest plugins[¶](#id33 "Link to this heading")

    Any conftest file can implement this hook. For a given collector, only conftest files in the collector's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_itemcollected]][(]*[[item]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_itemcollected)[¶](#pytest.hookspec.pytest_itemcollected "Link to this definition")

:   We just collected a test item.

    Parameters[:]

    :   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

    ::: 
    #### Use in conftest plugins[¶](#id34 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_collectreport]][(]*[[report]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_collectreport)[¶](#pytest.hookspec.pytest_collectreport "Link to this definition")

:   Collector finished collecting.

    Parameters[:]

    :   **report** ([*CollectReport*](#pytest.CollectReport "pytest.CollectReport")) -- The collect report.

    ::: 
    #### Use in conftest plugins[¶](#id35 "Link to this heading")

    Any conftest file can implement this hook. For a given collector, only conftest files in the collector's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_deselected]][(]*[[items]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_deselected)[¶](#pytest.hookspec.pytest_deselected "Link to this definition")

:   Called for deselected test items, e.g. by keyword.

    Note that this hook has two integration aspects for plugins:

    -   it can be *implemented* to be notified of deselected items

    -   it must be *called* from [[`pytest_collection_modifyitems`]](#std-hook-pytest_collection_modifyitems) implementations when items are deselected (to properly notify other plugins).

    May be called multiple times.

    Parameters[:]

    :   **items** (*Sequence\[*[*Item*](#pytest.Item "pytest.Item")*\]*) -- The items.

    ::: 
    #### Use in conftest plugins[¶](#id36 "Link to this heading")

    Any conftest file can implement this hook.
    :::

```
<!-- -->
```

[[pytest_report_header]][(]*[[config]]*, *[[start_path]]*, *[[startdir]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_report_header)[¶](#pytest.hookspec.pytest_report_header "Link to this definition")

:   Return a string or list of strings to be displayed as header info for terminal reporting.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **start_path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The starting dir.

        -   **startdir** (*LEGACY_PATH*) -- The starting dir (deprecated).

    ::: 
    Note

    Lines returned by a plugin are displayed before those of plugins which ran before it. If you want to have your line(s) displayed first, use [[trylast=True]](../how-to/writing_hook_functions.html#plugin-hookorder).
    :::

    ::: versionchanged
    [Changed in version 7.0.0: ]The [`start_path`] parameter was added as a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") equivalent of the [`startdir`] parameter. The [`startdir`] parameter has been deprecated.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id37 "Link to this heading")

    This hook is only called for [[initial conftests]](../how-to/writing_plugins.html#pluginorder).
    :::

```
<!-- -->
```

[[pytest_report_collectionfinish]][(]*[[config]]*, *[[start_path]]*, *[[startdir]]*, *[[items]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_report_collectionfinish)[¶](#pytest.hookspec.pytest_report_collectionfinish "Link to this definition")

:   Return a string or list of strings to be displayed after collection has finished successfully.

    These strings will be displayed after the standard "collected X items" message.

    ::: versionadded
    [Added in version 3.2.]
    :::

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **start_path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The starting dir.

        -   **startdir** (*LEGACY_PATH*) -- The starting dir (deprecated).

        -   **items** (*Sequence\[*[*Item*](#pytest.Item "pytest.Item")*\]*) -- List of pytest items that are going to be executed; this list should not be modified.

    ::: 
    Note

    Lines returned by a plugin are displayed before those of plugins which ran before it. If you want to have your line(s) displayed first, use [[trylast=True]](../how-to/writing_hook_functions.html#plugin-hookorder).
    :::

    ::: versionchanged
    [Changed in version 7.0.0: ]The [`start_path`] parameter was added as a [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") equivalent of the [`startdir`] parameter. The [`startdir`] parameter has been deprecated.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id38 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_report_teststatus]][(]*[[report]]*, *[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_report_teststatus)[¶](#pytest.hookspec.pytest_report_teststatus "Link to this definition")

:   Return result-category, shortletter and verbose word for status reporting.

    The result-category is a category in which to count the result, for example "passed", "skipped", "error" or the empty string.

    The shortletter is shown as testing progresses, for example ".", "s", "E" or the empty string.

    The verbose word is shown as testing progresses in verbose mode, for example "PASSED", "SKIPPED", "ERROR" or the empty string.

    pytest may style these implicitly according to the report outcome. To provide explicit styling, return a tuple for the verbose word, for example [`"rerun",`]` `[`"R",`]` `[`("RERUN",`]` `[`]` `[`True})`].

    Parameters[:]

    :   -   **report** ([*CollectReport*](#pytest.CollectReport "pytest.CollectReport") *\|* [*TestReport*](#pytest.TestReport "pytest.TestReport")) -- The report object whose status is to be returned.

        -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    Returns[:]

    :   The test status.

    Return type[:]

    :   [TestShortLogReport](#pytest.TestShortLogReport "pytest.TestShortLogReport") \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), Mapping\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\]\]\]

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    ::: 
    #### Use in conftest plugins[¶](#id39 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_report_to_serializable]][(]*[[config]]*, *[[report]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_report_to_serializable)[¶](#pytest.hookspec.pytest_report_to_serializable "Link to this definition")

:   Serialize the given report object into a data structure suitable for sending over the wire, e.g. converted to JSON.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **report** ([*CollectReport*](#pytest.CollectReport "pytest.CollectReport") *\|* [*TestReport*](#pytest.TestReport "pytest.TestReport")) -- The report.

    ::: 
    #### Use in conftest plugins[¶](#id40 "Link to this heading")

    Any conftest file can implement this hook. The exact details may depend on the plugin which calls the hook.
    :::

```
<!-- -->
```

[[pytest_report_from_serializable]][(]*[[config]]*, *[[data]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_report_from_serializable)[¶](#pytest.hookspec.pytest_report_from_serializable "Link to this definition")

:   Restore a report object previously serialized with [[`pytest_report_to_serializable`]](#std-hook-pytest_report_to_serializable).

    Parameters[:]

    :   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    ::: 
    #### Use in conftest plugins[¶](#id41 "Link to this heading")

    Any conftest file can implement this hook. The exact details may depend on the plugin which calls the hook.
    :::

```
<!-- -->
```

[[pytest_terminal_summary]][(]*[[terminalreporter]]*, *[[exitstatus]]*, *[[config]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_terminal_summary)[¶](#pytest.hookspec.pytest_terminal_summary "Link to this definition")

:   Add a section to terminal summary reporting.

    Parameters[:]

    :   -   **terminalreporter** ([*TerminalReporter*](#pytest.TerminalReporter "pytest.TerminalReporter")) -- The internal terminal reporter object.

        -   **exitstatus** ([*ExitCode*](#pytest.ExitCode "pytest.ExitCode")) -- The exit status that will be reported back to the OS.

        -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

    ::: versionadded
    [Added in version 4.2: ]The [`config`] parameter.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id42 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_fixture_setup]][(]*[[fixturedef]]*, *[[request]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_fixture_setup)[¶](#pytest.hookspec.pytest_fixture_setup "Link to this definition")

:   Perform fixture setup execution.

    Parameters[:]

    :   -   **fixturedef** ([*FixtureDef*](#pytest.FixtureDef "pytest.FixtureDef")*\[Any\]*) -- The fixture definition object.

        -   **request** (*SubRequest*) -- The fixture request object.

    Returns[:]

    :   The return value of the call to the fixture function.

    Return type[:]

    :   [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)") \| None

    Stops at first non-None result, see [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult).

    ::: 
    Note

    If the fixture function returns None, other implementations of this hook function will continue to be called, according to the behavior of the [[firstresult: stop at first non-None result]](../how-to/writing_hook_functions.html#firstresult) option.
    :::

    ::: 
    #### Use in conftest plugins[¶](#id43 "Link to this heading")

    Any conftest file can implement this hook. For a given fixture, only conftest files in the fixture scope's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_fixture_post_finalizer]][(]*[[fixturedef]]*, *[[request]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_fixture_post_finalizer)[¶](#pytest.hookspec.pytest_fixture_post_finalizer "Link to this definition")

:   Called after fixture teardown, but before the cache is cleared, so the fixture result [`fixturedef.cached_result`] is still available (not [`None`]).

    Parameters[:]

    :   -   **fixturedef** ([*FixtureDef*](#pytest.FixtureDef "pytest.FixtureDef")*\[Any\]*) -- The fixture definition object.

        -   **request** (*SubRequest*) -- The fixture request object.

    ::: 
    #### Use in conftest plugins[¶](#id44 "Link to this heading")

    Any conftest file can implement this hook. For a given fixture, only conftest files in the fixture scope's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_warning_recorded]][(]*[[warning_message]]*, *[[when]]*, *[[nodeid]]*, *[[location]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_warning_recorded)[¶](#pytest.hookspec.pytest_warning_recorded "Link to this definition")

:   Process a warning captured by the internal pytest warnings plugin.

    Parameters[:]

    :   -   **warning_message** (*warnings.WarningMessage*) -- The captured warning. This is the same object produced by [[`warnings.catch_warnings`]](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "(in Python v3.14)"), and contains the same attributes as the parameters of [[`warnings.showwarning()`]](https://docs.python.org/3/library/warnings.html#warnings.showwarning "(in Python v3.14)").

        -   **when** (*Literal\[\'config\',* *\'collect\',* *\'runtest\'\]*) --

            Indicates when the warning was captured. Possible values:

            -   [`"config"`]: during pytest configuration/initialization stage.

            -   [`"collect"`]: during test collection.

            -   [`"runtest"`]: during test execution.

        -   **nodeid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Full id of the item. Empty string for warnings that are not specific to a particular node.

        -   **location** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) -- When available, holds information about the execution context of the captured warning (filename, linenumber, function). [`function`] evaluates to \<module\> when the execution context is at the module level.

    ::: versionadded
    [Added in version 6.0.]
    :::

    ::: 
    #### Use in conftest plugins[¶](#id45 "Link to this heading")

    Any conftest file can implement this hook. If the warning is specific to a particular node, only conftest files in parent directories of the node are consulted.
    :::

Central hook for reporting about test execution:

[[pytest_runtest_logreport]][(]*[[report]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_runtest_logreport)[¶](#pytest.hookspec.pytest_runtest_logreport "Link to this definition")

:   Process the [[`TestReport`]](#pytest.TestReport "pytest.TestReport") produced for each of the setup, call and teardown runtest phases of an item.

    See [[`pytest_runtest_protocol`]](#std-hook-pytest_runtest_protocol) for a description of the runtest protocol.

    ::: 
    #### Use in conftest plugins[¶](#id46 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

Assertion related hooks:

[[pytest_assertrepr_compare]][(]*[[config]]*, *[[op]]*, *[[left]]*, *[[right]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_assertrepr_compare)[¶](#pytest.hookspec.pytest_assertrepr_compare "Link to this definition")

:   Return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list of strings. The strings will be joined by newlines but any newlines *in* a string will be escaped. Note that all but the first line will be indented slightly, the intention is for the first line to be a summary.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The operator, e.g. [`"=="`], [`"!="`], [`"not`]` `[`in"`].

        -   **left** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- The left operand.

        -   **right** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) -- The right operand.

    ::: 
    #### Use in conftest plugins[¶](#id47 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

```
<!-- -->
```

[[pytest_assertion_pass]][(]*[[item]]*, *[[lineno]]*, *[[orig]]*, *[[expl]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_assertion_pass)[¶](#pytest.hookspec.pytest_assertion_pass "Link to this definition")

:   Called whenever an assertion passes.

    ::: versionadded
    [Added in version 5.0.]
    :::

    Use this hook to do some processing after a passing assertion. The original assertion information is available in the [`orig`] string and the pytest introspected assertion information is available in the [`expl`] string.

    This hook must be explicitly enabled by the [[`enable_assertion_pass_hook`]](#confval-enable_assertion_pass_hook) configuration option:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        enable_assertion_pass_hook = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        enable_assertion_pass_hook = true
    :::
    :::
    :::
    :::

    You need to **clean the .pyc** files in your project directory and interpreter libraries when enabling this option, as assertions will require to be re-written.

    Parameters[:]

    :   -   **item** ([*Item*](#pytest.Item "pytest.Item")) -- pytest item object of current test.

        -   **lineno** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Line number of the assert statement.

        -   **orig** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- String with the original assertion.

        -   **expl** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- String with the assert explanation.

    ::: 
    #### Use in conftest plugins[¶](#id48 "Link to this heading")

    Any conftest file can implement this hook. For a given item, only conftest files in the item's directory and its parent directories are consulted.
    :::

### Debugging/Interaction hooks[¶](#debugging-interaction-hooks "Link to this heading")

There are few hooks which can be used for special reporting or interaction with exceptions:

[[pytest_internalerror]][(]*[[excrepr]]*, *[[excinfo]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_internalerror)[¶](#pytest.hookspec.pytest_internalerror "Link to this definition")

:   Called for internal errors.

    Return True to suppress the fallback handling of printing an INTERNALERROR message directly to sys.stderr.

    Parameters[:]

    :   -   **excrepr** (*ExceptionRepr*) -- The exception repr object.

        -   **excinfo** ([*ExceptionInfo*](#pytest.ExceptionInfo "pytest.ExceptionInfo")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]*) -- The exception info.

    ::: 
    #### Use in conftest plugins[¶](#id49 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_keyboard_interrupt]][(]*[[excinfo]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_keyboard_interrupt)[¶](#pytest.hookspec.pytest_keyboard_interrupt "Link to this definition")

:   Called for keyboard interrupt.

    Parameters[:]

    :   **excinfo** ([*ExceptionInfo*](#pytest.ExceptionInfo "pytest.ExceptionInfo")*\[*[*KeyboardInterrupt*](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.14)") *\|* *Exit\]*) -- The exception info.

    ::: 
    #### Use in conftest plugins[¶](#id50 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_exception_interact]][(]*[[node]]*, *[[call]]*, *[[report]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_exception_interact)[¶](#pytest.hookspec.pytest_exception_interact "Link to this definition")

:   Called when an exception was raised which can potentially be interactively handled.

    May be called during collection (see [[`pytest_make_collect_report`]](#std-hook-pytest_make_collect_report)), in which case [`report`] is a [[`CollectReport`]](#pytest.CollectReport "pytest.CollectReport").

    May be called during runtest of an item (see [[`pytest_runtest_protocol`]](#std-hook-pytest_runtest_protocol)), in which case [`report`] is a [[`TestReport`]](#pytest.TestReport "pytest.TestReport").

    This hook is not called if the exception that was raised is an internal exception like [`skip.Exception`].

    Parameters[:]

    :   -   **node** ([*Item*](#pytest.Item "pytest.Item") *\|* [*Collector*](#pytest.Collector "pytest.Collector")) -- The item or collector.

        -   **call** ([*CallInfo*](#pytest.CallInfo "pytest.CallInfo")*\[Any\]*) -- The call information. Contains the exception.

        -   **report** ([*CollectReport*](#pytest.CollectReport "pytest.CollectReport") *\|* [*TestReport*](#pytest.TestReport "pytest.TestReport")) -- The collection or test report.

    ::: 
    #### Use in conftest plugins[¶](#id51 "Link to this heading")

    Any conftest file can implement this hook. For a given node, only conftest files in parent directories of the node are consulted.
    :::

```
<!-- -->
```

[[pytest_enter_pdb]][(]*[[config]]*, *[[pdb]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_enter_pdb)[¶](#pytest.hookspec.pytest_enter_pdb "Link to this definition")

:   Called upon pdb.set_trace().

    Can be used by plugins to take special action just before the python debugger enters interactive mode.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **pdb** ([*pdb.Pdb*](https://docs.python.org/3/library/pdb.html#pdb.Pdb "(in Python v3.14)")) -- The Pdb instance.

    ::: 
    #### Use in conftest plugins[¶](#id52 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

```
<!-- -->
```

[[pytest_leave_pdb]][(]*[[config]]*, *[[pdb]]*[)][[[\[source\]]]](../_modules/_pytest/hookspec.html#pytest_leave_pdb)[¶](#pytest.hookspec.pytest_leave_pdb "Link to this definition")

:   Called when leaving pdb (e.g. with continue after pdb.set_trace()).

    Can be used by plugins to take special action just after the python debugger leaves interactive mode.

    Parameters[:]

    :   -   **config** ([*Config*](#pytest.Config "pytest.Config")) -- The pytest config object.

        -   **pdb** ([*pdb.Pdb*](https://docs.python.org/3/library/pdb.html#pdb.Pdb "(in Python v3.14)")) -- The Pdb instance.

    ::: 
    #### Use in conftest plugins[¶](#id53 "Link to this heading")

    Any conftest plugin can implement this hook.
    :::

## Collection tree objects[¶](#collection-tree-objects "Link to this heading")

These are the collector and item classes (collectively called "nodes") which make up the collection tree.

### Node[¶](#node "Link to this heading")

*[[class]][ ]*[[Node]][[[\[source\]]]](../_modules/_pytest/nodes.html#Node)[¶](#pytest.nodes.Node "Link to this definition")

:   Bases: [[`ABC`]](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Base class of [[`Collector`]](#pytest.Collector "_pytest.nodes.Collector") and [[`Item`]](#pytest.Item "_pytest.nodes.Item"), the components of the test collection tree.

    [`Collector`]\'s are the internal nodes of the tree, and [`Item`]\'s are the leaf nodes.

```
<!-- -->
```

[[fspath]]*[[:]][ ][LEGACY_PATH]*[¶](#pytest.nodes.Node.fspath "Link to this definition")

:   A [`LEGACY_PATH`] copy of the [[`path`]](#pytest.nodes.Node.path "_pytest.nodes.Node.path") attribute. Intended for usage for methods not migrated to [`pathlib.Path`] yet, such as [[`Item.reportinfo`]](#pytest.Item.reportinfo "pytest.Item.reportinfo"). Will be deprecated in a future release, prefer using [[`path`]](#pytest.nodes.Node.path "_pytest.nodes.Node.path") instead.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.nodes.Node.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.nodes.Node.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.nodes.Node.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.nodes.Node.session "Link to this definition")

:   The pytest session this node is part of.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.nodes.Node.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[keywords]]*[[:]][ ][MutableMapping][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][Any][[\]]]*[¶](#pytest.nodes.Node.keywords "Link to this definition")

:   Keywords/markers collected from all scopes.

```
<!-- -->
```

[[own_markers]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[Mark]](#pytest.Mark "pytest.Mark")[[\]]]*[¶](#pytest.nodes.Node.own_markers "Link to this definition")

:   The marker objects belonging to this node.

```
<!-- -->
```

[[extra_keyword_matches]]*[[:]][ ][[set]](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#pytest.nodes.Node.extra_keyword_matches "Link to this definition")

:   Allow adding of extra keywords to use for matching.

```
<!-- -->
```

[[stash]]*[[:]][ ][[Stash]](#pytest.Stash "pytest.Stash")*[¶](#pytest.nodes.Node.stash "Link to this definition")

:   A place where plugins can store information on the node for their own use.

```
<!-- -->
```

*[classmethod]* [[from_parent]][(]*[[parent]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.from_parent)[¶](#pytest.nodes.Node.from_parent "Link to this definition")

:   Public constructor for Nodes.

    This indirection got introduced in order to enable removing the fragile logic from the node constructors.

    Subclasses can use [`super().from_parent(...)`] when overriding the construction.

    Parameters[:]

    :   **parent** ([*Node*](#pytest.nodes.Node "_pytest.nodes.Node")) -- The parent node of this Node.

```
<!-- -->
```

*[[property]][ ]*[[ihook]]*[[:]][ ][[HookRelay]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.HookRelay "(in pluggy v0.1)")*[¶](#pytest.nodes.Node.ihook "Link to this definition")

:   fspath-sensitive hook proxy used to call pytest hooks.

```
<!-- -->
```

[[warn]][(]*[[warning]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.warn)[¶](#pytest.nodes.Node.warn "Link to this definition")

:   Issue a warning for this Node.

    Warnings will be displayed after the test session, unless explicitly suppressed.

    Parameters[:]

    :   **warning** ([*Warning*](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)")) -- The warning instance to issue.

    Raises[:]

    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") -- If [`warning`] instance is not a subclass of Warning.

    Example usage:

    ::: 
    ::: highlight
        node.warn(PytestWarning("some message"))
        node.warn(UserWarning("some message"))
    :::
    :::

    ::: versionchanged
    [Changed in version 6.2: ]Any subclass of [[`Warning`]](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)") is now accepted, rather than only [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning") subclasses.
    :::

```
<!-- -->
```

*[[property]][ ]*[[nodeid]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.nodes.Node.nodeid "Link to this definition")

:   A ::-separated string denoting its collection tree address.

```
<!-- -->
```

*[for] [\...] [in]* [[iter_parents]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.iter_parents)[¶](#pytest.nodes.Node.iter_parents "Link to this definition")

:   Iterate over all parent collectors starting from and including self up to the root of the collection tree.

    ::: versionadded
    [Added in version 8.1.]
    :::

```
<!-- -->
```

[[listchain]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.listchain)[¶](#pytest.nodes.Node.listchain "Link to this definition")

:   Return a list of all parent collectors starting from the root of the collection tree down to and including self.

```
<!-- -->
```

[[add_marker]][(]*[[marker]]*, *[[append]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.add_marker)[¶](#pytest.nodes.Node.add_marker "Link to this definition")

:   Dynamically add a marker object to the node.

    Parameters[:]

    :   -   **marker** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*MarkDecorator*](#pytest.MarkDecorator "_pytest.mark.structures.MarkDecorator")) -- The marker.

        -   **append** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to append the marker, or prepend it.

```
<!-- -->
```

[[iter_markers]][(]*[[name]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.iter_markers)[¶](#pytest.nodes.Node.iter_markers "Link to this definition")

:   Iterate over all markers of the node.

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- If given, filter the results by the name attribute.

    Returns[:]

    :   An iterator of the markers of the node.

    Return type[:]

    :   [*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")\[[*Mark*](#pytest.Mark "_pytest.mark.structures.Mark")\]

```
<!-- -->
```

*[for] [\...] [in]* [[iter_markers_with_node]][(]*[[name]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.iter_markers_with_node)[¶](#pytest.nodes.Node.iter_markers_with_node "Link to this definition")

:   Iterate over all markers of the node.

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- If given, filter the results by the name attribute.

    Returns[:]

    :   An iterator of (node, mark) tuples.

    Return type[:]

    :   [*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")\[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")\[[*Node*](#pytest.nodes.Node "_pytest.nodes.Node"), [*Mark*](#pytest.Mark "_pytest.mark.structures.Mark")\]\]

```
<!-- -->
```

[[get_closest_marker]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[Mark]](#pytest.Mark "_pytest.mark.structures.Mark")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.get_closest_marker)[¶](#pytest.nodes.Node.get_closest_marker "Link to this definition")\
[[get_closest_marker]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[default]][[:]][ ][[[Mark]](#pytest.Mark "_pytest.mark.structures.Mark")]*[)] [[→] [[[Mark]](#pytest.Mark "_pytest.mark.structures.Mark")]]

:   Return the first marker matching the name, from closest (for example function) to farther level (for example module level).

    Parameters[:]

    :   -   **default** -- Fallback return value if no marker was found.

        -   **name** -- Name to filter by.

```
<!-- -->
```

[[listextrakeywords]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.listextrakeywords)[¶](#pytest.nodes.Node.listextrakeywords "Link to this definition")

:   Return a set of all extra keywords in self and any parents.

```
<!-- -->
```

[[addfinalizer]][(]*[[fin]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.addfinalizer)[¶](#pytest.nodes.Node.addfinalizer "Link to this definition")

:   Register a function to be called without arguments when this node is finalized.

    This method can only be called when this node is active in a setup chain, for example during self.setup().

```
<!-- -->
```

[[getparent]][(]*[[cls]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.getparent)[¶](#pytest.nodes.Node.getparent "Link to this definition")

:   Get the closest parent node (including self) which is an instance of the given class.

    Parameters[:]

    :   **cls** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[\_NodeType\]*) -- The node class to search for.

    Returns[:]

    :   The node, if found.

    Return type[:]

    :   *\_NodeType* \| None

```
<!-- -->
```

[[repr_failure]][(]*[[excinfo]]*, *[[style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Node.repr_failure)[¶](#pytest.nodes.Node.repr_failure "Link to this definition")

:   Return a representation of a collection or test failure.

    ::: 
    See also

    [[Working with non-python tests]](../example/nonpython.html#non-python-tests)
    :::

    Parameters[:]

    :   **excinfo** ([*ExceptionInfo*](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]*) -- Exception information for the failure.

### Collector[¶](#collector "Link to this heading")

*[[class]][ ]*[[Collector]][[[\[source\]]]](../_modules/_pytest/nodes.html#Collector)[¶](#pytest.Collector "Link to this definition")

:   Bases: [[`Node`]](#pytest.nodes.Node "_pytest.nodes.Node"), [[`ABC`]](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Base class of all collectors.

    Collector create children through [`collect()`] and thus iteratively build the collection tree.

```
<!-- -->
```

*[[exception]][ ]*[[CollectError]][[[\[source\]]]](../_modules/_pytest/nodes.html#Collector.CollectError)[¶](#pytest.Collector.CollectError "Link to this definition")

:   Bases: [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

    An error during collection, contains a custom message.

```
<!-- -->
```

*[abstractmethod]* [[collect]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Collector.collect)[¶](#pytest.Collector.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[repr_failure]][(]*[[excinfo]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Collector.repr_failure)[¶](#pytest.Collector.repr_failure "Link to this definition")

:   Return a representation of a collection failure.

    Parameters[:]

    :   **excinfo** ([*ExceptionInfo*](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]*) -- Exception information for the failure.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Collector.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Collector.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Collector.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Collector.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Collector.session "Link to this definition")

:   The pytest session this node is part of.

### Item[¶](#item "Link to this heading")

*[[class]][ ]*[[Item]][[[\[source\]]]](../_modules/_pytest/nodes.html#Item)[¶](#pytest.Item "Link to this definition")

:   Bases: [[`Node`]](#pytest.nodes.Node "_pytest.nodes.Node"), [[`ABC`]](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Base class of all test invocation items.

    Note that for a single function there might be multiple test invocation items.

```
<!-- -->
```

[[user_properties]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]][[\]]]*[¶](#pytest.Item.user_properties "Link to this definition")

:   A list of tuples (name, value) that holds user defined properties for this test.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Item.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Item.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Item.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Item.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Item.session "Link to this definition")

:   The pytest session this node is part of.

```
<!-- -->
```

*[abstractmethod]* [[runtest]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Item.runtest)[¶](#pytest.Item.runtest "Link to this definition")

:   Run the test case for this item.

    Must be implemented by subclasses.

    ::: 
    See also

    [[Working with non-python tests]](../example/nonpython.html#non-python-tests)
    :::

```
<!-- -->
```

[[add_report_section]][(]*[[when]]*, *[[key]]*, *[[content]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#Item.add_report_section)[¶](#pytest.Item.add_report_section "Link to this definition")

:   Add a new report section, similar to what's done internally to add stdout and stderr captured output:

    ::: 
    ::: highlight
        item.add_report_section("call", "stdout", "report section contents")
    :::
    :::

    Parameters[:]

    :   -   **when** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- One of the possible capture states, [`"setup"`], [`"call"`], [`"teardown"`].

        -   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Name of the section, can be customized at will. Pytest uses [`"stdout"`] and [`"stderr"`] internally.

        -   **content** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The full contents as a string.

```
<!-- -->
```

[[reportinfo]][(][)][[[\[source\]]]](../_modules/_pytest/nodes.html#Item.reportinfo)[¶](#pytest.Item.reportinfo "Link to this definition")

:   Get location information for this item for test reports.

    Returns a tuple with three elements:

    -   The path of the test (default [`self.path`])

    -   The 0-based line number of the test (default [`None`])

    -   A name of the test to be shown (default [`""`])

    ::: 
    See also

    [[Working with non-python tests]](../example/nonpython.html#non-python-tests)
    :::

```
<!-- -->
```

*[[property]][ ]*[[location]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[[[\[source\]]]](../_modules/_pytest/nodes.html#Item.location)[¶](#pytest.Item.location "Link to this definition")

:   Returns a tuple of [`(relfspath,`]` `[`lineno,`]` `[`testname)`] for this item where [`relfspath`] is file path relative to [`config.rootpath`] and lineno is a 0-based line number.

### File[¶](#file "Link to this heading")

*[[class]][ ]*[[File]][[[\[source\]]]](../_modules/_pytest/nodes.html#File)[¶](#pytest.File "Link to this definition")

:   Bases: [[`FSCollector`]](#pytest.nodes.FSCollector "_pytest.nodes.FSCollector"), [[`ABC`]](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Base class for collecting tests from a file.

    [[Working with non-python tests]](../example/nonpython.html#non-python-tests).

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.File.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.File.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.File.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.File.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.File.session "Link to this definition")

:   The pytest session this node is part of.

### FSCollector[¶](#fscollector "Link to this heading")

*[[class]][ ]*[[FSCollector]][[[\[source\]]]](../_modules/_pytest/nodes.html#FSCollector)[¶](#pytest.nodes.FSCollector "Link to this definition")

:   Bases: [[`Collector`]](#pytest.Collector "_pytest.nodes.Collector"), [[`ABC`]](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Base class for filesystem collectors.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.nodes.FSCollector.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

*[classmethod]* [[from_parent]][(]*[[parent]]*, *[[\*]]*, *[[fspath]][[=]][[None]]*, *[[path]][[=]][[None]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/nodes.html#FSCollector.from_parent)[¶](#pytest.nodes.FSCollector.from_parent "Link to this definition")

:   The public constructor.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.nodes.FSCollector.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.nodes.FSCollector.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.nodes.FSCollector.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.nodes.FSCollector.session "Link to this definition")

:   The pytest session this node is part of.

### Session[¶](#session "Link to this heading")

*[[final]][ ][[class]][ ]*[[Session]][[[\[source\]]]](../_modules/_pytest/main.html#Session)[¶](#pytest.Session "Link to this definition")

:   Bases: [[`Collector`]](#pytest.Collector "_pytest.nodes.Collector")

    The root of the collection tree.

    [`Session`] collects the initial paths given as arguments to pytest.

```
<!-- -->
```

*[[exception]][ ]*[[Interrupted]][¶](#pytest.Session.Interrupted "Link to this definition")

:   Bases: [[`KeyboardInterrupt`]](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.14)")

    Signals that the test run was interrupted.

```
<!-- -->
```

*[[exception]][ ]*[[Failed]][¶](#pytest.Session.Failed "Link to this definition")

:   Bases: [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

    Signals a stop as failed test run.

```
<!-- -->
```

*[[property]][ ]*[[startpath]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Session.startpath "Link to this definition")

:   The path from which pytest was invoked.

    ::: versionadded
    [Added in version 7.0.0.]
    :::

```
<!-- -->
```

[[isinitpath]][(]*[[path]]*, *[[\*]]*, *[[with_parents]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/main.html#Session.isinitpath)[¶](#pytest.Session.isinitpath "Link to this definition")

:   Is path an initial path?

    An initial path is a path explicitly given to pytest on the command line.

    Parameters[:]

    :   **with_parents** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If set, also return True if the path is a parent of an initial path.

    ::: versionchanged
    [Changed in version 8.0: ]Added the [`with_parents`] parameter.
    :::

```
<!-- -->
```

[[perform_collect]][(]*[[args]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[genitems]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[True]][[\]]]][ ][[=]][ ][[True]]*[)] [[→] [[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[Item]](#pytest.Item "_pytest.nodes.Item")[[\]]]]][[[\[source\]]]](../_modules/_pytest/main.html#Session.perform_collect)[¶](#pytest.Session.perform_collect "Link to this definition")\
[[perform_collect]][(]*[[args]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[genitems]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)] [[→] [[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[Item]](#pytest.Item "_pytest.nodes.Item")[ ][[\|]][ ][[Collector]](#pytest.Collector "_pytest.nodes.Collector")[[\]]]]]

:   Perform the collection phase for this session.

    This is called by the default [[`pytest_collection`]](#std-hook-pytest_collection) hook implementation; see the documentation of this hook for more details. For testing purposes, it may also be called directly on a fresh [`Session`].

    This function normally recursively expands any collectors collected from the session to their items, and only items are returned. For testing purposes, this may be suppressed by passing [`genitems=False`], in which case the return value contains these collectors unexpanded, and [`session.items`] is empty.

```
<!-- -->
```

*[for] [\...] [in]* [[collect]][(][)][[[\[source\]]]](../_modules/_pytest/main.html#Session.collect)[¶](#pytest.Session.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Session.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Session.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Session.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Session.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Session.session "Link to this definition")

:   The pytest session this node is part of.

### Package[¶](#package "Link to this heading")

*[[class]][ ]*[[Package]][[[\[source\]]]](../_modules/_pytest/python.html#Package)[¶](#pytest.Package "Link to this definition")

:   Bases: [[`Directory`]](#pytest.Directory "_pytest.nodes.Directory")

    Collector for files and directories in a Python packages -- directories with an [`__init__.py`] file.

    ::: 
    Note

    Directories without an [`__init__.py`] file are instead collected by [[`Dir`]](#pytest.Dir "pytest.Dir") by default. Both are [[`Directory`]](#pytest.Directory "pytest.Directory") collectors.
    :::

    ::: versionchanged
    [Changed in version 8.0: ]Now inherits from [[`Directory`]](#pytest.Directory "pytest.Directory").
    :::

```
<!-- -->
```

*[for] [\...] [in]* [[collect]][(][)][[[\[source\]]]](../_modules/_pytest/python.html#Package.collect)[¶](#pytest.Package.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Package.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Package.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Package.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Package.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Package.session "Link to this definition")

:   The pytest session this node is part of.

### Module[¶](#module "Link to this heading")

*[[class]][ ]*[[Module]][[[\[source\]]]](../_modules/_pytest/python.html#Module)[¶](#pytest.Module "Link to this definition")

:   Bases: [[`File`]](#pytest.File "_pytest.nodes.File"), [`PyCollector`]

    Collector for test classes and functions in a Python module.

```
<!-- -->
```

[[collect]][(][)][[[\[source\]]]](../_modules/_pytest/python.html#Module.collect)[¶](#pytest.Module.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Module.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Module.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Module.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Module.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Module.session "Link to this definition")

:   The pytest session this node is part of.

### Class[¶](#class "Link to this heading")

*[[class]][ ]*[[Class]][[[\[source\]]]](../_modules/_pytest/python.html#Class)[¶](#pytest.Class "Link to this definition")

:   Bases: [`PyCollector`]

    Collector for test methods (and nested classes) in a Python class.

```
<!-- -->
```

*[classmethod]* [[from_parent]][(]*[[parent]]*, *[[\*]]*, *[[name]]*, *[[obj]][[=]][[None]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/python.html#Class.from_parent)[¶](#pytest.Class.from_parent "Link to this definition")

:   The public constructor.

```
<!-- -->
```

[[collect]][(][)][[[\[source\]]]](../_modules/_pytest/python.html#Class.collect)[¶](#pytest.Class.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Class.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Class.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Class.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Class.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Class.session "Link to this definition")

:   The pytest session this node is part of.

### Function[¶](#function "Link to this heading")

*[[class]][ ]*[[Function]][[[\[source\]]]](../_modules/_pytest/python.html#Function)[¶](#pytest.Function "Link to this definition")

:   Bases: [`PyobjMixin`], [[`Item`]](#pytest.Item "_pytest.nodes.Item")

    Item responsible for setting up and executing a Python test function.

    Parameters[:]

    :   -   **name** -- The full function name, including any decorations like those added by parametrization ([`my_func[my_param]`]).

        -   **parent** -- The parent Node.

        -   **config** -- The pytest Config object.

        -   **callspec** -- If given, this function has been parametrized and the callspec contains meta information about the parametrization.

        -   **callobj** -- If given, the object which will be called when the Function is invoked, otherwise the callobj will be obtained from [`parent`] using [`originalname`].

        -   **keywords** -- Keywords bound to the function object for "-k" matching.

        -   **session** -- The pytest Session object.

        -   **fixtureinfo** -- Fixture information already resolved at this fixture node..

        -   **originalname** -- The attribute name to use for accessing the underlying function object. Defaults to [`name`]. Set this if name is different from the original name, for example when it contains decorations like those added by parametrization ([`my_func[my_param]`]).

    [[originalname]][¶](#pytest.Function.originalname "Link to this definition")

    :   Original function name, without any decorations (for example parametrization adds a [`"[...]"`] suffix to function names), used to access the underlying function object from [`parent`] (in case [`callobj`] is not given explicitly).

        ::: versionadded
        [Added in version 3.0.]
        :::

    *[classmethod]* [[from_parent]][(]*[[parent]]*, *[[\*\*]][[kw]]*[)][[[\[source\]]]](../_modules/_pytest/python.html#Function.from_parent)[¶](#pytest.Function.from_parent "Link to this definition")

    :   The public constructor.

```
<!-- -->
```

*[[property]][ ]*[[function]][¶](#pytest.Function.function "Link to this definition")

:   Underlying python 'function' object.

```
<!-- -->
```

*[[property]][ ]*[[instance]][¶](#pytest.Function.instance "Link to this definition")

:   Python instance object the function is bound to.

    Returns None if not a test method, e.g. for a standalone test function, a class or a module.

```
<!-- -->
```

[[runtest]][(][)][[[\[source\]]]](../_modules/_pytest/python.html#Function.runtest)[¶](#pytest.Function.runtest "Link to this definition")

:   Execute the underlying test function.

```
<!-- -->
```

[[repr_failure]][(]*[[excinfo]]*[)][[[\[source\]]]](../_modules/_pytest/python.html#Function.repr_failure)[¶](#pytest.Function.repr_failure "Link to this definition")

:   Return a representation of a collection or test failure.

    ::: 
    See also

    [[Working with non-python tests]](../example/nonpython.html#non-python-tests)
    :::

    Parameters[:]

    :   **excinfo** ([*ExceptionInfo*](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]*) -- Exception information for the failure.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Function.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Function.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Function.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Function.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Function.session "Link to this definition")

:   The pytest session this node is part of.

### FunctionDefinition[¶](#functiondefinition "Link to this heading")

*[[class]][ ]*[[FunctionDefinition]][[[\[source\]]]](../_modules/_pytest/python.html#FunctionDefinition)[¶](#pytest.python.FunctionDefinition "Link to this definition")

:   Bases: [[`Function`]](#pytest.Function "_pytest.python.Function")

    This class is a stop gap solution until we evolve to have actual function definition nodes and manage to get rid of [`metafunc`].

```
<!-- -->
```

[[runtest]][(][)][[[\[source\]]]](../_modules/_pytest/python.html#FunctionDefinition.runtest)[¶](#pytest.python.FunctionDefinition.runtest "Link to this definition")

:   Execute the underlying test function.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.python.FunctionDefinition.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.python.FunctionDefinition.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.python.FunctionDefinition.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.python.FunctionDefinition.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.python.FunctionDefinition.session "Link to this definition")

:   The pytest session this node is part of.

```
<!-- -->
```

[[setup]][(][)][¶](#pytest.python.FunctionDefinition.setup "Link to this definition")

:   Execute the underlying test function.

## Objects[¶](#objects "Link to this heading")

Objects accessible from [[fixtures]](fixtures.html#fixture) or [[hooks]](#hook-reference) or importable from [`pytest`].

### CallInfo[¶](#callinfo "Link to this heading")

*[[final]][ ][[class]][ ]*[[CallInfo]][[[\[source\]]]](../_modules/_pytest/runner.html#CallInfo)[¶](#pytest.CallInfo "Link to this definition")

:   Result/Exception info of a function invocation.

```
<!-- -->
```

[[excinfo]]*[[:]][ ][[ExceptionInfo]](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")[[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#pytest.CallInfo.excinfo "Link to this definition")

:   The captured exception of the call, if it raised.

```
<!-- -->
```

[[start]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.CallInfo.start "Link to this definition")

:   The system time when the call started, in seconds since the epoch.

```
<!-- -->
```

[[stop]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.CallInfo.stop "Link to this definition")

:   The system time when the call ended, in seconds since the epoch.

```
<!-- -->
```

[[duration]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.CallInfo.duration "Link to this definition")

:   The call duration, in seconds.

```
<!-- -->
```

[[when]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'collect\']][[,]][ ][[\'setup\']][[,]][ ][[\'call\']][[,]][ ][[\'teardown\']][[\]]]*[¶](#pytest.CallInfo.when "Link to this definition")

:   The context of invocation: "collect", "setup", "call" or "teardown".

```
<!-- -->
```

*[[property]][ ]*[[result]]*[[:]][ ][TResult]*[¶](#pytest.CallInfo.result "Link to this definition")

:   The return value of the call, if it didn't raise.

    Can only be accessed if excinfo is None.

```
<!-- -->
```

*[classmethod]* [[from_call]][(]*[[func]]*, *[[when]]*, *[[reraise]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/runner.html#CallInfo.from_call)[¶](#pytest.CallInfo.from_call "Link to this definition")

:   Call func, wrapping the result in a CallInfo.

    Parameters[:]

    :   -   **func** (*Callable\[\[\],* *\_pytest.runner.TResult\]*) -- The function to call. Called without arguments.

        -   **when** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")*\[\'collect\',* *\'setup\',* *\'call\',* *\'teardown\'\]*) -- The phase in which the function is called.

        -   **reraise** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]* *\|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\],* *\...\]* *\|* *None*) -- Exception or exceptions that shall propagate if raised by the function, instead of being wrapped in the CallInfo.

### CollectReport[¶](#collectreport "Link to this heading")

*[[final]][ ][[class]][ ]*[[CollectReport]][[[\[source\]]]](../_modules/_pytest/reports.html#CollectReport)[¶](#pytest.CollectReport "Link to this definition")

:   Bases: [`BaseReport`]

    Collection report object.

    Reports can contain arbitrary extra attributes.

```
<!-- -->
```

[[nodeid]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.nodeid "Link to this definition")

:   Normalized collection nodeid.

```
<!-- -->
```

[[outcome]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'passed\']][[,]][ ][[\'failed\']][[,]][ ][[\'skipped\']][[\]]]*[¶](#pytest.CollectReport.outcome "Link to this definition")

:   Test outcome, always one of "passed", "failed", "skipped".

```
<!-- -->
```

[[longrepr]]*[[:]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[ExceptionInfo]](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")[[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][TerminalRepr]*[¶](#pytest.CollectReport.longrepr "Link to this definition")

:   None or a failure representation.

```
<!-- -->
```

[[result]][¶](#pytest.CollectReport.result "Link to this definition")

:   The collected items and collection nodes.

```
<!-- -->
```

[[sections]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]]*[¶](#pytest.CollectReport.sections "Link to this definition")

:   Tuples of str [`(heading,`]` `[`content)`] with extra information for the test report. Used by pytest to add text captured from [`stdout`], [`stderr`], and intercepted logging events. May be used by other plugins to add arbitrary information to reports.

```
<!-- -->
```

*[[property]][ ]*[[caplog]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.caplog "Link to this definition")

:   Return captured log lines, if log capturing is enabled.

    ::: versionadded
    [Added in version 3.5.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[capstderr]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.capstderr "Link to this definition")

:   Return captured text from stderr, if capturing is enabled.

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[capstdout]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.capstdout "Link to this definition")

:   Return captured text from stdout, if capturing is enabled.

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[count_towards_summary]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.CollectReport.count_towards_summary "Link to this definition")

:   **Experimental** Whether this report should be counted towards the totals shown at the end of the test session: "1 passed, 1 failure, etc".

    ::: 
    Note

    This function is considered **experimental**, so beware that it is subject to changes even in patch releases.
    :::

```
<!-- -->
```

*[[property]][ ]*[[failed]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.CollectReport.failed "Link to this definition")

:   Whether the outcome is failed.

```
<!-- -->
```

*[[property]][ ]*[[fspath]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.fspath "Link to this definition")

:   The path portion of the reported node, as a string.

```
<!-- -->
```

*[[property]][ ]*[[head_line]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#pytest.CollectReport.head_line "Link to this definition")

:   **Experimental** The head line shown with longrepr output for this report, more commonly during traceback representation during failures:

    ::: 
    ::: highlight
        ________ Test.foo ________
    :::
    :::

    In the example above, the head_line is "Test.foo".

    ::: 
    Note

    This function is considered **experimental**, so beware that it is subject to changes even in patch releases.
    :::

```
<!-- -->
```

*[[property]][ ]*[[longreprtext]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.CollectReport.longreprtext "Link to this definition")

:   Read-only property that returns the full string representation of [`longrepr`].

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[passed]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.CollectReport.passed "Link to this definition")

:   Whether the outcome is passed.

```
<!-- -->
```

*[[property]][ ]*[[skipped]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.CollectReport.skipped "Link to this definition")

:   Whether the outcome is skipped.

### Config[¶](#config "Link to this heading")

*[[final]][ ][[class]][ ]*[[Config]][[[\[source\]]]](../_modules/_pytest/config.html#Config)[¶](#pytest.Config "Link to this definition")

:   Access to configuration values, pluginmanager and plugin hooks.

    Parameters[:]

    :   -   **pluginmanager** ([*PytestPluginManager*](#pytest.PytestPluginManager "pytest.PytestPluginManager")) -- A pytest PluginManager.

        -   **invocation_params** ([*InvocationParams*](#pytest.Config.InvocationParams "pytest.Config.InvocationParams")) -- Object containing parameters regarding the [[`pytest.main()`]](#pytest.main "pytest.main") invocation.

    *[[final]][ ][[class]][ ]*[[InvocationParams]][(]*[[\*]]*, *[[args]]*, *[[plugins]]*, *[[dir]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.InvocationParams)[¶](#pytest.Config.InvocationParams "Link to this definition")

    :   Holds parameters passed during [[`pytest.main()`]](#pytest.main "pytest.main").

        The object attributes are read-only.

        ::: versionadded
        [Added in version 5.1.]
        :::

        ::: 
        Note

        Note that the environment variable [`PYTEST_ADDOPTS`] and the [`addopts`] configuration option are handled by pytest, not being included in the [`args`] attribute.

        Plugins accessing [`InvocationParams`] must be aware of that.
        :::

    [[args]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[\...]][[\]]]*[¶](#pytest.Config.InvocationParams.args "Link to this definition")

    :   The command-line arguments as passed to [[`pytest.main()`]](#pytest.main "pytest.main").

    [[plugins]]*[[:]][ ][[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#pytest.Config.InvocationParams.plugins "Link to this definition")

    :   Extra plugins, might be [`None`].

    [[dir]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Config.InvocationParams.dir "Link to this definition")

    :   The directory from which [[`pytest.main()`]](#pytest.main "pytest.main") was invoked.

```
<!-- -->
```

*[[class]][ ]*[[ArgsSource]][(]*[[\*]][[values]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.ArgsSource)[¶](#pytest.Config.ArgsSource "Link to this definition")

:   Indicates the source of the test arguments.

    ::: versionadded
    [Added in version 7.2.]
    :::

    [[ARGS]]*[ ][[=]][ ][1]*[¶](#pytest.Config.ArgsSource.ARGS "Link to this definition")

    :   Command line arguments.

    [[INVOCATION_DIR]]*[ ][[=]][ ][2]*[¶](#pytest.Config.ArgsSource.INVOCATION_DIR "Link to this definition")

    :   Invocation directory.

    [[TESTPATHS]]*[ ][[=]][ ][3]*[¶](#pytest.Config.ArgsSource.TESTPATHS "Link to this definition")

    :   'testpaths' configuration value.

```
<!-- -->
```

[[option]][¶](#pytest.Config.option "Link to this definition")

:   Access to command line option as attributes.

    Type[:]

    :   [argparse.Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace "(in Python v3.14)")

```
<!-- -->
```

[[invocation_params]][¶](#pytest.Config.invocation_params "Link to this definition")

:   The parameters with which pytest was invoked.

    Type[:]

    :   [InvocationParams](#pytest.Config.InvocationParams "pytest.Config.InvocationParams")

```
<!-- -->
```

[[pluginmanager]][¶](#pytest.Config.pluginmanager "Link to this definition")

:   The plugin manager handles plugin registration and hook invocation.

    Type[:]

    :   [PytestPluginManager](#pytest.PytestPluginManager "pytest.PytestPluginManager")

```
<!-- -->
```

[[stash]][¶](#pytest.Config.stash "Link to this definition")

:   A place where plugins can store information on the config for their own use.

    Type[:]

    :   [Stash](#pytest.Stash "pytest.Stash")

```
<!-- -->
```

*[[property]][ ]*[[rootpath]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Config.rootpath "Link to this definition")

:   The path to the [[rootdir]](customize.html#rootdir).

    ::: versionadded
    [Added in version 6.1.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[inipath]]*[[:]][ ][[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#pytest.Config.inipath "Link to this definition")

:   The path to the [[configfile]](customize.html#configfiles).

    ::: versionadded
    [Added in version 6.1.]
    :::

```
<!-- -->
```

[[add_cleanup]][(]*[[func]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.add_cleanup)[¶](#pytest.Config.add_cleanup "Link to this definition")

:   Add a function to be called when the config object gets out of use (usually coinciding with pytest_unconfigure).

```
<!-- -->
```

*[classmethod]* [[fromdictargs]][(]*[[option_dict]]*, *[[args]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.fromdictargs)[¶](#pytest.Config.fromdictargs "Link to this definition")

:   Constructor usable for subprocesses.

```
<!-- -->
```

[[issue_config_time_warning]][(]*[[warning]]*, *[[stacklevel]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.issue_config_time_warning)[¶](#pytest.Config.issue_config_time_warning "Link to this definition")

:   Issue and handle a warning during the "configure" stage.

    During [`pytest_configure`] we can't capture warnings using the [`catch_warnings_for_item`] function because it is not possible to have hook wrappers around [`pytest_configure`].

    This function is mainly intended for plugins that need to issue warnings during [`pytest_configure`] (or similar stages).

    Parameters[:]

    :   -   **warning** ([*Warning*](https://docs.python.org/3/library/exceptions.html#Warning "(in Python v3.14)")) -- The warning instance.

        -   **stacklevel** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- stacklevel forwarded to warnings.warn.

```
<!-- -->
```

[[addinivalue_line]][(]*[[name]]*, *[[line]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.addinivalue_line)[¶](#pytest.Config.addinivalue_line "Link to this definition")

:   Add a line to a configuration option. The option must have been declared but might not yet be set in which case the line becomes the first line in its value.

```
<!-- -->
```

[[getini]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.getini)[¶](#pytest.Config.getini "Link to this definition")

:   Return configuration value the an [[configuration file]](customize.html#configfiles).

    If a configuration value is not defined in a [[configuration file]](customize.html#configfiles), then the [`default`] value provided while registering the configuration through [[`parser.addini`]](#pytest.Parser.addini "pytest.Parser.addini") will be returned. Please note that you can even provide [`None`] as a valid default value.

    If [`default`] is not provided while registering using [[`parser.addini`]](#pytest.Parser.addini "pytest.Parser.addini"), then a default value based on the [`type`] parameter passed to [[`parser.addini`]](#pytest.Parser.addini "pytest.Parser.addini") will be returned. The default values based on [`type`] are: [`paths`], [`pathlist`], [`args`] and [`linelist`] : empty list [`[]`] [`bool`] : [`False`] [`string`] : empty string [`""`] [`int`] : [`0`] [`float`] : [`0.0`]

    If neither the [`default`] nor the [`type`] parameter is passed while registering the configuration through [[`parser.addini`]](#pytest.Parser.addini "pytest.Parser.addini"), then the configuration is treated as a string and a default empty string '' is returned.

    If the specified name hasn't been registered through a prior [[`parser.addini`]](#pytest.Parser.addini "pytest.Parser.addini") call (usually from a plugin), a ValueError is raised.

```
<!-- -->
```

[[getoption]][(]*[[name]]*, *[[default=\<NOTSET\>]]*, *[[skip=False]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.getoption)[¶](#pytest.Config.getoption "Link to this definition")

:   Return command line option value.

    Parameters[:]

    :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Name of the option. You may also specify the literal [`--OPT`] option instead of the "dest" option name.

        -   **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")) -- Fallback value if no option of that name is **declared** via [[`pytest_addoption`]](#std-hook-pytest_addoption). Note this parameter will be ignored when the option is **declared** even if the option's value is [`None`].

        -   **skip** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`], raise [[`pytest.skip()`]](#pytest.skip "pytest.skip") if option is undeclared or has a [`None`] value. Note that even if [`True`], if a default was specified it will be returned instead of a skip.

```
<!-- -->
```

[[getvalue]][(]*[[name]]*, *[[path]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.getvalue)[¶](#pytest.Config.getvalue "Link to this definition")

:   Deprecated, use getoption() instead.

```
<!-- -->
```

[[getvalueorskip]][(]*[[name]]*, *[[path]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.getvalueorskip)[¶](#pytest.Config.getvalueorskip "Link to this definition")

:   Deprecated, use getoption(skip=True) instead.

```
<!-- -->
```

[[VERBOSITY_ASSERTIONS]]*[[:]][ ][Final][ ][[=]][ ][\'assertions\']*[¶](#pytest.Config.VERBOSITY_ASSERTIONS "Link to this definition")

:   Verbosity type for failed assertions (see [[`verbosity_assertions`]](#confval-verbosity_assertions)).

```
<!-- -->
```

[[VERBOSITY_TEST_CASES]]*[[:]][ ][Final][ ][[=]][ ][\'test_cases\']*[¶](#pytest.Config.VERBOSITY_TEST_CASES "Link to this definition")

:   Verbosity type for test case execution (see [[`verbosity_test_cases`]](#confval-verbosity_test_cases)).

```
<!-- -->
```

[[VERBOSITY_SUBTESTS]]*[[:]][ ][Final][ ][[=]][ ][\'subtests\']*[¶](#pytest.Config.VERBOSITY_SUBTESTS "Link to this definition")

:   Verbosity type for failed subtests (see [[`verbosity_subtests`]](#confval-verbosity_subtests)).

```
<!-- -->
```

[[get_verbosity]][(]*[[verbosity_type]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#Config.get_verbosity)[¶](#pytest.Config.get_verbosity "Link to this definition")

:   Retrieve the verbosity level for a fine-grained verbosity type.

    Parameters[:]

    :   **verbosity_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- Verbosity type to get level for. If a level is configured for the given type, that value will be returned. If the given type is not a known verbosity type, the global verbosity level will be returned. If the given type is None (default), the global verbosity level will be returned.

    To configure a level for a fine-grained verbosity type, the configuration file should have a setting for the configuration name and a numeric value for the verbosity level. A special value of "auto" can be used to explicitly use the global verbosity level.

    Example:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [tool.pytest]
        verbosity_assertions = 2
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_assertions = 2
    :::
    :::
    :::
    :::

    ::: 
    ::: highlight
        pytest -v
    :::
    :::

    ::: 
    ::: highlight
        print(config.get_verbosity())  # 1
        print(config.get_verbosity(Config.VERBOSITY_ASSERTIONS))  # 2
    :::
    :::

### Dir[¶](#dir "Link to this heading")

*[[final]][ ][[class]][ ]*[[Dir]][[[\[source\]]]](../_modules/_pytest/main.html#Dir)[¶](#pytest.Dir "Link to this definition")

:   Collector of files in a file system directory.

    ::: versionadded
    [Added in version 8.0.]
    :::

    ::: 
    Note

    Python directories with an [`__init__.py`] file are instead collected by [[`Package`]](#pytest.Package "pytest.Package") by default. Both are [[`Directory`]](#pytest.Directory "pytest.Directory") collectors.
    :::

```
<!-- -->
```

*[classmethod]* [[from_parent]][(]*[[parent]]*, *[[\*]]*, *[[path]]*[)][[[\[source\]]]](../_modules/_pytest/main.html#Dir.from_parent)[¶](#pytest.Dir.from_parent "Link to this definition")

:   The public constructor.

    Parameters[:]

    :   -   **parent** ([*nodes.Collector*](#pytest.Collector "_pytest.nodes.Collector")) -- The parent collector of this Dir.

        -   **path** ([*pathlib.Path*](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")) -- The directory's path.

```
<!-- -->
```

*[for] [\...] [in]* [[collect]][(][)][[[\[source\]]]](../_modules/_pytest/main.html#Dir.collect)[¶](#pytest.Dir.collect "Link to this definition")

:   Collect children (items and collectors) for this collector.

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Dir.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Dir.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Dir.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Dir.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Dir.session "Link to this definition")

:   The pytest session this node is part of.

### Directory[¶](#directory "Link to this heading")

*[[class]][ ]*[[Directory]][[[\[source\]]]](../_modules/_pytest/nodes.html#Directory)[¶](#pytest.Directory "Link to this definition")

:   Base class for collecting files from a directory.

    A basic directory collector does the following: goes over the files and sub-directories in the directory and creates collectors for them by calling the hooks [[`pytest_collect_directory`]](#std-hook-pytest_collect_directory) and [[`pytest_collect_file`]](#std-hook-pytest_collect_file), after checking that they are not ignored using [[`pytest_ignore_collect`]](#std-hook-pytest_ignore_collect).

    The default directory collectors are [[`Dir`]](#pytest.Dir "pytest.Dir") and [[`Package`]](#pytest.Package "pytest.Package").

    ::: versionadded
    [Added in version 8.0.]
    :::

    [[Using a custom directory collector]](../example/customdirectory.html#custom-directory-collectors).

```
<!-- -->
```

[[config]]*[[:]][ ][[Config]](#pytest.Config "pytest.Config")*[¶](#pytest.Directory.config "Link to this definition")

:   The pytest config object.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Directory.name "Link to this definition")

:   A unique name within the scope of the parent node.

```
<!-- -->
```

[[parent]][¶](#pytest.Directory.parent "Link to this definition")

:   The parent collector node.

```
<!-- -->
```

[[path]]*[[:]][ ][[pathlib.Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*[¶](#pytest.Directory.path "Link to this definition")

:   Filesystem path where this node was collected from (can be None).

```
<!-- -->
```

[[session]]*[[:]][ ][[Session]](#pytest.Session "pytest.Session")*[¶](#pytest.Directory.session "Link to this definition")

:   The pytest session this node is part of.

### ExceptionInfo[¶](#exceptioninfo "Link to this heading")

*[[final]][ ][[class]][ ]*[[ExceptionInfo]][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo)[¶](#pytest.ExceptionInfo "Link to this definition")

:   Wraps sys.exc_info() objects and offers help for navigating the traceback.

```
<!-- -->
```

*[classmethod]* [[from_exception]][(]*[[exception]]*, *[[exprinfo]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.from_exception)[¶](#pytest.ExceptionInfo.from_exception "Link to this definition")

:   Return an ExceptionInfo for an existing exception.

    The exception must have a non-[`None`] [`__traceback__`] attribute, otherwise this function fails with an assertion error. This means that the exception must have been raised, or added a traceback with the [[`with_traceback()`]](https://docs.python.org/3/library/exceptions.html#BaseException.with_traceback "(in Python v3.14)") method.

    Parameters[:]

    :   **exprinfo** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- A text string helping to determine if we should strip [`AssertionError`] from the output. Defaults to the exception message/[`__str__()`].

    ::: versionadded
    [Added in version 7.4.]
    :::

```
<!-- -->
```

*[classmethod]* [[from_exc_info]][(]*[[exc_info]]*, *[[exprinfo]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.from_exc_info)[¶](#pytest.ExceptionInfo.from_exc_info "Link to this definition")

:   Like [[`from_exception()`]](#pytest.ExceptionInfo.from_exception "pytest.ExceptionInfo.from_exception"), but using old-style exc_info tuple.

```
<!-- -->
```

*[classmethod]* [[from_current]][(]*[[exprinfo]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.from_current)[¶](#pytest.ExceptionInfo.from_current "Link to this definition")

:   Return an ExceptionInfo matching the current traceback.

    ::: 
    Warning

    Experimental API
    :::

    Parameters[:]

    :   **exprinfo** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- A text string helping to determine if we should strip [`AssertionError`] from the output. Defaults to the exception message/[`__str__()`].

```
<!-- -->
```

*[classmethod]* [[for_later]][(][)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.for_later)[¶](#pytest.ExceptionInfo.for_later "Link to this definition")

:   Return an unfilled ExceptionInfo.

```
<!-- -->
```

[[fill_unfilled]][(]*[[exc_info]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.fill_unfilled)[¶](#pytest.ExceptionInfo.fill_unfilled "Link to this definition")

:   Fill an unfilled ExceptionInfo created with [`for_later()`].

```
<!-- -->
```

*[[property]][ ]*[[type]]*[[:]][ ][[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][E][[\]]]*[¶](#pytest.ExceptionInfo.type "Link to this definition")

:   The exception class.

```
<!-- -->
```

*[[property]][ ]*[[value]]*[[:]][ ][E]*[¶](#pytest.ExceptionInfo.value "Link to this definition")

:   The exception value.

```
<!-- -->
```

*[[property]][ ]*[[tb]]*[[:]][ ][[TracebackType]](https://docs.python.org/3/library/types.html#types.TracebackType "(in Python v3.14)")*[¶](#pytest.ExceptionInfo.tb "Link to this definition")

:   The exception raw traceback.

```
<!-- -->
```

*[[property]][ ]*[[typename]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.ExceptionInfo.typename "Link to this definition")

:   The type name of the exception.

```
<!-- -->
```

*[[property]][ ]*[[traceback]]*[[:]][ ][Traceback]*[¶](#pytest.ExceptionInfo.traceback "Link to this definition")

:   The traceback.

```
<!-- -->
```

[[exconly]][(]*[[tryshort]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.exconly)[¶](#pytest.ExceptionInfo.exconly "Link to this definition")

:   Return the exception as a string.

    When 'tryshort' resolves to True, and the exception is an AssertionError, only the actual exception part of the exception representation is returned (so 'AssertionError: ' is removed from the beginning).

```
<!-- -->
```

[[errisinstance]][(]*[[exc]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.errisinstance)[¶](#pytest.ExceptionInfo.errisinstance "Link to this definition")

:   Return True if the exception is an instance of exc.

    Consider using [`isinstance(excinfo.value,`]` `[`exc)`] instead.

```
<!-- -->
```

[[getrepr]][(]*[[showlocals]][[=]][[False]]*, *[[style]][[=]][[\'long\']]*, *[[abspath]][[=]][[False]]*, *[[tbfilter]][[=]][[True]]*, *[[funcargs]][[=]][[False]]*, *[[truncate_locals]][[=]][[True]]*, *[[truncate_args]][[=]][[True]]*, *[[chain]][[=]][[True]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.getrepr)[¶](#pytest.ExceptionInfo.getrepr "Link to this definition")

:   Return str()able representation of this exception info.

    Parameters[:]

    :   -   **showlocals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Show locals per traceback entry. Ignored if [`style=="native"`].

        -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- long\|short\|line\|no\|native\|value traceback style.

        -   **abspath** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If paths should be changed to absolute or left unchanged.

        -   **tbfilter** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *\|* [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*\[\[*[*ExceptionInfo*](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]\],* *Traceback\]*) --

            A filter for traceback entries.

            -   If false, don't hide any entries.

            -   If true, hide internal entries and entries that contain a local variable [`__tracebackhide__`]` `[`=`]` `[`True`].

            -   If a callable, delegates the filtering to the callable.

            Ignored if [`style`] is [`"native"`].

        -   **funcargs** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Show fixtures ("funcargs" for legacy purposes) per traceback entry.

        -   **truncate_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- With [`showlocals==True`], make sure locals can be safely represented as strings.

        -   **truncate_args** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- With [`showargs==True`], make sure args can be safely represented as strings.

        -   **chain** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If chained exceptions in Python 3 should be shown.

    ::: versionchanged
    [Changed in version 3.9: ]Added the [`chain`] parameter.
    :::

```
<!-- -->
```

[[match]][(]*[[regexp]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.match)[¶](#pytest.ExceptionInfo.match "Link to this definition")

:   Check whether the regular expression [`regexp`] matches the string representation of the exception using [[`re.search()`]](https://docs.python.org/3/library/re.html#re.search "(in Python v3.14)").

    If it matches [`True`] is returned, otherwise an [`AssertionError`] is raised.

```
<!-- -->
```

[[group_contains]][(]*[[expected_exception]]*, *[[\*]]*, *[[match]][[=]][[None]]*, *[[depth]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/_code/code.html#ExceptionInfo.group_contains)[¶](#pytest.ExceptionInfo.group_contains "Link to this definition")

:   Check whether a captured exception group contains a matching exception.

    Parameters[:]

    :   -   **expected_exception** (*Type\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]* *\|* *Tuple\[Type\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]\]*) -- The expected exception type, or a tuple if one of multiple possible exception types are expected.

        -   **match** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*re.Pattern*](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) --

            If specified, a string containing a regular expression, or a regular expression object, that is tested against the string representation of the exception and its [`PEP-678`]` `[`<https://peps.python.org/pep-0678/>`] [`__notes__`] using [[`re.search()`]](https://docs.python.org/3/library/re.html#re.search "(in Python v3.14)").

            To match a literal string that may contain [[special characters]](https://docs.python.org/3/library/re.html#re-syntax "(in Python v3.14)"), the pattern can first be escaped with [[`re.escape()`]](https://docs.python.org/3/library/re.html#re.escape "(in Python v3.14)").

        -   **depth** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*\]*) -- If [`None`], will search for a matching exception at any nesting depth. If \>= 1, will only match an exception if it's at the specified depth (depth = 1 being the exceptions contained within the topmost exception group).

    ::: versionadded
    [Added in version 8.0.]
    :::

    ::: 
    Warning

    This helper makes it easy to check for the presence of specific exceptions, but it is very bad for checking that the group does *not* contain *any other exceptions*. You should instead consider using [[`pytest.RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup")
    :::

### ExitCode[¶](#exitcode "Link to this heading")

*[[class]][ ]*[[ExitCode]][(]*[[\*]][[values]]*[)][¶](#pytest.ExitCode "Link to this definition")

:   Encodes the valid exit codes by pytest.

    Currently users and plugins may supply other exit codes as well.

    ::: versionadded
    [Added in version 5.0.]
    :::

### FixtureDef[¶](#fixturedef "Link to this heading")

*[[class]][ ]*[[FixtureDef]][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureDef)[¶](#pytest.FixtureDef "Link to this definition")

:   Bases: [[`Generic`]](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")\[[`FixtureValue`]\]

    A container for a fixture definition.

    Note: At this time, only explicitly documented fields and methods are considered public stable API.

```
<!-- -->
```

*[[property]][ ]*[[scope]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'session\']][[,]][ ][[\'package\']][[,]][ ][[\'module\']][[,]][ ][[\'class\']][[,]][ ][[\'function\']][[\]]]*[¶](#pytest.FixtureDef.scope "Link to this definition")

:   Scope string, one of "function", "class", "module", "package", "session".

```
<!-- -->
```

[[execute]][(]*[[request]]*[)][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureDef.execute)[¶](#pytest.FixtureDef.execute "Link to this definition")

:   Return the value of this fixture, executing it if not cached.

### MarkDecorator[¶](#markdecorator "Link to this heading")

*[[class]][ ]*[[MarkDecorator]][[[\[source\]]]](../_modules/_pytest/mark/structures.html#MarkDecorator)[¶](#pytest.MarkDecorator "Link to this definition")

:   A decorator for applying a mark on test functions and classes.

    [`MarkDecorators`] are created with [`pytest.mark`]:

    ::: 
    ::: highlight
        mark1 = pytest.mark.NAME  # Simple MarkDecorator
        mark2 = pytest.mark.NAME(name1=value)  # Parametrized MarkDecorator
    :::
    :::

    and can then be applied as decorators to test functions:

    ::: 
    ::: highlight
        @mark2
        def test_function():
            pass
    :::
    :::

    When a [`MarkDecorator`] is called, it does the following:

    1.  If called with a single class as its only positional argument and no additional keyword arguments, it attaches the mark to the class so it gets applied automatically to all test cases found in that class.

    2.  If called with a single function as its only positional argument and no additional keyword arguments, it attaches the mark to the function, containing all the arguments already stored internally in the [`MarkDecorator`].

    3.  When called in any other case, it returns a new [`MarkDecorator`] instance with the original [`MarkDecorator`]'s content updated with the arguments passed to this call.

    Note: The rules above prevent a [`MarkDecorator`] from storing only a single function or class reference as its positional argument with no additional keyword or positional arguments. You can work around this by using [`with_args()`].

```
<!-- -->
```

*[[property]][ ]*[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.MarkDecorator.name "Link to this definition")

:   Alias for mark.name.

```
<!-- -->
```

*[[property]][ ]*[[args]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[,]][ ][[\...]][[\]]]*[¶](#pytest.MarkDecorator.args "Link to this definition")

:   Alias for mark.args.

```
<!-- -->
```

*[[property]][ ]*[[kwargs]]*[[:]][ ][[Mapping]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]*[¶](#pytest.MarkDecorator.kwargs "Link to this definition")

:   Alias for mark.kwargs.

```
<!-- -->
```

[[with_args]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/_pytest/mark/structures.html#MarkDecorator.with_args)[¶](#pytest.MarkDecorator.with_args "Link to this definition")

:   Return a MarkDecorator with extra arguments added.

    Unlike calling the MarkDecorator, with_args() can be used even if the sole argument is a callable/class.

### MarkGenerator[¶](#markgenerator "Link to this heading")

*[[final]][ ][[class]][ ]*[[MarkGenerator]][[[\[source\]]]](../_modules/_pytest/mark/structures.html#MarkGenerator)[¶](#pytest.MarkGenerator "Link to this definition")

:   Factory for [[`MarkDecorator`]](#pytest.MarkDecorator "pytest.MarkDecorator") objects - exposed as a [`pytest.mark`] singleton instance.

    Example:

    ::: 
    ::: highlight
        import pytest

        @pytest.mark.slowtest
        def test_function():
            pass
    :::
    :::

    applies a 'slowtest' [[`Mark`]](#pytest.Mark "pytest.Mark") on [`test_function`].

### Mark[¶](#mark "Link to this heading")

*[[final]][ ][[class]][ ]*[[Mark]][[[\[source\]]]](../_modules/_pytest/mark/structures.html#Mark)[¶](#pytest.Mark "Link to this definition")

:   A pytest mark.

```
<!-- -->
```

[[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.Mark.name "Link to this definition")

:   Name of the mark.

```
<!-- -->
```

[[args]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[,]][ ][[\...]][[\]]]*[¶](#pytest.Mark.args "Link to this definition")

:   Positional arguments of the mark decorator.

```
<!-- -->
```

[[kwargs]]*[[:]][ ][[Mapping]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]*[¶](#pytest.Mark.kwargs "Link to this definition")

:   Keyword arguments of the mark decorator.

```
<!-- -->
```

[[combined_with]][(]*[[other]]*[)][[[\[source\]]]](../_modules/_pytest/mark/structures.html#Mark.combined_with)[¶](#pytest.Mark.combined_with "Link to this definition")

:   Return a new Mark which is a combination of this Mark and another Mark.

    Combines by appending args and merging kwargs.

    Parameters[:]

    :   **other** ([*Mark*](#pytest.Mark "pytest.Mark")) -- The mark to combine with.

    Return type[:]

    :   [Mark](#pytest.Mark "pytest.Mark")

### Metafunc[¶](#metafunc "Link to this heading")

*[[final]][ ][[class]][ ]*[[Metafunc]][[[\[source\]]]](../_modules/_pytest/python.html#Metafunc)[¶](#pytest.Metafunc "Link to this definition")

:   Objects passed to the [[`pytest_generate_tests`]](#std-hook-pytest_generate_tests) hook.

    They help to inspect a test function and to generate tests according to test configuration or values specified in the class or module where a test function is defined.

```
<!-- -->
```

[[definition]][¶](#pytest.Metafunc.definition "Link to this definition")

:   Access to the underlying [[`_pytest.python.FunctionDefinition`]](#pytest.python.FunctionDefinition "_pytest.python.FunctionDefinition").

```
<!-- -->
```

[[config]][¶](#pytest.Metafunc.config "Link to this definition")

:   Access to the [[`pytest.Config`]](#pytest.Config "pytest.Config") object for the test session.

```
<!-- -->
```

[[module]][¶](#pytest.Metafunc.module "Link to this definition")

:   The module object where the test function is defined in.

```
<!-- -->
```

[[function]][¶](#pytest.Metafunc.function "Link to this definition")

:   Underlying Python test function.

```
<!-- -->
```

[[fixturenames]][¶](#pytest.Metafunc.fixturenames "Link to this definition")

:   Set of fixture names required by the test function.

```
<!-- -->
```

[[cls]][¶](#pytest.Metafunc.cls "Link to this definition")

:   Class object where the test function is defined in or [`None`].

```
<!-- -->
```

[[parametrize]][(]*[[argnames]]*, *[[argvalues]]*, *[[indirect]][[=]][[False]]*, *[[ids]][[=]][[None]]*, *[[scope]][[=]][[None]]*, *[[\*]]*, *[[\_param_mark]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/python.html#Metafunc.parametrize)[¶](#pytest.Metafunc.parametrize "Link to this definition")

:   Add new invocations to the underlying test function using the list of argvalues for the given argnames. Parametrization is performed during the collection phase. If you need to setup expensive resources see about setting [`indirect`] to do it at test setup time instead.

    Can be called multiple times per test function (but only on different argument names), in which case each call parametrizes all previous parametrizations, e.g.

    ::: 
    ::: highlight
        unparametrized:         t
        parametrize ["x", "y"]: t[x], t[y]
        parametrize [1, 2]:     t[x-1], t[x-2], t[y-1], t[y-2]
    :::
    :::

    Parameters[:]

    :   -   **argnames** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- A comma-separated string denoting one or more argument names, or a list/tuple of argument strings.

        -   **argvalues** ([*Iterable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")*\[ParameterSet* *\|* [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")*\]* *\|* [*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")*\]*) --

            The list of argvalues determines how often a test is invoked with different argument values.

            If only one argname was specified argvalues is a list of values. If N argnames were specified, argvalues must be a list of N-tuples, where each tuple-element specifies a value for its respective argname.

        -   **indirect** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *\|* [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- A list of arguments' names (subset of argnames) or a boolean. If True the list contains all names from the argnames. Each argvalue corresponding to an argname in this list will be passed as request.param to its respective argname fixture function so that it can perform more expensive setups during the setup phase of a test rather than at collection time.

        -   **ids** ([*Iterable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")*\[*[*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)") *\|* *None\]* *\|* [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*\[\[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*\],* [*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)") *\|* *None\]* *\|* *None*) --

            Sequence of (or generator for) ids for [`argvalues`], or a callable to return part of the id for each argvalue.

            With sequences (and generators like [`itertools.count()`]) the returned ids should be of type [`string`], [`int`], [`float`], [`bool`], or [`None`]. They are mapped to the corresponding index in [`argvalues`]. [`None`] means to use the auto-generated id.

            ::: versionadded
            [Added in version 8.4: ][[pytest.HIDDEN_PARAM]](#hidden-param) means to hide the parameter set from the test name. Can only be used at most 1 time, as test names need to be unique.
            :::

            If it is a callable it will be called for each entry in [`argvalues`], and the return value is used as part of the auto-generated id for the whole set (where parts are joined with dashes ("-")). This is useful to provide more specific ids for certain items, e.g. dates. Returning [`None`] will use an auto-generated id.

            If no ids are provided they will be generated automatically from the argvalues.

        -   **scope** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")*\[\'session\',* *\'package\',* *\'module\',* *\'class\',* *\'function\'\]* *\|* *None*) -- If specified it denotes the scope of the parameters. The scope is used for grouping tests by parameter instances. It will also override any fixture-function defined scope, allowing to set a dynamic scope using test context or configuration.

### Parser[¶](#parser "Link to this heading")

*[[final]][ ][[class]][ ]*[[Parser]][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser)[¶](#pytest.Parser "Link to this definition")

:   Parser for command line arguments and config-file values.

    Variables[:]

    :   **extra_info** -- Dict of generic param -\> value to display in case there's an error processing the command line arguments.

    [[getgroup]][(]*[[name]]*, *[[description]][[=]][[\'\']]*, *[[after]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser.getgroup)[¶](#pytest.Parser.getgroup "Link to this definition")

    :   Get (or create) a named option Group.

        Parameters[:]

        :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Name of the option group.

            -   **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Long description for --help output.

            -   **after** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- Name of another group, used for ordering --help output.

        Returns[:]

        :   The option group.

        Return type[:]

        :   [*OptionGroup*](#pytest.OptionGroup "_pytest.config.argparsing.OptionGroup")

        The returned group object has an [`addoption`] method with the same signature as [[`parser.addoption`]](#pytest.Parser.addoption "pytest.Parser.addoption") but will be shown in the respective group in the output of [`pytest`]` `[`--help`].

    [[addoption]][(]*[[\*]][[opts]]*, *[[\*\*]][[attrs]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser.addoption)[¶](#pytest.Parser.addoption "Link to this definition")

    :   Register a command line option.

        Parameters[:]

        :   -   **opts** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Option names, can be short or long options.

            -   **attrs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")) -- Same attributes as the argparse library's [[`add_argument()`]](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "(in Python v3.14)") function accepts.

        After command line parsing, options are available on the pytest config object via [`config.option.NAME`] where [`NAME`] is usually set by passing a [`dest`] attribute, for example [`addoption("--long",`]` `[`dest="NAME",`]` `[`...)`].

    [[parse_known_args]][(]*[[args]]*, *[[namespace]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser.parse_known_args)[¶](#pytest.Parser.parse_known_args "Link to this definition")

    :   Parse the known arguments at this point.

        Returns[:]

        :   An argparse namespace object.

        Return type[:]

        :   [*Namespace*](https://docs.python.org/3/library/argparse.html#argparse.Namespace "(in Python v3.14)")

    [[parse_known_and_unknown_args]][(]*[[args]]*, *[[namespace]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser.parse_known_and_unknown_args)[¶](#pytest.Parser.parse_known_and_unknown_args "Link to this definition")

    :   Parse the known arguments at this point, and also return the remaining unknown flag arguments.

        Returns[:]

        :   A tuple containing an argparse namespace object for the known arguments, and a list of unknown flag arguments.

        Return type[:]

        :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")\[[*Namespace*](https://docs.python.org/3/library/argparse.html#argparse.Namespace "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\]\]

    [[addini]][(]*[[name]]*, *[[help]]*, *[[type=None]]*, *[[default=\<notset\>]]*, *[[\*]]*, *[[aliases=()]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#Parser.addini)[¶](#pytest.Parser.addini "Link to this definition")

    :   Register a configuration file option.

        Parameters[:]

        :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Name of the configuration.

            -   **type** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")*\[\'string\',* *\'paths\',* *\'pathlist\',* *\'args\',* *\'linelist\',* *\'bool\',* *\'int\',* *\'float\'\]* *\|* *None*) --

                Type of the configuration. Can be:

                > <div>
                >
                > -   [`string`]: a string
                >
                > -   [`bool`]: a boolean
                >
                > -   [`args`]: a list of strings, separated as in a shell
                >
                > -   [`linelist`]: a list of strings, separated by line breaks
                >
                > -   [`paths`]: a list of [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)"), separated as in a shell
                >
                > -   [`pathlist`]: a list of [`py.path`], separated as in a shell
                >
                > -   [`int`]: an integer
                >
                > -   [`float`]: a floating-point number
                >
                > ::: versionadded
                > [Added in version 8.4: ]The [`float`] and [`int`] types.
                > :::
                >
                > </div>

                For [`paths`] and [`pathlist`] types, they are considered relative to the config-file. In case the execution is happening without a config-file defined, they will be considered relative to the current working directory (for example with [`--override-ini`]).

                ::: versionadded
                [Added in version 7.0: ]The [`paths`] variable type.
                :::

                ::: versionadded
                [Added in version 8.1: ]Use the current working directory to resolve [`paths`] and [`pathlist`] in the absence of a config-file.
                :::

                Defaults to [`string`] if [`None`] or not passed.

            -   **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")) -- Default value if no config-file option exists but is queried.

            -   **aliases** ([*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) --

                Additional names by which this option can be referenced. Aliases resolve to the canonical name.

                ::: versionadded
                [Added in version 9.0: ]The [`aliases`] parameter.
                :::

        The value of configuration keys can be retrieved via a call to [[`config.getini(name)`]](#pytest.Config.getini "pytest.Config.getini").

### OptionGroup[¶](#optiongroup "Link to this heading")

*[[class]][ ]*[[OptionGroup]][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#OptionGroup)[¶](#pytest.OptionGroup "Link to this definition")

:   A group of options shown in its own section.

```
<!-- -->
```

[[addoption]][(]*[[\*]][[opts]]*, *[[\*\*]][[attrs]]*[)][[[\[source\]]]](../_modules/_pytest/config/argparsing.html#OptionGroup.addoption)[¶](#pytest.OptionGroup.addoption "Link to this definition")

:   Add an option to this group.

    If a shortened version of a long option is specified, it will be suppressed in the help. [`addoption('--twowords',`]` `[`'--two-words')`] results in help showing [`--two-words`] only, but [`--twowords`] gets accepted **and** the automatic destination is in [`args.twowords`].

    Parameters[:]

    :   -   **opts** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Option names, can be short or long options.

        -   **attrs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")) -- Same attributes as the argparse library's [[`add_argument()`]](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "(in Python v3.14)") function accepts.

### PytestPluginManager[¶](#pytestpluginmanager "Link to this heading")

*[[final]][ ][[class]][ ]*[[PytestPluginManager]][[[\[source\]]]](../_modules/_pytest/config.html#PytestPluginManager)[¶](#pytest.PytestPluginManager "Link to this definition")

:   Bases: [[`PluginManager`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluginManager "(in pluggy v0.1)")

    A [[`pluggy.PluginManager`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluginManager "(in pluggy v0.1)") with additional pytest-specific functionality:

    -   Loading plugins from the command line, [`PYTEST_PLUGINS`] env variable and [`pytest_plugins`] global variables found in plugins being loaded.

    -   [`conftest.py`] loading during start-up.

```
<!-- -->
```

[[register]][(]*[[plugin]]*, *[[name]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#PytestPluginManager.register)[¶](#pytest.PytestPluginManager.register "Link to this definition")

:   Register a plugin and return its name.

    Parameters[:]

    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- The name under which to register the plugin. If not specified, a name is generated using [[`get_canonical_name()`]](#pytest.PytestPluginManager.get_canonical_name "pytest.PytestPluginManager.get_canonical_name").

    Returns[:]

    :   The plugin name. If the name is blocked from registering, returns [`None`].

    Return type[:]

    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") \| None

    If the plugin is already registered, raises a [[`ValueError`]](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)").

```
<!-- -->
```

[[getplugin]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#PytestPluginManager.getplugin)[¶](#pytest.PytestPluginManager.getplugin "Link to this definition")

:   

```
<!-- -->
```

[[hasplugin]][(]*[[name]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#PytestPluginManager.hasplugin)[¶](#pytest.PytestPluginManager.hasplugin "Link to this definition")

:   Return whether a plugin with the given name is registered.

```
<!-- -->
```

[[import_plugin]][(]*[[modname]]*, *[[consider_entry_points]][[=]][[False]]*[)][[[\[source\]]]](../_modules/_pytest/config.html#PytestPluginManager.import_plugin)[¶](#pytest.PytestPluginManager.import_plugin "Link to this definition")

:   Import a plugin with [`modname`].

    If [`consider_entry_points`] is True, entry point names are also considered to find a plugin.

```
<!-- -->
```

[[add_hookcall_monitoring]][(]*[[before]]*, *[[after]]*[)][¶](#pytest.PytestPluginManager.add_hookcall_monitoring "Link to this definition")

:   Add before/after tracing functions for all hooks.

    Returns an undo function which, when called, removes the added tracers.

    [`before(hook_name,`]` `[`hook_impls,`]` `[`kwargs)`] will be called ahead of all hook calls and receive a hookcaller instance, a list of HookImpl instances and the keyword arguments for the hook call.

    [`after(outcome,`]` `[`hook_name,`]` `[`hook_impls,`]` `[`kwargs)`] receives the same arguments as [`before`] but also a [[`Result`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.Result "(in pluggy v0.1)") object which represents the result of the overall hook call.

```
<!-- -->
```

[[add_hookspecs]][(]*[[module_or_class]]*[)][¶](#pytest.PytestPluginManager.add_hookspecs "Link to this definition")

:   Add new hook specifications defined in the given [`module_or_class`].

    Functions are recognized as hook specifications if they have been decorated with a matching [`HookspecMarker`].

```
<!-- -->
```

[[check_pending]][(][)][¶](#pytest.PytestPluginManager.check_pending "Link to this definition")

:   Verify that all hooks which have not been verified against a hook specification are optional, otherwise raise [`PluginValidationError`].

```
<!-- -->
```

[[enable_tracing]][(][)][¶](#pytest.PytestPluginManager.enable_tracing "Link to this definition")

:   Enable tracing of hook calls.

    Returns an undo function which, when called, removes the added tracing.

```
<!-- -->
```

[[get_canonical_name]][(]*[[plugin]]*[)][¶](#pytest.PytestPluginManager.get_canonical_name "Link to this definition")

:   Return a canonical name for a plugin object.

    Note that a plugin may be registered under a different name specified by the caller of [[`register(plugin,`]` `[`name)`]](#pytest.PytestPluginManager.register "pytest.PytestPluginManager.register"). To obtain the name of a registered plugin use [[`get_name(plugin)`]](#pytest.PytestPluginManager.get_name "pytest.PytestPluginManager.get_name") instead.

```
<!-- -->
```

[[get_hookcallers]][(]*[[plugin]]*[)][¶](#pytest.PytestPluginManager.get_hookcallers "Link to this definition")

:   Get all hook callers for the specified plugin.

    Returns[:]

    :   The hook callers, or [`None`] if [`plugin`] is not registered in this plugin manager.

    Return type[:]

    :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")\[[*HookCaller*](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.HookCaller "(in pluggy v0.1)")\] \| None

```
<!-- -->
```

[[get_name]][(]*[[plugin]]*[)][¶](#pytest.PytestPluginManager.get_name "Link to this definition")

:   Return the name the plugin is registered under, or [`None`] if is isn't.

```
<!-- -->
```

[[get_plugin]][(]*[[name]]*[)][¶](#pytest.PytestPluginManager.get_plugin "Link to this definition")

:   Return the plugin registered under the given name, if any.

```
<!-- -->
```

[[get_plugins]][(][)][¶](#pytest.PytestPluginManager.get_plugins "Link to this definition")

:   Return a set of all registered plugin objects.

```
<!-- -->
```

[[has_plugin]][(]*[[name]]*[)][¶](#pytest.PytestPluginManager.has_plugin "Link to this definition")

:   Return whether a plugin with the given name is registered.

```
<!-- -->
```

[[is_blocked]][(]*[[name]]*[)][¶](#pytest.PytestPluginManager.is_blocked "Link to this definition")

:   Return whether the given plugin name is blocked.

```
<!-- -->
```

[[is_registered]][(]*[[plugin]]*[)][¶](#pytest.PytestPluginManager.is_registered "Link to this definition")

:   Return whether the plugin is already registered.

```
<!-- -->
```

[[list_name_plugin]][(][)][¶](#pytest.PytestPluginManager.list_name_plugin "Link to this definition")

:   Return a list of (name, plugin) pairs for all registered plugins.

```
<!-- -->
```

[[list_plugin_distinfo]][(][)][¶](#pytest.PytestPluginManager.list_plugin_distinfo "Link to this definition")

:   Return a list of (plugin, distinfo) pairs for all setuptools-registered plugins.

```
<!-- -->
```

[[load_setuptools_entrypoints]][(]*[[group]]*, *[[name]][[=]][[None]]*[)][¶](#pytest.PytestPluginManager.load_setuptools_entrypoints "Link to this definition")

:   Load modules from querying the specified setuptools [`group`].

    Parameters[:]

    :   -   **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Entry point group to load plugins.

        -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *None*) -- If given, loads only plugins with the given [`name`].

    Returns[:]

    :   The number of plugins loaded by this call.

    Return type[:]

    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

```
<!-- -->
```

[[set_blocked]][(]*[[name]]*[)][¶](#pytest.PytestPluginManager.set_blocked "Link to this definition")

:   Block registrations of the given name, unregister if already registered.

```
<!-- -->
```

[[subset_hook_caller]][(]*[[name]]*, *[[remove_plugins]]*[)][¶](#pytest.PytestPluginManager.subset_hook_caller "Link to this definition")

:   Return a proxy [[`HookCaller`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.HookCaller "(in pluggy v0.1)") instance for the named method which manages calls to all registered plugins except the ones from remove_plugins.

```
<!-- -->
```

[[unblock]][(]*[[name]]*[)][¶](#pytest.PytestPluginManager.unblock "Link to this definition")

:   Unblocks a name.

    Returns whether the name was actually blocked.

```
<!-- -->
```

[[unregister]][(]*[[plugin]][[=]][[None]]*, *[[name]][[=]][[None]]*[)][¶](#pytest.PytestPluginManager.unregister "Link to this definition")

:   Unregister a plugin and all of its hook implementations.

    The plugin can be specified either by the plugin object or the plugin name. If both are specified, they must agree.

    Returns the unregistered plugin, or [`None`] if not found.

```
<!-- -->
```

[[project_name]]*[[:]][ ][Final]*[¶](#pytest.PytestPluginManager.project_name "Link to this definition")

:   The project name.

```
<!-- -->
```

[[hook]]*[[:]][ ][Final]*[¶](#pytest.PytestPluginManager.hook "Link to this definition")

:   The "hook relay", used to call a hook on all registered plugins. See [Calling hooks](https://pluggy.readthedocs.io/en/stable/index.html#calling "(in pluggy v0.1)").

```
<!-- -->
```

[[trace]]*[[:]][ ][Final][[\[]][\_tracing.TagTracerSub][[\]]]*[¶](#pytest.PytestPluginManager.trace "Link to this definition")

:   The tracing entry point. See [Built-in tracing](https://pluggy.readthedocs.io/en/stable/index.html#tracing "(in pluggy v0.1)").

### RaisesExc[¶](#raisesexc "Link to this heading")

*[[final]][ ][[class]][ ]*[[RaisesExc]][[[\[source\]]]](../_modules/_pytest/raises.html#RaisesExc)[¶](#pytest.RaisesExc "Link to this definition")

:   ::: versionadded
    [Added in version 8.4.]
    :::

    This is the class constructed when calling [[`pytest.raises()`]](#pytest.raises "pytest.raises"), but may be used directly as a helper class with [[`RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup") when you want to specify requirements on sub-exceptions.

    You don't need this if you only want to specify the type, since [[`RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup") accepts [`type[BaseException]`].

    Parameters[:]

    :   -   **expected_exception** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]* *\|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*\[*[*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\]\]* *\|* *None*) --

            The expected type, or one of several possible types. May be [`None`] in order to only make use of [`match`] and/or [`check`]

            The type is checked with [[`isinstance()`]](https://docs.python.org/3/library/functions.html#isinstance "(in Python v3.14)"), and does not need to be an exact match. If that is wanted you can use the [`check`] parameter.

        -   **match** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* *Pattern\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- A regex to match.

        -   **check** (*Callable\[\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")*\],* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*\]*) -- If specified, a callable that will be called with the exception as a parameter after checking the type and the match regex if specified. If it returns [`True`] it will be considered a match, if not it will be considered a failed match.

    [[`RaisesExc.matches()`]](#pytest.RaisesExc.matches "pytest.RaisesExc.matches") can also be used standalone to check individual exceptions.

    Examples:

    ::: 
    ::: highlight
        with RaisesGroup(RaisesExc(ValueError, match="string"))
            ...
        with RaisesGroup(RaisesExc(check=lambda x: x.args == (3, "hello"))):
            ...
        with RaisesGroup(RaisesExc(check=lambda x: type(x) is ValueError)):
            ...
    :::
    :::

    [[fail_reason]][¶](#pytest.RaisesExc.fail_reason "Link to this definition")

    :   Set after a call to [[`matches()`]](#pytest.RaisesExc.matches "pytest.RaisesExc.matches") to give a human-readable reason for why the match failed. When used as a context manager the string will be printed as the reason for the test failing.

    [[matches]][(]*[[exception]]*[)][[[\[source\]]]](../_modules/_pytest/raises.html#RaisesExc.matches)[¶](#pytest.RaisesExc.matches "Link to this definition")

    :   Check if an exception matches the requirements of this [[`RaisesExc`]](#pytest.RaisesExc "pytest.RaisesExc"). If it fails, [[`RaisesExc.fail_reason`]](#pytest.RaisesExc.fail_reason "pytest.RaisesExc.fail_reason") will be set.

        Examples:

        ::: 
        ::: highlight
            assert RaisesExc(ValueError).matches(my_exception):
            # is equivalent to
            assert isinstance(my_exception, ValueError)

            # this can be useful when checking e.g. the ``__cause__`` of an exception.
            with pytest.raises(ValueError) as excinfo:
                ...
            assert RaisesExc(SyntaxError, match="foo").matches(excinfo.value.__cause__)
            # above line is equivalent to
            assert isinstance(excinfo.value.__cause__, SyntaxError)
            assert re.search("foo", str(excinfo.value.__cause__)
        :::
        :::

### RaisesGroup[¶](#raisesgroup "Link to this heading")

**Tutorial**: [[Assertions about expected exception groups]](../how-to/assert.html#assert-matching-exception-groups)

*[[final]][ ][[class]][ ]*[[RaisesGroup]][[[\[source\]]]](../_modules/_pytest/raises.html#RaisesGroup)[¶](#pytest.RaisesGroup "Link to this definition")

:   ::: versionadded
    [Added in version 8.4.]
    :::

    Contextmanager for checking for an expected [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)"). This works similar to [[`pytest.raises()`]](#pytest.raises "pytest.raises"), but allows for specifying the structure of an [[`ExceptionGroup`]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)"). [[`ExceptionInfo.group_contains()`]](#pytest.ExceptionInfo.group_contains "pytest.ExceptionInfo.group_contains") also tries to handle exception groups, but it is very bad at checking that you *didn't* get unexpected exceptions.

    The catching behaviour differs from [[except\*]](https://docs.python.org/3/reference/compound_stmts.html#except-star "(in Python v3.14)"), being much stricter about the structure by default. By using [`allow_unwrapped=True`] and [`flatten_subgroups=True`] you can match [[except\*]](https://docs.python.org/3/reference/compound_stmts.html#except-star "(in Python v3.14)") fully when expecting a single exception.

    Parameters[:]

    :   -   **args** --

            Any number of exception types, [[`RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup") or [[`RaisesExc`]](#pytest.RaisesExc "pytest.RaisesExc") to specify the exceptions contained in this exception. All specified exceptions must be present in the raised group, *and no others*.

            If you expect a variable number of exceptions you need to use [[`pytest.raises(ExceptionGroup)`]](#pytest.raises "pytest.raises") and manually check the contained exceptions. Consider making use of [[`RaisesExc.matches()`]](#pytest.RaisesExc.matches "pytest.RaisesExc.matches").

            It does not care about the order of the exceptions, so [`RaisesGroup(ValueError,`]` `[`TypeError)`] is equivalent to [`RaisesGroup(TypeError,`]` `[`ValueError)`].

        -   **match** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *\|* [*re.Pattern*](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.14)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]* *\|* *None*) --

            If specified, a string containing a regular expression, or a regular expression object, that is tested against the string representation of the exception group and its [][**PEP 678**](https://peps.python.org/pep-0678/) [`__notes__`] using [[`re.search()`]](https://docs.python.org/3/library/re.html#re.search "(in Python v3.14)").

            To match a literal string that may contain [[special characters]](https://docs.python.org/3/library/re.html#re-syntax "(in Python v3.14)"), the pattern can first be escaped with [[`re.escape()`]](https://docs.python.org/3/library/re.html#re.escape "(in Python v3.14)").

            Note that " (5 subgroups)" will be stripped from the [`repr`] before matching.

        -   **check** (*Callable\[\[E\],* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*\]*) -- If specified, a callable that will be called with the group as a parameter after successfully matching the expected exceptions. If it returns [`True`] it will be considered a match, if not it will be considered a failed match.

        -   **allow_unwrapped** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) --

            If expecting a single exception or [[`RaisesExc`]](#pytest.RaisesExc "pytest.RaisesExc") it will match even if the exception is not inside an exceptiongroup.

            Using this together with [`match`], [`check`] or expecting multiple exceptions will raise an error.

        -   **flatten_subgroups** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- "flatten" any groups inside the raised exception group, extracting all exceptions inside any nested groups, before matching. Without this it expects you to fully specify the nesting structure by passing [[`RaisesGroup`]](#pytest.RaisesGroup "pytest.RaisesGroup") as expected parameter.

    Examples:

    ::: 
    ::: highlight
        with RaisesGroup(ValueError):
            raise ExceptionGroup("", (ValueError(),))
        # match
        with RaisesGroup(
            ValueError,
            ValueError,
            RaisesExc(TypeError, match="^expected int$"),
            match="^my group$",
        ):
            raise ExceptionGroup(
                "my group",
                [
                    ValueError(),
                    TypeError("expected int"),
                    ValueError(),
                ],
            )
        # check
        with RaisesGroup(
            KeyboardInterrupt,
            match="^hello$",
            check=lambda x: isinstance(x.__cause__, ValueError),
        ):
            raise BaseExceptionGroup("hello", [KeyboardInterrupt()]) from ValueError
        # nested groups
        with RaisesGroup(RaisesGroup(ValueError)):
            raise ExceptionGroup("", (ExceptionGroup("", (ValueError(),)),))

        # flatten_subgroups
        with RaisesGroup(ValueError, flatten_subgroups=True):
            raise ExceptionGroup("", (ExceptionGroup("", (ValueError(),)),))

        # allow_unwrapped
        with RaisesGroup(ValueError, allow_unwrapped=True):
            raise ValueError
    :::
    :::

    [[`RaisesGroup.matches()`]](#pytest.RaisesGroup.matches "pytest.RaisesGroup.matches") can also be used directly to check a standalone exception group.

    The matching algorithm is greedy, which means cases such as this may fail:

    ::: 
    ::: highlight
        with RaisesGroup(ValueError, RaisesExc(ValueError, match="hello")):
            raise ExceptionGroup("", (ValueError("hello"), ValueError("goodbye")))
    :::
    :::

    even though it generally does not care about the order of the exceptions in the group. To avoid the above you should specify the first [[`ValueError`]](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") with a [[`RaisesExc`]](#pytest.RaisesExc "pytest.RaisesExc") as well.

    ::: 
    Note

    When raised exceptions don't match the expected ones, you'll get a detailed error message explaining why. This includes [`repr(check)`] if set, which in Python can be overly verbose, showing memory locations etc etc.

    If installed and imported (in e.g. [`conftest.py`]), the [`hypothesis`] library will monkeypatch this output to provide shorter & more readable repr's.
    :::

    [[fail_reason]][¶](#pytest.RaisesGroup.fail_reason "Link to this definition")

    :   Set after a call to [[`matches()`]](#pytest.RaisesGroup.matches "pytest.RaisesGroup.matches") to give a human-readable reason for why the match failed. When used as a context manager the string will be printed as the reason for the test failing.

    [[matches]][(]*[[exception]][[:]][ ][[[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[TypeGuard][[\[]][[ExceptionGroup]](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)")[[\[]][ExcT_1][[\]]][[\]]]]][[[\[source\]]]](../_modules/_pytest/raises.html#RaisesGroup.matches)[¶](#pytest.RaisesGroup.matches "Link to this definition")\
    [[matches]][(]*[[exception]][[:]][ ][[[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[TypeGuard][[\[]][[BaseExceptionGroup]](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "(in Python v3.14)")[[\[]][BaseExcT_1][[\]]][[\]]]]]

    :   Check if an exception matches the requirements of this RaisesGroup. If it fails, [`RaisesGroup.fail_reason`] will be set.

        Example:

        ::: 
        ::: highlight
            with pytest.raises(TypeError) as excinfo:
                ...
            assert RaisesGroup(ValueError).matches(excinfo.value.__cause__)
            # the above line is equivalent to
            myexc = excinfo.value.__cause
            assert isinstance(myexc, BaseExceptionGroup)
            assert len(myexc.exceptions) == 1
            assert isinstance(myexc.exceptions[0], ValueError)
        :::
        :::

### TerminalReporter[¶](#terminalreporter "Link to this heading")

*[[final]][ ][[class]][ ]*[[TerminalReporter]][(]*[[config]]*, *[[file]][[=]][[None]]*[)][[[\[source\]]]](../_modules/_pytest/terminal.html#TerminalReporter)[¶](#pytest.TerminalReporter "Link to this definition")

:   

```
<!-- -->
```

[[wrap_write]][(]*[[content]]*, *[[\*]]*, *[[flush]][[=]][[False]]*, *[[margin]][[=]][[8]]*, *[[line_sep]][[=]][[\'\\n\']]*, *[[\*\*]][[markup]]*[)][[[\[source\]]]](../_modules/_pytest/terminal.html#TerminalReporter.wrap_write)[¶](#pytest.TerminalReporter.wrap_write "Link to this definition")

:   Wrap message with margin for progress info.

```
<!-- -->
```

[[rewrite]][(]*[[line]]*, *[[\*\*]][[markup]]*[)][[[\[source\]]]](../_modules/_pytest/terminal.html#TerminalReporter.rewrite)[¶](#pytest.TerminalReporter.rewrite "Link to this definition")

:   Rewinds the terminal cursor to the beginning and writes the given line.

    Parameters[:]

    :   **erase** -- If True, will also add spaces until the full terminal width to ensure previous lines are properly erased.

    The rest of the keyword arguments are markup instructions.

```
<!-- -->
```

[[build_summary_stats_line]][(][)][[[\[source\]]]](../_modules/_pytest/terminal.html#TerminalReporter.build_summary_stats_line)[¶](#pytest.TerminalReporter.build_summary_stats_line "Link to this definition")

:   Build the parts used in the last summary stats line.

    The summary stats line is the line shown at the end, "=== 12 passed, 2 errors in Xs===".

    This function builds a list of the "parts" that make up for the text in that line, in the example above it would be:

    ::: 
    ::: highlight
        [
            ("12 passed", ),
            ("2 errors", 
        ]
    :::
    :::

    That last dict for each line is a "markup dictionary", used by TerminalWriter to color output.

    The final color of the line is also determined by this function, and is the second element of the returned tuple.

### TestReport[¶](#testreport "Link to this heading")

*[[class]][ ]*[[TestReport]][[[\[source\]]]](../_modules/_pytest/reports.html#TestReport)[¶](#pytest.TestReport "Link to this definition")

:   Bases: [`BaseReport`]

    Basic test report object (also used for setup and teardown calls if they fail).

    Reports can contain arbitrary extra attributes.

```
<!-- -->
```

[[nodeid]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.nodeid "Link to this definition")

:   Normalized collection nodeid.

```
<!-- -->
```

[[location]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#pytest.TestReport.location "Link to this definition")

:   A (filesystempath, lineno, domaininfo) tuple indicating the actual location of a test item - it might be different from the collected one e.g. if a method is inherited from a different module. The filesystempath may be relative to [`config.rootdir`]. The line number is 0-based.

```
<!-- -->
```

[[keywords]]*[[:]][ ][[Mapping]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]]*[¶](#pytest.TestReport.keywords "Link to this definition")

:   A name -\> value dictionary containing all keywords and markers associated with a test invocation.

```
<!-- -->
```

[[outcome]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'passed\']][[,]][ ][[\'failed\']][[,]][ ][[\'skipped\']][[\]]]*[¶](#pytest.TestReport.outcome "Link to this definition")

:   Test outcome, always one of "passed", "failed", "skipped".

```
<!-- -->
```

[[longrepr]]*[[:]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[ExceptionInfo]](#pytest.ExceptionInfo "_pytest._code.code.ExceptionInfo")[[\[]][[BaseException]](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.14)")[[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][TerminalRepr]*[¶](#pytest.TestReport.longrepr "Link to this definition")

:   None or a failure representation.

```
<!-- -->
```

[[when]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'setup\']][[,]][ ][[\'call\']][[,]][ ][[\'teardown\']][[\]]]*[¶](#pytest.TestReport.when "Link to this definition")

:   One of 'setup', 'call', 'teardown' to indicate runtest phase.

```
<!-- -->
```

[[user_properties]][¶](#pytest.TestReport.user_properties "Link to this definition")

:   User properties is a list of tuples (name, value) that holds user defined properties of the test.

```
<!-- -->
```

[[sections]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]]*[¶](#pytest.TestReport.sections "Link to this definition")

:   Tuples of str [`(heading,`]` `[`content)`] with extra information for the test report. Used by pytest to add text captured from [`stdout`], [`stderr`], and intercepted logging events. May be used by other plugins to add arbitrary information to reports.

```
<!-- -->
```

[[duration]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.TestReport.duration "Link to this definition")

:   Time it took to run just the test.

```
<!-- -->
```

[[start]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.TestReport.start "Link to this definition")

:   The system time when the call started, in seconds since the epoch.

```
<!-- -->
```

[[stop]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#pytest.TestReport.stop "Link to this definition")

:   The system time when the call ended, in seconds since the epoch.

```
<!-- -->
```

*[classmethod]* [[from_item_and_call]][(]*[[item]]*, *[[call]]*[)][[[\[source\]]]](../_modules/_pytest/reports.html#TestReport.from_item_and_call)[¶](#pytest.TestReport.from_item_and_call "Link to this definition")

:   Create and fill a TestReport with standard item and call info.

    Parameters[:]

    :   -   **item** ([*Item*](#pytest.Item "pytest.Item")) -- The item.

        -   **call** ([*CallInfo*](#pytest.CallInfo "pytest.CallInfo")*\[None\]*) -- The call info.

```
<!-- -->
```

*[[property]][ ]*[[caplog]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.caplog "Link to this definition")

:   Return captured log lines, if log capturing is enabled.

    ::: versionadded
    [Added in version 3.5.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[capstderr]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.capstderr "Link to this definition")

:   Return captured text from stderr, if capturing is enabled.

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[capstdout]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.capstdout "Link to this definition")

:   Return captured text from stdout, if capturing is enabled.

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[count_towards_summary]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.TestReport.count_towards_summary "Link to this definition")

:   **Experimental** Whether this report should be counted towards the totals shown at the end of the test session: "1 passed, 1 failure, etc".

    ::: 
    Note

    This function is considered **experimental**, so beware that it is subject to changes even in patch releases.
    :::

```
<!-- -->
```

*[[property]][ ]*[[failed]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.TestReport.failed "Link to this definition")

:   Whether the outcome is failed.

```
<!-- -->
```

*[[property]][ ]*[[fspath]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.fspath "Link to this definition")

:   The path portion of the reported node, as a string.

```
<!-- -->
```

*[[property]][ ]*[[head_line]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#pytest.TestReport.head_line "Link to this definition")

:   **Experimental** The head line shown with longrepr output for this report, more commonly during traceback representation during failures:

    ::: 
    ::: highlight
        ________ Test.foo ________
    :::
    :::

    In the example above, the head_line is "Test.foo".

    ::: 
    Note

    This function is considered **experimental**, so beware that it is subject to changes even in patch releases.
    :::

```
<!-- -->
```

*[[property]][ ]*[[longreprtext]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestReport.longreprtext "Link to this definition")

:   Read-only property that returns the full string representation of [`longrepr`].

    ::: versionadded
    [Added in version 3.0.]
    :::

```
<!-- -->
```

*[[property]][ ]*[[passed]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.TestReport.passed "Link to this definition")

:   Whether the outcome is passed.

```
<!-- -->
```

*[[property]][ ]*[[skipped]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[¶](#pytest.TestReport.skipped "Link to this definition")

:   Whether the outcome is skipped.

### TestShortLogReport[¶](#testshortlogreport "Link to this heading")

*[[class]][ ]*[[TestShortLogReport]][[[\[source\]]]](../_modules/_pytest/terminal.html#TestShortLogReport)[¶](#pytest.TestShortLogReport "Link to this definition")

:   Used to store the test status result category, shortletter and verbose word. For example [`"rerun",`]` `[`"R",`]` `[`("RERUN",`]` `[`]` `[`True})`].

    Variables[:]

    :   -   **category** -- The class of result, for example [`“passed”`], [`“skipped”`], [`“error”`], or the empty string.

        -   **letter** -- The short letter shown as testing progresses, for example [`"."`], [`"s"`], [`"E"`], or the empty string.

        -   **word** -- Verbose word is shown as testing progresses in verbose mode, for example [`"PASSED"`], [`"SKIPPED"`], [`"ERROR"`], or the empty string.

    [[category]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestShortLogReport.category "Link to this definition")

    :   Alias for field number 0

    [[letter]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#pytest.TestShortLogReport.letter "Link to this definition")

    :   Alias for field number 1

    [[word]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Mapping]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]][[\]]]*[¶](#pytest.TestShortLogReport.word "Link to this definition")

    :   Alias for field number 2

### Result[¶](#result "Link to this heading")

Result object used within [[hook wrappers]](../how-to/writing_hook_functions.html#hookwrapper), see [[`Result`]` `[`in`]` `[`the`]` `[`pluggy`]` `[`documentation`]](https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.Result "(in pluggy v0.1)") for more information.

### Stash[¶](#stash "Link to this heading")

*[[class]][ ]*[[Stash]][[[\[source\]]]](../_modules/_pytest/stash.html#Stash)[¶](#pytest.Stash "Link to this definition")

:   [`Stash`] is a type-safe heterogeneous mutable mapping that allows keys and value types to be defined separately from where it (the [`Stash`]) is created.

    Usually you will be given an object which has a [`Stash`], for example [[`Config`]](#pytest.Config "pytest.Config") or a [[`Node`]](#pytest.nodes.Node "_pytest.nodes.Node"):

    ::: 
    ::: highlight
        stash: Stash = some_object.stash
    :::
    :::

    If a module or plugin wants to store data in this [`Stash`], it creates [[`StashKey`]](#pytest.StashKey "pytest.StashKey")s for its keys (at the module level):

    ::: 
    ::: highlight
        # At the top-level of the module
        some_str_key = StashKey[str]()
        some_bool_key = StashKey[bool]()
    :::
    :::

    To store information:

    ::: 
    ::: highlight
        # Value type must match the key.
        stash[some_str_key] = "value"
        stash[some_bool_key] = True
    :::
    :::

    To retrieve the information:

    ::: 
    ::: highlight
        # The static type of some_str is str.
        some_str = stash[some_str_key]
        # The static type of some_bool is bool.
        some_bool = stash[some_bool_key]
    :::
    :::

    ::: versionadded
    [Added in version 7.0.]
    :::

```
<!-- -->
```

[[\_\_setitem\_\_]][(]*[[key]]*, *[[value]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.__setitem__)[¶](#pytest.Stash.__setitem__ "Link to this definition")

:   Set a value for key.

```
<!-- -->
```

[[\_\_getitem\_\_]][(]*[[key]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.__getitem__)[¶](#pytest.Stash.__getitem__ "Link to this definition")

:   Get the value for key.

    Raises [`KeyError`] if the key wasn't set before.

```
<!-- -->
```

[[get]][(]*[[key]]*, *[[default]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.get)[¶](#pytest.Stash.get "Link to this definition")

:   Get the value for key, or return default if the key wasn't set before.

```
<!-- -->
```

[[setdefault]][(]*[[key]]*, *[[default]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.setdefault)[¶](#pytest.Stash.setdefault "Link to this definition")

:   Return the value of key if already set, otherwise set the value of key to default and return default.

```
<!-- -->
```

[[\_\_delitem\_\_]][(]*[[key]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.__delitem__)[¶](#pytest.Stash.__delitem__ "Link to this definition")

:   Delete the value for key.

    Raises [`KeyError`] if the key wasn't set before.

```
<!-- -->
```

[[\_\_contains\_\_]][(]*[[key]]*[)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.__contains__)[¶](#pytest.Stash.__contains__ "Link to this definition")

:   Return whether key was set.

```
<!-- -->
```

[[\_\_len\_\_]][(][)][[[\[source\]]]](../_modules/_pytest/stash.html#Stash.__len__)[¶](#pytest.Stash.__len__ "Link to this definition")

:   Return how many items exist in the stash.

```
<!-- -->
```

*[[class]][ ]*[[StashKey]][[[\[source\]]]](../_modules/_pytest/stash.html#StashKey)[¶](#pytest.StashKey "Link to this definition")

:   Bases: [[`Generic`]](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")\[[`T`]\]

    [`StashKey`] is an object used as a key to a [[`Stash`]](#pytest.Stash "pytest.Stash").

    A [`StashKey`] is associated with the type [`T`] of the value of the key.

    A [`StashKey`] is unique and cannot conflict with another key.

    ::: versionadded
    [Added in version 7.0.]
    :::

## Global Variables[¶](#global-variables "Link to this heading")

pytest treats some global variables in a special manner when defined in a test module or [`conftest.py`] files.

[[collect_ignore]][¶](#globalvar-collect_ignore "Link to this definition")

:   

**Tutorial**: [[Customizing test collection]](../example/pythoncollection.html#customizing-test-collection)

Can be declared in *conftest.py files* to exclude test directories or modules. Needs to be a list of paths ([`str`], [[`pathlib.Path`]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") or any [[`os.PathLike`]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")).

    collect_ignore = ["setup.py"]

[[collect_ignore_glob]][¶](#globalvar-collect_ignore_glob "Link to this definition")

:   

**Tutorial**: [[Customizing test collection]](../example/pythoncollection.html#customizing-test-collection)

Can be declared in *conftest.py files* to exclude test directories or modules with Unix shell-style wildcards. Needs to be [`list[str]`] where [`str`] can contain glob patterns.

    collect_ignore_glob = ["*_ignore.py"]

[[pytest_plugins]][¶](#globalvar-pytest_plugins "Link to this definition")

:   

**Tutorial**: [[Requiring/Loading plugins in a test module or conftest file]](../how-to/plugins.html#available-installable-plugins)

Can be declared at the **global** level in *test modules* and *conftest.py files* to register additional plugins. Can be either a [`str`] or [`Sequence[str]`].

    pytest_plugins = "myapp.testsupport.myplugin"

    pytest_plugins = ("myapp.testsupport.tools", "myapp.testsupport.regression")

[[pytestmark]][¶](#globalvar-pytestmark "Link to this definition")

:   

**Tutorial**: [[Marking whole classes or modules]](../example/markers.html#scoped-marking)

Can be declared at the **global** level in *test modules* to apply one or more [[marks]](#marks-ref) to all test functions and methods. Can be either a single mark or a list of marks (applied in left-to-right order).

    import pytest

    pytestmark = pytest.mark.webtest

    import pytest

    pytestmark = [pytest.mark.integration, pytest.mark.slow]

## Environment Variables[¶](#environment-variables "Link to this heading")

Environment variables that can be used to change pytest's behavior.

[[CI]][¶](#envvar-CI "Link to this definition")

:   

When set to a non-empty value, pytest acknowledges that is running in a CI process. See also [[CI Pipelines]](../explanation/ci.html#ci-pipelines).

[[BUILD_NUMBER]][¶](#envvar-BUILD_NUMBER "Link to this definition")

:   

When set to a non-empty value, pytest acknowledges that is running in a CI process. Alternative to [][[`CI`]](#envvar-CI). See also [[CI Pipelines]](../explanation/ci.html#ci-pipelines).

[[PYTEST_ADDOPTS]][¶](#envvar-PYTEST_ADDOPTS "Link to this definition")

:   

This contains a command-line (parsed by the py:mod:[`shlex`] module) that will be **prepended** to the command line given by the user, see [[Builtin configuration file options]](customize.html#adding-default-options) for more information.

[[PYTEST_VERSION]][¶](#envvar-PYTEST_VERSION "Link to this definition")

:   

This environment variable is defined at the start of the pytest session and is undefined afterwards. It contains the value of [`pytest.__version__`], and among other things can be used to easily check if a code is running from within a pytest run.

[[PYTEST_CURRENT_TEST]][¶](#envvar-PYTEST_CURRENT_TEST "Link to this definition")

:   

This is not meant to be set by users, but is set by pytest internally with the name of the current test so other processes can inspect it, see [[PYTEST_CURRENT_TEST environment variable]](../example/simple.html#pytest-current-test-env) for more information.

[[PYTEST_DEBUG]][¶](#envvar-PYTEST_DEBUG "Link to this definition")

:   

When set, pytest will print tracing and debug information.

[[PYTEST_DEBUG_TEMPROOT]][¶](#envvar-PYTEST_DEBUG_TEMPROOT "Link to this definition")

:   

Root for temporary directories produced by fixtures like [[`tmp_path`]](#std-fixture-tmp_path) as discussed in [[Temporary directory location and retention]](../how-to/tmp_path.html#temporary-directory-location-and-retention).

[[PYTEST_DISABLE_PLUGIN_AUTOLOAD]][¶](#envvar-PYTEST_DISABLE_PLUGIN_AUTOLOAD "Link to this definition")

:   

When set, disables plugin auto-loading through [[entry point packaging metadata]](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/ "(in Python Packaging User Guide)"). Only plugins explicitly specified in [][[`PYTEST_PLUGINS`]](#envvar-PYTEST_PLUGINS) or with [[`-p`]](#cmdoption-p) will be loaded. See also [[--disable-plugin-autoload]](../how-to/plugins.html#disable-plugin-autoload).

[[PYTEST_PLUGINS]][¶](#envvar-PYTEST_PLUGINS "Link to this definition")

:   

Contains comma-separated list of modules that should be loaded as plugins:

    export PYTEST_PLUGINS=mymodule.plugin,xdist

See also [[`-p`]](#cmdoption-p).

[[PYTEST_THEME]][¶](#envvar-PYTEST_THEME "Link to this definition")

:   

Sets a [pygment style](https://pygments.org/docs/styles/) to use for the code output.

[[PYTEST_THEME_MODE]][¶](#envvar-PYTEST_THEME_MODE "Link to this definition")

:   

Sets the [][[`PYTEST_THEME`]](#envvar-PYTEST_THEME) to be either *dark* or *light*.

[[PY_COLORS]][¶](#envvar-PY_COLORS "Link to this definition")

:   

When set to [`1`], pytest will use color in terminal output. When set to [`0`], pytest will not use color. [`PY_COLORS`] takes precedence over [`NO_COLOR`] and [`FORCE_COLOR`].

[[NO_COLOR]][¶](#envvar-NO_COLOR "Link to this definition")

:   

When set to a non-empty string (regardless of value), pytest will not use color in terminal output. [`PY_COLORS`] takes precedence over [`NO_COLOR`], which takes precedence over [`FORCE_COLOR`]. See [no-color.org](https://no-color.org/) for other libraries supporting this community standard.

[[FORCE_COLOR]][¶](#envvar-FORCE_COLOR "Link to this definition")

:   

When set to a non-empty string (regardless of value), pytest will use color in terminal output. [`PY_COLORS`] and [`NO_COLOR`] take precedence over [`FORCE_COLOR`].

## Exceptions[¶](#exceptions "Link to this heading")

*[[exception]][ ]*[[UsageError]][¶](#pytest.UsageError "Link to this definition")

:   Bases: [[`Exception`]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

    Error in pytest usage or invocation.

```
<!-- -->
```

*[[final]][ ][[exception]][ ]*[[FixtureLookupError]][[[\[source\]]]](../_modules/_pytest/fixtures.html#FixtureLookupError)[¶](#pytest.FixtureLookupError "Link to this definition")

:   Bases: [[`LookupError`]](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)")

    Could not return a requested fixture (missing or invalid).

[]

## Warnings[¶](#warnings "Link to this heading")

Custom warnings generated in some situations such as improper usage or deprecated features.

*[[class]][ ]*[[PytestWarning]][¶](#pytest.PytestWarning "Link to this definition")

:   Bases: [[`UserWarning`]](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.14)")

    Base class for all warnings emitted by pytest.

```
<!-- -->
```

*[[class]][ ]*[[PytestAssertRewriteWarning]][¶](#pytest.PytestAssertRewriteWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted by the pytest assert rewrite module.

```
<!-- -->
```

*[[class]][ ]*[[PytestCacheWarning]][¶](#pytest.PytestCacheWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted by the cache plugin in various situations.

```
<!-- -->
```

*[[class]][ ]*[[PytestCollectionWarning]][¶](#pytest.PytestCollectionWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted when pytest is not able to collect a file or symbol in a module.

```
<!-- -->
```

*[[class]][ ]*[[PytestConfigWarning]][¶](#pytest.PytestConfigWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted for configuration issues.

```
<!-- -->
```

*[[class]][ ]*[[PytestDeprecationWarning]][¶](#pytest.PytestDeprecationWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning"), [[`DeprecationWarning`]](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")

    Warning class for features that will be removed in a future version.

```
<!-- -->
```

*[[class]][ ]*[[PytestExperimentalApiWarning]][¶](#pytest.PytestExperimentalApiWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning"), [[`FutureWarning`]](https://docs.python.org/3/library/exceptions.html#FutureWarning "(in Python v3.14)")

    Warning category used to denote experiments in pytest.

    Use sparingly as the API might change or even be removed completely in a future version.

```
<!-- -->
```

*[[class]][ ]*[[PytestReturnNotNoneWarning]][¶](#pytest.PytestReturnNotNoneWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted when a test function returns a value other than [`None`].

    See [[Returning non-None value in test functions]](../how-to/assert.html#return-not-none) for details.

```
<!-- -->
```

*[[class]][ ]*[[PytestRemovedIn9Warning]][¶](#pytest.PytestRemovedIn9Warning "Link to this definition")

:   Bases: [[`PytestDeprecationWarning`]](#pytest.PytestDeprecationWarning "pytest.PytestDeprecationWarning")

    Warning class for features that will be removed in pytest 9.

```
<!-- -->
```

*[[class]][ ]*[[PytestUnknownMarkWarning]][¶](#pytest.PytestUnknownMarkWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    Warning emitted on use of unknown markers.

    See [[How to mark test functions with attributes]](../how-to/mark.html#mark) for details.

```
<!-- -->
```

*[[class]][ ]*[[PytestUnraisableExceptionWarning]][¶](#pytest.PytestUnraisableExceptionWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    An unraisable exception was reported.

    Unraisable exceptions are exceptions raised in [[`__del__`]](https://docs.python.org/3/reference/datamodel.html#object.__del__ "(in Python v3.14)") implementations and similar situations when the exception cannot be raised as normal.

```
<!-- -->
```

*[[class]][ ]*[[PytestUnhandledThreadExceptionWarning]][¶](#pytest.PytestUnhandledThreadExceptionWarning "Link to this definition")

:   Bases: [[`PytestWarning`]](#pytest.PytestWarning "pytest.PytestWarning")

    An unhandled exception occurred in a [[`Thread`]](https://docs.python.org/3/library/threading.html#threading.Thread "(in Python v3.14)").

    Such exceptions don't propagate normally.

Consult the [[Internal pytest warnings]](../how-to/capture-warnings.html#internal-warnings) section in the documentation for more information.

[]

## Configuration Options[¶](#configuration-options "Link to this heading")

Here is a list of builtin configuration options that may be written in a [`pytest.ini`] (or [`.pytest.ini`]), [`pyproject.toml`], [`tox.ini`], or [`setup.cfg`] file, usually located at the root of your repository.

To see each file format in details, see [[Configuration file formats]](customize.html#config-file-formats).

Warning

Usage of [`setup.cfg`] is not recommended except for very simple use cases. [`.cfg`] files use a different parser than [`pytest.ini`] and [`tox.ini`] which might cause hard to track down problems. When possible, it is recommended to use the latter files, or [`pytest.toml`] or [`pyproject.toml`], to hold your pytest configuration.

Configuration options may be overwritten in the command-line by using [`-o/--override-ini`], which can also be passed multiple times. The expected format is [`name=value`]. For example:

    pytest -o console_output_style=classic -o cache_dir=/tmp/mycache

[[addopts]][¶](#confval-addopts "Link to this definition")

:   Add the specified [`OPTS`] to the set of command line arguments as if they had been specified by the user. Example: if you have this configuration file content:

    ::: 
    ::: highlight
        # content of pytest.toml
        [pytest]
        addopts = ["--maxfail=2", "-rf"]  # exit after 2 failures, report fail info
    :::
    :::

    issuing [`pytest`]` `[`test_hello.py`] actually means:

    ::: 
    ::: highlight
        pytest --maxfail=2 -rf test_hello.py
    :::
    :::

    Default is to add no options.

```
<!-- -->
```

[[cache_dir]][¶](#confval-cache_dir "Link to this definition")

:   Sets the directory where the cache plugin's content is stored. Default directory is [`.pytest_cache`] which is created in [[rootdir]](customize.html#rootdir). Directory may be relative or absolute path. If setting relative path, then directory is created relative to [[rootdir]](customize.html#rootdir). Additionally, a path may contain environment variables, that will be expanded. For more information about cache plugin please refer to [[How to re-run failed tests and maintain state between test runs]](../how-to/cache.html#cache-provider).

```
<!-- -->
```

[[collect_imported_tests]][¶](#confval-collect_imported_tests "Link to this definition")

:   ::: versionadded
    [Added in version 8.4.]
    :::

    Setting this to [`false`] will make pytest collect classes/functions from test files **only** if they are defined in that file (as opposed to imported there).

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        collect_imported_tests = false
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        collect_imported_tests = false
    :::
    :::
    :::
    :::

    Default: [`true`]

    pytest traditionally collects classes/functions in the test module namespace even if they are imported from another file.

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

    In this scenario, with the default options, pytest will collect the class [`Testament`] from [`tests/test_testament.py`] because it starts with [`Test`], even though in this case it is a production class being imported in the test module namespace.

    Set [`collected_imported_tests`] to [`false`] in the configuration file prevents that.

```
<!-- -->
```

[[consider_namespace_packages]][¶](#confval-consider_namespace_packages "Link to this definition")

:   Controls if pytest should attempt to identify [namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages) when collecting Python modules. Default is [`False`].

    Set to [`True`] if the package you are testing is part of a namespace package. Namespace packages are also supported as [[`--pyargs`]](#cmdoption-pyargs) target.

    Only [native namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages) are supported, with no plans to support [legacy namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#legacy-namespace-packages).

    ::: versionadded
    [Added in version 8.1.]
    :::

```
<!-- -->
```

[[console_output_style]][¶](#confval-console_output_style "Link to this definition")

:   Sets the console output style while running tests:

    -   [`classic`]: classic pytest output.

    -   [`progress`]: like classic pytest output, but with a progress indicator.

    -   [`progress-even-when-capture-no`]: allows the use of the progress indicator even when [`capture=no`].

    -   [`count`]: like progress, but shows progress as the number of tests completed instead of a percent.

    -   [`times`]: show tests duration.

    The default is [`progress`], but you can fallback to [`classic`] if you prefer or the new mode is causing unexpected problems:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        console_output_style = "classic"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        console_output_style = classic
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[disable_test_id_escaping_and_forfeit_all_rights_to_community_support]][¶](#confval-disable_test_id_escaping_and_forfeit_all_rights_to_community_support "Link to this definition")

:   ::: versionadded
    [Added in version 4.4.]
    :::

    pytest by default escapes any non-ascii characters used in unicode strings for the parametrization because it has several downsides. If however you would like to use unicode strings in parametrization and see them in the terminal as is (non-escaped), use this option in your configuration file:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        disable_test_id_escaping_and_forfeit_all_rights_to_community_support = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        disable_test_id_escaping_and_forfeit_all_rights_to_community_support = true
    :::
    :::
    :::
    :::

    Keep in mind however that this might cause unwanted side effects and even bugs depending on the OS used and plugins currently installed, so use it at your own risk.

    Default: [`False`].

    See [[\@pytest.mark.parametrize: parametrizing test functions]](../how-to/parametrize.html#parametrizemark).

```
<!-- -->
```

[[doctest_encoding]][¶](#confval-doctest_encoding "Link to this definition")

:   Default encoding to use to decode text files with docstrings. [[See how pytest handles doctests]](../how-to/doctest.html#doctest).

```
<!-- -->
```

[[doctest_optionflags]][¶](#confval-doctest_optionflags "Link to this definition")

:   One or more doctest flag names from the standard [`doctest`] module. [[See how pytest handles doctests]](../how-to/doctest.html#doctest).

```
<!-- -->
```

[[empty_parameter_set_mark]][¶](#confval-empty_parameter_set_mark "Link to this definition")

:   Allows to pick the action for empty parametersets in parameterization

    -   [`skip`] skips tests with an empty parameterset (default)

    -   [`xfail`] marks tests with an empty parameterset as xfail(run=False)

    -   [`fail_at_collect`] raises an exception if parametrize collects an empty parameter set

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        empty_parameter_set_mark = "xfail"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        empty_parameter_set_mark = xfail
    :::
    :::
    :::
    :::

    ::: 
    Note

    The default value of this option is planned to change to [`xfail`] in future releases as this is considered less error prone, see [#3155](https://github.com/pytest-dev/pytest/issues/3155) for more details.
    :::

```
<!-- -->
```

[[enable_assertion_pass_hook]][¶](#confval-enable_assertion_pass_hook "Link to this definition")

:   Enables the [[`pytest_assertion_pass`]](#std-hook-pytest_assertion_pass) hook. Make sure to delete any previously generated [`.pyc`] cache files.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        enable_assertion_pass_hook = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        enable_assertion_pass_hook = true
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[faulthandler_exit_on_timeout]][¶](#confval-faulthandler_exit_on_timeout "Link to this definition")

:   Exit the pytest process after the per-test timeout is reached by passing [`exit=True`] to the [[`faulthandler.dump_traceback_later()`]](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "(in Python v3.14)") function. This is particularly useful to avoid wasting CI resources for test suites that are prone to putting the main Python interpreter into a deadlock state.

    This option is set to 'false' by default.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        faulthandler_timeout = 5
        faulthandler_exit_on_timeout = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        faulthandler_timeout = 5
        faulthandler_exit_on_timeout = true
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[faulthandler_timeout]][¶](#confval-faulthandler_timeout "Link to this definition")

:   Dumps the tracebacks of all threads if a test takes longer than [`X`] seconds to run (including fixture setup and teardown). Implemented using the [[`faulthandler.dump_traceback_later()`]](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "(in Python v3.14)") function, so all caveats there apply.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        faulthandler_timeout = 5
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        faulthandler_timeout = 5
    :::
    :::
    :::
    :::

    For more information please refer to [[Fault Handler]](../how-to/failures.html#faulthandler). For more information please refer to [[Fault Handler]](../how-to/failures.html#faulthandler).

```
<!-- -->
```

[[filterwarnings]][¶](#confval-filterwarnings "Link to this definition")

:   Sets a list of filters and actions that should be taken for matched warnings. By default all warnings emitted during the test session will be displayed in a summary at the end of the test session.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        filterwarnings = ["error", "ignore::DeprecationWarning"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        filterwarnings =
            error
            ignore::DeprecationWarning
    :::
    :::
    :::
    :::

    This tells pytest to ignore deprecation warnings and turn all other warnings into errors. For more information please refer to [[How to capture warnings]](../how-to/capture-warnings.html#warnings).

```
<!-- -->
```

[[junit_duration_report]][¶](#confval-junit_duration_report "Link to this definition")

:   ::: versionadded
    [Added in version 4.1.]
    :::

    Configures how durations are recorded into the JUnit XML report:

    -   [`total`] (the default): duration times reported include setup, call, and teardown times.

    -   [`call`]: duration times reported include only call times, excluding setup and teardown.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_duration_report = "call"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_duration_report = call
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[junit_family]][¶](#confval-junit_family "Link to this definition")

:   ::: versionadded
    [Added in version 4.2.]
    :::

    ::: versionchanged
    [Changed in version 6.1: ]Default changed to [`xunit2`].
    :::

    Configures the format of the generated JUnit XML file. The possible options are:

    -   [`xunit1`] (or [`legacy`]): produces old style output, compatible with the xunit 1.0 format.

    -   [`xunit2`]: produces [xunit 2.0 style output](https://github.com/jenkinsci/xunit-plugin/blob/xunit-2.3.2/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd), which should be more compatible with latest Jenkins versions. **This is the default**.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_family = "xunit2"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_family = xunit2
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[junit_log_passing_tests]][¶](#confval-junit_log_passing_tests "Link to this definition")

:   ::: versionadded
    [Added in version 4.6.]
    :::

    If [`junit_logging`]` `[`!=`]` `[`"no"`], configures if the captured output should be written to the JUnit XML file for **passing** tests. Default is [`True`].

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_log_passing_tests = false
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_log_passing_tests = False
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[junit_logging]][¶](#confval-junit_logging "Link to this definition")

:   ::: versionadded
    [Added in version 3.5.]
    :::

    ::: versionchanged
    [Changed in version 5.4: ][`log`], [`all`], [`out-err`] options added.
    :::

    Configures if captured output should be written to the JUnit XML file. Valid values are:

    -   [`log`]: write only [`logging`] captured output.

    -   [`system-out`]: write captured [`stdout`] contents.

    -   [`system-err`]: write captured [`stderr`] contents.

    -   [`out-err`]: write both captured [`stdout`] and [`stderr`] contents.

    -   [`all`]: write captured [`logging`], [`stdout`] and [`stderr`] contents.

    -   [`no`] (the default): no captured output is written.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_logging = "system-out"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_logging = system-out
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[junit_suite_name]][¶](#confval-junit_suite_name "Link to this definition")

:   To set the name of the root test suite xml item, you can configure the [`junit_suite_name`] option in your config file:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_suite_name = "my_suite"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        junit_suite_name = my_suite
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[log_auto_indent]][¶](#confval-log_auto_indent "Link to this definition")

:   Allow selective auto-indentation of multiline log messages.

    Supports command line option [[`--log-auto-indent=[value]`]](#cmdoption-log-auto-indent) and config option [`log_auto_indent`]` `[`=`]` `[`[value]`] to set the auto-indentation behavior for all logging.

    [`[value]`] can be:

    :   -   True or "On" - Dynamically auto-indent multiline log messages

        -   False or "Off" or 0 - Do not auto-indent multiline log messages (the default behavior)

        -   \[positive integer\] - auto-indent multiline log messages by \[value\] spaces

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_auto_indent = false
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_auto_indent = false
    :::
    :::
    :::
    :::

    Supports passing kwarg [`extra=]` `[`[value]}`] to calls to [`logging.log()`] to specify auto-indentation behavior for a specific entry in the log. [`extra`] kwarg overrides the value specified on the command line or in the config.

```
<!-- -->
```

[[log_cli]][¶](#confval-log_cli "Link to this definition")

:   Enable log display during test run (also known as [["live logging"]](../how-to/logging.html#live-logs)). The default is [`False`].

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli = true
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[log_cli_date_format]][¶](#confval-log_cli_date_format "Link to this definition")

:   Sets a [[`time.strftime()`]](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.14)")-compatible string that will be used when formatting dates for live logging.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_date_format = "%Y-%m-%d %H:%M:%S"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_date_format = %Y-%m-%d %H:%M:%S
    :::
    :::
    :::
    :::

    For more information, see [[Live Logs]](../how-to/logging.html#live-logs).

```
<!-- -->
```

[[log_cli_format]][¶](#confval-log_cli_format "Link to this definition")

:   Sets a [[`logging`]](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")-compatible string used to format live logging messages.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_format = "%(asctime)s %(levelname)s %(message)s"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_format = %(asctime)s %(levelname)s %(message)s
    :::
    :::
    :::
    :::

    For more information, see [[Live Logs]](../how-to/logging.html#live-logs).

```
<!-- -->
```

[[log_cli_level]][¶](#confval-log_cli_level "Link to this definition")

:   Sets the minimum log message level that should be captured for live logging. The integer value or the names of the levels can be used.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_level = "INFO"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_cli_level = INFO
    :::
    :::
    :::
    :::

    For more information, see [[Live Logs]](../how-to/logging.html#live-logs).

```
<!-- -->
```

[[log_date_format]][¶](#confval-log_date_format "Link to this definition")

:   Sets a [[`time.strftime()`]](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.14)")-compatible string that will be used when formatting dates for logging capture.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_date_format = "%Y-%m-%d %H:%M:%S"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_date_format = %Y-%m-%d %H:%M:%S
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_file]][¶](#confval-log_file "Link to this definition")

:   Sets a file name relative to the current working directory where log messages should be written to, in addition to the other logging facilities that are active.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file = "logs/pytest-logs.txt"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file = logs/pytest-logs.txt
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_file_date_format]][¶](#confval-log_file_date_format "Link to this definition")

:   Sets a [[`time.strftime()`]](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.14)")-compatible string that will be used when formatting dates for the logging file.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_date_format = "%Y-%m-%d %H:%M:%S"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_date_format = %Y-%m-%d %H:%M:%S
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_file_format]][¶](#confval-log_file_format "Link to this definition")

:   Sets a [[`logging`]](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")-compatible string used to format logging messages redirected to the logging file.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_format = "%(asctime)s %(levelname)s %(message)s"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_format = %(asctime)s %(levelname)s %(message)s
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_file_level]][¶](#confval-log_file_level "Link to this definition")

:   Sets the minimum log message level that should be captured for the logging file. The integer value or the names of the levels can be used.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_level = "INFO"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_level = INFO
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_file_mode]][¶](#confval-log_file_mode "Link to this definition")

:   Sets the mode that the logging file is opened with. The options are [`"w"`] to recreate the file (the default) or [`"a"`] to append to the file.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_mode = "a"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_file_mode = a
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_format]][¶](#confval-log_format "Link to this definition")

:   Sets a [[`logging`]](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.14)")-compatible string used to format captured logging messages.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_format = "%(asctime)s %(levelname)s %(message)s"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_format = %(asctime)s %(levelname)s %(message)s
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[log_level]][¶](#confval-log_level "Link to this definition")

:   Sets the minimum log message level that should be captured for logging capture. The integer value or the names of the levels can be used.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_level = "INFO"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        log_level = INFO
    :::
    :::
    :::
    :::

    For more information, see [[How to manage logging]](../how-to/logging.html#logging).

```
<!-- -->
```

[[markers]][¶](#confval-markers "Link to this definition")

:   When the [[`strict_markers`]](#confval-strict_markers) configuration option is set, only known markers - defined in code by core pytest or some plugin - are allowed.

    You can list additional markers in this setting to add them to the whitelist, in which case you probably want to set [[`strict_markers`]](#confval-strict_markers) to [`true`] to avoid future regressions:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        addopts = ["--strict-markers"]
        markers = ["slow", "serial"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_markers = true
        markers =
            slow
            serial
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[minversion]][¶](#confval-minversion "Link to this definition")

:   Specifies a minimal pytest version required for running tests.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        minversion = 3.0  # will fail if we run with pytest-2.8
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        minversion = 3.0  # will fail if we run with pytest-2.8
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[norecursedirs]][¶](#confval-norecursedirs "Link to this definition")

:   Set the directory basename patterns to avoid when recursing for test discovery. The individual (fnmatch-style) patterns are applied to the basename of a directory to decide if to recurse into it. Pattern matching characters:

    ::: 
    ::: highlight
        *       matches everything
        ?       matches any single character
        [seq]   matches any character in seq
        [!seq]  matches any char not in seq
    :::
    :::

    Default patterns are [`'*.egg'`], [`'.*'`], [`'_darcs'`], [`'build'`], [`'CVS'`], [`'dist'`], [`'node_modules'`], [`'venv'`], [`''`]. Setting a [`norecursedirs`] replaces the default. Here is an example of how to avoid certain directories:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        norecursedirs = [".svn", "_build", "tmp*"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        norecursedirs = .svn _build tmp*
    :::
    :::
    :::
    :::

    This would tell [`pytest`] to not look into typical subversion or sphinx-build directories or into any [`tmp`] prefixed directory.

    Additionally, [`pytest`] will attempt to intelligently identify and ignore a virtualenv. Any directory deemed to be the root of a virtual environment will not be considered during test collection unless [[`--collect-in-virtualenv`]](#cmdoption-collect-in-virtualenv) is given. Note also that [`norecursedirs`] takes precedence over [`--collect-in-virtualenv`]; e.g. if you intend to run tests in a virtualenv with a base directory that matches [`'.*'`] you *must* override [`norecursedirs`] in addition to using the [`--collect-in-virtualenv`] flag.

```
<!-- -->
```

[[python_classes]][¶](#confval-python_classes "Link to this definition")

:   One or more name prefixes or glob-style patterns determining which classes are considered for test collection. Search for multiple glob patterns by adding a space between patterns. By default, pytest will consider any class prefixed with [`Test`] as a test collection. Here is an example of how to collect tests from classes that end in [`Suite`]:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_classes = ["*Suite"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_classes = *Suite
    :::
    :::
    :::
    :::

    Note that [`unittest.TestCase`] derived classes are always collected regardless of this option, as [`unittest`]'s own collection framework is used to collect those tests.

```
<!-- -->
```

[[python_files]][¶](#confval-python_files "Link to this definition")

:   One or more Glob-style file patterns determining which python files are considered as test modules. Search for multiple glob patterns by adding a space between patterns:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_files = ["test_*.py", "check_*.py", "example_*.py"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_files = test_*.py check_*.py example_*.py
    :::
    :::

    Or one per line:

    ::: 
    ::: highlight
        [pytest]
        python_files =
            test_*.py
            check_*.py
            example_*.py
    :::
    :::
    :::
    :::

    By default, files matching [`test_*.py`] and [`*_test.py`] will be considered test modules.

```
<!-- -->
```

[[python_functions]][¶](#confval-python_functions "Link to this definition")

:   One or more name prefixes or glob-patterns determining which test functions and methods are considered tests. Search for multiple glob patterns by adding a space between patterns. By default, pytest will consider any function prefixed with [`test`] as a test. Here is an example of how to collect test functions and methods that end in [`_test`]:

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_functions = ["*_test"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        python_functions = *_test
    :::
    :::
    :::
    :::

    Note that this has no effect on methods that live on a [`unittest.TestCase`] derived class, as [`unittest`]'s own collection framework is used to collect those tests.

    See [[Changing naming conventions]](../example/pythoncollection.html#change-naming-conventions) for more detailed examples.

```
<!-- -->
```

[[pythonpath]][¶](#confval-pythonpath "Link to this definition")

:   Sets list of directories that should be added to the python search path. Directories will be added to the head of [[`sys.path`]](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.14)"). Similar to the [][[`PYTHONPATH`]](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH "(in Python v3.14)") environment variable, the directories will be included in where Python will look for imported modules. Paths are relative to the [[rootdir]](customize.html#rootdir) directory. Directories remain in path for the duration of the test session.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        pythonpath = ["src1", "src2"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        pythonpath = src1 src2
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[required_plugins]][¶](#confval-required_plugins "Link to this definition")

:   A space separated list of plugins that must be present for pytest to run. Plugins can be listed with or without version specifiers directly following their name. Whitespace between different version specifiers is not allowed. If any one of the plugins is not found, emit an error.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        required_plugins = ["pytest-django>=3.0.0,<4.0.0", "pytest-html", "pytest-xdist>=1.0.0"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        required_plugins = pytest-django>=3.0.0,<4.0.0 pytest-html pytest-xdist>=1.0.0
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[strict]][¶](#confval-strict "Link to this definition")

:   If set to [`true`], enable "strict mode", which enables the following options:

    -   [[`strict_config`]](#confval-strict_config)

    -   [[`strict_markers`]](#confval-strict_markers)

    -   [[`strict_parametrization_ids`]](#confval-strict_parametrization_ids)

    -   [[`strict_xfail`]](#confval-strict_xfail)

    Plugins may also enable their own strictness options.

    If you explicitly set an individual strictness option, it takes precedence over [`strict`].

    ::: 
    Note

    If pytest adds new strictness options in the future, they will also be enabled in strict mode. Therefore, you should only enable strict mode if you use a pinned/locked version of pytest, or if you want to proactively adopt new strictness options as they are added.
    :::

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict = true
    :::
    :::
    :::
    :::

    ::: versionadded
    [Added in version 9.0.]
    :::

```
<!-- -->
```

[[strict_config]][¶](#confval-strict_config "Link to this definition")

:   If set to [`true`], any warnings encountered while parsing the [`pytest`] section of the configuration file will raise errors.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_config = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_config = true
    :::
    :::
    :::
    :::

    You can also enable this option via the [[`strict`]](#confval-strict) option.

```
<!-- -->
```

[[strict_markers]][¶](#confval-strict_markers "Link to this definition")

:   If set to [`true`], markers not registered in the [`markers`] section of the configuration file will raise errors.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_markers = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_markers = true
    :::
    :::
    :::
    :::

    You can also enable this option via the [[`strict`]](#confval-strict) option.

```
<!-- -->
```

[[strict_parametrization_ids]][¶](#confval-strict_parametrization_ids "Link to this definition")

:   If set to [`true`], pytest emits an error if it detects non-unique parameter set IDs.

    If not set (the default), pytest automatically handles this by adding [`0`], [`1`], ... to duplicate IDs, making them unique.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_parametrization_ids = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_parametrization_ids = true
    :::
    :::
    :::
    :::

    You can also enable this option via the [[`strict`]](#confval-strict) option.

    For example,

    ::: 
    ::: highlight
        import pytest

        @pytest.mark.parametrize("letter", ["a", "a"])
        def test_letter_is_ascii(letter):
            assert letter.isascii()
    :::
    :::

    will emit an error because both cases (parameter sets) have the same auto-generated ID "a".

    To fix the error, if you decide to keep the duplicates, explicitly assign unique IDs:

    ::: 
    ::: highlight
        import pytest

        @pytest.mark.parametrize("letter", ["a", "a"], ids=["a0", "a1"])
        def test_letter_is_ascii(letter):
            assert letter.isascii()
    :::
    :::

    See [[`parametrize`]](#pytest.Metafunc.parametrize "pytest.Metafunc.parametrize") and [[`pytest.param()`]](#pytest.param "pytest.param") for other ways to set IDs.

```
<!-- -->
```

[[strict_xfail]][¶](#confval-strict_xfail "Link to this definition")

:   If set to [`true`], tests marked with [`@pytest.mark.xfail`] that actually succeed will by default fail the test suite. For more information, see [[strict parameter]](../how-to/skipping.html#xfail-strict-tutorial).

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_xfail = true
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        strict_xfail = true
    :::
    :::
    :::
    :::

    You can also enable this option via the [[`strict`]](#confval-strict) option.

    ::: versionchanged
    [Changed in version 9.0: ]Renamed from [`xfail_strict`] to [`strict_xfail`]. [`xfail_strict`] is accepted as an alias for [`strict_xfail`].
    :::

```
<!-- -->
```

[[testpaths]][¶](#confval-testpaths "Link to this definition")

:   Sets list of directories that should be searched for tests when no specific directories, files or test ids are given in the command line when executing pytest from the [[rootdir]](customize.html#rootdir) directory. File system paths may use shell-style wildcards, including the recursive [`**`] pattern.

    Useful when all project tests are in a known location to speed up test collection and to avoid picking up undesired tests by accident.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        testpaths = ["testing", "doc"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        testpaths = testing doc
    :::
    :::
    :::
    :::

    This configuration means that executing:

    ::: 
    ::: highlight
        pytest
    :::
    :::

    has the same practical effects as executing:

    ::: 
    ::: highlight
        pytest testing doc
    :::
    :::

```
<!-- -->
```

[[tmp_path_retention_count]][¶](#confval-tmp_path_retention_count "Link to this definition")

:   How many sessions should we keep the [`tmp_path`] directories, according to [[`tmp_path_retention_policy`]](#confval-tmp_path_retention_policy).

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        tmp_path_retention_count = "3"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        tmp_path_retention_count = 3
    :::
    :::
    :::
    :::

    Default: [`3`]

```
<!-- -->
```

[[tmp_path_retention_policy]][¶](#confval-tmp_path_retention_policy "Link to this definition")

:   Controls which directories created by the [`tmp_path`] fixture are kept around, based on test outcome.

    > <div>
    >
    > -   [`all`]: retains directories for all tests, regardless of the outcome.
    >
    > -   [`failed`]: retains directories only for tests with outcome [`error`] or [`failed`].
    >
    > -   [`none`]: directories are always removed after each test ends, regardless of the outcome.
    >
    > </div>

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        tmp_path_retention_policy = "all"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        tmp_path_retention_policy = all
    :::
    :::
    :::
    :::

    Default: [`all`]

```
<!-- -->
```

[[truncation_limit_chars]][¶](#confval-truncation_limit_chars "Link to this definition")

:   Controls maximum number of characters to truncate assertion message contents.

    Setting value to [`0`] disables the character limit for truncation.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        truncation_limit_chars = 640
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        truncation_limit_chars = 640
    :::
    :::
    :::
    :::

    pytest truncates the assert messages to a certain limit by default to prevent comparison with large data to overload the console output.

    Default: [`640`]

    ::: 
    Note

    If pytest detects it is [[running on CI]](../explanation/ci.html#ci-pipelines), truncation is disabled automatically.
    :::

```
<!-- -->
```

[[truncation_limit_lines]][¶](#confval-truncation_limit_lines "Link to this definition")

:   Controls maximum number of linesto truncate assertion message contents.

    Setting value to [`0`] disables the lines limit for truncation.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        truncation_limit_lines = 8
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        truncation_limit_lines = 8
    :::
    :::
    :::
    :::

    pytest truncates the assert messages to a certain limit by default to prevent comparison with large data to overload the console output.

    Default: [`8`]

    ::: 
    Note

    If pytest detects it is [[running on CI]](../explanation/ci.html#ci-pipelines), truncation is disabled automatically.
    :::

```
<!-- -->
```

[[usefixtures]][¶](#confval-usefixtures "Link to this definition")

:   List of fixtures that will be applied to all test functions; this is semantically the same to apply the [`@pytest.mark.usefixtures`] marker to all test functions.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        usefixtures = ["clean_db"]
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        usefixtures =
            clean_db
    :::
    :::
    :::
    :::

```
<!-- -->
```

[[verbosity_assertions]][¶](#confval-verbosity_assertions "Link to this definition")

:   Set a verbosity level specifically for assertion related output, overriding the application wide level.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_assertions = "2"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_assertions = 2
    :::
    :::
    :::
    :::

    If not set, defaults to application wide verbosity level (via the [[`-v`]](#cmdoption-v) command-line option). A special value of [`"auto"`] can be used to explicitly use the global verbosity level.

```
<!-- -->
```

[[verbosity_subtests]][¶](#confval-verbosity_subtests "Link to this definition")

:   Set the verbosity level specifically for **passed** subtests.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_subtests = "1"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_subtests = 1
    :::
    :::
    :::
    :::

    A value of [`1`] or higher will show output for **passed** subtests (**failed** subtests are always reported). Passed subtests output can be suppressed with the value [`0`], which overwrites the [[`-v`]](#cmdoption-v) command-line option.

    If not set, defaults to application wide verbosity level (via the [[`-v`]](#cmdoption-v) command-line option). A special value of [`"auto"`] can be used to explicitly use the global verbosity level.

    See also: [[How to use subtests]](../how-to/subtests.html#subtests).

```
<!-- -->
```

[[verbosity_test_cases]][¶](#confval-verbosity_test_cases "Link to this definition")

:   Set a verbosity level specifically for test case execution related output, overriding the application wide level.

    ::: 
    toml

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_test_cases = "2"
    :::
    :::
    :::

    ini

    ::: 
    ::: 
    ::: highlight
        [pytest]
        verbosity_test_cases = 2
    :::
    :::
    :::
    :::

    If not set, defaults to application wide verbosity level (via the [[`-v`]](#cmdoption-v) command-line option). A special value of [`"auto"`] can be used to explicitly use the global verbosity level.

[]

## Command-line Flags[¶](#command-line-flags "Link to this heading")

This section documents all command-line options provided by pytest's core plugins.

Note

External plugins can add their own command-line options. This reference documents only the options from pytest's core plugins. To see all available options including those from installed plugins, run [`pytest`]` `[`--help`].

### Test Selection[¶](#test-selection "Link to this heading")

[[-k]][ [EXPRESSION]][¶](#cmdoption-k "Link to this definition")

:   Only run tests which match the given substring expression. An expression is a Python evaluable expression where all names are substring-matched against test names and their parent classes.

    Examples:

    ::: 
    ::: highlight
        pytest -k "test_method or test_other"  # matches names containing 'test_method' OR 'test_other'
        pytest -k "not test_method"            # matches names NOT containing 'test_method'
        pytest -k "not test_method and not test_other"  # excludes both
    :::
    :::

    The matching is case-insensitive. Keywords are also matched to classes and functions containing extra names in their [`extra_keyword_matches`] set.

    See [[Specifying which tests to run]](../how-to/usage.html#select-tests) for more information and examples.

```
<!-- -->
```

[[-m]][ [MARKEXPR]][¶](#cmdoption-m "Link to this definition")

:   Only run tests matching given mark expression. Supports [`and`], [`or`], and [`not`] operators.

    Examples:

    ::: 
    ::: highlight
        pytest -m slow                  # run tests marked with @pytest.mark.slow
        pytest -m "not slow"            # run tests NOT marked slow
        pytest -m "mark1 and not mark2" # run tests marked mark1 but not mark2
    :::
    :::

    See [[How to mark test functions with attributes]](../how-to/mark.html#mark) for more information on markers.

```
<!-- -->
```

[[\--markers]][][¶](#cmdoption-markers "Link to this definition")

:   Show all available markers (builtin, plugin, and per-project markers defined in configuration).

### Test Execution Control[¶](#test-execution-control "Link to this heading")

[][[-x]][][[,] ][[\--exitfirst]][][¶](#cmdoption-x "Link to this definition")

:   Exit instantly on first error or failed test.

```
<!-- -->
```

[[\--maxfail]][[=NUM]][¶](#cmdoption-maxfail "Link to this definition")

:   Exit after first [`num`] failures or errors. Useful for CI environments where you want to fail fast but see a few failures.

```
<!-- -->
```

[][[\--last-failed]][][[,] ][[\--lf]][][¶](#cmdoption-last-failed "Link to this definition")

:   Rerun only the tests that failed at the last run. If no tests failed (or no cached data exists), all tests are run. See also [[`cache_dir`]](#confval-cache_dir) and [[How to re-run failed tests and maintain state between test runs]](../how-to/cache.html#cache).

```
<!-- -->
```

[][[\--failed-first]][][[,] ][[\--ff]][][¶](#cmdoption-failed-first "Link to this definition")

:   Run all tests, but run the last failures first. This may re-order tests and thus lead to repeated fixture setup/teardown.

```
<!-- -->
```

[][[\--new-first]][][[,] ][[\--nf]][][¶](#cmdoption-new-first "Link to this definition")

:   Run tests from new files first, then the rest of the tests sorted by file modification time.

```
<!-- -->
```

[][[\--stepwise]][][[,] ][[\--sw]][][¶](#cmdoption-stepwise "Link to this definition")

:   Exit on test failure and continue from last failing test next time. Useful for fixing multiple test failures one at a time.

    See [[Stepwise]](../how-to/cache.html#cache-stepwise) for more information.

```
<!-- -->
```

[][[\--stepwise-skip]][][[,] ][[\--sw-skip]][][¶](#cmdoption-stepwise-skip "Link to this definition")

:   Ignore the first failing test but stop on the next failing test. Implicitly enables [[`--stepwise`]](#cmdoption-stepwise).

```
<!-- -->
```

[][[\--stepwise-reset]][][[,] ][[\--sw-reset]][][¶](#cmdoption-stepwise-reset "Link to this definition")

:   Resets stepwise state, restarting the stepwise workflow. Implicitly enables [[`--stepwise`]](#cmdoption-stepwise).

```
<!-- -->
```

[][[\--last-failed-no-failures]][][[,] ][[\--lfnf]][][¶](#cmdoption-last-failed-no-failures "Link to this definition")

:   With [[`--last-failed`]](#cmdoption-last-failed), determines whether to execute tests when there are no previously known failures or when no cached [`lastfailed`] data was found.

    -   [`all`] (default): runs the full test suite again

    -   [`none`]: just emits a message about no known failures and exits successfully

```
<!-- -->
```

[[\--runxfail]][][¶](#cmdoption-runxfail "Link to this definition")

:   Report the results of xfail tests as if they were not marked. Useful for debugging xfailed tests. See [[XFail: mark test functions as expected to fail]](../how-to/skipping.html#xfail).

### Collection[¶](#collection "Link to this heading")

[][[\--collect-only]][][[,] ][[\--co]][][¶](#cmdoption-collect-only "Link to this definition")

:   Only collect tests, don't execute them. Shows which tests would be collected and run.

```
<!-- -->
```

[[\--pyargs]][][¶](#cmdoption-pyargs "Link to this definition")

:   Try to interpret all arguments as Python packages. Useful for running tests of installed packages:

    ::: 
    ::: highlight
        pytest --pyargs pkg.testing
    :::
    :::

```
<!-- -->
```

[[\--ignore]][[=PATH]][¶](#cmdoption-ignore "Link to this definition")

:   Ignore path during collection (multi-allowed). Can be specified multiple times.

```
<!-- -->
```

[[\--ignore-glob]][[=PATTERN]][¶](#cmdoption-ignore-glob "Link to this definition")

:   Ignore path pattern during collection (multi-allowed). Supports glob patterns.

```
<!-- -->
```

[[\--deselect]][[=NODEID_PREFIX]][¶](#cmdoption-deselect "Link to this definition")

:   Deselect item (via node id prefix) during collection (multi-allowed).

```
<!-- -->
```

[[\--confcutdir]][[=DIR]][¶](#cmdoption-confcutdir "Link to this definition")

:   Only load [`conftest.py`] files relative to specified directory.

```
<!-- -->
```

[[\--noconftest]][][¶](#cmdoption-noconftest "Link to this definition")

:   Don't load any [`conftest.py`] files.

```
<!-- -->
```

[[\--keep-duplicates]][][¶](#cmdoption-keep-duplicates "Link to this definition")

:   Keep duplicate tests. By default, pytest removes duplicate test items.

```
<!-- -->
```

[[\--collect-in-virtualenv]][][¶](#cmdoption-collect-in-virtualenv "Link to this definition")

:   Don't ignore tests in a local virtualenv directory. By default, pytest skips tests in virtualenv directories.

```
<!-- -->
```

[[\--continue-on-collection-errors]][][¶](#cmdoption-continue-on-collection-errors "Link to this definition")

:   Force test execution even if collection errors occur.

```
<!-- -->
```

[[\--import-mode]][][¶](#cmdoption-import-mode "Link to this definition")

:   Prepend/append to sys.path when importing test modules and conftest files.

    -   [`prepend`] (default): prepend to sys.path

    -   [`append`]: append to sys.path

    -   [`importlib`]: use importlib to import test modules

    See [[pytest import mechanisms and sys.path/PYTHONPATH]](../explanation/pythonpath.html#pythonpath) for more information.

### Fixtures[¶](#id55 "Link to this heading")

[][[\--fixtures]][][[,] ][[\--funcargs]][][¶](#cmdoption-fixtures "Link to this definition")

:   Show available fixtures, sorted by plugin appearance. Fixtures with leading [`_`] are only shown with [[`--verbose`]](#cmdoption-v).

```
<!-- -->
```

[[\--fixtures-per-test]][][¶](#cmdoption-fixtures-per-test "Link to this definition")

:   Show fixtures per test.

```
<!-- -->
```

[[\--setup-only]][][¶](#cmdoption-setup-only "Link to this definition")

:   Only setup fixtures, do not execute tests. See [[How to use fixtures]](../how-to/fixtures.html#how-to-fixtures).

```
<!-- -->
```

[[\--setup-show]][][¶](#cmdoption-setup-show "Link to this definition")

:   Show setup of fixtures while executing tests.

```
<!-- -->
```

[[\--setup-plan]][][¶](#cmdoption-setup-plan "Link to this definition")

:   Show what fixtures and tests would be executed but don't execute anything.

### Debugging[¶](#debugging "Link to this heading")

[[\--pdb]][][¶](#cmdoption-pdb "Link to this definition")

:   Start the interactive Python debugger on errors or KeyboardInterrupt. See [[Using python:library/pdb with pytest]](../how-to/failures.html#pdb-option).

```
<!-- -->
```

[[\--pdbcls]][[=MODULENAME:CLASSNAME]][¶](#cmdoption-pdbcls "Link to this definition")

:   Specify a custom interactive Python debugger for use with [[`--pdb`]](#cmdoption-pdb).

    Example:

    ::: 
    ::: highlight
        pytest --pdbcls=IPython.terminal.debugger:TerminalPdb
    :::
    :::

```
<!-- -->
```

[[\--trace]][][¶](#cmdoption-trace "Link to this definition")

:   Immediately break when running each test.

    See [[Dropping to pdb at the start of a test]](../how-to/failures.html#trace-option) for more information.

```
<!-- -->
```

[[\--full-trace]][][¶](#cmdoption-full-trace "Link to this definition")

:   Don't cut any tracebacks (default is to cut).

    See [[Modifying Python traceback printing]](../how-to/output.html#how-to-modifying-python-tb-printing) for more information.

```
<!-- -->
```

[][[\--debug]][][[,] ][[\--debug]][[=DEBUG_FILE_NAME]][¶](#cmdoption-debug "Link to this definition")

:   Store internal tracing debug information in this log file. This file is opened with [`'w'`] and truncated as a result, care advised. Default file name if not specified: [`pytestdebug.log`].

```
<!-- -->
```

[[\--trace-config]][][¶](#cmdoption-trace-config "Link to this definition")

:   Trace considerations of conftest.py files.

### Output and Reporting[¶](#output-and-reporting "Link to this heading")

[][[-v]][][[,] ][[\--verbose]][][¶](#cmdoption-v "Link to this definition")

:   Increase verbosity. Can be specified multiple times (e.g., [`-vv`]) for even more verbose output.

    See [[Fine-grained verbosity]](../how-to/output.html#pytest-fine-grained-verbosity) for fine-grained control over verbosity.

```
<!-- -->
```

[][[-q]][][[,] ][[\--quiet]][][¶](#cmdoption-q "Link to this definition")

:   Decrease verbosity.

```
<!-- -->
```

[[\--verbosity]][[=NUM]][¶](#cmdoption-verbosity "Link to this definition")

:   Set verbosity level explicitly. Default: 0.

```
<!-- -->
```

[[-r]][ [CHARS]][¶](#cmdoption-r "Link to this definition")

:   Show extra test summary info as specified by chars:

    -   [`f`]: failed

    -   [`E`]: error

    -   [`s`]: skipped

    -   [`x`]: xfailed

    -   [`X`]: xpassed

    -   [`p`]: passed

    -   [`P`]: passed with output

    -   [`a`]: all except passed (p/P)

    -   [`A`]: all

    -   [`w`]: warnings (enabled by default)

    -   [`N`]: resets the list

    Default: [`'fE'`]

    Examples:

    ::: 
    ::: highlight
        pytest -rA           # show all outcomes
        pytest -rfE          # show only failed and errors (default)
        pytest -rfs          # show failed and skipped
    :::
    :::

    See [[Producing a detailed summary report]](../how-to/output.html#pytest-detailed-failed-tests-usage) for more information.

```
<!-- -->
```

[[\--no-header]][][¶](#cmdoption-no-header "Link to this definition")

:   Disable header.

```
<!-- -->
```

[[\--no-summary]][][¶](#cmdoption-no-summary "Link to this definition")

:   Disable summary.

```
<!-- -->
```

[[\--no-fold-skipped]][][¶](#cmdoption-no-fold-skipped "Link to this definition")

:   Do not fold skipped tests in short summary.

```
<!-- -->
```

[[\--force-short-summary]][][¶](#cmdoption-force-short-summary "Link to this definition")

:   Force condensed summary output regardless of verbosity level.

```
<!-- -->
```

[][[-l]][][[,] ][[\--showlocals]][][¶](#cmdoption-l "Link to this definition")

:   Show locals in tracebacks (disabled by default).

```
<!-- -->
```

[[\--no-showlocals]][][¶](#cmdoption-no-showlocals "Link to this definition")

:   Hide locals in tracebacks (negate [[`--showlocals`]](#cmdoption-l) passed through addopts).

```
<!-- -->
```

[[\--tb]][[=STYLE]][¶](#cmdoption-tb "Link to this definition")

:   Traceback print mode:

    -   [`auto`]: intelligent traceback formatting (default)

    -   [`long`]: exhaustive, informative traceback formatting

    -   [`short`]: shorter traceback format

    -   [`line`]: only the failing line

    -   [`native`]: Python's standard traceback

    -   [`no`]: no traceback

    See [[Modifying Python traceback printing]](../how-to/output.html#how-to-modifying-python-tb-printing) for examples.

```
<!-- -->
```

[[\--xfail-tb]][][¶](#cmdoption-xfail-tb "Link to this definition")

:   Show tracebacks for xfail (as long as [[`--tb`]](#cmdoption-tb) != [`no`]).

```
<!-- -->
```

[[\--show-capture]][][¶](#cmdoption-show-capture "Link to this definition")

:   Controls how captured stdout/stderr/log is shown on failed tests.

    -   [`no`]: don't show captured output

    -   [`stdout`]: show captured stdout

    -   [`stderr`]: show captured stderr

    -   [`log`]: show captured logging

    -   [`all`] (default): show all captured output

```
<!-- -->
```

[[\--color]][[=WHEN]][¶](#cmdoption-color "Link to this definition")

:   Color terminal output:

    -   [`yes`]: always use color

    -   [`no`]: never use color

    -   [`auto`] (default): use color if terminal supports it

```
<!-- -->
```

[[\--code-highlight]][[=]][¶](#cmdoption-code-highlight "Link to this definition")

:   Whether code should be highlighted (only if [[`--color`]](#cmdoption-color) is also enabled). Default: [`yes`].

```
<!-- -->
```

[[\--pastebin]][[=MODE]][¶](#cmdoption-pastebin "Link to this definition")

:   Send failed\|all info to bpaste.net pastebin service.

```
<!-- -->
```

[[\--durations]][[=NUM]][¶](#cmdoption-durations "Link to this definition")

:   Show N slowest setup/test durations (N=0 for all). See [[Profiling test execution duration]](../how-to/usage.html#durations).

```
<!-- -->
```

[[\--durations-min]][[=NUM]][¶](#cmdoption-durations-min "Link to this definition")

:   Minimal duration in seconds for inclusion in slowest list. Default: 0.005 (or 0.0 if [`-vv`] is given).

### Output Capture[¶](#output-capture "Link to this heading")

[[\--capture]][[=METHOD]][¶](#cmdoption-capture "Link to this definition")

:   Per-test capturing method:

    -   [`fd`]: capture at file descriptor level (default)

    -   [`sys`]: capture at sys level

    -   [`no`]: don't capture output

    -   [`tee-sys`]: capture but also show output on terminal

    See [[How to capture stdout/stderr output]](../how-to/capture-stdout-stderr.html#captures).

```
<!-- -->
```

[[-s]][][¶](#cmdoption-s "Link to this definition")

:   Shortcut for [[`--capture=no`]](#cmdoption-capture).

### JUnit XML[¶](#junit-xml "Link to this heading")

[][[\--junit-xml]][[=PATH]][[,] ][[\--junitxml]][[=PATH]][¶](#cmdoption-junit-xml "Link to this definition")

:   Create junit-xml style report file at given path.

```
<!-- -->
```

[][[\--junit-prefix]][[=STR]][[,] ][[\--junitprefix]][[=STR]][¶](#cmdoption-junit-prefix "Link to this definition")

:   Prepend prefix to classnames in junit-xml output.

### Cache[¶](#cache "Link to this heading")

[[\--cache-show]][[\[=PATTERN\]]][¶](#cmdoption-cache-show "Link to this definition")

:   Show cache contents, don't perform collection or tests. Default glob pattern: [`'*'`].

```
<!-- -->
```

[[\--cache-clear]][][¶](#cmdoption-cache-clear "Link to this definition")

:   Remove all cache contents at start of test run. See [[How to re-run failed tests and maintain state between test runs]](../how-to/cache.html#cache).

### Warnings[¶](#id56 "Link to this heading")

[][[\--disable-pytest-warnings]][][[,] ][[\--disable-warnings]][][¶](#cmdoption-disable-pytest-warnings "Link to this definition")

:   Disable warnings summary.

```
<!-- -->
```

[][[-W]][ [WARNING]][[,] ][[\--pythonwarnings]][[=WARNING]][¶](#cmdoption-W "Link to this definition")

:   Set which warnings to report, see [`-W`] option of Python itself. Can be specified multiple times.

### Doctest[¶](#doctest "Link to this heading")

[[\--doctest-modules]][][¶](#cmdoption-doctest-modules "Link to this definition")

:   Run doctests in all .py modules.

    See [[How to run doctests]](../how-to/doctest.html#doctest) for more information on using doctests with pytest.

```
<!-- -->
```

[[\--doctest-report]][][¶](#cmdoption-doctest-report "Link to this definition")

:   Choose another output format for diffs on doctest failure:

    -   [`none`]

    -   [`cdiff`]

    -   [`ndiff`]

    -   [`udiff`]

    -   [`only_first_failure`]

```
<!-- -->
```

[[\--doctest-glob]][[=PATTERN]][¶](#cmdoption-doctest-glob "Link to this definition")

:   Doctests file matching pattern. Default: [`test*.txt`].

```
<!-- -->
```

[[\--doctest-ignore-import-errors]][][¶](#cmdoption-doctest-ignore-import-errors "Link to this definition")

:   Ignore doctest collection errors.

```
<!-- -->
```

[[\--doctest-continue-on-failure]][][¶](#cmdoption-doctest-continue-on-failure "Link to this definition")

:   For a given doctest, continue to run after the first failure.

### Configuration[¶](#configuration "Link to this heading")

[][[-c]][ [FILE]][[,] ][[\--config-file]][[=FILE]][¶](#cmdoption-c "Link to this definition")

:   Load configuration from [`FILE`] instead of trying to locate one of the implicit configuration files.

```
<!-- -->
```

[[\--rootdir]][[=ROOTDIR]][¶](#cmdoption-rootdir "Link to this definition")

:   Define root directory for tests. Can be relative path: [`'root_dir'`], [`'./root_dir'`], [`'root_dir/another_dir/'`]; absolute path: [`'/home/user/root_dir'`]; path with variables: [`'$HOME/root_dir'`].

```
<!-- -->
```

[[\--basetemp]][[=DIR]][¶](#cmdoption-basetemp "Link to this definition")

:   Base temporary directory for this test run. Warning: this directory is removed if it exists.

    See [[Temporary directory location and retention]](../how-to/tmp_path.html#temporary-directory-location-and-retention) for more information.

```
<!-- -->
```

[][[-o]][ [OPTION=VALUE]][[,] ][[\--override-ini]][[=OPTION=VALUE]][¶](#cmdoption-o "Link to this definition")

:   Override configuration option with [`option=value`] style. Can be specified multiple times.

    Example:

    ::: 
    ::: highlight
        pytest -o strict_xfail=true -o cache_dir=cache
    :::
    :::

```
<!-- -->
```

[[\--strict-config]][][¶](#cmdoption-strict-config "Link to this definition")

:   Enables the [[`strict_config`]](#confval-strict_config) option.

```
<!-- -->
```

[[\--strict-markers]][][¶](#cmdoption-strict-markers "Link to this definition")

:   Enables the [[`strict_markers`]](#confval-strict_markers) option.

```
<!-- -->
```

[[\--strict]][][¶](#cmdoption-strict "Link to this definition")

:   Enables the [[`strict`]](#confval-strict) option (which enables all strictness options).

```
<!-- -->
```

[[\--assert]][[=MODE]][¶](#cmdoption-assert "Link to this definition")

:   Control assertion debugging tools:

    -   [`plain`]: performs no assertion debugging

    -   [`rewrite`] (default): rewrites assert statements in test modules on import to provide assert expression information

### Logging[¶](#logging "Link to this heading")

See [[How to manage logging]](../how-to/logging.html#logging) for a guide on using these flags.

[[\--log-level]][[=LEVEL]][¶](#cmdoption-log-level "Link to this definition")

:   Level of messages to catch/display. Not set by default, so it depends on the root/parent log handler's effective level, where it is [`WARNING`] by default.

```
<!-- -->
```

[[\--log-format]][[=FORMAT]][¶](#cmdoption-log-format "Link to this definition")

:   Log format used by the logging module.

```
<!-- -->
```

[[\--log-date-format]][[=FORMAT]][¶](#cmdoption-log-date-format "Link to this definition")

:   Log date format used by the logging module.

```
<!-- -->
```

[[\--log-cli-level]][[=LEVEL]][¶](#cmdoption-log-cli-level "Link to this definition")

:   CLI logging level. See [[Live Logs]](../how-to/logging.html#live-logs).

```
<!-- -->
```

[[\--log-cli-format]][[=FORMAT]][¶](#cmdoption-log-cli-format "Link to this definition")

:   Log format used by the logging module for CLI output.

```
<!-- -->
```

[[\--log-cli-date-format]][[=FORMAT]][¶](#cmdoption-log-cli-date-format "Link to this definition")

:   Log date format used by the logging module for CLI output.

```
<!-- -->
```

[[\--log-file]][[=PATH]][¶](#cmdoption-log-file "Link to this definition")

:   Path to a file when logging will be written to.

```
<!-- -->
```

[[\--log-file-mode]][][¶](#cmdoption-log-file-mode "Link to this definition")

:   Log file open mode:

    -   [`w`] (default): recreate the file

    -   [`a`]: append to the file

```
<!-- -->
```

[[\--log-file-level]][[=LEVEL]][¶](#cmdoption-log-file-level "Link to this definition")

:   Log file logging level.

```
<!-- -->
```

[[\--log-file-format]][[=FORMAT]][¶](#cmdoption-log-file-format "Link to this definition")

:   Log format used by the logging module for the log file.

```
<!-- -->
```

[[\--log-file-date-format]][[=FORMAT]][¶](#cmdoption-log-file-date-format "Link to this definition")

:   Log date format used by the logging module for the log file.

```
<!-- -->
```

[[\--log-auto-indent]][[=VALUE]][¶](#cmdoption-log-auto-indent "Link to this definition")

:   Auto-indent multiline messages passed to the logging module. Accepts [`true|on`], [`false|off`] or an integer.

```
<!-- -->
```

[[\--log-disable]][[=LOGGER]][¶](#cmdoption-log-disable "Link to this definition")

:   Disable a logger by name. Can be passed multiple times.

### Plugin and Extension Management[¶](#plugin-and-extension-management "Link to this heading")

[[-p]][ [NAME]][¶](#cmdoption-p "Link to this definition")

:   Early-load given plugin module name or entry point (multi-allowed). To avoid loading of plugins, use the [`no:`] prefix, e.g. [`no:doctest`]. See also [[`--disable-plugin-autoload`]](#cmdoption-disable-plugin-autoload).

```
<!-- -->
```

[[\--disable-plugin-autoload]][][¶](#cmdoption-disable-plugin-autoload "Link to this definition")

:   Disable plugin auto-loading through entry point packaging metadata. Only plugins explicitly specified in [[`-p`]](#cmdoption-p) or env var [][[`PYTEST_PLUGINS`]](#envvar-PYTEST_PLUGINS) will be loaded.

### Version and Help[¶](#version-and-help "Link to this heading")

[][[-V]][][[,] ][[\--version]][][¶](#cmdoption-V "Link to this definition")

:   Display pytest version and information about plugins. When given twice, also display information about plugins.

```
<!-- -->
```

[][[-h]][][[,] ][[\--help]][][¶](#cmdoption-h "Link to this definition")

:   Show help message and configuration info.

### Complete Help Output[¶](#complete-help-output "Link to this heading")

All the command-line flags can also be obtained by running [`pytest`]` `[`--help`]:

    $ pytest --help
    usage: pytest [options] [file_or_dir] [file_or_dir] [...]

    positional arguments:
      file_or_dir

    general:
      -k EXPRESSION         Only run tests which match the given substring
                            expression. An expression is a Python evaluable
                            expression where all names are substring-matched
                            against test names and their parent classes.
                            Example: -k 'test_method or test_other' matches all
                            test functions and classes whose name contains
                            'test_method' or 'test_other', while -k 'not
                            test_method' matches those that don't contain
                            'test_method' in their names. -k 'not test_method
                            and not test_other' will eliminate the matches.
                            Additionally keywords are matched to classes and
                            functions containing extra names in their
                            'extra_keyword_matches' set, as well as functions
                            which have names assigned directly to them. The
                            matching is case-insensitive.
      -m MARKEXPR           Only run tests matching given mark expression. For
                            example: -m 'mark1 and not mark2'.
      --markers             show markers (builtin, plugin and per-project ones).
      -x, --exitfirst       Exit instantly on first error or failed test
      --maxfail=num         Exit after first num failures or errors
      --strict-config       Enables the strict_config option
      --strict-markers      Enables the strict_markers option
      --strict              Enables the strict option
      --fixtures, --funcargs
                            Show available fixtures, sorted by plugin appearance
                            (fixtures with leading '_' are only shown with '-v')
      --fixtures-per-test   Show fixtures per test
      --pdb                 Start the interactive Python debugger on errors or
                            KeyboardInterrupt
      --pdbcls=modulename:classname
                            Specify a custom interactive Python debugger for use
                            with --pdb.For example:
                            --pdbcls=IPython.terminal.debugger:TerminalPdb
      --trace               Immediately break when running each test
      --capture=method      Per-test capturing method: one of fd|sys|no|tee-sys
      -s                    Shortcut for --capture=no
      --runxfail            Report the results of xfail tests as if they were
                            not marked
      --lf, --last-failed   Rerun only the tests that failed at the last run (or
                            all if none failed)
      --ff, --failed-first  Run all tests, but run the last failures first. This
                            may re-order tests and thus lead to repeated fixture
                            setup/teardown.
      --nf, --new-first     Run tests from new files first, then the rest of the
                            tests sorted by file mtime
      --cache-show=[CACHESHOW]
                            Show cache contents, don't perform collection or
                            tests. Optional argument: glob (default: '*').
      --cache-clear         Remove all cache contents at start of test run
      --lfnf, --last-failed-no-failures=
                            With ``--lf``, determines whether to execute tests
                            when there are no previously (known) failures or
                            when no cached ``lastfailed`` data was found.
                            ``all`` (the default) runs the full test suite
                            again. ``none`` just emits a message about no known
                            failures and exits successfully.
      --sw, --stepwise      Exit on test failure and continue from last failing
                            test next time
      --sw-skip, --stepwise-skip
                            Ignore the first failing test but stop on the next
                            failing test. Implicitly enables --stepwise.
      --sw-reset, --stepwise-reset
                            Resets stepwise state, restarting the stepwise
                            workflow. Implicitly enables --stepwise.

    Reporting:
      --durations=N         Show N slowest setup/test durations (N=0 for all)
      --durations-min=N     Minimal duration in seconds for inclusion in slowest
                            list. Default: 0.005 (or 0.0 if -vv is given).
      -v, --verbose         Increase verbosity
      --no-header           Disable header
      --no-summary          Disable summary
      --no-fold-skipped     Do not fold skipped tests in short summary.
      --force-short-summary
                            Force condensed summary output regardless of
                            verbosity level.
      -q, --quiet           Decrease verbosity
      --verbosity=VERBOSE   Set verbosity. Default: 0.
      -r chars              Show extra test summary info as specified by chars:
                            (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                            (p)assed, (P)assed with output, (a)ll except passed
                            (p/P), or (A)ll. (w)arnings are enabled by default
                            (see --disable-warnings), 'N' can be used to reset
                            the list. (default: 'fE').
      --disable-warnings, --disable-pytest-warnings
                            Disable warnings summary
      -l, --showlocals      Show locals in tracebacks (disabled by default)
      --no-showlocals       Hide locals in tracebacks (negate --showlocals
                            passed through addopts)
      --tb=style            Traceback print mode
                            (auto/long/short/line/native/no)
      --xfail-tb            Show tracebacks for xfail (as long as --tb != no)
      --show-capture=
                            Controls how captured stdout/stderr/log is shown on
                            failed tests. Default: all.
      --full-trace          Don't cut any tracebacks (default is to cut)
      --color=color         Color terminal output (yes/no/auto)
      --code-highlight=
                            Whether code should be highlighted (only if --color
                            is also enabled). Default: yes.
      --pastebin=mode       Send failed|all info to bpaste.net pastebin service
      --junitxml, --junit-xml=path
                            Create junit-xml style report file at given path
      --junitprefix, --junit-prefix=str
                            Prepend prefix to classnames in junit-xml output

    pytest-warnings:
      -W, --pythonwarnings PYTHONWARNINGS
                            Set which warnings to report, see -W option of
                            Python itself

    collection:
      --collect-only, --co  Only collect tests, don't execute them
      --pyargs              Try to interpret all arguments as Python packages
      --ignore=path         Ignore path during collection (multi-allowed)
      --ignore-glob=path    Ignore path pattern during collection (multi-
                            allowed)
      --deselect=nodeid_prefix
                            Deselect item (via node id prefix) during collection
                            (multi-allowed)
      --confcutdir=dir      Only load conftest.py's relative to specified dir
      --noconftest          Don't load any conftest.py files
      --keep-duplicates     Keep duplicate tests
      --collect-in-virtualenv
                            Don't ignore tests in a local virtualenv directory
      --continue-on-collection-errors
                            Force test execution even if collection errors occur
      --import-mode=
                            Prepend/append to sys.path when importing test
                            modules and conftest files. Default: prepend.
      --doctest-modules     Run doctests in all .py modules
      --doctest-report=
                            Choose another output format for diffs on doctest
                            failure
      --doctest-glob=pat    Doctests file matching pattern, default: test*.txt
      --doctest-ignore-import-errors
                            Ignore doctest collection errors
      --doctest-continue-on-failure
                            For a given doctest, continue to run after the first
                            failure

    test session debugging and configuration:
      -c, --config-file FILE
                            Load configuration from `FILE` instead of trying to
                            locate one of the implicit configuration files.
      --rootdir=ROOTDIR     Define root directory for tests. Can be relative
                            path: 'root_dir', './root_dir',
                            'root_dir/another_dir/'; absolute path:
                            '/home/user/root_dir'; path with variables:
                            '$HOME/root_dir'.
      --basetemp=dir        Base temporary directory for this test run.
                            (Warning: this directory is removed if it exists.)
      -V, --version         Display pytest version and information about
                            plugins. When given twice, also display information
                            about plugins.
      -h, --help            Show help message and configuration info
      -p name               Early-load given plugin module name or entry point
                            (multi-allowed). To avoid loading of plugins, use
                            the `no:` prefix, e.g. `no:doctest`. See also
                            --disable-plugin-autoload.
      --disable-plugin-autoload
                            Disable plugin auto-loading through entry point
                            packaging metadata. Only plugins explicitly
                            specified in -p or env var PYTEST_PLUGINS will be
                            loaded.
      --trace-config        Trace considerations of conftest.py files
      --debug=[DEBUG_FILE_NAME]
                            Store internal tracing debug information in this log
                            file. This file is opened with 'w' and truncated as
                            a result, care advised. Default: pytestdebug.log.
      -o, --override-ini OVERRIDE_INI
                            Override configuration option with "option=value"
                            style, e.g. `-o strict_xfail=True -o
                            cache_dir=cache`.
      --assert=MODE         Control assertion debugging tools.
                            'plain' performs no assertion debugging.
                            'rewrite' (the default) rewrites assert statements
                            in test modules on import to provide assert
                            expression information.
      --setup-only          Only setup fixtures, do not execute tests
      --setup-show          Show setup of fixtures while executing tests
      --setup-plan          Show what fixtures and tests would be executed but
                            don't execute anything

    logging:
      --log-level=LEVEL     Level of messages to catch/display. Not set by
                            default, so it depends on the root/parent log
                            handler's effective level, where it is "WARNING" by
                            default.
      --log-format=LOG_FORMAT
                            Log format used by the logging module
      --log-date-format=LOG_DATE_FORMAT
                            Log date format used by the logging module
      --log-cli-level=LOG_CLI_LEVEL
                            CLI logging level
      --log-cli-format=LOG_CLI_FORMAT
                            Log format used by the logging module
      --log-cli-date-format=LOG_CLI_DATE_FORMAT
                            Log date format used by the logging module
      --log-file=LOG_FILE   Path to a file when logging will be written to
      --log-file-mode=
                            Log file open mode
      --log-file-level=LOG_FILE_LEVEL
                            Log file logging level
      --log-file-format=LOG_FILE_FORMAT
                            Log format used by the logging module
      --log-file-date-format=LOG_FILE_DATE_FORMAT
                            Log date format used by the logging module
      --log-auto-indent=LOG_AUTO_INDENT
                            Auto-indent multiline messages passed to the logging
                            module. Accepts true|on, false|off or an integer.
      --log-disable=LOGGER_DISABLE
                            Disable a logger by name. Can be passed multiple
                            times.

    [pytest] configuration options in the first pytest.toml|pytest.ini|tox.ini|setup.cfg|pyproject.toml file found:

      markers (linelist):   Register new markers for test functions
      empty_parameter_set_mark (string):
                            Default marker for empty parametersets
      strict_config (bool): Any warnings encountered while parsing the `pytest`
                            section of the configuration file raise errors
      strict_markers (bool):
                            Markers not registered in the `markers` section of
                            the configuration file raise errors
      strict (bool):        Enables all strictness options, currently:
                            strict_config, strict_markers, strict_xfail,
                            strict_parametrization_ids
      filterwarnings (linelist):
                            Each line specifies a pattern for
                            warnings.filterwarnings. Processed after
                            -W/--pythonwarnings.
      norecursedirs (args): Directory patterns to avoid for recursion
      testpaths (args):     Directories to search for tests when no files or
                            directories are given on the command line
      collect_imported_tests (bool):
                            Whether to collect tests in imported modules outside
                            `testpaths`
      consider_namespace_packages (bool):
                            Consider namespace packages when resolving module
                            names during import
      usefixtures (args):   List of default fixtures to be used with this
                            project
      python_files (args):  Glob-style file patterns for Python test module
                            discovery
      python_classes (args):
                            Prefixes or glob names for Python test class
                            discovery
      python_functions (args):
                            Prefixes or glob names for Python test function and
                            method discovery
      disable_test_id_escaping_and_forfeit_all_rights_to_community_support (bool):
                            Disable string escape non-ASCII characters, might
                            cause unwanted side effects(use at your own risk)
      strict_parametrization_ids (bool):
                            Emit an error if non-unique parameter set IDs are
                            detected
      console_output_style (string):
                            Console output: "classic", or with additional
                            progress information ("progress" (percentage) |
                            "count" | "progress-even-when-capture-no" (forces
                            progress even when capture=no)
      verbosity_test_cases (string):
                            Specify a verbosity level for test case execution,
                            overriding the main level. Higher levels will
                            provide more detailed information about each test
                            case executed.
      strict_xfail (bool):  Default for the strict parameter of xfail markers
                            when not given explicitly (default: False) (alias:
                            xfail_strict)
      tmp_path_retention_count (string):
                            How many sessions should we keep the `tmp_path`
                            directories, according to
                            `tmp_path_retention_policy`.
      tmp_path_retention_policy (string):
                            Controls which directories created by the `tmp_path`
                            fixture are kept around, based on test outcome.
                            (all/failed/none)
      enable_assertion_pass_hook (bool):
                            Enables the pytest_assertion_pass hook. Make sure to
                            delete any previously generated pyc cache files.
      truncation_limit_lines (string):
                            Set threshold of LINES after which truncation will
                            take effect
      truncation_limit_chars (string):
                            Set threshold of CHARS after which truncation will
                            take effect
      verbosity_assertions (string):
                            Specify a verbosity level for assertions, overriding
                            the main level. Higher levels will provide more
                            detailed explanation when an assertion fails.
      junit_suite_name (string):
                            Test suite name for JUnit report
      junit_logging (string):
                            Write captured log messages to JUnit report: one of
                            no|log|system-out|system-err|out-err|all
      junit_log_passing_tests (bool):
                            Capture log information for passing tests to JUnit
                            report:
      junit_duration_report (string):
                            Duration time to report: one of total|call
      junit_family (string):
                            Emit XML for schema: one of legacy|xunit1|xunit2
      doctest_optionflags (args):
                            Option flags for doctests
      doctest_encoding (string):
                            Encoding used for doctest files
      cache_dir (string):   Cache directory path
      log_level (string):   Default value for --log-level
      log_format (string):  Default value for --log-format
      log_date_format (string):
                            Default value for --log-date-format
      log_cli (bool):       Enable log display during test run (also known as
                            "live logging")
      log_cli_level (string):
                            Default value for --log-cli-level
      log_cli_format (string):
                            Default value for --log-cli-format
      log_cli_date_format (string):
                            Default value for --log-cli-date-format
      log_file (string):    Default value for --log-file
      log_file_mode (string):
                            Default value for --log-file-mode
      log_file_level (string):
                            Default value for --log-file-level
      log_file_format (string):
                            Default value for --log-file-format
      log_file_date_format (string):
                            Default value for --log-file-date-format
      log_auto_indent (string):
                            Default value for --log-auto-indent
      faulthandler_timeout (string):
                            Dump the traceback of all threads if a test takes
                            more than TIMEOUT seconds to finish
      faulthandler_exit_on_timeout (bool):
                            Exit the test process if a test takes more than
                            faulthandler_timeout seconds to finish
      verbosity_subtests (string):
                            Specify verbosity level for subtests. Higher levels
                            will generate output for passed subtests. Failed
                            subtests are always reported.
      addopts (args):       Extra command line options
      minversion (string):  Minimally required pytest version
      pythonpath (paths):   Add paths to sys.path
      required_plugins (args):
                            Plugins that must be present for pytest to run

    Environment variables:
      CI                       When set to a non-empty value, pytest knows it is running in a CI process and does not truncate summary info
      BUILD_NUMBER             Equivalent to CI
      PYTEST_ADDOPTS           Extra command line options
      PYTEST_PLUGINS           Comma-separated plugins to load during startup
      PYTEST_DISABLE_PLUGIN_AUTOLOAD Set to disable plugin auto-loading
      PYTEST_DEBUG             Set to enable debug tracing of pytest's internals
      PYTEST_DEBUG_TEMPROOT    Override the system temporary directory
      PYTEST_THEME             The Pygments style to use for code output
      PYTEST_THEME_MODE        Set the PYTEST_THEME to be either 'dark' or 'light'

    to see available markers type: pytest --markers
    to see available fixtures type: pytest --fixtures
    (shown according to specified file_or_dir or current dir if not specified; fixtures with leading '_' are only shown with the '-v' option