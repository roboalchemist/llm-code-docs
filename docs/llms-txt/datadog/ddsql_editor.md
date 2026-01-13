# Source: https://docs.datadoghq.com/ddsql_editor.md

---
title: DDSQL Editor
description: >-
  Query infrastructure resources and telemetry data using natural language or
  DDSQL syntax with support for tags as table columns.
breadcrumbs: Docs > DDSQL Editor
source_url: https://docs.datadoghq.com/index.html
---

# DDSQL Editor

{% callout %}
##### Advanced Data Sources

If you want to query data sources not yet available, use this form to submit your request.

[Request Access](https://www.datadoghq.com/product-preview/additional-advanced-querying-data-sources/)
{% /callout %}

## Overview{% #overview %}

With [DDSQL Editor](https://app.datadoghq.com/ddsql/editor), you can get deeper visibility into your infrastructure by querying your resources with natural language or with DDSQL, a dialect of SQL with additional support for querying tags.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/query-results-cloud-provider-host-count.84f58cf65c38fc78069fbe4b6b9f0632.png?auto=format"
   alt="The result of a SQL query showing cloud provider host count on the DDSQL page in Datadog" /%}

## Query in natural language{% #query-in-natural-language %}

Type your question into the search box, and Datadog builds the SQL query for you. You can accept or discard changes, and can provide feedback to help improve the feature.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/natural-language-query-2.be927449ad6468534debd8b9fcff1523.png?auto=format"
   alt="A query inputted into the natural language search box" /%}

## Use SQL syntax (DDSQL){% #use-sql-syntax-ddsql %}

DDSQL is a query language for Datadog data. It implements several standard SQL operations, such as `SELECT`, and allows queries against unstructured data, such as [tags](https://docs.datadoghq.com/ddsql_reference/ddsql_default/#tags). Get exactly the data you want by writing your own `SELECT` statement. Query tags as if they are standard table columns. For more information, see the [DDSQL Reference](https://docs.datadoghq.com/ddsql_reference/ddsql_default/).

```sql
SELECT instance_type, count(instance_type)
FROM aws.ec2_instance
WHERE tags->'region' = 'us-east-1' -- region is a tag, not a column
GROUP BY instance_type
```

## Explore your telemetry{% #explore-your-telemetry %}

{% alert level="danger" %}
Querying Logs, Metrics, Spans, and RUM through DDSQL is in Preview. Use this [form](https://www.datadoghq.com/product-preview/logs-metrics-support-in-ddsql-editor/) to request access.
If you want access to Spans, RUM, or other data sources not listed in the use cases section, mention them in the access request form.
{% /alert %}

View, filter, and built queries in the Data Explorer.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/data-tab-available-tables.a4044e1502126fc4337c2bda8ecfee7c.png?auto=format"
   alt="Side panel showing a list of available tables for querying in the DDSQL Editor" /%}

Click a table name to view its columns and relationships:

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/data-tab.eff4086b5445e1ddbd3ffcb487c90603.png?auto=format"
   alt="The data tab showing table information for aws.ec2_instance" /%}

For data sources such as Logs, use the query builder to generate table functions.

## Save and share queries{% #save-and-share-queries %}

Save useful queries for future reference or download the data as CSV.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/save_export.3bfe4fe562297fe245c3f13184a58717.png?auto=format"
   alt="DDSQL Editor interface showing query results with save and export options highlighted" /%}

Export a saved query to a dashboard by clicking **Save to Dashboard**. From a dashboard you can visualize results and send Scheduled Reports.

Browse and re-run recent or saved queries in the side panel.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/queries-tab-recent-queries.5a67c8a87843a31fb80f4d2cb386c0c0.png?auto=format"
   alt="Side panel showing the Queries tab with a list of saved and recent queries in the DDSQL Editor" /%}

## Permissions{% #permissions %}

To access the DDSQL Editor app, users need the `ddsql_editor_read` permission. This permission is included in the Datadog Read Only Role by default. If your organization uses custom roles, add this permission to the appropriate role. For more information on managing permissions, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/).

## Further reading{% #further-reading %}

- [DDSQL Reference](https://docs.datadoghq.com/ddsql_reference/ddsql_default)
- [Explore your data with Sheets, DDSQL Editor, and Notebooks for advanced analysis in Datadog](https://www.datadoghq.com/blog/advanced-analysis-tools/)
