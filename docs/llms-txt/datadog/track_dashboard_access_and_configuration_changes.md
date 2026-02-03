# Source: https://docs.datadoghq.com/account_management/audit_trail/guides/track_dashboard_access_and_configuration_changes.md

---
title: Track Dashboard Access and Configuration Changes
description: >-
  Use Audit Trail to track dashboard usage, access patterns, and configuration
  changes with API request monitoring and diff inspection.
breadcrumbs: >-
  Docs > Account Management > Datadog Audit Trail > Audit Trail Guides > Track
  Dashboard Access and Configuration Changes
---

# Track Dashboard Access and Configuration Changes

## Overview{% #overview %}

Audit Trail provides Datadog administrators visibility into who within the organization is using Datadog and how they are using it. This guide walks you through how you can see usage information for a specific dashboard.

## View usage information for a specific dashboard{% #view-usage-information-for-a-specific-dashboard %}

### Get dashboard ID{% #get-dashboard-id %}

You need the dashboard's ID to get usage information for the dashboard.

1. Navigate to [Dashboards](https://app.datadoghq.com/dashboard/lists).
1. Select your dashboard.
1. The dashboard ID is in the dashboard URL, located after `https://app.datadoghq.com/dashboard/`. For example, if the dashboard URL is `https://app.datadoghq.com/dashboard/pte-tos-7kc/escalations-report`, the dashboard ID is `pte-tos-7kc`.
1. Copy the dashboard ID.

### View dashboard usage in Audit Trail{% #view-dashboard-usage-in-audit-trail %}

To see usage information for the dashboard, use Audit Trail to search for all API `GET` requests for that dashboard ID.

1. Navigate to [Audit Trail](https://app.datadoghq.com/audit-trail).
1. In the search bar, enter the query: `@http.status_code:200 @http.method:GET @http.url_details.path:/api/v1/dashboard/<dashboard_id>`. Replace `<dashboard_id>` with the dashboard ID you copied earlier.For example, if the dashboard ID is `pte-tos-7kc`, the search query looks like this:
   {% image
      source="https://datadog-docs.imgix.net/images/account_management/audit_logs/dashboard_access_query.e403f3b72b2e32984e9e045933a8a976.png?auto=format"
      alt="Search query for all successful GET requests for the dashboard ID pte-tos-7kc" /%}
`@http.status_code:200` narrows down the results to successful requests only.**Note**: You can also use the facet panel on the left side of the page to formulate the search query.
1. Select the timeframe in the upper right side of the page to see the events for a specific time period.
1. You can configure the **Group into fields** section and select different visualization tools to break down and analyze the data based on your use case. For example, if you set the `group by` field to `User Email` and click **Top List** in the **Visualize as** section, you get a top list of users who accessed the dashboard.
1. See [Create a dashboard or a graph](https://docs.datadoghq.com/account_management/audit_trail/#create-a-dashboard-or-a-graph) if you want to put this information into a dashboard or graph.

## View recent dashboard configuration changes{% #view-recent-dashboard-configuration-changes %}

You can use [event queries](https://docs.datadoghq.com/account_management/audit_trail/events) in Audit Trail to see a list of dashboards that have had recent changes to their configurations.

1. Navigate to [Audit Trail](https://app.datadoghq.com/audit-trail).

1. In the **Search for** field, paste a query to filter for the kind of changes you want to see. Here are some common examples:

| Audit event                                                                                                                                            | Query in audit explorer                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| [Recently created dashboards](https://app.datadoghq.com/audit-trail?query=%40evt.name%3ADashboard%20%40asset.type%3Adashboard%20%40action%3Acreated)   | `@evt.name:Dashboard @asset.type:dashboard @action:created`  |
| [Recently modified dashboards](https://app.datadoghq.com/audit-trail?query=%40evt.name%3ADashboard%20%40asset.type%3Adashboard%20%40action%3Amodified) | `@evt.name:Dashboard @asset.type:dashboard @action:modified` |
| [Recently deleted dashboards](https://app.datadoghq.com/audit-trail?query=%40evt.name%3ADashboard%20%40asset.type%3Adashboard%20%40action%3Adeleted)   | `@evt.name:Dashboard @asset.type:dashboard @action:deleted`  |

1. Optionally, on the facet panel, use filters like **Asset ID** or **Asset Name** to narrow your results down to a specific dashboard.

1. For each event in the table, you can see the email address of the user who performed the last change, and a summary of what happened.

To see additional information about a specific change, click the row in the table. Then, click the **Inspect Changes (Diff)** tab to see the changes that were made to the dashboard's configuration:

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/audit_logs/dashboard_change_diff.6c7a3fdac5247e32e98003c5a07e36cc.png?auto=format"
      alt="A text diff showing a new widget being added to the dashboard" /%}

1. See [Create a dashboard or a graph](https://docs.datadoghq.com/account_management/audit_trail/#create-a-dashboard-or-a-graph) if you want to put this information into a dashboard or graph.

## Further reading{% #further-reading %}

- [Set up Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/)
