# Source: https://docs.readthedocs.com/platform/latest/faq.html

# Frequently asked questions[](#frequently-asked-questions "Link to this heading")

-   [Building and publishing your project](#building-and-publishing-your-project)

    -   [Why does my project have status "failing"?](#why-does-my-project-have-status-failing)

    -   [Why do I get import errors from libraries depending on C modules?](#why-do-i-get-import-errors-from-libraries-depending-on-c-modules)

    -   [Where do I need to put my docs for Read the Docs to find it?](#where-do-i-need-to-put-my-docs-for-read-the-docs-to-find-it)

    -   [How can I avoid search results having a deprecated version of my docs?](#how-can-i-avoid-search-results-having-a-deprecated-version-of-my-docs)

    -   [How do I change the version slug of my project?](#how-do-i-change-the-version-slug-of-my-project)

    -   [What commit of Read the Docs is in production?](#what-commit-of-read-the-docs-is-in-production)

-   [Additional features and configuration](#additional-features-and-configuration)

    -   [How do I add additional software dependencies for my documentation?](#how-do-i-add-additional-software-dependencies-for-my-documentation)

    -   [How do I change behavior when building with Read the Docs?](#how-do-i-change-behavior-when-building-with-read-the-docs)

    -   [I want comments in my docs](#i-want-comments-in-my-docs)

    -   [Can I remove advertising from my documentation?](#can-i-remove-advertising-from-my-documentation)

    -   [How do I change my project slug (the URL your docs are served at)?](#how-do-i-change-my-project-slug-the-url-your-docs-are-served-at)

-   [Big projects](#big-projects)

    -   [How do I host multiple projects on one custom domain?](#how-do-i-host-multiple-projects-on-one-custom-domain)

    -   [How do I support multiple languages of documentation?](#how-do-i-support-multiple-languages-of-documentation)

-   [Sphinx](#sphinx)

    -   [I want to use the Read the Docs theme](#i-want-to-use-the-read-the-docs-theme)

    -   [Image scaling doesn't work in my documentation](#image-scaling-doesn-t-work-in-my-documentation)

-   [Python](#python)

    -   [Can I document a Python package that is not at the root of my repository?](#can-i-document-a-python-package-that-is-not-at-the-root-of-my-repository)

    -   [Does Read the Docs work well with "legible" docstrings?](#does-read-the-docs-work-well-with-legible-docstrings)

    -   [I need to install a package in a environment with pinned versions](#i-need-to-install-a-package-in-a-environment-with-pinned-versions)

-   [Other documentation frameworks](#other-documentation-frameworks)

    -   [How can I deploy Jupyter Book projects on Read the Docs?](#how-can-i-deploy-jupyter-book-projects-on-read-the-docs)

## [Building and publishing your project](#id2)[](#building-and-publishing-your-project "Link to this heading")

[]

### [Why does my project have status "failing"?](#id3)[](#why-does-my-project-have-status-failing "Link to this heading")

Projects have the status "failing" because something in the build process has failed. This can be because the project is not correctly configured, because the contents of the Git repository cannot be built, or in the most rare cases because a system that Read the Docs connects to is not working.

First, you should check out the [Builds] tab of your project. By clicking on the failing step, you will be able to see details that can lead to resolutions to your build error.

If the solution is not self-evident, you can use an important word or message from the error to search for a solution.

See also

[[Troubleshooting build errors]](guides/build-troubleshooting.html)

:   Common errors and solutions for build failures.

Other FAQ entries

:   -   [[How do I add additional software dependencies for my documentation?]](#how-do-i-add-additional-software-dependencies-for-my-documentation)

    -   [[Why do I get import errors from libraries depending on C modules?]](#why-do-i-get-import-errors-from-libraries-depending-on-c-modules)