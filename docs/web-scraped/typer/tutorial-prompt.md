# Source: https://typer.tiangolo.com/tutorial/prompt/

# Ask with Prompt[¶](#ask-with-prompt "Permanent link")

When you need to ask the user for info interactively you should normally use [\*CLI Option\*s with Prompt](../options/prompt/), because they allow using the CLI program in a non-interactive way (for example, a Bash script could use it).

But if you absolutely need to ask for interactive information without using a *CLI option*, you can use `typer.prompt()`:

Python 3.9+

Check it:

    $ python main.py

    # What's your name?:$ Camila

    Hello Camila

## Confirm[¶](#confirm "Permanent link")

There\'s also an alternative to ask for confirmation. Again, if possible, you should use a [*CLI Option* with a confirmation prompt](../options/prompt/):

Python 3.9+

Check it:

    $ python main.py

    # Are you sure you want to delete it? [y/N]:$ y

    Deleting it!

    // This time cancel it
    $ python main.py

    # Are you sure you want to delete it? [y/N]:$ n

    Not deleting
    Aborted!

## Confirm or abort[¶](#confirm-or-abort "Permanent link")

As it\'s very common to abort if the user doesn\'t confirm, there\'s an integrated parameter `abort` that does it automatically:

Python 3.9+

    $ python main.py

    # Are you sure you want to delete it? [y/N]:$ y

    Deleting it!

    // This time cancel it
    $ python main.py

    # Are you sure you want to delete it? [y/N]:$ n

    Aborted!

## Prompt with Rich[¶](#prompt-with-rich "Permanent link")

If you installed Rich as described in [Printing and Colors](../printing/), you can use Rich to prompt the user for input:

Python 3.9+

And when you run it, it will look like:

    $ python main.py

    # Enter your name 😎:$ Morty

    Hello Morty