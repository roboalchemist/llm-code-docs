# Source: https://typer.tiangolo.com/tutorial/commands/arguments/

# Command CLI Arguments[¶](#command-cli-arguments "Permanent link")

The same way as with a CLI application with a single command, subcommands (or just \"commands\") can also have their own *CLI arguments*:

Python 3.9+

    // Check the help for create
    $ python main.py create --help

    Usage: main.py create [OPTIONS] USERNAME

    Options:
      --help  Show this message and exit.

    // Call it with a CLI argument
    $ python main.py create Camila

    Creating user: Camila

    // The same for delete
    $ python main.py delete Camila

    Deleting user: Camila

Tip

Everything to the *right* of the *command* are *CLI parameters* (*CLI arguments* and *CLI options*) for that command.

Technical Details

Actually, it\'s everything to the right of that command, *before any subcommand*.

It\'s possible to have groups of *subcommands*, it\'s like if one *command* also had *subcommands*. And then those *subcommands* could have their own *CLI parameters*, taking their own *CLI parameters*.

You will see about them later in another section.