# Source: https://rich.readthedocs.io/en/latest/columns.html

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

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).