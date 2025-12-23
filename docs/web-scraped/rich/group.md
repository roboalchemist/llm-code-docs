# Source: https://rich.readthedocs.io/en/latest/group.html

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
-   [Render Groups](#)
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

# Render Groups[](#render-groups "Link to this heading")

The [[`Group`]](reference/console.html#rich.console.Group "rich.console.Group") class allows you to group several renderables together so they may be rendered in a context where only a single renderable may be supplied. For instance, you might want to display several renderables within a [[`Panel`]](reference/panel.html#rich.panel.Panel "rich.panel.Panel").

To render two panels within a third panel, you would construct a Group with the *child* renderables as positional arguments then wrap the result in another Panel:

    from rich import print
    from rich.console import Group
    from rich.panel import Panel

    panel_group = Group(
        Panel("Hello", style="on blue"),
        Panel("World", style="on red"),
    )
    print(Panel(panel_group))

This pattern is nice when you know in advance what renderables will be in a group, but can get awkward if you have a larger number of renderables, especially if they are dynamic. Rich provides a [[`group()`]](reference/console.html#rich.console.group "rich.console.group") decorator to help with these situations. The decorator builds a group from an iterator of renderables. The following is the equivalent of the previous example using the decorator:

    from rich import print
    from rich.console import group
    from rich.panel import Panel

    @group()
    def get_panels():
        yield Panel("Hello", style="on blue")
        yield Panel("World", style="on red")

    print(Panel(get_panels()))

[[] Previous](columns.html "Columns") [Next []](markdown.html "Markdown")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).