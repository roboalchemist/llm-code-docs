# Source: https://typer.tiangolo.com/tutorial/options/callback-and-context/

# CLI Option Callback and Context[¶](#cli-option-callback-and-context "Permanent link")

In some occasions you might want to have some custom logic for a specific *CLI parameter* (for a *CLI option* or *CLI argument*) that is executed with the value received from the terminal.

In those cases you can use a *CLI parameter* callback function.

## Validate *CLI parameters*[¶](#validate-cli-parameters "Permanent link")

For example, you could do some validation before the rest of the code is executed.

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    def name_callback(value: str):
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: str | None = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    def name_callback(value: str):
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: Optional[str] = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Here you pass a function to `typer.Option()` or `typer.Argument()` with the keyword argument `callback`.

The function receives the value from the command line. It can do anything with it, and then return the value.

In this case, if the `--name` is not `Camila` we raise a `typer.BadParameter()` exception.

The `BadParameter` exception is special, it shows the error with the parameter that generated it.

Check it:

    $ python main.py --name Camila

    Hello Camila

    $ python main.py --name Rick

    Usage: main.py [OPTIONS]

    // We get the error from the callback
    Error: Invalid value for '--name': Only Camila is allowed

## Handling completion[¶](#handling-completion "Permanent link")

There\'s something to be aware of with callbacks and completion that requires some small special handling.

But first let\'s just use completion in your shell (Bash, Zsh, Fish, or PowerShell).

After installing completion (for your own Python package), when you use your CLI program and start adding a *CLI option* with `--` and then hit [TAB], your shell will show you the available *CLI options* (the same for *CLI arguments*, etc).

To check it quickly with the previous script use the `typer` command:

    // Hit the TAB key in your keyboard below where you see the: [TAB]
    $ typer ./main.py [TAB][TAB]

    // Depending on your terminal/shell you will get some completion like this ✨
    run    -- Run the provided Typer app.
    utils  -- Extra utility commands for Typer apps.

    // Then try with "run" and --help
    $ typer ./main.py run --help

    // You get a help text with your CLI options as you normally would
    Usage: typer run [OPTIONS]

      Run the provided Typer app.

    Options:
      --name TEXT  [required]
      --help       Show this message and exit.

    // Then try completion with your program
    $ typer ./main.py run --[TAB][TAB]

    // You get completion for CLI options
    --help  -- Show this message and exit.
    --name

    // And you can run it as if it was with Python directly
    $ typer ./main.py run --name Camila

    Hello Camila

### How shell completion works[¶](#how-shell-completion-works "Permanent link")

The way it works internally is that the shell/terminal will call your CLI program with some special environment variables (that hold the current *CLI parameters*, etc) and your CLI program will print some special values that the shell will use to present completion. All this is handled for you by **Typer** behind the scenes.

But the main **important point** is that it is all based on values printed by your program that the shell reads.

### Breaking completion in a callback[¶](#breaking-completion-in-a-callback "Permanent link")

Let\'s say that when the callback is running, we want to show a message saying that it\'s validating the name:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    def name_callback(value: str):
        print("Validating name")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: str | None = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    def name_callback(value: str):
        print("Validating name")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: Optional[str] = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

And because the callback will be called when the shell calls your program asking for completion, that message `"Validating name"` will be printed and it will break completion.

It will look something like:

    // Run it normally
    $ typer ./main.py run --name Camila

    // See the extra message "Validating name"
    Validating name
    Hello Camila

    $ typer ./main.py run --[TAB][TAB]

    // Some weird broken error message ⛔️
    (eval):1: command not found: Validating
    rutyper ./main.pyed Typer app.

### Fix completion - using the `Context`[¶](#fix-completion-using-the-context "Permanent link") 

When you create a **Typer** application it uses Click underneath.

And every Click application has a special object called a [\"Context\"](https://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts) that is normally hidden.

But you can access the context by declaring a function parameter of type `typer.Context`.

The \"context\" has some additional data about the current execution of your program:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    def name_callback(ctx: typer.Context, value: str):
        if ctx.resilient_parsing:
            return
        print("Validating name")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: str | None = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    def name_callback(ctx: typer.Context, value: str):
        if ctx.resilient_parsing:
            return
        print("Validating name")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: Optional[str] = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

The `ctx.resilient_parsing` will be `True` when handling completion, so you can just return without printing anything else.

But it will be `False` when calling the program normally. So you can continue the execution of your previous code.

That\'s all is needed to fix completion. 🚀

Check it:

    $ typer ./main.py run --[TAB][TAB]

    // Now it works correctly 🎉
    --help  -- Show this message and exit.
    --name

    // And you can call it normally
    $ typer ./main.py run --name Camila

    Validating name
    Hello Camila

## Using the `CallbackParam` object[¶](#using-the-callbackparam-object "Permanent link")

The same way you can access the `typer.Context` by declaring a function parameter with its value, you can declare another function parameter with type `typer.CallbackParam` to get the specific Click `Parameter` object.

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    def name_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
        if ctx.resilient_parsing:
            return
        print(f"Validating param: ")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: str | None = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

    from typing import Optional

    import typer

    app = typer.Typer()

    def name_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
        if ctx.resilient_parsing:
            return
        print(f"Validating param: ")
        if value != "Camila":
            raise typer.BadParameter("Only Camila is allowed")
        return value

    @app.command()
    def main(name: Optional[str] = typer.Option(default=None, callback=name_callback)):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

It\'s probably not very common, but you could do it if you need it.

For example if you had a callback that could be used by several *CLI parameters*, that way the callback could know which parameter is each time.

Check it:

    $ python main.py --name Camila

    Validating param: name
    Hello Camila

## Technical Details[¶](#technical-details "Permanent link")

Because you get the relevant data in the callback function based on standard Python type annotations, you get type checks and autocompletion in your editor for free.

And **Typer** will make sure you get the function parameters you want.

You don\'t have to worry about their names, their order, etc.

As it\'s based on standard Python types, it \"**just works**\". ✨

### Click\'s `Parameter`[¶](#clicks-parameter "Permanent link")

The `typer.CallbackParam` is actually just a sub-class of Click\'s [`Parameter`](https://click.palletsprojects.com/en/7.x/api/#click.Parameter), so you get all the right completion in your editor.

### Callback with type annotations[¶](#callback-with-type-annotations "Permanent link")

You can get the `typer.Context` and the `typer.CallbackParam` simply by declaring a function parameter of each type.

The order doesn\'t matter, the name of the function parameters doesn\'t matter.

You could also get only the `typer.CallbackParam` and not the `typer.Context`, or vice versa, it will still work.

### `value` function parameter[¶](#value-function-parameter "Permanent link")

The `value` function parameter in the callback can also have any name (e.g. `lastname`) and any type, but it should have the same type annotation as in the main function, because that\'s what it will receive.

It\'s also possible to not declare its type. It will still work.

And it\'s possible to not declare the `value` parameter at all, and, for example, only get the `typer.Context`. That will also work.