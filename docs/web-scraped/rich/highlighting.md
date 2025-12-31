# Source: https://rich.readthedocs.io/en/latest/highlighting.html

[]

# Highlighting[](#highlighting "Link to this heading")

Rich will automatically highlight patterns in text, such as numbers, strings, collections, booleans, None, and a few more exotic patterns such as file paths, URLs and UUIDs.

You can disable highlighting either by setting [`highlight=False`] on [[`print()`]](reference/console.html#rich.console.Console.print "rich.console.Console.print") or [[`log()`]](reference/console.html#rich.console.Console.log "rich.console.Console.log"), or by setting [`highlight=False`] on the [[`Console`]](reference/console.html#rich.console.Console "rich.console.Console") constructor which disables it everywhere. If you disable highlighting on the constructor, you can still selectively *enable* highlighting with [`highlight=True`] on print / log.

## Custom Highlighters[](#custom-highlighters "Link to this heading")

If the default highlighting doesn't fit your needs, you can define a custom highlighter. The easiest way to do this is to extend the [[`RegexHighlighter`]](reference/highlighter.html#rich.highlighter.RegexHighlighter "rich.highlighter.RegexHighlighter") class which applies a style to any text matching a list of regular expressions.

Here's an example which highlights text that looks like an email address:

    from rich.console import Console
    from rich.highlighter import RegexHighlighter
    from rich.theme import Theme

    class EmailHighlighter(RegexHighlighter):
        """Apply style to anything that looks like an email."""

        base_style = "example."
        highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]

    theme = Theme()
    console = Console(highlighter=EmailHighlighter(), theme=theme)
    console.print("Send funds to money@example.org")

The [`highlights`] class variable should contain a list of regular expressions. The group names of any matching expressions are prefixed with the [`base_style`] attribute and used as styles for matching text. In the example above, any email addresses will have the style "example.email" applied, which we've defined in a custom [[Theme]](style.html#themes).

Setting the highlighter on the Console will apply highlighting to all text you print (if enabled). You can also use a highlighter on a more granular level by using the instance as a callable and printing the result. For example, we could use the email highlighter class like this:

    console = Console(theme=theme)
    highlight_emails = EmailHighlighter()
    console.print(highlight_emails("Send funds to money@example.org"))

While [[`RegexHighlighter`]](reference/highlighter.html#rich.highlighter.RegexHighlighter "rich.highlighter.RegexHighlighter") is quite powerful, you can also extend its base class [[`Highlighter`]](reference/highlighter.html#rich.highlighter.Highlighter "rich.highlighter.Highlighter") to implement a custom scheme for highlighting. It contains a single method [[`highlight`]](reference/highlighter.html#rich.highlighter.Highlighter.highlight "rich.highlighter.Highlighter.highlight") which is passed the [[`Text`]](reference/text.html#rich.text.Text "rich.text.Text") to highlight.

Here's a silly example that highlights every character with a different color:

    from random import randint

    from rich import print
    from rich.highlighter import Highlighter

    class RainbowHighlighter(Highlighter):
        def highlight(self, text):
            for index in range(len(text)):
                text.stylize(f"color()", index, index + 1)

    rainbow = RainbowHighlighter()
    print(rainbow("I must not fear. Fear is the mind-killer."))