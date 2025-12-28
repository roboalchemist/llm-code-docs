# Source: https://docs.readthedocs.com/platform/latest/reference/robots.html

# [`robots.txt`] support[](#robots-txt-support "Link to this heading")

The [robots.txt](https://developers.google.com/search/reference/robots_txt) files allow you to customize how your documentation is indexed in search engines. It's useful for:

-   Hiding various pages from search engines

-   Disabling certain web crawlers from accessing your documentation

-   Disallowing any indexing of your documentation

Read the Docs automatically generates one for you with a configuration that works for most projects. By default, the automatically created [`robots.txt`]:

-   Hides versions which are set to [[Hidden]](../versions.html#version-states) from being indexed.

-   Allows indexing of all other versions.

Warning

[`robots.txt`] files are respected by most search engines, but they aren't a guarantee that your pages will not be indexed. Search engines may choose to ignore your [`robots.txt`] file, and index your docs anyway.

If you require *private* documentation, please see [[Sharing private documentation]](../commercial/sharing.html).

## How it works[](#how-it-works "Link to this heading")

You can customize this file to add more rules to it. The [`robots.txt`] file will be served from the **default version** of your project. This is because the [`robots.txt`] file is served at the top-level of your domain, so we must choose a version to find the file in. The **default version** is the best place to look for it.