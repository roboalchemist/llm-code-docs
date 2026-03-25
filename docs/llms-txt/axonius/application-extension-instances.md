# Source: https://docs.axonius.com/docs/application-extension-instances.md

# Application Extension Instances

An extension is an instance of a SaaS application granting access permissions to another SaaS or native application to allow for a seamless user experience across SaaS applications. The Application Extension Instances page displays each individual extension instance that can be reviewed and managed as its own separate unit.

Click the **Assets** icon and from the left-pane, select **Application Extension Instances**.

![AppExtensionInstancesNew.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppExtensionInstancesNew.png)

## Overview

The Overview section contains three visual displays of the Application Extension Instances in your organization. These charts adjust reflect any query applied to the page.

You can click the Hide Charts icon ![HideDynamicCharts](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideDynamicCharts.png) to hide the graphs in the Overview section. Click it again to display the graphs.

* The **Active vs Inactive Users in Application Extension** chart shows the number of [Active and Inactive](/docs/configuring-data-aggregation-settings) extensions, segmented by application. Use the check boxes to display the Active and/or Inactive users. Hover over the chart to see the percentage of users represented by each segment. Select the corresponding check boxes to display data for only active or inactive users.
* The **Extension Types by Number of Users** graph shows the number of users with each extension type. Hover over the various bars to see the percentage of users for each extension type.
* The **Extensions by Number of Users** graph shows the number of users with extension types for each application. Hover over the various bars to see the percentage of extensions for each user.

![AppExtensionsCharts.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppExtensionsCharts.png)

## Application Extension Instances Table

The **Application Extension Instances** table opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Application Extension Instances Fields

There are many fields that you can view and query on the  Application Extension Instances page. This includes the following fields:

* **Name** - Name of the extension instance.
* **Used By** - The SaaS application leveraging the extension instance. If the extension's application does not exist in Axonius's application repository, then this field will be empty.
* **Extension Type** -The type of extension (SSO, ASK, admin consent, etc.). For more details, see [Extension Types](/docs/extension-types).
* **Permissions** - Details of permissions granted for the application.
* **Activity Status** - Indicates the extension instance activity within the application/account.
* **Associated User** - Details for the user associated with the extension instance.
* **Is Operational**- Indicates if the extension instance is operational.
* **Last Accessed** - The date of the last usage of the extension instance.
* **Never Accessed** - Indicates if the extension instance has never been used.
* **Permissions: Is Admin** - Indicates if admin level permission has been granted for this extension instance.
* **Permissions: Is Identity** - Indicates if identity level permission has been granted for this extension instance.
* **User Activity Status** - User account activity for the associated application/account.
* **Association scope** - Shows if an extension instance is for a specific user, a group, or all users.

## Viewing Permissions

To view the permissions that are granted for an extension instance, hover over the number in the Permissions column.

## Creating Queries on Application Extension Instances

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as the Extension Type, Activity Status, Is Operational, and more. You can add additional levels to the query, such as querying by risk and security policy. Use these queries to find out which extensions are associated with inactive users, the permission level associated with an extension, and more. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

For example, this query enables you  to locate all of the extensions that contain 'Write" level permissions:

![AppExtensQueryN.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppExtensQueryN.png)

After running the query, the overview and table show the queried extensions, filtered by the criteria you defined in your query.

## Adding Tags to Application Extension Instances

Use tags to assign context to your assets for granular filters and queries. Apply new or existing tags to the selected user extensions. The list of selected tags is applied to all selected extensions.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to user extensions.

## Viewing an Application Extension InstanceProfile

You can click on an individual Extension instance asset to see all the data for that particular asset. For more information, see [Asset Profile Page](/docs/asset-profile-page).