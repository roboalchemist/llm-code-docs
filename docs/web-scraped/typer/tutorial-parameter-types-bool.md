# Source: https://typer.tiangolo.com/tutorial/parameter-types/bool/

# Boolean CLI Options[¶](#boolean-cli-options "Permanent link")

We have seen some examples of *CLI options* with `bool`, and how **Typer** creates `--something` and `--no-something` automatically.

But we can customize those names.

## Only `--force`[¶](#only-force "Permanent link") 

Let\'s say that we want a `--force` *CLI option* only, we want to discard `--no-force`.

We can do that by specifying the exact name we want:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(force: bool = typer.Option(False, "--force")):
        if force:
            print("Forcing operation")
        else:
            print("Not forcing")

    if __name__ == "__main__":
        app()

Now there\'s only a `--force` *CLI option*:

    // Check the help
    $ python main.py --help

    // Notice there's only --force, we no longer have --no-force
    Usage: main.py [OPTIONS]

    Options:
      --force               [default: False]
      --help                Show this message and exit.

    // Try it:
    $ python main.py

    Not forcing

    // Now add --force
    $ python main.py --force

    Forcing operation

    // And --no-force no longer exists ⛔️
    $ python main.py --no-force

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: No such option: --no-force

## Alternative names[¶](#alternative-names "Permanent link")

Now let\'s imagine we have a *CLI option* `--accept`.

And we want to allow setting `--accept` or the contrary, but `--no-accept` looks ugly.

We might want to instead have `--accept` and `--reject`.

We can do that by passing a single `str` with the 2 names for the `bool` *CLI option* separated by `/`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(accept: bool | None = typer.Option(None, "--accept/--reject")):
        if accept is None:
            print("I don't know what you want yet")
        elif accept:
            print("Accepting!")
        else:
            print("Rejecting!")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    @app.command()
    def main(accept: Optional[bool] = typer.Option(None, "--accept/--reject")):
        if accept is None:
            print("I don't know what you want yet")
        elif accept:
            print("Accepting!")
        else:
            print("Rejecting!")

    if __name__ == "__main__":
        app()

Check it:

    // Check the help
    $ python main.py --help

    // Notice the --accept / --reject
    Usage: main.py [OPTIONS]

    Options:
      --accept / --reject
      --help                Show this message and exit.

    // Try it
    $ python main.py

    I don't know what you want yet

    // Now pass --accept
    $ python main.py --accept

    Accepting!

    // And --reject
    $ python main.py --reject

    Rejecting!

## Short names[¶](#short-names "Permanent link")

The same way, you can declare short versions of the names for these *CLI options*.

For example, let\'s say we want `-f` for `--force` and `-F` for `--no-force`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(force: bool = typer.Option(False, "--force/--no-force", "-f/-F")):
        if force:
            print("Forcing operation")
        else:
            print("Not forcing")

    if __name__ == "__main__":
        app()

Check it:

    // Check the help
    $ python main.py --help

    // Notice the -f, --force / -F, --no-force
    Usage: main.py [OPTIONS]

    Options:
      -f, --force / -F, --no-force  [default: False]
      --help                        Show this message and exit.

    // Try with the short name -f
    $ python main.py -f

    Forcing operation

    // Try with the short name -F
    $ python main.py -F

    Not forcing

## Only names for `False`[¶](#only-names-for-false "Permanent link")

If you want to (although it might not be a good idea), you can declare only *CLI option* names to set the `False` value.

To do that, use a space and a single `/` and pass the negative name after:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(in_prod: bool = typer.Option(True, " /--demo", " /-d")):
        if in_prod:
            print("Running in production")
        else:
            print("Running demo")

    if __name__ == "__main__":
        app()

Tip

Have in mind that it\'s a string with a preceding space and then a `/`.

So, it\'s `" /-S"` not `"/-S"`.

Check it:

    // Check the help
    $ python main.py --help

    // Notice the / -d, --demo
    Usage: main.py [OPTIONS]

    Options:
       / -d, --demo         [default: True]
      --help                Show this message and exit.

    // Try it
    $ python main.py

    Running in production

    // Now pass --demo
    $ python main.py --demo

    Running demo

    // And the short version
    $ python main.py -d

    Running demo