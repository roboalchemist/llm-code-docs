# Source: https://rich.readthedocs.io/en/latest/reference/tree.html

[]

# rich.tree[](#module-rich.tree "Link to this heading")

*[[class]][ ]*[[rich.tree.]][[Tree]][(]*[[label]]*, *[[\*]]*, *[[style]][[=]][[\'tree\']]*, *[[guide_style]][[=]][[\'tree.line\']]*, *[[expanded]][[=]][[True]]*, *[[highlight]][[=]][[False]]*, *[[hide_root]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/tree.html#Tree)[](#rich.tree.Tree "Link to this definition")

:   A renderable for a tree structure.

    [[ASCII_GUIDES]][](#rich.tree.Tree.ASCII_GUIDES "Link to this definition")

    :   Guide lines used when Console.ascii_only is True.

        Type[:]

        :   GuideType

    [[TREE_GUIDES]][](#rich.tree.Tree.TREE_GUIDES "Link to this definition")

    :   Default guide lines.

        Type[:]

        :   List\[GuideType, GuideType, GuideType\]

    Parameters[:]

    :   -   **label** (*RenderableType*) -- The renderable or str for the tree label.

        -   **style** (*StyleType,* *optional*) -- Style of this tree. Defaults to "tree".

        -   **guide_style** (*StyleType,* *optional*) -- Style of the guide lines. Defaults to "tree.line".

        -   **expanded** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also display children. Defaults to True.

        -   **highlight** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Highlight renderable (if str). Defaults to False.

        -   **hide_root** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Hide the root node. Defaults to False.

    [[add]][(]*[[label]]*, *[[\*]]*, *[[style]][[=]][[None]]*, *[[guide_style]][[=]][[None]]*, *[[expanded]][[=]][[True]]*, *[[highlight]][[=]][[False]]*[)][[[\[source\]]]](../_modules/rich/tree.html#Tree.add)[](#rich.tree.Tree.add "Link to this definition")

    :   Add a child tree.

        Parameters[:]

        :   -   **label** (*RenderableType*) -- The renderable or str for the tree label.

            -   **style** (*StyleType,* *optional*) -- Style of this tree. Defaults to "tree".

            -   **guide_style** (*StyleType,* *optional*) -- Style of the guide lines. Defaults to "tree.line".

            -   **expanded** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Also display children. Defaults to True.

            -   **highlight** (*Optional\[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*\],* *optional*) -- Highlight renderable (if str). Defaults to False.

        Returns[:]

        :   A new child Tree, which may be further modified.

        Return type[:]

        :   [Tree](#rich.tree.Tree "rich.tree.Tree")

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).