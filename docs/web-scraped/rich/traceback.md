# Source: https://rich.readthedocs.io/en/latest/traceback.html

[Contents:]

-   [Introduction](introduction.html)
-   [Console API](console.html)
-   [Styles](style.html)
-   [Console Markup](markup.html)
-   [Rich Text](text.html)
-   [Highlighting](highlighting.html)
-   [Pretty Printing](pretty.html)
-   [Logging Handler](logging.html)
-   [Traceback](#)
    -   [Printing tracebacks](#printing-tracebacks)
    -   [Traceback Handler](#traceback-handler)
        -   [Automatic Traceback Handler](#automatic-traceback-handler)
    -   [Suppressing Frames](#suppressing-frames)
    -   [Max Frames](#max-frames)
-   [Prompt](prompt.html)
-   [Columns](columns.html)
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

# Traceback[](#traceback "Link to this heading")

Rich can render Python tracebacks with syntax highlighting and formatting. Rich tracebacks are easier to read and show more code than standard Python tracebacks.

To see an example of a Rich traceback, running the following command:

    python -m rich.traceback

## Printing tracebacks[](#printing-tracebacks "Link to this heading")

The [[`print_exception()`]](reference/console.html#rich.console.Console.print_exception "rich.console.Console.print_exception") method will print a traceback for the current exception being handled. Here's an example:

    from rich.console import Console
    console = Console()

    try:
        do_something()
    except Exception:
        console.print_exception(show_locals=True)

The [`show_locals=True`] parameter causes Rich to display the value of local variables for each frame of the traceback.

See [exception.py](https://github.com/willmcgugan/rich/blob/master/examples/exception.py) for a larger example.

## Traceback Handler[](#traceback-handler "Link to this heading")

Rich can be installed as the default traceback handler so that all uncaught exceptions will be rendered with highlighting. Here's how:

    from rich.traceback import install
    install(show_locals=True)

There are a few options to configure the traceback handler, see [[`install()`]](reference/traceback.html#rich.traceback.install "rich.traceback.install") for details.

### Automatic Traceback Handler[](#automatic-traceback-handler "Link to this heading")

In some cases you may want to have the traceback handler installed automatically without having to worry about importing the code in your module. You can do that by modifying the sitecustomize.py in your virtual environment. Typically it would be located in your virtual environment path, underneath the site-packages folder, something like this:

    ./.venv/lib/python3.9/site-packages/sitecustomize.py

In most cases this file will not exist. If it doesn't exist, you can create it by:

    $ touch .venv/lib/python3.9/site-packages/sitecustomize.py

Add the following code to the file:

    from rich.traceback import install
    install(show_locals=True)

At this point, the traceback will be installed for any code that is run within the virtual environment.

Note

If you plan on sharing your code, it is probably best to include the traceback install in your main entry point module.

## Suppressing Frames[](#suppressing-frames "Link to this heading")

If you are working with a framework (click, django etc), you may only be interested in seeing the code from your own application within the traceback. You can exclude framework code by setting the suppress argument on Traceback, install, Console.print_exception, and RichHandler, which should be a list of modules or str paths.

Here's how you would exclude [click](https://click.palletsprojects.com/en/8.0.x/) from Rich exceptions:

    import click
    from rich.traceback import install
    install(suppress=[click])

Suppressed frames will show the line and file only, without any code.

## Max Frames[](#max-frames "Link to this heading")

A recursion error can generate very large tracebacks that take a while to render and contain a lot of repetitive frames. Rich guards against this with a max_frames argument, which defaults to 100. If a traceback contains more than 100 frames then only the first 50, and last 50 will be shown. You can disable this feature by setting max_frames to 0.

Here's an example of printing a recursive error:

    from rich.console import Console

    def foo(n):
        return bar(n)

    def bar(n):
        return foo(n)

    console = Console()

    try:
        foo(1)
    except Exception:
        console.print_exception(max_frames=20)

[[] Previous](logging.html "Logging Handler") [Next []](prompt.html "Prompt")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).