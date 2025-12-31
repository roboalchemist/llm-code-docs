# Source: https://typer.tiangolo.com/tutorial/parameter-types/number/

# Number[¶](#number "Permanent link")

You can define numeric validations with `max` and `min` values for `int` and `float` *CLI parameters*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        id: int = typer.Argument(..., min=0, max=1000),
        age: int = typer.Option(20, min=18),
        score: float = typer.Option(0, max=100),
    ):
        print(f"ID is ")
        print(f"--age is ")
        print(f"--score is ")

    if __name__ == "__main__":
        app()

*CLI arguments* and *CLI options* can both use these validations.

You can specify `min`, `max` or both.

Check it:

    $ python main.py --help

    // Notice the extra RANGE in the help text for --age and --score
    Usage: main.py [OPTIONS] ID

    Arguments:
      ID  [required]

    Options:
      --age INTEGER RANGE   [default: 20]
      --score FLOAT RANGE   [default: 0]
      --help                Show this message and exit.

    // Pass all the CLI parameters
    $ python main.py 5 --age 20 --score 90

    ID is 5
    --age is 20
    --score is 90.0

    // Pass an invalid ID
    $ python main.py 1002

    Usage: main.py [OPTIONS] ID
    Try "main.py --help" for help.

    Error: Invalid value for 'ID': 1002 is not in the range 0<=x<=1000.

    // Pass an invalid age
    $ python main.py 5 --age 15

    Usage: main.py [OPTIONS] ID
    Try "main.py --help" for help.

    Error: Invalid value for '--age': 15 is not in the range x>=18.

    // Pass an invalid score
    $ python main.py 5 --age 20 --score 100.5

    Usage: main.py [OPTIONS] ID
    Try "main.py --help" for help.

    Error: Invalid value for '--score': 100.5 is not in the range x<=100.

    // But as we didn't specify a minimum score, this is accepted
    $ python main.py 5 --age 20 --score -5

    ID is 5
    --age is 20
    --score is -5.0

## Clamping numbers[¶](#clamping-numbers "Permanent link")

You might want to, instead of showing an error, use the closest minimum or maximum valid values.

You can do it with the `clamp` parameter:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        id: int = typer.Argument(..., min=0, max=1000),
        rank: int = typer.Option(0, max=10, clamp=True),
        score: float = typer.Option(0, min=0, max=100, clamp=True),
    ):
        print(f"ID is ")
        print(f"--rank is ")
        print(f"--score is ")

    if __name__ == "__main__":
        app()

And then, when you pass data that is out of the valid range, it will be \"clamped\", the closest valid value will be used:

    // ID doesn't have clamp, so it shows an error
    $ python main.py 1002

    Usage: main.py [OPTIONS] ID
    Try "main.py --help" for help.

    Error: Invalid value for 'ID': 1002 is not in the range 0<=x<=1000.

    // But --rank and --score use clamp
    $ python main.py 5 --rank 11 --score -5

    ID is 5
    --rank is 10
    --score is 0

## Counter *CLI options*[¶](#counter-cli-options "Permanent link")

You can make a *CLI option* work as a counter with the `count` parameter:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(verbose: int = typer.Option(0, "--verbose", "-v", count=True)):
        print(f"Verbose level is ")

    if __name__ == "__main__":
        app()

It means that the *CLI option* will be like a boolean flag, e.g. `--verbose`.

And the value you receive in the function will be the amount of times that `--verbose` was added:

    // Check it
    $ python main.py

    Verbose level is 0

    // Now use one --verbose
    $ python main.py --verbose

    Verbose level is 1

    // Now 3 --verbose
    $ python main.py --verbose --verbose --verbose

    Verbose level is 3

    // And with the short name
    $ python main.py -v

    Verbose level is 1

    // And with the short name 3 times
    $ python main.py -v -v -v

    Verbose level is 3

    // As short names can be put together, this also works
    $ python main.py -vvv

    Verbose level is 3