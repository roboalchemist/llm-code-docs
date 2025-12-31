# Source: https://typer.tiangolo.com/tutorial/commands/one-or-multiple/

# One or Multiple Commands[¶](#one-or-multiple-commands "Permanent link")

You might have noticed that if you create a single command, as in the following example:

Python 3.9+

**Typer** is smart enough to create a CLI application with that single function as the main CLI application, not as a command/subcommand:

    // Without a CLI argument
    $ python main.py

    Usage: main.py [OPTIONS] NAME
    Try "main.py --help" for help.

    Error: Missing argument 'NAME'.

    // With the NAME CLI argument
    $ python main.py Camila

    Hello Camila

    // Asking for help
    $ python main.py

    Usage: main.py [OPTIONS] NAME

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

Tip

Notice that it doesn\'t show a command `main`, even though the function name is `main`.

But if you add multiple commands, **Typer** will create one *CLI command* for each one of them:

Python 3.9+

Here we have 2 commands `create` and `delete`:

    // Check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create
      delete

    // Test the commands
    $ python main.py create

    Creating user: Hiro Hamada

    $ python main.py delete

    Deleting user: Hiro Hamada

## One command and one callback[¶](#one-command-and-one-callback "Permanent link")

If you want to create a CLI app with one single command but you still want it to be a command/subcommand you can just add a callback:

Python 3.9+

And now your CLI program will have a single command.

Check it:

    // Check the help
    $ python main.py --help

    // Notice the single command create
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create

    // Try it
    $ python main.py create

    Creating user: Hiro Hamada

## Using the callback to document[¶](#using-the-callback-to-document "Permanent link")

Now that you are using a callback just to have a single command, you might as well use it to add documentation for your app:

Python 3.9+

And now the docstring from the callback will be used as the help text:

    $ python main.py --help

    // Notice the help text from the docstring
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

      Creates a single user Hiro Hamada.

      In the next version it will create 5 more users.

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create

    // And it still works the same, the callback does nothing
    $ python main.py create

    Creating user: Hiro Hamada