# Source: https://rich.readthedocs.io/en/latest/reference/columns.html

[]

# rich.columns[](#module-rich.columns "Link to this heading")

*[[class]][ ]*[[rich.columns.]][[Columns]][(]*[[renderables]][[=]][[None]]*, *[[padding]][[=]][[(0,] [1)]]*, *[[\*]]*, *[[width]][[=]][[None]]*, *[[expand]][[=]][[False]]*, *[[equal]][[=]][[False]]*, *[[column_first]][[=]][[False]]*, *[[right_to_left]][[=]][[False]]*, *[[align]][[=]][[None]]*, *[[title]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/columns.html#Columns)[](#rich.columns.Columns "Link to this definition")

:   Display renderables in neat columns.

    Parameters[:]

    :   -   **renderables** (*Iterable\[RenderableType\]*) -- Any number of Rich renderables (including str).

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- The desired width of the columns, or None to auto detect. Defaults to None.

        -   **padding** (*PaddingDimensions,* *optional*) -- Optional padding around cells. Defaults to (0, 1).

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand columns to full width. Defaults to False.

        -   **equal** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Arrange in to equal sized columns. Defaults to False.

        -   **column_first** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Align items from top to bottom (rather than left to right). Defaults to False.

        -   **right_to_left** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Start column from right hand side. Defaults to False.

        -   **align** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Align value ("left", "right", or "center") or None for default. Defaults to None.

        -   **title** (*TextType,* *optional*) -- Optional title for Columns.

    [[add_renderable]][(]*[[renderable]]*[)][[[\[source\]]]](../_modules/rich/columns.html#Columns.add_renderable)[](#rich.columns.Columns.add_renderable "Link to this definition")

    :   Add a renderable to the columns.

        Parameters[:]

        :   **renderable** (*RenderableType*) -- Any renderable object.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).