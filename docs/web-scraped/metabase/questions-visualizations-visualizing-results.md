# Source: https://www.metabase.com/docs/latest/questions/visualizations/visualizing-results

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

# Visualization overview

While tables are useful for looking up information or finding specific numbers, it's usually easier to see trends and make sense of data using charts.

## Visualize query results

The query builder will automatically select an appropriate chart to visual your results. With native queries, however, you'll need to manually select a chart type.

### Visualizing questions in the query builder

To visualize results of a question built in the [query builder](../query-builder/editor), click on the **Visualize** button under the last query builder step. Metabase will select a chart type most appropriate for your data, but you can [change the visualization type](#change-visualization-type). You can also toggle between the visualization and the table of results.

You can switch between the visualization view and the query builder using the **Visualization**/**Editor** button in the top right.

![Switch to editor](../images/switch-to-editor.png)

### Visualizing native questions

To visualize results of a native query, click on the **Visualization** button in the bottom of the screen and select a visualization type.

![Visualize a native query](../images/visualize-native.png)

As long as the shape of the native query results is appropriate for the chart type - for example, a metric grouped by a date column for a trend chart - you'll be able to use all chart types, except [pivot tables](./pivot-table). [Pivot tables](./pivot-table) are currently unavailable for native queries.

## Change visualization type

To change how the answer to your question is displayed, click on the **Visualization** button in the bottom-left of the screen to open the visualization sidebar.

![Visualization options](../images/VisualizeChoices.png)

If a particular visualization doesn't make sense for your answer, that option will appear in the "Other charts" section. You can still select one of these other charts, though you might need to fiddle with the chart options to make the chart work with your data.

Not sure which visualization type to use? Check out [Which chart should you use?](/learn/metabase-basics/querying-and-dashboards/visualization/chart-guide)

## Visualization options

![Options for a chart](../images/viz-options.png)

Each visualization type has its own advanced options. To change the settings for a specific chart, for example a row chart, click on the **Gear** button in the bottom left.

## Area charts

[Area charts](./line-bar-and-area-charts) are useful when comparing the proportions of two metrics over time. Both bar and area charts can be stacked.

![Stacked area chart](../images/area.png)

## Bar charts

[Bar charts](./line-bar-and-area-charts) are great for displaying a number grouped by a category (e.g., the number of users you have by country).

![Bar chart](../images/bar.png)

## Combo charts

[Combo charts](./combo-chart) let you combine bars and lines (or areas) on the same chart.

![Line + bar](../images/combo-chart.png)

## Detail

The [Detail](./detail) visualization shows a single result record (row) in an easy-to-read, two-column display.

![Detail of a record in the account table](../images/detail.png)

## Funnel charts

[Funnels](./funnel) are commonly used in e-commerce or sales to visualize how many customers are present within each step of a checkout flow or sales cycle. At their most general, funnels show you values broken out by steps, and the percent decrease between each successive step.

![Funnel](../images/funnel.png)

## Gauges

[Gauges](./gauge) allow you to show a single number in the context of a set of colored ranges that you can specify.

![Gauge](../images/gauge.png)

## Line charts

[Line charts](./line-bar-and-area-charts) are best for displaying the trend of a number over time, especially when you have lots of x-axis values. For more, check out our [Guide to line charts](/learn/metabase-basics/querying-and-dashboards/visualization/line-charts) and [Time series analysis](/learn/metabase-basics/querying-and-dashboards/time-series) tutorials.

![Trend lines](../images/trend-lines.png)

## Maps

When you select the [Map](./map) visualization, Metabase will automatically try and pick the best kind of map to use based on the table or result set.

![Region map](../images/map.png)

## Numbers

The [Numbers](./numbers) option is for displaying a single number, nice and big.

![Number](../images/number.png)

## Pie, donut, and sunburst charts

A [pie chart or donut chart](./pie-or-donut-chart) can be used when breaking out a metric by a single dimension, especially when the number of possible breakouts is small, like accounts by plan.

A [sunburst chart](./pie-or-donut-chart) is a pie chart with more than one ring to show the data broken out by additional dimensions.

![Donut](../images/pie-sunburst-demo.png)

## Pivot tables

[Pivot tables](./pivot-table) allow you swap rows and columns, group data, and include subtotals in your table. You can group one or more metrics by one or more dimensions.

![Pivot table options](../images/pivot-table-options.png)

## Progress bars

[Progress bars](./progress-bar) are for comparing a single number to a goal value that you set.

![Progress bar](../images/progress.png)

## Row charts

[Row charts](./line-bar-and-area-charts) are good for visualizing data grouped by a column that has a lot of possible values, like a Vendor or Product Title field.

![Row chart](../images/row.png)

## Tables

The [Table](./table) option is good for looking at tabular data (duh), or for lists of things like users or orders.

![Conditional formatting](../images/conditional-formatting.png)

## Trends

The [Trend](./trend) visualization is great for displaying how a single number has changed between two time periods.

![Trend settings](../images/trend-settings.png)

## Histograms

If you have a bar chart like Count of Users by Age, where the x-axis is a number, you'll get a special kind of bar chart called a [histogram](./line-bar-and-area-charts) where each bar represents a range of values (called a "bin").

![Histogram](../images/histogram.png)

## Sankey charts

[Sankey charts](./sankey) show how data flows through multi-dimensional steps.

![Left-aligned sankey chart](../images/sankey-left-aligned.png)

## Waterfall charts

[Waterfall charts](./waterfall-chart) are a kind of bar chart useful for visualizing results that contain both positive and negative values.

![Waterfall chart](../images/waterfall-chart.png)

## Scatterplots and bubble charts

[Scatterplots](./scatterplot-or-bubble-chart) are useful for visualizing the correlation between two variables, like comparing the age of your people using your app vs. how many dollars they've spent on your products.

![Scatter](../images/scatter.png)

## Styling and formatting data in charts

![Chart formatting options](../images/chart-formatting-options.png)

You can access formatting options for the columns used in a chart. Just open the visualization settings by clicking on the **Gear** icon in bottom left.

Options differ depending on the chart, and can include settings for the chart's data, its display, and its axes.

See also [Formatting defaults](../../data-modeling/formatting).

## Further reading

-   [Charts with multiple series](../../dashboards/multiple-series)
-   [Appearance](../../configuring-metabase/appearance)
-   [BI dashboard best practices](/learn/metabase-basics/querying-and-dashboards/dashboards/bi-dashboard-best-practices)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/visualizations/visualizing-results.md) ]