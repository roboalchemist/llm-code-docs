# Source: https://rich.readthedocs.io/en/latest/reference/status.html

[]

# rich.status[](#module-rich.status "Link to this heading")

*[[class]][ ]*[[rich.status.]][[Status]][(]*[[status]]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[spinner]][[=]][[\'dots\']]*, *[[spinner_style]][[=]][[\'status.spinner\']]*, *[[speed]][[=]][[1.0]]*, *[[refresh_per_second]][[=]][[12.5]]*[)][[[\[source\]]]](../_modules/rich/status.html#Status)[](#rich.status.Status "Link to this definition")

:   Displays a status indicator with a 'spinner' animation.

    Parameters[:]

    :   -   **status** (*RenderableType*) -- A status renderable (str or Text typically).

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console instance to use, or None for global console. Defaults to None.

        -   **spinner** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Name of spinner animation (see python -m rich.spinner). Defaults to "dots".

        -   **spinner_style** (*StyleType,* *optional*) -- Style of spinner. Defaults to "status.spinner".

        -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor for spinner animation. Defaults to 1.0.

        -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of refreshes per second. Defaults to 12.5.

    *[[property]][ ]*[[console]]*[[:]][ ][[Console]](console.html#rich.console.Console "rich.console.Console")*[](#rich.status.Status.console "Link to this definition")

    :   Get the Console used by the Status objects.

    [[start]][(][)][[[\[source\]]]](../_modules/rich/status.html#Status.start)[](#rich.status.Status.start "Link to this definition")

    :   Start the status animation.

        Return type[:]

        :   None

    [[stop]][(][)][[[\[source\]]]](../_modules/rich/status.html#Status.stop)[](#rich.status.Status.stop "Link to this definition")

    :   Stop the spinner animation.

        Return type[:]

        :   None

    [[update]][(]*[[status]][[=]][[None]]*, *[[\*]]*, *[[spinner]][[=]][[None]]*, *[[spinner_style]][[=]][[None]]*, *[[speed]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/status.html#Status.update)[](#rich.status.Status.update "Link to this definition")

    :   Update status.

        Parameters[:]

        :   -   **status** (*Optional\[RenderableType\],* *optional*) -- New status renderable or None for no change. Defaults to None.

            -   **spinner** (*Optional\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- New spinner or None for no change. Defaults to None.

            -   **spinner_style** (*Optional\[StyleType\],* *optional*) -- New spinner style or None for no change. Defaults to None.

            -   **speed** (*Optional\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\],* *optional*) -- Speed factor for spinner animation or None for no change. Defaults to None.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).