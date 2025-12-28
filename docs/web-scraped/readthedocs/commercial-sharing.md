# Source: https://docs.readthedocs.com/platform/latest/commercial/sharing.html

# Sharing private documentation[](#sharing-private-documentation "Link to this heading")

Note

This feature is only available on [Read the Docs for Business](https://app.readthedocs.com/).

Sharing private documentation is useful for giving quick access to your documentation to users outside of your organization. It allows you to share specific projects or versions of a project with users who don't have access to your organization.

Common sharing use cases include:

-   Sharing a project with contractors or partners.

-   Sharing documentation for your product only to specific customers.

-   Embedding documentation in a SaaS application dashboard.

## Creating a shared item[](#creating-a-shared-item "Link to this heading")

-   Go into your project's [Admin] page and click on [Sharing].

-   Click on [New Share]

-   Select access type (secret link, password, or HTTP header token), add an expiration date and a *Description* to help with managing access in the future.

-   Check [`Allow`]` `[`access`]` `[`to`]` `[`all`]` `[`versions?`] if you want to grant access to all versions, or uncheck that option and select the specific versions you want to grant access to.

-   Click [Save].

-   Get the info needed to share your documentation with other users:

    -   **Secret link:** copy the link that is generated

    -   **Password:** copy the link and password

    -   **HTTP header token**: Copy the token, and then pass the [`Authorization`] header in your HTTP request.

-   Give that information to the person who you want to give access.

Note

You can always revoke access by removing the sharing item on this page.