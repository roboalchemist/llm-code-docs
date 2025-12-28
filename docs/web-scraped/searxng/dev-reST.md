# Source: https://docs.searxng.org/dev/reST.html

[]

# reST primer[¶](#rest-primer "Link to this heading")

[KISS](https://en.wikipedia.org/wiki/KISS_principle) and [readability](https://docs.python-guide.org/writing/style/)

Instead of defining more and more roles, we at SearXNG encourage our contributors to follow principles like [KISS](https://en.wikipedia.org/wiki/KISS_principle) and [readability](https://docs.python-guide.org/writing/style/).

We at SearXNG are using reStructuredText (aka [reST](https://docutils.sourceforge.io/rst.html)) markup for all kind of documentation. With the builders from the [Sphinx](https://www.sphinx-doc.org) project a HTML output is generated and deployed at [docs.searxng.org](https://docs.searxng.org/). For build prerequisites read [[Build docs]](../admin/buildhosts.html#docs-build).

The source files of SearXNG's documentation are located at [git://docs](https://github.com/searxng/searxng/blob/master/docs). Sphinx assumes source files to be encoded in UTF-8 by default. Run [[make docs.live]](contribution_guide.html#make-docs-live) to build HTML while editing.

Further reading

-   [Sphinx-Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

-   [Sphinx markup constructs](https://www.sphinx-doc.org/en/stable/markup/index.html)

-   [reST](https://docutils.sourceforge.io/rst.html), [docutils](http://docutils.sourceforge.net/docs/index.html), [docutils FAQ](http://docutils.sourceforge.net/FAQ.html)

-   [Sphinx](https://www.sphinx-doc.org), [sphinx-doc FAQ](https://www.sphinx-doc.org/en/stable/faq.html)

-   [sphinx config](https://www.sphinx-doc.org/en/stable/config.html), [doctree](https://www.sphinx-doc.org/en/master/extdev/tutorial.html?highlight=doctree#build-phases)

-   [sphinx cross references](https://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-arbitrary-locations)

-   [linuxdoc](https://return42.github.io/linuxdoc)

-   [intersphinx](https://www.sphinx-doc.org/en/stable/ext/intersphinx.html)

-   [sphinx-jinja](https://github.com/tardyp/sphinx-jinja)

-   [Sphinx's autodoc](https://www.sphinx-doc.org/en/stable/ext/autodoc.html)

-   [Sphinx's Python domain](https://www.sphinx-doc.org/en/stable/domains.html#the-python-domain), [Sphinx's C domain](https://www.sphinx-doc.org/en/stable/domains.html#cross-referencing-c-constructs)

-   [SVG](https://www.w3.org/TR/SVG11/expanded-toc.html), [ImageMagick](https://www.imagemagick.org)

-   [DOT](https://graphviz.gitlab.io/_pages/doc/info/lang.html), [Graphviz's dot](https://graphviz.gitlab.io/_pages/pdf/dotguide.pdf), [Graphviz](https://graphviz.gitlab.io)

```
<!-- -->
```
-   [Soft skills](#soft-skills)

-   [Basic inline markup](#basic-inline-markup)

-   [Basic article structure](#basic-article-structure)

    -   [reST template](#rest-template)

    -   [Headings](#headings)

-   [Anchors & Links](#anchors-links)

    -   [Anchors](#anchors)

    -   [Link ordinary URL](#link-ordinary-url)

    -   [Smart refs](#smart-refs)

-   [Literal blocks](#literal-blocks)

    -   [[`::`]](#rest-literal)

    -   [[`code-block`]](#code-block)

-   [Unicode substitution](#unicode-substitution)

-   [Roles](#roles)

-   [Figures & Images](#figures-images)

    -   [DOT files (aka Graphviz)](#dot-files-aka-graphviz)

    -   [[`kernel-render`] DOT](#kernel-render-dot)

    -   [[`kernel-render`] SVG](#kernel-render-svg)

-   [List markups](#list-markups)

    -   [Bullet list](#bullet-list)

    -   [Horizontal list](#horizontal-list)

    -   [Definition list](#definition-list)

    -   [Quoted paragraphs](#quoted-paragraphs)

    -   [Field Lists](#field-lists)

    -   [Further list blocks](#further-list-blocks)

-   [Admonitions](#admonitions)

    -   [Sidebar](#sidebar)

    -   [Generic admonition](#generic-admonition)

    -   [Specific admonitions](#specific-admonitions)

-   [Tables](#tables)

    -   [Simple tables](#simple-tables)

    -   [Grid tables](#grid-tables)

    -   [flat-table](#flat-table)

    -   [CSV table](#csv-table)

-   [Templating](#templating)

-   [Tabbed views](#tabbed-views)

-   [Math equations](#math-equations)

[Sphinx](https://www.sphinx-doc.org) and [reST](https://docutils.sourceforge.io/rst.html) have their place in the python ecosystem. Over that reST is used in popular projects, e.g the Linux kernel documentation [\[kernel doc\]](https://www.kernel.org/doc/html/latest/doc-guide/sphinx.html).

Content matters

The [readability](https://docs.python-guide.org/writing/style/) of the reST sources has its value, therefore we recommend to make sparse usage of reST markup / .. content matters!

**reST** is a plaintext markup language, its markup is *mostly* intuitive and you will not need to learn much to produce well formed articles with. I use the word *mostly*: like everything in live, reST has its advantages and disadvantages, some markups feel a bit grumpy (especially if you are used to other plaintext markups).

## [Soft skills](#id15)[¶](#soft-skills "Link to this heading")

Before going any deeper into the markup let's face on some **soft skills** a trained author brings with, to reach a well feedback from readers:

-   Documentation is dedicated to an audience and answers questions from the audience point of view.

-   Don't detail things which are general knowledge from the audience point of view.

-   Limit the subject, use cross links for any further reading.

To be more concrete what a *point of view* means. In the ([git://docs](https://github.com/searxng/searxng/blob/master/docs)) folder we have three sections (and the *blog* folder), each dedicate to a different group of audience.

User's POV: [git://docs/user](https://github.com/searxng/searxng/blob/master/docs/user)

:   A typical user knows about search engines and might have heard about meta crawlers and privacy.

Admin's POV: [git://docs/admin](https://github.com/searxng/searxng/blob/master/docs/admin)

:   A typical Admin knows about setting up services on a linux system, but he does not know all the pros and cons of a SearXNG setup.

Developer's POV: [git://docs/dev](https://github.com/searxng/searxng/blob/master/docs/dev)

:   Depending on the [readability](https://docs.python-guide.org/writing/style/) of code, a typical developer is able to read and understand source code. Describe what a item aims to do (e.g. a function). If the chronological order matters, describe it. Name the *out-of-limits conditions* and all the side effects a external developer will not know.

[]

## [Basic inline markup](#id16)[¶](#basic-inline-markup "Link to this heading")

Inline markup

-   [[Roles]](#rest-roles)

-   [[Smart refs]](#rest-smart-ref)

Basic inline markup is done with asterisks and backquotes. If asterisks or backquotes appear in running text and could be confused with inline markup delimiters, they have to be escaped with a backslash ([`\*pointer`]).

+------------------------------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description                              | rendered                                         | markup                                                                                                                                                                                                                                                                                                  |
+==========================================+==================================================+=========================================================================================================================================================================================================================================================================================================+
| one asterisk for emphasis                | *italics*                                        | [`*italics*`]                                                                                                                                                                                                                                                    |
+------------------------------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| two asterisks for strong emphasis        | **boldface**                                     | [`**boldface**`]                                                                                                                                                                                                                                                 |
+------------------------------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| backquotes for code samples and literals | [`foo()`] | [``` ``foo()`` ```]                                                                                                                                                                                                                                              |
+------------------------------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| quote asterisks or backquotes            | \*foo is a pointer                               | [`\*foo`]` `[`is`]` `[`a`]` `[`pointer`] |
+------------------------------------------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: [Table 9 ][basic inline markup][¶](#id4 "Link to this table")

[]

## [Basic article structure](#id17)[¶](#basic-article-structure "Link to this heading")

The basic structure of an article makes use of heading adornments to markup chapter, sections and subsections.

[]

### [reST template](#id18)[¶](#rest-template "Link to this heading")

reST template for an simple article:

    .. _doc refname:

    ==============
    Document title
    ==============

    Lorem ipsum dolor sit amet, consectetur adipisici elit ..  Further read
    :ref:`chapter refname`.

    .. _chapter refname:

    Chapter
    =======

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquid ex ea commodi consequat ...

    .. _section refname:

    Section
    -------

    lorem ..

    .. _subsection refname:

    Subsection
    ~~~~~~~~~~

    lorem ..

### [Headings](#id19)[¶](#headings "Link to this heading")

1.  title - with overline for document title:

> <div>
>
> ::: 
> ::: highlight
>     ==============
>     Document title
>     ==============
> :::
> :::
>
> </div>

1.  chapter - with anchor named [`anchor`]` `[`name`]:

    ::: 
    ::: highlight
        .. _anchor name:

        Chapter
        =======
    :::
    :::

2.  section

    ::: 
    ::: highlight
        Section
        -------
    :::
    :::

3.  subsection

    ::: 
    ::: highlight
        Subsection
        ~~~~~~~~~~
    :::
    :::

## [Anchors & Links](#id20)[¶](#anchors-links "Link to this heading")

[]

### [Anchors](#id21)[¶](#anchors "Link to this heading")

To refer a point in the documentation a anchor is needed. The [[reST template]](#rest-template) shows an example where a chapter titled *"Chapters"* gets an anchor named [`chapter`]` `[`title`]. Another example from *this* document, where the anchor named [`reST`]` `[`anchor`]:

    .. _reST anchor:

    Anchors
    -------

    To refer a point in the documentation a anchor is needed ...

To refer anchors use the [ref role](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref) markup:

    Visit chapter :ref:`reST anchor`.  Or set hyperlink text manually :ref:`foo
    bar <reST anchor>`.

[`:ref:`] role

Visit chapter [[Anchors]](#rest-anchor). Or set hyperlink text manually [[foo bar]](#rest-anchor).

[]

### [Link ordinary URL](#id22)[¶](#link-ordinary-url "Link to this heading")

If you need to reference external URLs use *named* hyperlinks to maintain readability of reST sources. Here is a example taken from *this* article:

    .. _Sphinx Field Lists:
       https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html

    With the *named* hyperlink `Sphinx Field Lists`_, the raw text is much more
    readable.

    And this shows the alternative (less readable) hyperlink markup `Sphinx Field
    Lists
    <https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html>`__.

Named hyperlink

With the *named* hyperlink [Sphinx Field Lists](https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html), the raw text is much more readable.

And this shows the alternative (less readable) hyperlink markup [Sphinx Field Lists](https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html).

[]

### [Smart refs](#id23)[¶](#smart-refs "Link to this heading")

With the power of [sphinx.ext.extlinks](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html) and [intersphinx](https://www.sphinx-doc.org/en/stable/ext/intersphinx.html) referencing external content becomes smart.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| refer ...                                                                                                                                                                                            | rendered example                                                                                                                                                                              | markup                                                                     |
+======================================================================================================================================================================================================+===============================================================================================================================================================================================+============================================================================+
| [[`rfc`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-rfc "(in Sphinx v9.1.0rc1)") | [][**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)                                                                               | [`` :rfc:`822` ``]                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| [[`pep`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-pep "(in Sphinx v9.1.0rc1)") | [][**PEP 8**](https://peps.python.org/pep-0008/)                                                                                                 | [`` :pep:`8` ``]                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| [sphinx.ext.extlinks](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html)                                                                                     |                                                                                                                                                                                               |                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| project's wiki article                                                                                                                                                                               | [Offline-engines](https://github.com/searxng/searxng/wiki/Offline-engines)                                                                                | [`` :wiki:`Offline-engines` ``]     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| to docs public URL                                                                                                                                                                                   | [docs: dev/reST.html](https://docs.searxng.org//dev/reST.html)                                                                                            | [`` :docs:`dev/reST.html` ``]       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| files & folders origin                                                                                                                                                                               | [git://docs/dev/reST.rst](https://github.com/searxng/searxng/blob/master/docs/dev/reST.rst)                                                             | [`` :origin:`docs/dev/reST.rst` ``] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| pull request                                                                                                                                                                                         | [PR 4](https://github.com/searxng/searxng/pull/4)                                                                                                         | [`` :pull:`4` ``]                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| patch                                                                                                                                                                                                | [#af2cae6](https://github.com/searxng/searxng/commit/af2cae6)                                                                                            | [`` :patch:`af2cae6` ``]            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| PyPi package                                                                                                                                                                                         | [PyPi: httpx](https://pypi.org/project/httpx)                                                                                                             | [`` :pypi:`httpx` ``]               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| manual page man                                                                                                                                                                                      | [bash](https://manpages.debian.org/jump?q=bash)                                                                                                            | [`` :man:`bash` ``]                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| [intersphinx](https://www.sphinx-doc.org/en/stable/ext/intersphinx.html)                                                                                                       |                                                                                                                                                                                               |                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| external anchor                                                                                                                                                                                      | [Boolean operations](https://docs.python.org/3/reference/expressions.html#and "(in Python v3.14)")                                                                      | [`` :ref:`python:and` ``]           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| external doc anchor                                                                                                                                                                                  | [Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/ "(in Jinja v3.1.x)")                                                           | [`` :doc:`jinja:templates` ``]      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| python code object                                                                                                                                                                                   | [[`datetime.datetime`]](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [`` :py:obj:`datetime.datetime` ``] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| flask code object                                                                                                                                                                                    | [[`flask.Flask`]](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "(in Flask v3.1.x)")            | [`` :py:obj:`flask.Flask` ``]       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

: [Table 10 ][smart refs with [sphinx.ext.extlinks](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html) and [intersphinx](https://www.sphinx-doc.org/en/stable/ext/intersphinx.html)][¶](#id5 "Link to this table")

Intersphinx is configured in [git://docs/conf.py](https://github.com/searxng/searxng/blob/master/docs/conf.py):

    intersphinx_mapping = 

To list all anchors of the inventory (e.g. [`python`]) use:

    $ python -m sphinx.ext.intersphinx https://docs.python.org/3/objects.inv
    ...
    $ python -m sphinx.ext.intersphinx https://docs.searxng.org/objects.inv
    ...

## [Literal blocks](#id24)[¶](#literal-blocks "Link to this heading")

The simplest form of [literal-blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks) is a indented block introduced by two colons ([`::`]). For highlighting use [highlight](https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlight) or [[code-block]](#rest-code) directive. To include literals from external files use [[`literalinclude`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude "(in Sphinx v9.1.0rc1)") or [[kernel-include]](https://return42.github.io/linuxdoc/linuxdoc-howto/kernel-include-directive.html#kernel-include-directive "(in LinuxDoc v20240924.dev1)") directive (latter one expands environment variables in the path name).

[]

### [[`::`]](#id25)[¶](#rest-literal "Link to this heading")

    ::

      Literal block

    Lorem ipsum dolor::

      Literal block

    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore ::

      Literal block

Literal block

    Literal block

Lorem ipsum dolor:

    Literal block

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore

    Literal block

[]

### [[`code-block`]](#id26)[¶](#code-block "Link to this heading")

Syntax highlighting

is handled by [pygments](https://pygments.org/languages/).

The [[`code-block`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block "(in Sphinx v9.1.0rc1)") directive is a variant of the [code](https://docutils.sourceforge.io/docs/ref/rst/directives.html#code) directive with additional options. To learn more about code literals visit [Showing code examples](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#code-examples "(in Sphinx v9.1.0rc1)").

    The URL ``/stats`` handle is shown in :ref:`stats-handle`

    .. code-block:: Python
       :caption: python code block
       :name: stats-handle

       @app.route('/stats', methods=['GET'])
       def stats():
           """Render engine statistics page."""
           stats = get_engines_stats()
           return render(
               'stats.html'
               , stats = stats )

Code block

The URL [`/stats`] handle is shown in [[python code block]](#stats-handle)

[Listing 1 ][python code block][¶](#stats-handle "Link to this code")

    @app.route('/stats', methods=['GET'])
    def stats():
        """Render engine statistics page."""
        stats = get_engines_stats()
        return render(
            'stats.html'
            , stats = stats )

## [Unicode substitution](#id27)[¶](#unicode-substitution "Link to this heading")

The [unicode directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#unicode-character-codes) converts Unicode character codes (numerical values) to characters. This directive can only be used within a substitution definition.

    .. |copy| unicode:: 0xA9 .. copyright sign
    .. |(TM)| unicode:: U+2122

    Trademark |(TM)| and copyright |copy| glyphs.

Unicode

Trademark ™ and copyright © glyphs.

[]

## [Roles](#id28)[¶](#roles "Link to this heading")

Further reading

-   [Sphinx Roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)

-   [MOVED: Domains](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html "(in Sphinx v9.1.0rc1)")

A *custom interpreted text role* ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#roles)) is an inline piece of explicit markup. It signifies that that the enclosed text should be interpreted in a specific way.

The general markup is one of:

    :rolename:`ref-name`
    :rolename:`ref text <ref-name>`

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| role                                                                                                                                                                                                                     | rendered example                                                                                                                                                                                                                                                                          | markup                                                                                                                                                                                                                                                                                                                                                                                             |
+==========================================================================================================================================================================================================================+===========================================================================================================================================================================================================================================================================================+====================================================================================================================================================================================================================================================================================================================================================================================================+
| [[`guilabel`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-guilabel "(in Sphinx v9.1.0rc1)")           | [[C]ancel]                                                                                                                                                                                                                                                       | [`` :guilabel:`&Cancel` ``]                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`kbd`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-kbd "(in Sphinx v9.1.0rc1)")                     | [C]-[x] [C]-[f]                                                                                               | [`` :kbd:`C-x ``]` `[`` C-f` ``]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`menuselection`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-menuselection "(in Sphinx v9.1.0rc1)") | [Open ‣ File]                                                                                                                                                                                                                                                             | [`` :menuselection:`Open ``]` `[`-->`]` `[`` File` ``]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`download`]](https://www.sphinx-doc.org/en/master/usage/referencing.html#role-download "(in Sphinx v9.1.0rc1)")                      | [[`this`]` `[`file`]](../_downloads/ad0ebe55d6b53b1559e0ca8dee6f30b9/reST.rst) | [`` :download:`this ``]` `[`file`]` `[`` <reST.rst>` ``]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [math](#math)                                                                                                                                                                                      | [a\^2 + b\^2 = c\^2]                                                                                                                                                                                                                                                               | [`` :math:`a^2 ``]` `[`+`]` `[`b^2`]` `[`=`]` `[`` c^2` ``] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`ref`]](https://www.sphinx-doc.org/en/master/usage/referencing.html#role-ref "(in Sphinx v9.1.0rc1)")                                | [[Simple SVG image.]](#svg-image-example)                                                                                                                                                                                                            | [`` :ref:`svg ``]` `[`image`]` `[`` example` ``]                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [[`command`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-command "(in Sphinx v9.1.0rc1)")             | **ls -la**                                                                                                                                                                                                                                                                                | [`` :command:`ls ``]` `[`` -la` ``]                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [emphasis](https://docutils.sourceforge.io/docs/ref/rst/roles.html#emphasis)                                                                                                       | *italic*                                                                                                                                                                                                                                                                                  | [`` :emphasis:`italic` ``]                                                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [strong](https://docutils.sourceforge.io/docs/ref/rst/roles.html#strong)                                                                                                           | **bold**                                                                                                                                                                                                                                                                                  | [`` :strong:`bold` ``]                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [literal](https://docutils.sourceforge.io/docs/ref/rst/roles.html#literal)                                                                                                         | [`foo()`]                                                                                                                                                                                                                                          | [`` :literal:`foo()` ``]                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [subscript](https://docutils.sourceforge.io/docs/ref/rst/roles.html#subscript)                                                                                                     | H~2~O                                                                                                                                                                                                                                                                                     | [`H\`]` `[`` :sub:`2`\ ``]` `[`O`]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [superscript](https://docutils.sourceforge.io/docs/ref/rst/roles.html#superscript)                                                                                                 | E = mc^2^                                                                                                                                                                                                                                                                                 | [`E`]` `[`=`]` `[`mc\`]` `[`` :sup:`2` ``]                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [title-reference](https://docutils.sourceforge.io/docs/ref/rst/roles.html#title-reference)                                                                                         | Time                                                                                                                                                                                                                                                                                      | [`` :title:`Time` ``]                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: [Table 11 ][smart refs with [sphinx.ext.extlinks](https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html) and [intersphinx](https://www.sphinx-doc.org/en/stable/ext/intersphinx.html)][¶](#id6 "Link to this table")

## [Figures & Images](#id29)[¶](#figures-images "Link to this heading")

Image processing

With the directives from [[linuxdoc]](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kfigure "(in LinuxDoc v20240924.dev1)") the build process is flexible. To get best results in the generated output format, install [ImageMagick](https://www.imagemagick.org) and [Graphviz](https://graphviz.gitlab.io).

SearXNG's sphinx setup includes: [Scalable figure and image handling](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kfigure "(in LinuxDoc v20240924.dev1)"). Scalable here means; scalable in sense of the build process. Normally in absence of a converter tool, the build process will break. From the authors POV it's annoying to care about the build process when handling with images, especially since he has no access to the build process. With [Scalable figure and image handling](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kfigure "(in LinuxDoc v20240924.dev1)") the build process continues and scales output quality in dependence of installed image processors.

If you want to add an image, you should use the [`kernel-figure`] (inheritance of [figure](https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure)) and [`kernel-image`] (inheritance of [image](https://docutils.sourceforge.io/docs/ref/rst/directives.html#image)) directives. E.g. to insert a figure with a scalable image format use SVG ([[Simple SVG image.]](#svg-image-example)):

    .. _svg image example:

    .. kernel-figure:: svg_image.svg
       :alt: SVG image example

       Simple SVG image

     To refer the figure, a caption block is needed: :ref:`svg image example`.

<figure id="id7" class="align-default">
<img src="../_images/svg_image.svg" alt="SVG image example" />
<figcaption><p><span class="caption-number">Fig. 4 </span><span class="caption-text">Simple SVG image.</span><a href="#id7" class="headerlink" title="Link to this image">¶</a></p></figcaption>
</figure>

To refer the figure, a caption block is needed: [[Simple SVG image.]](#svg-image-example).

### [DOT files (aka Graphviz)](#id30)[¶](#dot-files-aka-graphviz "Link to this heading")

With [kernel-figure & kernel-image](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kernel-figure "(in LinuxDoc v20240924.dev1)") reST support for **DOT** formatted files is given.

-   [Graphviz's dot](https://graphviz.gitlab.io/_pages/pdf/dotguide.pdf)

-   [DOT](https://graphviz.gitlab.io/_pages/doc/info/lang.html)

-   [Graphviz](https://graphviz.gitlab.io)

A simple example is shown in [[DOT's hello world example]](#dot-file-example):

    .. _dot file example:

    .. kernel-figure:: hello.dot
       :alt: hello world

       DOT's hello world example

hello.dot

<figure id="id8" class="align-default">
<div class="highlight-default notranslate">
<div class="highlight">
<pre><code>graph G </code></pre>
</div>
</div>
<figcaption><p><span class="caption-number">Fig. 5 </span><span class="caption-text">DOT’s hello world example</span><a href="#id8" class="headerlink" title="Link to this image">¶</a></p></figcaption>
</figure>

### [[`kernel-render`] DOT](#id31)[¶](#kernel-render-dot "Link to this heading")

Embed *render* markups (or languages) like Graphviz's **DOT** is provided by the [kernel-render](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kernel-render "(in LinuxDoc v20240924.dev1)") directive. A simple example of embedded [DOT](https://graphviz.gitlab.io/_pages/doc/info/lang.html) is shown in figure [[Embedded DOT (Graphviz) code]](#dot-render-example):

    .. _dot render example:

    .. kernel-render:: DOT
       :alt: digraph
       :caption: Embedded  DOT (Graphviz) code

       digraph foo 

    Attribute ``caption`` is needed, if you want to refer the figure: :ref:`dot
    render example`.

Please note [[build tools]](https://return42.github.io/linuxdoc/linuxdoc-howto/kfigure.html#kfigure-build-tools "(in LinuxDoc v20240924.dev1)"). If [Graphviz](https://graphviz.gitlab.io) is installed, you will see an vector image. If not, the raw markup is inserted as *literal-block*.

kernel-render DOT

<figure id="id9" class="align-default">
<span id="dot-render-example"></span>
<div class="highlight-default notranslate">
<div class="highlight">
<pre><code>digraph foo </code></pre>
</div>
</div>
<figcaption><p><span class="caption-number">Fig. 6 </span><span class="caption-text">Embedded DOT (Graphviz) code</span><a href="#id9" class="headerlink" title="Link to this image">¶</a></p></figcaption>
</figure>

Attribute [`caption`] is needed, if you want to refer the figure: [[Embedded DOT (Graphviz) code]](#dot-render-example).

### [[`kernel-render`] SVG](#id32)[¶](#kernel-render-svg "Link to this heading")

A simple example of embedded [SVG](https://www.w3.org/TR/SVG11/expanded-toc.html) is shown in figure [[Embedded SVG markup]](#svg-render-example):

    .. _svg render example:

    .. kernel-render:: SVG
       :caption: Embedded **SVG** markup
       :alt: so-nw-arrow

> <div>
>
> ::: 
> ::: highlight
>     <?xml version="1.0" encoding="UTF-8"?>
>     <svg xmlns="http://www.w3.org/2000/svg" version="1.1"
>          baseProfile="full" width="70px" height="40px"
>          viewBox="0 0 700 400"
>          >
>       <line x1="180" y1="370"
>             x2="500" y2="50"
>             stroke="black" stroke-width="15px"
>             />
>       <polygon points="585 0 525 25 585 50"
>                transform="rotate(135 525 25)"
>                />
>     </svg>
> :::
> :::
>
> </div>

kernel-render SVG

<figure id="id10" class="align-default">
<span id="svg-render-example"></span><img src="../_images/SVG-1fb7029fa2cc454a267bae271cccb2c591387416.svg" alt="so-nw-arrow" />
<figcaption><p><span class="caption-number">Fig. 7 </span><span class="caption-text">Embedded <strong>SVG</strong> markup</span><a href="#id10" class="headerlink" title="Link to this image">¶</a></p></figcaption>
</figure>

[]

## [List markups](#id33)[¶](#list-markups "Link to this heading")

### [Bullet list](#id34)[¶](#bullet-list "Link to this heading")

List markup ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists)) is simple:

    - This is a bulleted list.

      1. Nested lists are possible, but be aware that they must be separated from
         the parent list items by blank line
      2. Second item of nested list

    - It has two items, the second
      item uses two lines.

    #. This is a numbered list.
    #. It has two items too.

bullet list

-   This is a bulleted list.

    1.  Nested lists are possible, but be aware that they must be separated from the parent list items by blank line

    2.  Second item of nested list

-   It has two items, the second item uses two lines.

1.  This is a numbered list.

2.  It has two items too.

### [Horizontal list](#id35)[¶](#horizontal-list "Link to this heading")

The [[`..`]` `[`hlist::`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-hlist "(in Sphinx v9.1.0rc1)") transforms a bullet list into a more compact list.

    .. hlist::

       - first list item
       - second list item
       - third list item
       ...

hlist

+-----------------------------------+-----------------------------------+
| -   first list item               | -   next list item xxxx           |
|                                   |                                   |
| -   second list item              | -   next list item yyyy           |
|                                   |                                   |
| -   third list item               | -   next list item zzzz           |
|                                   |                                   |
| -   next list item                |                                   |
+-----------------------------------+-----------------------------------+

### [Definition list](#id36)[¶](#definition-list "Link to this heading")

Note ..

-   the term cannot have more than one line of text

-   there is **no blank line between term and definition block** // this distinguishes definition lists ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists)) from block quotes ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes)).

Each definition list ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists)) item contains a term, optional classifiers and a definition. A term is a simple one-line word or phrase. Optional classifiers may follow the term on the same line, each after an inline ' : ' (**space, colon, space**). A definition is a block indented relative to the term, and may contain multiple paragraphs and other body elements. There may be no blank line between a term line and a definition block (*this distinguishes definition lists from block quotes*). Blank lines are required before the first and after the last definition list item, but are optional in-between.

Definition lists are created as follows:

    term 1 (up to a line of text)
        Definition 1.

    See the typo : this line is not a term!

      And this is not term's definition.  **There is a blank line** in between
      the line above and this paragraph.  That's why this paragraph is taken as
      **block quote** (:duref:`ref <block-quotes>`) and not as term's definition!

    term 2
        Definition 2, paragraph 1.

        Definition 2, paragraph 2.

    term 3 : classifier
        Definition 3.

    term 4 : classifier one : classifier two
        Definition 4.

definition list

term 1 (up to a line of text)

:   Definition 1.

See the typo : this line is not a term!

> <div>
>
> And this is not term's definition. **There is a blank line** in between the line above and this paragraph. That's why this paragraph is taken as **block quote** ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes)) and not as term's definition!
>
> </div>

term 2

:   Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3[classifier]

:   Definition 3.

term 4 : classifier one : classifier two

### [Quoted paragraphs](#id37)[¶](#quoted-paragraphs "Link to this heading")

Quoted paragraphs ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes)) are created by just indenting them more than the surrounding paragraphs. Line blocks ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks)) are a way of preserving line breaks:

    normal paragraph ...
    lorem ipsum.

       Quoted paragraph ...
       lorem ipsum.

    | These lines are
    | broken exactly like in
    | the source file.

Quoted paragraph and line block

normal paragraph ... lorem ipsum.

> <div>
>
> Quoted paragraph ... lorem ipsum.
>
> </div>

These lines are

broken exactly like in

the source file.

[]

### [Field Lists](#id38)[¶](#field-lists "Link to this heading")

bibliographic fields

First lines fields are bibliographic fields, see [Sphinx Field Lists](https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html).

Field lists are used as part of an extension syntax, such as options for directives, or database-like records meant for further processing. Field lists are mappings from field names to field bodies. They marked up like this:

    :fieldname: Field content
    :foo:       first paragraph in field foo

                second paragraph in field foo

    :bar:       Field content

Field List

fieldname[:]

:   Field content

foo[:]

:   first paragraph in field foo

    second paragraph in field foo

bar[:]

:   Field content

They are commonly used in Python documentation:

    def my_function(my_arg, my_other_arg):
        """A function just for me.

        :param my_arg: The first of my arguments.
        :param my_other_arg: The second of my arguments.

        :returns: A message (just for me, of course).
        """

### [Further list blocks](#id39)[¶](#further-list-blocks "Link to this heading")

-   field lists ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists), with caveats noted in [[Field Lists]](#rest-field-list))

-   option lists ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists))

-   quoted literal blocks ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quoted-literal-blocks))

-   doctest blocks ([ref](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks))

## [Admonitions](#id40)[¶](#admonitions "Link to this heading")

### [Sidebar](#id41)[¶](#sidebar "Link to this heading")

Sidebar is an eye catcher, often used for admonitions pointing further stuff or site effects. Here is the source of the sidebar [[on top of this page]](#rest-primer).

    .. sidebar:: KISS_ and readability_

       Instead of defining more and more roles, we at SearXNG encourage our
       contributors to follow principles like KISS_ and readability_.

### [Generic admonition](#id42)[¶](#generic-admonition "Link to this heading")

The generic [admonition](https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions) needs a title:

    .. admonition:: generic admonition title

       lorem ipsum ..

generic admonition title

lorem ipsum ..

### [Specific admonitions](#id43)[¶](#specific-admonitions "Link to this heading")

Specific admonitions: [hint](https://docutils.sourceforge.io/docs/ref/rst/directives.html#hint), [note](https://docutils.sourceforge.io/docs/ref/rst/directives.html#note), [tip](https://docutils.sourceforge.io/docs/ref/rst/directives.html#tip) [attention](https://docutils.sourceforge.io/docs/ref/rst/directives.html#attention), [caution](https://docutils.sourceforge.io/docs/ref/rst/directives.html#caution), [danger](https://docutils.sourceforge.io/docs/ref/rst/directives.html#danger), [error](https://docutils.sourceforge.io/docs/ref/rst/directives.html#error), , [important](https://docutils.sourceforge.io/docs/ref/rst/directives.html#important), and [warning](https://docutils.sourceforge.io/docs/ref/rst/directives.html#warning) .

    .. hint::

       lorem ipsum ..

    .. note::

       lorem ipsum ..

    .. warning::

       lorem ipsum ..

Hint

lorem ipsum ..

Note

lorem ipsum ..

Tip

lorem ipsum ..

Attention

lorem ipsum ..

Caution

lorem ipsum ..

Danger

lorem ipsum ..

Important

lorem ipsum ..

Error

lorem ipsum ..

Warning

lorem ipsum ..

## [Tables](#id44)[¶](#tables "Link to this heading")

Nested tables

Nested tables are ugly! Not all builder support nested tables, don't use them!

ASCII-art tables like [[Simple tables]](#rest-simple-table) and [[Grid tables]](#rest-grid-table) might be comfortable for readers of the text-files, but they have huge disadvantages in the creation and modifying. First, they are hard to edit. Think about adding a row or a column to a ASCII-art table or adding a paragraph in a cell, it is a nightmare on big tables.

List tables

For meaningful patch and diff use [[flat-table]](#rest-flat-table).

Second the diff of modifying ASCII-art tables is not meaningful, e.g. widening a cell generates a diff in which also changes are included, which are only ascribable to the ASCII-art. Anyway, if you prefer ASCII-art for any reason, here are some helpers:

-   [Emacs Table Mode](https://www.emacswiki.org/emacs/TableMode)

-   [Online Tables Generator](https://www.tablesgenerator.com/text_tables)

[]

### [Simple tables](#id45)[¶](#simple-tables "Link to this heading")

[Simple tables](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables) allow *colspan* but not *rowspan*. If your table need some metadata (e.g. a title) you need to add the [`..`]` `[`table::`]` `[`directive`] [(ref)](https://docutils.sourceforge.io/docs/ref/rst/directives.html#table) in front and place the table in its body:

    .. table:: foo gate truth table
       :widths: grid
       :align: left

       ====== ====== ======
           Inputs    Output
       ------------- ------
       A      B      A or B
       ====== ====== ======
       False
       --------------------
       True
       --------------------
       True   False  True
              (foo)
       ------ ------ ------
       False  True
              (foo)
       ====== =============

Simple ASCII table

+----------------------+----------------------+----------------------+
| Inputs               |                      | Output               |
+======================+======================+======================+
| A                    | B                    | A or B               |
+----------------------+----------------------+----------------------+
| False                |                      |                      |
+----------------------+----------------------+----------------------+
| True                 |                      |                      |
+----------------------+----------------------+----------------------+
| True                 | False (foo)          | True                 |
+----------------------+----------------------+----------------------+
| False                | True (foo)           |                      |
+----------------------+----------------------+----------------------+

: [Table 12 ][foo gate truth table][¶](#id11 "Link to this table")

[]

### [Grid tables](#id46)[¶](#grid-tables "Link to this heading")

[Grid tables](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables) allow colspan *colspan* and *rowspan*:

    .. table:: grid table example
       :widths: 1 1 5

       +------------+------------+-----------+
       | Header 1   | Header 2   | Header 3  |
       +============+============+===========+
       | body row 1 | column 2   | column 3  |
       +------------+------------+-----------+
       | body row 2 | Cells may span columns.|
       +------------+------------+-----------+
       | body row 3 | Cells may  | - Cells   |
       +------------+ span rows. | - contain |
       | body row 4 |            | - blocks. |
       +------------+------------+-----------+

ASCII grid table

+------------+-------------------------+--------------------------------------------------+
| Header 1   | Header 2                | Header 3                                         |
+============+=========================+==================================================+
| body row 1 | column 2                | column 3                                         |
+------------+-------------------------+--------------------------------------------------+
| body row 2 | Cells may span columns. |                                                  |
+------------+-------------------------+--------------------------------------------------+
| body row 3 | Cells may span rows.    | -   Cells                                        |
|            |                         |                                                  |
|            |                         | -   contain                                      |
|            |                         |                                                  |
|            |                         | -   blocks.                                      |
+------------+-------------------------+--------------------------------------------------+
| body row 4 |                         |                                                  |
+------------+-------------------------+--------------------------------------------------+

: [Table 13 ][grid table example][¶](#id12 "Link to this table")

[]

### [flat-table](#id47)[¶](#flat-table "Link to this heading")

The [`flat-table`] is a further developed variant of the [[list tables]](https://return42.github.io/linuxdoc/linuxdoc-howto/table-markup.html#list-table-directives "(in LinuxDoc v20240924.dev1)"). It is a double-stage list similar to the [list-table](https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table) with some additional features:

column-span: [`cspan`]

:   with the role [`cspan`] a cell can be extended through additional columns

row-span: [`rspan`]

:   with the role [`rspan`] a cell can be extended through additional rows

auto-span:

:   spans rightmost cell of a table row over the missing cells on the right side of that table-row. With Option [`:fill-cells:`] this behavior can changed from *auto span* to *auto fill*, which automatically inserts (empty) cells instead of spanning the last cell.

options:

:   

    header-rows[:]

    :   \[int\] count of header rows

    stub-columns[:]

    :   \[int\] count of stub columns

    widths[:]

    :   \[\[int\] \[int\] ... \] widths of columns

    fill-cells[:]

    :   instead of auto-span missing cells, insert missing cells

roles:

:   

    cspan[:]

    :   \[int\] additional columns (*morecols*)

    rspan[:]

    :   \[int\] additional rows (*morerows*)

The example below shows how to use this markup. The first level of the staged list is the *table-row*. In the *table-row* there is only one markup allowed, the list of the cells in this *table-row*. Exception are *comments* ( [`..`] ) and *targets* (e.g. a ref to [[row 2 of table's body]](#row-body-2)).

    .. flat-table:: ``flat-table`` example
       :header-rows: 2
       :stub-columns: 1
       :widths: 1 1 1 1 2

       * - :rspan:`1` head / stub
         - :cspan:`3` head 1.1-4

       * - head 2.1
         - head 2.2
         - head 2.3
         - head 2.4

       * .. row body 1 / this is a comment

         - row 1
         - :rspan:`2` cell 1-3.1
         - cell 1.2
         - cell 1.3
         - cell 1.4

       * .. Comments and targets are allowed on *table-row* stage.
         .. _`row body 2`:

         - row 2
         - cell 2.2
         - :rspan:`1` :cspan:`1`
           cell 2.3 with a span over

           * col 3-4 &
           * row 2-3

       * - row 3
         - cell 3.2

       * - row 4
         - cell 4.1
         - cell 4.2
         - cell 4.3
         - cell 4.4

       * - row 5
         - cell 5.1 with automatic span to right end

       * - row 6
         - cell 6.1
         - ..

List table

+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| head / stub | head 1.1-4                                |           |                           |                      |
+=============+===========================================+===========+===========================+======================+
|             | head 2.1                                  | head 2.2  | head 2.3                  | head 2.4             |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 1       | cell 1-3.1                                | cell 1.2  | cell 1.3                  | cell 1.4             |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 2       |                                           | cell 2.2  | cell 2.3 with a span over |                      |
|             |                                           |           |                           |                      |
|             |                                           |           | -   col 3-4 &             |                      |
|             |                                           |           |                           |                      |
|             |                                           |           | -   row 2-3               |                      |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 3       |                                           | cell 3.2  |                           |                      |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 4       | cell 4.1                                  | cell 4.2  | cell 4.3                  | cell 4.4             |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 5       | cell 5.1 with automatic span to right end |           |                           |                      |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+
| row 6       | cell 6.1                                  |           |                           |                      |
+-------------+-------------------------------------------+-----------+---------------------------+----------------------+

: [Table 14 ][[`flat-table`] example][¶](#id13 "Link to this table")

### [CSV table](#id48)[¶](#csv-table "Link to this heading")

CSV table might be the choice if you want to include CSV-data from a outstanding (build) process into your documentation.

    .. csv-table:: CSV table example
       :header: .. , Column 1, Column 2
       :widths: 2 5 5
       :stub-columns: 1
       :file: csv_table.txt

Content of file [`csv_table.txt`]:

    stub col row 1, column, "loremLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua."
    stub col row 1, "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita
    kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.", column
    stub col row 1, column, column

CSV table

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                | Column 1                                                                                                                                    | Column 2                                                                                                                                                         |
+================+=============================================================================================================================================+==================================================================================================================================================================+
| stub col row 1 | column                                                                                                                                      | loremLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stub col row 1 | At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. | column                                                                                                                                                           |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| stub col row 1 | column                                                                                                                                      | column                                                                                                                                                           |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: [Table 15 ][CSV table example][¶](#id14 "Link to this table")

## [Templating](#id49)[¶](#templating "Link to this heading")

Build environment

All *generic-doc* tasks are running in the [[Python environment (make install)]](makefile.html#make-install).

Templating is suitable for documentation which is created generic at the build time. The [sphinx-jinja](https://github.com/tardyp/sphinx-jinja) extension evaluates [jinja](https://jinja.palletsprojects.com/) templates in the [[Python environment (make install)]](makefile.html#make-install) (with SearXNG modules installed). We use this e.g. to build chapter: [[Configured Engines]](../user/configured_engines.html#configured-engines). Below the jinja directive from the [git://docs/admin/engines.rst](https://github.com/searxng/searxng/blob/master/docs/admin/engines.rst) is shown:

    ==================
    Configured Engines
    ==================

    .. sidebar:: Further reading ..

       - :ref:`settings categories_as_tabs`
       - :ref:`engines-dev`
       - :ref:`settings engines`
       - :ref:`general engine configuration`

    .. jinja:: searx

       SearXNG supports } search engines of which
       } are enabled by default.

       Engines can be assigned to multiple :ref:`categories <engine categories>`.
       The UI displays the tabs that are configured in :ref:`categories_as_tabs
       <settings categories_as_tabs>`.  In addition to these UI categories (also
       called *tabs*), engines can be queried by their name or the categories they
       belong to, by using a :ref:`\!bing syntax <search-syntax>`.

    .. contents::
       :depth: 2
       :local:
       :backlinks: entry

    .. jinja:: searx

       

       tab ``!}``
       ---------------------------------------

       

       
       group ``}``}
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       

       .. flat-table::
          :header-rows: 2
          :stub-columns: 1
          :widths: 10 1 10 1 1 1 1 1 1 1

          * - :cspan:`5` Engines configured by default (in :ref:`settings.yml <engine settings>`)
            - :cspan:`3` :ref:`Supported features <engine file>`

          * - Name
            - !bang
            - Module
            - Disabled
            - Timeout
            - Weight
            - Paging
            - Locale
            - Safe search
            - Time range

          

          * - `} <}>`_
              
              (})
              
            - ``!}``
            - 
              :py:mod:`~searx.engines.}`
              
              :origin:`} <searx/engines/}.py>`
              
            - }
            - }
            - }
            
            - }
            - }
            - }
            - }
            
            - :cspan:`3` not applicable (})
            

         
         
         

The context for the template is selected in the line [`..`]` `[`jinja::`]` `[`searx`]. In sphinx's build configuration ([git://docs/conf.py](https://github.com/searxng/searxng/blob/master/docs/conf.py)) the [`searx`] context contains the [`engines`] and [`plugins`].

    import searx.search
    import searx.engines
    import searx.plugins
    searx.search.initialize()
    jinja_contexts = ,
    }

## [Tabbed views](#id50)[¶](#tabbed-views "Link to this heading")

With [sphinx-tabs](https://github.com/djungelorm/sphinx-tabs) extension we have *tabbed views*. To provide installation instructions with one tab per distribution we use the [group-tabs](https://github.com/djungelorm/sphinx-tabs#group-tabs) directive, others are [basic-tabs](https://github.com/djungelorm/sphinx-tabs#basic-tabs) and [code-tabs](https://github.com/djungelorm/sphinx-tabs#code-tabs). Below a *group-tab* example from [[Build docs]](../admin/buildhosts.html#docs-build) is shown:

    .. tabs::

       .. group-tab:: Ubuntu / debian

          .. code-block:: sh

             $ sudo apt install shellcheck

       .. group-tab:: Arch Linux

          .. code-block:: sh

             $ sudo pacman -S shellcheck

       .. group-tab::  Fedora / RHEL

          .. code-block:: sh

             $ sudo dnf install ShellCheck

[]

## [Math equations](#id51)[¶](#math-equations "Link to this heading")

About LaTeX

-   [amsmath user guide](http://vesta.informatik.rwth-aachen.de/ftp/pub/mirror/ctan/macros/latex/required/amsmath/amsldoc.pdf)

-   [Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

-   [[Build docs]](../admin/buildhosts.html#docs-build)

The input language for mathematics is LaTeX markup using the [CTAN: amsmath](https://ctan.org/pkg/amsmath) package.

To embed LaTeX markup in reST documents, use role [[`:math:`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-math "(in Sphinx v9.1.0rc1)") for inline and directive [[`..`]` `[`math::`]](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-math "(in Sphinx v9.1.0rc1)") for block markup.

    In :math:numref:`schroedinger general` the time-dependent Schrödinger equation
    is shown.

    .. math::
       :label: schroedinger general

        \mathrm\hbar\dfrac |\,\psi (t) \rangle =
              \hat |\,\psi (t) \rangle.

LaTeX math equation

In [(1)](#equation-schroedinger-general) the time-dependent Schrödinger equation is shown.

[(1)[¶](#equation-schroedinger-general "Link to this equation")][\\mathrm\\hbar\\dfrac \|\\,\\psi (t) \\rangle = \\hat \|\\,\\psi (t) \\rangle.]

The next example shows the difference of [`\tfrac`] (*textstyle*) and [`\dfrac`] (*displaystyle*) used in a inline markup or another fraction.

    ``\tfrac`` **inline example** :math:`\tfrac+\tfrac}`
    ``\dfrac`` **inline example** :math:`\dfrac+\dfrac}`

Line spacing

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. ... [`\tfrac`] **inline example** [\\tfrac+\\tfrac}] At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. ... [`\tfrac`] **inline example** [\\dfrac+\\dfrac}] At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.