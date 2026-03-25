# Source: https://rich.readthedocs.io/en/latest/reference/console.html

[]

# rich.console[](#module-rich.console "Link to this heading")

*[[class]][ ]*[[rich.console.]][[Capture]][(]*[[console]]*[)][[[\[source\]]]](../_modules/rich/console.html#Capture)[](#rich.console.Capture "Link to this definition")

:   Context manager to capture the result of printing to the console. See [[`capture()`]](#rich.console.Console.capture "rich.console.Console.capture") for how to use.

    Parameters[:]

    :   **console** ([*Console*](#rich.console.Console "rich.console.Console")) -- A console instance to capture output.

    [[get]][(][)][[[\[source\]]]](../_modules/rich/console.html#Capture.get)[](#rich.console.Capture.get "Link to this definition")

    :   Get the result of the capture.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[exception]][ ]*[[rich.console.]][[CaptureError]][[[\[source\]]]](../_modules/rich/console.html#CaptureError)[](#rich.console.CaptureError "Link to this definition")

:   An error in the Capture context manager.

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[Console]][(]*[[\*]]*, *[[color_system=\'auto\']]*, *[[force_terminal=None]]*, *[[force_jupyter=None]]*, *[[force_interactive=None]]*, *[[soft_wrap=False]]*, *[[theme=None]]*, *[[stderr=False]]*, *[[file=None]]*, *[[quiet=False]]*, *[[width=None]]*, *[[height=None]]*, *[[style=None]]*, *[[no_color=None]]*, *[[tab_size=8]]*, *[[record=False]]*, *[[markup=True]]*, *[[emoji=True]]*, *[[emoji_variant=None]]*, *[[highlight=True]]*, *[[log_time=True]]*, *[[log_path=True]]*, *[[log_time_format=\'\[%X\]\']]*, *[[highlighter=\<rich.highlighter.ReprHighlighter] [object\>]]*, *[[legacy_windows=None]]*, *[[safe_box=True]]*, *[[get_datetime=None]]*, *[[get_time=None]]*, *[[\_environ=None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console)[](#rich.console.Console "Link to this definition")

:   A high level console interface.

    Parameters[:]

    :   -   **color_system** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The color system supported by your terminal, either [`"standard"`], [`"256"`] or [`"truecolor"`]. Leave as [`"auto"`] to autodetect.

        -   **force_terminal** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable/disable terminal control codes, or None to auto-detect terminal. Defaults to None.

        -   **force_jupyter** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable/disable Jupyter rendering, or None to auto-detect Jupyter. Defaults to None.

        -   **force_interactive** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable/disable interactive mode, or None to auto detect. Defaults to None.

        -   **soft_wrap** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Set soft wrap default on print method. Defaults to False.

        -   **theme** ([*Theme*](theme.html#rich.theme.Theme "rich.theme.Theme")*,* *optional*) -- An optional style theme object, or [`None`] for default theme.

        -   **stderr** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Use stderr rather than stdout if [`file`] is not specified. Defaults to False.

        -   **file** (*IO,* *optional*) -- A file object where the console should write to. Defaults to stdout.

        -   **quiet** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *Optional*) -- Boolean to suppress all output. Defaults to False.

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- The width of the terminal. Leave as default to auto-detect width.

        -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- The height of the terminal. Leave as default to auto-detect height.

        -   **style** (*StyleType,* *optional*) -- Style to apply to all output, or None for no style. Defaults to None.

        -   **no_color** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enabled no color mode, or None to auto detect. Defaults to None.

        -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of spaces used to replace a tab character. Defaults to 8.

        -   **record** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Boolean to enable recording of terminal output, required to call [[`export_html()`]](#rich.console.Console.export_html "rich.console.Console.export_html"), [[`export_svg()`]](#rich.console.Console.export_svg "rich.console.Console.export_svg"), and [[`export_text()`]](#rich.console.Console.export_text "rich.console.Console.export_text"). Defaults to False.

        -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Boolean to enable [[Console Markup]](../markup.html#console-markup). Defaults to True.

        -   **emoji** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable emoji code. Defaults to True.

        -   **emoji_variant** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional emoji variant, either "text" or "emoji". Defaults to None.

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable automatic highlighting. Defaults to True.

        -   **log_time** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Boolean to enable logging of time by [[`log()`]](#rich.console.Console.log "rich.console.Console.log") methods. Defaults to True.

        -   **log_path** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Boolean to enable the logging of the caller by [[`log()`]](#rich.console.Console.log "rich.console.Console.log"). Defaults to True.

        -   **log_time_format** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *TimeFormatterCallable\],* *optional*) -- If [`log_time`] is enabled, either string for strftime or callable that formats the time. Defaults to "\[%X\] ".

        -   **highlighter** (*HighlighterType,* *optional*) -- Default highlighter.

        -   **legacy_windows** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable legacy Windows mode, or [`None`] to auto detect. Defaults to [`None`].

        -   **safe_box** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Restrict box options that don't render on legacy Windows.

        -   **get_datetime** (*Callable\[\[\],* *datetime\],* *optional*) -- Callable that gets the current time as a datetime.datetime object (used by Console.log), or None for datetime.now.

        -   **get_time** (*Callable\[\[\],* *time\],* *optional*) -- Callable that gets the current time in seconds, default uses time.monotonic.

        -   **\_environ** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*)

    [[begin_capture]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.begin_capture)[](#rich.console.Console.begin_capture "Link to this definition")

    :   Begin capturing console output. Call [[`end_capture()`]](#rich.console.Console.end_capture "rich.console.Console.end_capture") to exit capture mode and return output.

        Return type[:]

        :   None

    [[bell]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.bell)[](#rich.console.Console.bell "Link to this definition")

    :   Play a 'bell' sound (if supported by the terminal).

        Return type[:]

        :   None

    [[capture]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.capture)[](#rich.console.Console.capture "Link to this definition")

    :   A context manager to *capture* the result of print() or log() in a string, rather than writing it to the console.

        Example

        ::: 
        ::: highlight
            >>> from rich.console import Console
            >>> console = Console()
            >>> with console.capture() as capture:
            ...     console.print("[bold magenta]Hello World[/]")
            >>> print(capture.get())
        :::
        :::

        Returns[:]

        :   Context manager with disables writing to the terminal.

        Return type[:]

        :   [Capture](#rich.console.Capture "rich.console.Capture")

    [[clear]][(]*[[home]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.clear)[](#rich.console.Console.clear "Link to this definition")

    :   Clear the screen.

        Parameters[:]

        :   **home** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also move the cursor to 'home' position. Defaults to True.

        Return type[:]

        :   None

    [[clear_live]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.clear_live)[](#rich.console.Console.clear_live "Link to this definition")

    :   Clear the Live instance. Used by the Live context manager (no need to call directly).

        Return type[:]

        :   None

    *[[property]][ ]*[[color_system]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.console.Console.color_system "Link to this definition")

    :   Get color system string.

        Returns[:]

        :   "standard", "256" or "truecolor".

        Return type[:]

        :   Optional\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]

    [[control]][(]*[[\*]][[control]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.control)[](#rich.console.Console.control "Link to this definition")

    :   Insert non-printing control codes.

        Parameters[:]

        :   -   **control_codes** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Control codes, such as those that may move the cursor.

            -   **control** ([*Control*](control.html#rich.control.Control "rich.control.Control"))

        Return type[:]

        :   None

    *[[property]][ ]*[[encoding]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.console.Console.encoding "Link to this definition")

    :   Get the encoding of the console file, e.g. [`"utf-8"`].

        Returns[:]

        :   A standard encoding string.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[end_capture]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.end_capture)[](#rich.console.Console.end_capture "Link to this definition")

    :   End capture mode and return captured string.

        Returns[:]

        :   Console output.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[export_html]][(]*[[\*]]*, *[[theme]][[=]][[None]]*, *[[clear]][[=]][[True]]*, *[[code_format]][[=]][[None]]*, *[[inline_styles]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.export_html)[](#rich.console.Console.export_html "Link to this definition")

    :   Generate HTML from console contents (requires record=True argument in constructor).

        Parameters[:]

        :   -   **theme** (*TerminalTheme,* *optional*) -- TerminalTheme object containing console colors.

            -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`].

            -   **code_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format string to render HTML. In addition to '', '', and '', should contain '' if inline_styles is [`False`].

            -   **inline_styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- If [`True`] styles will be inlined in to spans, which makes files larger but easier to cut and paste markup. If [`False`], styles will be embedded in a style tag. Defaults to False.

        Returns[:]

        :   String containing console contents as HTML.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[export_svg]][(]*[[\*]]*, *[[title]][[=]][[\'Rich\']]*, *[[theme]][[=]][[None]]*, *[[clear]][[=]][[True]]*, *[[code_format]][[=]][[\'\<svg] [class=\"rich-terminal\"] [viewBox=\"0] [0] [] [\"] [xmlns=\"http://www.w3.org/2000/svg\"\>\\n]    [\<!\--] [Generated] [with] [Rich] [https://www.textualize.io] [\--\>\\n]    [\<style\>\\n\\n]    [\@font-face] [        [font-family:] [\"Fira] [Code\";\\n]        [src:] [local(\"FiraCode-Regular\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Regular.woff2\")] [format(\"woff2\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Regular.woff\")] [format(\"woff\");\\n]        [font-style:] [normal;\\n]        [font-weight:] [400;\\n]    [}}\\n]    [\@font-face] [        [font-family:] [\"Fira] [Code\";\\n]        [src:] [local(\"FiraCode-Bold\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Bold.woff2\")] [format(\"woff2\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Bold.woff\")] [format(\"woff\");\\n]        [font-style:] [bold;\\n]        [font-weight:] [700;\\n]    [}}\\n\\n]    [.-matrix] [        [font-family:] [Fira] [Code,] [monospace;\\n]        [font-size:] [px;\\n]        [line-height:] [px;\\n]        [font-variant-east-asian:] [full-width;\\n]    [}}\\n\\n]    [.-title] [        [font-size:] [18px;\\n]        [font-weight:] [bold;\\n]        [font-family:] [arial;\\n]    [}}\\n\\n]    [\\n]    [\</style\>\\n\\n]    [\<defs\>\\n]    [\<clipPath] [id=\"-clip-terminal\"\>\\n]      [\<rect] [x=\"0\"] [y=\"0\"] [width=\"\"] [height=\"\"] [/\>\\n]    [\</clipPath\>\\n]    [\\n]    [\</defs\>\\n\\n]    [\\n]    [\<g] [transform=\"translate(,] [)\"] [clip-path=\"url(#-clip-terminal)\"\>\\n]    [\\n]    [\<g] [class=\"-matrix\"\>\\n]    [\\n]    [\</g\>\\n]    [\</g\>\\n\</svg\>\\n\']]*, *[[font_aspect_ratio]][[=]][[0.61]]*, *[[unique_id]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.export_svg)[](#rich.console.Console.export_svg "Link to this definition")

    :   Generate an SVG from the console contents (requires record=True in Console constructor).

        Parameters[:]

        :   -   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The title of the tab in the output image

            -   **theme** (*TerminalTheme,* *optional*) -- The [`TerminalTheme`] object to use to style the terminal

            -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`]

            -   **code_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format string used to generate the SVG. Rich will inject a number of variables into the string in order to form the final SVG output. The default template used and the variables injected by Rich can be found by inspecting the [`console.CONSOLE_SVG_FORMAT`] variable.

            -   **font_aspect_ratio** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- The width to height ratio of the font used in the [`code_format`] string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font). If you aren't specifying a different font inside [`code_format`], you probably don't need this.

            -   **unique_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- unique id that is used as the prefix for various elements (CSS styles, node ids). If not set, this defaults to a computed value based on the recorded content.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[export_text]][(]*[[\*]]*, *[[clear]][[=]][[True]]*, *[[styles]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.export_text)[](#rich.console.Console.export_text "Link to this definition")

    :   Generate text from console contents (requires record=True argument in constructor).

        Parameters[:]

        :   -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`].

            -   **styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- If [`True`], ansi escape codes will be included. [`False`] for plain text. Defaults to [`False`].

        Returns[:]

        :   String containing console contents.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    *[[property]][ ]*[[file]]*[[:]][ ][[IO]](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]]*[](#rich.console.Console.file "Link to this definition")

    :   Get the file object to write to.

    [[get_style]][(]*[[name]]*, *[[\*]]*, *[[default]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.get_style)[](#rich.console.Console.get_style "Link to this definition")

    :   Get a Style instance by its theme name or parse a definition.

        Parameters[:]

        :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The name of a style or a style definition.

            -   **default** ([*Style*](style.html#rich.style.Style "rich.style.Style") *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *None*)

        Returns[:]

        :   A Style object.

        Return type[:]

        :   [Style](style.html#rich.style.Style "rich.style.Style")

        Raises[:]

        :   **MissingStyle** -- If no style could be parsed from name.

    *[[property]][ ]*[[height]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.Console.height "Link to this definition")

    :   Get the height of the console.

        Returns[:]

        :   The height (in lines) of the console.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    [[input]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[markup]][[=]][[True]]*, *[[emoji]][[=]][[True]]*, *[[password]][[=]][[False]]*, *[[stream]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.input)[](#rich.console.Console.input "Link to this definition")

    :   Displays a prompt and waits for input from the user. The prompt may contain color / style.

        It works in the same way as Python's builtin [[`input()`]](#rich.console.Console.input "rich.console.Console.input") function and provides elaborate line editing and history features if Python's builtin [[`readline`]](https://docs.python.org/3/library/readline.html#module-readline "(in Python v3.13)") module is previously loaded.

        Parameters[:]

        :   -   **prompt** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\]*) -- Text to render in the prompt.

            -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable console markup (requires a str prompt). Defaults to True.

            -   **emoji** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable emoji (requires a str prompt). Defaults to True.

            -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- (bool, optional): Hide typed text. Defaults to False.

            -   **stream** ([*TextIO*](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)") *\|* *None*) -- (TextIO, optional): Optional file to read input from (rather than stdin). Defaults to None.

        Returns[:]

        :   Text read from stdin.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    *[[property]][ ]*[[is_alt_screen]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.Console.is_alt_screen "Link to this definition")

    :   Check if the alt screen was enabled.

        Returns[:]

        :   True if the alt screen was enabled, otherwise False.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    *[[property]][ ]*[[is_dumb_terminal]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.Console.is_dumb_terminal "Link to this definition")

    :   Detect dumb terminal.

        Returns[:]

        :   True if writing to a dumb terminal, otherwise False.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    *[[property]][ ]*[[is_terminal]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.Console.is_terminal "Link to this definition")

    :   Check if the console is writing to a terminal.

        Returns[:]

        :   

            True if the console writing to a device capable of

            :   understanding escape sequences, otherwise False.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[line]][(]*[[count]][[=]][[1]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.line)[](#rich.console.Console.line "Link to this definition")

    :   Write new line(s).

        Parameters[:]

        :   **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of new lines. Defaults to 1.

        Return type[:]

        :   None

    [[log]][(]*[[\*]][[objects]]*, *[[sep]][[=]][[\'] [\']]*, *[[end]][[=]][[\'\\n\']]*, *[[style]][[=]][[None]]*, *[[justify]][[=]][[None]]*, *[[emoji]][[=]][[None]]*, *[[markup]][[=]][[None]]*, *[[highlight]][[=]][[None]]*, *[[log_locals]][[=]][[False]]*, *[[\_stack_offset]][[=]][[1]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.log)[](#rich.console.Console.log "Link to this definition")

    :   Log rich content to the terminal.

        Parameters[:]

        :   -   **objects** (*positional args*) -- Objects to log to the terminal.

            -   **sep** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write between print data. Defaults to " ".

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write at end of print data. Defaults to "\\n".

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- A style to apply to output. Defaults to None.

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- One of "left", "right", "center", or "full". Defaults to [`None`].

            -   **emoji** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable emoji code, or [`None`] to use console default. Defaults to None.

            -   **markup** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable markup, or [`None`] to use console default. Defaults to None.

            -   **highlight** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable automatic highlighting, or [`None`] to use console default. Defaults to None.

            -   **log_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Boolean to enable logging of locals where [`log()`] was called. Defaults to False.

            -   **\_stack_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Offset of caller from end of call stack. Defaults to 1.

        Return type[:]

        :   None

    [[measure]][(]*[[renderable]]*, *[[\*]]*, *[[options]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.measure)[](#rich.console.Console.measure "Link to this definition")

    :   Measure a renderable. Returns a [[`Measurement`]](measure.html#rich.measure.Measurement "rich.measure.Measurement") object which contains information regarding the number of characters required to print the renderable.

        Parameters[:]

        :   -   **renderable** (*RenderableType*) -- Any renderable or string.

            -   **options** (*Optional\[*[*ConsoleOptions*](#rich.console.ConsoleOptions "rich.console.ConsoleOptions")*\],* *optional*) -- Options to use when measuring, or None to use default options. Defaults to None.

        Returns[:]

        :   A measurement of the renderable.

        Return type[:]

        :   [Measurement](measure.html#rich.measure.Measurement "rich.measure.Measurement")

    [[on_broken_pipe]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.on_broken_pipe)[](#rich.console.Console.on_broken_pipe "Link to this definition")

    :   This function is called when a BrokenPipeError is raised.

        This can occur when piping Textual output in Linux and macOS. The default implementation is to exit the app, but you could implement this method in a subclass to change the behavior.

        See [https://docs.python.org/3/library/signal.html#note-on-sigpipe](https://docs.python.org/3/library/signal.html#note-on-sigpipe) for details.

        Return type[:]

        :   None

    *[[property]][ ]*[[options]]*[[:]][ ][[ConsoleOptions]](#rich.console.ConsoleOptions "rich.console.ConsoleOptions")*[](#rich.console.Console.options "Link to this definition")

    :   Get default console options.

    [[out]][(]*[[\*]][[objects]]*, *[[sep]][[=]][[\'] [\']]*, *[[end]][[=]][[\'\\n\']]*, *[[style]][[=]][[None]]*, *[[highlight]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.out)[](#rich.console.Console.out "Link to this definition")

    :   Output to the terminal. This is a low-level way of writing to the terminal which unlike [[`print()`]](#rich.console.Console.print "rich.console.Console.print") won't pretty print, wrap text, or apply markup, but will optionally apply highlighting and a basic style.

        Parameters[:]

        :   -   **sep** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write between print data. Defaults to " ".

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write at end of print data. Defaults to "\\n".

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- A style to apply to output. Defaults to None.

            -   **highlight** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable automatic highlighting, or [`None`] to use console default. Defaults to [`None`].

            -   **objects** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"))

        Return type[:]

        :   None

    [[pager]][(]*[[pager]][[=]][[None]]*, *[[styles]][[=]][[False]]*, *[[links]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.pager)[](#rich.console.Console.pager "Link to this definition")

    :   A context manager to display anything printed within a "pager". The pager application is defined by the system and will typically support at least pressing a key to scroll.

        Parameters[:]

        :   -   **pager** (*Pager,* *optional*) -- A pager object, or None to use [`SystemPager`]. Defaults to None.

            -   **styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show styles in pager. Defaults to False.

            -   **links** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show links in pager. Defaults to False.

        Return type[:]

        :   [*PagerContext*](#rich.console.PagerContext "rich.console.PagerContext")

        Example

        ::: 
        ::: highlight
            >>> from rich.console import Console
            >>> from rich.__main__ import make_test_card
            >>> console = Console()
            >>> with console.pager():
                    console.print(make_test_card())
        :::
        :::

        Returns[:]

        :   A context manager.

        Return type[:]

        :   [PagerContext](#rich.console.PagerContext "rich.console.PagerContext")

        Parameters[:]

        :   -   **pager** (*Pager* *\|* *None*)

            -   **styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

            -   **links** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[pop_render_hook]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.pop_render_hook)[](#rich.console.Console.pop_render_hook "Link to this definition")

    :   Pop the last renderhook from the stack.

        Return type[:]

        :   None

    [[pop_theme]][(][)][[[\[source\]]]](../_modules/rich/console.html#Console.pop_theme)[](#rich.console.Console.pop_theme "Link to this definition")

    :   Remove theme from top of stack, restoring previous theme.

        Return type[:]

        :   None

    [[print]][(]*[[\*]][[objects]]*, *[[sep]][[=]][[\'] [\']]*, *[[end]][[=]][[\'\\n\']]*, *[[style]][[=]][[None]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[None]]*, *[[emoji]][[=]][[None]]*, *[[markup]][[=]][[None]]*, *[[highlight]][[=]][[None]]*, *[[width]][[=]][[None]]*, *[[height]][[=]][[None]]*, *[[crop]][[=]][[True]]*, *[[soft_wrap]][[=]][[None]]*, *[[new_line_start]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.print)[](#rich.console.Console.print "Link to this definition")

    :   Print to the console.

        Parameters[:]

        :   -   **objects** (*positional args*) -- Objects to log to the terminal.

            -   **sep** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write between print data. Defaults to " ".

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to write at end of print data. Defaults to "\\n".

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- A style to apply to output. Defaults to None.

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "default", "left", "right", "center", or "full". Defaults to [`None`].

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "ignore", "crop", "fold", or "ellipsis". Defaults to None.

            -   **no_wrap** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Disable word wrapping. Defaults to None.

            -   **emoji** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable emoji code, or [`None`] to use console default. Defaults to [`None`].

            -   **markup** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable markup, or [`None`] to use console default. Defaults to [`None`].

            -   **highlight** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable automatic highlighting, or [`None`] to use console default. Defaults to [`None`].

            -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Width of output, or [`None`] to auto-detect. Defaults to [`None`].

            -   **crop** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Crop output to width of terminal. Defaults to True.

            -   **soft_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable soft wrap mode which disables word wrapping and cropping of text or [`None`] for Console default. Defaults to [`None`].

            -   **new_line_start** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *False*) -- Insert a new line at the start if the output contains more than one line. Defaults to [`False`].

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        Return type[:]

        :   None

    [[print_exception]][(]*[[\*]]*, *[[width]][[=]][[100]]*, *[[extra_lines]][[=]][[3]]*, *[[theme]][[=]][[None]]*, *[[word_wrap]][[=]][[False]]*, *[[show_locals]][[=]][[False]]*, *[[suppress]][[=]][[()]]*, *[[max_frames]][[=]][[100]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.print_exception)[](#rich.console.Console.print_exception "Link to this definition")

    :   Prints a rich render of the last exception and traceback.

        Parameters[:]

        :   -   **width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Number of characters used to render code. Defaults to 100.

            -   **extra_lines** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Additional lines of code to render. Defaults to 3.

            -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Override pygments theme used in traceback

            -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of long lines. Defaults to False.

            -   **show_locals** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable display of local variables. Defaults to False.

            -   **suppress** (*Iterable\[Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *ModuleType\]\]*) -- Optional sequence of modules or paths to exclude from traceback.

            -   **max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

        Return type[:]

        :   None

    [[print_json]][(]*[[json]][[=]][[None]]*, *[[\*]]*, *[[data]][[=]][[None]]*, *[[indent]][[=]][[2]]*, *[[highlight]][[=]][[True]]*, *[[skip_keys]][[=]][[False]]*, *[[ensure_ascii]][[=]][[False]]*, *[[check_circular]][[=]][[True]]*, *[[allow_nan]][[=]][[True]]*, *[[default]][[=]][[None]]*, *[[sort_keys]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.print_json)[](#rich.console.Console.print_json "Link to this definition")

    :   Pretty prints JSON. Output will be valid JSON.

        Parameters[:]

        :   -   **json** (*Optional\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- A string containing JSON.

            -   **data** (*Any*) -- If json is not supplied, then encode this data.

            -   **indent** (*Union\[None,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Number of spaces to indent. Defaults to 2.

            -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable highlighting of output: Defaults to True.

            -   **skip_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Skip keys not of a basic type. Defaults to False.

            -   **ensure_ascii** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Escape all non-ascii characters. Defaults to False.

            -   **check_circular** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Check for circular references. Defaults to True.

            -   **allow_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Allow NaN and Infinity values. Defaults to True.

            -   **default** (*Callable,* *optional*) -- A callable that converts values that can not be encoded in to something that can be JSON encoded. Defaults to None.

            -   **sort_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Sort dictionary keys. Defaults to False.

        Return type[:]

        :   None

    [[push_render_hook]][(]*[[hook]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.push_render_hook)[](#rich.console.Console.push_render_hook "Link to this definition")

    :   Add a new render hook to the stack.

        Parameters[:]

        :   **hook** ([*RenderHook*](#rich.console.RenderHook "rich.console.RenderHook")) -- Render hook instance.

        Return type[:]

        :   None

    [[push_theme]][(]*[[theme]]*, *[[\*]]*, *[[inherit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.push_theme)[](#rich.console.Console.push_theme "Link to this definition")

    :   Push a new theme on to the top of the stack, replacing the styles from the previous theme. Generally speaking, you should call [[`use_theme()`]](#rich.console.Console.use_theme "rich.console.Console.use_theme") to get a context manager, rather than calling this method directly.

        Parameters[:]

        :   -   **theme** ([*Theme*](theme.html#rich.theme.Theme "rich.theme.Theme")) -- A theme instance.

            -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Inherit existing styles. Defaults to True.

        Return type[:]

        :   None

    [[render]][(]*[[renderable]]*, *[[options]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.render)[](#rich.console.Console.render "Link to this definition")

    :   Render an object in to an iterable of Segment instances.

        This method contains the logic for rendering objects with the console protocol. You are unlikely to need to use it directly, unless you are extending the library.

        Parameters[:]

        :   -   **renderable** (*RenderableType*) -- An object supporting the console protocol, or an object that may be converted to a string.

            -   **options** ([*ConsoleOptions*](#rich.console.ConsoleOptions "rich.console.ConsoleOptions")*,* *optional*) -- An options object, or None to use self.options. Defaults to None.

        Returns[:]

        :   An iterable of segments that may be rendered.

        Return type[:]

        :   Iterable\[[Segment](segment.html#rich.segment.Segment "rich.segment.Segment")\]

    [[render_lines]][(]*[[renderable]]*, *[[options]][[=]][[None]]*, *[[\*]]*, *[[style]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.render_lines)[](#rich.console.Console.render_lines "Link to this definition")

    :   Render objects in to a list of lines.

        > <div>
        >
        > The output of render_lines is useful when further formatting of rendered console text is required, such as the Panel class which draws a border around any renderable object.
        >
        > Args:
        >
        > :   renderable (RenderableType): Any object renderable in the console. options (Optional\[ConsoleOptions\], optional): Console options, or None to use self.options. Default to [`None`]. style (Style, optional): Optional style to apply to renderables. Defaults to [`None`]. pad (bool, optional): Pad lines shorter than render width. Defaults to [`True`]. new_lines (bool, optional): Include "
        >
        > </div>

        " characters at end of lines.

        > <div>
        >
        > Returns:
        >
        > :   List\[List\[Segment\]\]: A list of lines, where a line is a list of Segment objects.
        >
        > </div>

        Parameters[:]

        :   -   **renderable** ([*ConsoleRenderable*](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") *\|* [*RichCast*](#rich.console.RichCast "rich.console.RichCast") *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

            -   **options** ([*ConsoleOptions*](#rich.console.ConsoleOptions "rich.console.ConsoleOptions") *\|* *None*)

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

            -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](segment.html#rich.segment.Segment "rich.segment.Segment")\]\]

    [[render_str]][(]*[[text]]*, *[[\*]]*, *[[style]][[=]][[\'\']]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[emoji]][[=]][[None]]*, *[[markup]][[=]][[None]]*, *[[highlight]][[=]][[None]]*, *[[highlighter]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.render_str)[](#rich.console.Console.render_str "Link to this definition")

    :   Convert a string to a Text instance. This is called automatically if you print or log a string.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Text to render.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style to apply to rendered text.

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "default", "left", "center", "full", or "right". Defaults to [`None`].

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", or "ellipsis". Defaults to [`None`].

            -   **emoji** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable emoji, or [`None`] to use Console default.

            -   **markup** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable markup, or [`None`] to use Console default.

            -   **highlight** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable highlighting, or [`None`] to use Console default.

            -   **highlighter** (*HighlighterType,* *optional*) -- Optional highlighter to apply.

        Returns[:]

        :   Renderable object.

        Return type[:]

        :   [ConsoleRenderable](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")

    [[rule]][(]*[[title]][[=]][[\'\']]*, *[[\*]]*, *[[characters]][[=]][[\'─\']]*, *[[style]][[=]][[\'rule.line\']]*, *[[align]][[=]][[\'center\']]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.rule)[](#rich.console.Console.rule "Link to this definition")

    :   Draw a line with optional centered title.

        Parameters[:]

        :   -   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Text to render over the rule. Defaults to "".

            -   **characters** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character(s) to form the line. Defaults to "─".

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Style of line. Defaults to "rule.line".

            -   **align** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- How to align the title, one of "left", "center", or "right". Defaults to "center".

        Return type[:]

        :   None

    [[save_html]][(]*[[path]]*, *[[\*]]*, *[[theme]][[=]][[None]]*, *[[clear]][[=]][[True]]*, *[[code_format]][[=]][[\'\<!DOCTYPE] [html\>\\n\<html\>\\n\<head\>\\n\<meta] [charset=\"UTF-8\"\>\\n\<style\>\\n\\nbody] [    [color:] [;\\n]    [background-color:] [;\\n}}\\n\</style\>\\n\</head\>\\n\<body\>\\n]    [\<pre] [style=\"font-family:Menlo,\\\'DejaVu] [Sans] [Mono\\\',consolas,\\\'Courier] [New\\\',monospace\"\>\<code] [style=\"font-family:inherit\"\>\</code\>\</pre\>\\n\</body\>\\n\</html\>\\n\']]*, *[[inline_styles]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.save_html)[](#rich.console.Console.save_html "Link to this definition")

    :   Generate HTML from console contents and write to a file (requires record=True argument in constructor).

        Parameters[:]

        :   -   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Path to write html file.

            -   **theme** (*TerminalTheme,* *optional*) -- TerminalTheme object containing console colors.

            -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`].

            -   **code_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format string to render HTML. In addition to '', '', and '', should contain '' if inline_styles is [`False`].

            -   **inline_styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- If [`True`] styles will be inlined in to spans, which makes files larger but easier to cut and paste markup. If [`False`], styles will be embedded in a style tag. Defaults to False.

        Return type[:]

        :   None

    [[save_svg]][(]*[[path]]*, *[[\*]]*, *[[title]][[=]][[\'Rich\']]*, *[[theme]][[=]][[None]]*, *[[clear]][[=]][[True]]*, *[[code_format]][[=]][[\'\<svg] [class=\"rich-terminal\"] [viewBox=\"0] [0] [] [\"] [xmlns=\"http://www.w3.org/2000/svg\"\>\\n]    [\<!\--] [Generated] [with] [Rich] [https://www.textualize.io] [\--\>\\n]    [\<style\>\\n\\n]    [\@font-face] [        [font-family:] [\"Fira] [Code\";\\n]        [src:] [local(\"FiraCode-Regular\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Regular.woff2\")] [format(\"woff2\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Regular.woff\")] [format(\"woff\");\\n]        [font-style:] [normal;\\n]        [font-weight:] [400;\\n]    [}}\\n]    [\@font-face] [        [font-family:] [\"Fira] [Code\";\\n]        [src:] [local(\"FiraCode-Bold\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Bold.woff2\")] [format(\"woff2\"),\\n]                [url(\"https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Bold.woff\")] [format(\"woff\");\\n]        [font-style:] [bold;\\n]        [font-weight:] [700;\\n]    [}}\\n\\n]    [.-matrix] [        [font-family:] [Fira] [Code,] [monospace;\\n]        [font-size:] [px;\\n]        [line-height:] [px;\\n]        [font-variant-east-asian:] [full-width;\\n]    [}}\\n\\n]    [.-title] [        [font-size:] [18px;\\n]        [font-weight:] [bold;\\n]        [font-family:] [arial;\\n]    [}}\\n\\n]    [\\n]    [\</style\>\\n\\n]    [\<defs\>\\n]    [\<clipPath] [id=\"-clip-terminal\"\>\\n]      [\<rect] [x=\"0\"] [y=\"0\"] [width=\"\"] [height=\"\"] [/\>\\n]    [\</clipPath\>\\n]    [\\n]    [\</defs\>\\n\\n]    [\\n]    [\<g] [transform=\"translate(,] [)\"] [clip-path=\"url(#-clip-terminal)\"\>\\n]    [\\n]    [\<g] [class=\"-matrix\"\>\\n]    [\\n]    [\</g\>\\n]    [\</g\>\\n\</svg\>\\n\']]*, *[[font_aspect_ratio]][[=]][[0.61]]*, *[[unique_id]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.save_svg)[](#rich.console.Console.save_svg "Link to this definition")

    :   Generate an SVG file from the console contents (requires record=True in Console constructor).

        Parameters[:]

        :   -   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The path to write the SVG to.

            -   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The title of the tab in the output image

            -   **theme** (*TerminalTheme,* *optional*) -- The [`TerminalTheme`] object to use to style the terminal

            -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`]

            -   **code_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Format string used to generate the SVG. Rich will inject a number of variables into the string in order to form the final SVG output. The default template used and the variables injected by Rich can be found by inspecting the [`console.CONSOLE_SVG_FORMAT`] variable.

            -   **font_aspect_ratio** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- The width to height ratio of the font used in the [`code_format`] string. Defaults to 0.61, which is the width to height ratio of Fira Code (the default font). If you aren't specifying a different font inside [`code_format`], you probably don't need this.

            -   **unique_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- unique id that is used as the prefix for various elements (CSS styles, node ids). If not set, this defaults to a computed value based on the recorded content.

        Return type[:]

        :   None

    [[save_text]][(]*[[path]]*, *[[\*]]*, *[[clear]][[=]][[True]]*, *[[styles]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.save_text)[](#rich.console.Console.save_text "Link to this definition")

    :   Generate text from console and save to a given location (requires record=True argument in constructor).

        Parameters[:]

        :   -   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Path to write text files.

            -   **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Clear record buffer after exporting. Defaults to [`True`].

            -   **styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- If [`True`], ansi style codes will be included. [`False`] for plain text. Defaults to [`False`].

        Return type[:]

        :   None

    [[screen]][(]*[[hide_cursor]][[=]][[True]]*, *[[style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.screen)[](#rich.console.Console.screen "Link to this definition")

    :   Context manager to enable and disable 'alternative screen' mode.

        Parameters[:]

        :   -   **hide_cursor** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also hide the cursor. Defaults to False.

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style")*,* *optional*) -- Optional style for screen. Defaults to None.

        Returns[:]

        :   Context which enables alternate screen on enter, and disables it on exit.

        Return type[:]

        :   \~ScreenContext

    [[set_alt_screen]][(]*[[enable]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.set_alt_screen)[](#rich.console.Console.set_alt_screen "Link to this definition")

    :   Enables alternative screen mode.

        Note, if you enable this mode, you should ensure that is disabled before the application exits. See [`screen()`] for a context manager that handles this for you.

        Parameters[:]

        :   **enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable (True) or disable (False) alternate screen. Defaults to True.

        Returns[:]

        :   True if the control codes were written.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[set_live]][(]*[[live]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.set_live)[](#rich.console.Console.set_live "Link to this definition")

    :   Set Live instance. Used by Live context manager (no need to call directly).

        Parameters[:]

        :   **live** ([*Live*](live.html#rich.live.Live "rich.live.Live")) -- Live instance using this Console.

        Returns[:]

        :   Boolean that indicates if the live is the topmost of the stack.

        Raises[:]

        :   **errors.LiveError** -- If this Console has a Live context currently active.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[set_window_title]][(]*[[title]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.set_window_title)[](#rich.console.Console.set_window_title "Link to this definition")

    :   Set the title of the console terminal window.

        Warning: There is no means within Rich of "resetting" the window title to its previous value, meaning the title you set will persist even after your application exits.

        [`fish`] shell resets the window title before and after each command by default, negating this issue. Windows Terminal and command prompt will also reset the title for you. Most other shells and terminals, however, do not do this.

        Some terminals may require configuration changes before you can set the title. Some terminals may not support setting the title at all.

        Other software (including the terminal itself, the shell, custom prompts, plugins, etc.) may also set the terminal window title. This could result in whatever value you write using this method being overwritten.

        Parameters[:]

        :   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The new title of the terminal window.

        Returns[:]

        :   

            True if the control code to change the terminal title was

            :   written, otherwise False. Note that a return value of True does not guarantee that the window title has actually changed, since the feature may be unsupported/disabled in some terminals.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[show_cursor]][(]*[[show]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.show_cursor)[](#rich.console.Console.show_cursor "Link to this definition")

    :   Show or hide the cursor.

        Parameters[:]

        :   **show** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Set visibility of the cursor.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    *[[property]][ ]*[[size]]*[[:]][ ][[ConsoleDimensions]](#rich.console.ConsoleDimensions "rich.console.ConsoleDimensions")*[](#rich.console.Console.size "Link to this definition")

    :   Get the size of the console.

        Returns[:]

        :   A named tuple containing the dimensions.

        Return type[:]

        :   [ConsoleDimensions](#rich.console.ConsoleDimensions "rich.console.ConsoleDimensions")

    [[status]][(]*[[status]]*, *[[\*]]*, *[[spinner]][[=]][[\'dots\']]*, *[[spinner_style]][[=]][[\'status.spinner\']]*, *[[speed]][[=]][[1.0]]*, *[[refresh_per_second]][[=]][[12.5]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.status)[](#rich.console.Console.status "Link to this definition")

    :   Display a status and spinner.

        Parameters[:]

        :   -   **status** (*RenderableType*) -- A status renderable (str or Text typically).

            -   **spinner** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Name of spinner animation (see python -m rich.spinner). Defaults to "dots".

            -   **spinner_style** (*StyleType,* *optional*) -- Style of spinner. Defaults to "status.spinner".

            -   **speed** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Speed factor for spinner animation. Defaults to 1.0.

            -   **refresh_per_second** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*,* *optional*) -- Number of refreshes per second. Defaults to 12.5.

        Returns[:]

        :   A Status object that may be used as a context manager.

        Return type[:]

        :   [Status](status.html#rich.status.Status "rich.status.Status")

    [[update_screen]][(]*[[renderable]]*, *[[\*]]*, *[[region]][[=]][[None]]*, *[[options]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.update_screen)[](#rich.console.Console.update_screen "Link to this definition")

    :   Update the screen at a given offset.

        Parameters[:]

        :   -   **renderable** (*RenderableType*) -- A Rich renderable.

            -   **region** (*Region,* *optional*) -- Region of screen to update, or None for entire screen. Defaults to None.

            -   **x** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- x offset. Defaults to 0.

            -   **y** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- y offset. Defaults to 0.

            -   **options** ([*ConsoleOptions*](#rich.console.ConsoleOptions "rich.console.ConsoleOptions") *\|* *None*)

        Raises[:]

        :   **errors.NoAltScreen** -- If the Console isn't in alt screen mode.

        Return type[:]

        :   None

    [[update_screen_lines]][(]*[[lines]]*, *[[x]][[=]][[0]]*, *[[y]][[=]][[0]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.update_screen_lines)[](#rich.console.Console.update_screen_lines "Link to this definition")

    :   Update lines of the screen at a given offset.

        Parameters[:]

        :   -   **lines** (*List\[List\[*[*Segment*](segment.html#rich.segment.Segment "rich.segment.Segment")*\]\]*) -- Rendered lines (as produced by [`render_lines()`]).

            -   **x** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- x offset (column no). Defaults to 0.

            -   **y** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- y offset (column no). Defaults to 0.

        Raises[:]

        :   **errors.NoAltScreen** -- If the Console isn't in alt screen mode.

        Return type[:]

        :   None

    [[use_theme]][(]*[[theme]]*, *[[\*]]*, *[[inherit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Console.use_theme)[](#rich.console.Console.use_theme "Link to this definition")

    :   Use a different theme for the duration of the context manager.

        Parameters[:]

        :   -   **theme** ([*Theme*](theme.html#rich.theme.Theme "rich.theme.Theme")) -- Theme instance to user.

            -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Inherit existing console styles. Defaults to True.

        Returns[:]

        :   \[description\]

        Return type[:]

        :   [ThemeContext](#rich.console.ThemeContext "rich.console.ThemeContext")

    *[[property]][ ]*[[width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.Console.width "Link to this definition")

    :   Get the width of the console.

        Returns[:]

        :   The width (in characters) of the console.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ConsoleDimensions]][(]*[[width]]*, *[[height]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleDimensions)[](#rich.console.ConsoleDimensions "Link to this definition")

:   Size of the terminal.

    Parameters[:]

    :   -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

    [[height]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.ConsoleDimensions.height "Link to this definition")

    :   The height of the console in lines.

    [[width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.ConsoleDimensions.width "Link to this definition")

    :   The width of the console in 'cells'.

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ConsoleOptions]][(]*[[size]]*, *[[legacy_windows]]*, *[[min_width]]*, *[[max_width]]*, *[[is_terminal]]*, *[[encoding]]*, *[[max_height]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[False]]*, *[[highlight]][[=]][[None]]*, *[[markup]][[=]][[None]]*, *[[height]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions)[](#rich.console.ConsoleOptions "Link to this definition")

:   Options for \_\_rich_console\_\_ method.

    Parameters[:]

    :   -   **size** ([*ConsoleDimensions*](#rich.console.ConsoleDimensions "rich.console.ConsoleDimensions"))

        -   **legacy_windows** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **min_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **is_terminal** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **max_height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **justify** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'default\',* *\'left\',* *\'center\',* *\'right\',* *\'full\'\]* *\|* *None*)

        -   **overflow** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'fold\',* *\'crop\',* *\'ellipsis\',* *\'ignore\'\]* *\|* *None*)

        -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None*)

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None*)

        -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None*)

        -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

    *[[property]][ ]*[[ascii_only]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.ConsoleOptions.ascii_only "Link to this definition")

    :   Check if renderables should use ascii only.

    [[copy]][(][)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.copy)[](#rich.console.ConsoleOptions.copy "Link to this definition")

    :   Return a copy of the options.

        Returns[:]

        :   a copy of self.

        Return type[:]

        :   [ConsoleOptions](#rich.console.ConsoleOptions "rich.console.ConsoleOptions")

    [[encoding]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.console.ConsoleOptions.encoding "Link to this definition")

    :   Encoding of terminal.

    [[highlight]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.console.ConsoleOptions.highlight "Link to this definition")

    :   Highlight override for render_str.

    [[is_terminal]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.ConsoleOptions.is_terminal "Link to this definition")

    :   True if the target is a terminal, otherwise False.

    [[justify]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'default\']][[,]][ ][[\'left\']][[,]][ ][[\'center\']][[,]][ ][[\'right\']][[,]][ ][[\'full\']][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.console.ConsoleOptions.justify "Link to this definition")

    :   Justify value override for renderable.

    [[legacy_windows]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.console.ConsoleOptions.legacy_windows "Link to this definition")

    :   flag for legacy windows.

        Type[:]

        :   legacy_windows

    [[markup]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.console.ConsoleOptions.markup "Link to this definition")

    :   Enable markup when rendering strings.

    [[max_height]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.ConsoleOptions.max_height "Link to this definition")

    :   Height of container (starts as terminal)

    [[max_width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.ConsoleOptions.max_width "Link to this definition")

    :   Maximum width of renderable.

    [[min_width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.console.ConsoleOptions.min_width "Link to this definition")

    :   Minimum width of renderable.

    [[no_wrap]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][False]*[](#rich.console.ConsoleOptions.no_wrap "Link to this definition")

    :   Disable wrapping for text.

    [[overflow]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[[\[]][[\'fold\']][[,]][ ][[\'crop\']][[,]][ ][[\'ellipsis\']][[,]][ ][[\'ignore\']][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.console.ConsoleOptions.overflow "Link to this definition")

    :   Overflow value override for renderable.

    [[reset_height]][(][)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.reset_height)[](#rich.console.ConsoleOptions.reset_height "Link to this definition")

    :   Return a copy of the options with height set to [`None`].

        Returns[:]

        :   New console options instance.

        Return type[:]

        :   \~ConsoleOptions

    [[size]]*[[:]][ ][[ConsoleDimensions]](#rich.console.ConsoleDimensions "rich.console.ConsoleDimensions")*[](#rich.console.ConsoleOptions.size "Link to this definition")

    :   Size of console.

    [[update]][(]*[[\*]]*, *[[width=\<rich.console.NoChange] [object\>]]*, *[[min_width=\<rich.console.NoChange] [object\>]]*, *[[max_width=\<rich.console.NoChange] [object\>]]*, *[[justify=\<rich.console.NoChange] [object\>]]*, *[[overflow=\<rich.console.NoChange] [object\>]]*, *[[no_wrap=\<rich.console.NoChange] [object\>]]*, *[[highlight=\<rich.console.NoChange] [object\>]]*, *[[markup=\<rich.console.NoChange] [object\>]]*, *[[height=\<rich.console.NoChange] [object\>]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.update)[](#rich.console.ConsoleOptions.update "Link to this definition")

    :   Update values, return a copy.

        Parameters[:]

        :   -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *NoChange*)

            -   **min_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *NoChange*)

            -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *NoChange*)

            -   **justify** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'default\',* *\'left\',* *\'center\',* *\'right\',* *\'full\'\]* *\|* *None* *\|* *\~rich.console.NoChange*)

            -   **overflow** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'fold\',* *\'crop\',* *\'ellipsis\',* *\'ignore\'\]* *\|* *None* *\|* *\~rich.console.NoChange*)

            -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None* *\|* *NoChange*)

            -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None* *\|* *NoChange*)

            -   **markup** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") *\|* *None* *\|* *NoChange*)

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None* *\|* *NoChange*)

        Return type[:]

        :   [*ConsoleOptions*](#rich.console.ConsoleOptions "rich.console.ConsoleOptions")

    [[update_dimensions]][(]*[[width]]*, *[[height]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.update_dimensions)[](#rich.console.ConsoleOptions.update_dimensions "Link to this definition")

    :   Update the width and height, and return a copy.

        Parameters[:]

        :   -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- New width (sets both min_width and max_width).

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- New height.

        Returns[:]

        :   New console options instance.

        Return type[:]

        :   \~ConsoleOptions

    [[update_height]][(]*[[height]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.update_height)[](#rich.console.ConsoleOptions.update_height "Link to this definition")

    :   Update the height, and return a copy.

        Parameters[:]

        :   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- New height

        Returns[:]

        :   New Console options instance.

        Return type[:]

        :   \~ConsoleOptions

    [[update_width]][(]*[[width]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleOptions.update_width)[](#rich.console.ConsoleOptions.update_width "Link to this definition")

    :   Update just the width, return a copy.

        Parameters[:]

        :   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- New width (sets both min_width and max_width)

        Returns[:]

        :   New console options instance.

        Return type[:]

        :   \~ConsoleOptions

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ConsoleRenderable]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleRenderable)[](#rich.console.ConsoleRenderable "Link to this definition")

:   An object that supports the console protocol.

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ConsoleThreadLocals]][(]*[[theme_stack]]*, *[[buffer=\<factory\>]]*, *[[buffer_index=0]]*[)][[[\[source\]]]](../_modules/rich/console.html#ConsoleThreadLocals)[](#rich.console.ConsoleThreadLocals "Link to this definition")

:   Thread local values for Console context.

    Parameters[:]

    :   -   **theme_stack** (*ThemeStack*)

        -   **buffer** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](segment.html#rich.segment.Segment "rich.segment.Segment")*\]*)

        -   **buffer_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[Group]][(]*[[\*]][[renderables]]*, *[[fit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#Group)[](#rich.console.Group "Link to this definition")

:   Takes a group of renderables and returns a renderable object that renders the group.

    Parameters[:]

    :   -   **renderables** (*Iterable\[RenderableType\]*) -- An iterable of renderable objects.

        -   **fit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Fit dimension of group to contents, or fill available space. Defaults to True.

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[NewLine]][(]*[[count]][[=]][[1]]*[)][[[\[source\]]]](../_modules/rich/console.html#NewLine)[](#rich.console.NewLine "Link to this definition")

:   A renderable to generate new line(s)

    Parameters[:]

    :   **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[PagerContext]][(]*[[console]]*, *[[pager]][[=]][[None]]*, *[[styles]][[=]][[False]]*, *[[links]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/console.html#PagerContext)[](#rich.console.PagerContext "Link to this definition")

:   A context manager that 'pages' content. See [[`pager()`]](#rich.console.Console.pager "rich.console.Console.pager") for usage.

    Parameters[:]

    :   -   **console** ([*Console*](#rich.console.Console "rich.console.Console"))

        -   **pager** (*Pager* *\|* *None*)

        -   **styles** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **links** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[RenderHook]][[[\[source\]]]](../_modules/rich/console.html#RenderHook)[](#rich.console.RenderHook "Link to this definition")

:   Provides hooks in to the render process.

    *[[abstractmethod]][ ]*[[process_renderables]][(]*[[renderables]]*[)][[[\[source\]]]](../_modules/rich/console.html#RenderHook.process_renderables)[](#rich.console.RenderHook.process_renderables "Link to this definition")

    :   Called with a list of objects to render.

        This method can return a new list of renderables, or modify and return the same list.

        Parameters[:]

        :   **renderables** (*List\[*[*ConsoleRenderable*](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")*\]*) -- A number of renderable objects.

        Returns[:]

        :   A replacement list of renderables.

        Return type[:]

        :   List\[[ConsoleRenderable](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")\]

```
<!-- -->
```

[[rich.console.]][[RenderableType]][](#rich.console.RenderableType "Link to this definition")

:   A string or any object that may be rendered by Rich.

    alias of [[`ConsoleRenderable`]](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") \| [[`RichCast`]](#rich.console.RichCast "rich.console.RichCast") \| [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[RichCast]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/rich/console.html#RichCast)[](#rich.console.RichCast "Link to this definition")

:   An object that may be 'cast' to a console renderable.

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ScreenContext]][(]*[[console]]*, *[[hide_cursor]]*, *[[style]][[=]][[\'\']]*[)][[[\[source\]]]](../_modules/rich/console.html#ScreenContext)[](#rich.console.ScreenContext "Link to this definition")

:   A context manager that enables an alternative screen. See [[`screen()`]](#rich.console.Console.screen "rich.console.Console.screen") for usage.

    Parameters[:]

    :   -   **console** ([*Console*](#rich.console.Console "rich.console.Console"))

        -   **hide_cursor** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style"))

    [[update]][(]*[[\*]][[renderables]]*, *[[style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/console.html#ScreenContext.update)[](#rich.console.ScreenContext.update "Link to this definition")

    :   Update the screen.

        Parameters[:]

        :   -   **renderable** (*RenderableType,* *optional*) -- Optional renderable to replace current renderable, or None for no change. Defaults to None.

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*) -- (Style, optional): Replacement style, or None for no change. Defaults to None.

            -   **renderables** ([*ConsoleRenderable*](#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable") *\|* [*RichCast*](#rich.console.RichCast "rich.console.RichCast") *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ScreenUpdate]][(]*[[lines]]*, *[[x]]*, *[[y]]*[)][[[\[source\]]]](../_modules/rich/console.html#ScreenUpdate)[](#rich.console.ScreenUpdate "Link to this definition")

:   Render a list of lines at a given offset.

    Parameters[:]

    :   -   **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](segment.html#rich.segment.Segment "rich.segment.Segment")*\]\]*)

        -   **x** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **y** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

```
<!-- -->
```

*[[class]][ ]*[[rich.console.]][[ThemeContext]][(]*[[console]]*, *[[theme]]*, *[[inherit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#ThemeContext)[](#rich.console.ThemeContext "Link to this definition")

:   A context manager to use a temporary theme. See [[`use_theme()`]](#rich.console.Console.use_theme "rich.console.Console.use_theme") for usage.

    Parameters[:]

    :   -   **console** ([*Console*](#rich.console.Console "rich.console.Console"))

        -   **theme** ([*Theme*](theme.html#rich.theme.Theme "rich.theme.Theme"))

        -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

```
<!-- -->
```

[[rich.console.]][[detect_legacy_windows]][(][)][[[\[source\]]]](../_modules/rich/console.html#detect_legacy_windows)[](#rich.console.detect_legacy_windows "Link to this definition")

:   Detect legacy Windows.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

[[rich.console.]][[group]][(]*[[fit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/console.html#group)[](#rich.console.group "Link to this definition")

:   A decorator that turns an iterable of renderables in to a group.

    Parameters[:]

    :   **fit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Fit dimension of group to contents, or fill available space. Defaults to True.

    Return type[:]

    :   [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")\[\[...\], [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")\[\[...\], [*Group*](#rich.console.Group "rich.console.Group")\]\]

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).