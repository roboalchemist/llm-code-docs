# Source: https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility.md

---
title: Cross-Organization Visibility
description: >-
  Share data and perform queries between different organizations in the same
  account.
breadcrumbs: Docs > Account Management > Cross-Organization Visibility
source_url: https://docs.datadoghq.com/org_settings/cross_org_visibility/index.html
---

# Cross-Organization Visibility

## Overview{% #overview %}

Some companies rely on multiple Datadog [organizations](https://docs.datadoghq.com/account_management/multi_organization/) to separate data for compliance or other reasons.

Cross-organization visibility allows customers to share data between different organizations in the same account, and show insights from multiple organizations in one place.

This document explains:

- What cross-organization visibility enables
- How to share data across your organizations
- How to create a Dashboard and Notebook widget with data from your other organizations

## Capabilities{% #capabilities %}

### Organization connection{% #organization-connection %}

A *source* organization exposes data to a *destination* organization through an *organization connection*. A source organization can have multiple destinations, and a destination organization can have multiple sources.

The following limitations apply to organization connections:

- The source and destination organizations must be in the same [account](https://docs.datadoghq.com/account_management/multi_organization/)
- The source and destination organizations must be in the same [site](https://docs.datadoghq.com/getting_started/site).
- Non-Enterprise organizations can share with a maximum of 5 other organizations.

**Note**: After the connection is established, the destination organization can query the source organization's data in the same ways it can query its own data. This means that the source organization's dataâincluding sensitive dataâmay be queried and displayed as permitted by the *destination organization's* access-control and other settings. This may include, for example, the destination organization's ability to create [public Dashboards](https://docs.datadoghq.com/dashboards/sharing/shared_dashboards/#public-shared-dashboards) using the source organization's data even if the source organization's own settings do not permit the creation of public Dashboards.

After you set up an organization connection, the exposed data is still stored in the source organization and does not move to the destination. Instead, the destination organization queries the data from the source. Connections do not duplicate the data, and do not incur extra charges. The destination organization can query source data from any time range supported by the source data, including prior to the date of the creation of the connection. If you remove the connection, the destination can no longer access any data from the source and any queries or Dashboards created from the source organization's data may no longer function.

### Scope{% #scope %}

Cross-organization visibility supports the following telemetry in [Dashboard and Notebook widgets](https://docs.datadoghq.com/dashboards/widgets):

- Metrics (all types supported, including [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/#overview), [trace metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/), and [metrics generated from logs](https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/))
- Logs
- CI Visibility pipelines
- Test Optimization tests

## Configure connections{% #configure-connections %}

### List connections{% #list-connections %}

To browse connections, navigate to the [cross-organization visibility page](https://app.datadoghq.com/organization-settings/cross-org-visibility) in Organization Settings. The table lists all of your cross-organization connections.

### Create a connection{% #create-a-connection %}

Creating a cross-organization connection allows you to query metrics from the source organization in the destination organization.

1. Make sure you are signed in to the *source* organization that contains the data you want to expose.
1. On the [cross-organization visibility page](https://app.datadoghq.com/organization-settings/cross-org-visibility), click **New Connection**. The **New Connection** dialog box appears.
1. In the drop-down menu, select the *destination* organization where you want to see the data.
1. Click **Connect**.

### Update a connection{% #update-a-connection %}

Updating an existing cross-organization connection allows you to change the data types that are shared from the source organization in the destination organization.

1. Make sure you are signed in to the *source* organization of the existing connection.
1. Hover over the connection you wish to update. A pencil (**Edit**) icon appears on the right.
1. Click the pencil (**Edit**) icon on the connection you wish to update. The **Edit Connection** dialog box appears.
1. Select the checkboxes for the data types you wish to include.
1. Click **Save**.

### Delete a connection{% #delete-a-connection %}

Deleting a connection disables cross-organization querying from the destination organization of the source organization's metrics.

1. Navigate to the [cross-organization visibility page](https://app.datadoghq.com/organization-settings/cross-org-visibility) in Organization Settings.
1. Hover over the connection you wish to delete. A trash can (**Delete**) icon appears on the right.
1. Click the trash can (**Delete**) icon on the connection you wish to delete. The **Are you sure?** prompt appears.
1. Click **Delete**.

### In the API{% #in-the-api %}

To configure connections using the API, see the [cross-organizations connections API](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility_api).

## Create a widget with cross-organization data{% #create-a-widget-with-cross-organization-data %}

Cross-organization [Dashboard and Notebook widgets](https://docs.datadoghq.com/dashboards/widgets) are available for Datadog organizations that exist as a *destination* organization for at least one connection.

Each query in a widget can display data from a single organization. You can combine queries into a cross-organization formula query.

### In the UI{% #in-the-ui %}

Dashboard and Notebook widgets allow you to create cross-organization queries when the following conditions are met:

- You have cross-organization visibility enabled in your organization
- At least one connection exists where the current organization is the destination

If the previous conditions are true, an organization drop-down selector appears between the drop-down menus for data type and metric name. Use the organization drop-down selector to chose a source organization for your query.

The following screenshot shows an example of a cross-organization formula query. The widget graphs the number of ingested events per service. To get the total number of events, the cross-organization formula query sums the data from organization A (in the query **a**) and organization B (in the query **b**).

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/cross_org_visibility/cross_org_query-1.4235ba0c1da1e4ea9945c0b215d8b55e.png?auto=format"
   alt="Screenshot showing configuration of a Dashboard widget with a cross-organization query" /%}

### In the API{% #in-the-api-1 %}

{% alert level="info" %}
The [Datadog Terraform Provider](https://registry.terraform.io/providers/DataDog/datadog/latest/docs) does not support creation of cross-organization connections. However, you can manage a dashboard containing widgets with cross-org queries through Terraform by exporting the dashboard to JSON.
{% /alert %}

You can define cross-organization queries in the following endpoint:

- [Timeseries](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products)

When you define a widget in the Dashboard API, use the `cross_org_uuids` parameter in the JSON widget definition payload to identify the source organization in a cross-organization query.

The `cross_org_uuids` parameter is optional. If you omit `cross_org_uuids`, the query runs on the same organization in which you defined the widget.

### Example JSON widget definition{% #example-json-widget-definition %}

```json
{
    "viz": "timeseries",
    "requests": [
        {
            "style": {
                "palette": "dog_classic",
                "type": "solid",
                "width": "normal"
            },
            "type": "line",
            "formulas": [
                {
                    "formula": "query2 + query1"
                }
            ],
            "queries": [
                {
                    "name": "query2",
                    "data_source": "metrics",
                    "query": "sum:datadog.estimated_usage.events.ingested_events{env:prod} by {service}.as_count()",
                    "cross_org_uuids": ["6434abde-xxxx-yyyy-zzzz-da7ad0900001"]
                },
                {
                    "name": "query1",
                    "data_source": "metrics",
                    "query": "sum:datadog.estimated_usage.events.ingested_events{env:prod} by {service}.as_count()",
                    "cross_org_uuids": ["74edde28-xxxx-yyyy-zzzz-da7ad0900001"]
                }
            ],
            "response_format": "timeseries"
        }
    ]
}
```

Note the `cross_org_uuids` parameter in the JSON widget definition payload.

- This parameter is optional. If omitted, the query runs on the organization on which the widget is defined.
- Use the organization identifier, which you can recover from the [Organizations endpoint](https://docs.datadoghq.com/api/latest/organizations/#list-your-managed-organizations), to identify the organization on which the query runs.
- Though this parameter accepts an array, the array must contain only one element. Adding multiple elements to the `cross_org_uuids` array results in a 400 error.

## Permissions{% #permissions %}

By default, only users attached to roles with the *Org Connection Read* permission can see the list of cross-organization connections. Users attached to roles with the *Org Connection Write* permission can create and delete cross-organization connections.

### Granular access controls{% #granular-access-controls %}

Use [granular access controls](https://docs.datadoghq.com/account_management/rbac/granular_access) to limit the teams, roles, or users that can edit or query a cross-organization connection. These access controls govern:

- From the source organization: who can edit the connection.
- From the destination organization: who can view the shared data, and who can edit the connection.

Connections from the source org inherit the data access permissions of the connection's creator. If the creator is restricted from seeing any data by [Data Access Control](https://docs.datadoghq.com/account_management/rbac/data_access/) or [Log Restriction Queries](https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/?tab=ui#create-a-restriction-query), this data is not accessible from the destination org.

**Note:** Connections created from HIPAA-enabled organizations may allow the sharing of protected health information (PHI) to destination organizations. Customers are responsible for any sensitive data transferred, including PHI.

1. Navigate to the [cross-organization visibility page](https://app.datadoghq.com/organization-settings/cross-org-visibility) in Organization Settings.
1. Hover over the cross-organization connection on which you would like to set granular permissions. **Permissions** and **Delete** icons appear on the right.
1. Click on the padlock (**Permissions**) icon.
1. Select **Restrict Access**.
1. The dialog box updates to show that members of your organization have **Viewer** access by default.
1. Use the dropdown to select one or more teams, roles, or users that may edit the cross-organization connection.
1. Click **Add**.
1. The dialog box updates to show that the role you selected has the **Editor** permission.
1. Click **Save**.

**Note**: To maintain your edit access to the cross-organization connection, the system requires you to include at least one role or team that you are a member of before saving.

To restore general access to a cross-organization connection with restricted access, follow the steps below:

1. In the cross-organization visibility page, hover over the cross-organization connection you would like to restore general access to. **Permissions** and **Delete** icons appear on the right.
1. Click on the padlock (**Permissions**) icon.
1. Click **Restore Full Access**.
1. Click **Save**.
