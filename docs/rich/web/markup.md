# Source: https://rich.readthedocs.io/en/latest/markup.html

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