# Source: https://rich.readthedocs.io/en/latest/style.html

[]

# Styles[](#styles "Link to this heading")

In various places in the Rich API you can set a "style" which defines the color of the text and various attributes such as bold, italic etc. A style may be given as a string containing a *style definition* or as an instance of a [[`Style`]](reference/style.html#rich.style.Style "rich.style.Style") class.

## Defining Styles[](#defining-styles "Link to this heading")

A style definition is a string containing one or more words to set colors and attributes.

To specify a foreground color use one of the 256 [[Standard Colors]](appendix/colors.html#appendix-colors). For example, to print "Hello" in magenta:

    console.print("Hello", style="magenta")

You may also use the color's number (an integer between 0 and 255) with the syntax [`"color(<number>)"`]. The following will give the equivalent output:

    console.print("Hello", style="color(5)")

Alternatively you can use a CSS-like syntax to specify a color with a "#" followed by three pairs of hex characters, or in RGB form with three decimal integers. The following two lines both print "Hello" in the same color (purple):

    console.print("Hello", style="#af00ff")
    console.print("Hello", style="rgb(175,0,255)")

The hex and rgb forms allow you to select from the full *truecolor* set of 16.7 million colors.

Note

Some terminals only support 256 colors. Rich will attempt to pick the closest color it can if your color isn't available.

By itself, a color will change the *foreground* color. To specify a *background* color, precede the color with the word "on". For example, the following prints text in red on a white background:

    console.print("DANGER!", style="red on white")

You can also set a color with the word [`"default"`] which will reset the color to a default managed by your terminal software. This works for backgrounds as well, so the style of [`"default`]` `[`on`]` `[`default"`] is what your terminal starts with.

You can set a style attribute by adding one or more of the following words:

-   [`"bold"`] or [`"b"`] for bold text.

-   [`"blink"`] for text that flashes (use this one sparingly).

-   [`"blink2"`] for text that flashes rapidly (not supported by most terminals).

-   [`"conceal"`] for *concealed* text (not supported by most terminals).

-   [`"italic"`] or [`"i"`] for italic text (not supported on Windows).

-   [`"reverse"`] or [`"r"`] for text with foreground and background colors reversed.

-   [`"strike"`] or [`"s"`] for text with a line through it.

-   [`"underline"`] or [`"u"`] for underlined text.

Rich also supports the following styles, which are not well supported and may not display in your terminal:

-   [`"underline2"`] or [`"uu"`] for doubly underlined text.

-   [`"frame"`] for framed text.

-   [`"encircle"`] for encircled text.

-   [`"overline"`] or [`"o"`] for overlined text.

Style attributes and colors may be used in combination with each other. For example:

    console.print("Danger, Will Robinson!", style="blink bold red underline on white")

Styles may be negated by prefixing the attribute with the word "not". This can be used to turn off styles if they overlap. For example:

    console.print("foo [not bold]bar[/not bold] baz", style="bold")

This will print "foo" and "baz" in bold, but "bar" will be in normal text.

Styles may also have a [`"link"`] attribute, which will turn any styled text in to a *hyperlink* (if supported by your terminal software).

To add a link to a style, the definition should contain the word [`"link"`] followed by a URL. The following example will make a clickable link:

    console.print("Google", style="link https://google.com")

Note

If you are familiar with HTML you may find applying links in this way a little odd, but the terminal considers a link to be another attribute just like bold, italic etc.