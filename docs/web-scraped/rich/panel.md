# Source: https://rich.readthedocs.io/en/latest/panel.html

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
-   [Panel](#)
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

# Panel[](#panel "Link to this heading")

To draw a border around text or other renderable, construct a [[`Panel`]](reference/panel.html#rich.panel.Panel "rich.panel.Panel") with the renderable as the first positional argument. Here's an example:

    from rich import print
    from rich.panel import Panel
    print(Panel("Hello, [red]World!"))

You can change the style of the panel by setting the [`box`] argument to the Panel constructor. See [[Box]](appendix/box.html#appendix-box) for a list of available box styles.

Panels will extend to the full width of the terminal. You can make panel *fit* the content by setting [`expand=False`] on the constructor, or by creating the Panel with [[`fit()`]](reference/panel.html#rich.panel.Panel.fit "rich.panel.Panel.fit"). For example:

    from rich import print
    from rich.panel import Panel
    print(Panel.fit("Hello, [red]World!"))

The Panel constructor accepts a [`title`] argument which will draw a title on the top of the panel, as well as a [`subtitle`] argument which will draw a subtitle on the bottom of the panel:

    from rich import print
    from rich.panel import Panel
    print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

See [[`Panel`]](reference/panel.html#rich.panel.Panel "rich.panel.Panel") for details how to customize Panels.

[[] Previous](padding.html "Padding") [Next []](progress.html "Progress Display")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).