# Source: https://rich.readthedocs.io/en/latest/reference/logging.html

[][]

# rich.logging[](#module-rich.logging "Link to this heading")

*[[class]][ ]*[[rich.logging.]][[RichHandler]][(]*[[level]][[=]][[0]]*, *[[console]][[=]][[None]]*, *[[\*]]*, *[[show_time]][[=]][[True]]*, *[[omit_repeated_times]][[=]][[True]]*, *[[show_level]][[=]][[True]]*, *[[show_path]][[=]][[True]]*, *[[enable_link_path]][[=]][[True]]*, *[[highlighter]][[=]][[None]]*, *[[markup]][[=]][[False]]*, *[[rich_tracebacks]][[=]][[False]]*, *[[tracebacks_width]][[=]][[None]]*, *[[tracebacks_code_width]][[=]][[88]]*, *[[tracebacks_extra_lines]][[=]][[3]]*, *[[tracebacks_theme]][[=]][[None]]*, *[[tracebacks_word_wrap]][[=]][[True]]*, *[[tracebacks_show_locals]][[=]][[False]]*, *[[tracebacks_suppress]][[=]][[()]]*, *[[tracebacks_max_frames]][[=]][[100]]*, *[[locals_max_length]][[=]][[10]]*, *[[locals_max_string]][[=]][[80]]*, *[[log_time_format]][[=]][[\'\[%x] [%X\]\']]*, *[[keywords]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/logging.html#RichHandler)[](#rich.logging.RichHandler "Link to this definition")

:   A logging handler that renders output with Rich. The time / level / message and file are displayed in columns. The level is color coded, and the message is syntax highlighted.

    ::: 
    Note

    Be careful when enabling console markup in log messages if you have configured logging for libraries not under your control. If a dependency writes messages containing square brackets, it may not produce the intended output.
    :::

    Parameters[:]

    :   -   **level** (*Union\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Log level. Defaults to logging.NOTSET.

        -   **console** ([[`Console`]](console.html#rich.console.Console "rich.console.Console"), optional) -- Optional console instance to write logs. Default will use a global console instance writing to stdout.

        -   **show_time** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a column for the time. Defaults to True.

        -   **omit_repeated_times** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Omit repetition of the same time. Defaults to True.

        -   **show_level** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a column for the level. Defaults to True.

        -   **show_path** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show the path to the original log call. Defaults to True.

        -   **enable_link_path** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable terminal link of path column to file. Defaults to True.

        -   **highlighter** ([*Highlighter*](highlighter.html#rich.highlighter.Highlighter "rich.highlighter.Highlighter")*,* *optional*) -- Highlighter to style log messages, or None to use ReprHighlighter. Defaults to None.

        -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable console markup in log messages. Defaults to False.

        -   **rich_tracebacks** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable rich tracebacks with syntax highlighting and formatting. Defaults to False.

        -   **tracebacks_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of characters used to render tracebacks, or None for full width. Defaults to None.

        -   **tracebacks_code_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of code characters used to render tracebacks, or None for full width. Defaults to 88.

        -   **tracebacks_extra_lines** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Additional lines of code to render tracebacks, or None for full width. Defaults to None.

        -   **tracebacks_theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Override pygments theme used in traceback.

        -   **tracebacks_word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of long tracebacks lines. Defaults to True.

        -   **tracebacks_show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of locals in tracebacks. Defaults to False.

        -   **tracebacks_suppress** (*Sequence\[Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *ModuleType\]\]*) -- Optional sequence of modules or paths to exclude from traceback.

        -   **tracebacks_max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Optional maximum number of frames returned by traceback.

        -   **locals_max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to 10.

        -   **locals_max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to 80.

        -   **log_time_format** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *TimeFormatterCallable\],* *optional*) -- If [`log_time`] is enabled, either string for strftime or callable that formats the time. Defaults to "\[%x %X\] ".

        -   **keywords** (*List\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- List of words to highlight instead of [`RichHandler.KEYWORDS`].

    [[HIGHLIGHTER_CLASS]][](#rich.logging.RichHandler.HIGHLIGHTER_CLASS "Link to this definition")

    :   alias of [[`ReprHighlighter`]](highlighter.html#rich.highlighter.ReprHighlighter "rich.highlighter.ReprHighlighter")

    [[emit]][(]*[[record]]*[)][[[\[source\]]]](../_modules/rich/logging.html#RichHandler.emit)[](#rich.logging.RichHandler.emit "Link to this definition")

    :   Invoked by logging.

        Parameters[:]

        :   **record** ([*LogRecord*](https://docs.python.org/3/library/logging.html#logging.LogRecord "(in Python v3.13)"))

        Return type[:]

        :   None

    [[get_level_text]][(]*[[record]]*[)][[[\[source\]]]](../_modules/rich/logging.html#RichHandler.get_level_text)[](#rich.logging.RichHandler.get_level_text "Link to this definition")

    :   Get the level name from the record.

        Parameters[:]

        :   **record** (*LogRecord*) -- LogRecord instance.

        Returns[:]

        :   A tuple of the style and level name.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

    [[render]][(]*[[\*]]*, *[[record]]*, *[[traceback]]*, *[[message_renderable]]*[)][[[\[source\]]]](../_modules/rich/logging.html#RichHandler.render)[](#rich.logging.RichHandler.render "Link to this definition")

    :   Render log for display.

        Parameters[:]

        :   -   **record** (*LogRecord*) -- logging Record.

            -   **traceback** (*Optional\[*[*Traceback*](traceback.html#rich.traceback.Traceback "rich.traceback.Traceback")*\]*) -- Traceback instance or None for no Traceback.

            -   **message_renderable** ([*ConsoleRenderable*](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")) -- Renderable (typically Text) containing log message contents.

        Returns[:]

        :   Renderable to display log.

        Return type[:]

        :   [ConsoleRenderable](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")

    [[render_message]][(]*[[record]]*, *[[message]]*[)][[[\[source\]]]](../_modules/rich/logging.html#RichHandler.render_message)[](#rich.logging.RichHandler.render_message "Link to this definition")

    :   Render message text in to Text.

        Parameters[:]

        :   -   **record** (*LogRecord*) -- logging Record.

            -   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- String containing log message.

        Returns[:]

        :   Renderable to display log message.

        Return type[:]

        :   [ConsoleRenderable](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).