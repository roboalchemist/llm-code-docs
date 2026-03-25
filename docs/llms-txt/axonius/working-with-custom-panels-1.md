# Source: https://docs.axonius.com/docs/working-with-custom-panels-1.md

# Working with Custom Charts

Use custom charts to create tailored dashboards that meet your specific needs.

## Adding a New Chart

While the default dashboard charts contribute the first and immediate insights based on basic and known policies, you can leverage the dashboard to add additional custom charts. Additional charts provide a more complete and comprehensive view for your organization's custom policies.

**To add a new chart:**

1. Open the **Dashboard** page by clicking ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dashboard%20icon%281%29.png) icon on the left navigation panel, select a dashboard and click **Add Chart**.

   <Image alt="DashboardNew-AddChart.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/f1643b6fbeb32da931ecc526ebd6c1dea181ebbd/Images/DashboardNew-AddChart.png" />

2. The **Chart Wizard** opens. Select a chart widget, enter a chart title, and set the configuration options for the visual/chart type and parameters according to the chosen metric.

   <Image align="center" alt="ChartConfig-Left.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartConfig-Left.png" />

   * The widget determines the type of measurement displayed. In a data context, these are the numbers or values that can be summed and/or averaged together with dimensions, which are the categorical buckets that can be used to segment, filter, or group.
   * As you add metrics to the chart, a preview is displayed in the left preview pane.
   * Visuals, like all other elements, are derived from saved queries. Some visuals relate to  measurements that apply to multiple queries and while others relate to a single query:
   * Multiple query metrics compare the number of results of different queries.
   * Single query metrics segment or sum/average results of a single field of a query.
     * You can create the following custom charts:
       * [Query Intersection](/docs/query-intersection-chart)
       * [Query Comparison](/docs/query-comparison-chart)
       * [Field Segmentation](/docs/field-segmentation-chart)
       * [Adapter Segmentation](/docs/adapter-segmentation-chart)
       * [Field Summary](/docs/field-summary-chart)
       * [Query Timeline](/docs/query-timeline-chart)
       * [Matrix Data](/docs/matrix-data-chart)
       * [Pivot chart](/docs/adv-pivot-chart)
       * [Asset Table](/docs/asset-table)
       * [Text Only](/docs/text-only)

3. Click  **Save** to create the chart.
   Once created, use the chart actions to edit, remove, copy, move or refresh. Hover over the chart to reorder it or to pick a date in order to display historical data. For details, see [Chart Actions](/docs/chart-actions).

## Display a List of the Assets Represented by a Chart or Chart Section

Use chart click-through to verify your chart configuration. When configuring a chart, you can click on a chart segment in the preview to open a list of those assets represented by that section.

When viewing a chart on a dashboard, you can click on some charts or their chart sections to display a table listing those relevant assets, similar to what you see when clicking on a chart section in the chart preview. The columns of the table will be updated to reflect what is displayed in the chart.