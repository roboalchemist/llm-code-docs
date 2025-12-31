# Source: https://typer.tiangolo.com/tutorial/install/

# Install **Typer**[¶](#install-typer "Permanent link")

The first step is to install **Typer**.

First, make sure you create your [virtual environment](../../virtual-environments/), activate it, and then install it, for example with:

    $ pip install typer
    ---> 100%
    Successfully installed typer click shellingham rich

By default, `typer` comes with `rich` and `shellingham`.

Note

If you are an advanced user and want to opt out of these default extra dependencies, you can instead install `typer-slim`.

    pip install typer

\...includes the same optional dependencies as:

    pip install "typer-slim[standard]"