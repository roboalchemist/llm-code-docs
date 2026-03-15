# Source: https://rich.readthedocs.io/en/latest/reference/progress_bar.html

[]

# rich.progress_bar[](#module-rich.progress_bar "Link to this heading")

*[[class]][ ]*[[rich.progress_bar.]][[ProgressBar]][(]*[[total]][[=]][[100.0]]*, *[[completed]][[=]][[0]]*, *[[width]][[=]][[None]]*, *[[pulse]][[=]][[False]]*, *[[style]][[=]][[\'bar.back\']]*, *[[complete_style]][[=]][[\'bar.complete\']]*, *[[finished_style]][[=]][[\'bar.finished\']]*, *[[pulse_style]][[=]][[\'bar.pulse\']]*, *[[animation_time]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress_bar.html#ProgressBar)[](#rich.progress_bar.ProgressBar "Link to this definition")

:   Renders a (progress) bar. Used by rich.progress.

    Parameters[:]

    :   -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of steps in the bar. Defaults to 100. Set to None to render a pulsing animation.

        -   **completed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of steps completed. Defaults to 0.

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Width of the bar, or [`None`] for maximum width. Defaults to None.

        -   **pulse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable pulse effect. Defaults to False. Will pulse if a None total was passed.

        -   **style** (*StyleType,* *optional*) -- Style for the bar background. Defaults to "bar.back".

        -   **complete_style** (*StyleType,* *optional*) -- Style for the completed bar. Defaults to "bar.complete".

        -   **finished_style** (*StyleType,* *optional*) -- Style for a finished bar. Defaults to "bar.finished".

        -   **pulse_style** (*StyleType,* *optional*) -- Style for pulsing bars. Defaults to "bar.pulse".

        -   **animation_time** (*Optional\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*\],* *optional*) -- Time in seconds to use for animation, or None to use system time.

    *[[property]][ ]*[[percentage_completed]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.progress_bar.ProgressBar.percentage_completed "Link to this definition")

    :   Calculate percentage complete.

    [[update]][(]*[[completed]]*, *[[total]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/progress_bar.html#ProgressBar.update)[](#rich.progress_bar.ProgressBar.update "Link to this definition")

    :   Update progress with new values.

        Parameters[:]

        :   -   **completed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Number of steps completed.

            -   **total** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Total number of steps, or [`None`] to not change. Defaults to None.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).