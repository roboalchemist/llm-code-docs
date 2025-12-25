# Source: https://docs.readthedocs.com/platform/latest/user-defined-redirects.html

# Redirects[](#redirects "Link to this heading")

Over time, a documentation project may want to rename and move contents around. Redirects allow changes in a documentation project to happen without bad user experiences.

If you do not manage URL structures, users will eventually encounter 404 File Not Found errors. While this may be acceptable in some cases, the bad user experience of a 404 page is usually best to avoid.

[Built-in redirects](#built-in-redirects) ⬇️

:   Allows for simple and long-term sharing of external references to your documentation.

[User-defined redirects](#user-defined-redirects) ⬇️

:   Makes it easier to move contents around

See also

[[How to use custom URL redirects in documentation projects]](guides/redirects.html)

:   This guide shows you how to add redirects with practical examples.

[[Best practices for linking to your documentation]](guides/best-practice/links.html)

:   Information and tips about creating and handling external references.

[[How to deprecate content]](guides/deprecating-content.html)

:   A guide to deprecating features and other topics in a documentation.

## Built-in redirects[](#built-in-redirects "Link to this heading")

This section explains the redirects that are automatically active for all projects and how they are useful. Built-in redirects are especially useful for creating and sharing incoming links, which is discussed in depth in [[Best practices for linking to your documentation]](guides/best-practice/links.html).

[]

### Page redirects at [`/page/`][](#page-redirects-at-page "Link to this heading")

You can link to a specific page and have it redirect to your default version, allowing you to create links on external sources that are always up to date. This is done with the [`/page/`] URL prefix.

For instance, you can reach the page you are reading now by going to [https://docs.readthedocs.io/page/guides/best-practice/links.html](https://docs.readthedocs.io/page/guides/best-practice/links.html).

Another way to handle this is the [`latest`] version. You can set your [`latest`] version to a specific version and just always link to [`latest`]. You can reach this page by going to [https://docs.readthedocs.io/en/latest/guides/best-practice/links.html](https://docs.readthedocs.io/en/latest/guides/best-practice/links.html).