# Source: https://docs.readthedocs.com/platform/latest/guides/best-practice/links.html

[]

# Best practices for linking to your documentation[](#best-practices-for-linking-to-your-documentation "Link to this heading")

Once you start to publish documentation, external sources will inevitably link to specific pages in your documentation.

Sources of incoming links vary greatly depending on the type of documentation project that is published. They can include everything from old emails to GitHub issues, wiki articles, software comments, PDF publications, or StackOverflow answers. Most of these incoming sources are not in your control.

Read the Docs makes it easier to create and manage incoming links by redirecting certain URLs automatically and giving you access to define your own redirects.

In this article, we explain how our built-in redirects work and what we consider "best practice" for managing incoming links.

See also

[[Versions]](../../versions.html)

:   Read more about how to handle versioned documentation and URL structures.

[[Redirects]](../../user-defined-redirects.html)

:   Overview of all the redirect features available on Read the Docs. Many of the redirect features are useful either for building external links or handling requests to old URLs.

[[How to use custom URL redirects in documentation projects]](../redirects.html)

:   How to add a user-defined redirect, step-by-step. Useful if your content changes location!

## Best practice: "permalink" your pages[](#best-practice-permalink-your-pages "Link to this heading")

You might be familiar with the concept of [permalinks](https://en.wikipedia.org/wiki/Permalink) from blogging. The idea is that a blog post receives a unique link as soon as it's published and that the link does not change afterward. Incoming sources can reference the blog post even though the blog changes structure or the post title changes.

When creating an external link to a specific documentation page, chances are that the page is moved as the documentation changes over time.

How should a permalink look for a documentation project? Firstly, you should know that a *permalink* does not really exist in documentation but it is the result of careful actions to avoid breaking incoming links.

As a documentation owner, you most likely want users clicking on incoming links to see the latest version of the page.

### Good practice ✅[](#good-practice "Link to this heading")

-   Use [[page redirects]](../../user-defined-redirects.html#id2) if you are linking to the page in the [[default version]](../../glossary.html#term-default-version) of the default language. This allows links to continue working even if those defaults change.

-   If you move a page that likely has incoming references, [[create a custom redirect rule]](../redirects.html).

-   Links to other Sphinx projects should use [[intersphinx]](../intersphinx.html).

-   Use minimal filenames that don't require renaming often.

-   When possible, keep original file names rather than going for low-impact URL renaming. Renaming an article's title is great for the reader and great for SEO, but this does not have to involve the URL.

-   Establish your understanding of the *latest* and [[default version]](../../glossary.html#term-default-version) of your documentation at the beginning. Changing their meaning is disruptive to incoming links.

-   Keep development versions [[hidden]](../../versions.html#version-states) so people do not find them on search engines by mistake. This is the best way to ensure that nobody links to URLs that are intended for development purposes.

-   Use a [[version warning notifications]](../../versions.html#version-warning-notifications) to ensure the reader is aware in case they are reading an old (archived) version.

Tip

Using Sphinx?

:   If you are using [`:ref:`] for [[cross-referencing]](../cross-referencing-with-sphinx.html), you may add as many reference labels to a headline as you need, keeping old reference labels. This will make refactoring documentation easier and avoid that external projects referencing your documentation through [[intersphinx]](../intersphinx.html) break.