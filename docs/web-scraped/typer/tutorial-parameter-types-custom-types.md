# Source: https://typer.tiangolo.com/tutorial/parameter-types/custom-types/

# Custom Types[¶](#custom-types "Permanent link")

You can easily use your own custom types in your **Typer** applications.

The way to do it is by providing a way to parse input into your own types.

There are two ways to achieve this:

-   Adding a type `parser`
-   Expanding Click\'s custom types

## Type Parser[¶](#type-parser "Permanent link")

`typer.Argument` and `typer.Option` can create custom parameter types with a `parser` callable.

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    class CustomClass:
        def __init__(self, value: str):
            self.value = value

        def __str__(self):
            return f"<CustomClass: value=>"

    def parse_custom_class(value: str):
        return CustomClass(value * 2)

    app = typer.Typer()

    @app.command()
    def main(
        custom_arg: CustomClass = typer.Argument(parser=parse_custom_class),
        custom_opt: CustomClass = typer.Option("Foo", parser=parse_custom_class),
    ):
        print(f"custom_arg is ")
        print(f"--custom-opt is ")

    if __name__ == "__main__":
        app()

The function (or callable) that you pass to the parameter `parser` will receive the input value as a string and should return the parsed value with your own custom type.

## Click Custom Type[¶](#click-custom-type "Permanent link")

If you already have a [Click Custom Type](https://click.palletsprojects.com/en/8.1.x/parameters/#implementing-custom-types), you can use it in `typer.Argument()` and `typer.Option()` with the `click_type` parameter.

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import click
    import typer

    class CustomClass:
        def __init__(self, value: str):
            self.value = value

        def __repr__(self):
            return f"<CustomClass: value=>"

    class CustomClassParser(click.ParamType):
        name = "CustomClass"

        def convert(self, value, param, ctx):
            return CustomClass(value * 3)

    app = typer.Typer()

    @app.command()
    def main(
        custom_arg: CustomClass = typer.Argument(click_type=CustomClassParser()),
        custom_opt: CustomClass = typer.Option("Foo", click_type=CustomClassParser()),
    ):
        print(f"custom_arg is ")
        print(f"--custom-opt is ")

    if __name__ == "__main__":
        app()