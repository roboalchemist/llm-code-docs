# Source: https://typer.tiangolo.com/tutorial/parameter-types/enum/

# Enum - Choices[¶](#enum-choices "Permanent link") 

To define a *CLI parameter* that can take a value from a predefined set of values you can use a standard Python [`enum.Enum`](https://docs.python.org/3/library/enum.html):

Python 3.9+

Tip

Notice that the function parameter `network` will be an `Enum`, not a `str`.

To get the `str` value in your function\'s code use `network.value`.

Check it:

    $ python main.py --help

    // Notice the predefined values [simple|conv|lstm]
    Usage: main.py [OPTIONS]

    Options:
      --network [simple|conv|lstm]  [default: simple]
      --help                        Show this message and exit.

    // Try it
    $ python main.py --network conv

    Training neural network of type: conv

    // Invalid value
    $ python main.py --network capsule

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: Invalid value for '--network': 'capsule' is not one of 'simple', 'conv', 'lstm'.

    // Note that enums are case sensitive by default
    $ python main.py --network CONV

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: Invalid value for '--network': 'CONV' is not one of 'simple', 'conv', 'lstm'.

### Case insensitive Enum choices[¶](#case-insensitive-enum-choices "Permanent link")

You can make an `Enum` (choice) *CLI parameter* be case-insensitive with the `case_sensitive` parameter:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    from enum import Enum

    import typer

    class NeuralNetwork(str, Enum):
        simple = "simple"
        conv = "conv"
        lstm = "lstm"

    app = typer.Typer()

    @app.command()
    def main(
        network: NeuralNetwork = typer.Option(NeuralNetwork.simple, case_sensitive=False),
    ):
        print(f"Training neural network of type: ")

    if __name__ == "__main__":
        app()

And then the values of the `Enum` will be checked no matter if lower case, upper case, or a mix:

    // Notice the upper case CONV
    $ python main.py --network CONV

    Training neural network of type: conv

    // A mix also works
    $ python main.py --network LsTm

    Training neural network of type: lstm

### List of Enum values[¶](#list-of-enum-values "Permanent link")

A *CLI parameter* can also take a list of `Enum` values:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    from enum import Enum

    import typer

    class Food(str, Enum):
        food_1 = "Eggs"
        food_2 = "Bacon"
        food_3 = "Cheese"

    app = typer.Typer()

    @app.command()
    def main(groceries: list[Food] = typer.Option([Food.food_1, Food.food_3])):
        print(f"Buying groceries: ")

    if __name__ == "__main__":
        app()

This works just like any other parameter value taking a list of things:

    $ python main.py --help

    // Notice the default values being shown
    Usage: main.py [OPTIONS]

    Options:
      --groceries [Eggs|Bacon|Cheese]  [default: Eggs, Cheese]
      --help                           Show this message and exit.

    // Try it with the default values
    $ python main.py

    Buying groceries: Eggs, Cheese

    // Try it with a single value
    $ python main.py --groceries "Eggs"

    Buying groceries: Eggs

    // Try it with multiple values
    $ python main.py --groceries "Eggs" --groceries "Bacon"

    Buying groceries: Eggs, Bacon

### Literal choices[¶](#literal-choices "Permanent link")

You can also use `Literal` to represent a set of possible predefined choices, without having to use an `Enum`:

Python 3.10+

🤓 Other versions and variants

Python 3.9+Python 3.10+ - non-AnnotatedPython 3.9+ - non-Annotated

    from typing import Literal

    import typer

    app = typer.Typer()

    @app.command()
    def main(network: Literal["simple", "conv", "lstm"] = typer.Option("simple")):
        print(f"Training neural network of type: ")

    if __name__ == "__main__":
        app()

    from typing import Literal

    import typer

    app = typer.Typer()

    @app.command()
    def main(network: Literal["simple", "conv", "lstm"] = typer.Option("simple")):
        print(f"Training neural network of type: ")

    if __name__ == "__main__":
        app()

    $ python main.py --help

    // Notice the predefined values [simple|conv|lstm]
    Usage: main.py [OPTIONS]

    Options:
      --network [simple|conv|lstm]  [default: simple]
      --help                        Show this message and exit.

    // Try it
    $ python main.py --network conv

    Training neural network of type: conv

    // Invalid value
    $ python main.py --network capsule

    Usage: main.py [OPTIONS]
    Try "main.py --help" for help.

    Error: Invalid value for '--network': 'capsule' is not one of 'simple', 'conv', 'lstm'.