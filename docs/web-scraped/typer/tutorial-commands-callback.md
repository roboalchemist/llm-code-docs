# Source: https://typer.tiangolo.com/tutorial/commands/callback/

# Typer Callback[¶](#typer-callback "Permanent link")

When you create an `app = typer.Typer()` it works as a group of commands.

And you can create multiple commands with it.

Each of those commands can have their own *CLI parameters*.

But as those *CLI parameters* are handled by each of those commands, they don\'t allow us to create *CLI parameters* for the main CLI application itself.

But we can use `@app.callback()` for that.

It\'s very similar to `@app.command()`, but it declares the *CLI parameters* for the main CLI application (before the commands):

Python 3.9+

Here we create a `callback` with a `--verbose` *CLI option*.

Tip

After getting the `--verbose` flag, we modify a global `state`, and we use it in the other commands.

There are other ways to achieve the same, but this will suffice for this example.

And as we added a docstring to the callback function, by default it will be extracted and used as the help text.

Check it:

    // Check the help
    $ python main.py --help

    // Notice the main help text, extracted from the callback function: "Manage users in the awesome CLI app."
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

      Manage users in the awesome CLI app.

    Options:
      --verbose / --no-verbose  [default: False]
      --install-completion      Install completion for the current shell.
      --show-completion         Show completion for the current shell, to copy it or customize the installation.
      --help                    Show this message and exit.

    Commands:
      create
      delete

    // Check the new top level CLI option --verbose

    // Try it normally
    $ python main.py create Camila

    Creating user: Camila

    // And now with --verbose
    $ python main.py --verbose create Camila

    Will write verbose output
    About to create a user
    Creating user: Camila
    Just created a user

    // Notice that --verbose belongs to the callback, it has to go before create or delete ⛔️
    $ python main.py create --verbose Camila

    Usage: main.py create [OPTIONS] USERNAME
    Try "main.py create --help" for help.

    Error: No such option: --verbose

## Adding a callback on creation[¶](#adding-a-callback-on-creation "Permanent link")

It\'s also possible to add a callback when creating the `typer.Typer()` app:

Python 3.9+

That achieves the same as with `@app.callback()`.

Check it:

    $ python main.py create Camila

    Running a command
    Creating user: Camila

## Overriding a callback[¶](#overriding-a-callback "Permanent link")

If you added a callback when creating the `typer.Typer()` app, it\'s possible to override it with `@app.callback()`:

Python 3.9+

Now `new_callback()` will be the one used.

Check it:

    $ python main.py create Camila

    // Notice that the message is the one from new_callback()
    Override callback, running a command
    Creating user: Camila

## Adding a callback only for documentation[¶](#adding-a-callback-only-for-documentation "Permanent link")

You can also add a callback just to add the documentation in the docstring.

It can be convenient especially if you have several lines of text, as the indentation will be automatically handled for you:

Python 3.9+

Now the callback will be used mainly to extract the docstring for the help text.

Check it:

    $ python main.py --help

    // Notice all the help text extracted from the callback docstring
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

      Manage users CLI app.

      Use it with the create command.

      A new user with the given NAME will be created.

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create

    // And it just works as normally
    $ python main.py create Camila

    Creating user: Camila

## Click Group[¶](#click-group "Permanent link")

If you come from Click, this **Typer** callback is the equivalent of the function in a [Click Group](https://click.palletsprojects.com/en/7.x/quickstart/#nesting-commands).

For example:

    import click

    @click.group()
    def cli():
        pass

The original function `cli` would be the equivalent of a Typer callback.

Technical Details

When using Click, it converts that `cli` variable to a Click `Group` object. And then the original function no longer exists in that variable.

**Typer** doesn\'t do that, the callback function is not modified, only registered in the `typer.Typer` app. This is intentional, it\'s part of **Typer**\'s design, to allow having editor auto completion and type checks.