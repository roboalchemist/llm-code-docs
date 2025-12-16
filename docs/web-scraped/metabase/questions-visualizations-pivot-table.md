# Source: https://www.metabase.com/docs/latest/questions/visualizations/pivot-table

<div>

1.  [Home](/docs/latest/)
2.  [Questions](/docs/latest/questions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Pivot tables

> Pivot tables are currently only supported for questions built in the [query builder](../query-builder/editor). Pivot tables are not supported for NoSQL databases like MongoDB.

Pivot tables allow you swap rows and columns, group data, and include subtotals in your table. You can group one or more metrics by one or more dimensions.

                    width: 100%;
                    height: 0;
                    padding-bottom: 56.25%"}

## Pivot tables vs. regular tables 

Your typical, basic table is a grid of cells. Every dimension (also known as attribute, "group by") is represented by a column. Each record is represented as a row. For example, in the table below, `Source`, `Plan`, and `Created at` are dimensions/attributes for metric values `Sum of Seats` and `Count`:

![Unpivoted table](../images/unpivoted-table.png)

A pivot table is a table that has dimensions in both rows and columns, and metric values in the cells. Pivot tables can include summary rows with totals across for those dimensions:

![Pivoted table](../images/pivoted-table.png)

The reason they're called pivot tables is because you can rotate ("pivot") a column 90 degrees so that the values in that column become column headings themselves. Pivoting values into column headings is useful when analyzing data across multiple attributes, like time, location, and category. You can pivot multiple rows to columns and vice versa, or not pivot any at all.

Pivot table is the only Metabase visualization type (besides the plain table, of course) can display several metrics simultaneously along several dimensions.

## How to create a pivot table

To create a pivot table, you'll need to use the query builder. Currently, you can't build pivot tables for questions written in SQL, because Metabase would need to modify your SQL code to calculate subtotals. If you need to use SQL, the workaround here is to create your question in two steps: first do all the complex things you need to do in SQL, save the results as a question, then use that saved SQL question as the starting point for a new query builder question which summarizes that data.

1.  Create a question in the query builder that has a summary with at least one breakout, for example "`Count` of orders by `Category` and `Month`".

    You can have multiple metrics in the query (for example, "`Count` *and `Average of Total` of orders* by `Category` and `Month`")

    ![Pivot table notebook](../images/pivot-table-notebook.png)

2.  Click on **Visualize**.

3.  To change the visualization to the pivot table, click on the **Visualization** icon in the bottom left and select **Pivot table** in the sidebar.

4.  To configure fields displayed as rows and columns in the pivot table, click on the **gear** icon and assign fields to one of three "buckets": **rows**, **columns** or **measures**.

    -   **Rows** and **Columns** should contain the dimensions, or breakouts - in other words, the fields you're grouping by, like `Category` or `Created at`.
    -   **Measures** should contain your summaries, or metrics - things like `Count` or `Average of Total`.

    ![Pivot table options](../images/pivot-table-options.png)

    You can put multiple fields in the "rows" and "columns" buckets, but note that the order of the fields changes how Metabase displays the table: each additional field will nest within the previous field.

Currently, all the dimension and metrics in your query must appear as either rows, columns, or measures in the pivot table (although you can [collapse rows to their totals](#totals-and-grand-totals)). If you don't want to display a breakout or metric in the pivot table, you'll need to remove it from the query - you can't hide it from the pivot table.

## Totals and grand totals

Where it makes sense, Metabase will automatically include subtotals for grouped rows.

![Pivot table options](../images/pivot-table-options.png)

For example, as in the image above, because we've grouped our rows first by `Source`, then by `Plan`, Metabase will list each plan for each `Source`, and then aggregate the metric(s) for that source..

To collapse a group on a pivot table, you can click on the minus (--) button next to the group's heading (or the plus (+) button to expand it). When you save a pivot table, Metabase will remember which groups were expanded and which were collapsed.

You can ask Metabase to hide the totals by going to pivot table settings (**gear** icon) and toggling off "Show row/column totals".

## Conditional formatting in pivot tables

You can add colors to pivot tables based on conditions, or using a range of values:

![Conditional formatting](../images/pivot-conditional-formatting.png)

Metabase won't format totals or grand totals.

Conditional formatting for pivot tables works the same way as for regular tables, so see [Conditional formatting](./table#conditional-table-formatting)

## Using pivot tables as heatmaps

You can use conditional formatting in pivot tables to mimic a "heat map" of values by dimensions:

1.  Create a query builder question with a summary block that has:

-   One metric that defines the intensity of the cells in heatmap
-   Two breakouts to define the horizontal and vertical components of the map

1.  Visualize the query as a pivot table.
2.  Add a **"Color range"** conditional formatting.

For example, to build a heatmap of hourly activity by day of the week, use a query with breakouts by hour of day and day of the week:

![Query for the heatmap](../images/heatmap-query.png)

Use pivot table with conditional formatting:

![Pivot table as a heatmap](../images/pivot-table-as-heatmap.png)

## Pivot table exports

There are special considerations when exporting pivot tables as XLSX files. See [Exporting pivot tables](../exporting-results#exporting-pivot-tables).

## Pivot table limitations

-   Pivot tables are only available for SQL databases.
-   All metrics and dimensions specified in the query will be displayed in the pivot table.
-   Pivot tables are only available for questions built with the query builder.
-   The query builder question must have a summary block.

If you must use SQL, and your SQL query doesn't have parameters, you can save that SQL query , then use its [results as the starting point](../native-editor/writing-sql#explore-sql-question-results-using-the-query-builder) for a query builder question to build a question. The trick here is to do your aggregation and grouping in the query builder. That is, use the SQL question to grab the raw data you want to work with (maybe [create a model](../../data-modeling/models)), then start a new question in the query builder to filter, summarize, and group that data.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/visualizations/pivot-table.md) ]