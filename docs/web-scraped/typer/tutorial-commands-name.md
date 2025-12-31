# Source: https://typer.tiangolo.com/tutorial/commands/name/

# Custom Command Name[¶](#custom-command-name "Permanent link")

By default, the command names are generated from the function name.

So, if your function is something like:

    def create(username: str):
        ...

Then the command name will be `create`.

But if you already had a function called `create()` somewhere in your code, you would have to name your CLI function differently.

And what if you wanted the command to still be named `create`?

For this, you can set the name of the command in the first parameter for the `@app.command()` decorator:

Python 3.9+

Now, even though the functions are named `cli_create_user()` and `cli_delete_user()`, the commands will still be named `create` and `delete`:

    $ python main.py --help

    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or customize the installation.
      --help                Show this message and exit.

    Commands:
      create
      delete

    // Test it
    $ python main.py create Camila

    Creating user: Camila

Note that any underscores in the function name will be replaced with dashes.

So if your function is something like:

    def create_user(username: str):
        ...

Then the command name will be `create-user`.