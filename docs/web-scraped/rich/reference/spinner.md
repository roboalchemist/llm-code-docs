# Source: https://rich.readthedocs.io/en/latest/reference/spinner.html

[]

# rich.spinner[](#module-rich.spinner "Link to this heading")

*[[class]][ ]*[[rich.spinner.]][[Spinner]][(]*[[name]]*, *[[text]][[=]][[\'\']]*, *[[\*]]*, *[[style]][[=]][[None]]*, *[[speed]][[=]][[1.0]]*[)][[[\[source\]]]](../_modules/rich/spinner.html#Spinner)[](#rich.spinner.Spinner "Link to this definition")

:   A spinner animation.

    Parameters[:]

    :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Name of spinner (run python -m rich.spinner).

        -   **text** (*RenderableType,* *optional*) -- A renderable to display at the right of the spinner (str or Text typically). Defaults to "".

        -   **style** (*StyleType,* *optional*) -- Style for spinner animation. Defaults to None.

        -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor for animation. Defaults to 1.0.

    Raises[:]

    :   [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.13)") -- If name isn't one of the supported spinner animations.

    [[render]][(]*[[time]]*[)][[[\[source\]]]](../_modules/rich/spinner.html#Spinner.render)[](#rich.spinner.Spinner.render "Link to this definition")

    :   Render the spinner for a given time.

        Parameters[:]

        :   **time** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Time in seconds.

        Returns[:]

        :   A renderable containing animation frame.

        Return type[:]

        :   RenderableType

    [[update]][(]*[[\*]]*, *[[text]][[=]][[\'\']]*, *[[style]][[=]][[None]]*, *[[speed]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/spinner.html#Spinner.update)[](#rich.spinner.Spinner.update "Link to this definition")

    :   Updates attributes of a spinner after it has been started.

        Parameters[:]

        :   -   **text** (*RenderableType,* *optional*) -- A renderable to display at the right of the spinner (str or Text typically). Defaults to "".

            -   **style** (*StyleType,* *optional*) -- Style for spinner animation. Defaults to None.

            -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor for animation. Defaults to None.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).