# Source: https://typer.tiangolo.com/tutorial/multiple-values/arguments-with-multiple-values/

# CLI Arguments with Multiple Values[¶](#cli-arguments-with-multiple-values "Permanent link")

*CLI arguments* can also receive multiple values.

You can define the type of a *CLI argument* using `list`.

Python 3.9+

And then you can pass it as many *CLI arguments* of that type as you want:

    $ python main.py ./index.md ./first-steps.md woohoo!

    This file exists: index.md
    woohoo!
    This file exists: first-steps.md
    woohoo!

Tip

We also declared a final *CLI argument* `celebration`, and it\'s correctly used even if we pass an arbitrary number of `files` first.

Info

A `list` can only be used in the last command (if there are subcommands), as this will take anything to the right and assume it\'s part of the expected *CLI arguments*.

## *CLI arguments* with tuples[¶](#cli-arguments-with-tuples "Permanent link")

If you want a specific number of values and types, you can use a tuple, and it can even have default values:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        names: tuple[str, str, str] = typer.Argument(
            ("Harry", "Hermione", "Ron"), help="Select 3 characters to play with"
        ),
    ):
        for name in names:
            print(f"Hello ")

    if __name__ == "__main__":
        app()

Check it:

    // Check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] [NAMES]...

    Arguments:
      [NAMES]...  Select 3 characters to play with  [default: Harry, Hermione, Ron]

    Options:
      --help                Show this message and exit.

    // Use it with its defaults
    $ python main.py

    Hello Harry
    Hello Hermione
    Hello Ron

    // If you pass an invalid number of arguments you will get an error
    $ python main.py Draco Hagrid

    Error: Argument 'names' takes 3 values

    // And if you pass the exact number of values it will work correctly
    $ python main.py Draco Hagrid Dobby

    Hello Draco
    Hello Hagrid
    Hello Dobby