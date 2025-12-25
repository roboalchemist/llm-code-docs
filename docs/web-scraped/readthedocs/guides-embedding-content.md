# Source: https://docs.readthedocs.com/platform/latest/guides/embedding-content.html

# How to embed content from your documentation[](#how-to-embed-content-from-your-documentation "Link to this heading")

Read the Docs allows you to embed content from any of the projects we host and specific allowed external domains (currently, [`docs.python.org`], [`docs.scipy.org`], [`docs.sympy.org`], [`numpy.org`]) This allows reuse of content across sites, making sure the content is always up to date.

There are a number of use cases for embedding content, so we've built our integration in a way that enables users to build on top of it. This guide will show you some of our favorite integrations:

-   [Contextualized tooltips on documentation pages](#contextualized-tooltips-on-documentation-pages)

-   [Inline help on application website](#inline-help-on-application-website)

-   [Calling the Embed API directly](#calling-the-embed-api-directly)

## [Contextualized tooltips on documentation pages](#id1)[](#contextualized-tooltips-on-documentation-pages "Link to this heading")

Tooltips on your own documentation are really useful to add more context to the current page the user is reading. You can embed any content that is available via an HTML id.

We built an addon called [[Link previews]](../link-previews.html) on top of our Embed API that you can enable from the addons settings of your project using the [[dashboard]](../glossary.html#term-dashboard).