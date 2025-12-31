# Source: https://rich.readthedocs.io/en/latest/reference/table.html

[]

# rich.table[](#module-rich.table "Link to this heading")

*[[class]][ ]*[[rich.table.]][[Column]][(]*[[header=\'\']]*, *[[footer=\'\']]*, *[[header_style=\'\']]*, *[[footer_style=\'\']]*, *[[style=\'\']]*, *[[justify=\'left\']]*, *[[vertical=\'top\']]*, *[[overflow=\'ellipsis\']]*, *[[width=None]]*, *[[min_width=None]]*, *[[max_width=None]]*, *[[ratio=None]]*, *[[no_wrap=False]]*, *[[highlight=False]]*, *[[\_index=0]]*, *[[\_cells=\<factory\>]]*[)][[[\[source\]]]](../_modules/rich/table.html#Column)[](#rich.table.Column "Link to this definition")

:   Defines a column within a \~Table.

    Parameters[:]

    :   -   **title** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\],* *optional*) -- The title of the table rendered at the top. Defaults to None.

        -   **caption** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\],* *optional*) -- The table caption rendered below. Defaults to None.

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- The width in characters of the table, or [`None`] to automatically fit. Defaults to None.

        -   **min_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- The minimum width of the table, or [`None`] for no minimum. Defaults to None.

        -   **box** (*box.Box,* *optional*) -- One of the constants in box.py used to draw the edges (see [[Box]](../appendix/box.html#appendix-box)), or [`None`] for no box lines. Defaults to box.HEAVY_HEAD.

        -   **safe_box** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.

        -   **padding** (*PaddingDimensions,* *optional*) -- Padding for cells (top, right, bottom, left). Defaults to (0, 1).

        -   **collapse_padding** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable collapsing of padding around cells. Defaults to False.

        -   **pad_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable padding of edge cells. Defaults to True.

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand the table to fit the available space if [`True`], otherwise the table width will be auto-calculated. Defaults to False.

        -   **show_header** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a header row. Defaults to True.

        -   **show_footer** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a footer row. Defaults to False.

        -   **show_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Draw a box around the outside of the table. Defaults to True.

        -   **show_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Draw lines between every row. Defaults to False.

        -   **leading** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of blank lines between rows (precludes [`show_lines`]). Defaults to 0.

        -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Default style for the table. Defaults to "none".

        -   **row_styles** (*List\[Union,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.

        -   **header_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the header. Defaults to "table.header".

        -   **footer_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the footer. Defaults to "table.footer".

        -   **border_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the border. Defaults to None.

        -   **title_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the title. Defaults to None.

        -   **caption_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the caption. Defaults to None.

        -   **title_justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method for title. Defaults to "center".

        -   **caption_justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method for caption. Defaults to "center".

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Highlight cell contents (if str). Defaults to False.

        -   **header** (*RenderableType*)

        -   **footer** (*RenderableType*)

        -   **justify** (*JustifyMethod*)

        -   **vertical** (*VerticalAlignMethod*)

        -   **overflow** (*OverflowMethod*)

        -   **max_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        -   **ratio** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

        -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **\_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        -   **\_cells** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[RenderableType\]*)

    *[[property]][ ]*[[cells]]*[[:]][ ][[Iterable]](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")[[\[]][RenderableType][[\]]]*[](#rich.table.Column.cells "Link to this definition")

    :   Get all cells in the column, not including header.

    [[copy]][(][)][[[\[source\]]]](../_modules/rich/table.html#Column.copy)[](#rich.table.Column.copy "Link to this definition")

    :   Return a copy of this Column.

        Return type[:]

        :   [*Column*](#rich.table.Column "rich.table.Column")

    *[[property]][ ]*[[flexible]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.table.Column.flexible "Link to this definition")

    :   Check if this column is flexible.

    [[footer]]*[[:]][ ][RenderableType][ ][[=]][ ][\'\']*[](#rich.table.Column.footer "Link to this definition")

    :   Renderable for the footer (typically a string)

        Type[:]

        :   RenderableType

    [[footer_style]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")[ ][[=]][ ][\'\']*[](#rich.table.Column.footer_style "Link to this definition")

    :   The style of the footer.

        Type[:]

        :   StyleType

    [[header]]*[[:]][ ][RenderableType][ ][[=]][ ][\'\']*[](#rich.table.Column.header "Link to this definition")

    :   Renderable for the header (typically a string)

        Type[:]

        :   RenderableType

    [[header_style]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")[ ][[=]][ ][\'\']*[](#rich.table.Column.header_style "Link to this definition")

    :   The style of the header.

        Type[:]

        :   StyleType

    [[highlight]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[=]][ ][False]*[](#rich.table.Column.highlight "Link to this definition")

    :   Apply highlighter to column. Defaults to [`False`].

        Type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[justify]]*[[:]][ ][JustifyMethod][ ][[=]][ ][\'left\']*[](#rich.table.Column.justify "Link to this definition")

    :   How to justify text within the column ("left", "center", "right", or "full")

        Type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[max_width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.table.Column.max_width "Link to this definition")

    :   Maximum width of column, or [`None`] for no maximum. Defaults to None.

        Type[:]

        :   Optional\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

    [[min_width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.table.Column.min_width "Link to this definition")

    :   Minimum width of column, or [`None`] for no minimum. Defaults to None.

        Type[:]

        :   Optional\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

    [[no_wrap]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[=]][ ][False]*[](#rich.table.Column.no_wrap "Link to this definition")

    :   Prevent wrapping of text within the column. Defaults to [`False`].

        Type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[overflow]]*[[:]][ ][OverflowMethod][ ][[=]][ ][\'ellipsis\']*[](#rich.table.Column.overflow "Link to this definition")

    :   Overflow method.

        Type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[ratio]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.table.Column.ratio "Link to this definition")

    :   Ratio to use when calculating column width, or [`None`] (default) to adapt to column contents.

        Type[:]

        :   Optional\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

    [[style]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")[ ][[=]][ ][\'\']*[](#rich.table.Column.style "Link to this definition")

    :   The style of the column.

        Type[:]

        :   StyleType

    [[vertical]]*[[:]][ ][VerticalAlignMethod][ ][[=]][ ][\'top\']*[](#rich.table.Column.vertical "Link to this definition")

    :   How to vertically align content ("top", "middle", or "bottom")

        Type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[width]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.table.Column.width "Link to this definition")

    :   Width of the column, or [`None`] (default) to auto calculate width.

        Type[:]

        :   Optional\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")\]

```
<!-- -->
```

*[[class]][ ]*[[rich.table.]][[Row]][(]*[[style]][[=]][[None]]*, *[[end_section]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/table.html#Row)[](#rich.table.Row "Link to this definition")

:   Information regarding a row.

    Parameters[:]

    :   -   **style** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style") *\|* *None*)

        -   **end_section** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[end_section]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")[ ][[=]][ ][False]*[](#rich.table.Row.end_section "Link to this definition")

    :   Indicated end of section, which will force a line beneath the row.

    [[style]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")[ ][[=]][ ][None]*[](#rich.table.Row.style "Link to this definition")

    :   Style to apply to row.

```
<!-- -->
```

*[[class]][ ]*[[rich.table.]][[Table]][(]*[[\*]][[headers]]*, *[[title]][[=]][[None]]*, *[[caption]][[=]][[None]]*, *[[width]][[=]][[None]]*, *[[min_width]][[=]][[None]]*, *[[box]][[=]][[Box(\...)]]*, *[[safe_box]][[=]][[None]]*, *[[padding]][[=]][[(0,] [1)]]*, *[[collapse_padding]][[=]][[False]]*, *[[pad_edge]][[=]][[True]]*, *[[expand]][[=]][[False]]*, *[[show_header]][[=]][[True]]*, *[[show_footer]][[=]][[False]]*, *[[show_edge]][[=]][[True]]*, *[[show_lines]][[=]][[False]]*, *[[leading]][[=]][[0]]*, *[[style]][[=]][[\'none\']]*, *[[row_styles]][[=]][[None]]*, *[[header_style]][[=]][[\'table.header\']]*, *[[footer_style]][[=]][[\'table.footer\']]*, *[[border_style]][[=]][[None]]*, *[[title_style]][[=]][[None]]*, *[[caption_style]][[=]][[None]]*, *[[title_justify]][[=]][[\'center\']]*, *[[caption_justify]][[=]][[\'center\']]*, *[[highlight]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/table.html#Table)[](#rich.table.Table "Link to this definition")

:   A console renderable to draw a table.

    Parameters[:]

    :   -   **\*headers** (*Union\[*[*Column*](#rich.table.Column "rich.table.Column")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- Column headers, either as a string, or [[`Column`]](#rich.table.Column "rich.table.Column") instance.

        -   **title** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\],* *optional*) -- The title of the table rendered at the top. Defaults to None.

        -   **caption** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\],* *optional*) -- The table caption rendered below. Defaults to None.

        -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- The width in characters of the table, or [`None`] to automatically fit. Defaults to None.

        -   **min_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- The minimum width of the table, or [`None`] for no minimum. Defaults to None.

        -   **box** (*box.Box,* *optional*) -- One of the constants in box.py used to draw the edges (see [[Box]](../appendix/box.html#appendix-box)), or [`None`] for no box lines. Defaults to box.HEAVY_HEAD.

        -   **safe_box** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Disable box characters that don't display on windows legacy terminal with *raster* fonts. Defaults to True.

        -   **padding** (*PaddingDimensions,* *optional*) -- Padding for cells (top, right, bottom, left). Defaults to (0, 1).

        -   **collapse_padding** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable collapsing of padding around cells. Defaults to False.

        -   **pad_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable padding of edge cells. Defaults to True.

        -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand the table to fit the available space if [`True`], otherwise the table width will be auto-calculated. Defaults to False.

        -   **show_header** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a header row. Defaults to True.

        -   **show_footer** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show a footer row. Defaults to False.

        -   **show_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Draw a box around the outside of the table. Defaults to True.

        -   **show_lines** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Draw lines between every row. Defaults to False.

        -   **leading** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Number of blank lines between rows (precludes [`show_lines`]). Defaults to 0.

        -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Default style for the table. Defaults to "none".

        -   **row_styles** (*List\[Union,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.

        -   **header_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the header. Defaults to "table.header".

        -   **footer_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the footer. Defaults to "table.footer".

        -   **border_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the border. Defaults to None.

        -   **title_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the title. Defaults to None.

        -   **caption_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style of the caption. Defaults to None.

        -   **title_justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method for title. Defaults to "center".

        -   **caption_justify** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Justify method for caption. Defaults to "center".

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Highlight cell contents (if str). Defaults to False.

    [[add_column]][(]*[[header]][[=]][[\'\']]*, *[[footer]][[=]][[\'\']]*, *[[\*]]*, *[[header_style]][[=]][[None]]*, *[[highlight]][[=]][[None]]*, *[[footer_style]][[=]][[None]]*, *[[style]][[=]][[None]]*, *[[justify]][[=]][[\'left\']]*, *[[vertical]][[=]][[\'top\']]*, *[[overflow]][[=]][[\'ellipsis\']]*, *[[width]][[=]][[None]]*, *[[min_width]][[=]][[None]]*, *[[max_width]][[=]][[None]]*, *[[ratio]][[=]][[None]]*, *[[no_wrap]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/table.html#Table.add_column)[](#rich.table.Table.add_column "Link to this definition")

    :   Add a column to the table.

        Parameters[:]

        :   -   **header** (*RenderableType,* *optional*) -- Text or renderable for the header. Defaults to "".

            -   **footer** (*RenderableType,* *optional*) -- Text or renderable for the footer. Defaults to "".

            -   **header_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style for the header, or None for default. Defaults to None.

            -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Whether to highlight the text. The default of None uses the value of the table (self) object.

            -   **footer_style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style for the footer, or None for default. Defaults to None.

            -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Style for the column cells, or None for default. Defaults to None.

            -   **justify** (*JustifyMethod,* *optional*) -- Alignment for cells. Defaults to "left".

            -   **vertical** (*VerticalAlignMethod,* *optional*) -- Vertical alignment, one of "top", "middle", or "bottom". Defaults to "top".

            -   **overflow** (*OverflowMethod*) -- Overflow method: "crop", "fold", "ellipsis". Defaults to "ellipsis".

            -   **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Desired width of column in characters, or None to fit to contents. Defaults to None.

            -   **min_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Minimum width of column, or [`None`] for no minimum. Defaults to None.

            -   **max_width** (*Optional\[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*\],* *optional*) -- Maximum width of column, or [`None`] for no maximum. Defaults to None.

            -   **ratio** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Flexible ratio for the column (requires [`Table.expand`] or [`Table.width`]). Defaults to None.

            -   **no_wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Set to [`True`] to disable wrapping of this column.

        Return type[:]

        :   None

    [[add_row]][(]*[[\*]][[renderables]]*, *[[style]][[=]][[None]]*, *[[end_section]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/table.html#Table.add_row)[](#rich.table.Table.add_row "Link to this definition")

    :   Add a row of renderables.

        Parameters[:]

        :   -   **\*renderables** (*None* *or* *renderable*) -- Each cell in a row must be a renderable object (including str), or [`None`] for a blank cell.

            -   **style** (*StyleType,* *optional*) -- An optional style to apply to the entire row. Defaults to None.

            -   **end_section** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- End a section and draw a line. Defaults to False.

        Raises[:]

        :   **errors.NotRenderableError** -- If you add something that can't be rendered.

        Return type[:]

        :   None

    [[add_section]][(][)][[[\[source\]]]](../_modules/rich/table.html#Table.add_section)[](#rich.table.Table.add_section "Link to this definition")

    :   Add a new section (draw a line after current row).

        Return type[:]

        :   None

    *[[property]][ ]*[[expand]]*[[:]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*[](#rich.table.Table.expand "Link to this definition")

    :   Setting a non-None self.width implies expand.

    [[get_row_style]][(]*[[console]]*, *[[index]]*[)][[[\[source\]]]](../_modules/rich/table.html#Table.get_row_style)[](#rich.table.Table.get_row_style "Link to this definition")

    :   Get the current row style.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console"))

            -   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"))

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") \| [Style](style.html#rich.style.Style "rich.style.Style")

    *[[classmethod]][ ]*[[grid]][(]*[[\*]][[headers]]*, *[[padding]][[=]][[0]]*, *[[collapse_padding]][[=]][[True]]*, *[[pad_edge]][[=]][[False]]*, *[[expand]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/table.html#Table.grid)[](#rich.table.Table.grid "Link to this definition")

    :   Get a table with no lines, headers, or footer.

        Parameters[:]

        :   -   **\*headers** (*Union\[*[*Column*](#rich.table.Column "rich.table.Column")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- Column headers, either as a string, or [[`Column`]](#rich.table.Column "rich.table.Column") instance.

            -   **padding** (*PaddingDimensions,* *optional*) -- Get padding around cells. Defaults to 0.

            -   **collapse_padding** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable collapsing of padding around cells. Defaults to True.

            -   **pad_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable padding around edges of table. Defaults to False.

            -   **expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Expand the table to fit the available space if [`True`], otherwise the table width will be auto-calculated. Defaults to False.

        Returns[:]

        :   A table instance.

        Return type[:]

        :   [Table](#rich.table.Table "rich.table.Table")

    *[[property]][ ]*[[padding]]*[[:]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")[[\]]]*[](#rich.table.Table.padding "Link to this definition")

    :   Get cell padding.

    *[[property]][ ]*[[row_count]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*[](#rich.table.Table.row_count "Link to this definition")

    :   Get the current number of rows.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).