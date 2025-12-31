# Source: https://rich.readthedocs.io/en/latest/reference/syntax.html

[]

# rich.syntax[](#module-rich.syntax "Link to this heading")

*[[class]][ ]*[[rich.syntax.]][[Syntax]][(]*[[code]]*, *[[lexer]]*, *[[\*]]*, *[[theme]][[=]][[\'monokai\']]*, *[[dedent]][[=]][[False]]*, *[[line_numbers]][[=]][[False]]*, *[[start_line]][[=]][[1]]*, *[[line_range]][[=]][[None]]*, *[[highlight_lines]][[=]][[None]]*, *[[code_width]][[=]][[None]]*, *[[tab_size]][[=]][[4]]*, *[[word_wrap]][[=]][[False]]*, *[[background_color]][[=]][[None]]*, *[[indent_guides]][[=]][[False]]*, *[[padding]][[=]][[0]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax)[](#rich.syntax.Syntax "Link to this definition")

:   Construct a Syntax object to render syntax highlighted code.

    Parameters[:]

    :   -   **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Code to highlight.

        -   **lexer** (*Lexer* *\|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Lexer to use (see [https://pygments.org/docs/lexers/](https://pygments.org/docs/lexers/))

        -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Color theme, aka Pygments style (see [https://pygments.org/docs/styles/#getting-a-list-of-available-styles](https://pygments.org/docs/styles/#getting-a-list-of-available-styles)). Defaults to "monokai".

        -   **dedent** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable stripping of initial whitespace. Defaults to False.

        -   **line_numbers** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable rendering of line numbers. Defaults to False.

        -   **start_line** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Starting number for line numbers. Defaults to 1.

        -   **line_range** (*Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None\],* *optional*) -- If given should be a tuple of the start and end line to render. A value of None in the tuple indicates the range is open in that direction.

        -   **highlight_lines** (*Set\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- A set of line numbers to highlight.

        -   **code_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- Width of code to render (not including line numbers), or [`None`] to use all available width.

        -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Size of tabs. Defaults to 4.

        -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping.

        -   **background_color** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional background color, or None to use theme color. Defaults to None.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show indent guides. Defaults to False.

        -   **padding** (*PaddingDimensions*) -- Padding to apply around the syntax. Defaults to 0 (no padding).

    *[[property]][ ]*[[default_lexer]]*[[:]][ ][Lexer]*[](#rich.syntax.Syntax.default_lexer "Link to this definition")

    :   A Pygments Lexer to use if one is not specified or invalid.

    *[[classmethod]][ ]*[[from_path]][(]*[[path]]*, *[[encoding]][[=]][[\'utf-8\']]*, *[[lexer]][[=]][[None]]*, *[[theme]][[=]][[\'monokai\']]*, *[[dedent]][[=]][[False]]*, *[[line_numbers]][[=]][[False]]*, *[[line_range]][[=]][[None]]*, *[[start_line]][[=]][[1]]*, *[[highlight_lines]][[=]][[None]]*, *[[code_width]][[=]][[None]]*, *[[tab_size]][[=]][[4]]*, *[[word_wrap]][[=]][[False]]*, *[[background_color]][[=]][[None]]*, *[[indent_guides]][[=]][[False]]*, *[[padding]][[=]][[0]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax.from_path)[](#rich.syntax.Syntax.from_path "Link to this definition")

    :   Construct a Syntax object from a file.

        Parameters[:]

        :   -   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Path to file to highlight.

            -   **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Encoding of file.

            -   **lexer** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *Lexer,* *optional*) -- Lexer to use. If None, lexer will be auto-detected from path/file content.

            -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Color theme, aka Pygments style (see [https://pygments.org/docs/styles/#getting-a-list-of-available-styles](https://pygments.org/docs/styles/#getting-a-list-of-available-styles)). Defaults to "emacs".

            -   **dedent** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable stripping of initial whitespace. Defaults to True.

            -   **line_numbers** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable rendering of line numbers. Defaults to False.

            -   **start_line** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Starting number for line numbers. Defaults to 1.

            -   **line_range** (*Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- If given should be a tuple of the start and end line to render.

            -   **highlight_lines** (*Set\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- A set of line numbers to highlight.

            -   **code_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*) -- Width of code to render (not including line numbers), or [`None`] to use all available width.

            -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Size of tabs. Defaults to 4.

            -   **word_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable word wrapping of code.

            -   **background_color** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional background color, or None to use theme color. Defaults to None.

            -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show indent guides. Defaults to False.

            -   **padding** (*PaddingDimensions*) -- Padding to apply around the syntax. Defaults to 0 (no padding).

        Returns[:]

        :   A Syntax object that may be printed to the console

        Return type[:]

        :   \[[Syntax](#rich.syntax.Syntax "rich.syntax.Syntax")\]

    *[[classmethod]][ ]*[[get_theme]][(]*[[name]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax.get_theme)[](#rich.syntax.Syntax.get_theme "Link to this definition")

    :   Get a syntax theme instance.

        Parameters[:]

        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *SyntaxTheme*)

        Return type[:]

        :   *SyntaxTheme*

    *[[classmethod]][ ]*[[guess_lexer]][(]*[[path]]*, *[[code]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax.guess_lexer)[](#rich.syntax.Syntax.guess_lexer "Link to this definition")

    :   Guess the alias of the Pygments lexer to use based on a path and an optional string of code. If code is supplied, it will use a combination of the code and the filename to determine the best lexer to use. For example, if the file is [`index.html`] and the file contains Django templating syntax, then "html+django" will be returned. If the file is [`index.html`], and no templating language is used, the "html" lexer will be used. If no string of code is supplied, the lexer will be chosen based on the file extension..

        Parameters[:]

        :   -   **path** (*AnyStr*) -- The path to the file containing the code you wish to know the lexer for.

            -   **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional string of code that will be used as a fallback if no lexer is found for the supplied path.

        Returns[:]

        :   The name of the Pygments lexer that best matches the supplied path/code.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[highlight]][(]*[[code]]*, *[[line_range]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax.highlight)[](#rich.syntax.Syntax.highlight "Link to this definition")

    :   Highlight code and return a Text instance.

        Parameters[:]

        :   -   **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Code to highlight.

            -   **line_range** (*Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Optional line range to highlight.

        Returns[:]

        :   A text instance containing highlighted syntax.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

    *[[property]][ ]*[[lexer]]*[[:]][ ][Lexer][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.syntax.Syntax.lexer "Link to this definition")

    :   The lexer for this syntax, or None if no lexer was found.

        Tries to find the lexer by name if a string was passed to the constructor.

    [[stylize_range]][(]*[[style]]*, *[[start]]*, *[[end]]*, *[[style_before]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/syntax.html#Syntax.stylize_range)[](#rich.syntax.Syntax.stylize_range "Link to this definition")

    :   Adds a custom style on a part of the code, that will be applied to the syntax display when it's rendered. Line numbers are 1-based, while column indexes are 0-based.

        Parameters[:]

        :   -   **style** (*StyleType*) -- The style to apply.

            -   **start** (*Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- The start of the range, in the form \[line number, column index\].

            -   **end** (*Tuple\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- The end of the range, in the form \[line number, column index\].

            -   **style_before** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- Apply the style before any existing styles.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).