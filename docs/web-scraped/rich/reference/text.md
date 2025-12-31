# Source: https://rich.readthedocs.io/en/latest/reference/text.html

[]

# rich.text[](#module-rich.text "Link to this heading")

*[[class]][ ]*[[rich.text.]][[Text]][(]*[[text]][[=]][[\'\']]*, *[[style]][[=]][[\'\']]*, *[[\*]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[None]]*, *[[end]][[=]][[\'\\n\']]*, *[[tab_size]][[=]][[None]]*, *[[spans]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text)[](#rich.text.Text "Link to this definition")

:   Text with color / style.

    Parameters[:]

    :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Default unstyled text. Defaults to "".

        -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Base style for text. Defaults to "".

        -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "left", "center", "full", "right". Defaults to None.

        -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to None.

        -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable text wrapping, or None for default. Defaults to None.

        -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to end text with. Defaults to "\\n".

        -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of spaces per tab, or [`None`] to use [`console.tab_size`]. Defaults to None.

        -   **spans** (*List\[Span\],* *optional*)

    [[align]][(]*[[align]]*, *[[width]]*, *[[character]][[=]][[\'] [\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.align)[](#rich.text.Text.align "Link to this definition")

    :   Align text to a given width.

        Parameters[:]

        :   -   **align** (*AlignMethod*) -- One of "left", "center", or "right".

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Desired width.

            -   **character** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to pad with. Defaults to " ".

        Return type[:]

        :   None

    [[append]][(]*[[text]]*, *[[style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.append)[](#rich.text.Text.append "Link to this definition")

    :   Add text with an optional style.

        Parameters[:]

        :   -   **text** (*Union\[*[*Text*](#rich.text.Text "rich.text.Text")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- A str or Text to append.

            -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- A style name. Defaults to None.

        Returns[:]

        :   Returns self for chaining.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[append_text]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.append_text)[](#rich.text.Text.append_text "Link to this definition")

    :   Append another Text instance. This method is more performant that Text.append, but only works for Text.

        Parameters[:]

        :   **text** ([*Text*](#rich.text.Text "rich.text.Text")) -- The Text instance to append to this instance.

        Returns[:]

        :   Returns self for chaining.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[append_tokens]][(]*[[tokens]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.append_tokens)[](#rich.text.Text.append_tokens "Link to this definition")

    :   Append iterable of str and style. Style may be a Style instance or a str style definition.

        Parameters[:]

        :   **tokens** (*Iterable\[Tuple\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Optional\[StyleType\]\]\]*) -- An iterable of tuples containing str content and style.

        Returns[:]

        :   Returns self for chaining.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[apply_meta]][(]*[[meta]]*, *[[start]][[=]][[0]]*, *[[end]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.apply_meta)[](#rich.text.Text.apply_meta "Link to this definition")

    :   Apply metadata to the text, or a portion of the text.

        Parameters[:]

        :   -   **meta** (*Dict\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Any\]*) -- A dict of meta information.

            -   **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Start offset (negative indexing is supported). Defaults to 0.

            -   **end** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- End offset (negative indexing is supported), or None for end of text. Defaults to None.

        Return type[:]

        :   None

    *[[classmethod]][ ]*[[assemble]][(]*[[\*]][[parts]]*, *[[style]][[=]][[\'\']]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[None]]*, *[[end]][[=]][[\'\\n\']]*, *[[tab_size]][[=]][[8]]*, *[[meta]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.assemble)[](#rich.text.Text.assemble "Link to this definition")

    :   Construct a text instance by combining a sequence of strings with optional styles. The positional arguments should be either strings, or a tuple of string + style.

        Parameters[:]

        :   -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Base style for text. Defaults to "".

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "left", "center", "full", "right". Defaults to None.

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to None.

            -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable text wrapping, or None for default. Defaults to None.

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to end text with. Defaults to "\\n".

            -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of spaces per tab, or [`None`] to use [`console.tab_size`]. Defaults to None.

            -   **meta** (*Dict\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Any\],* *optional*)

            -   **parts** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](#rich.text.Text "rich.text.Text") *\|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style")*\]*)

        Returns[:]

        :   A new text instance.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[blank_copy]][(]*[[plain]][[=]][[\'\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.blank_copy)[](#rich.text.Text.blank_copy "Link to this definition")

    :   Return a new Text instance with copied metadata (but not the string or spans).

        Parameters[:]

        :   **plain** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        Return type[:]

        :   [*Text*](#rich.text.Text "rich.text.Text")

    *[[property]][ ]*[[cell_len]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.text.Text.cell_len "Link to this definition")

    :   Get the number of cells required to render this text.

    [[copy]][(][)][[[\[source\]]]](../_modules/rich/text.html#Text.copy)[](#rich.text.Text.copy "Link to this definition")

    :   Return a copy of this instance.

        Return type[:]

        :   [*Text*](#rich.text.Text "rich.text.Text")

    [[copy_styles]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.copy_styles)[](#rich.text.Text.copy_styles "Link to this definition")

    :   Copy styles from another Text instance.

        Parameters[:]

        :   **text** ([*Text*](#rich.text.Text "rich.text.Text")) -- A Text instance to copy styles from, must be the same length.

        Return type[:]

        :   None

    [[detect_indentation]][(][)][[[\[source\]]]](../_modules/rich/text.html#Text.detect_indentation)[](#rich.text.Text.detect_indentation "Link to this definition")

    :   Auto-detect indentation of code.

        Returns[:]

        :   Number of spaces used to indent code.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    [[divide]][(]*[[offsets]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.divide)[](#rich.text.Text.divide "Link to this definition")

    :   Divide text in to a number of lines at given offsets.

        Parameters[:]

        :   **offsets** (*Iterable\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- Offsets used to divide text.

        Returns[:]

        :   New RichText instances between offsets.

        Return type[:]

        :   Lines

    [[expand_tabs]][(]*[[tab_size]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.expand_tabs)[](#rich.text.Text.expand_tabs "Link to this definition")

    :   Converts tabs to spaces.

        Parameters[:]

        :   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Size of tabs. Defaults to 8.

        Return type[:]

        :   None

    [[extend_style]][(]*[[spaces]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.extend_style)[](#rich.text.Text.extend_style "Link to this definition")

    :   Extend the Text given number of spaces where the spaces have the same style as the last character.

        Parameters[:]

        :   **spaces** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of spaces to add to the Text.

        Return type[:]

        :   None

    [[fit]][(]*[[width]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.fit)[](#rich.text.Text.fit "Link to this definition")

    :   Fit the text in to given width by chopping in to lines.

        Parameters[:]

        :   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum characters in a line.

        Returns[:]

        :   Lines container.

        Return type[:]

        :   Lines

    *[[classmethod]][ ]*[[from_ansi]][(]*[[text]]*, *[[\*]]*, *[[style]][[=]][[\'\']]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[no_wrap]][[=]][[None]]*, *[[end]][[=]][[\'\\n\']]*, *[[tab_size]][[=]][[8]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.from_ansi)[](#rich.text.Text.from_ansi "Link to this definition")

    :   Create a Text object from a string containing ANSI escape codes.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing escape codes.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Base style for text. Defaults to "".

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "left", "center", "full", "right". Defaults to None.

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to None.

            -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable text wrapping, or None for default. Defaults to None.

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to end text with. Defaults to "\\n".

            -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of spaces per tab, or [`None`] to use [`console.tab_size`]. Defaults to None.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    *[[classmethod]][ ]*[[from_markup]][(]*[[text]]*, *[[\*]]*, *[[style]][[=]][[\'\']]*, *[[emoji]][[=]][[True]]*, *[[emoji_variant]][[=]][[None]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[end]][[=]][[\'\\n\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.from_markup)[](#rich.text.Text.from_markup "Link to this definition")

    :   Create Text instance from markup.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing console markup.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Base style for text. Defaults to "".

            -   **emoji** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also render emoji code. Defaults to True.

            -   **emoji_variant** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional emoji variant, either "text" or "emoji". Defaults to None.

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "left", "center", "full", "right". Defaults to None.

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to None.

            -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to end text with. Defaults to "\\n".

        Returns[:]

        :   A Text instance with markup rendered.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[get_style_at_offset]][(]*[[console]]*, *[[offset]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.get_style_at_offset)[](#rich.text.Text.get_style_at_offset "Link to this definition")

    :   Get the style of a character at give offset.

        Parameters[:]

        :   -   **console** (*\~Console*) -- Console where text will be rendered.

            -   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Offset in to text (negative indexing supported)

        Returns[:]

        :   A Style instance.

        Return type[:]

        :   [Style](style.html#rich.style.Style "rich.style.Style")

    [[highlight_regex]][(]*[[re_highlight]]*, *[[style]][[=]][[None]]*, *[[\*]]*, *[[style_prefix]][[=]][[\'\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.highlight_regex)[](#rich.text.Text.highlight_regex "Link to this definition")

    :   Highlight text with a regular expression, where group names are translated to styles.

        Parameters[:]

        :   -   **re_highlight** (*Union\[*[*re.Pattern*](https://docs.python.org/3/library/re.html#re.Pattern "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- A regular expression object or string.

            -   **style** (*Union\[GetStyleCallable,* *StyleType\]*) -- Optional style to apply to whole match, or a callable which accepts the matched text and returns a style. Defaults to None.

            -   **style_prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional prefix to add to style group names.

        Returns[:]

        :   Number of regex matches

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    [[highlight_words]][(]*[[words]]*, *[[style]]*, *[[\*]]*, *[[case_sensitive]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.highlight_words)[](#rich.text.Text.highlight_words "Link to this definition")

    :   Highlight words with a style.

        Parameters[:]

        :   -   **words** (*Iterable\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- Words to highlight.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\]*) -- Style to apply.

            -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable case sensitive matching. Defaults to True.

        Returns[:]

        :   Number of words highlighted.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    [[join]][(]*[[lines]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.join)[](#rich.text.Text.join "Link to this definition")

    :   Join text together with this instance as the separator.

        Parameters[:]

        :   **lines** (*Iterable\[*[*Text*](#rich.text.Text "rich.text.Text")*\]*) -- An iterable of Text instances to join.

        Returns[:]

        :   A new text instance containing join text.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    *[[property]][ ]*[[markup]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.text.Text.markup "Link to this definition")

    :   Get console markup to render this Text.

        Returns[:]

        :   A string potentially creating markup tags.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[on]][(]*[[meta]][[=]][[None]]*, *[[\*\*]][[handlers]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.on)[](#rich.text.Text.on "Link to this definition")

    :   Apply event handlers (used by Textual project).

        Example

        ::: 
        ::: highlight
            >>> from rich.text import Text
            >>> text = Text("hello world")
            >>> text.on(click="view.toggle('world')")
        :::
        :::

        Parameters[:]

        :   -   **meta** (*Dict\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Any\]*) -- Mapping of meta information.

            -   **\*\*handlers** -- Keyword args are prefixed with "@" to defined handlers.

        Returns[:]

        :   Self is returned to method may be chained.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[pad]][(]*[[count]]*, *[[character]][[=]][[\'] [\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.pad)[](#rich.text.Text.pad "Link to this definition")

    :   Pad left and right with a given number of characters.

        Parameters[:]

        :   -   **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Width of padding.

            -   **character** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- The character to pad with. Must be a string of length 1.

        Return type[:]

        :   None

    [[pad_left]][(]*[[count]]*, *[[character]][[=]][[\'] [\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.pad_left)[](#rich.text.Text.pad_left "Link to this definition")

    :   Pad the left with a given character.

        Parameters[:]

        :   -   **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of characters to pad.

            -   **character** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to pad with. Defaults to " ".

        Return type[:]

        :   None

    [[pad_right]][(]*[[count]]*, *[[character]][[=]][[\'] [\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.pad_right)[](#rich.text.Text.pad_right "Link to this definition")

    :   Pad the right with a given character.

        Parameters[:]

        :   -   **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of characters to pad.

            -   **character** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to pad with. Defaults to " ".

        Return type[:]

        :   None

    *[[property]][ ]*[[plain]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.text.Text.plain "Link to this definition")

    :   Get the text as a single string.

    [[remove_suffix]][(]*[[suffix]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.remove_suffix)[](#rich.text.Text.remove_suffix "Link to this definition")

    :   Remove a suffix if it exists.

        Parameters[:]

        :   **suffix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Suffix to remove.

        Return type[:]

        :   None

    [[render]][(]*[[console]]*, *[[end]][[=]][[\'\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.render)[](#rich.text.Text.render "Link to this definition")

    :   Render the text as Segments.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

            -   **end** (*Optional\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Optional end character.

        Returns[:]

        :   Result of render that may be written to the console.

        Return type[:]

        :   Iterable\[[Segment](segment.html#rich.segment.Segment "rich.segment.Segment")\]

    [[right_crop]][(]*[[amount]][[=]][[1]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.right_crop)[](#rich.text.Text.right_crop "Link to this definition")

    :   Remove a number of characters from the end of the text.

        Parameters[:]

        :   **amount** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        Return type[:]

        :   None

    [[rstrip]][(][)][[[\[source\]]]](../_modules/rich/text.html#Text.rstrip)[](#rich.text.Text.rstrip "Link to this definition")

    :   Strip whitespace from end of text.

        Return type[:]

        :   None

    [[rstrip_end]][(]*[[size]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.rstrip_end)[](#rich.text.Text.rstrip_end "Link to this definition")

    :   Remove whitespace beyond a certain width at the end of the text.

        Parameters[:]

        :   **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- The desired size of the text.

        Return type[:]

        :   None

    [[set_length]][(]*[[new_length]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.set_length)[](#rich.text.Text.set_length "Link to this definition")

    :   Set new length of the text, clipping or padding is required.

        Parameters[:]

        :   **new_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        Return type[:]

        :   None

    *[[property]][ ]*[[spans]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][Span][[\]]]*[](#rich.text.Text.spans "Link to this definition")

    :   Get a reference to the internal list of spans.

    [[split]][(]*[[separator]][[=]][[\'\\n\']]*, *[[\*]]*, *[[include_separator]][[=]][[False]]*, *[[allow_blank]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.split)[](#rich.text.Text.split "Link to this definition")

    :   Split rich text in to lines, preserving styles.

        Parameters[:]

        :   -   **separator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- String to split on. Defaults to "\\n".

            -   **include_separator** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Include the separator in the lines. Defaults to False.

            -   **allow_blank** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Return a blank line if the text ends with a separator. Defaults to False.

        Returns[:]

        :   A list of rich text, one per line of the original.

        Return type[:]

        :   List\[RichText\]

    *[[classmethod]][ ]*[[styled]][(]*[[text]]*, *[[style]][[=]][[\'\']]*, *[[\*]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.styled)[](#rich.text.Text.styled "Link to this definition")

    :   Construct a Text instance with a pre-applied styled. A style applied in this way won't be used to pad the text when it is justified.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing console markup.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\]*) -- Style to apply to the text. Defaults to "".

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "left", "center", "full", "right". Defaults to None.

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to None.

        Returns[:]

        :   A text instance with a style applied to the entire string.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[stylize]][(]*[[style]]*, *[[start]][[=]][[0]]*, *[[end]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.stylize)[](#rich.text.Text.stylize "Link to this definition")

    :   Apply a style to the text, or a portion of the text.

        Parameters[:]

        :   -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\]*) -- Style instance or style definition to apply.

            -   **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Start offset (negative indexing is supported). Defaults to 0.

            -   **end** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- End offset (negative indexing is supported), or None for end of text. Defaults to None.

        Return type[:]

        :   None

    [[stylize_before]][(]*[[style]]*, *[[start]][[=]][[0]]*, *[[end]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.stylize_before)[](#rich.text.Text.stylize_before "Link to this definition")

    :   Apply a style to the text, or a portion of the text. Styles will be applied before other styles already present.

        Parameters[:]

        :   -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\]*) -- Style instance or style definition to apply.

            -   **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Start offset (negative indexing is supported). Defaults to 0.

            -   **end** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- End offset (negative indexing is supported), or None for end of text. Defaults to None.

        Return type[:]

        :   None

    [[truncate]][(]*[[max_width]]*, *[[\*]]*, *[[overflow]][[=]][[None]]*, *[[pad]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.truncate)[](#rich.text.Text.truncate "Link to this definition")

    :   Truncate text if it is longer that a given width.

        Parameters[:]

        :   -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Maximum number of characters in text.

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", or "ellipsis". Defaults to None, to use self.overflow.

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Pad with spaces if the length is less than max_width. Defaults to False.

        Return type[:]

        :   None

    [[with_indent_guides]][(]*[[indent_size]][[=]][[None]]*, *[[\*]]*, *[[character]][[=]][[\'│\']]*, *[[style]][[=]][[\'dim] [green\']]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.with_indent_guides)[](#rich.text.Text.with_indent_guides "Link to this definition")

    :   Adds indent guide lines to text.

        Parameters[:]

        :   -   **indent_size** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- Size of indentation, or None to auto detect. Defaults to None.

            -   **character** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character to use for indentation. Defaults to "│".

            -   **style** (*Union\[*[*Style*](style.html#rich.style.Style "rich.style.Style")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Style of indent guides.

        Returns[:]

        :   New text with indentation guides.

        Return type[:]

        :   [Text](#rich.text.Text "rich.text.Text")

    [[wrap]][(]*[[console]]*, *[[width]]*, *[[\*]]*, *[[justify]][[=]][[None]]*, *[[overflow]][[=]][[None]]*, *[[tab_size]][[=]][[8]]*, *[[no_wrap]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/text.html#Text.wrap)[](#rich.text.Text.wrap "Link to this definition")

    :   Word wrap the text.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Number of cells available per line.

            -   **justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method: "default", "left", "center", "full", "right". Defaults to "default".

            -   **overflow** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Overflow method: "crop", "fold", or "ellipsis". Defaults to None.

            -   **tab_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Default tab size. Defaults to 8.

            -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Disable wrapping, Defaults to False.

        Returns[:]

        :   Number of lines.

        Return type[:]

        :   Lines

```
<!-- -->
```

[[rich.text.]][[TextType]][](#rich.text.TextType "Link to this definition")

:   A plain string or a [[`Text`]](#rich.text.Text "rich.text.Text") instance.

    alias of [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \| [[`Text`]](#rich.text.Text "rich.text.Text")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).