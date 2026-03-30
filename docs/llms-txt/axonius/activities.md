# Source: https://docs.axonius.com/docs/activities.md

# Activities

The Activities page provides insight into users in SaaS application usage by both individual users as well as entities. This allows you to detect any unusual or suspicious behaviors; reducing risk and maintaining strong security for your organization.

Examples of unusual and potentially threatening behavior that you can detect and review with the Activities module might include:

**Creation of suspicious SSO admin accounts** - If a new admin user is created in an SSO application and that admin logs into an app shortly after it's created, Axonius flags that account as 'suspicious.'

**Addition of Admin permissions** - Axonius can create alerts when Admin permissions are added to user accounts in a SaaS application.

Click the **Assets** icon and from the left-pane, select **Activities**.

<Image alt="ActivitesnewUI.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActivitesnewUI.png" />

The **Activities** page opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Activities Fields

There are many fields that you can view and query on the Activities page. These fields include:

* **Location fields** - Fields that show data related to the location where the activity occurred.

* **Actor State fields** - Fields that describe the actor who performed the recorded activity.

* **Adapter Connections** - The SaaS applications that the activity occurred on.

* **Custom Properties** - Shows event attributes such as "Failed" "Important" and others.

* **Action Type** - Indicate if events' actions were performed by a user or a system (SaaS application).

## Creating Queries on Activities

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as timestamp, location, affected user, type, and more. Use these queries to find out which events exist with asset context in your environment or how many events meet certain defined criteria. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

For example, you can use a query to locate all admin assignments in the past seven days.

After running the query, the table shows the queried applications, filtered by the criteria you defined in your query.

## Adding Custom Data to an Activity

You can add custom fields to one or more activity at the same time. You can use this to add your own notes or other data specific to your organization.

Select one or more applications and from the **Actions** menu choose **Add Custom Fields**.

Refer to [Working with Custom Data](/docs/working-with-custom-data) to learn about adding custom fields.

## Add Tags to an Activity

Use tags to assign context to your activities for granular filters and queries. Apply new or existing tags to the selected applications. The list of selected tags is applied to all selected applications.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to activities.

## View an Event Profile

You can click on an individual asset in Activities to see all its relevant data. For more information, see [Asset Profile Page](/docs/asset-profile-page).