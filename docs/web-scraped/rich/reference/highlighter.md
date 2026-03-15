# Source: https://rich.readthedocs.io/en/latest/reference/highlighter.html

[]

# rich.highlighter[](#module-rich.highlighter "Link to this heading")

*[[class]][ ]*[[rich.highlighter.]][[Highlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#Highlighter)[](#rich.highlighter.Highlighter "Link to this definition")

:   Abstract base class for highlighters.

    [[\_\_call\_\_]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/highlighter.html#Highlighter.__call__)[](#rich.highlighter.Highlighter.__call__ "Link to this definition")

    :   Highlight a str or Text instance.

        Parameters[:]

        :   **text** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *\~Text\]*) -- Text to highlight.

        Raises[:]

        :   [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") -- If not called with text or str.

        Returns[:]

        :   A test instance with highlighting applied.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

    *[[abstractmethod]][ ]*[[highlight]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/highlighter.html#Highlighter.highlight)[](#rich.highlighter.Highlighter.highlight "Link to this definition")

    :   Apply highlighting in place to text.

        Parameters[:]

        :   **text** (*\~Text*) -- A text object highlight.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.highlighter.]][[ISO8601Highlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#ISO8601Highlighter)[](#rich.highlighter.ISO8601Highlighter "Link to this definition")

:   Highlights the ISO8601 date time strings. Regex reference: [https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s07.html](https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s07.html)

```
<!-- -->
```

*[[class]][ ]*[[rich.highlighter.]][[JSONHighlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#JSONHighlighter)[](#rich.highlighter.JSONHighlighter "Link to this definition")

:   Highlights JSON

    [[highlight]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/highlighter.html#JSONHighlighter.highlight)[](#rich.highlighter.JSONHighlighter.highlight "Link to this definition")

    :   Highlight [[`rich.text.Text`]](text.html#rich.text.Text "rich.text.Text") using regular expressions.

        Parameters[:]

        :   **text** (*\~Text*) -- Text to highlighted.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.highlighter.]][[NullHighlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#NullHighlighter)[](#rich.highlighter.NullHighlighter "Link to this definition")

:   A highlighter object that doesn't highlight.

    May be used to disable highlighting entirely.

    [[highlight]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/highlighter.html#NullHighlighter.highlight)[](#rich.highlighter.NullHighlighter.highlight "Link to this definition")

    :   Nothing to do

        Parameters[:]

        :   **text** ([*Text*](text.html#rich.text.Text "rich.text.Text"))

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.highlighter.]][[RegexHighlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#RegexHighlighter)[](#rich.highlighter.RegexHighlighter "Link to this definition")

:   Applies highlighting from a list of regular expressions.

    [[highlight]][(]*[[text]]*[)][[[\[source\]]]](../_modules/rich/highlighter.html#RegexHighlighter.highlight)[](#rich.highlighter.RegexHighlighter.highlight "Link to this definition")

    :   Highlight [[`rich.text.Text`]](text.html#rich.text.Text "rich.text.Text") using regular expressions.

        Parameters[:]

        :   **text** (*\~Text*) -- Text to highlighted.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.highlighter.]][[ReprHighlighter]][[[\[source\]]]](../_modules/rich/highlighter.html#ReprHighlighter)[](#rich.highlighter.ReprHighlighter "Link to this definition")

:   Highlights the text typically produced from [`__repr__`] methods.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).