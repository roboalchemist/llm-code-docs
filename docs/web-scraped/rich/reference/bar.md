# Source: https://rich.readthedocs.io/en/latest/reference/bar.html

[]

# rich.bar[](#module-rich.bar "Link to this heading")

*[[class]][ ]*[[rich.bar.]][[Bar]][(]*[[size]]*, *[[begin]]*, *[[end]]*, *[[\*]]*, *[[width]][[=]][[None]]*, *[[color]][[=]][[\'default\']]*, *[[bgcolor]][[=]][[\'default\']]*[)][[[\[source\]]]](../_modules/rich/bar.html#Bar)[](#rich.bar.Bar "Link to this definition")

:   Renders a solid block bar.

    Parameters[:]

    :   -   **size** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Value for the end of the bar.

        -   **begin** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Begin point (between 0 and size, inclusive).

        -   **end** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- End point (between 0 and size, inclusive).

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Width of the bar, or [`None`] for maximum width. Defaults to None.

        -   **color** (*Union\[*[*Color*](color.html#rich.color.Color "rich.color.Color")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Color of the bar. Defaults to "default".

        -   **bgcolor** (*Union\[*[*Color*](color.html#rich.color.Color "rich.color.Color")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Color of bar background. Defaults to "default".

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).