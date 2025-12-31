# Source: https://rich.readthedocs.io/en/latest/reference/style.html

[]

# rich.style[](#module-rich.style "Link to this heading")

*[[class]][ ]*[[rich.style.]][[Style]][(]*[[\*]]*, *[[color]][[=]][[None]]*, *[[bgcolor]][[=]][[None]]*, *[[bold]][[=]][[None]]*, *[[dim]][[=]][[None]]*, *[[italic]][[=]][[None]]*, *[[underline]][[=]][[None]]*, *[[blink]][[=]][[None]]*, *[[blink2]][[=]][[None]]*, *[[reverse]][[=]][[None]]*, *[[conceal]][[=]][[None]]*, *[[strike]][[=]][[None]]*, *[[underline2]][[=]][[None]]*, *[[frame]][[=]][[None]]*, *[[encircle]][[=]][[None]]*, *[[overline]][[=]][[None]]*, *[[link]][[=]][[None]]*, *[[meta]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style)[](#rich.style.Style "Link to this definition")

:   A terminal style.

    A terminal style consists of a color (color), a background color (bgcolor), and a number of attributes, such as bold, italic etc. The attributes have 3 states: they can either be on ([`True`]), off ([`False`]), or not set ([`None`]).

    Parameters[:]

    :   -   **color** (*Union\[*[*Color*](color.html#rich.color.Color "rich.color.Color")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Color of terminal text. Defaults to None.

        -   **bgcolor** (*Union\[*[*Color*](color.html#rich.color.Color "rich.color.Color")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Color of terminal background. Defaults to None.

        -   **bold** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable bold text. Defaults to None.

        -   **dim** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable dim text. Defaults to None.

        -   **italic** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable italic text. Defaults to None.

        -   **underline** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable underlined text. Defaults to None.

        -   **blink** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enabled blinking text. Defaults to None.

        -   **blink2** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable fast blinking text. Defaults to None.

        -   **reverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enabled reverse text. Defaults to None.

        -   **conceal** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable concealed text. Defaults to None.

        -   **strike** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable strikethrough text. Defaults to None.

        -   **underline2** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable doubly underlined text. Defaults to None.

        -   **frame** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable framed text. Defaults to None.

        -   **encircle** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable encircled text. Defaults to None.

        -   **overline** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable overlined text. Defaults to None.

        -   **link** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *link*) -- Link URL. Defaults to None.

        -   **meta** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")*\]* *\|* *None*)

    *[[property]][ ]*[[background_style]]*[[:]][ ][[Style]](#rich.style.Style "rich.style.Style")*[](#rich.style.Style.background_style "Link to this definition")

    :   A Style with background only.

    *[[property]][ ]*[[bgcolor]]*[[:]][ ][[Color]](color.html#rich.color.Color "rich.color.Color")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.style.Style.bgcolor "Link to this definition")

    :   The background color or None if it is not set.

    *[[classmethod]][ ]*[[chain]][(]*[[\*]][[styles]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.chain)[](#rich.style.Style.chain "Link to this definition")

    :   Combine styles from positional argument in to a single style.

        Parameters[:]

        :   **\*styles** (*Iterable\[*[*Style*](#rich.style.Style "rich.style.Style")*\]*) -- Styles to combine.

        Returns[:]

        :   A new style instance.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    [[clear_meta_and_links]][(][)][[[\[source\]]]](../_modules/rich/style.html#Style.clear_meta_and_links)[](#rich.style.Style.clear_meta_and_links "Link to this definition")

    :   Get a copy of this style with link and meta information removed.

        Returns[:]

        :   New style object.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    *[[property]][ ]*[[color]]*[[:]][ ][[Color]](color.html#rich.color.Color "rich.color.Color")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.style.Style.color "Link to this definition")

    :   The foreground color or None if it is not set.

    *[[classmethod]][ ]*[[combine]][(]*[[styles]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.combine)[](#rich.style.Style.combine "Link to this definition")

    :   Combine styles and get result.

        Parameters[:]

        :   **styles** (*Iterable\[*[*Style*](#rich.style.Style "rich.style.Style")*\]*) -- Styles to combine.

        Returns[:]

        :   A new style instance.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    [[copy]][(][)][[[\[source\]]]](../_modules/rich/style.html#Style.copy)[](#rich.style.Style.copy "Link to this definition")

    :   Get a copy of this style.

        Returns[:]

        :   A new Style instance with identical attributes.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    *[[classmethod]][ ]*[[from_color]][(]*[[color]][[=]][[None]]*, *[[bgcolor]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.from_color)[](#rich.style.Style.from_color "Link to this definition")

    :   Create a new style with colors and no attributes.

        Returns[:]

        :   A (foreground) color, or None for no color. Defaults to None. bgcolor (Optional\[Color\]): A (background) color, or None for no color. Defaults to None.

        Return type[:]

        :   color (Optional\[[Color](color.html#rich.color.Color "rich.color.Color")\])

        Parameters[:]

        :   -   **color** ([*Color*](color.html#rich.color.Color "rich.color.Color") *\|* *None*)

            -   **bgcolor** ([*Color*](color.html#rich.color.Color "rich.color.Color") *\|* *None*)

    *[[classmethod]][ ]*[[from_meta]][(]*[[meta]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.from_meta)[](#rich.style.Style.from_meta "Link to this definition")

    :   Create a new style with meta data.

        Returns[:]

        :   A dictionary of meta data. Defaults to None.

        Return type[:]

        :   meta (Optional\[Dict\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"), Any\]\])

        Parameters[:]

        :   **meta** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")*\]* *\|* *None*)

    [[get_html_style]][(]*[[theme]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.get_html_style)[](#rich.style.Style.get_html_style "Link to this definition")

    :   Get a CSS style rule.

        Parameters[:]

        :   **theme** (*TerminalTheme* *\|* *None*)

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    *[[property]][ ]*[[link]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.style.Style.link "Link to this definition")

    :   Link text, if set.

    *[[property]][ ]*[[link_id]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.style.Style.link_id "Link to this definition")

    :   Get a link id, used in ansi code for links.

    *[[property]][ ]*[[meta]]*[[:]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.13)")[[\]]]*[](#rich.style.Style.meta "Link to this definition")

    :   Get meta information (can not be changed after construction).

    *[[classmethod]][ ]*[[normalize]][(]*[[style]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.normalize)[](#rich.style.Style.normalize "Link to this definition")

    :   Normalize a style definition so that styles with the same effect have the same string representation.

        Parameters[:]

        :   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A style definition.

        Returns[:]

        :   Normal form of style definition.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    *[[classmethod]][ ]*[[null]][(][)][[[\[source\]]]](../_modules/rich/style.html#Style.null)[](#rich.style.Style.null "Link to this definition")

    :   Create an 'null' style, equivalent to Style(), but more performant.

        Return type[:]

        :   [*Style*](#rich.style.Style "rich.style.Style")

    *[[classmethod]][ ]*[[on]][(]*[[meta]][[=]][[None]]*, *[[\*\*]][[handlers]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.on)[](#rich.style.Style.on "Link to this definition")

    :   Create a blank style with meta information.

        Example

        style = Style.on(click=self.on_click)

        Parameters[:]

        :   -   **meta** (*Optional\[Dict\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Any\]\],* *optional*) -- An optional dict of meta information.

            -   **\*\*handlers** (*Any*) -- Keyword arguments are translated in to handlers.

        Returns[:]

        :   A Style with meta information attached.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    *[[classmethod]][ ]*[[parse]][(]*[[style_definition]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.parse)[](#rich.style.Style.parse "Link to this definition")

    :   Parse a style definition.

        Parameters[:]

        :   **style_definition** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing a style.

        Raises[:]

        :   **errors.StyleSyntaxError** -- If the style definition syntax is invalid.

        Returns[:]

        :   A Style instance.

        Return type[:]

        :   Style

    *[[classmethod]][ ]*[[pick_first]][(]*[[\*]][[values]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.pick_first)[](#rich.style.Style.pick_first "Link to this definition")

    :   Pick first non-None style.

        Parameters[:]

        :   **values** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](#rich.style.Style "rich.style.Style") *\|* *None*)

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \| [*Style*](#rich.style.Style "rich.style.Style")

    [[render]][(]*[[text]][[=]][[\'\']]*, *[[\*]]*, *[[color_system]][[=]][[ColorSystem.TRUECOLOR]]*, *[[legacy_windows]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.render)[](#rich.style.Style.render "Link to this definition")

    :   Render the ANSI codes for the style.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- A string to style. Defaults to "".

            -   **color_system** (*Optional\[*[*ColorSystem*](color.html#rich.color.ColorSystem "rich.color.ColorSystem")*\],* *optional*) -- Color system to render to. Defaults to ColorSystem.TRUECOLOR.

            -   **legacy_windows** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Returns[:]

        :   A string containing ANSI style codes.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[test]][(]*[[text]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.test)[](#rich.style.Style.test "Link to this definition")

    :   Write text with style directly to terminal.

        This method is for testing purposes only.

        Parameters[:]

        :   **text** (*Optional\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Text to style or None for style name.

        Return type[:]

        :   None

    *[[property]][ ]*[[transparent_background]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.style.Style.transparent_background "Link to this definition")

    :   Check if the style specified a transparent background.

    [[update_link]][(]*[[link]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/style.html#Style.update_link)[](#rich.style.Style.update_link "Link to this definition")

    :   Get a copy with a different value for link.

        Parameters[:]

        :   **link** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- New value for link. Defaults to None.

        Returns[:]

        :   A new Style instance.

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    *[[property]][ ]*[[without_color]]*[[:]][ ][[Style]](#rich.style.Style "rich.style.Style")*[](#rich.style.Style.without_color "Link to this definition")

    :   Get a copy of the style with color removed.

```
<!-- -->
```

*[[class]][ ]*[[rich.style.]][[StyleStack]][(]*[[default_style]]*[)][[[\[source\]]]](../_modules/rich/style.html#StyleStack)[](#rich.style.StyleStack "Link to this definition")

:   A stack of styles.

    Parameters[:]

    :   **default_style** ([*Style*](#rich.style.Style "rich.style.Style"))

    *[[property]][ ]*[[current]]*[[:]][ ][[Style]](#rich.style.Style "rich.style.Style")*[](#rich.style.StyleStack.current "Link to this definition")

    :   Get the Style at the top of the stack.

    [[pop]][(][)][[[\[source\]]]](../_modules/rich/style.html#StyleStack.pop)[](#rich.style.StyleStack.pop "Link to this definition")

    :   Pop last style and discard.

        Returns[:]

        :   New current style (also available as stack.current)

        Return type[:]

        :   [Style](#rich.style.Style "rich.style.Style")

    [[push]][(]*[[style]]*[)][[[\[source\]]]](../_modules/rich/style.html#StyleStack.push)[](#rich.style.StyleStack.push "Link to this definition")

    :   Push a new style on to the stack.

        Parameters[:]

        :   **style** ([*Style*](#rich.style.Style "rich.style.Style")) -- New style to combine with current style.

        Return type[:]

        :   None

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).