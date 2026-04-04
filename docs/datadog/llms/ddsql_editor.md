# Source: https://docs.datadoghq.com/ddsql_editor.md

---
title: DDSQL Editor
description: >-
  Query infrastructure resources and telemetry data using natural language or
  DDSQL syntax with support for tags as table columns.
breadcrumbs: Docs > DDSQL Editor
---

# DDSQL Editor

{% callout %}
##### Advanced Data Sources

If you want to query data sources not yet available, use the following form to submit your request. For a full list of supported data sources, see the [Data Directory](https://docs.datadoghq.com/ddsql_reference/data_directory/).

[Request Access](https://www.datadoghq.com/product-preview/additional-advanced-querying-data-sources/)
{% /callout %}

## Overview{% #overview %}

With [DDSQL Editor](https://app.datadoghq.com/ddsql/editor), you can get deeper visibility into your telemetry by querying your resources with natural language or with DDSQL, a dialect of SQL with additional support for querying tags.

You can also export the results of a DDSQL query to visualize in a Dashboard or Notebook or to automate in a Datadog Workflow through DDSQL Action.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/query-results-avg-cpu-usage-by-host.1eff5518135e1ba57f61251514e83e33.png?auto=format"
   alt="The result of a SQL query showing average CPU usage by host on the DDSQL page in Datadog" /%}

## Query in natural language{% #query-in-natural-language %}

Type your question into the search box, and Datadog builds the SQL query for you. You can accept or discard changes, and can provide feedback to help improve the feature.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/natural-language-query-2.be927449ad6468534debd8b9fcff1523.png?auto=format"
   alt="A query inputted into the natural language search box" /%}

## Use SQL syntax (DDSQL){% #use-sql-syntax-ddsql %}

[DDSQL](https://docs.datadoghq.com/ddsql_reference/ddsql_default/) is a query language for Datadog data. It implements several standard SQL operations, such as `SELECT`, and allows queries against unstructured data, such as [tags](https://docs.datadoghq.com/ddsql_reference/ddsql_default/#tags). Get exactly the data you want by writing your own `SELECT` statement. Query tags as if they are standard table columns. For more information, see the [DDSQL Reference](https://docs.datadoghq.com/ddsql_reference/ddsql_default/).

```sql
SELECT instance_type, count(instance_type)
FROM aws.ec2_instance
WHERE tags->'region' = 'us-east-1' -- region is a tag, not a column
GROUP BY instance_type
```

## Explore your telemetry{% #explore-your-telemetry %}

View, filter, and built queries in the Data Explorer.

Click a table name to view its columns and relationships:

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/data-tab.eff4086b5445e1ddbd3ffcb487c90603.png?auto=format"
   alt="The data tab showing table information for aws.ec2_instance" /%}

For data sources such as Logs, use the query builder to generate table functions.

## Save and share queries{% #save-and-share-queries %}

Save useful queries for future reference or download the data as CSV. Browse and re-run recent or saved queries in the side panel.

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/save-and-actions.f11eaafcd68ac6d877d9c174b9800a98.png?auto=format"
   alt="DDSQL Editor interface showing query results with save and actions downdown highlighted" /%}

Export the results of a saved query to:

- A Dashboard or Notebook for visualization and reporting
- Automate using a [DDSQL Action](https://app.datadoghq.com/actions/action-catalog#com.datadoghq.dd/com.datadoghq.dd.ddsql/com.datadoghq.dd.ddsql.tableQuery) in a Datadog Workflow, with which you can:
  - [Create a custom metric from a DDSQL query](https://app.datadoghq.com/workflow/blueprints/create-a-metric-from-a-ddsql-query)
  - [Programmatically export the results of a DDSQL query](https://app.datadoghq.com/workflow/blueprints/export-ebs-volumes-not-in-ddsql-as-s3-csv)
  - [Schedule a Slack message for checking compliance of resources](https://app.datadoghq.com/workflow/blueprints/idle-compute-check-via-ddsql-with-slack-updates)
- Alert on a DDSQL query in Preview (Logs, Metrics, RUM, Spans, and Product Analytics only; [contact support](https://docs.datadoghq.com/help/) for access)

{% image
   source="https://datadog-docs.imgix.net/images/ddsql_editor/queries-tab-recent-queries.5a67c8a87843a31fb80f4d2cb386c0c0.png?auto=format"
   alt="Side panel showing the Queries tab with a list of saved and recent queries in the DDSQL Editor" /%}

## Permissions{% #permissions %}

To access the DDSQL Editor app, users need the `ddsql_editor_read` permission. This permission is included in the Datadog Read Only Role by default. If your organization uses custom roles, add this permission to the appropriate role. For more information on managing permissions, see the [RBAC documentation](https://docs.datadoghq.com/account_management/rbac/).

## Further reading{% #further-reading %}

- [DDSQL Reference](https://docs.datadoghq.com/ddsql_reference/ddsql_default)
- [Explore your data with Sheets, DDSQL Editor, and Notebooks for advanced analysis in Datadog](https://www.datadoghq.com/blog/advanced-analysis-tools/)
