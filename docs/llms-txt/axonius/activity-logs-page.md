# Source: https://docs.axonius.com/docs/activity-logs-page.md

# Activity Logs Page

Use the **Activity Logs** page to track all User and System activities in the Axonius system.

By default, all User and System activities are written to the relevant Activity Logs, with the exception of Read activities. You can enable logging access (Read) activities to the Activity Logs from the [Activity Logs System Settings](/docs/configuring-activity-logs-settings).

<Callout icon="📘" theme="info">
  Note

  When a user is required to change their expired password upon logging in, this action is logged even though no user is yet logged in to the system.
</Callout>

To open the **Activity Logs** page, from the left navigation panel, click the **Activity Logs**  icon.

<Image alt="ActivityLogsNEWUI.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActivityLogsNEWUI.png" />

## Activity Logs Overview

The **Activity Logs** page displays a list of all activities in the Axonius system, sorted from the newest to the oldest activities.

This page provides the following details:

* **Type** - the type of activity.
  * User Activity ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(795\).png) - Activity done by a user (e.g., Delete Report, Add Role).
  * System Activity ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(796\).png) - Activity done by the system (e.g., Fetch devices, Discovery Cycle Ended)

* **Date** - The timestamp of the activity in UTC time.

* **User** - The user who performed the activity. The user name is displayed with a prefix:
  * **internal** - A user defined internally in Axonius by one of the system admins.
  * **saml** or **ldap** - A user who logged in using the SAML or LDAP-based login options.

* **Role** - The role that defines the permissions of the user.

* **Data Scope** - When the 'Data Scope' feature is activated on the system, the log page shows the Data Scope that defines the assets that the user can access.

* **Impersonated by** - When the 'Impersonation' feature is activated on the system, the log page shows which activities were performed by a user in impersonation mode.

* **Action** - The action of the activity. Includes **View** actions only if you enable the option in [Activity Logs System Settings](/docs/configuring-activity-logs-settings).

* **Category** - The category of the activity.

* **Discovery Cycle** - The identifier of the discovery cycle in which the activity occurred. This is presented as the start date and time of the discovery cycle. You can also select the **Latest** discovery cycle.

* **Message** - A message with additional details about the activity.  Hover over the "Copy to Clipboard" icon at the end of the message, and click on it, to copy the complete text of the message.
  * **Edit Connection Messages** - Messages for *Edit Connection* actions show:
    * *Old configuration*
    * *New configuration*
    * *Changed configuration only* - presents only changes that were made.
  * **Edit Advanced Settings in Adapters** - Messages for *Edit Advanced Settings* actions show:
    * *Old configuration*
    * *New configuration*
    * *Changed configuration only* - presents only changes that were made.

<Callout icon="📘" theme="info">
  Note

  When there are multiple changes to a user account, each change is detailed in a separate log entry.
</Callout>

### Changing the Order Columns are Displayed

You can change the order of columns displayed.
Drag and drop columns on the table to arrange them in the order you want. The changes are only for the current session.

## Searching and Filtering

You can filter the logs that are displayed. You can then use the filters to create System queries based on the filters and also save them as queries which can be used later on. [Read more about System Queries.](/docs/creating-queries-filters)

<Image alt="Logfilters2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Logfilters2.png" />

The following filters are available:

* **User** - The user or users who performed actions.
* **Role** - The role or roles that performed actions.
* **Data Scope** - The data scope or scopes in which actions were performed.
* **Action** - The type or types of actions performed on your system.
* **Category** - The category or categories of the actions available on your system.
* **Type** - The type of log message that indicates the source of system activity.
* **Discovery Cycle** - Display only fetch history from a specific Discovery Cycle, or Cycles.
* **Time Range** - The activities that occurred in a specified period of time. See [Filtering by Date](/docs/activity-logs-page#filtering-by-date) below to learn how to choose the date range.
* **Search Log Messages** - Search for any text in a log message.

### Filtering by Date

You can filter activities by date with the date range picker or by a specified last number of hours, days, weeks, months, or years, or for a time range prior to the number of hours, days, weeks, months, or years set.

**To filter by date range:**

1. From the **Time Range** dropdown, select **In range**.
2. Select **Start date** and **End date** to indicate the date range to display results.
3. To filter results only for a specific date, select the same date twice.
4. If you want to include specific times in the date range, click **Select Time** in the date range picker.
5. Click **OK** to set the **Time Range** filter.

<Image align="center" border={false} src="https://files.readme.io/4a99c189562800f25a248d7a4365d148569aa631bb8188f466de83d7dde13d06-TimeRange.png" />

**To filter by the last number of hours, days, weeks, months, or years:**

1. From the **Time Range** dropdown, select **Last** and specify a value in the field next to **Last**.
2. By default, the value is the number of days. If you want to filter by hours/weeks/months/years, select the relevant option from the **days** dropdown.

<Image align="center" border={false} src="https://files.readme.io/463b27b594730e9231d2f7a9d1051023528b0d95da5b0f5612709b81d4bbaa59-TimeRangePeriod.png" />

<br />

**To filter by the number of days ago:**

You can set a Time Range to show only the events prior to the number of hours, days, weeks, months, or years set.

1. From the **Time Range** dropdown, select **Prior to**.
2. In the number field, enter a value or use the arrows to select the value you want.

* By default, the value is the number of days. If you want to filter by hours/weeks/months/years, select the relevant option from the **days** dropdown.

<Image align="center" border={false} src="https://files.readme.io/36c67deeb100cf2b603f534e257755c0a1625454ed6443ba9da09f8fdd815bab-TimeRangePriorto.png" />

* Click **Clear All** to clear all selections in a specific filter.
* Click **Reset**  from the top left of the Activity Logs page to clear all filters and display the entire log activity.

<Image alt="New Query_ActivityLog" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/New%20Query_ActivityLog.png" />

### Saving Filters and Searches

You can save filters and searches you configure on this page as Queries, Refer to [System Queries (Creating Queries Using Filters)](/docs/creating-queries-filters) for full details. Once you save a query, you can see it on the [Queries page](/docs/queries).
Use:

* **Save As** - to save the filters/search as a Query
* **Reset**  - to reset the display

## Activity Logs Retention

The Activity Logs page displays up to 5 million of the most recent activities recorded in the system.

## Exporting Activity Logs

You can export the activity logs results table data to a CSV file.

**To export the results to a CSV file:**

* In the **Activity Logs** page, on the right side above the table, click **Export CSV** .
  The CSV file is automatically downloaded with a name format as: <br />
  `axonius_activity_logs_< date >< time >.csv`

When you set a filter, only the filtered data is exported to the CSV file.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).