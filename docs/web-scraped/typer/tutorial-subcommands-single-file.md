# Source: https://typer.tiangolo.com/tutorial/subcommands/single-file/

# SubCommands in a Single File[¶](#subcommands-in-a-single-file "Permanent link")

In some cases, it\'s possible that your application code needs to live on a single file.

You can still use the same ideas:

Python 3.9+

There are several things to notice here\...

## Apps at the top[¶](#apps-at-the-top "Permanent link")

First, you can create `typer.Typer()` objects and add them to another one at the top.

It doesn\'t have to be done after creating the subcommands:

Python 3.9+

You can add the commands (subcommands) to each `typer.Typer()` app later and it will still work.

## Function names[¶](#function-names "Permanent link")

As you now have subcommands like `create` for `users` and for `items`, you can no longer call the functions with just the name, like `def create()`, because they would overwrite each other.

So we use longer names:

Python 3.9+

## Command name[¶](#command-name "Permanent link")

We are naming the functions with longer names so that they don\'t overwrite each other.

But we still want the subcommands to be `create`, `delete`, etc.

To call them like:

    // We want this ✔️
    $ python main.py items create

instead of:

    // We don't want this ⛔️
    $ python main.py items items-create

So we pass the name we want to use for each subcommand as the function argument to the decorator:

Python 3.9+

## Check it[¶](#check-it "Permanent link")

It still works the same:

    // Check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --install-completion  Install completion for the current shell.
      --show-completion     Show completion for the current shell, to copy it or
                            customize the installation.
      --help                Show this message and exit.

    Commands:
      items
      users

Check the `items` command:

    // Check the help for items
    $ python main.py items --help

    // It shows its own commands (subcommands): create, delete, sell
    Usage: main.py items [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create
      delete
      sell

    // Try it
    $ python main.py items create Wand

    Creating item: Wand

    $ python main.py items sell Vase

    Selling item: Vase

And the same for the `users` command:

    $ python main.py users --help

    Usage: main.py users [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      create
      delete

    // Try it
    $ python main.py users create Camila

    Creating user: Camila