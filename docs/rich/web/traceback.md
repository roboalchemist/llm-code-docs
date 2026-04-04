# Source: https://rich.readthedocs.io/en/latest/traceback.html

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