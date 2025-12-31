# Source: https://rich.readthedocs.io/en/latest/reference/theme.html

[]

# rich.theme[](#module-rich.theme "Link to this heading")

*[[class]][ ]*[[rich.theme.]][[Theme]][(]*[[styles]][[=]][[None]]*, *[[inherit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/theme.html#Theme)[](#rich.theme.Theme "Link to this definition")

:   A container for style information, used by [[`Console`]](console.html#rich.console.Console "rich.console.Console").

    Parameters[:]

    :   -   **styles** (*Dict\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- A mapping of style names on to styles. Defaults to None for a theme with no styles.

        -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Inherit default styles. Defaults to True.

    *[[property]][ ]*[[config]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.theme.Theme.config "Link to this definition")

    :   Get contents of a config file for this theme.

    *[[classmethod]][ ]*[[from_file]][(]*[[config_file]]*, *[[source]][[=]][[None]]*, *[[inherit]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/theme.html#Theme.from_file)[](#rich.theme.Theme.from_file "Link to this definition")

    :   Load a theme from a text mode file.

        Parameters[:]

        :   -   **config_file** (*IO\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- An open conf file.

            -   **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- The filename of the open file. Defaults to None.

            -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Inherit default styles. Defaults to True.

        Returns[:]

        :   A New theme instance.

        Return type[:]

        :   [Theme](#rich.theme.Theme "rich.theme.Theme")

    *[[classmethod]][ ]*[[read]][(]*[[path]]*, *[[inherit]][[=]][[True]]*, *[[encoding]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/theme.html#Theme.read)[](#rich.theme.Theme.read "Link to this definition")

    :   Read a theme from a path.

        Parameters[:]

        :   -   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Path to a config file readable by Python configparser module.

            -   **inherit** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Inherit default styles. Defaults to True.

            -   **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Encoding of the config file. Defaults to None.

        Returns[:]

        :   A new theme instance.

        Return type[:]

        :   [Theme](#rich.theme.Theme "rich.theme.Theme")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).