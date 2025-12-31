# Source: https://typer.tiangolo.com/tutorial/arguments/envvar/

# CLI Arguments with Environment Variables[¶](#cli-arguments-with-environment-variables "Permanent link")

You can also configure a *CLI argument* to read a value from an environment variable if it is not provided in the command line as a *CLI argument*.

Tip

You can learn more about environment variables in the [Environment Variables](../../../environment-variables/) page.

To do that, use the `envvar` parameter for `typer.Argument()`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", envvar="AWESOME_NAME")):
        print(f"Hello Mr. ")

    if __name__ == "__main__":
        app()

In this case, the *CLI argument* `name` will have a default value of `"World"`, but will also read any value passed to the environment variable `AWESOME_NAME` if no value is provided in the command line:

    // Check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] [NAME]

    Arguments:
      [NAME]  [env var: AWESOME_NAME;default: World]

    Options:
      --help                Show this message and exit.

    // Call it without a CLI argument
    $ python main.py

    Hello Mr. World

    // Now pass a value for the CLI argument
    $ python main.py Czernobog

    Hello Mr. Czernobog

    // And now use the environment variable
    $ AWESOME_NAME=Wednesday python main.py

    Hello Mr. Wednesday

    // CLI arguments take precedence over env vars
    $ AWESOME_NAME=Wednesday python main.py Czernobog

    Hello Mr. Czernobog

## Multiple environment variables[¶](#multiple-environment-variables "Permanent link")

You are not restricted to a single environment variable, you can declare a list of environment variables that could be used to get a value if it was not passed in the command line:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
        print(f"Hello Mr. ")

    if __name__ == "__main__":
        app()

Check it:

    // Check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] [NAME]

    Arguments:
      [NAME]  [env var: AWESOME_NAME, GOD_NAME;default: World]

    Options:
      --help                Show this message and exit.

    // Try the first env var
    $ AWESOME_NAME=Wednesday python main.py

    Hello Mr. Wednesday

    // Try the second env var
    $ GOD_NAME=Anubis python main.py

    Hello Mr. Anubis

## Hide an env var from the help text[¶](#hide-an-env-var-from-the-help-text "Permanent link")

By default, environment variables used will be shown in the help text, but you can disable them with `show_envvar=False`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", envvar="AWESOME_NAME", show_envvar=False)):
        print(f"Hello Mr. ")

    if __name__ == "__main__":
        app()

Check it:

    //Check the help
    $ python main.py --help

    // It won't show the env var
    Usage: main.py [OPTIONS] [NAME]

    Arguments:
      [NAME]  [default: World]

    Options:
      --help                Show this message and exit.

    // But it will still be able to use it
    $ AWESOME_NAME=Wednesday python main.py

    Hello Mr. Wednesday

Technical Details

In Click applications the env vars are hidden by default. 🙈

In **Typer** these env vars are shown by default. 👀