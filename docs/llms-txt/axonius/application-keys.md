# Source: https://docs.axonius.com/docs/application-keys.md

# Application Keys

Application Key Extensions are a type of User Extension that allows users and administrators to manage authentication credentials for specific applications. These extensions provide methods for accessing applications without full user logins, taking into account different access needs. They include the following kind of extensions:

* **ASP (Application-Specific Password)** - Enables users to set up stored credentials for legacy applications so they can access the applications without needing to remember passwords for each.
* **Key (API Key)** - Allows administrators to generate an API key for programmatic or machine-level access, enabling automated integrations and access for applications.

The Application Keys page displays each individual Application Key extension that can be reviewed and managed as its own separate unit.

Click the **Assets** icon and from the left pane, select **Application Keys**.

## Application Keys Table

The **Application Keys** table opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Application Key Fields

There are many fields that you can view and query on the Application Keys page. This includes the following fields:

* **Name** - Name of the extension.
* **Used By** - The SaaS application leveraging the extension. If the extension's application does not exist in Axonius's application repository, then this field will be empty.
* **Extension Type** -The type of extension (SSO, ASK, admin consent, etc.). For more details, see [Extension Types](/docs/extension-types).

## Viewing Permissions

To view the permissions that are granted for an Application Key, hover over the number in the Permissions column.

## Creating Queries on Application Keys

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as the Extension Type, Name, Used by, and more. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

## Adding Tags to Application Keys

Use tags to assign context to your assets for granular filters and queries. Apply new or existing tags to the selected Application Keys. The list of selected tags is applied to all selected application keys.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to application keys.

## Viewing an Application Key Profile

You can click on an individual Application Key asset to see all the data for that particular asset. For more information, see [Asset Profile Page](/docs/asset-profile-page).