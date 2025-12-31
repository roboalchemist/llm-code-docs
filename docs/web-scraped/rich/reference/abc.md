# Source: https://rich.readthedocs.io/en/latest/reference/abc.html

[]

# rich.abc[](#module-rich.abc "Link to this heading")

*[[class]][ ]*[[rich.abc.]][[RichRenderable]][[[\[source\]]]](../_modules/rich/abc.html#RichRenderable)[](#rich.abc.RichRenderable "Link to this definition")

:   An abstract base class for Rich renderables.

    Note that there is no need to extend this class, the intended use is to check if an object supports the Rich renderable protocol. For example:

    ::: 
    ::: highlight
        if isinstance(my_object, RichRenderable):
            console.print(my_object)
    :::
    :::

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).