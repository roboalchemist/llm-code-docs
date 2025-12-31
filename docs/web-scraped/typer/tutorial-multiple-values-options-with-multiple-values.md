# Source: https://typer.tiangolo.com/tutorial/multiple-values/options-with-multiple-values/

# CLI Options with Multiple Values[¶](#cli-options-with-multiple-values "Permanent link")

You can also declare a *CLI option* that takes several values of different types.

You can set the number of values and types to anything you want, but it has to be a fixed number of values.

For this, use the standard Python `tuple`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(user: tuple[str, int, bool] = typer.Option((None, None, None))):
        username, coins, is_wizard = user
        if not username:
            print("No user provided")
            raise typer.Abort()
        print(f"The username  has  coins")
        if is_wizard:
            print("And this user is a wizard!")

    if __name__ == "__main__":
        app()

Each of the internal types defines the type of each value in the tuple.

So:

    user: tuple[str, int, bool]

means that the parameter `user` is a tuple of 3 values.

-   The first value is a `str`.
-   The second value is an `int`.
-   The third value is a `bool`.

Later we do:

    username, coins, is_wizard = user

If you hadn\'t seen that, it means that `user` is a tuple with 3 values, and we are assigning each of the values to a new variable:

-   The first value in the tuple `user` (a `str`) goes to the variable `username`.
-   The second value in the tuple `user` (an `int`) goes to the variable `coins`.
-   The third value in the tuple `user` (a `bool`) goes to the variable `is_wizard`.

So, this:

    username, coins, is_wizard = user

is equivalent to this:

    username = user[0]
    coins = user[1]
    is_wizard = user[2]

Tip

Notice that the default is a tuple with `(None, None, None)`.

You cannot simply use `None` here as the default because [Click doesn\'t support it](https://github.com/pallets/click/issues/472).

## Check it[¶](#check-it "Permanent link")

Now let\'s see how this works in the terminal:

    // check the help
    $ python main.py --help

    // Notice the &lt;TEXT INTEGER BOOLEAN&gt;
    Usage: main.py [OPTIONS]

    Options:
      --user &lt;TEXT INTEGER BOOLEAN&gt;...
      --help                          Show this message and exit.

    // Now try it
    $ python main.py --user Camila 50 yes

    The username Camila has 50 coins
    And this user is a wizard!

    // With other values
    $ python main.py --user Morty 3 no

    The username Morty has 3 coins

    // Try with invalid values (not enough)
    $ python main.py --user Camila 50

    Error: Option '--user' requires 3 arguments