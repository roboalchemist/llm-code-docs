# Source: https://rich.readthedocs.io/en/latest/reference/color.html

[]

# rich.color[](#module-rich.color "Link to this heading")

*[[class]][ ]*[[rich.color.]][[Color]][(]*[[name]]*, *[[type]]*, *[[number]][[=]][[None]]*, *[[triplet]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color)[](#rich.color.Color "Link to this definition")

:   Terminal color definition.

    Parameters[:]

    :   -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **type** ([*ColorType*](#rich.color.ColorType "rich.color.ColorType"))

        -   **number** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        -   **triplet** (*ColorTriplet* *\|* *None*)

    *[[classmethod]][ ]*[[default]][(][)][[[\[source\]]]](../_modules/rich/color.html#Color.default)[](#rich.color.Color.default "Link to this definition")

    :   Get a Color instance representing the default color.

        Returns[:]

        :   Default color.

        Return type[:]

        :   [Color](#rich.color.Color "rich.color.Color")

    [[downgrade]][(]*[[system]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.downgrade)[](#rich.color.Color.downgrade "Link to this definition")

    :   Downgrade a color system to a system with fewer colors.

        Parameters[:]

        :   **system** ([*ColorSystem*](#rich.color.ColorSystem "rich.color.ColorSystem"))

        Return type[:]

        :   [*Color*](#rich.color.Color "rich.color.Color")

    *[[classmethod]][ ]*[[from_ansi]][(]*[[number]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.from_ansi)[](#rich.color.Color.from_ansi "Link to this definition")

    :   Create a Color number from it's 8-bit ansi number.

        Parameters[:]

        :   **number** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- A number between 0-255 inclusive.

        Returns[:]

        :   A new Color instance.

        Return type[:]

        :   [Color](#rich.color.Color "rich.color.Color")

    *[[classmethod]][ ]*[[from_rgb]][(]*[[red]]*, *[[green]]*, *[[blue]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.from_rgb)[](#rich.color.Color.from_rgb "Link to this definition")

    :   Create a truecolor from three color components in the range(0-\>255).

        Parameters[:]

        :   -   **red** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Red component in range 0-255.

            -   **green** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Green component in range 0-255.

            -   **blue** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")) -- Blue component in range 0-255.

        Returns[:]

        :   A new color object.

        Return type[:]

        :   [Color](#rich.color.Color "rich.color.Color")

    *[[classmethod]][ ]*[[from_triplet]][(]*[[triplet]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.from_triplet)[](#rich.color.Color.from_triplet "Link to this definition")

    :   Create a truecolor RGB color from a triplet of values.

        Parameters[:]

        :   **triplet** (*ColorTriplet*) -- A color triplet containing red, green and blue components.

        Returns[:]

        :   A new color object.

        Return type[:]

        :   [Color](#rich.color.Color "rich.color.Color")

    [[get_ansi_codes]][(]*[[foreground]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.get_ansi_codes)[](#rich.color.Color.get_ansi_codes "Link to this definition")

    :   Get the ANSI escape codes for this color.

        Parameters[:]

        :   **foreground** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), ...\]

    [[get_truecolor]][(]*[[theme]][[=]][[None]]*, *[[foreground]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.get_truecolor)[](#rich.color.Color.get_truecolor "Link to this definition")

    :   Get an equivalent color triplet for this color.

        Parameters[:]

        :   -   **theme** (*TerminalTheme,* *optional*) -- Optional terminal theme, or None to use default. Defaults to None.

            -   **foreground** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- True for a foreground color, or False for background. Defaults to True.

        Returns[:]

        :   A color triplet containing RGB components.

        Return type[:]

        :   ColorTriplet

    *[[property]][ ]*[[is_default]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.color.Color.is_default "Link to this definition")

    :   Check if the color is a default color.

    *[[property]][ ]*[[is_system_defined]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.color.Color.is_system_defined "Link to this definition")

    :   Check if the color is ultimately defined by the system.

    [[name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.color.Color.name "Link to this definition")

    :   The name of the color (typically the input to Color.parse).

    [[number]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.color.Color.number "Link to this definition")

    :   The color number, if a standard color, or None.

    *[[classmethod]][ ]*[[parse]][(]*[[color]]*[)][[[\[source\]]]](../_modules/rich/color.html#Color.parse)[](#rich.color.Color.parse "Link to this definition")

    :   Parse a color definition.

        Parameters[:]

        :   **color** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        Return type[:]

        :   [*Color*](#rich.color.Color "rich.color.Color")

    *[[property]][ ]*[[system]]*[[:]][ ][[ColorSystem]](#rich.color.ColorSystem "rich.color.ColorSystem")*[](#rich.color.Color.system "Link to this definition")

    :   Get the native color system for this color.

    [[triplet]]*[[:]][ ][ColorTriplet][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.color.Color.triplet "Link to this definition")

    :   A triplet of color components, if an RGB color.

    [[type]]*[[:]][ ][[ColorType]](#rich.color.ColorType "rich.color.ColorType")*[](#rich.color.Color.type "Link to this definition")

    :   The type of the color.

```
<!-- -->
```

*[[exception]][ ]*[[rich.color.]][[ColorParseError]][[[\[source\]]]](../_modules/rich/color.html#ColorParseError)[](#rich.color.ColorParseError "Link to this definition")

:   The color could not be parsed.

```
<!-- -->
```

*[[class]][ ]*[[rich.color.]][[ColorSystem]][(]*[[\*]][[values]]*[)][[[\[source\]]]](../_modules/rich/color.html#ColorSystem)[](#rich.color.ColorSystem "Link to this definition")

:   One of the 3 color system supported by terminals.

```
<!-- -->
```

*[[class]][ ]*[[rich.color.]][[ColorType]][(]*[[\*]][[values]]*[)][[[\[source\]]]](../_modules/rich/color.html#ColorType)[](#rich.color.ColorType "Link to this definition")

:   Type of color stored in Color class.

```
<!-- -->
```

[[rich.color.]][[blend_rgb]][(]*[[color1]]*, *[[color2]]*, *[[cross_fade]][[=]][[0.5]]*[)][[[\[source\]]]](../_modules/rich/color.html#blend_rgb)[](#rich.color.blend_rgb "Link to this definition")

:   Blend one RGB color in to another.

    Parameters[:]

    :   -   **color1** (*ColorTriplet*)

        -   **color2** (*ColorTriplet*)

        -   **cross_fade** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"))

    Return type[:]

    :   *ColorTriplet*

```
<!-- -->
```

[[rich.color.]][[parse_rgb_hex]][(]*[[hex_color]]*[)][[[\[source\]]]](../_modules/rich/color.html#parse_rgb_hex)[](#rich.color.parse_rgb_hex "Link to this definition")

:   Parse six hex characters in to RGB triplet.

    Parameters[:]

    :   **hex_color** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    Return type[:]

    :   *ColorTriplet*

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).