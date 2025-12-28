# Source: https://docs.readthedocs.com/platform/latest/tutorial/index.html

# Read the Docs tutorial[](#read-the-docs-tutorial "Link to this heading")

In this tutorial you will learn how to host a public documentation project on Read the Docs Community.

Note

Find out the [differences between Read the Docs Community and Read the Docs for Business](https://about.readthedocs.com/pricing/#/community).

In the tutorial we will:

1.  Import a Sphinx project from a GitHub repository (no prior experience with Sphinx is required).

2.  Tailor the project's configuration.

3.  Explore other useful Read the Docs features.

If you don't have a GitHub account, you'll need to [register for a free account](https://github.com/signup) before you start.

## Preparing your repository on GitHub[](#preparing-your-repository-on-github "Link to this heading")

1.  [Sign in to GitHub](https://github.com/login) and navigate to the [tutorial GitHub template](https://github.com/readthedocs/tutorial-template/).

2.  Click the green [Use this template] button, then click [Create a new Repository]. On the new page:

    Owner

    :   Leave the default, or change it to something suitable for a tutorial project.

    Repository name

    :   Something memorable and appropriate, for example [`rtd-tutorial`].

    Visibility

    :   Make sure the project is "Public", rather than "Private".

3.  Click the green [Create repository] button to create a public repository that you will use in this Read the Docs tutorial, containing following files:

    [`.readthedocs.yaml`]

    :   Read the Docs configuration file. Required.

    [`README.rst`]

    :   Description of the repository.

    [`pyproject.toml`]

    :   Python project metadata that makes it installable. Useful for automatic documentation generation from sources.

    [`lumache.py`]

    :   Source code of the fictional Python library.

    [`docs/`]

    :   Directory holding all the fictional Python library documentation in reStructuredText, the Sphinx configuration [`docs/source/conf.py`] and the root document [`docs/source/index.rst`].

<figure id="id3" class="align-center">
<a href="../_images/github-template.png" class="reference internal image-reference"><img src="../_images/github-template.png" style="width: 80%;" alt="GitHub template for the tutorial" /></a>
<figcaption><p><span class="caption-text">GitHub template for the tutorial</span><a href="#id3" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>