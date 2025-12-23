# Source: https://rich.readthedocs.io/en/latest/prompt.html

[Contents:]

-   [Introduction](introduction.html)
-   [Console API](console.html)
-   [Styles](style.html)
-   [Console Markup](markup.html)
-   [Rich Text](text.html)
-   [Highlighting](highlighting.html)
-   [Pretty Printing](pretty.html)
-   [Logging Handler](logging.html)
-   [Traceback](traceback.html)
-   [Prompt](#)
-   [Columns](columns.html)
-   [Render Groups](group.html)
-   [Markdown](markdown.html)
-   [Padding](padding.html)
-   [Panel](panel.html)
-   [Progress Display](progress.html)
-   [Syntax](syntax.html)
-   [Tables](tables.html)
-   [Tree](tree.html)
-   [Live Display](live.html)
-   [Layout](layout.html)
-   [Console Protocol](protocol.html)
-   [Reference](reference.html)
-   [Appendix](appendix.html)

[Rich](index.html)

# Prompt[](#prompt "Link to this heading")

Rich has a number of [[`Prompt`]](reference/prompt.html#rich.prompt.Prompt "rich.prompt.Prompt") classes which ask a user for input and loop until a valid response is received (they all use the [[Console API]](console.html#input) internally). Here's a simple example:

    >>> from rich.prompt import Prompt
    >>> name = Prompt.ask("Enter your name")

The prompt may be given as a string (which may contain [[Console Markup]](markup.html#console-markup) and emoji code) or as a [[`Text`]](reference/text.html#rich.text.Text "rich.text.Text") instance.

You can set a default value which will be returned if the user presses return without entering any text:

    >>> from rich.prompt import Prompt
    >>> name = Prompt.ask("Enter your name", default="Paul Atreides")

If you supply a list of choices, the prompt will loop until the user enters one of the choices:

    >>> from rich.prompt import Prompt
    >>> name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")

By default this is case sensitive, but you can set case_sensitive=False to make it case insensitive:

    >>> from rich.prompt import Prompt
    >>> name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul", case_sensitive=False)

Now, it would accept "paul" or "Paul" as valid responses.

In addition to [[`Prompt`]](reference/prompt.html#rich.prompt.Prompt "rich.prompt.Prompt") which returns strings, you can also use [[`IntPrompt`]](reference/prompt.html#rich.prompt.IntPrompt "rich.prompt.IntPrompt") which asks the user for an integer, and [[`FloatPrompt`]](reference/prompt.html#rich.prompt.FloatPrompt "rich.prompt.FloatPrompt") for floats.

The [[`Confirm`]](reference/prompt.html#rich.prompt.Confirm "rich.prompt.Confirm") class is a specialized prompt which may be used to ask the user a simple yes / no question. Here's an example:

    >>> from rich.prompt import Confirm
    >>> is_rich_great = Confirm.ask("Do you like rich?")
    >>> assert is_rich_great

The Prompt class was designed to be customizable via inheritance. See [prompt.py](https://github.com/willmcgugan/rich/blob/master/rich/prompt.py) for examples.

To see some of the prompts in action, run the following command from the command line:

    python -m rich.prompt

[[] Previous](traceback.html "Traceback") [Next []](columns.html "Columns")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).