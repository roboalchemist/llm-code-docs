# Source: https://typer.tiangolo.com/tutorial/options/required/

# Required CLI Options[¶](#required-cli-options "Permanent link")

We said before that *by default*:

-   *CLI options* are **optional**
-   *CLI arguments* are **required**

Well, that\'s how they work *by default*, and that\'s the convention in many CLI programs and systems.

But if you really want, you can change that.

To make a *CLI option* required, you can put `typer.Option()` inside of `Annotated` and leave the parameter without a default value.

Let\'s make `--lastname` a required *CLI option*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str, lastname: str = typer.Option()):
        print(f"Hello  ")

    if __name__ == "__main__":
        app()

The same way as with `typer.Argument()`, the old style of using the function parameter default value is also supported, in that case you would just not pass anything to the `default` parameter.

Python 3.9+ - non-Annotated

🤓 Other versions and variants

Python 3.9+

Or you can explicitly pass `...` to `typer.Option(default=...)`:

Python 3.9+

Info

If you hadn\'t seen that `...` before: it is a special single value, it is [part of Python and is called \"Ellipsis\"](https://docs.python.org/3/library/constants.html#Ellipsis).

That will tell **Typer** that it\'s still a *CLI option*, but it doesn\'t have a default value, and it\'s required.

Tip

Again, prefer to use the `Annotated` version if possible. That way your code will mean the same in standard Python and in **Typer**.

And test it:

    // Pass the NAME CLI argument
    $ python main.py Camila

    // We didn't pass the now required --lastname CLI option
    Usage: main.py [OPTIONS] NAME
    Try "main.py --help" for help.

    Error: Missing option '--lastname'.

    // Now update it to pass the required --lastname CLI option
    $ python main.py Camila --lastname Gutiérrez

    Hello Camila Gutiérrez

    // And if you check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] NAME

    Options:
      --lastname TEXT       [required]
      --help                Show this message and exit.

    // It now tells you that --lastname is required 🎉