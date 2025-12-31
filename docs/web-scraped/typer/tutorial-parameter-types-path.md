# Source: https://typer.tiangolo.com/tutorial/parameter-types/path/

# Path[¶](#path "Permanent link")

You can declare a *CLI parameter* to be a standard Python [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#basic-use).

This is what you would do for directory paths, file paths, etc:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    from pathlib import Path

    import typer

    app = typer.Typer()

    @app.command()
    def main(config: Path | None = typer.Option(None)):
        if config is None:
            print("No config file")
            raise typer.Abort()
        if config.is_file():
            text = config.read_text()
            print(f"Config file contents: ")
        elif config.is_dir():
            print("Config is a directory, will use all its config files")
        elif not config.exists():
            print("The config doesn't exist")

    if __name__ == "__main__":
        app()

    from pathlib import Path
    from typing import Optional

    import typer

    app = typer.Typer()

    @app.command()
    def main(config: Optional[Path] = typer.Option(None)):
        if config is None:
            print("No config file")
            raise typer.Abort()
        if config.is_file():
            text = config.read_text()
            print(f"Config file contents: ")
        elif config.is_dir():
            print("Config is a directory, will use all its config files")
        elif not config.exists():
            print("The config doesn't exist")

    if __name__ == "__main__":
        app()

And again, as you receive a standard Python `Path` object the same as the type annotation, your editor will give you autocompletion for all its attributes and methods.

Check it:

    // No config
    $ python main.py

    No config file
    Aborted!

    // Pass a config that doesn't exist
    $ python main.py --config config.txt

    The config doesn't exist

    // Now create a quick config
    $ echo "some settings" > config.txt

    // And try again
    $ python main.py --config config.txt

    Config file contents: some settings

    // And with a directory
    $ python main.py --config ./

    Config is a directory, will use all its config files

## Path validations[¶](#path-validations "Permanent link")

You can perform several validations for `Path` *CLI parameters*:

-   `exists`: if set to true, the file or directory needs to exist for this value to be valid. If this is not required and a file does indeed not exist, then all further checks are silently skipped.
-   `file_okay`: controls if a file is a possible value.
-   `dir_okay`: controls if a directory is a possible value.
-   `writable`: if true, a writable check is performed.
-   `readable`: if true, a readable check is performed.
-   `resolve_path`: if this is true, then the path is fully resolved before the value is passed onwards. This means that it's absolute and symlinks are resolved.

Technical Details

It will not expand a tilde-prefix (something with `~`, like `~/Documents/`), as this is supposed to be done by the shell only.

Tip

All these parameters come directly from [Click](https://click.palletsprojects.com/en/7.x/parameters/#parameter-types).

For example:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    from pathlib import Path

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        config: Path = typer.Option(
            ...,
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ):
        text = config.read_text()
        print(f"Config file contents: ")

    if __name__ == "__main__":
        app()

Check it:

    $ python main.py --config config.txt

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: Invalid value for '--config': File 'config.txt' does not exist.

    // Now create a quick config
    $ echo "some settings" > config.txt

    // And try again
    $ python main.py --config config.txt

    Config file contents: some settings

    // And with a directory
    $ python main.py --config ./

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: Invalid value for '--config': File './' is a directory.

### Advanced `Path` configurations[¶](#advanced-path-configurations "Permanent link")

Advanced Details

You probably won\'t need these configurations at first, you may want to skip it.

They are used for more advanced use cases.

-   `allow_dash`: If this is set to True, a single dash to indicate standard streams is permitted.
-   `path_type`: optionally a string type that should be used to represent the path. The default is None which means the return value will be either bytes or unicode depending on what makes most sense given the input data Click deals with.