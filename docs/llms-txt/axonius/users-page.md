# Source: https://docs.axonius.com/docs/users-page.md

# Users Page

The Users page displays all the users  that were fetched for the query run. The query name is displayed above the search bar. If no query was chosen, the page displays all users.

To open the **Users** page, click the **Assets** icon and from the left pane, under **Identity**, select  **Users**.

<Image alt="Users Page New.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Users%20Page%20New.png" />

User entities refer to identities used in the organization for authentication and ownership of devices, therefore user information is collected and correlated from different adapters that hold identity information like Microsoft Active Directory, Google Mobile Management (G-Suite), Okta and others.

For each User the query results table displays multiple columns, with the leftmost being the Adapters Connection column.

The Adapters Connection column displays the logos of the adapters that the user was fetched from and is considered by Axonius as  **the correlation of data from different adapters to the same user**.

You can set the columns displayed on the page and freeze specific columns so that they are not scrolled. The Adapter Connections column is frozen by default. Refer to [Setting Page Columns Display](/docs/setting-page-columns-display).

## Overview

The Overview section contains three visual displays of the users in your organization:

* The Number of Admins per SaaS Application graph shows the number of users with admin-level access in each detected SaaS application.
* The Users by Department graph shows the number of users per department in your organization.
* The SaaS Application by Number of Users graph shows the number of users using each detected SaaS application.

You can click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideDynamicCharts.png) to hide the graphs in the Overview section. Click it again to display the graphs.

## User Fields

There are many fields that you can view and query on the Users page. This includes the following fields. 'General' pertains to fields that are relevant for accounts with Cybersecurity Asset Management and/or SaaS Management capabilities.

### General

* **User Department** - Displays the department that the user belongs to.

* **User Name** - Displays the name of the user.

* **User Status** - Indicates the status(es) of the users for the relevant applications (Active, Suspended, etc.).

* **Last logon date** - Displays the date and time the user last logged in to an application.

* **Is User External** - Indicates if the user account is external to the organization.

* **Is Admin** - Indicates if the user has been granted admin-level permission for the application.
  * For the the following adapters, this field is displayed as **Is Super Admin** and only displays a value of "Yes" when the user has the highest possible admin permissions for that application:
    * Tenable IO
    * Salesforce
    * Crowdstrike falcon Identity Protection
    * MongoDB Atlas
    * Atlassian (formerly Atlassian Jira software)
      For these adapters, you can use the 'Has Administrative Level Permissions' field to show if a user has some admin permissions for those applications.

* **Associated Employees** - Displays all the users managed by the user (when the user is a manager). You can click the user's internal ID in the Associated Employees table to view that user's profile.

* **User Manager Remote ID** - Displays the ID of the user's manager and links to the manager's asset page.

### Cybersecurity Asset Management

* **Account Disabled** - Indicates if the user's accounts are disabled.
* **Domain** - Displays the user's domain name.
* **Last seen in domain** - Displays the date and time the user was last seen in a given domain.
* **Groups** - Displays the groups that the user belongs to.
* **Is local** - Indicates if the user's accounts are defined locally on a device.
* **Is locked** - Indicates if the user's accounts are currently locked.
* **Password is not required** - Indicates if the user requires a password to log in to their applications.
* **Password never expires** - Indicates if the user's passwords are set to never expire.
* **Last password change** - Displays the date and time the user's password was last changed.

### SaaS Management

* **Assigned Applications** - SaaS application data fetched from the adapter: extensions, SaaS applications, and other discovered data (for example, DNS records from Zscaler, extensions from Okta, connected adapters, etc.).
* **Is Managed by SSO** - Indicates if each of the user's applications are managed by the organization’s SSO solution.
* **Associated License** - Displays all the licenses associated with the user, along with the cost of licenses and unit of payment. You can click this field in the user profile to view a Licenses asset table, filtered for this user.

## Performing Actions on Users

Select one or more users and use the options in the Actions menu to perform various actions. Refer to [Asset Actions](/docs/devices-actions)

The structure of the **Users** page and navigating it are similar to all the **Assets** pages.
For more details on the different elements and the navigation in the **Users** page, see [Assets page.](/docs/assets-page)

## Creating Queries

Use the Queries to create granular queries to better understand your users. You can define a wide variety of filters, from which you can easily drill down to the assets that match the required search criteria.
You can create queries on users using one of the following modes:

* **Query Wizard** (the default) - Create a query using the **Query Wizard**,  or in the query bar, selecting a saved query or writing a query.

* **Basic** mode - Create a query by selecting filters.

Use either of these modes to create a unique set of queries.

Learn more about [how to create Queries using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard) and [how to create Queries in Basic mode](/docs/basic-query-mode).

## SaaS Users View

The SaaS Users view is a predefined saved view that expands rows by the users' SaaS applications (“Assigned Applications” field) instead of by adapter connections. Each SaaS application is displayed in a separate row.

When you export data from the SaaS Users view,  the Export Data dialog includes the option to split the users by their applications instead of asset entities. <br />
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SMUserView_ExportCSV.png)

**To select the SaaS Users view:**

1. Click **Edit Table**.
2. Select **Saved Views `>` SaaS Users**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SM%20Users%20View.png)

Each row displays separate information for the user's individual SaaS Applications.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SMUsersViewEXpandedN.png)

**To revert to the default view:**

1. Click **Edit Table**.
2. Select **Saved Views `>` System View (Default)**.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).