# Source: https://typer.tiangolo.com/tutorial/options/password/

# Password CLI Option and Confirmation Prompt[¶](#password-cli-option-and-confirmation-prompt "Permanent link")

Apart from having a prompt, you can make a *CLI option* have a `confirmation_prompt=True`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str, email: str = typer.Option(..., prompt=True, confirmation_prompt=True)
    ):
        print(f"Hello , your email is ")

    if __name__ == "__main__":
        app()

And the CLI program will ask for confirmation:

    $ python main.py Camila

    // It prompts for the email
    # Email: $ camila@example.com
    # Repeat for confirmation: $ camila@example.com

    Hello Camila, your email is camila@example.com

## A Password prompt[¶](#a-password-prompt "Permanent link")

When receiving a password, it is very common (in most shells) to not show anything on the screen while typing the password.

The program will still receive the password, but nothing will be shown on screen, not even `****`.

You can achieve the same using `hide_input=True`.

And if you combine it with `confirmation_prompt=True` you can easily receive a password with double confirmation:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str,
        password: str = typer.Option(
            ..., prompt=True, confirmation_prompt=True, hide_input=True
        ),
    ):
        print(f"Hello . Doing something very secure with password.")
        print(f"...just kidding, here it is, very insecure: ")

    if __name__ == "__main__":
        app()

Check it:

    $ python main.py Camila

    // It prompts for the password, but doesn't show anything when you type
    # Password: $
    # Repeat for confirmation: $

    // Let's imagine the password typed was "typerrocks"
    Hello Camila. Doing something very secure with password.
    ...just kidding, here it is, very insecure: typerrocks