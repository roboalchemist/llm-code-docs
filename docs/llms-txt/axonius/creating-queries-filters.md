# Source: https://docs.axonius.com/docs/creating-queries-filters.md

# System Queries (Creating Queries Using Filters)

You can create and save queries in two modes.

* Create Queries on assets using the Query Wizard.
* Create System queries on **[Activity Logs](/docs/activity-logs-page)**, **[Adapters Fetch History](/docs/adapters-fetch-history)**,[**Asset Investigation**](/docs/advanced-asset-investigation), and [**Findings**](/docs/findings-center-page#searching-and-filtering) using filters.

This page explains how to create System Queries for **Activity Logs**,  **Adapters Fetch History**, **Asset Investigation**, and **Findings** using  filters.
Use these queries to easily view data about the running of the system. Once you create a System Query using filters you can save it and use it like any other saved query in the system. Learn more about viewing and saving queries on [Queries Page](/docs/managing-queries) and [Saved Queries](/docs/saved-queries-devices).
Filters and Search structure are very similar on the Adapter Fetch History, Activity Logs, Asset Investigation, and Findings pages. The filters and searches that you run can be saved like any other query and be reused and retrieved from the **Query** page.

## Creating System Queries Using Filters

1. Set filters on the page you are interested in, for instance on the Activity Log page, or set a search.

![NewActivityLogUp.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewActivityLogUp.png)

2. In **Query name**, enter a unique name for the query.
3. In **Query description**, enter a description (optional).
4. In **Tags**, choose a tag from the drop down list of tags available in the system or start typing to add a new tag. You can add as many tags as you need. When you add a new tag, click **Add  New** to add the tag to the system. Use **Clear All** to remove a tag you selected. Tags help organize your queries. You can add a tag to a query when you create the query, as well as  from the **Saved Queries** page. The list of tags used in queries is the same across the whole system. Tags are optional.
5. To create an Asset Scope query, toggle **Asset scope query** on. The query will be saved in the **Asset Scope Queries** folder and it can be used to create Data Scopes. If this option is on, the **Access** section is not displayed.
6. In [**Who has access**](/docs/who-has-access), configure the access privileges for the query.
7. In **Folder name**, select the folder where you want to save the query. The folders available depend on whether the query is private or public.
   * By default, public queries are saved in the folder of the current Data Scope.
   * Queries accessible to all Data Scopes are saved in the **Shared Queries** folder.
   * Private queries are saved in the **My Private Queries** folder.
8. Click **Save**.

The Query now appears on the Queries page.

### Loading a Saved Query

You can find and load the queries that you saved from the [Queries](/docs/queries) page.

## Copying a Query

You can copy a query.
Once you configure filters or a Search and saved them as a query, an arrow appears next to **Save As**.
To copy the query, click the arrow and choose **Copy Query Link**.

![CopyQueryLinkN.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CopyQueryLinkN.png)

* You can only copy query links for a saved query (not an edited query.

## Updating  Query Details

Once you configure filters or a Search and saved them as a query, an arrow appears next to **Save As**.
Click the arrow and choose **Update Details** to change any other query details, such as the name, description, tags and folder where it is saved.

## Using Activity Log, Adapter Fetch History, Asset Investigation, and Findings Queries in Enforcement Actions

System queries created using filters can be used as queries in the following basic Enforcement Set actions:

* [Send Email](/docs/send-email)
* [Send to Syslog Server](/docs/send-to-syslog-server)
* [Send to HTTPS Log Server](/docs/send-to-https-log-server)
* [Send Slack Message](/docs/send-slack-message)
* [Push System notification](/docs/push-system-notification)
* [AWS - Send JSON to S3](/docs/send-json-to-amazon-s3)
* Any Enforcement Action that supports attaching a CSV file.

In this way you can set the system to send the results of a specific query to a certain destination.

<Callout icon="📘" theme="info">
  Note

  These  actions send JSON files and not tables.
</Callout>