# Source: https://typer.tiangolo.com/tutorial/options/prompt/

# CLI Option Prompt[¶](#cli-option-prompt "Permanent link")

It\'s also possible to, instead of just showing an error, ask for the missing value with `prompt=True`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str, lastname: str = typer.Option(..., prompt=True)):
        print(f"Hello  ")

    if __name__ == "__main__":
        app()

And then your program will ask the user for it in the terminal:

    // Call it with the NAME CLI argument
    $ python main.py Camila

    // It asks for the missing CLI option --lastname
    # Lastname: $ Gutiérrez

    Hello Camila Gutiérrez

## Customize the prompt[¶](#customize-the-prompt "Permanent link")

You can also set a custom prompt, passing the string that you want to use instead of just `True`:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        name: str, lastname: str = typer.Option(..., prompt="Please tell me your last name")
    ):
        print(f"Hello  ")

    if __name__ == "__main__":
        app()

And then your program will ask for it using with your custom prompt:

    // Call it with the NAME CLI argument
    $ python main.py Camila

    // It uses the custom prompt
    # Please tell me your last name: $ Gutiérrez

    Hello Camila Gutiérrez

## Confirmation prompt[¶](#confirmation-prompt "Permanent link")

In some cases you could want to prompt for something and then ask the user to confirm it by typing it twice.

You can do it passing the parameter `confirmation_prompt=True`.

Let\'s say it\'s a CLI app to delete a project:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(project_name: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
        print(f"Deleting project ")

    if __name__ == "__main__":
        app()

And it will prompt the user for a value and then for the confirmation:

    $ python main.py

    // Your app will first prompt for the project name, and then for the confirmation
    # Project name: $ Old Project
    # Repeat for confirmation: $ Old Project

    Deleting project Old Project

    // If the user doesn't type the same, receives an error and a new prompt
    $ python main.py

    # Project name: $ Old Project
    # Repeat for confirmation: $ New Spice

    Error: The two entered values do not match

    # Project name: $ Old Project
    # Repeat for confirmation: $ Old Project

    Deleting project Old Project

    // Now it works 🎉