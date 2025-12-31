# Source: https://typer.tiangolo.com/tutorial/commands/help/

# Command Help[¶](#command-help "Permanent link")

The same as before, you can add help for the commands in the docstrings and the *CLI options*.

And the `typer.Typer()` application receives a parameter `help` that you can pass with the main help text for your CLI program:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer(help="Awesome CLI user manager.")

    @app.command()
    def create(username: str):
        """
        Create a new user with USERNAME.
        """
        print(f"Creating user: ")

    @app.command()
    def delete(
        username: str,
        force: bool = typer.Option(
            ...,
            prompt="Are you sure you want to delete the user?",
            help="Force deletion without confirmation.",
        ),
    ):
        """
        Delete a user with USERNAME.

        If --force is not used, will ask for confirmation.
        """
        if force:
            print(f"Deleting user: ")
        else:
            print("Operation cancelled")

    @app.command()
    def delete_all(
        force: bool = typer.Option(
            ...,
            prompt="Are you sure you want to delete ALL users?",
            help="Force deletion without confirmation.",
        ),
    ):
        """
        Delete ALL users in the database.

        If --force is not used, will ask for confirmation.
        """
        if force:
            print("Deleting all users")
        else:
            print("Operation cancelled")

    @app.command()
    def init():
        """
        Initialize the users database.
        """
        print("Initializing user database")

    if __name__ == "__main__":
        app()

Check it:

    // Check the new help
    $ python main.py --help

    Usage: main.py [OPTIONS] COMMAND [ARGS]...

      Awesome CLI user manager.

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create      Create a new user with USERNAME.
      delete      Delete a user with USERNAME.
      delete-all  Delete ALL users in the database.
      init        Initialize the users database.

    // Now the commands have inline help 🎉

    // Check the help for create
    $ python main.py create --help

    Usage: main.py create [OPTIONS] USERNAME

      Create a new user with USERNAME.

    Options:
      --help  Show this message and exit.

    // Check the help for delete
    $ python main.py delete --help

    Usage: main.py delete [OPTIONS] USERNAME

      Delete a user with USERNAME.

      If --force is not used, will ask for confirmation.

    Options:
      --force / --no-force  Force deletion without confirmation.  [required]
      --help                Show this message and exit.

    // Check the help for delete-all
    $ python main.py delete-all --help

    Usage: main.py delete-all [OPTIONS]

      Delete ALL users in the database.

      If --force is not used, will ask for confirmation.

    Options:
      --force / --no-force  Force deletion without confirmation.  [required]
      --help                Show this message and exit.

    // Check the help for init
    $ python main.py init --help

    Usage: main.py init [OPTIONS]

      Initialize the users database.

    Options:
      --help  Show this message and exit.

Tip

`typer.Typer()` receives several other parameters for other things, we\'ll see that later.

You will also see how to use \"Callbacks\" later, and those include a way to add this same help message in a function docstring.

## Overwrite command help[¶](#overwrite-command-help "Permanent link")

You will probably be better adding the help text as a docstring to your functions, but if for some reason you wanted to overwrite it, you can use the `help` function argument passed to `@app.command()`:

Python 3.9+

Check it:

    // Check the help
    $ python main.py --help

    // Notice it uses the help passed to @app.command()
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy
                            it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create  Create a new user with USERNAME.
      delete  Delete a user with USERNAME.

    // It uses "Create a new user with USERNAME." instead of "Some internal utility function to create."

## Deprecate a Command[¶](#deprecate-a-command "Permanent link")

There could be cases where you have a command in your app that you need to deprecate, so that your users stop using it, even while it\'s still supported for a while.

You can mark it with the parameter `deprecated=True`:

Python 3.9+

And when you show the `--help` option you will see it\'s marked as \"`deprecated`\":

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                  </b>
    <b>                                                                     </b>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
    <font color="#A5A5A1">│                               shell.                              │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
    <font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
    <font color="#A5A5A1">│                               installation.                       │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create       </b></font> Create a user.                                      │
    <font color="#A5A5A1">│ </font><font color="#6B9F98"><b>delete       </b></font> Delete a user.              <font color="#F92672">(deprecated)           </font> │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

And if you check the `--help` for the deprecated command (in this example, the command `delete`), it also shows it as deprecated:

    $ python main.py delete --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                    </b>
    <b>                                                                     </b>
     <font color="#F92672">(deprecated) </font>
     Delete a user.
     This is deprecated and will stop being supported soon.

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>               │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

## Suggest Commands[¶](#suggest-commands "Permanent link")

As of version 0.20.0, Typer added support for suggesting mistyped command names. This feature is **enabled by default**, but you can disable it with the parameter `suggest_commands=False`:

Python 3.9+

If a user mistypes a command, they\'ll see a helpful suggestion:

    $ python main.py crate

    <font color="#C4A000">Usage: </font>main.py [OPTIONS] COMMAND [ARGS]...
    <font color="#AAAAAA">Try </font><font color="#22436D">&apos;main.py </font><font color="#4C6A8A"><b>--help</b></font><font color="#22436D">&apos;</font><font color="#AAAAAA"> for help.</font>
    <font color="#CC0000">╭─ Error ───────────────────────────────────────────────────────────╮</font>
    <font color="#CC0000">│</font> No such command &apos;crate&apos;. Did you mean &apos;create&apos;?                   <font color="#CC0000">│</font>
    <font color="#CC0000">╰───────────────────────────────────────────────────────────────────╯</font>

If there are multiple close matches, Typer will suggest them all. This feature uses Python\'s built-in `difflib.get_close_matches()` to find similar command names, making your CLI more user-friendly by helping users recover from typos.

## Rich Markdown and Markup[¶](#rich-markdown-and-markup "Permanent link")

If you have **Rich** installed as described in [Printing and Colors](../../printing/), you can configure your app to enable markup text with the parameter `rich_markup_mode`.

Then you can use more formatting in the docstrings and the `help` parameter for *CLI arguments* and *CLI options*. You will see more about it below. 👇

Info

By default, `rich_markup_mode` is `None` if Rich is not installed, and `"rich"` if it is installed. In the latter case, you can set `rich_markup_mode` to `None` to disable rich text formatting.

### Rich Markup[¶](#rich-markup "Permanent link")

If you set `rich_markup_mode="rich"` when creating the `typer.Typer()` app, you will be able to use [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html) in the docstring, and even in the help for the *CLI arguments* and options:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer(rich_markup_mode="rich")

    @app.command()
    def create(
        username: str = typer.Argument(
            ..., help="The username to be [green]created[/green]"
        ),
    ):
        """
        [bold green]Create[/bold green] a new [italic]shiny[/italic] user. :sparkles:

        This requires a [underline]username[/underline].
        """
        print(f"Creating user: ")

    @app.command(help="[bold red]Delete[/bold red] a user with [italic]USERNAME[/italic].")
    def delete(
        username: str = typer.Argument(..., help="The username to be [red]deleted[/red]"),
        force: bool = typer.Option(
            False, help="Force the [bold red]deletion[/bold red] :boom:"
        ),
    ):
        """
        Some internal utility function to delete.
        """
        print(f"Deleting user: ")

    if __name__ == "__main__":
        app()

With that, you can use [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html) to format the text in the docstring for the command `create`, make the word \"`create`\" bold and green, and even use an [emoji](https://rich.readthedocs.io/en/stable/markup.html#emoji).

You can also use markup in the help for the `username` CLI Argument.

And the same as before, the help text overwritten for the command `delete` can also use Rich Markup, the same in the CLI Argument and CLI Option.

If you run the program and check the help, you will see that **Typer** uses **Rich** internally to format the help.

Check the help for the `create` command:

    $ python main.py create --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME                     </b>
    <b>                                                                     </b>
     <font color="#A6E22E"><b>Create</b></font> a new <i>shiny</i> user. ✨
     This requires a <font color="#A5A5A1"><u style="text-decoration-style:single">username</u></font><font color="#A5A5A1">.                                           </font>

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <font color="#A6E22E">created</font>               │
    <font color="#A5A5A1">│                          [default: None]                          │</font>
    <font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                </font>               │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

And check the help for the `delete` command:

    $ python main.py delete --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                     </b>
    <b>                                                                     </b>
     <font color="#F92672"><b>Delete</b></font> a user with <i>USERNAME</i>.

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <font color="#F92672">deleted</font>               │
    <font color="#A5A5A1">│                          [default: None]                          │</font>
    <font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                </font>               │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the <font color="#F92672"><b>deletion</b></font> 💥                  │
    <font color="#A5A5A1">│                            [default: no-force]                    │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

### Rich Markdown[¶](#rich-markdown "Permanent link")

If you set `rich_markup_mode="markdown"` when creating the `typer.Typer()` app, you will be able to use Markdown in the docstring:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer(rich_markup_mode="markdown")

    @app.command()
    def create(username: str = typer.Argument(..., help="The username to be **created**")):
        """
        **Create** a new *shiny* user. :sparkles:

        * Create a username

        * Show that the username is created

        ---

        Learn more at the [Typer docs website](https://typer.tiangolo.com)
        """
        print(f"Creating user: ")

    @app.command(help="**Delete** a user with *USERNAME*.")
    def delete(
        username: str = typer.Argument(..., help="The username to be **deleted**"),
        force: bool = typer.Option(False, help="Force the **deletion** :boom:"),
    ):
        """
        Some internal utility function to delete.
        """
        print(f"Deleting user: ")

    if __name__ == "__main__":
        app()

With that, you can use Markdown to format the text in the docstring for the command `create`, make the word \"`create`\" bold, show a list of items, and even use an [emoji](https://rich.readthedocs.io/en/stable/markup.html#emoji).

And the same as before, the help text overwritten for the command `delete` can also use Markdown.

Check the help for the `create` command:

    $ python main.py create --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME                     </b>
    <b>                                                                     </b>
     <b>Create</b> a new <i>shiny</i> user. ✨

     <font color="#F4BF75"><b> • </b></font><font color="#A5A5A1">Create a username                                                </font>
     <font color="#F4BF75"><b> • </b></font><font color="#A5A5A1">Show that the username is created                                </font>

     <font color="#F4BF75">───────────────────────────────────────────────────────────────────</font>
     Learn more at the <font color="#44919F">Typer docs website</font>

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <b>created</b>               │
    <font color="#A5A5A1">│                          [default: None]                          │</font>
    <font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                              </font> │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

And the same for the `delete` command:

    $ python main.py delete --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                     </b>
    <b>                                                                     </b>
     <b>Delete</b> a user with <i>USERNAME</i>.

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <b>deleted</b>               │
    <font color="#A5A5A1">│                          [default: None]                          │</font>
    <font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                              </font> │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the <b>deletion</b> 💥                  │
    <font color="#A5A5A1">│                            [default: no-force]                    │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

Info

Notice that in Markdown you cannot define colors. For colors you might prefer to use Rich markup.

## Help Panels[¶](#help-panels "Permanent link")

If you have many commands or CLI parameters, you might want to show their documentation in different panels when using the `--help` option.

If you installed [Rich](https://rich.readthedocs.io/) as described in [Printing and Colors](../../printing/), you can configure the panel to use for each command or CLI parameter.

### Help Panels for Commands[¶](#help-panels-for-commands "Permanent link")

To set the panel for a command you can pass the argument `rich_help_panel` with the name of the panel you want to use:

Python 3.9+

Commands without a panel will be shown in the default panel `Commands`, and the rest will be shown in the next panels:

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                   </b>
    <b>                                                                     </b>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
    <font color="#A5A5A1">│                               shell.                              │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
    <font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
    <font color="#A5A5A1">│                               installation.                       │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create          </b></font> <font color="#A6E22E">Create</font> a new user. ✨                            │
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>delete          </b></font> <font color="#F92672">Delete</font> a user. ❌                                │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Utils and Configs ───────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>config  </b></font> <font color="#66D9EF">Configure</font> the system. ⚙                                  │
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>sync    </b></font> <font color="#66D9EF">Synchronize</font> the system or something fancy like that. ♻   │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Help and Others ─────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>help         </b></font> Get <font color="#F4BF75">help</font> with the system. ❓                        │
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>report       </b></font> <font color="#F4BF75">Report</font> an issue. ❗                                 │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

### Help Panels for CLI Parameters[¶](#help-panels-for-cli-parameters "Permanent link")

The same way, you can configure the panels for *CLI arguments* and *CLI options* with `rich_help_panel`.

And of course, in the same application you can also set the `rich_help_panel` for commands.

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer(rich_markup_mode="rich")

    @app.command()
    def create(
        username: str = typer.Argument(..., help="The username to create"),
        lastname: str = typer.Argument(
            "", help="The last name of the new user", rich_help_panel="Secondary Arguments"
        ),
        force: bool = typer.Option(False, help="Force the creation of the user"),
        age: int | None = typer.Option(
            None, help="The age of the new user", rich_help_panel="Additional Data"
        ),
        favorite_color: str | None = typer.Option(
            None,
            help="The favorite color of the new user",
            rich_help_panel="Additional Data",
        ),
    ):
        """
        [green]Create[/green] a new user. :sparkles:
        """
        print(f"Creating user: ")

    @app.command(rich_help_panel="Utils and Configs")
    def config(configuration: str):
        """
        [blue]Configure[/blue] the system. :gear:
        """
        print(f"Configuring the system with: ")

    if __name__ == "__main__":
        app()

    from typing import Union

    import typer

    app = typer.Typer(rich_markup_mode="rich")

    @app.command()
    def create(
        username: str = typer.Argument(..., help="The username to create"),
        lastname: str = typer.Argument(
            "", help="The last name of the new user", rich_help_panel="Secondary Arguments"
        ),
        force: bool = typer.Option(False, help="Force the creation of the user"),
        age: Union[int, None] = typer.Option(
            None, help="The age of the new user", rich_help_panel="Additional Data"
        ),
        favorite_color: Union[str, None] = typer.Option(
            None,
            help="The favorite color of the new user",
            rich_help_panel="Additional Data",
        ),
    ):
        """
        [green]Create[/green] a new user. :sparkles:
        """
        print(f"Creating user: ")

    @app.command(rich_help_panel="Utils and Configs")
    def config(configuration: str):
        """
        [blue]Configure[/blue] the system. :gear:
        """
        print(f"Configuring the system with: ")

    if __name__ == "__main__":
        app()

Then if you run the application you will see all the *CLI parameters* in their respective panels.

-   First the ***CLI arguments*** that don\'t have a panel name set in a **default** one named \"`Arguments`\".
-   Next the ***CLI arguments*** with a **custom panel**. In this example named \"`Secondary Arguments`\".
-   After that, the ***CLI options*** that don\'t have a panel in a **default** one named \"`Options`\".
-   And finally, the ***CLI options*** with a **custom panel** set. In this example named \"`Additional Data`\".

You can check the `--help` option for the command `create`:

    $ python main.py create --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME [LASTNAME]          </b>
    <b>                                                                     </b>
     <font color="#A6E22E">Create</font> a new user. ✨

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to create [default: None]   │
    <font color="#A5A5A1">│                          </font><font color="#A6194C">[required]            </font>                   │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Secondary Arguments ─────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│   lastname      </font><font color="#A37F4E"><b>[LASTNAME]</b></font>  The last name of the new user         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the creation of the user         │
    <font color="#A5A5A1">│                            [default: no-force]                    │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Additional Data ─────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--age</b></font>                   <font color="#F4BF75"><b>INTEGER</b></font>  The age of the new user          │
    <font color="#A5A5A1">│                                  [default: None]                  │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--favorite-color</b></font>        <font color="#F4BF75"><b>TEXT   </b></font>  The favorite color of the new    │
    <font color="#A5A5A1">│                                  user                             │</font>
    <font color="#A5A5A1">│                                  [default: None]                  │</font>
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

And of course, the `rich_help_panel` can be used in the same way for commands in the same application.

And those panels will be shown when you use the main `--help` option.

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                   </b>
    <b>                                                                     </b>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
    <font color="#A5A5A1">│                               shell.                              │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
    <font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
    <font color="#A5A5A1">│                               installation.                       │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create          </b></font> <font color="#A6E22E">Create</font> a new user. ✨                            │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Utils and Configs ───────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>config         </b></font> <font color="#66D9EF">Configure</font> the system. ⚙                           │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

You can see the custom panel for the commands for \"`Utils and Configs`\".

## Epilog[¶](#epilog "Permanent link")

If you need, you can also add an epilog section to the help of your commands:

Python 3.9+

And when you check the `--help` option it will look like:

    $ python main.py --help

    <b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] USERNAME                            </b>
    <b>                                                                     </b>
     <font color="#A6E22E">Create</font> a new user. ✨

    <font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>               │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
    <font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
    <font color="#A5A5A1">│                               shell.                              │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
    <font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
    <font color="#A5A5A1">│                               installation.                       │</font>
    <font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
    <font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

     Made with ❤ in <font color="#66D9EF">Venus</font>