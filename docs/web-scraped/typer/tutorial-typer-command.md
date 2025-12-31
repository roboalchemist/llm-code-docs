# Source: https://typer.tiangolo.com/tutorial/typer-command/

# `typer` command[¶](#typer-command "Permanent link")

The `typer` command provides ✨ completion ✨ in the Terminal for your own small scripts. Even if they don\'t use Typer internally. Of course, it works better if you use **Typer** in your script.

It\'s probably most useful if you have a small custom Python script using **Typer** (maybe as part of some project), for some small tasks, and it\'s not complex/important enough to create a whole installable Python package for it (something to be installed with `pip`).

In that case, you can run your program with the `typer` command in your Terminal, and it will provide completion for your script.

The `typer` command also has functionality to generate Markdown documentation for your own **Typer** programs 📝.

## Install[¶](#install "Permanent link")

When you install **Typer** with:

    pip install typer

\...it includes the `typer` command.

If you don\'t want to have the `typer` command, you can install instead:

    pip install typer-slim

You can still use it by calling the Typer library as a module with:

    python -m typer

## Install completion[¶](#install-completion "Permanent link")

You can then install completion for the `typer` command with:

    $ typer --install-completion

    bash completion installed in /home/user/.bashrc.
    Completion will take effect once you restart the terminal.

### Sample script[¶](#sample-script "Permanent link")

Let\'s say you have a script that uses **Typer** in `my_custom_script.py`:

    from typing import Optional

    import typer

    app = typer.Typer()

    @app.command()
    def hello(name: Optional[str] = None):
        if name:
            typer.echo(f"Hello ")
        else:
            typer.echo("Hello World!")

    @app.command()
    def bye(name: Optional[str] = None):
        if name:
            typer.echo(f"Bye ")
        else:
            typer.echo("Goodbye!")

    if __name__ == "__main__":
        app()

For it to work, you would also install **Typer**:

    $ python -m pip install typer
    ---> 100%
    Successfully installed typer

### Run with Python[¶](#run-with-python "Permanent link")

Then you could run your script with normal Python:

    $ python my_custom_script.py hello

    Hello World!

    $ python my_custom_script.py hello --name Camila

    Hello Camila!

    $ python my_custom_script.py bye --name Camila

    Bye Camila

There\'s nothing wrong with using Python directly to run it. And, in fact, if some other code or program uses your script, that would probably be the best way to do it.

⛔️ But in your terminal, you won\'t get completion when hitting [TAB] for any of the subcommands or options, like `hello`, `bye`, and `--name`.

### Run with the `typer` command.[¶](#run-with-the-typer-command "Permanent link") 

You can also run the same script with the `typer` command:

    $ typer my_custom_script.py run hello

    Hello World!

    $ typer my_custom_script.py run hello --name Camila

    Hello Camila!

    $ typer my_custom_script.py run bye --name Camila

    Bye Camila

-   Instead of using `python` directly you use the `typer` command.
-   After the name of the file, add the subcommand `run`.

✔️ If you installed completion for the `typer` command as described above, when you hit [TAB] you will have ✨ completion for everything ✨, including all the subcommands and options of your script, like `hello`, `bye`, and `--name` 🚀.

## If main[¶](#if-main "Permanent link")

Because the `typer` command won\'t use the block with:

    if __name__ == "__main__":
        app()

\...you can also remove it if you are calling that script only with the `typer` command.

## Run other files[¶](#run-other-files "Permanent link")

The `typer` command can run any script with **Typer**, but the script doesn\'t even have to use **Typer** at all.

You could even run a file with a function that could be used with `typer.run()`, even if the script doesn\'t use `typer.run()` or anything else.

For example, a file `main.py` like this will still work:

    def main(name: str = "World"):
        """
        Say hi to someone, by default to the World.
        """
        print(f"Hello ")

Then you can call it with:

    $ typer main.py run --help
    Usage: typer run [OPTIONS]

      Say hi to someone, by default to the World.

    Options:
      --name TEXT
      --help       Show this message and exit.

    $ typer main.py run --name Camila

    Hello Camila

And it will also have completion for things like the `--name` *CLI Option*.

## Run a package or module[¶](#run-a-package-or-module "Permanent link")

Instead of a file path you can pass a module (possibly in a package) to import.

For example:

    $ typer my_package.main run --help
    Usage: typer run [OPTIONS]

    Options:
      --name TEXT
      --help       Show this message and exit.

    $ typer my_package.main run --name Camila

    Hello Camila

## Options[¶](#options "Permanent link")

You can specify one of the following **CLI options**:

-   `--app`: the name of the variable with a `Typer()` object to run as the main app.
-   `--func`: the name of the variable with a function that would be used with `typer.run()`.

### Defaults[¶](#defaults "Permanent link")

When your run a script with the `typer` command it will use the app from the following priority:

-   An app object from the `--app` *CLI Option*.
-   A function to convert to a **Typer** app from `--func` *CLI Option* (like when using `typer.run()`).
-   A **Typer** app in a variable with a name of `app`, `cli`, or `main`.
-   The first **Typer** app available in the file, with any name.
-   A function in a variable with a name of `main`, `cli`, or `app`.
-   The first function in the file, with any name.

## Generate docs[¶](#generate-docs "Permanent link")

You can also use the `typer` command to generate Markdown documentation for your **Typer** application.

### Sample script with docs[¶](#sample-script-with-docs "Permanent link")

For example, you could have a script like:

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

### Generate docs with the `typer` command[¶](#generate-docs-with-the-typer-command "Permanent link")

Then you could generate docs for it with the `typer` command.

You can use the subcommand `utils`.

And then the subcommand `docs`.

    $ typer some_script.py utils docs

Tip

If you installed only `typer-slim` and you don\'t have the `typer` command, you can still generate docs with:

    $ python -m typer some_script.py utils docs

**Options**:

-   `--name TEXT`: The name of the CLI program to use in docs.
-   `--output FILE`: An output file to write docs to, like README.md.
-   `--title TEXT`: A title to use in the docs, by default the name of the command.

For example:

    $ typer my_package.main utils docs --name awesome-cli --output README.md

    Docs saved to: README.md

### Sample docs output[¶](#sample-docs-output "Permanent link")

For example, for the previous script, the generated docs would look like:

------------------------------------------------------------------------

## `awesome-cli`[¶](#awesome-cli "Permanent link")

Awesome CLI user manager.

**Usage**:

    $ awesome-cli [OPTIONS] COMMAND [ARGS]...

**Options**:

-   `--install-completion`: Install completion for the current shell.
-   `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
-   `--help`: Show this message and exit.

**Commands**:

-   `create`: Create a new user with USERNAME.
-   `delete`: Delete a user with USERNAME.
-   `delete-all`: Delete ALL users in the database.
-   `init`: Initialize the users database.

## `awesome-cli create`[¶](#awesome-cli-create "Permanent link")

Create a new user with USERNAME.

**Usage**:

    $ awesome-cli create [OPTIONS] USERNAME

**Options**:

-   `--help`: Show this message and exit.

## `awesome-cli delete`[¶](#awesome-cli-delete "Permanent link")

Delete a user with USERNAME.

If \--force is not used, will ask for confirmation.

**Usage**:

    $ awesome-cli delete [OPTIONS] USERNAME

**Options**:

-   `--force / --no-force`: Force deletion without confirmation. \[required\]
-   `--help`: Show this message and exit.

## `awesome-cli delete-all`[¶](#awesome-cli-delete-all "Permanent link")

Delete ALL users in the database.

If \--force is not used, will ask for confirmation.

**Usage**:

    $ awesome-cli delete-all [OPTIONS]

**Options**:

-   `--force / --no-force`: Force deletion without confirmation. \[required\]
-   `--help`: Show this message and exit.

## `awesome-cli init`[¶](#awesome-cli-init "Permanent link")

Initialize the users database.

**Usage**:

    $ awesome-cli init [OPTIONS]

**Options**:

-   `--help`: Show this message and exit.