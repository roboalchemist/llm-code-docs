# Source: https://rich.readthedocs.io/en/latest/appendix/box.html

[]

# Box[](#box "Link to this heading")

Rich has a number of constants that set the box characters used to draw tables and panels. To select a box style import one of the constants below from [`rich.box`]. For example:

    from rich import box
    table = Table(box=box.SQUARE)

Note

Some of the box drawing characters will not display correctly on Windows legacy terminal (cmd.exe) with *raster* fonts, and are disabled by default. If you want the full range of box options on Windows legacy terminal, use a *truetype* font and set the [`safe_box`] parameter on the Table class to [`False`].

The following table is generated with this command:

    python -m rich.box

![](../_images/box.svg)

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).