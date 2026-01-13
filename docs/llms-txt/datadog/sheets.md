# Source: https://docs.datadoghq.com/sheets.md

---
title: Sheets
description: >-
  Analyze Datadog data in a familiar spreadsheet interface with pivot tables,
  lookups, calculated columns, and complex analysis tools.
breadcrumbs: Docs > Sheets
source_url: https://docs.datadoghq.com/index.html
---

# Sheets

{% callout %}
##### Join the Preview!

Create flexible spreadsheets: built to let you start from scratch, build models, track operations, and more.

[Request Access](https://www.datadoghq.com/product-preview/flexible-spreadsheets-in-datadog-sheets/)
{% /callout %}

## Overview{% #overview %}

Sheets is a spreadsheet tool that you can populate with Datadog data, enabling you to perform complex analysis and build reports without requiring technical expertise. It allows teams to use familiar spreadsheet functions like lookups, pivot tables, and calculations on Datadog data, so you don't have to export and use another tool with stale data.

Sheets lets you manipulate, transform, and analyze data from logs, real user monitoring, and cloud cost monitoring in a familiar spreadsheet interface.

## Create a table{% #create-a-table %}

Start by creating a table of data, either by building a new query from Sheets or transferring a query from the logs explorer, RUM explorer or metrics explorer.

### Add a new table in Sheets{% #add-a-new-table-in-sheets %}

{% image
   source="https://datadog-docs.imgix.net/images/sheets/create_table.3378b949ca5659f4af76bf322e274a16.png?auto=format"
   alt="Modal to create to create a table from Sheets, showing a Logs query with status:error" /%}

1. On the [Datadog Sheets page](https://app.datadoghq.com/sheets), click **New Spreadsheet**.
1. Click **Add Data**.**Note**: if there is a data source you want that is not available, request it [here](https://www.datadoghq.com/product-preview/additional-advanced-querying-data-sources/).
1. Start building your query by selecting your Data source, and adding filtering parameters.
1. Select the columns you want to display and preview the resulting table.
1. Click **Create Table**.

### Transfer your query to a spreadsheet{% #transfer-your-query-to-a-spreadsheet %}

1. On the page of a supported product (such as the [Log Explorer](https://app.datadoghq.com/logs)), build the query of data you want to analyze, such as filtering your Logs view to those that have `status:error`.
1. Click **Open in Sheets**. For a list of product pages you can create a table from, see the Supported data sources section.
1. You can create a **New Spreadsheet** or add this table of data to an **Existing Spreadsheet**.
1. Click **Save and Open**.

## Calculated columns{% #calculated-columns %}

You can use a calculated column to add a formula, parse a log message, extract regex, or add business logic to your data. Your calculated columns can be used in the pivot table you'll create later.

From the header of the far right column of your table, click the Plus icon to **Add calculated column**. Enter a function to view the syntax and description of the function. For a full list of supported functions, see the [Functions and Operators](https://docs.datadoghq.com/sheets/functions_operators) documentation.

{% image
   source="https://datadog-docs.imgix.net/images/sheets/calculated_columns.211c885d6f565891b279eb4706da69cf.png?auto=format"
   alt="Added calculated column with the Plus icon, and an example IFS function" /%}

## Lookup{% #lookup %}

Lookup enriches your existing data and adds more context to your table. Click **Add Lookup** at the top of the page to add columns from another table or data source, such as [Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=manualupload), logs, or RUM data. Lookup is like a left join or a vlookup in Excel or Google Sheets; it matches records on a common column, and returns additional columns of data to enrich your existing Sheets table.

{% image
   source="https://datadog-docs.imgix.net/images/sheets/lookup.68d197af43261459b72139ef7a0432f4.png?auto=format"
   alt="Example Lookup which adds a user's team metadata sourced from a reference table" /%}

For example, you have a table of RUM data with user emails, and you want to know which teams these users belong to. You can add a lookup that compares the user email column in your table with the work email column in a Reference Table. Lookup pulls the team from the Reference Table and adds it as a new column to your spreadsheet.

## Pivot table{% #pivot-table %}

After you add a table of data to a spreadsheet, analyze and add context to your raw data with a Pivot table. Use pivot tables to summarize and organize large amounts of data into customized tables. It helps you analyze data to find patterns and trends, and see comparisons. For example, you can have a table with a hundred rows, but with a pivot table you can break down that data into a summary table that counts your data by method or region. To create a pivot table:

1. From an existing spreadsheet that already has a table of data, click **Add Pivot Table**.
1. In the **Rows** and **Columns** section, select the dimensions you want to analyze, such as the status of logs.
1. In the **Calculations** section, select the dimensions you want to use in calculations, including sum, average, count, min, and max.

{% image
   source="https://datadog-docs.imgix.net/images/sheets/example_pivot_table.40381dd8992287f38af91a2851d2721a.png?auto=format"
   alt="Example pivot table configuration panel" /%}

### Visualizations{% #visualizations %}

After you have your pivot table, you can click **Show Graphs** and add up to six widgets to graph your data. Supported widget types include **Top List**, **Treemap**, and **Pie Chart** widgets. Hover over the widget title to delete, duplicate, expand, export, and reposition widgets. To edit a widget, click the pencil icon. Editing options allow you to select the widget type, choose which pivot calculation to graph (if there is more than one), and specify the rows, columns, and the number of groupings graphed per row or column.

## Supported data sources{% #supported-data-sources %}

{% callout %}
##### Advanced Data Sources

If you want to query data sources not yet available, use this form to submit your request.

[Request Access](https://www.datadoghq.com/product-preview/additional-advanced-querying-data-sources/)
{% /callout %}

Create tables and analyze the data pulled from the following data sources:

| Data Source          | Product page                                                       |
| -------------------- | ------------------------------------------------------------------ |
| APM Spans            | [APM Explorer](https://app.datadoghq.com/apm/traces)               |
| Audit Trail          | [Audit Trail](https://app.datadoghq.com/audit-trail)               |
| CI Pipelines         | [CI Visibility](https://app.datadoghq.com/ci/pipelines)            |
| Cloud Cost           | [Cloud Cost Analytics](https://app.datadoghq.com/cost)             |
| Database Queries     | [Database Monitoring](https://app.datadoghq.com/databases/queries) |
| Events               | [Event Management](https://app.datadoghq.com/event/explorer)       |
| Infrastructure       | [DDSQL Editor](https://app.datadoghq.com/ddsql/editor)             |
| LLM Observability    | [LLM Observability](https://app.datadoghq.com/llm/applications)    |
| Logs                 | [Logs Explorer](https://app.datadoghq.com/logs)                    |
| Metrics              | [Metrics Explorer](https://app.datadoghq.com/metric/explorer)      |
| Real User Monitoring | [RUM Explorer](https://app.datadoghq.com/rum/sessions)             |
| Reference Tables     | [Reference Tables](https://app.datadoghq.com/reference-tables)     |
| Security Findings    | [Cloud Security](https://app.datadoghq.com/security/compliance)    |
| Security Signals     | [Security](https://app.datadoghq.com/security)                     |

## Configuring a spreadsheet{% #configuring-a-spreadsheet %}

### Permissions{% #permissions %}

By default, all users have full access to spreadsheets.

Use granular access controls to limit the [roles](https://docs.datadoghq.com/account_management/rbac/) that may edit a particular spreadsheet:

1. While viewing a spreadsheet, click on the cog in the upper right. The settings menu opens.
1. Select **Permissions**.
1. Click **Restrict Access**. The dialog box updates to show that members of your organization have **Viewer** access by default.
1. Use the dropdown to select one or more roles, teams, or users that may edit the spreadsheet.
1. Click **Add**. The dialog box updates to show that the role you selected has the **Editor** permission.
1. Click **Save**.

**Note:** To maintain your edit access to the spreadsheet, you must include at least one role that you are a member of before saving.

You must have edit access to restore general access to a restricted spreadsheet. Complete the following steps:

1. While viewing the spreadsheet, click on the cog in the upper right. The settings menu opens.
1. Select **Permissions**.
1. Click **Restore Full Access**.
1. Click **Save**.

## Further reading{% #further-reading %}

- [Functions and Operators](https://docs.datadoghq.com/sheets/functions_operators)
- [Explore your data with Sheets, DDSQL Editor, and Notebooks for advanced analysis in Datadog](https://www.datadoghq.com/blog/advanced-analysis-tools/)
