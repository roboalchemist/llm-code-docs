# Source: https://rich.readthedocs.io/en/latest/reference/panel.html

[]

# rich.panel[](#module-rich.panel "Link to this heading")

*[[class]][ ]*[[rich.panel.]][[Panel]][(]*[[renderable]]*, *[[box]][[=]][[Box(\...)]]*, *[[\*]]*, *[[title]][[=]][[None]]*, *[[title_align]][[=]][[\'center\']]*, *[[subtitle]][[=]][[None]]*, *[[subtitle_align]][[=]][[\'center\']]*, *[[safe_box]][[=]][[None]]*, *[[expand]][[=]][[True]]*, *[[style]][[=]][[\'none\']]*, *[[border_style]][[=]][[\'none\']]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*, *[[padding]][[=]][[(0,] [1)]]*, *[[highlight]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/panel.html#Panel)[](#rich.panel.Panel "Link to this definition")

:   A console renderable that draws a border around its contents.

    Example

    ::: 
    ::: highlight
        >>> console.print(Panel("Hello, World!"))
    :::
    :::

    Parameters[:]

    :   -   **renderable** (*RenderableType*) -- A console renderable object.

        -   **box** (*Box*) -- A Box instance that defines the look of the border (see [[Box]](../appendix/box.html#appendix-box). Defaults to box.ROUNDED.

        -   **title** (*Optional\[TextType\],* *optional*) -- Optional title displayed in panel header. Defaults to None.

        -   **title_align** (*AlignMethod,* *optional*) -- Alignment of title. Defaults to "center".

        -   **subtitle** (*Optional\[TextType\],* *optional*) -- Optional subtitle displayed in panel footer. Defaults to None.

        -   **subtitle_align** (*AlignMethod,* *optional*) -- Alignment of subtitle. Defaults to "center".

        -   **safe_box** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- If True the panel will stretch to fill the console width, otherwise it will be sized to fit the contents. Defaults to True.

        -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The style of the panel (border and contents). Defaults to "none".

        -   **border_style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The style of the border. Defaults to "none".

        -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Optional width of panel. Defaults to None to auto-detect.

        -   **height** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Optional height of panel. Defaults to None to auto-detect.

        -   **padding** (*Optional\[PaddingDimensions\]*) -- Optional padding around renderable. Defaults to 0.

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable automatic highlighting of panel title (if str). Defaults to False.

    *[[classmethod]][ ]*[[fit]][(]*[[renderable]]*, *[[box]][[=]][[Box(\...)]]*, *[[\*]]*, *[[title]][[=]][[None]]*, *[[title_align]][[=]][[\'center\']]*, *[[subtitle]][[=]][[None]]*, *[[subtitle_align]][[=]][[\'center\']]*, *[[safe_box]][[=]][[None]]*, *[[style]][[=]][[\'none\']]*, *[[border_style]][[=]][[\'none\']]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*, *[[padding]][[=]][[(0,] [1)]]*, *[[highlight]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/panel.html#Panel.fit)[](#rich.panel.Panel.fit "Link to this definition")

    :   An alternative constructor that sets expand=False.

        Parameters[:]

        :   -   **renderable** (*RenderableType*)

            -   **box** (*Box*)

            -   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text") *\|* *None*)

            -   **title_align** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'left\',* *\'center\',* *\'right\'\]*)

            -   **subtitle** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text") *\|* *None*)

            -   **subtitle_align** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'left\',* *\'center\',* *\'right\'\]*)

            -   **safe_box** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None*)

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style"))

            -   **border_style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style"))

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]* *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]* *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*)

            -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [Panel](#rich.panel.Panel "rich.panel.Panel")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).