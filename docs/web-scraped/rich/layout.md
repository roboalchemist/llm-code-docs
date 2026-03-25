# Source: https://rich.readthedocs.io/en/latest/layout.html

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