# Source: https://rich.readthedocs.io/en/latest/reference/padding.html

[]

# rich.padding[](#module-rich.padding "Link to this heading")

*[[class]][ ]*[[rich.padding.]][[Padding]][(]*[[renderable]]*, *[[pad]][[=]][[(0,] [0,] [0,] [0)]]*, *[[\*]]*, *[[style]][[=]][[\'none\']]*, *[[expand]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/padding.html#Padding)[](#rich.padding.Padding "Link to this definition")

:   Draw space around content.

    Example

    ::: 
    ::: highlight
        >>> print(Padding("Hello", (2, 4), style="on blue"))
    :::
    :::

    Parameters[:]

    :   -   **renderable** (*RenderableType*) -- String or other renderable.

        -   **pad** (*Union\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]\]*) -- Padding for top, right, bottom, and left borders. May be specified with 1, 2, or 4 integers (CSS style).

        -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style for padding characters. Defaults to "none".

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand padding to fit available width. Defaults to True.

    *[[classmethod]][ ]*[[indent]][(]*[[renderable]]*, *[[level]]*[)][[[\[source\]]]](../_modules/rich/padding.html#Padding.indent)[](#rich.padding.Padding.indent "Link to this definition")

    :   Make padding instance to render an indent.

        Parameters[:]

        :   -   **renderable** (*RenderableType*) -- String or other renderable.

            -   **level** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of characters to indent.

        Returns[:]

        :   A Padding instance.

        Return type[:]

        :   [Padding](#rich.padding.Padding "rich.padding.Padding")

    *[[static]][ ]*[[unpack]][(]*[[pad]]*[)][[[\[source\]]]](../_modules/rich/padding.html#Padding.unpack)[](#rich.padding.Padding.unpack "Link to this definition")

    :   Unpack padding specified in CSS style.

        Parameters[:]

        :   **pad** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]* *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]* *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*)

        Return type[:]

        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).