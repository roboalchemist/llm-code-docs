# Source: https://rich.readthedocs.io/en/latest/reference/layout.html

[]

# rich.layout[](#module-rich.layout "Link to this heading")

*[[class]][ ]*[[rich.layout.]][[ColumnSplitter]][[[\[source\]]]](../_modules/rich/layout.html#ColumnSplitter)[](#rich.layout.ColumnSplitter "Link to this definition")

:   Split a layout region in to columns.

    [[divide]][(]*[[children]]*, *[[region]]*[)][[[\[source\]]]](../_modules/rich/layout.html#ColumnSplitter.divide)[](#rich.layout.ColumnSplitter.divide "Link to this definition")

    :   Divide a region amongst several child layouts.

        Parameters[:]

        :   -   **children** (*Sequence(*[*Layout*](#rich.layout.Layout "rich.layout.Layout")*)*) -- A number of child layouts.

            -   **region** (*Region*) -- A rectangular region to divide.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[*Layout*](#rich.layout.Layout "rich.layout.Layout"), *Region*\]\]

    [[get_tree_icon]][(][)][[[\[source\]]]](../_modules/rich/layout.html#ColumnSplitter.get_tree_icon)[](#rich.layout.ColumnSplitter.get_tree_icon "Link to this definition")

    :   Get the icon (emoji) used in layout.tree

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.layout.]][[Layout]][(]*[[renderable]][[=]][[None]]*, *[[\*]]*, *[[name]][[=]][[None]]*, *[[size]][[=]][[None]]*, *[[minimum_size]][[=]][[1]]*, *[[ratio]][[=]][[1]]*, *[[visible]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout)[](#rich.layout.Layout "Link to this definition")

:   A renderable to divide a fixed height in to rows or columns.

    Parameters[:]

    :   -   **renderable** (*RenderableType,* *optional*) -- Renderable content, or None for placeholder. Defaults to None.

        -   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Optional identifier for Layout. Defaults to None.

        -   **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Optional fixed size of layout. Defaults to None.

        -   **minimum_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Minimum size of layout. Defaults to 1.

        -   **ratio** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*,* *optional*) -- Optional ratio for flexible layout. Defaults to 1.

        -   **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Visibility of layout. Defaults to True.

    [[add_split]][(]*[[\*]][[layouts]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.add_split)[](#rich.layout.Layout.add_split "Link to this definition")

    :   Add a new layout(s) to existing split.

        Parameters[:]

        :   **\*layouts** (*Union\[*[*Layout*](#rich.layout.Layout "rich.layout.Layout")*,* *RenderableType\]*) -- Positional arguments should be renderables or (sub) Layout instances.

        Return type[:]

        :   None

    *[[property]][ ]*[[children]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[Layout]](#rich.layout.Layout "rich.layout.Layout")[[\]]]*[](#rich.layout.Layout.children "Link to this definition")

    :   Gets (visible) layout children.

    [[get]][(]*[[name]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.get)[](#rich.layout.Layout.get "Link to this definition")

    :   Get a named layout, or None if it doesn't exist.

        Parameters[:]

        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Name of layout.

        Returns[:]

        :   Layout instance or None if no layout was found.

        Return type[:]

        :   Optional\[[Layout](#rich.layout.Layout "rich.layout.Layout")\]

    *[[property]][ ]*[[map]]*[[:]][ ][[Dict]](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.13)")[[\[]][[Layout]](#rich.layout.Layout "rich.layout.Layout")[[,]][ ][[LayoutRender]](#rich.layout.LayoutRender "rich.layout.LayoutRender")[[\]]]*[](#rich.layout.Layout.map "Link to this definition")

    :   Get a map of the last render.

    [[refresh_screen]][(]*[[console]]*, *[[layout_name]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.refresh_screen)[](#rich.layout.Layout.refresh_screen "Link to this definition")

    :   Refresh a sub-layout.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance where Layout is to be rendered.

            -   **layout_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Name of layout.

        Return type[:]

        :   None

    [[render]][(]*[[console]]*, *[[options]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.render)[](#rich.layout.Layout.render "Link to this definition")

    :   Render the sub_layouts.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

            -   **options** ([*ConsoleOptions*](console.html#rich.console.ConsoleOptions "rich.console.ConsoleOptions")) -- Console options.

        Returns[:]

        :   A dict that maps Layout on to a tuple of Region, lines

        Return type[:]

        :   RenderMap

    *[[property]][ ]*[[renderable]]*[[:]][ ][[ConsoleRenderable]](console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")[ ][[\|]][ ][[RichCast]](console.html#rich.console.RichCast "rich.console.RichCast")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*[](#rich.layout.Layout.renderable "Link to this definition")

    :   Layout renderable.

    [[split]][(]*[[\*]][[layouts]]*, *[[splitter]][[=]][[\'column\']]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.split)[](#rich.layout.Layout.split "Link to this definition")

    :   Split the layout in to multiple sub-layouts.

        Parameters[:]

        :   -   **\*layouts** ([*Layout*](#rich.layout.Layout "rich.layout.Layout")) -- Positional arguments should be (sub) Layout instances.

            -   **splitter** (*Union\[*[*Splitter*](#rich.layout.Splitter "rich.layout.Splitter")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*) -- Splitter instance or name of splitter.

        Return type[:]

        :   None

    [[split_column]][(]*[[\*]][[layouts]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.split_column)[](#rich.layout.Layout.split_column "Link to this definition")

    :   Split the layout in to a column (layouts stacked on top of each other).

        Parameters[:]

        :   **\*layouts** ([*Layout*](#rich.layout.Layout "rich.layout.Layout")) -- Positional arguments should be (sub) Layout instances.

        Return type[:]

        :   None

    [[split_row]][(]*[[\*]][[layouts]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.split_row)[](#rich.layout.Layout.split_row "Link to this definition")

    :   Split the layout in to a row (layouts side by side).

        Parameters[:]

        :   **\*layouts** ([*Layout*](#rich.layout.Layout "rich.layout.Layout")) -- Positional arguments should be (sub) Layout instances.

        Return type[:]

        :   None

    *[[property]][ ]*[[tree]]*[[:]][ ][[Tree]](tree.html#rich.tree.Tree "rich.tree.Tree")*[](#rich.layout.Layout.tree "Link to this definition")

    :   Get a tree renderable to show layout structure.

    [[unsplit]][(][)][[[\[source\]]]](../_modules/rich/layout.html#Layout.unsplit)[](#rich.layout.Layout.unsplit "Link to this definition")

    :   Reset splits to initial state.

        Return type[:]

        :   None

    [[update]][(]*[[renderable]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Layout.update)[](#rich.layout.Layout.update "Link to this definition")

    :   Update renderable.

        Parameters[:]

        :   **renderable** (*RenderableType*) -- New renderable object.

        Return type[:]

        :   None

```
<!-- -->
```

*[[exception]][ ]*[[rich.layout.]][[LayoutError]][[[\[source\]]]](../_modules/rich/layout.html#LayoutError)[](#rich.layout.LayoutError "Link to this definition")

:   Layout related error.

```
<!-- -->
```

*[[class]][ ]*[[rich.layout.]][[LayoutRender]][(]*[[region]]*, *[[render]]*[)][[[\[source\]]]](../_modules/rich/layout.html#LayoutRender)[](#rich.layout.LayoutRender "Link to this definition")

:   An individual layout render.

    Parameters[:]

    :   -   **region** (*Region*)

        -   **render** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*Segment*](segment.html#rich.segment.Segment "rich.segment.Segment")*\]\]*)

    [[region]]*[[:]][ ][Region]*[](#rich.layout.LayoutRender.region "Link to this definition")

    :   Alias for field number 0

    [[render]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[Segment]](segment.html#rich.segment.Segment "rich.segment.Segment")[[\]]][[\]]]*[](#rich.layout.LayoutRender.render "Link to this definition")

    :   Alias for field number 1

```
<!-- -->
```

*[[exception]][ ]*[[rich.layout.]][[NoSplitter]][[[\[source\]]]](../_modules/rich/layout.html#NoSplitter)[](#rich.layout.NoSplitter "Link to this definition")

:   Requested splitter does not exist.

```
<!-- -->
```

*[[class]][ ]*[[rich.layout.]][[RowSplitter]][[[\[source\]]]](../_modules/rich/layout.html#RowSplitter)[](#rich.layout.RowSplitter "Link to this definition")

:   Split a layout region in to rows.

    [[divide]][(]*[[children]]*, *[[region]]*[)][[[\[source\]]]](../_modules/rich/layout.html#RowSplitter.divide)[](#rich.layout.RowSplitter.divide "Link to this definition")

    :   Divide a region amongst several child layouts.

        Parameters[:]

        :   -   **children** (*Sequence(*[*Layout*](#rich.layout.Layout "rich.layout.Layout")*)*) -- A number of child layouts.

            -   **region** (*Region*) -- A rectangular region to divide.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[*Layout*](#rich.layout.Layout "rich.layout.Layout"), *Region*\]\]

    [[get_tree_icon]][(][)][[[\[source\]]]](../_modules/rich/layout.html#RowSplitter.get_tree_icon)[](#rich.layout.RowSplitter.get_tree_icon "Link to this definition")

    :   Get the icon (emoji) used in layout.tree

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.layout.]][[Splitter]][[[\[source\]]]](../_modules/rich/layout.html#Splitter)[](#rich.layout.Splitter "Link to this definition")

:   Base class for a splitter.

    *[[abstractmethod]][ ]*[[divide]][(]*[[children]]*, *[[region]]*[)][[[\[source\]]]](../_modules/rich/layout.html#Splitter.divide)[](#rich.layout.Splitter.divide "Link to this definition")

    :   Divide a region amongst several child layouts.

        Parameters[:]

        :   -   **children** (*Sequence(*[*Layout*](#rich.layout.Layout "rich.layout.Layout")*)*) -- A number of child layouts.

            -   **region** (*Region*) -- A rectangular region to divide.

        Return type[:]

        :   [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.13)")\[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.13)")\[[*Layout*](#rich.layout.Layout "rich.layout.Layout"), *Region*\]\]

    *[[abstractmethod]][ ]*[[get_tree_icon]][(][)][[[\[source\]]]](../_modules/rich/layout.html#Splitter.get_tree_icon)[](#rich.layout.Splitter.get_tree_icon "Link to this definition")

    :   Get the icon (emoji) used in layout.tree

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).