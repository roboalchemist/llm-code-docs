# Source: https://docs.axonius.com/docs/application-extensions.md

# Application Extension

An extension is an instance of a SaaS application granting access permissions to another SaaS or native application, to allow for a seamless user experience across SaaS applications. The **Application Extensions** page displays the aggregation of similar extensions for a high-level view of the extensions that exist in your organization's SaaS environment. To see each individual extension instances, refer to [Application Extension Instances](/docs/application-extension-instances).

Click the **Assets** icon  and from the left-pane, select **Application Extensions**.

![ApplicationExtensionsUpdated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationExtensionsUpdated.png)

## Overview

The Overview section contains three visual displays of the application extensions in your organization. These charts adjust reflect any query applied to the page.

You can click the Hide Charts icon ![HideDynamicCharts](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideDynamicCharts.png) to hide the graphs in the Overview section. Click it again to display the graphs.

* The **Active vs Inactive Users per SaaS Application Extension** chart shows the number [Active and Inactive](/docs/configuring-data-aggregation-settings) users associated with each application extension. Hover over the various bars to see the percentage of active and inactive users for each application extension. Select the corresponding check boxes to display data for only active or inactive users.
* The **Extensions per SaaS Application** graph shows the number of extensions in use in each detected SaaS application. Hover over the various bars to see the percentage of extensions for each application.
* The **Users by Extension** graph shows the number of users for each extension in your organization. Hover over the various bars to see the percentage of users for each application.

![ApplicationExtensionsCharts](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationExtensionsCharts.png)

## Application Extensions Table

The **Application Extensions** table opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Application Extension Fields

There are many fields that you can view and query on the Application Extensions page. These fields include:

### Static Fields

* **Name** - Name of the extension.
* **Used By** - The SaaS application leveraging the extension. If the extension's application does not exist in Axonius's application repository, then this field will be empty. For more information refer to [SaaS Applications](/docs/saas-applications).
* **Extension Type** -The type of extension (SSO, ASK, admin consent, etc.). For more details, see [Extension Types](/docs/extension-types).
* **Association scope** - Shows if an Extension is for a specific user, a group, or all users.

### Counter fields

These fields display a number which you can click to view the list of items that the number represents.

* **User Count** -  The number of users associated with an extension.
* **User Extension Count** - The number of user extensions included in an application extension.
* **Permissions Count** - A group of fields that indicate the number of instances of this extension per permission that they have been granted.
  * Permissions - Is Admin count
  * Permissions - Is identity count
  * Permissions - Mail count
  * Permissions - Drive count
  * Permissions - Calendar count

## Viewing Permissions

To view the permissions that are granted for an extension, hover over the number in the Permissions column.

## Creating Queries on Application Extensions

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as the Extension Type, Activity Status, Is Operational, and more. You can add additional levels to the query, such as querying by risk and security policy. Use these queries to find out which extensions are associated with inactive users, the permission level associated with an extension, and more. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

For example, this query enables you to locate all of the extensions that contain 'Write" level permissions:

![ApplicationExtensionQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApplicationExtensionQuery.png)

After running the query, the overview and table show the queried extensions, filtered by the criteria you defined in your query.

## Adding Tags to Application Extensions

Use tags to assign context to your assets for granular filters and queries. Apply new or existing tags to the selected application extensions. The list of selected tags is applied to all selected extensions.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to application extensions.

## Viewing an Application Extension Profile

You can click on an individual Application Extension asset to see all the data for that particular asset. For more information, see [Asset Profile Page](/docs/asset-profile-page).