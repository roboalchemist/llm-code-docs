# Source: https://typer.tiangolo.com/tutorial/multiple-values/multiple-options/

# Multiple CLI Options[¶](#multiple-cli-options "Permanent link")

You can declare a *CLI option* that can be used multiple times, and then get all the values.

For example, let\'s say you want to accept several users in a single execution.

For this, use the standard Python `list` to declare it as a list of `str`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(user: list[str] | None = typer.Option(None)):
        if not user:
            print(f"No provided users (raw input = )")
            raise typer.Abort()
        for u in user:
            print(f"Processing user: ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    @app.command()
    def main(user: Optional[list[str]] = typer.Option(None)):
        if not user:
            print(f"No provided users (raw input = )")
            raise typer.Abort()
        for u in user:
            print(f"Processing user: ")

    if __name__ == "__main__":
        app()

You will receive the values as you declared them, as a `list` of `str`.

Check it:

    // The default value is 'None'
    $ python main.py

    No provided users (raw input = None)
    Aborted!

    // Now pass a user
    $ python main.py --user Camila

    Processing user: Camila

    // And now try with several users
    $ python main.py --user Camila --user Rick --user Morty

    Processing user: Camila
    Processing user: Rick
    Processing user: Morty

## Multiple `float`[¶](#multiple-float "Permanent link")

The same way, you can use other types and they will be converted by **Typer** to their declared type:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(number: list[float] = typer.Option([])):
        print(f"The sum is ")

    if __name__ == "__main__":
        app()

Check it:

    $ python main.py

    The sum is 0

    // Try with some numbers
    $ python main.py --number 2

    The sum is 2.0

    // Try with some numbers
    $ python main.py --number 2 --number 3 --number 4.5

    The sum is 9.5