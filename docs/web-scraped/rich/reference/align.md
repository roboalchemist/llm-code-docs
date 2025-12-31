# Source: https://rich.readthedocs.io/en/latest/reference/align.html

[]

# rich.align[](#module-rich.align "Link to this heading")

*[[class]][ ]*[[rich.align.]][[Align]][(]*[[renderable]]*, *[[align]][[=]][[\'left\']]*, *[[style]][[=]][[None]]*, *[[\*]]*, *[[vertical]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/align.html#Align)[](#rich.align.Align "Link to this definition")

:   Align a renderable by adding spaces if necessary.

    Parameters[:]

    :   -   **renderable** (*RenderableType*) -- A console renderable.

        -   **align** (*AlignMethod*) -- One of "left", "center", or "right""

        -   **style** (*StyleType,* *optional*) -- An optional style to apply to the background.

        -   **vertical** (*Optional\[VerticalAlignMethod\],* *optional*) -- Optional vertical align, one of "top", "middle", or "bottom". Defaults to None.

        -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Pad the right with spaces. Defaults to True.

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Restrict contents to given width, or None to use default width. Defaults to None.

        -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Set height of align renderable, or None to fit to contents. Defaults to None.

    Raises[:]

    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.13)") -- if [`align`] is not one of the expected values.

    *[[classmethod]][ ]*[[center]][(]*[[renderable]]*, *[[style]][[=]][[None]]*, *[[\*]]*, *[[vertical]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/align.html#Align.center)[](#rich.align.Align.center "Link to this definition")

    :   Align a renderable to the center.

        Parameters[:]

        :   -   **renderable** (*RenderableType*)

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

            -   **vertical** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'top\',* *\'middle\',* *\'bottom\'\]* *\|* *None*)

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        Return type[:]

        :   [Align](#rich.align.Align "rich.align.Align")

    *[[classmethod]][ ]*[[left]][(]*[[renderable]]*, *[[style]][[=]][[None]]*, *[[\*]]*, *[[vertical]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/align.html#Align.left)[](#rich.align.Align.left "Link to this definition")

    :   Align a renderable to the left.

        Parameters[:]

        :   -   **renderable** (*RenderableType*)

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

            -   **vertical** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'top\',* *\'middle\',* *\'bottom\'\]* *\|* *None*)

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        Return type[:]

        :   [Align](#rich.align.Align "rich.align.Align")

    *[[classmethod]][ ]*[[right]][(]*[[renderable]]*, *[[style]][[=]][[None]]*, *[[\*]]*, *[[vertical]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/align.html#Align.right)[](#rich.align.Align.right "Link to this definition")

    :   Align a renderable to the right.

        Parameters[:]

        :   -   **renderable** (*RenderableType*)

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

            -   **vertical** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'top\',* *\'middle\',* *\'bottom\'\]* *\|* *None*)

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        Return type[:]

        :   [Align](#rich.align.Align "rich.align.Align")

```
<!-- -->
```

*[[class]][ ]*[[rich.align.]][[VerticalCenter]][(]*[[renderable]]*, *[[style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/align.html#VerticalCenter)[](#rich.align.VerticalCenter "Link to this definition")

:   Vertically aligns a renderable.

    Warns[:]

    :   -   **This class is deprecated and may be removed in a future version. Use Align class with**

        -   **\`vertical="middle"\`.**

    Parameters[:]

    :   -   **renderable** (*RenderableType*) -- A renderable object.

        -   **style** (*StyleType,* *optional*) -- An optional style to apply to the background. Defaults to None.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).