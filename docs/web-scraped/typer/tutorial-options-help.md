# Source: https://typer.tiangolo.com/tutorial/options/help/

# CLI Options with Help[¶](#cli-options-with-help "Permanent link")

You already saw how to add a help text for *CLI arguments* with the `help` parameter.

Let\'s now do the same for *CLI options*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str,
        lastname: str = typer.Option("", help="Last name of person to greet."),
        formal: bool = typer.Option(False, help="Say hi formally."),
    ):
        """
        Say hi to NAME, optionally with a --lastname.

        If --formal is used, say hi very formally.
        """
        if formal:
            print(f"Good day Ms.  .")
        else:
            print(f"Hello  ")

    if __name__ == "__main__":
        app()

The same way as with `typer.Argument()`, we can put `typer.Option()` inside of `Annotated`.

We can then pass the `help` keyword parameter:

    lastname: Annotated[str, typer.Option(help="this option does this and that")] = ""

\...to create the help for that *CLI option*.

The same way as with `typer.Argument()`, **Typer** also supports the old style using the function parameter default value:

    lastname: str = typer.Option(default="", help="this option does this and that")

Copy that example from above to a file `main.py`.

Test it:

    $ python main.py --help

    Usage: main.py [OPTIONS] NAME

      Say hi to NAME, optionally with a --lastname.

      If --formal is used, say hi very formally.

    Arguments:
      NAME  [required]

    Options:
      --lastname TEXT         Last name of person to greet. [default: ]
      --formal / --no-formal  Say hi formally.  [default: False]
      --help                  Show this message and exit.

    // Now you have a help text for the --lastname and --formal CLI options 🎉

## *CLI Options* help panels[¶](#cli-options-help-panels "Permanent link")

The same as with *CLI arguments*, you can put the help for some *CLI options* in different panels to be shown with the `--help` option.

If you have installed Rich as described in the docs for [Printing and Colors](../../printing/), you can set the `rich_help_panel` parameter to the name of the panel you want for each *CLI option*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str,
        lastname: str = typer.Option("", help="Last name of person to greet."),
        formal: bool = typer.Option(
            False, help="Say hi formally.", rich_help_panel="Customization and Utils"
        ),
        debug: bool = typer.Option(
            False, help="Enable debugging.", rich_help_panel="Customization and Utils"
        ),
    ):
        """
        Say hi to NAME, optionally with a --lastname.

        If --formal is used, say hi very formally.
        """
        if formal:
            print(f"Good day Ms.  .")
        else:
            print(f"Hello  ")

    if __name__ == "__main__":
        app()

Now, when you check the `--help` option, you will see a default panel named \"`Options`\" for the *CLI options* that don\'t have a custom `rich_help_panel`.

And below you will see other panels for the *CLI options* that have a custom panel set in the `rich_help_panel` parameter:

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] NAME                                </b>
    <b>                                                                     </b>
     Say hi to NAME, optionally with a <font color="#A1EFE4"><b>--lastname</b></font>.
     If <font color="#6B9F98"><b>--formal</b></font><font color="#A5A5A1"> is used, say hi very formally.                          </font>

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    name      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>                   │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--lastname</b></font>                  <font color="#F4BF75"><b>TEXT</b></font>  Last name of person to greet.   │
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                      <font color="#F4BF75"><b>    </b></font>  Show this message and exit.     │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Customization and Utils ─────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--formal</b></font>    <font color="#AE81FF"><b>--no-formal</b></font>      Say hi formally.                     │
    <font color="#A5A5A1">│                              [default: no-formal]                 │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--debug</b></font>     <font color="#AE81FF"><b>--no-debug</b></font>       Enable debugging.                    │
    <font color="#A5A5A1">│                              [default: no-debug]                  │</font>
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

Here we have a custom *CLI options* panel named \"`Customization and Utils`\".

## Help with style using Rich[¶](#help-with-style-using-rich "Permanent link")

In a future section you will see how to use custom markup in the `help` for *CLI options* when reading about [Commands - Command Help](../../commands/help/#rich-markdown-and-markup).

If you are in a hurry you can jump there, but otherwise, it would be better to continue reading here and following the tutorial in order.

## Hide default from help[¶](#hide-default-from-help "Permanent link")

You can tell Typer to not show the default value in the help text with `show_default=False`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(fullname: str = typer.Option("Wade Wilson", show_default=False)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And it will no longer show the default value in the help text:

    $ python main.py

    Hello Wade Wilson

    // Show the help
    $ python main.py --help

    Usage: main.py [OPTIONS]

    Options:
      --fullname TEXT
      --help                Show this message and exit.

    // Notice there's no [default: Wade Wilson] 🔥

Technical Details

In Click applications the default values are hidden by default. 🙈

In **Typer** these default values are shown by default. 👀

## Custom default string[¶](#custom-default-string "Permanent link")

You can use the same `show_default` to pass a custom string (instead of a `bool`) to customize the default value to be shown in the help text:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        fullname: str = typer.Option(
            "Wade Wilson", show_default="Deadpoolio the amazing's name"
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And it will be used in the help text:

    $ python main.py

    Hello Wade Wilson

    // Show the help
    $ python main.py --help

    Usage: main.py [OPTIONS]

    Options:
      --fullname TEXT       [default: (Deadpoolio the amazing's name)]
      --help                Show this message and exit.

    // Notice how it shows "(Deadpoolio the amazing's name)" instead of the actual default of "Wade Wilson"