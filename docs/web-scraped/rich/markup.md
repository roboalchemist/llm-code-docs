# Source: https://rich.readthedocs.io/en/latest/markup.html

[Contents:]

-   [Introduction](introduction.html)
-   [Console API](console.html)
-   [Styles](style.html)
-   [Console Markup](#)
    -   [Syntax](#syntax)
        -   [Errors](#errors)
        -   [Links](#links)
        -   [Escaping](#escaping)
        -   [Emoji](#emoji)
    -   [Rendering Markup](#rendering-markup)
    -   [Markup API](#markup-api)
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
-   [Layout](layout.html)
-   [Console Protocol](protocol.html)
-   [Reference](reference.html)
-   [Appendix](appendix.html)

[Rich](index.html)

[]

# Console Markup[](#console-markup "Link to this heading")

Rich supports a simple markup which you can use to insert color and styles virtually everywhere Rich would accept a string (e.g. [[`print()`]](reference/console.html#rich.console.Console.print "rich.console.Console.print") and [[`log()`]](reference/console.html#rich.console.Console.log "rich.console.Console.log")).

Run the following command to see some examples:

    python -m rich.markup

## Syntax[](#syntax "Link to this heading")

Console markup uses a syntax inspired by [bbcode](https://en.wikipedia.org/wiki/BBCode). If you write the style (see [[Styles]](style.html#styles)) in square brackets, e.g. [`[bold`]` `[`red]`], that style will apply until it is *closed* with a corresponding [`[/bold`]` `[`red]`].

Here's a simple example:

    from rich import print
    print("[bold red]alert![/bold red] Something happened")

If you don't close a style, it will apply until the end of the string. Which is sometimes convenient if you want to style a single line. For example:

    print("[bold italic yellow on red blink]This text is impossible to read")

There is a shorthand for closing a style. If you omit the style name from the closing tag, Rich will close the last style. For example:

    print("[bold red]Bold and red[/] not bold or red")

These markup tags may be use in combination with each other and don't need to be strictly nested. The following example demonstrates overlapping of markup tags:

    print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]")

### Errors[](#errors "Link to this heading")

Rich will raise [`MarkupError`] if the markup contains one of the following errors:

-   Mismatched tags, e.g. [`"[bold]Hello[/red]"`]

-   No matching tag for implicit close, e.g. [`"no`]` `[`tags[/]"`]

### Links[](#links "Link to this heading")

Console markup can output hyperlinks with the following syntax: [`[link=URL]text[/link]`]. Here's an example:

    print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")

If your terminal software supports hyperlinks, you will be able to click the word "blog" which will typically open a browser. If your terminal doesn't support hyperlinks, you will see the text but it won't be clickable.

### Escaping[](#escaping "Link to this heading")

Occasionally you may want to print something that Rich would interpret as markup. You can *escape* a tag by preceding it with a backslash. Here's an example:

    >>> from rich import print
    >>> print(r"foo\[bar]")
    foo[bar]

Without the backslash, Rich will assume that [`[bar]`] is a tag and remove it from the output if there is no "bar" style.

Note

If you want to prevent the backslash from escaping the tag and output a literal backslash before a tag you can enter two backslashes.

The function [[`escape()`]](reference/markup.html#rich.markup.escape "rich.markup.escape") will handle escaping of text for you.

Escaping is important if you construct console markup dynamically, with [`str.format`] or f strings (for example). Without escaping it may be possible to inject tags where you don't want them. Consider the following function:

    def greet(name):
        console.print(f"Hello !")

Calling [`greet("Will")`] will print a greeting, but if you were to call [`greet("[blink]Gotcha![/blink]")`] then you will also get blinking text, which may not be desirable. The solution is to escape the arguments:

    from rich.markup import escape
    def greet(name):
        console.print(f"Hello !")

### Emoji[](#emoji "Link to this heading")

If you add an *emoji code* to markup it will be replaced with the equivalent unicode character. An emoji code consists of the name of the emoji surrounded be colons (:). Here's an example:

    >>> from rich import print
    >>> print(":warning:")
    ⚠️

Some emojis have two variants, the "emoji" variant displays in full color, and the "text" variant displays in monochrome (whatever your default colors are set to). You can specify the variant you want by adding either "-emoji" or "-text" to the emoji code. Here's an example:

    >>> from rich import print
    >>> print(":red_heart-emoji:")
    >>> print(":red_heart-text:")

To see a list of all the emojis available, run the following command:

    python -m rich.emoji

## Rendering Markup[](#rendering-markup "Link to this heading")

By default, Rich will render console markup when you explicitly pass a string to [`print()`] or implicitly when you embed a string in another renderable object such as [[`Table`]](reference/table.html#rich.table.Table "rich.table.Table") or [[`Panel`]](reference/panel.html#rich.panel.Panel "rich.panel.Panel").

Console markup is convenient, but you may wish to disable it if the syntax clashes with the string you want to print. You can do this by setting [`markup=False`] on the [`print()`] method or on the [[`Console`]](reference/console.html#rich.console.Console "rich.console.Console") constructor.

## Markup API[](#markup-api "Link to this heading")

You can convert a string to styled text by calling [[`from_markup()`]](reference/text.html#rich.text.Text.from_markup "rich.text.Text.from_markup"), which returns a [[`Text`]](reference/text.html#rich.text.Text "rich.text.Text") instance you can print or add more styles to.

[[] Previous](style.html "Styles") [Next []](text.html "Rich Text")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).