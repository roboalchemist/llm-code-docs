# Source: https://rich.readthedocs.io/en/latest/reference/markdown.html

[]

# rich.markdown[](#module-rich.markdown "Link to this heading")

*[[class]][ ]*[[rich.markdown.]][[BlockQuote]][[[\[source\]]]](../_modules/rich/markdown.html#BlockQuote)[](#rich.markdown.BlockQuote "Link to this definition")

:   A block quote.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#BlockQuote.on_child_close)[](#rich.markdown.BlockQuote.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[CodeBlock]][(]*[[lexer_name]]*, *[[theme]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#CodeBlock)[](#rich.markdown.CodeBlock "Link to this definition")

:   A code block with syntax highlighting.

    Parameters[:]

    :   -   **lexer_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#CodeBlock.create)[](#rich.markdown.CodeBlock.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[Heading]][(]*[[tag]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Heading)[](#rich.markdown.Heading "Link to this definition")

:   A heading.

    Parameters[:]

    :   **tag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Heading.create)[](#rich.markdown.Heading.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

    [[on_enter]][(]*[[context]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Heading.on_enter)[](#rich.markdown.Heading.on_enter "Link to this definition")

    :   Called when the node is entered.

        Parameters[:]

        :   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[HorizontalRule]][[[\[source\]]]](../_modules/rich/markdown.html#HorizontalRule)[](#rich.markdown.HorizontalRule "Link to this definition")

:   A horizontal rule to divide sections.

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[ImageItem]][(]*[[destination]]*, *[[hyperlinks]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ImageItem)[](#rich.markdown.ImageItem "Link to this definition")

:   Renders a placeholder for an image.

    Parameters[:]

    :   -   **destination** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **hyperlinks** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ImageItem.create)[](#rich.markdown.ImageItem.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Any*) -- A token from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

    [[on_enter]][(]*[[context]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ImageItem.on_enter)[](#rich.markdown.ImageItem.on_enter "Link to this definition")

    :   Called when the node is entered.

        Parameters[:]

        :   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[Link]][(]*[[text]]*, *[[href]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Link)[](#rich.markdown.Link "Link to this definition")

:   

    Parameters[:]

    :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **href** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Link.create)[](#rich.markdown.Link.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[ListElement]][(]*[[list_type]]*, *[[list_start]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ListElement)[](#rich.markdown.ListElement "Link to this definition")

:   A list element.

    Parameters[:]

    :   -   **list_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        -   **list_start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *\|* *None*)

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ListElement.create)[](#rich.markdown.ListElement.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

    [[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ListElement.on_child_close)[](#rich.markdown.ListElement.on_child_close "Link to this definition")

    :   Called when a child element is closed.

        This method allows a parent element to take over rendering of its children.

        Parameters[:]

        :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

            -   **child** (*MarkdownElement*) -- The child markdown element.

        Returns[:]

        :   Return True to render the element, or False to not render the element.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[ListItem]][[[\[source\]]]](../_modules/rich/markdown.html#ListItem)[](#rich.markdown.ListItem "Link to this definition")

:   An item in a list.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#ListItem.on_child_close)[](#rich.markdown.ListItem.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[Markdown]][(]*[[markup]]*, *[[code_theme]][[=]][[\'monokai\']]*, *[[justify]][[=]][[None]]*, *[[style]][[=]][[\'none\']]*, *[[hyperlinks]][[=]][[True]]*, *[[inline_code_lexer]][[=]][[None]]*, *[[inline_code_theme]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Markdown)[](#rich.markdown.Markdown "Link to this definition")

:   A Markdown renderable.

    Parameters[:]

    :   -   **markup** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- A string containing markdown.

        -   **code_theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Pygments theme for code blocks. Defaults to "monokai". See [https://pygments.org/styles/](https://pygments.org/styles/) for code themes.

        -   **justify** (*JustifyMethod,* *optional*) -- Justify value for paragraphs. Defaults to None.

        -   **style** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Style*](style.html#rich.style.Style "rich.style.Style")*\],* *optional*) -- Optional style to apply to markdown.

        -   **hyperlinks** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable hyperlinks. Defaults to [`True`].

        -   **inline_code_lexer** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *None*) -- (str, optional): Lexer to use if inline code highlighting is enabled. Defaults to None.

        -   **inline_code_theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *None*) -- (Optional\[str\], optional): Pygments theme for inline code highlighting, or None for no highlighting. Defaults to None.

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[MarkdownContext]][(]*[[console]]*, *[[options]]*, *[[style]]*, *[[inline_code_lexer]][[=]][[None]]*, *[[inline_code_theme]][[=]][[\'monokai\']]*[)][[[\[source\]]]](../_modules/rich/markdown.html#MarkdownContext)[](#rich.markdown.MarkdownContext "Link to this definition")

:   Manages the console render state.

    Parameters[:]

    :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console"))

        -   **options** ([*ConsoleOptions*](console.html#rich.console.ConsoleOptions "rich.console.ConsoleOptions"))

        -   **style** ([*Style*](style.html#rich.style.Style "rich.style.Style"))

        -   **inline_code_lexer** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* *None*)

        -   **inline_code_theme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

    *[[property]][ ]*[[current_style]]*[[:]][ ][[Style]](style.html#rich.style.Style "rich.style.Style")*[](#rich.markdown.MarkdownContext.current_style "Link to this definition")

    :   Current style which is the product of all styles on the stack.

    [[enter_style]][(]*[[style_name]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#MarkdownContext.enter_style)[](#rich.markdown.MarkdownContext.enter_style "Link to this definition")

    :   Enter a style context.

        Parameters[:]

        :   **style_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Style*](style.html#rich.style.Style "rich.style.Style"))

        Return type[:]

        :   [*Style*](style.html#rich.style.Style "rich.style.Style")

    [[leave_style]][(][)][[[\[source\]]]](../_modules/rich/markdown.html#MarkdownContext.leave_style)[](#rich.markdown.MarkdownContext.leave_style "Link to this definition")

    :   Leave a style context.

        Return type[:]

        :   [*Style*](style.html#rich.style.Style "rich.style.Style")

    [[on_text]][(]*[[text]]*, *[[node_type]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#MarkdownContext.on_text)[](#rich.markdown.MarkdownContext.on_text "Link to this definition")

    :   Called when the parser visits text.

        Parameters[:]

        :   -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

            -   **node_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[Paragraph]][(]*[[justify]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Paragraph)[](#rich.markdown.Paragraph "Link to this definition")

:   A Paragraph.

    Parameters[:]

    :   **justify** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")*\[\'default\',* *\'left\',* *\'center\',* *\'right\',* *\'full\'\]*)

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#Paragraph.create)[](#rich.markdown.Paragraph.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TableBodyElement]][[[\[source\]]]](../_modules/rich/markdown.html#TableBodyElement)[](#rich.markdown.TableBodyElement "Link to this definition")

:   MarkdownElement corresponding to tbody_open and tbody_close.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableBodyElement.on_child_close)[](#rich.markdown.TableBodyElement.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TableDataElement]][(]*[[justify]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableDataElement)[](#rich.markdown.TableDataElement "Link to this definition")

:   MarkdownElement corresponding to td_open and td_close and th_open and th_close.

    Parameters[:]

    :   **justify** (*JustifyMethod*)

    *[[classmethod]][ ]*[[create]][(]*[[markdown]]*, *[[token]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableDataElement.create)[](#rich.markdown.TableDataElement.create "Link to this definition")

    :   Factory to create markdown element,

        Parameters[:]

        :   -   **markdown** ([*Markdown*](#rich.markdown.Markdown "rich.markdown.Markdown")) -- The parent Markdown object.

            -   **token** (*Token*) -- A node from markdown-it.

        Returns[:]

        :   A new markdown element

        Return type[:]

        :   MarkdownElement

    [[on_text]][(]*[[context]]*, *[[text]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableDataElement.on_text)[](#rich.markdown.TableDataElement.on_text "Link to this definition")

    :   Called when text is parsed.

        Parameters[:]

        :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

            -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TableElement]][[[\[source\]]]](../_modules/rich/markdown.html#TableElement)[](#rich.markdown.TableElement "Link to this definition")

:   MarkdownElement corresponding to table_open.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableElement.on_child_close)[](#rich.markdown.TableElement.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TableHeaderElement]][[[\[source\]]]](../_modules/rich/markdown.html#TableHeaderElement)[](#rich.markdown.TableHeaderElement "Link to this definition")

:   MarkdownElement corresponding to thead_open and thead_close.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableHeaderElement.on_child_close)[](#rich.markdown.TableHeaderElement.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TableRowElement]][[[\[source\]]]](../_modules/rich/markdown.html#TableRowElement)[](#rich.markdown.TableRowElement "Link to this definition")

:   MarkdownElement corresponding to tr_open and tr_close.

```
<!-- -->
```

[[on_child_close]][(]*[[context]]*, *[[child]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TableRowElement.on_child_close)[](#rich.markdown.TableRowElement.on_child_close "Link to this definition")

:   Called when a child element is closed.

    This method allows a parent element to take over rendering of its children.

    Parameters[:]

    :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        -   **child** (*MarkdownElement*) -- The child markdown element.

    Returns[:]

    :   Return True to render the element, or False to not render the element.

    Return type[:]

    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[TextElement]][[[\[source\]]]](../_modules/rich/markdown.html#TextElement)[](#rich.markdown.TextElement "Link to this definition")

:   Base class for elements that render text.

    [[on_enter]][(]*[[context]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TextElement.on_enter)[](#rich.markdown.TextElement.on_enter "Link to this definition")

    :   Called when the node is entered.

        Parameters[:]

        :   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

        Return type[:]

        :   None

    [[on_leave]][(]*[[context]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TextElement.on_leave)[](#rich.markdown.TextElement.on_leave "Link to this definition")

    :   Called when the parser leaves the element.

        Parameters[:]

        :   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- \[description\]

        Return type[:]

        :   None

    [[on_text]][(]*[[context]]*, *[[text]]*[)][[[\[source\]]]](../_modules/rich/markdown.html#TextElement.on_text)[](#rich.markdown.TextElement.on_text "Link to this definition")

    :   Called when text is parsed.

        Parameters[:]

        :   -   **context** ([*MarkdownContext*](#rich.markdown.MarkdownContext "rich.markdown.MarkdownContext")) -- The markdown context.

            -   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        Return type[:]

        :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.markdown.]][[UnknownElement]][[[\[source\]]]](../_modules/rich/markdown.html#UnknownElement)[](#rich.markdown.UnknownElement "Link to this definition")

:   An unknown element.

    Hopefully there will be no unknown elements, and we will have a MarkdownElement for everything in the document.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).