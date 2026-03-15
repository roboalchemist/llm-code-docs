# Source: https://rich.readthedocs.io/en/latest/reference/traceback.html

[]

# rich.traceback[](#module-rich.traceback "Link to this heading")

*[[class]][ ]*[[rich.traceback.]][[Traceback]][(]*[[trace]][[=]][[None]]*, *[[\*]]*, *[[width]][[=]][[100]]*, *[[code_width]][[=]][[88]]*, *[[extra_lines]][[=]][[3]]*, *[[theme]][[=]][[None]]*, *[[word_wrap]][[=]][[False]]*, *[[show_locals]][[=]][[False]]*, *[[locals_max_length]][[=]][[10]]*, *[[locals_max_string]][[=]][[80]]*, *[[locals_hide_dunder]][[=]][[True]]*, *[[locals_hide_sunder]][[=]][[False]]*, *[[indent_guides]][[=]][[True]]*, *[[suppress]][[=]][[()]]*, *[[max_frames]][[=]][[100]]*[)][[[\[source\]]]](../_modules/rich/traceback.html#Traceback)[](#rich.traceback.Traceback "Link to this definition")

:   A Console renderable that renders a traceback.

    Parameters[:]

    :   -   **trace** (*Trace,* *optional*) -- A Trace object produced from extract. Defaults to None, which uses the last exception.

        -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of characters used to traceback. Defaults to 100.

        -   **code_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of code characters used to traceback. Defaults to 88.

        -   **extra_lines** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Additional lines of code to render. Defaults to 3.

        -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Override pygments theme used in traceback.

        -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of long lines. Defaults to False.

        -   **show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of local variables. Defaults to False.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indent guides in code and locals. Defaults to True.

        -   **locals_max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to 10.

        -   **locals_max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to 80.

        -   **locals_hide_dunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with double underscore. Defaults to True.

        -   **locals_hide_sunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with single underscore. Defaults to False.

        -   **suppress** (*Sequence\[Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *ModuleType\]\]*) -- Optional sequence of modules or paths to exclude from traceback.

        -   **max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

    *[[classmethod]][ ]*[[extract]][(]*[[exc_type]]*, *[[exc_value]]*, *[[traceback]]*, *[[\*]]*, *[[show_locals]][[=]][[False]]*, *[[locals_max_length]][[=]][[10]]*, *[[locals_max_string]][[=]][[80]]*, *[[locals_hide_dunder]][[=]][[True]]*, *[[locals_hide_sunder]][[=]][[False]]*, *[[\_visited_exceptions]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/traceback.html#Traceback.extract)[](#rich.traceback.Traceback.extract "Link to this definition")

    :   Extract traceback information.

        Parameters[:]

        :   -   **exc_type** (*Type\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.13)")*\]*) -- Exception type.

            -   **exc_value** ([*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.13)")) -- Exception value.

            -   **traceback** (*TracebackType*) -- Python Traceback object.

            -   **show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of local variables. Defaults to False.

            -   **locals_max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to 10.

            -   **locals_max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to 80.

            -   **locals_hide_dunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with double underscore. Defaults to True.

            -   **locals_hide_sunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with single underscore. Defaults to False.

            -   **\_visited_exceptions** ([*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.13)")*\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.13)")*\]* *\|* *None*)

        Returns[:]

        :   A Trace instance which you can use to construct a Traceback.

        Return type[:]

        :   Trace

    *[[classmethod]][ ]*[[from_exception]][(]*[[exc_type]]*, *[[exc_value]]*, *[[traceback]]*, *[[\*]]*, *[[width]][[=]][[100]]*, *[[code_width]][[=]][[88]]*, *[[extra_lines]][[=]][[3]]*, *[[theme]][[=]][[None]]*, *[[word_wrap]][[=]][[False]]*, *[[show_locals]][[=]][[False]]*, *[[locals_max_length]][[=]][[10]]*, *[[locals_max_string]][[=]][[80]]*, *[[locals_hide_dunder]][[=]][[True]]*, *[[locals_hide_sunder]][[=]][[False]]*, *[[indent_guides]][[=]][[True]]*, *[[suppress]][[=]][[()]]*, *[[max_frames]][[=]][[100]]*[)][[[\[source\]]]](../_modules/rich/traceback.html#Traceback.from_exception)[](#rich.traceback.Traceback.from_exception "Link to this definition")

    :   Create a traceback from exception info

        Parameters[:]

        :   -   **exc_type** (*Type\[*[*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.13)")*\]*) -- Exception type.

            -   **exc_value** ([*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException "(in Python v3.13)")) -- Exception value.

            -   **traceback** (*TracebackType*) -- Python Traceback object.

            -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of characters used to traceback. Defaults to 100.

            -   **code_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of code characters used to traceback. Defaults to 88.

            -   **extra_lines** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Additional lines of code to render. Defaults to 3.

            -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Override pygments theme used in traceback.

            -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of long lines. Defaults to False.

            -   **show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of local variables. Defaults to False.

            -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indent guides in code and locals. Defaults to True.

            -   **locals_max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to 10.

            -   **locals_max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to 80.

            -   **locals_hide_dunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with double underscore. Defaults to True.

            -   **locals_hide_sunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with single underscore. Defaults to False.

            -   **suppress** (*Iterable\[Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *ModuleType\]\]*) -- Optional sequence of modules or paths to exclude from traceback.

            -   **max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

        Returns[:]

        :   A Traceback instance that may be printed.

        Return type[:]

        :   [Traceback](#rich.traceback.Traceback "rich.traceback.Traceback")

```
<!-- -->
```

[[rich.traceback.]][[install]][(]*[[\*]]*, *[[console]][[=]][[None]]*, *[[width]][[=]][[100]]*, *[[code_width]][[=]][[88]]*, *[[extra_lines]][[=]][[3]]*, *[[theme]][[=]][[None]]*, *[[word_wrap]][[=]][[False]]*, *[[show_locals]][[=]][[False]]*, *[[locals_max_length]][[=]][[10]]*, *[[locals_max_string]][[=]][[80]]*, *[[locals_hide_dunder]][[=]][[True]]*, *[[locals_hide_sunder]][[=]][[None]]*, *[[indent_guides]][[=]][[True]]*, *[[suppress]][[=]][[()]]*, *[[max_frames]][[=]][[100]]*[)][[[\[source\]]]](../_modules/rich/traceback.html#install)[](#rich.traceback.install "Link to this definition")

:   Install a rich traceback handler.

    Once installed, any tracebacks will be printed with syntax highlighting and rich formatting.

    Parameters[:]

    :   -   **console** (*Optional\[*[*Console*](console.html#rich.console.Console "rich.console.Console")*\],* *optional*) -- Console to write exception to. Default uses internal Console instance.

        -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Width (in characters) of traceback. Defaults to 100.

        -   **code_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Code width (in characters) of traceback. Defaults to 88.

        -   **extra_lines** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Extra lines of code. Defaults to 3.

        -   **theme** (*Optional\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Pygments theme to use in traceback. Defaults to [`None`] which will pick a theme appropriate for the platform.

        -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of long lines. Defaults to False.

        -   **show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of local variables. Defaults to False.

        -   **locals_max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to 10.

        -   **locals_max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to 80.

        -   **locals_hide_dunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with double underscore. Defaults to True.

        -   **locals_hide_sunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide locals prefixed with single underscore. Defaults to False.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indent guides in code and locals. Defaults to True.

        -   **suppress** (*Sequence\[Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *ModuleType\]\]*) -- Optional sequence of modules or paths to exclude from traceback.

        -   **max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

    Returns[:]

    :   The previous exception handler that was replaced.

    Return type[:]

    :   Callable

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).