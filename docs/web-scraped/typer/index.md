# Source: https://typer.tiangolo.com/

# Typer

[![Typer](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg#only-light)](https://typer.tiangolo.com) [![Typer](img/logo-margin/logo-margin-white-vector.svg#only-dark)](https://typer.tiangolo.com)

*Typer, build great CLIs. Easy to code. Based on Python type hints.*

[![Test](https://github.com/fastapi/typer/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/typer/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster) [![Publish](https://github.com/fastapi/typer/workflows/Publish/badge.svg)](https://github.com/fastapi/typer/actions?query=workflow%3APublish) [![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/typer.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/typer) [![Package version](https://img.shields.io/pypi/v/typer?color=%2334D058&label=pypi%20package)](https://pypi.org/project/typer)

------------------------------------------------------------------------

**Documentation**: [https://typer.tiangolo.com](https://typer.tiangolo.com)

**Source Code**: [https://github.com/fastapi/typer](https://github.com/fastapi/typer)

------------------------------------------------------------------------

Typer is a library for building CLI applications that users will **love using** and developers will **love creating**. Based on Python type hints.

It\'s also a command line tool to run scripts, automatically converting them to CLI applications.

The key features are:

-   **Intuitive to write**: Great editor support. Completion everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
-   **Easy to use**: It\'s easy to use for the final users. Automatic help, and automatic completion for all shells.
-   **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
-   **Start simple**: The simplest example adds only 2 lines of code to your app: **1 import, 1 function call**.
-   **Grow large**: Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.
-   **Run scripts**: Typer includes a `typer` command/program that you can use to run scripts, automatically converting them to CLIs, even if they don\'t use Typer internally.

## FastAPI of CLIs[¶](#fastapi-of-clis "Permanent link")

**Typer** is [FastAPI](https://fastapi.tiangolo.com)\'s little sibling, it\'s the FastAPI of CLIs.

## Installation[¶](#installation "Permanent link")

Create and activate a [virtual environment](https://typer.tiangolo.com/virtual-environments/) and then install **Typer**:

    $ pip install typer
    ---> 100%
    Successfully installed typer rich shellingham

## Example[¶](#example "Permanent link")

### The absolute minimum[¶](#the-absolute-minimum "Permanent link")

-   Create a file `main.py` with:

    def main(name: str):
        print(f"Hello ")

This script doesn\'t even use Typer internally. But you can use the `typer` command to run it as a CLI application.

### Run it[¶](#run-it "Permanent link")

Run your application with the `typer` command:

    // Run your application
    $ typer main.py run

    // You get a nice error, you are missing NAME
    Usage: typer [PATH_OR_MODULE] run [OPTIONS] NAME
    Try 'typer [PATH_OR_MODULE] run --help' for help.
    ╭─ Error ───────────────────────────────────────────╮
    │ Missing argument 'NAME'.                          │
    ╰───────────────────────────────────────────────────╯

    // You get a --help for free
    $ typer main.py run --help

    Usage: typer [PATH_OR_MODULE] run [OPTIONS] NAME

    Run the provided Typer app.

    ╭─ Arguments ───────────────────────────────────────╮
    │ *    name      TEXT  [default: None] [required]   |
    ╰───────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────╮
    │ --help          Show this message and exit.       │
    ╰───────────────────────────────────────────────────╯

    // Now pass the NAME argument
    $ typer main.py run Camila

    Hello Camila

    // It works! 🎉

This is the simplest use case, not even using Typer internally, but it can already be quite useful for simple scripts.

**Note**: auto-completion works when you create a Python package and run it with `--install-completion` or when you use the `typer` command.

## Use Typer in your code[¶](#use-typer-in-your-code "Permanent link")

Now let\'s start using Typer in your own code, update `main.py` with:

    import typer

    def main(name: str):
        print(f"Hello ")

    if __name__ == "__main__":
        typer.run(main)

Now you could run it with Python directly:

    // Run your application
    $ python main.py

    // You get a nice error, you are missing NAME
    Usage: main.py [OPTIONS] NAME
    Try 'main.py --help' for help.
    ╭─ Error ───────────────────────────────────────────╮
    │ Missing argument 'NAME'.                          │
    ╰───────────────────────────────────────────────────╯

    // You get a --help for free
    $ python main.py --help

    Usage: main.py [OPTIONS] NAME

    ╭─ Arguments ───────────────────────────────────────╮
    │ *    name      TEXT  [default: None] [required]   |
    ╰───────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────╮
    │ --help          Show this message and exit.       │
    ╰───────────────────────────────────────────────────╯

    // Now pass the NAME argument
    $ python main.py Camila

    Hello Camila

    // It works! 🎉

**Note**: you can also call this same script with the `typer` command, but you don\'t need to.

## Example upgrade[¶](#example-upgrade "Permanent link")

This was the simplest example possible.

Now let\'s see one a bit more complex.

### An example with two subcommands[¶](#an-example-with-two-subcommands "Permanent link")

Modify the file `main.py`.

Create a `typer.Typer()` app, and create two subcommands with their parameters.

    import typer

    app = typer.Typer()

    @app.command()
    def hello(name: str):
        print(f"Hello ")

    @app.command()
    def goodbye(name: str, formal: bool = False):
        if formal:
            print(f"Goodbye Ms. . Have a good day.")
        else:
            print(f"Bye !")

    if __name__ == "__main__":
        app()

And that will:

-   Explicitly create a `typer.Typer` app.
    -   The previous `typer.run` actually creates one implicitly for you.
-   Add two subcommands with `@app.command()`.
-   Execute the `app()` itself, as if it was a function (instead of `typer.run`).

### Run the upgraded example[¶](#run-the-upgraded-example "Permanent link")

Check the new help:

    $ python main.py --help

     Usage: main.py [OPTIONS] COMMAND [ARGS]...

    ╭─ Options ─────────────────────────────────────────╮
    │ --install-completion          Install completion  │
    │                               for the current     │
    │                               shell.              │
    │ --show-completion             Show completion for │
    │                               the current shell,  │
    │                               to copy it or       │
    │                               customize the       │
    │                               installation.       │
    │ --help                        Show this message   │
    │                               and exit.           │
    ╰───────────────────────────────────────────────────╯
    ╭─ Commands ────────────────────────────────────────╮
    │ goodbye                                           │
    │ hello                                             │
    ╰───────────────────────────────────────────────────╯

    // When you create a package you get ✨ auto-completion ✨ for free, installed with --install-completion

    // You have 2 subcommands (the 2 functions): goodbye and hello

Now check the help for the `hello` command:

    $ python main.py hello --help

     Usage: main.py hello [OPTIONS] NAME

    ╭─ Arguments ───────────────────────────────────────╮
    │ *    name      TEXT  [default: None] [required]   │
    ╰───────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────╮
    │ --help          Show this message and exit.       │
    ╰───────────────────────────────────────────────────╯

And now check the help for the `goodbye` command:

    $ python main.py goodbye --help

     Usage: main.py goodbye [OPTIONS] NAME

    ╭─ Arguments ───────────────────────────────────────╮
    │ *    name      TEXT  [default: None] [required]   │
    ╰───────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────╮
    │ --formal    --no-formal      [default: no-formal] │
    │ --help                       Show this message    │
    │                              and exit.            │
    ╰───────────────────────────────────────────────────╯

    // Automatic --formal and --no-formal for the bool option 🎉

Now you can try out the new command line application:

    // Use it with the hello command

    $ python main.py hello Camila

    Hello Camila

    // And with the goodbye command

    $ python main.py goodbye Camila

    Bye Camila!

    // And with --formal

    $ python main.py goodbye --formal Camila

    Goodbye Ms. Camila. Have a good day.

**Note**: If your app only has one command, by default the command name is **omitted** in usage: `python main.py Camila`. However, when there are multiple commands, you must **explicitly include the command name**: `python main.py hello Camila`. See [One or Multiple Commands](https://typer.tiangolo.com/tutorial/commands/one-or-multiple/) for more details.

### Recap[¶](#recap "Permanent link")

In summary, you declare **once** the types of parameters (*CLI arguments* and *CLI options*) as function parameters.

You do that with standard modern Python types.

You don\'t have to learn a new syntax, the methods or classes of a specific library, etc.

Just standard **Python**.

For example, for an `int`:

    total: int

or for a `bool` flag:

    force: bool

And similarly for **files**, **paths**, **enums** (choices), etc. And there are tools to create **groups of subcommands**, add metadata, extra **validation**, etc.

**You get**: great editor support, including **completion** and **type checks** everywhere.

**Your users get**: automatic **`--help`**, **auto-completion** in their terminal (Bash, Zsh, Fish, PowerShell) when they install your package or when using the `typer` command.

For a more complete example including more features, see the [Tutorial - User Guide](https://typer.tiangolo.com/tutorial/).

## Dependencies[¶](#dependencies "Permanent link")

**Typer** stands on the shoulders of a giant. Its only internal required dependency is [Click](https://click.palletsprojects.com/).

By default it also comes with extra standard dependencies:

-   [`rich`](https://rich.readthedocs.io/en/stable/index.html): to show nicely formatted errors automatically.
-   [`shellingham`](https://github.com/sarugaku/shellingham): to automatically detect the current shell when installing completion.
    -   With `shellingham` you can just use `--install-completion`.
    -   Without `shellingham`, you have to pass the name of the shell to install completion for, e.g. `--install-completion bash`.

### `typer-slim`[¶](#typer-slim "Permanent link")

If you don\'t want the extra standard optional dependencies, install `typer-slim` instead.

When you install with:

    pip install typer

\...it includes the same code and dependencies as:

    pip install "typer-slim[standard]"

The `standard` extra dependencies are `rich` and `shellingham`.

**Note**: The `typer` command is only included in the `typer` package.

## License[¶](#license "Permanent link")

This project is licensed under the terms of the MIT license.