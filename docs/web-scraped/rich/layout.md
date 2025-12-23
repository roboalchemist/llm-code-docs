# Source: https://rich.readthedocs.io/en/latest/layout.html

[Contents:]

-   [Introduction](introduction.html)
-   [Console API](console.html)
-   [Styles](style.html)
-   [Console Markup](markup.html)
-   [Rich Text](text.html)
-   [Highlighting](highlighting.html)
-   [Pretty Printing](pretty.html)
-   [Logging Handler](logging.html)
-   [Traceback](traceback.html)
-   [Prompt](prompt.html)
-   [Columns](columns.html)
-   [Render Groups](group.html)
-   [Markdown](markdown.html)
-   [Padding](padding.html)
-   [Panel](panel.html)
-   [Progress Display](progress.html)
-   [Syntax](syntax.html)
-   [Tables](tables.html)
-   [Tree](tree.html)
-   [Live Display](live.html)
-   [Layout](#)
    -   [Creating layouts](#creating-layouts)
    -   [Setting renderables](#setting-renderables)
    -   [Fixed size](#fixed-size)
    -   [Ratio](#ratio)
    -   [Visibility](#visibility)
    -   [Tree](#tree)
    -   [Example](#example)
-   [Console Protocol](protocol.html)
-   [Reference](reference.html)
-   [Appendix](appendix.html)

[Rich](index.html)

# Layout[](#layout "Link to this heading")

Rich offers a [[`Layout`]](reference/layout.html#rich.layout.Layout "rich.layout.Layout") class which can be used to divide the screen area in to parts, where each part may contain independent content. It can be used with [[Live Display]](live.html#live) to create full-screen "applications" but may be used standalone.

To see an example of a Layout, run the following from the command line:

    python -m rich.layout

## Creating layouts[](#creating-layouts "Link to this heading")

To define a layout, construct a Layout object and print it:

    from rich import print
    from rich.layout import Layout

    layout = Layout()
    print(layout)

This will draw a box the size of the terminal with some information regarding the layout. The box is a "placeholder" because we have yet to add any content to it. Before we do that, let's create a more interesting layout by calling the [[`split_column()`]](reference/layout.html#rich.layout.Layout.split_column "rich.layout.Layout.split_column") method to divide the layout in to two sub-layouts:

    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    print(layout)

This will divide the terminal screen in to two equal sized portions, one on top of the other. The [`name`] attribute is an internal identifier we can use to look up the sub-layout later. Let's use that to create another split, this time we will call [[`split_row()`]](reference/layout.html#rich.layout.Layout.split_row "rich.layout.Layout.split_row") to split the lower layout in to a row of two sub-layouts:

    layout["lower"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )
    print(layout)

You should now see the screen area divided in to 3 portions; an upper half and a lower half that is split in to two quarters.

``` 
╭─────────────────────────────── 'upper' (84 x 13) ────────────────────────────────╮
│                                                                                  │
│                                                                                  │
│                                                                                  │
│                                                                                  │
│                                                                                  │
│                    │
│                                                                                  │
│                                                                                  │
│                                                                                  │
│                                                                                  │
│                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────╯
╭─────────── 'left' (42 x 14) ───────────╮╭────────── 'right' (42 x 14) ───────────╮
│                                        ││                                        │
│                                        ││                                        │
│                                        ││                                        │
│                                       ││         }                              │
│                                        ││                                        │
│                                        ││                                        │
│                                        ││                                        │
╰────────────────────────────────────────╯╰────────────────────────────────────────╯
```

You can continue to call split() in this way to create as many parts to the screen as you wish.

## Setting renderables[](#setting-renderables "Link to this heading")

The first position argument to [`Layout`] can be any Rich renderable, which will be sized to fit within the layout's area. Here's how we might divide the "right" layout in to two panels:

    from rich.panel import Panel

    layout["right"].split(
        Layout(Panel("Hello")),
        Layout(Panel("World!"))
    )

You can also call [[`update()`]](reference/layout.html#rich.layout.Layout.update "rich.layout.Layout.update") to set or replace the current renderable:

    layout["left"].update(
        "The mystery of life isn't a problem to solve, but a reality to experience."
    )
    print(layout)

## Fixed size[](#fixed-size "Link to this heading")

You can set a layout to use a fixed size by setting the [`size`] argument on the Layout constructor or by setting the attribute. Here's an example:

    layout["upper"].size = 10
    print(layout)

This will set the upper portion to be exactly 10 rows, no matter the size of the terminal. If the parent layout is horizontal rather than vertical, then the size applies to the number of characters rather that rows.

## Ratio[](#ratio "Link to this heading")

In addition to a fixed size, you can also make a flexible layout setting the [`ratio`] argument on the constructor or by assigning to the attribute. The ratio defines how much of the screen the layout should occupy in relation to other layouts. For example, let's reset the size and set the ratio of the upper layout to 2:

    layout["upper"].size = None
    layout["upper"].ratio = 2
    print(layout)

This makes the top layout take up two thirds of the space. This is because the default ratio is 1, giving the upper and lower layouts a combined total of 3. As the upper layout has a ratio of 2, it takes up two thirds of the space, leaving the remaining third for the lower layout.

A layout with a ratio set may also have a minimum size to prevent it from getting too small. For instance, here's how we could set the minimum size of the lower sub-layout so that it won't shrink beyond 10 rows:

    layout["lower"].minimum_size = 10

## Visibility[](#visibility "Link to this heading")

You can make a layout invisible by setting the [`visible`] attribute to False. Here's an example:

    layout["upper"].visible = False
    print(layout)

The top layout is now invisible, and the "lower" layout will expand to fill the available space. Set [`visible`] to True to bring it back:

    layout["upper"].visible = True
    print(layout)

You could use this to toggle parts of your interface based on your application's configuration.

## Tree[](#tree "Link to this heading")

To help visualize complex layouts you can print the [`tree`] attribute which will display a summary of the layout as a tree:

    print(layout.tree)

## Example[](#example "Link to this heading")

See [fullscreen.py](https://github.com/willmcgugan/rich/blob/master/examples/fullscreen.py) for an example that combines [[`Layout`]](reference/layout.html#rich.layout.Layout "rich.layout.Layout") and [[`Live`]](reference/live.html#rich.live.Live "rich.live.Live") to create a fullscreen "application".

[[] Previous](live.html "Live Display") [Next []](protocol.html "Console Protocol")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).