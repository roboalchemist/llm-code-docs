# Source: https://rich.readthedocs.io/en/latest/reference/pretty.html

[]

# rich.pretty[](#module-rich.pretty "Link to this heading")

*[[class]][ ]*[[rich.pretty.]][[Node]][(]*[[key_repr]][[=]][[\'\']]*, *[[value_repr]][[=]][[\'\']]*, *[[open_brace]][[=]][[\'\']]*, *[[close_brace]][[=]][[\'\']]*, *[[empty]][[=]][[\'\']]*, *[[last]][[=]][[False]]*, *[[is_tuple]][[=]][[False]]*, *[[is_namedtuple]][[=]][[False]]*, *[[children]][[=]][[None]]*, *[[key_separator]][[=]][[\':] [\']]*, *[[separator]][[=]][[\',] [\']]*[)][[[\[source\]]]](../_modules/rich/pretty.html#Node)[](#rich.pretty.Node "Link to this definition")

:   A node in a repr tree. May be atomic or a container.

    Parameters[:]

    :   -   **key_repr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **value_repr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **open_brace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **close_brace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **empty** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **last** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **is_tuple** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **is_namedtuple** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **children** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Node*](#rich.pretty.Node "rich.pretty.Node")*\]* *\|* *None*)

        -   **key_separator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **separator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    [[check_length]][(]*[[start_length]]*, *[[max_length]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#Node.check_length)[](#rich.pretty.Node.check_length "Link to this definition")

    :   Check the length fits within a limit.

        Parameters[:]

        :   -   **start_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Starting length of the line (indent, prefix, suffix).

            -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum length.

        Returns[:]

        :   True if the node can be rendered within max length, otherwise False.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[iter_tokens]][(][)][[[\[source\]]]](../_modules/rich/pretty.html#Node.iter_tokens)[](#rich.pretty.Node.iter_tokens "Link to this definition")

    :   Generate tokens for this node.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")\]

    [[render]][(]*[[max_width]][[=]][[80]]*, *[[indent_size]][[=]][[4]]*, *[[expand_all]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#Node.render)[](#rich.pretty.Node.render "Link to this definition")

    :   Render the node to a pretty repr.

        Parameters[:]

        :   -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum width of the repr. Defaults to 80.

            -   **indent_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Size of indents. Defaults to 4.

            -   **expand_all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand all levels. Defaults to False.

        Returns[:]

        :   A repr string of the original object.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.pretty.]][[Pretty]][(]*[[\_object]]*, *[[highlighter]][[=]][[None]]*, *[[\*]]*, *[[indent_size]][[=]][[4]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[False]]*, *[[indent_guides]][[=]][[False]]*, *[[max_length]][[=]][[None]]*, *[[max_string]][[=]][[None]]*, *[[max_depth]][[=]][[None]]*, *[[expand_all]][[=]][[False]]*, *[[margin]][[=]][[0]]*, *[[insert_line]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#Pretty)[](#rich.pretty.Pretty "Link to this definition")

:   A rich renderable that pretty prints an object.

    Parameters[:]

    :   -   **\_object** (*Any*) -- An object to pretty print.

        -   **highlighter** (*HighlighterType,* *optional*) -- Highlighter object to apply to result, or None for ReprHighlighter. Defaults to None.

        -   **indent_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of spaces in indent. Defaults to 4.

        -   **justify** (*JustifyMethod,* *optional*) -- Justify method, or None for default. Defaults to None.

        -   **overflow** (*OverflowMethod,* *optional*) -- Overflow method, or None for default. Defaults to None.

        -   **no_wrap** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Disable word wrapping. Defaults to False.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indentation guides. Defaults to False.

        -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to None.

        -   **max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to None.

        -   **max_depth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum depth of nested data structures, or None for no maximum. Defaults to None.

        -   **expand_all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand all containers. Defaults to False.

        -   **margin** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Subtrace a margin from width to force containers to expand earlier. Defaults to 0.

        -   **insert_line** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Insert a new line if the output has multiple new lines. Defaults to False.

```
<!-- -->
```

[[rich.pretty.]][[install]][(]*[[console]][[=]][[None]]*, *[[overflow]][[=]][[\'ignore\']]*, *[[crop]][[=]][[False]]*, *[[indent_guides]][[=]][[False]]*, *[[max_length]][[=]][[None]]*, *[[max_string]][[=]][[None]]*, *[[max_depth]][[=]][[None]]*, *[[expand_all]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#install)[](#rich.pretty.install "Link to this definition")

:   Install automatic pretty printing in the Python REPL.

    Parameters[:]

    :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console instance or [`None`] to use global console. Defaults to None.

        -   **overflow** (*Optional\[OverflowMethod\],* *optional*) -- Overflow method. Defaults to "ignore".

        -   **crop** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Enable cropping of long lines. Defaults to False.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indentation guides. Defaults to False.

        -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to None.

        -   **max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable. Defaults to None.

        -   **max_depth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum depth of nested data structures, or None for no maximum. Defaults to None.

        -   **expand_all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand all containers. Defaults to False.

        -   **max_frames** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

    Return type[:]

    :   None

```
<!-- -->
```

[[rich.pretty.]][[is_expandable]][(]*[[obj]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#is_expandable)[](#rich.pretty.is_expandable "Link to this definition")

:   Check if an object may be expanded by pretty print.

    Parameters[:]

    :   **obj** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"))

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

[[rich.pretty.]][[pprint]][(]*[[\_object]]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[indent_guides]][[=]][[True]]*, *[[max_length]][[=]][[None]]*, *[[max_string]][[=]][[None]]*, *[[max_depth]][[=]][[None]]*, *[[expand_all]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#pprint)[](#rich.pretty.pprint "Link to this definition")

:   A convenience function for pretty printing.

    Parameters[:]

    :   -   **\_object** (*Any*) -- Object to pretty print.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- Console instance, or None to use default. Defaults to None.

        -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to None.

        -   **max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of strings before truncating, or None to disable. Defaults to None.

        -   **max_depth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum depth for nested data structures, or None for unlimited depth. Defaults to None.

        -   **indent_guides** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable indentation guides. Defaults to True.

        -   **expand_all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand all containers. Defaults to False.

    Return type[:]

    :   None

```
<!-- -->
```

[[rich.pretty.]][[pretty_repr]][(]*[[\_object]]*, *[[\*]]*, *[[max_width]][[=]][[80]]*, *[[indent_size]][[=]][[4]]*, *[[max_length]][[=]][[None]]*, *[[max_string]][[=]][[None]]*, *[[max_depth]][[=]][[None]]*, *[[expand_all]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#pretty_repr)[](#rich.pretty.pretty_repr "Link to this definition")

:   Prettify repr string by expanding on to new lines to fit within a given width.

    Parameters[:]

    :   -   **\_object** (*Any*) -- Object to repr.

        -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Desired maximum width of repr string. Defaults to 80.

        -   **indent_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of spaces to indent. Defaults to 4.

        -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to None.

        -   **max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable truncating. Defaults to None.

        -   **max_depth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum depth of nested data structure, or None for no depth. Defaults to None.

        -   **expand_all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand all containers regardless of available width. Defaults to False.

    Returns[:]

    :   A possibly multi-line representation of the object.

    Return type[:]

    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

[[rich.pretty.]][[traverse]][(]*[[\_object]]*, *[[max_length]][[=]][[None]]*, *[[max_string]][[=]][[None]]*, *[[max_depth]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/pretty.html#traverse)[](#rich.pretty.traverse "Link to this definition")

:   Traverse object and generate a tree.

    Parameters[:]

    :   -   **\_object** (*Any*) -- Object to be traversed.

        -   **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of containers before abbreviating, or None for no abbreviation. Defaults to None.

        -   **max_string** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum length of string before truncating, or None to disable truncating. Defaults to None.

        -   **max_depth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Maximum depth of data structures, or None for no maximum. Defaults to None.

    Returns[:]

    :   The root of a tree structure which can be used to render a pretty repr.

    Return type[:]

    :   [Node](#rich.pretty.Node "rich.pretty.Node")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).