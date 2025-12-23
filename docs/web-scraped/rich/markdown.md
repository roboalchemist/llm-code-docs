# Source: https://rich.readthedocs.io/en/latest/markdown.html

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
-   [Markdown](#)
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

# Markdown[](#markdown "Link to this heading")

Rich can render Markdown to the console. To render markdown, construct a [[`Markdown`]](reference/markdown.html#rich.markdown.Markdown "rich.markdown.Markdown") object then print it to the console. Markdown is a great way of adding rich content to your command line applications. Here's an example of use:

    MARKDOWN = """
    # This is an h1

    Rich can do a pretty *decent* job of rendering markdown.

    1. This is a list item
    2. This is another list item
    """
    from rich.console import Console
    from rich.markdown import Markdown

    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

Note that code blocks are rendered with full syntax highlighting!

You can also use the Markdown class from the command line. The following example displays a readme in the terminal:

    python -m rich.markdown README.md

Run the following to see the full list of arguments for the markdown command:

    python -m rich.markdown -h

[[] Previous](group.html "Render Groups") [Next []](padding.html "Padding")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).