# Source: https://typer.tiangolo.com/tutorial/arguments/optional/

# Optional CLI Arguments[¶](#optional-cli-arguments "Permanent link")

We said before that *by default*:

-   *CLI options* are **optional**
-   *CLI arguments* are **required**

Again, that\'s how they work *by default*, and that\'s the convention in many CLI programs and systems.

But you can change that.

In fact, it\'s very common to have **optional** *CLI arguments*, it\'s way more common than having **required** *CLI options*.

As an example of how it could be useful, let\'s see how the `ls` CLI program works.

    // If you just type
    $ ls

    // ls will "list" the files and directories in the current directory
    typer  tests  README.md  LICENSE

    // But it also receives an optional CLI argument
    $ ls ./tests/

    // And then ls will list the files and directories inside of that directory from the CLI argument
    __init__.py  test_tutorial

## An alternative *CLI argument* declaration[¶](#an-alternative-cli-argument-declaration "Permanent link")

In the [First Steps](../../first-steps/#add-a-cli-argument) you saw how to add a *CLI argument*:

Python 3.9+

Now let\'s see an alternative way to create the same *CLI argument*:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    def main(name: str = typer.Argument()):
        print(f"Hello ")

    if __name__ == "__main__":
        typer.run(main)

Or, using an explicit `Typer()` instance creation:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument()):
        print(f"Hello ")

    if __name__ == "__main__":
        app()

Info

Typer added support for `Annotated` (and started recommending it) in version 0.9.0.

If you have an older version, you would get errors when trying to use `Annotated`.

Make sure you upgrade the Typer version to at least 0.9.0 before using `Annotated`.

Before, you had this function parameter:

    name: str

And now we wrap it with `Annotated`:

    name: Annotated[str]

Both of these versions mean the same thing, `Annotated` is part of standard Python and is there for this.

But the second version using `Annotated` allows us to pass additional metadata that can be used by **Typer**:

    name: Annotated[str, typer.Argument()]

Now we are being explicit that `name` is a *CLI argument*. It\'s still a `str` and it\'s still required (it doesn\'t have a default value).

All we did there achieves the same thing as before, a **required** *CLI argument*:

    $ python main.py

    Usage: main.py [OPTIONS] NAME
    Try "main.py --help" for help.

    Error: Missing argument 'NAME'.

It\'s still not very useful, but it works correctly.

And being able to declare a **required** *CLI argument* using

    name: Annotated[str, typer.Argument()]

\...that works exactly the same as

    name: str

\...will come handy later.

## Make an optional *CLI argument*[¶](#make-an-optional-cli-argument "Permanent link")

Now, finally what we came for, an optional *CLI argument*.

To make a *CLI argument* optional, use `typer.Argument()` and make sure to provide a \"default\" value, for example `"World"`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str = typer.Argument(default="World")):
        print(f"Hello !")

    if __name__ == "__main__":
        app()

Now we have:

    name: Annotated[str, typer.Argument()] = "World"

Because we are using `typer.Argument()` **Typer** will know that this is a *CLI argument* (no matter if *required* or *optional*).

Check the help:

    // First check the help
    $ python main.py --help

    Usage: main.py [OPTIONS] [NAME]

    Arguments:
      [NAME]

    Options:
      --help                Show this message and exit.

Tip

Notice that `NAME` is still a *CLI argument*, it\'s shown up there in the \"`Usage: main.py` \...\".

Also notice that now `[NAME]` has brackets (\"`[`\" and \"`]`\") around (before it was just `NAME`) to denote that it\'s **optional**, not **required**.

Now run it and test it:

    // With no CLI argument
    $ python main.py

    Hello World!

    // With one optional CLI argument
    $ python main.py Camila

    Hello Camila

Tip

Notice that \"`Camila`\" here is an optional *CLI argument*, not a *CLI option*, because we didn\'t use something like \"`--name Camila`\", we just passed \"`Camila`\" directly to the program.

## Alternative (old) `typer.Argument()` as the default value[¶](#alternative-old-typerargument-as-the-default-value "Permanent link") 

**Typer** also supports another older alternative syntax for declaring *CLI arguments* with additional metadata.

Instead of using `Annotated`, you can use `typer.Argument()` as the default value:

Python 3.9+ - non-Annotated

🤓 Other versions and variants

Python 3.9+

Tip

Prefer to use the `Annotated` version if possible.

Before, because `name` didn\'t have any default value it would be a **required parameter** for the Python function, in Python terms.

When using `typer.Argument()` as the default value **Typer** does the same and makes it a **required** *CLI argument*.

We changed it to:

    name: str = typer.Argument()

But now as `typer.Argument()` is the \"default value\" of the function\'s parameter, it would mean that \"it is no longer required\" (in Python terms).

As we no longer have the Python function default value (or its absence) to tell if something is required or not and what is the default value, `typer.Argument()` receives a first parameter `default` that serves the same purpose of defining that default value, or making it required.

Not passing any value to the `default` argument is the same as marking it as required. But you can also explicitly mark it as *required* by passing `...` as the `default` argument, passed to `typer.Argument(default=...)`.

    name: str = typer.Argument(default=...)

Info

If you hadn\'t seen that `...` before: it is a special single value, it is [part of Python and is called \"Ellipsis\"](https://docs.python.org/3/library/constants.html#Ellipsis).

Python 3.9+

And the same way, you can make it optional by passing a different `default` value, for example `"World"`:

Python 3.9+ - non-Annotated

🤓 Other versions and variants

Python 3.9+

Because the first parameter passed to `typer.Argument(default="World")` (the new \"default\" value) is `"World"`, **Typer** knows that this is an **optional** *CLI argument*, if no value is provided when calling it in the command line, it will have that default value of `"World"`.

The `default` argument is the first one, so it\'s possible that you see code that passes the value without explicitly using `default=`, like:

    name: str = typer.Argument(...)

\...or like:

    name: str = typer.Argument("World")

\...but again, try to use `Annotated` if possible, that way your code in terms of Python will mean the same thing as with **Typer** and you won\'t have to remember any of these details.