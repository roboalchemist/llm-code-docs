# Source: https://rich.readthedocs.io/en/latest/reference/json.html

[]

# rich.json[](#module-rich.json "Link to this heading")

*[[class]][ ]*[[rich.json.]][[JSON]][(]*[[json]]*, *[[indent]][[=]][[2]]*, *[[highlight]][[=]][[True]]*, *[[skip_keys]][[=]][[False]]*, *[[ensure_ascii]][[=]][[False]]*, *[[check_circular]][[=]][[True]]*, *[[allow_nan]][[=]][[True]]*, *[[default]][[=]][[None]]*, *[[sort_keys]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/json.html#JSON)[](#rich.json.JSON "Link to this definition")

:   A renderable which pretty prints JSON.

    Parameters[:]

    :   -   **json** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- JSON encoded data.

        -   **indent** (*Union\[None,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Number of characters to indent by. Defaults to 2.

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable highlighting. Defaults to True.

        -   **skip_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Skip keys not of a basic type. Defaults to False.

        -   **ensure_ascii** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Escape all non-ascii characters. Defaults to False.

        -   **check_circular** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Check for circular references. Defaults to True.

        -   **allow_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Allow NaN and Infinity values. Defaults to True.

        -   **default** (*Callable,* *optional*) -- A callable that converts values that can not be encoded in to something that can be JSON encoded. Defaults to None.

        -   **sort_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Sort dictionary keys. Defaults to False.

    *[[classmethod]][ ]*[[from_data]][(]*[[data]]*, *[[indent]][[=]][[2]]*, *[[highlight]][[=]][[True]]*, *[[skip_keys]][[=]][[False]]*, *[[ensure_ascii]][[=]][[False]]*, *[[check_circular]][[=]][[True]]*, *[[allow_nan]][[=]][[True]]*, *[[default]][[=]][[None]]*, *[[sort_keys]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/json.html#JSON.from_data)[](#rich.json.JSON.from_data "Link to this definition")

    :   Encodes a JSON object from arbitrary data.

        Parameters[:]

        :   -   **data** (*Any*) -- An object that may be encoded in to JSON

            -   **indent** (*Union\[None,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Number of characters to indent by. Defaults to 2.

            -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable highlighting. Defaults to True.

            -   **default** (*Callable,* *optional*) -- Optional callable which will be called for objects that cannot be serialized. Defaults to None.

            -   **skip_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Skip keys not of a basic type. Defaults to False.

            -   **ensure_ascii** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Escape all non-ascii characters. Defaults to False.

            -   **check_circular** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Check for circular references. Defaults to True.

            -   **allow_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Allow NaN and Infinity values. Defaults to True.

            -   **default** -- A callable that converts values that can not be encoded in to something that can be JSON encoded. Defaults to None.

            -   **sort_keys** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Sort dictionary keys. Defaults to False.

        Returns[:]

        :   New JSON object from the given data.

        Return type[:]

        :   [JSON](#rich.json.JSON "rich.json.JSON")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).