# Source: https://typer.tiangolo.com/tutorial/arguments/help/

# CLI Arguments with Help[¶](#cli-arguments-with-help "Permanent link")

In the *First Steps* section you saw how to add help for a CLI app/command by adding it to a function\'s docstring.

Here\'s how that last example looked like:

Python 3.9+

Now that you also know how to use `typer.Argument()`, let\'s use it to add documentation specific for a *CLI argument*.

## Add a `help` text for a *CLI argument*[¶](#add-a-help-text-for-a-cli-argument "Permanent link")

You can use the `help` parameter to add a help text for a *CLI argument*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument(..., help="The name of the user to greet")):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And it will be used in the automatic `--help` option:

    $ python main.py --help

    // Check the section with Arguments below 🚀
    Usage: main.py [OPTIONS] NAME

    Arguments:
      NAME  The name of the user to greet  [required]

    Options:
      --help                Show this message and exit.

## Combine help text and docstrings[¶](#combine-help-text-and-docstrings "Permanent link")

And of course, you can also combine that `help` with the docstring:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument(..., help="The name of the user to greet")):
        """
        Say hi to NAME very gently, like Dirk.
        """
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And the `--help` option will combine all the information:

    $ python main.py --help

    // Notice that we have the help text from the docstring and also the Arguments 📝
    Usage: main.py [OPTIONS] NAME

      Say hi to NAME very gently, like Dirk.

    Arguments:
      NAME  The name of the user to greet  [required]

    Options:
      --help                Show this message and exit.

## Help with defaults[¶](#help-with-defaults "Permanent link")

If you have a *CLI argument* with a default value, like `"World"`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", help="Who to greet")):
        """
        Say hi to NAME very gently, like Dirk.
        """
        print(f"Hello ")

    if __name__ == "__main__":
        app()

It will show that default value in the help text:

    $ python main.py --help

    // Notice the [default: World] 🔍
    Usage: main.py [OPTIONS] [NAME]

      Say hi to NAME very gently, like Dirk.

    Arguments:
      [NAME]  Who to greet  [default: World]

    Options:
      --help                Show this message and exit.

But you can disable that if you want to, with `show_default=False`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", help="Who to greet", show_default=False)):
        """
        Say hi to NAME very gently, like Dirk.
        """
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And then it won\'t show the default value:

    $ python main.py --help

    // Notice the there's no [default: World] now 🔥
    Usage: main.py [OPTIONS] [NAME]

      Say hi to NAME very gently, like Dirk.

    Arguments:
      [NAME]  Who to greet

    Options:
      --help                Show this message and exit.

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
        name: str = typer.Argument(
            "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
        ),
    ):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And it will be used in the help text:

    $ python main.py --help

    Usage: main.py [OPTIONS] [NAME]

    Arguments:
      [NAME]  Who to greet  [default: (Deadpoolio the amazing's name)]

    Options:
      --help                Show this message and exit.

    // See it shows "(Deadpoolio the amazing's name)" instead of the actual default of "Wade Wilson"

## Custom help name (`metavar`)[¶](#custom-help-name-metavar "Permanent link")

You can also customize the text used in the generated help text to represent a *CLI argument*.

By default, it will be the same name you declared, in uppercase letters.

So, if you declare it as:

    name: str

It will be shown as:

    NAME

But you can customize it with the `metavar` parameter for `typer.Argument()`.

For example, let\'s say you don\'t want to have the default of `NAME`, you want to have `username`, in lowercase, and you really want ✨ emojis ✨ everywhere:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", metavar="✨username✨")):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Now the generated help text will have `✨username✨` instead of `NAME`:

    $ python main.py --help

    Usage: main.py [OPTIONS] [✨username✨]

    Arguments:
      [✨username✨]  [default: World]

    Options:
      --help                Show this message and exit.

## *CLI Argument* help panels[¶](#cli-argument-help-panels "Permanent link")

You might want to show the help information for *CLI arguments* in different panels when using the `--help` option.

If you have installed Rich as described in the docs for [Printing and Colors](../../printing/), you can set the `rich_help_panel` parameter to the name of the panel where you want this *CLI argument* to be shown:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str = typer.Argument(..., help="Who to greet"),
        lastname: str = typer.Argument(
            "", help="The last name", rich_help_panel="Secondary Arguments"
        ),
        age: str = typer.Argument(
            "", help="The user's age", rich_help_panel="Secondary Arguments"
        ),
    ):
        """
        Say hi to NAME very gently, like Dirk.
        """
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Then, if you check the `--help` option, you will see a default panel named \"`Arguments`\" for the *CLI arguments* that don\'t have a custom `rich_help_panel`.

And next you will see other panels for the *CLI arguments* that have a custom panel set in the `rich_help_panel` parameter:

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] NAME [LASTNAME] [AGE]               </b>
    <b>                                                                     </b>
     Say hi to NAME very gently, like Dirk.

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    name      <font color="#F4BF75"><b>TEXT</b></font>  Who to greet [default: None] <font color="#A6194C">[required]</font>      │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Secondary Arguments ─────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│   lastname      </font><font color="#A37F4E"><b>[LASTNAME]</b></font>  The last name                         │
    <font color="#A5A5A1">│   age           </font><font color="#A37F4E"><b>[AGE]     </b></font>  The user&apos;s age                        │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

In this example we have a custom *CLI arguments* panel named \"`Secondary Arguments`\".

## Help with style using Rich[¶](#help-with-style-using-rich "Permanent link")

In a future section you will see how to use custom markup in the `help` for *CLI arguments* when reading about [Commands - Command Help](../../commands/help/#rich-markdown-and-markup).

If you are in a hurry you can jump there, but otherwise, it would be better to continue reading here and following the tutorial in order.

## Hide a *CLI argument* from the help text[¶](#hide-a-cli-argument-from-the-help-text "Permanent link")

If you want, you can make a *CLI argument* **not** show up in the `Arguments` section in the help text.

You will probably not want to do this normally, but it\'s possible:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument("World", hidden=True)):
        """
        Say hi to NAME very gently, like Dirk.
        """
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Check it:

    $ python main.py --help

    // Notice there's no Arguments section at all 🔥
    Usage: main.py [OPTIONS] [NAME]

      Say hi to NAME very gently, like Dirk.

    Options:
      --help                Show this message and exit.

Info

Have in mind that the *CLI argument* will still show up in the first line with `Usage`.

But it won\'t show up in the main help text under the `Arguments` section.

### Help text for *CLI arguments* in Click[¶](#help-text-for-cli-arguments-in-click "Permanent link")

Click itself doesn\'t support adding help for *CLI arguments*, and it doesn\'t generate help for them as in the \"`Arguments:`\" sections in the examples above.

Not supporting `help` in *CLI arguments* is an intentional [design decision in Click](https://click.palletsprojects.com/en/7.x/documentation/#documenting-arguments):

> This is to follow the general convention of Unix tools of using arguments for only the most necessary things, and to document them in the command help text by referring to them by name.

So, in Click applications, you are expected to write all the documentation for *CLI arguments* by hand in the docstring.

------------------------------------------------------------------------

Nevertheless, **Typer supports `help` for *CLI arguments***. ✨ 🤷‍♂

**Typer** doesn\'t follow that convention and instead supports `help` to make it easier to have consistent help texts with a consistent format for your CLI programs. 🎨

This is also to help you create CLI programs that are ✨ awesome ✨ *by default*. With very little code.

If you want to keep Click\'s convention in a **Typer** app, you can do it with the `hidden` parameter as described above.

Technical Details

To support `help` in *CLI arguments* **Typer** does a lot of internal work in its own sub-classes of Click\'s internal classes.