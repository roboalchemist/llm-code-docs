# Source: https://docs.readthedocs.com/platform/latest/guides/cross-referencing-with-sphinx.html

# How to use cross-references with Sphinx[](#how-to-use-cross-references-with-sphinx "Link to this heading")

When writing documentation you often need to link to other pages of your documentation, other sections of the current page, or sections from other pages.

An easy way is just to use the raw URL that Sphinx generates for each page/section. This works, but it has some disadvantages:

-   Links can change, so they are hard to maintain.

-   Links can be verbose and hard to read, so it is unclear what page/section they are linking to.

-   There is no easy way to link to specific sections like paragraphs, figures, or code blocks.

-   URL links only work for the html version of your documentation.

Instead, Sphinx offers a powerful way to linking to the different elements of the document, called *cross-references*. Some advantages of using them:

-   Use a human-readable name of your choice, instead of a URL.

-   Portable between formats: html, PDF, ePub.

-   Sphinx will warn you of invalid references.

-   You can cross reference more than just pages and section headers.

This page describes some best-practices for cross-referencing with Sphinx with two markup options: reStructuredText and MyST (Markdown).

-   If you are not familiar with reStructuredText, check [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html "(in Sphinx v9.1.0rc1)") for a quick introduction.

-   If you want to learn more about the MyST Markdown dialect, check out [Syntax tokens](https://myst-parser.readthedocs.io/en/stable/syntax/reference.html "(in MyST Parser v4.0.1)").

Table of contents

-   [Getting started](#getting-started)

    -   [Explicit targets](#explicit-targets)

    -   [Implicit targets](#implicit-targets)

-   [Cross-referencing using roles](#cross-referencing-using-roles)

    -   [The ref role](#the-ref-role)

    -   [The doc role](#the-doc-role)

    -   [The numref role](#the-numref-role)

-   [Automatically label sections](#automatically-label-sections)

-   [Invalid targets](#invalid-targets)

-   [Finding the reference name](#finding-the-reference-name)

-   [Cross-referencing targets in other documentation sites](#cross-referencing-targets-in-other-documentation-sites)

## Getting started[](#getting-started "Link to this heading")

[]

### Explicit targets[](#explicit-targets "Link to this heading")

Cross referencing in Sphinx uses two components, **references** and **targets**.

-   **references** are pointers in your documentation to other parts of your documentation.

-   **targets** are where the references can point to.

You can manually create a *target* in any location of your documentation, allowing you to *reference* it from other pages. These are called **explicit targets**.

For example, one way of creating an explicit target for a section is:

reStructuredText

MyST (Markdown)

    .. _My target:

    Explicit targets
    ~~~~~~~~~~~~~~~~

    Reference `My target`_.

    (My_target)=
    ## Explicit targets

    Reference [](My_target).

Then the reference will be rendered as [My target](#my-target).

You can also add explicit targets before paragraphs (or any other part of a page).

Another example, add a target to a paragraph:

reStructuredText

MyST (Markdown)

    .. _target to paragraph:

    An easy way is just to use the final link of the page/section.
    This works, but it has :ref:`some disadvantages <target to paragraph>`:

    (target_to_paragraph)=

    An easy way is just to use the final link of the page/section.
    This works, but it has [some disadvantages](target_to_paragraph):

Then the reference will be rendered as: [some disadvantages](targettoparagraph).

You can also create [in-line targets] within an element on your page, allowing you to, for example, reference text *within* a paragraph.

For example, an in-line target inside a paragraph:

reStructuredText

    You can also create _`in-line targets` within an element on your page,
    allowing you to, for example, reference text *within* a paragraph.

Then you can reference it using [`` `in-line ``]` `[`` targets`_ ``], that will be rendered as: [in-line targets](#in-line-targets).