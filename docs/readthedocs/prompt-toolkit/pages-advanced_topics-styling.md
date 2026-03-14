# More about styling

This page will attempt to explain in more detail how to use styling in
prompt_toolkit.

To some extent, it is very similar to how Pygments [http://pygments.org/]
styling works.

## Style strings

Many user interface controls, like `Window`
accept a `style` argument which can be used to pass the formatting as a
string. For instance, we can select a foreground color:

- 

`"fg:ansired"`  (ANSI color palette)

- 

`"fg:ansiblue"` (ANSI color palette)

- 

`"fg:#ffaa33"`  (hexadecimal notation)

- 

`"fg:darkred"`  (named color)

Or a background color:

- 

`"bg:ansired"`  (ANSI color palette)

- 

`"bg:#ffaa33"`  (hexadecimal notation)

Or we can add one of the following flags:

- 

`"bold"`

- 

`"italic"`

- 

`"underline"`

- 

`"blink"`

- 

`"reverse"`  (reverse foreground and background on the terminal.)

- 

`"hidden"`

Or their negative variants:

- 

`"nobold"`

- 

`"noitalic"`

- 

`"nounderline"`

- 

`"noblink"`

- 

`"noreverse"`

- 

`"nohidden"`

All of these formatting options can be combined as well:

- 

`"fg:ansiyellow bg:black bold underline"`

The style string can be given to any user control directly, or to a
`Container` object from where it will propagate
to all its children. A style defined by a parent user control can be overridden
by any of its children. The parent can for instance say `style="bold
underline"` where a child overrides this style partly by specifying
`style="nobold bg:ansired"`.

Note

These styles are actually compatible with
Pygments [http://pygments.org/] styles, with additional support for
reverse and blink. Further, we ignore flags like roman, sans,
mono and border.