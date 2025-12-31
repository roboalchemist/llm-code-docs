# Source: https://rich.readthedocs.io/en/latest/reference/markup.html

[]

# rich.markup[](#module-rich.markup "Link to this heading")

*[[class]][ ]*[[rich.markup.]][[Tag]][(]*[[name]]*, *[[parameters]]*[)][[[\[source\]]]](../_modules/rich/markup.html#Tag)[](#rich.markup.Tag "Link to this definition")

:   A tag in console markup.

    Parameters[:]

    :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **parameters** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *None*)

    *[[property]][ ]*[[markup]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.markup.Tag.markup "Link to this definition")

    :   Get the string representation of this tag.

    [[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.markup.Tag.name "Link to this definition")

    :   The tag name. e.g. 'bold'.

    [[parameters]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.markup.Tag.parameters "Link to this definition")

    :   Any additional parameters after the name.

```
<!-- -->
```

[[rich.markup.]][[escape]][(]*[[markup]]*, *[[\_escape=\<built-in] [method] [sub] [of] [re.Pattern] [object\>]]*[)][[[\[source\]]]](../_modules/rich/markup.html#escape)[](#rich.markup.escape "Link to this definition")

:   Escapes text so that it won't be interpreted as markup.

    Parameters[:]

    :   -   **markup** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Content to be inserted in to markup.

        -   **\_escape** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")*\[\[*[*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.13)")*\[\[*[*Match*](https://docs.python.org/3/library/typing.html#typing.Match "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]\],* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*)

    Returns[:]

    :   Markup with square brackets escaped.

    Return type[:]

    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

[[rich.markup.]][[render]][(]*[[markup]]*, *[[style]][[=]][[\'\']]*, *[[emoji]][[=]][[True]]*, *[[emoji_variant]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/markup.html#render)[](#rich.markup.render "Link to this definition")

:   Render console markup in to a Text instance.

    Parameters[:]

    :   -   **markup** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing console markup.

        -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style")) -- (Union\[str, Style\]): The style to use.

        -   **emoji** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also render emoji code. Defaults to True.

        -   **emoji_variant** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional emoji variant, either "text" or "emoji". Defaults to None.

    Raises[:]

    :   **MarkupError** -- If there is a syntax error in the markup.

    Returns[:]

    :   A test instance.

    Return type[:]

    :   [Text](text.html#rich.text.Text "rich.text.Text")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).