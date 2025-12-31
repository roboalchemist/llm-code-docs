# Source: https://rich.readthedocs.io/en/latest/reference/live.html

[]

# rich.live[](#module-rich.live "Link to this heading")

*[[class]][ ]*[[rich.live.]][[Live]][(]*[[renderable]][[=]][[None]]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[screen]][[=]][[False]]*, *[[auto_refresh]][[=]][[True]]*, *[[refresh_per_second]][[=]][[4]]*, *[[transient]][[=]][[False]]*, *[[redirect_stdout]][[=]][[True]]*, *[[redirect_stderr]][[=]][[True]]*, *[[vertical_overflow]][[=]][[\'ellipsis\']]*, *[[get_renderable]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/live.html#Live)[](#rich.live.Live "Link to this definition")

:   Renders an auto-updating live display of any given renderable.

    Parameters[:]

    :   -   **renderable** (*RenderableType,* *optional*) -- The renderable to live display. Defaults to displaying nothing.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Optional Console instance. Defaults to an internal Console instance writing to stdout.

        -   **screen** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable alternate screen mode. Defaults to False.

        -   **auto_refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable auto refresh. If disabled, you will need to call refresh() or update() with refresh flag. Defaults to True

        -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of times per second to refresh the live display. Defaults to 4.

        -   **transient** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear the renderable on exit (has no effect when screen=True). Defaults to False.

        -   **redirect_stdout** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable redirection of stdout, so [`print`] may be used. Defaults to True.

        -   **redirect_stderr** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable redirection of stderr. Defaults to True.

        -   **vertical_overflow** (*VerticalOverflowMethod,* *optional*) -- How to handle renderable when it is too tall for the console. Defaults to "ellipsis".

        -   **get_renderable** (*Callable\[\[\],* *RenderableType\],* *optional*) -- Optional callable to get renderable. Defaults to None.

    *[[property]][ ]*[[is_started]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.live.Live.is_started "Link to this definition")

    :   Check if live display has been started.

    [[process_renderables]][(]*[[renderables]]*[)][[[\[source\]]]](../_modules/rich/live.html#Live.process_renderables)[](#rich.live.Live.process_renderables "Link to this definition")

    :   Process renderables to restore cursor and display progress.

        Parameters[:]

        :   **renderables** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")*\]*)

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")\]

    [[refresh]][(][)][[[\[source\]]]](../_modules/rich/live.html#Live.refresh)[](#rich.live.Live.refresh "Link to this definition")

    :   Update the display of the Live Render.

        Return type[:]

        :   None

    *[[property]][ ]*[[renderable]]*[[:]][ ][[ConsoleRenderable]](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")[ ][[\|]][ ][[RichCast]](console.html#rich.console.RichCast "rich.console.RichCast")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.live.Live.renderable "Link to this definition")

    :   Get the renderable that is being displayed

        Returns[:]

        :   Displayed renderable.

        Return type[:]

        :   RenderableType

    [[start]][(]*[[refresh]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/live.html#Live.start)[](#rich.live.Live.start "Link to this definition")

    :   Start live rendering display.

        Parameters[:]

        :   **refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also refresh. Defaults to False.

        Return type[:]

        :   None

    [[stop]][(][)][[[\[source\]]]](../_modules/rich/live.html#Live.stop)[](#rich.live.Live.stop "Link to this definition")

    :   Stop live rendering display.

        Return type[:]

        :   None

    [[update]][(]*[[renderable]]*, *[[\*]]*, *[[refresh]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/live.html#Live.update)[](#rich.live.Live.update "Link to this definition")

    :   Update the renderable that is being displayed

        Parameters[:]

        :   -   **renderable** (*RenderableType*) -- New renderable to use.

            -   **refresh** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Refresh the display. Defaults to False.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).