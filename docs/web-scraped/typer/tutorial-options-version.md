# Source: https://typer.tiangolo.com/tutorial/options/version/

# Version CLI Option, `is_eager`[¶](#version-cli-option-is_eager "Permanent link")

You could use a callback to implement a `--version` *CLI option*.

It would show the version of your CLI program and then it would terminate it. Even before any other *CLI parameter* is processed.

## First version of `--version`[¶](#first-version-of-version "Permanent link") 

Let\'s see a first version of how it could look like:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    @app.command()
    def main(
        name: str = typer.Option("World"),
        version: bool | None = typer.Option(None, "--version", callback=version_callback),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    @app.command()
    def main(
        name: str = typer.Option("World"),
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Tip

Notice that we don\'t have to get the `typer.Context` and check for `ctx.resilient_parsing` for completion to work, because we only print and modify the program when `--version` is passed, otherwise, nothing is printed or changed from the callback.

If the `--version` *CLI option* is passed, we get a value `True` in the callback.

Then we can print the version and raise `typer.Exit()` to make sure the program is terminated before anything else is executed.

We also declare the explicit *CLI option* name `--version`, because we don\'t want an automatic `--no-version`, it would look awkward.

Check it:

    $ python main.py --help

    // We get a --version, and don't get an awkward --no-version 🎉
    Usage: main.py [OPTIONS]

    Options:
      --version
      --name TEXT
      --help                Show this message and exit.

    // We can call it normally
    $ python main.py --name Camila

    Hello Camila

    // And we can get the version
    $ python main.py --version

    Awesome CLI Version: 0.1.0

    // Because we exit in the callback, we don't get a "Hello World" message after the version 🚀

## Previous parameters and `is_eager`[¶](#previous-parameters-and-is_eager "Permanent link")

But now let\'s say that the `--name` *CLI option* that we declared before `--version` is required, and it has a callback that could exit the program:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    def name_callback(name: str):
        if name != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return name

    @app.command()
    def main(
        name: str = typer.Option(..., callback=name_callback),
        version: bool | None = typer.Option(None, "--version", callback=version_callback),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    def name_callback(name: str):
        if name != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return name

    @app.command()
    def main(
        name: str = typer.Option(..., callback=name_callback),
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Then our CLI program could not work as expected in some cases as it is *right now*, because if we use `--version` after `--name` then the callback for `--name` will be processed before and we can get its error:

    $ python main.py --name Rick --version

    Only Camila is allowed
    Aborted!

Tip

We don\'t have to check for `ctx.resilient_parsing` in the `name_callback()` for completion to work, because we are not using `typer.echo()`, instead we are raising a `typer.BadParameter`.

Technical Details

`typer.BadParameter` prints the error to \"standard error\", not to \"standard output\", and because the completion system only reads from \"standard output\", it won\'t break completion.

Info

If you need a refresher about what is \"standard output\" and \"standard error\" check the section in [Printing and Colors: \"Standard Output\" and \"Standard Error\"](../../printing/#standard-output-and-standard-error).

### Fix with `is_eager`[¶](#fix-with-is_eager "Permanent link")

For those cases, we can mark a *CLI parameter* (a *CLI option* or *CLI argument*) with `is_eager=True`.

That will tell **Typer** (actually Click) that it should process this *CLI parameter* before the others:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    def name_callback(name: str):
        if name != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return name

    @app.command()
    def main(
        name: str = typer.Option(..., callback=name_callback),
        version: bool | None = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    __version__ = "0.1.0"

    app = typer.Typer()

    def version_callback(value: bool):
        if value:
            print(f"Awesome CLI Version: ")
            raise typer.Exit()

    def name_callback(name: str):
        if name != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return name

    @app.command()
    def main(
        name: str = typer.Option(..., callback=name_callback),
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Check it:

    $ python main.py --name Rick --version

    // Now we only get the version, and the name is not used
    Awesome CLI Version: 0.1.0