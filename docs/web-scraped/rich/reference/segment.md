# Source: https://rich.readthedocs.io/en/latest/reference/segment.html

[]

# rich.segment[](#module-rich.segment "Link to this heading")

*[[class]][ ]*[[rich.segment.]][[ControlType]][(]*[[\*]][[values]]*[)][[[\[source\]]]](../_modules/rich/segment.html#ControlType)[](#rich.segment.ControlType "Link to this definition")

:   Non-printable control codes which typically translate to ANSI codes.

```
<!-- -->
```

*[[class]][ ]*[[rich.segment.]][[Segment]][(]*[[text]]*, *[[style]][[=]][[None]]*, *[[control]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment)[](#rich.segment.Segment "Link to this definition")

:   A piece of text with associated style. Segments are produced by the Console render process and are ultimately converted in to strings to be written to the terminal.

    Parameters[:]

    :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A piece of text.

        -   **style** ([[`Style`]](style.html#rich.style.Style "rich.style.Style"), optional) -- An optional style to apply to the text.

        -   **control** (*Tuple\[ControlCode\],* *optional*) -- Optional sequence of control codes.

    [[cell_length]][](#rich.segment.Segment.cell_length "Link to this definition")

    :   The cell length of this Segment.

        Type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    *[[classmethod]][ ]*[[adjust_line_length]][(]*[[line]]*, *[[length]]*, *[[style]][[=]][[None]]*, *[[pad]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.adjust_line_length)[](#rich.segment.Segment.adjust_line_length "Link to this definition")

    :   Adjust a line to a given width (cropping or padding as required).

        Parameters[:]

        :   -   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- A list of segments in a single line.

            -   **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- The desired width of the line.

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style")*,* *optional*) -- The style of padding if used (space on the end). Defaults to None.

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Pad lines with spaces if they are shorter than length. Defaults to True.

            -   **line** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*)

        Returns[:]

        :   A line of segments with the desired length.

        Return type[:]

        :   List\[[Segment](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[align_bottom]][(]*[[lines]]*, *[[width]]*, *[[height]]*, *[[style]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.align_bottom)[](#rich.segment.Segment.align_bottom "Link to this definition")

    :   Aligns render to bottom (adds extra lines above as required).

        > <div>
        >
        > Args:
        >
        > :   lines (List\[List\[Segment\]\]): A list of lines. width (int): Desired width. height (int, optional): Desired height or None for no change. style (Style): Style of any padding added. Defaults to None. new_lines (bool, optional): Padded lines should include "
        >
        > </div>

        ". Defaults to False.

        > <div>
        >
        > Returns:
        >
        > :   List\[List\[Segment\]\]: New list of lines.
        >
        > </div>

        Parameters[:]

        :   -   **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]\]*)

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style"))

            -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[align_middle]][(]*[[lines]]*, *[[width]]*, *[[height]]*, *[[style]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.align_middle)[](#rich.segment.Segment.align_middle "Link to this definition")

    :   Aligns lines to middle (adds extra lines to above and below as required).

        > <div>
        >
        > Args:
        >
        > :   lines (List\[List\[Segment\]\]): A list of lines. width (int): Desired width. height (int, optional): Desired height or None for no change. style (Style): Style of any padding added. new_lines (bool, optional): Padded lines should include "
        >
        > </div>

        ". Defaults to False.

        > <div>
        >
        > Returns:
        >
        > :   List\[List\[Segment\]\]: New list of lines.
        >
        > </div>

        Parameters[:]

        :   -   **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]\]*)

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style"))

            -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[align_top]][(]*[[lines]]*, *[[width]]*, *[[height]]*, *[[style]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.align_top)[](#rich.segment.Segment.align_top "Link to this definition")

    :   Aligns lines to top (adds extra lines to bottom as required).

        > <div>
        >
        > Args:
        >
        > :   lines (List\[List\[Segment\]\]): A list of lines. width (int): Desired width. height (int, optional): Desired height or None for no change. style (Style): Style of any padding added. new_lines (bool, optional): Padded lines should include "
        >
        > </div>

        ". Defaults to False.

        > <div>
        >
        > Returns:
        >
        > :   List\[List\[Segment\]\]: New list of lines.
        >
        > </div>

        Parameters[:]

        :   -   **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]\]*)

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style"))

            -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[apply_style]][(]*[[segments]]*, *[[style]][[=]][[None]]*, *[[post_style]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.apply_style)[](#rich.segment.Segment.apply_style "Link to this definition")

    :   Apply style(s) to an iterable of segments.

        Returns an iterable of segments where the style is replaced by [`style`]` `[`+`]` `[`segment.style`]` `[`+`]` `[`post_style`].

        Parameters[:]

        :   -   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- Segments to process.

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style")*,* *optional*) -- Base style. Defaults to None.

            -   **post_style** ([*Style*](style.html#rich.style.Style "rich.style.Style")*,* *optional*) -- Style to apply on top of segment style. Defaults to None.

        Returns[:]

        :   A new iterable of segments (possibly the same iterable).

        Return type[:]

        :   Iterable\[[Segments](#rich.segment.Segments "rich.segment.Segments")\]

    *[[property]][ ]*[[cell_length]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#id0 "Link to this definition")

    :   The number of terminal cells required to display self.text.

        Returns[:]

        :   A number of cells.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    [[control]]*[[:]][ ][[Sequence]](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")[[\[]][[ControlType]](#rich.segment.ControlType "rich.segment.ControlType")[[\]]][ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")[[\[]][[ControlType]](#rich.segment.ControlType "rich.segment.ControlType")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")[[\[]][[ControlType]](#rich.segment.ControlType "rich.segment.ControlType")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[\]]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.segment.Segment.control "Link to this definition")

    :   Alias for field number 2

    *[[classmethod]][ ]*[[divide]][(]*[[segments]]*, *[[cuts]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.divide)[](#rich.segment.Segment.divide "Link to this definition")

    :   Divides an iterable of segments in to portions.

        Parameters[:]

        :   -   **cuts** (*Iterable\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\]*) -- Cell positions where to divide.

            -   **segments** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*)

        Yields[:]

        :   *\[Iterable\[List\[Segment\]\]\]* -- An iterable of Segments in List.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[filter_control]][(]*[[segments]]*, *[[is_control]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.filter_control)[](#rich.segment.Segment.filter_control "Link to this definition")

    :   Filter segments by [`is_control`] attribute.

        Parameters[:]

        :   -   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable of Segment instances.

            -   **is_control** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- is_control flag to match in search.

        Returns[:]

        :   And iterable of Segment instances.

        Return type[:]

        :   Iterable\[[Segment](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[get_line_length]][(]*[[line]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.get_line_length)[](#rich.segment.Segment.get_line_length "Link to this definition")

    :   Get the length of list of segments.

        Parameters[:]

        :   **line** (*List\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- A line encoded as a list of Segments (assumes no '\\n' characters),

        Returns[:]

        :   The length of the line.

        Return type[:]

        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    *[[classmethod]][ ]*[[get_shape]][(]*[[lines]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.get_shape)[](#rich.segment.Segment.get_shape "Link to this definition")

    :   Get the shape (enclosing rectangle) of a list of lines.

        Parameters[:]

        :   **lines** (*List\[List\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]\]*) -- A list of lines (no '\\n' characters).

        Returns[:]

        :   Width and height in characters.

        Return type[:]

        :   Tuple\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

    *[[property]][ ]*[[is_control]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.segment.Segment.is_control "Link to this definition")

    :   Check if the segment contains control codes.

    *[[classmethod]][ ]*[[line]][(][)][[[\[source\]]]](../_modules/rich/segment.html#Segment.line)[](#rich.segment.Segment.line "Link to this definition")

    :   Make a new line segment.

        Return type[:]

        :   [*Segment*](#rich.segment.Segment "rich.segment.Segment")

    *[[classmethod]][ ]*[[remove_color]][(]*[[segments]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.remove_color)[](#rich.segment.Segment.remove_color "Link to this definition")

    :   Remove all color from an iterable of segments.

        Parameters[:]

        :   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable segments.

        Yields[:]

        :   *Segment* -- Segments with colorless style.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[set_shape]][(]*[[lines]]*, *[[width]]*, *[[height]][[=]][[None]]*, *[[style]][[=]][[None]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.set_shape)[](#rich.segment.Segment.set_shape "Link to this definition")

    :   Set the shape of a list of lines (enclosing rectangle).

        > <div>
        >
        > Args:
        >
        > :   lines (List\[List\[Segment\]\]): A list of lines. width (int): Desired width. height (int, optional): Desired height or None for no change. style (Style, optional): Style of any padding added. new_lines (bool, optional): Padded lines should include "
        >
        > </div>

        ". Defaults to False.

        > <div>
        >
        > Returns:
        >
        > :   List\[List\[Segment\]\]: New list of lines.
        >
        > </div>

        Parameters[:]

        :   -   **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]\]*)

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

            -   **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

            -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Return type[:]

        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[simplify]][(]*[[segments]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.simplify)[](#rich.segment.Segment.simplify "Link to this definition")

    :   Simplify an iterable of segments by combining contiguous segments with the same style.

        Parameters[:]

        :   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable of segments.

        Returns[:]

        :   A possibly smaller iterable of segments that will render the same way.

        Return type[:]

        :   Iterable\[[Segment](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[split_and_crop_lines]][(]*[[segments]]*, *[[length]]*, *[[style]][[=]][[None]]*, *[[pad]][[=]][[True]]*, *[[include_new_lines]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.split_and_crop_lines)[](#rich.segment.Segment.split_and_crop_lines "Link to this definition")

    :   Split segments in to lines, and crop lines greater than a given length.

        Parameters[:]

        :   -   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable of segments, probably generated from console.render.

            -   **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Desired line length.

            -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style")*,* *optional*) -- Style to use for any padding.

            -   **pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- Enable padding of lines that are less than length.

            -   **include_new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        Returns[:]

        :   An iterable of lines of segments.

        Return type[:]

        :   Iterable\[List\[[Segment](#rich.segment.Segment "rich.segment.Segment")\]\]

    [[split_cells]][(]*[[cut]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.split_cells)[](#rich.segment.Segment.split_cells "Link to this definition")

    :   Split segment in to two segments at the specified column.

        If the cut point falls in the middle of a 2-cell wide character then it is replaced by two spaces, to preserve the display width of the parent segment.

        Parameters[:]

        :   **cut** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) -- Offset within the segment to cut.

        Returns[:]

        :   Two segments.

        Return type[:]

        :   Tuple\[[Segment](#rich.segment.Segment "rich.segment.Segment"), [Segment](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[split_lines]][(]*[[segments]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.split_lines)[](#rich.segment.Segment.split_lines "Link to this definition")

    :   Split a sequence of segments in to a list of lines.

        Parameters[:]

        :   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- Segments potentially containing line feeds.

        Yields[:]

        :   *Iterable\[List\[Segment\]\]* -- Iterable of segment lists, one per line.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]\]

    *[[classmethod]][ ]*[[strip_links]][(]*[[segments]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.strip_links)[](#rich.segment.Segment.strip_links "Link to this definition")

    :   Remove all links from an iterable of styles.

        Parameters[:]

        :   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable segments.

        Yields[:]

        :   *Segment* -- Segments with link removed.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]

    *[[classmethod]][ ]*[[strip_styles]][(]*[[segments]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segment.strip_styles)[](#rich.segment.Segment.strip_styles "Link to this definition")

    :   Remove all styles from an iterable of segments.

        Parameters[:]

        :   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable segments.

        Yields[:]

        :   *Segment* -- Segments with styles replace with None

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Segment*](#rich.segment.Segment "rich.segment.Segment")\]

    [[style]]*[[:]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")*[](#rich.segment.Segment.style "Link to this definition")

    :   Alias for field number 1

    [[text]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.segment.Segment.text "Link to this definition")

    :   Alias for field number 0

```
<!-- -->
```

*[[class]][ ]*[[rich.segment.]][[Segments]][(]*[[segments]]*, *[[new_lines]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/segment.html#Segments)[](#rich.segment.Segments "Link to this definition")

:   A simple renderable to render an iterable of segments. This class may be useful if you want to print segments outside of a \_\_rich_console\_\_ method.

    Parameters[:]

    :   -   **segments** (*Iterable\[*[*Segment*](#rich.segment.Segment "rich.segment.Segment")*\]*) -- An iterable of segments.

        -   **new_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Add new lines between segments. Defaults to False.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).