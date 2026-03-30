# Source: https://docs.axonius.com/docs/admin-managed-extensions.md

# Admin Managed Extensions

Admin Managed Extensions allow administrators to configure and manage how users access applications. These extensions provide centralized control over authentication and authorization.\
They include the following kinds of extensions:

* **Admin Consent** - Allows administrators to grant application access to organizational data by approving OAuth scopes that require admin approval, regardless of the SSO configuration.

* **Single Sign-On (SSO)** - Allows administrators to configure centralized login with SAML, OAuth2 or other authentication methods.

* **Bookmark** - Allows administrators to add a shortcut for user access without authentication configuration.

* **Identity Provider (IDP) Connection** - Allows administrators to connect an IDP with an application through the application configuration page.

When an SSO, bookmark, or IDP connection are created, a corresponding [Account asset](/docs/accounts) is created.

The Admin Managed Extensions page displays each extension that can be reviewed and managed separately.

Click the **Assets** icon  and from the left pane, select **Admin Managed Extensions**.

## Admin Managed Extensions Table

The **Admin Managed Extensions** table opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Admin Managed Extension Fields

There are many fields that you can view and query on the User Extensions page. This includes the following fields:

* **Name** - Name of the extension.
* **Used By** - The SaaS application using the extension. If the extension's application does not exist in Axonius's application repository, then this field will be empty.
* **Extension Type** -The type of extension (SSO, ASK, admin consent, etc.). For more details, see [Extension Types](/docs/extension-types).
* **Source Application** - The application that provides the extension information.
* **User Count** -The number of relevant users. Clicking the number opens a list of users filtered for Admin Managed Extension instances.
* **User Extension Count** - The number of relevant extensions in Admin Managed Extension instances. Clicking the number opens a list of extensions filtered for Admin Managed Extension instances.
* **Last Accessed** - The date of the last usage of the extension

## Viewing Permissions

To view the permissions that are granted for an extension, hover over the number in the Permissions column.

## Creating Queries on Admin Managed Extensions

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as the Extension Type, Source application, Used by, and more. You can add additional levels to the query, such as querying by risk and security policy. Use these queries to find out which extensions are associated with inactive users, the permission level associated with an extension, and more. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

## Adding Tags to Admin Managed Extension

Use tags to assign context to your assets for granular filters and queries. Apply new or existing tags to the selected Admin Managed Extension. The list of selected tags is applied to all selected extensions.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to user extensions.

## Viewing an Admin Managed Extension Profile

You can click on an individual Admin Managed Extension asset to see all the data for that particular asset. For more information, see [Asset Profile Page](/docs/asset-profile-page).