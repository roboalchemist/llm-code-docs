# Source: https://rich.readthedocs.io/en/latest/reference/rule.html

[]

# rich.rule[](#module-rich.rule "Link to this heading")

*[[class]][ ]*[[rich.rule.]][[Rule]][(]*[[title]][[=]][[\'\']]*, *[[\*]]*, *[[characters]][[=]][[\'─\']]*, *[[style]][[=]][[\'rule.line\']]*, *[[end]][[=]][[\'\\n\']]*, *[[align]][[=]][[\'center\']]*[)][[[\[source\]]]](../_modules/rich/rule.html#Rule)[](#rich.rule.Rule "Link to this definition")

:   A console renderable to draw a horizontal rule (line).

    Parameters[:]

    :   -   **title** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\],* *optional*) -- Text to render in the rule. Defaults to "".

        -   **characters** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character(s) used to draw the line. Defaults to "─".

        -   **style** (*StyleType,* *optional*) -- Style of Rule. Defaults to "rule.line".

        -   **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- Character at end of Rule. defaults to "\\n"

        -   **align** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *optional*) -- How to align the title, one of "left", "center", or "right". Defaults to "center".

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).