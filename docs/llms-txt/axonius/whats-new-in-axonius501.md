# Source: https://docs.axonius.com/docs/whats-new-in-axonius501.md

# What's New in Axonius 5.0.1

These Release Notes contain new features and enhancements added in version 5.0.1.
Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Field Summary Support for Software Management

It is now possible to create [**Field Summary**](/docs/field-summary-chart) charts based on Software Management queries. Timeline is not currently supported for Software Management.

#### Query Timeline Support for Vulnerabilities and Software Management

It is now possible to create [**Query Timeline**](/docs/query-timeline-chart) charts based on Vulnerability and Software Management queries.

## Devices and Users Pages New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages:

### Displaying Historical Data on the Asset Profile Page

It is now possible to use a date picker to display the data of a specific date on the [**Asset Profile**](/docs/asset-profile-page#displaying-historical-data) page. This enables users to look at various assets for a specific date without having to go back to the relevant asset table to adjust the dates.

### Asset Investigation

It is now possible to create a Query using filters from the **[Asset Investigation](/docs/advanced-asset-investigation)** page. The queries are not currently available for use in Dashboards, Enforcement Sets etc.

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Create Enforcement Sets from Saved Queries Page

The capability was added to  create supported Vulnerabilities and Software Management Enforcement Sets directly from the **Action** menu of the [**Queries** page](/docs/managing-queries).

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Last Successful Fetch Filter

It is now possible to filter [**Connections**](/docs/adapter-connections#filtering-the-display) by **Last Successful Fetch** time. Apart from being able to see a successful fetch in a certain time range, it is also possible to show successful fetches from a certain amount of days back.

## Activity Log New Features and Enhancements

### Information about Adapter Configuration Changes  in Activity Logs

In addition to showing the old and new configuration (after changes), the **[Activity Logs page](/docs/activity-logs-page)** now also shows  information about only the specific changes made to adapter configuration. This information is shown in the **Messages** column for **Edit Connection** actions.

### Filtering Logs by Type

The capability has been added to [filter](/docs/activity-logs-page#searching-and-filtering) the **Activity Log** by activity **Type**: API, Error, Info, and User.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Behavior of Unencrypted Email SSL Connection

When selecting the **Unencrypted** option for the email SSL connection (**Use SSL for connection** under **System Settings> External Integrations> Email**), the system attempts to use TLS when sending emails (the default; no TLS configuration required). If TLS fails and the connection is active (if lost, the system first reestablishes the connection), the system proceeds to send emails without TLS.