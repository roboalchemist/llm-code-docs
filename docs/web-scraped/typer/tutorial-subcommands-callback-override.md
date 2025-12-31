# Source: https://typer.tiangolo.com/tutorial/subcommands/callback-override/

# Sub-Typer Callback Override[¶](#sub-typer-callback-override "Permanent link")

When creating a **Typer** app you can define a callback function, it always executes and defines the *CLI arguments* and *CLI options* that go before a command.

When adding a Typer app inside of another, the sub-Typer can also have its own callback.

It can handle any *CLI parameters* that go before its own commands and execute any extra code:

Python 3.9+

In this case it doesn\'t define any *CLI parameters*, it just writes a message.

Check it:

    $ python main.py users create Camila

    // Notice the first message is not created by the command function but by the callback
    Running a users command
    Creating user: Camila

## Add a callback on creation[¶](#add-a-callback-on-creation "Permanent link")

It\'s also possible to add a callback when creating the `typer.Typer()` app that will be added to another Typer app:

Python 3.9+

This achieves exactly the same as above, it\'s just another place to add the callback.

Check it:

    $ python main.py users create Camila

    Running a users command
    Creating user: Camila

## Overriding the callback on creation[¶](#overriding-the-callback-on-creation "Permanent link")

If a callback was added when creating the `typer.Typer()` app, it\'s possible to override it with a new one using `@app.callback()`.

This is the same information you saw on the section about [Commands - Typer Callback](../../commands/callback/), and it applies the same for sub-Typer apps:

Python 3.9+

Here we had defined a callback when creating the `typer.Typer()` sub-app, but then we override it with a new callback with the function `user_callback()`.

As `@app.callback()` takes precedence over `typer.Typer(callback=some_function)`, now our CLI app will use this new callback.

Check it:

    $ python main.py users create Camila

    // Notice the message from the new callback
    Callback override, running users command
    Creating user: Camila

## Overriding the callback when adding a sub-Typer[¶](#overriding-the-callback-when-adding-a-sub-typer "Permanent link")

Lastly, you can override the callback defined anywhere else when adding a sub-Typer with `app.add_typer()` using the `callback` parameter.

This has the highest priority:

Python 3.9+

Notice that the precedence goes to `app.add_typer()` and is not affected by the order of execution. There\'s another callback defined below, but the one from `app.add_typer()` wins.

Now when you use the CLI program it will use the new callback function `callback_for_add_typer()`.

Check it:

    $ python users create Camila

    // Notice the message from the callback added in add_typer()
    I have the high land! Running users command
    Creating user: Camila