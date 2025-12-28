# Source: https://docs.readthedocs.com/platform/latest/subprojects.html

# Subprojects[](#subprojects "Link to this heading")

In this article, you can learn more about how several documentation projects can be combined and presented to the reader on the same website.

Read the Docs can be configured to make other *projects* available on the website of the *main project* as **subprojects**. This allows for documentation projects to share a search index and a namespace or custom domain, but still be maintained independently.

This is useful for:

-   Organizations that need all their projects visible in one documentation portal or landing page

-   Projects that document and release several packages or extensions

-   Organizations or projects that want to have a common search function for several sets of documentation

For a main project [`example-project`], a subproject [`example-project-plugin`] can be made available as follows:

-   Main project: [`https://example-project.readthedocs.io/en/latest/`]

-   Subproject: [`https://example-project.readthedocs.io/projects/plugin/en/latest/`]

See also

[[Managing subprojects]](guides/subprojects.html)

:   Learn how to create and manage subprojects

[[How to link to other documentation projects with Intersphinx]](guides/intersphinx.html)

:   Learn how to use references between different Sphinx projects, for instance between subprojects

## Sharing a custom domain[](#sharing-a-custom-domain "Link to this heading")

Projects and subprojects can be used to share a custom domain. To configure this, one project should be established as the main project and configured with a custom domain. Other projects are then added as subprojects to the main project.

If the example project [`example-project`] was set up with a custom domain, [`docs.example.com`], the URLs for projects [`example-project`] and [`example-project-plugin`] with alias [`plugin`] would respectively be at:

-   [`example-project`]: [`https://docs.example.com/en/latest/`]

-   [`example-project-plugin`]: [`https://docs.example.com/projects/plugin/en/latest/`]