# Source: https://rich.readthedocs.io/en/latest/reference/init.html

[]

# rich[](#module-rich "Link to this heading")

Rich text and beautiful formatting in the terminal.

[[rich.]][[get_console]][(][)][[[\[source\]]]](../_modules/rich.html#get_console)[](#rich.get_console "Link to this definition")

:   Get a global [[`Console`]](console.html#rich.console.Console "rich.console.Console") instance. This function is used when Rich requires a Console, and hasn't been explicitly given one.

    Returns[:]

    :   A console instance.

    Return type[:]

    :   [Console](console.html#rich.console.Console "rich.console.Console")

```
<!-- -->
```

[[rich.]][[inspect]][(]*[[obj]]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[title]][[=]][[None]]*, *[[help]][[=]][[False]]*, *[[methods]][[=]][[False]]*, *[[docs]][[=]][[True]]*, *[[private]][[=]][[False]]*, *[[dunder]][[=]][[False]]*, *[[sort]][[=]][[True]]*, *[[all]][[=]][[False]]*, *[[value]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich.html#inspect)[](#rich.inspect "Link to this definition")

:   Inspect any Python object.

    -   inspect(\<OBJECT\>) to see summarized info.

    -   inspect(\<OBJECT\>, methods=True) to see methods.

    -   inspect(\<OBJECT\>, help=True) to see full (non-abbreviated) help.

    -   inspect(\<OBJECT\>, private=True) to see private attributes (single underscore).

    -   inspect(\<OBJECT\>, dunder=True) to see attributes beginning with double underscore.

    -   inspect(\<OBJECT\>, all=True) to see all attributes.

    Parameters[:]

    :   -   **obj** (*Any*) -- An object to inspect.

        -   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Title to display over inspect result, or None use type. Defaults to None.

        -   **help** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show full help text rather than just first paragraph. Defaults to False.

        -   **methods** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable inspection of callables. Defaults to False.

        -   **docs** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also render doc strings. Defaults to True.

        -   **private** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show private attributes (beginning with underscore). Defaults to False.

        -   **dunder** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show attributes starting with double underscore. Defaults to False.

        -   **sort** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Sort attributes alphabetically. Defaults to True.

        -   **all** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show all attributes. Defaults to False.

        -   **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Pretty print value. Defaults to True.

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console") *\|* *None*)

    Return type[:]

    :   None

```
<!-- -->
```

[[rich.]][[print]][(]*[[\*]][[objects]]*, *[[sep]][[=]][[\'] [\']]*, *[[end]][[=]][[\'\\n\']]*, *[[file]][[=]][[None]]*, *[[flush]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich.html#print)[](#rich.print "Link to this definition")

:   Print object(s) supplied via positional arguments. This function has an identical signature to the built-in print. For more advanced features, see the [[`Console`]](console.html#rich.console.Console "rich.console.Console") class.

    Parameters[:]

    :   -   **sep** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Separator between printed objects. Defaults to " ".

        -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to write at end of output. Defaults to "\\n".

        -   **file** (*IO\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- File to write to, or None for stdout. Defaults to None.

        -   **flush** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Has no effect as Rich always flushes output. Defaults to False.

        -   **objects** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)"))

    Return type[:]

    :   None

```
<!-- -->
```

[[rich.]][[print_json]][(]*[[json]][[=]][[None]]*, *[[\*]]*, *[[data]][[=]][[None]]*, *[[indent]][[=]][[2]]*, *[[highlight]][[=]][[True]]*, *[[skip_keys]][[=]][[False]]*, *[[ensure_ascii]][[=]][[False]]*, *[[check_circular]][[=]][[True]]*, *[[allow_nan]][[=]][[True]]*, *[[default]][[=]][[None]]*, *[[sort_keys]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich.html#print_json)[](#rich.print_json "Link to this definition")

:   Pretty prints JSON. Output will be valid JSON.

    Parameters[:]

    :   -   **json** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing JSON.

        -   **data** (*Any*) -- If json is not supplied, then encode this data.

        -   **indent** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of spaces to indent. Defaults to 2.

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable highlighting of output: Defaults to True.

        -   **skip_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Skip keys not of a basic type. Defaults to False.

        -   **ensure_ascii** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Escape all non-ascii characters. Defaults to False.

        -   **check_circular** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Check for circular references. Defaults to True.

        -   **allow_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Allow NaN and Infinity values. Defaults to True.

        -   **default** (*Callable,* *optional*) -- A callable that converts values that can not be encoded in to something that can be JSON encoded. Defaults to None.

        -   **sort_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Sort dictionary keys. Defaults to False.

    Return type[:]

    :   None

```
<!-- -->
```

[[rich.]][[reconfigure]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/rich.html#reconfigure)[](#rich.reconfigure "Link to this definition")

:   Reconfigures the global console by replacing it with another.

    Parameters[:]

    :   -   **\*args** (*Any*) -- Positional arguments for the replacement [[`Console`]](console.html#rich.console.Console "rich.console.Console").

        -   **\*\*kwargs** (*Any*) -- Keyword arguments for the replacement [[`Console`]](console.html#rich.console.Console "rich.console.Console").

    Return type[:]

    :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).