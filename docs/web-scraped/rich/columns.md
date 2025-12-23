# Source: https://rich.readthedocs.io/en/latest/columns.html

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
-   [Columns](#)
-   [Render Groups](group.html)
-   [Markdown](markdown.html)
-   [Padding](padding.html)
-   [Panel](panel.html)
-   [Progress Display](progress.html)
-   [Syntax](syntax.html)
-   [Tables](tables.html)
-   [Tree](tree.html)
-   [Live Display](live.html)
-   [Layout](layout.html)
-   [Console Protocol](protocol.html)
-   [Reference](reference.html)
-   [Appendix](appendix.html)

[Rich](index.html)

# Columns[](#columns "Link to this heading")

Rich can render text or other Rich renderables in neat columns with the [[`Columns`]](reference/columns.html#rich.columns.Columns "rich.columns.Columns") class. To use, construct a Columns instance with an iterable of renderables and print it to the Console.

The following example is a very basic clone of the [`ls`] command in OSX / Linux to list directory contents:

    import os
    import sys

    from rich import print
    from rich.columns import Columns

    if len(sys.argv) < 2:
        print("Usage: python columns.py DIRECTORY")
    else:
        directory = os.listdir(sys.argv[1])
        columns = Columns(directory, equal=True, expand=True)
        print(columns)

See [columns.py](https://github.com/willmcgugan/rich/blob/master/examples/columns.py) for an example which outputs columns containing more than just text.

[[] Previous](prompt.html "Prompt") [Next []](group.html "Render Groups")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).