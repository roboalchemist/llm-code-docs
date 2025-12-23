# Source: https://rich.readthedocs.io/en/latest/syntax.html

[Contents:]

-   [Introduction](introduction.html)
-   [Console API](console.html)
-   [Styles](style.html)
-   [Console Markup](markup.html)
-   [Rich Text](text.html)
-   [Highlighting](highlighting.html)
-   [Pretty Printing](pretty.html)
-   [Logging Handler](logging.html)
-   [Traceback](traceback.html)
-   [Prompt](prompt.html)
-   [Columns](columns.html)
-   [Render Groups](group.html)
-   [Markdown](markdown.html)
-   [Padding](padding.html)
-   [Panel](panel.html)
-   [Progress Display](progress.html)
-   [Syntax](#)
    -   [Line numbers](#line-numbers)
    -   [Theme](#theme)
    -   [Background color](#background-color)
    -   [Syntax CLI](#syntax-cli)
-   [Tables](tables.html)
-   [Tree](tree.html)
-   [Live Display](live.html)
-   [Layout](layout.html)
-   [Console Protocol](protocol.html)
-   [Reference](reference.html)
-   [Appendix](appendix.html)

[Rich](index.html)

# Syntax[](#syntax "Link to this heading")

Rich can syntax highlight various programming languages with line numbers.

To syntax highlight code, construct a [[`Syntax`]](reference/syntax.html#rich.syntax.Syntax "rich.syntax.Syntax") object and print it to the console. Here's an example:

    from rich.console import Console
    from rich.syntax import Syntax

    console = Console()
    with open("syntax.py", "rt") as code_file:
        syntax = Syntax(code_file.read(), "python")
    console.print(syntax)

You may also use the [[`from_path()`]](reference/syntax.html#rich.syntax.Syntax.from_path "rich.syntax.Syntax.from_path") alternative constructor which will load the code from disk and auto-detect the file type. The example above could be re-written as follows:

    from rich.console import Console
    from rich.syntax import Syntax

    console = Console()
    syntax = Syntax.from_path("syntax.py")
    console.print(syntax)

## Line numbers[](#line-numbers "Link to this heading")

If you set [`line_numbers=True`], Rich will render a column for line numbers:

    syntax = Syntax.from_path("syntax.py", line_numbers=True)

## Theme[](#theme "Link to this heading")

The Syntax constructor (and [[`from_path()`]](reference/syntax.html#rich.syntax.Syntax.from_path "rich.syntax.Syntax.from_path")) accept a [`theme`] attribute which should be the name of a [Pygments theme](https://pygments.org/demo/). It may also be one of the special case theme names "ansi_dark" or "ansi_light" which will use the color theme configured by the terminal.

## Background color[](#background-color "Link to this heading")

You can override the background color from the theme by supplying a [`background_color`] argument to the constructor. This should be a string in the same format a style definition accepts, e.g. "red", "#ff0000", "rgb(255,0,0)" etc. You may also set the special value "default" which will use the default background color set in the terminal.

## Syntax CLI[](#syntax-cli "Link to this heading")

You can use this class from the command line. Here's how you would syntax highlight a file called "syntax.py":

    python -m rich.syntax syntax.py

For the full list of arguments, run the following:

    python -m rich.syntax -h

[[] Previous](progress.html "Progress Display") [Next []](tables.html "Tables")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).