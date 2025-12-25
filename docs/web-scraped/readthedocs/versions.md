# Source: https://docs.readthedocs.com/platform/latest/versions.html

# Versions[](#versions "Link to this heading")

Read the Docs supports publishing multiple versions of your documentation. This allows your users to read the exact documentation for the specific version of the project they are using.

Versioning is useful for many reasons, but a few common use cases are:

-   Shipping API client libraries that release versions across time.

-   Having a "stable" and "latest" branch so that users can see the current release and the upcoming changes.

-   Having a private development branch and a public stable branch so that in development releases aren't accidentally seen by users until they are released.

## Versions are Git tags and branches[](#versions-are-git-tags-and-branches "Link to this heading")

When you add a project to Read the Docs, all Git tags and branches are created as **Inactive** and **Not Hidden** versions by default. During initial setup, Read the Docs also creates a [`latest`] version that points to the default branch defined in your Git repository (usually [`main`]). This version should always exist and is the default version for your project.

If your project has any tags or branches with a name following [semantic versioning](https://semver.org/) (with or without a [`v`] prefix), we also create a [`stable`] version tracking your most recent release. If you want a custom [`stable`] version, create either a tag or branch in your project with that name.

Note

If you have at least one tag, tags will take preference over branches when selecting the stable version.

When you have [[Git integration (GitHub, GitLab, Bitbucket)]](reference/git-integration.html) configured for your repository, we will automatically build each version when you push a commit.