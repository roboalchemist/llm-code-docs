# Source: https://rich.readthedocs.io/en/latest/reference/protocol.html

[]

# rich.protocol[](#module-rich.protocol "Link to this heading")

[[rich.protocol.]][[is_renderable]][(]*[[check_object]]*[)][[[\[source\]]]](../_modules/rich/protocol.html#is_renderable)[](#rich.protocol.is_renderable "Link to this definition")

:   Check if an object may be rendered by Rich.

    Parameters[:]

    :   **check_object** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"))

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

[[rich.protocol.]][[rich_cast]][(]*[[renderable]]*[)][[[\[source\]]]](../_modules/rich/protocol.html#rich_cast)[](#rich.protocol.rich_cast "Link to this definition")

:   Cast an object to a renderable by calling \_\_rich\_\_ if present.

    Parameters[:]

    :   **renderable** ([*object*](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")) -- A potentially renderable object

    Returns[:]

    :   The result of recursively calling \_\_rich\_\_.

    Return type[:]

    :   [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).