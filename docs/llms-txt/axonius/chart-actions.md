# Source: https://docs.axonius.com/docs/chart-actions.md

# Chart Actions

You can perform the following actions on Axonius dashboard charts:

* [Display Chart Tools](/docs/chart-actions#display-chart-tools) - Hover over a chart to display the available chart tools.
* [Edit](#edit) - Using the chart action menu.
* [Move or Copy](#move-or-copy) - Using the chart action menu.
* [Sort](#sort) - Sort the order of bar chart segments.
* [Refresh](#refresh) - Using the chart action menu.
* [Pin](#pin) - Using the chart action menu.
* [Copy link](#copy-link) - Using the chart action menu.
* [Export to CSV](#export-to-csv) - Using the chart action menu.
* [Capture Chart](#capture-chart) - Using the chart action menu.
* [Delete](#delete) - Using the chart action menu.
* [Display Historical Data](#display-historical-data) - By hovering over the chart.
* [View Results](/docs/chart-actions#view-results) - By clicking on part of the chart.
* [Reorder](#reorder) - By hovering over the chart reorder button and use drag-and-drop.
* [Pie Chart Legend](#pie-chart-legend) - By clicking the pie chart legend button.
* [Viewing Chart Slice or Section Data](/docs/chart-actions#viewing-chart-slice-or-section-data) - By hovering over parts of the chart.

<Image alt="ChartActions" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartActions.jpg" />

**Permissions**:

* Only users with 'Edit Charts' permissions can access the chart menu, move a chart, or resize a chart.
* Only users with 'Delete charts' permissions can delete a chart.

## Display Chart Tools

Chart tools appear when hovering over a chart.

<Image alt="OnHoverChartItems" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OnHoverChartItems.png" />

For more information on filtering Dashboard charts, see [Filtering a Chart](/docs/update-chart-dynamically).

## Edit

Use **Edit** to edit chart configuration. This action is applicable only to [custom charts](/docs/working-with-custom-panels).

## Move or Copy

Use **Move or Copy** to  either copy or move a chart to a different Dashboard. Only [custom charts](/docs/working-with-custom-panels) can be moved or copied.
When selected, a **Move or Copy** dialog opens, which lets you select the Dashboard location to which the chart will be copied or moved.
To move a chart without copying it, deselect **Create a copy**.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(626).png" />

Charts created with a Dashboard template can only be copied. Custom charts added to a Dashboard created from a template can be moved or copied.

If the source dashboard is available to All Data Scopes but the destination Dashboard is accessible only from the Current Data Scope, the chart queries must be updated to ADS first.

To move a chart from a Dashboard with All Data Scope permissions to a Dashboard with Current Data Scope permissions.

## Export to CSV

Use **Export to CSV** to export the chart data to a CSV file or export as an image. The following charts can be exported to CSV:

* [Pivot chart](/docs/adv-pivot-chart)
* [Field Segmentation charts](/docs/field-segmentation-chart)
* [Adapter Segmentation charts](/docs/adapter-segmentation-chart)
* [Query Timeline charts](/docs/query-timeline-chart)
* [Matrix Data charts in table view](/docs/matrix-data-chart#Configuring-a-Matrix-Data-Table)

**To export chart data to CSV:**

1. Find the chart whose data you want to export.
2. From the 3-dot more menu, click Export to CSV.
3. The data is downloaded to your local device.

## Capture Chart

Use **Capture Chart** to download a .png image of any chart to your device. You can then share the image or include it in a presentation.

## Delete

Use **Delete** to delete a chart and remove it from the current Dashboard. Only custom charts can be deleted.
Any background calculations for this chart should stop running within 24 hours after you delete the chart.

## Sort

Use **Sort** to determine the default sort of data for bar charts. Sort is available for the [Field Segmentation](/docs/field-segmentation-chart) and [Query Comparison](/docs/query-comparison-chart) bar charts.

* The available sort options are:
  * Sort by Value (Descending/Ascending) - Sorts by the segment size.
  * Sort by Name (Descending/Ascending): Sorts by the segment title.
* You can also use the chart menu to change the default sort.

<Image alt="ChartSorting" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartSorting.png" />

## Refresh

Use **Refresh** to refresh the chart data. Refresh reruns the queries configured in the chart.

## Pin

Click **Pin** to pin a chart to the dashboard. Once a chart is pinned it cannot be moved or resized. This can ensure a consistent order when making other changes in the Dashboard or for fixing important KPIs at the top of the dashboard.

You can unpin a chart by clicking **Unpin** from the Actions menu.

## Copy Link

Click **Copy Link** to copy a link to the dashboard to your clipboard. This allows you to share the dashboard with other users.

<Callout icon="📘" theme="info">
  Note

  Users who access the dashboard with this link will only see data according to the access granted by their assigned role permissions.
</Callout>

## Display Historical Data

Axonius saves daily “snapshots” of all collected data. You can use this historical data to view any query on the **Devices** page, on the **Users** page, or to access Dashboard insights relevant to a specific day in history.

To view Dashboard chart results for a specific date, click the **Chart Filters** button and then click the **Select historical date** field.

A date picker control opens, enabling you to select the desired date. By default, the latest date for which data was collected is displayed.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1356).png" />

Notice that only dates with collected data are available.
To clear the historical view and set back to the latest date, click **Clear Filters**.

## View Results

Click a bar, pie slice, matrix field, or other data point on a dashboard chart to view the list of assets it represents.
The following options are available when clicking on a chart segment or link:

* **Standard Click**: Opens in a new tab and switches focus.
* **CTRL+Click**: Opens in a new tab, focus stays on the dashboard.
* **SHIFT+Click**: Opens in a new window.

The Asset page that opens also shows the corresponding query in the Query Wizard. When the dashboard uses a Saved Query, the query wizard expression will show the query name, and the AQL will show the query ID.

## Reorder

Hover over the icon on the top of the chart, and use drag-and-drop to reorder the charts in the Dashboard.

## Pie Chart Legend

[Resize](/docs/chart-actions#resizing-dashboard-charts) a chart to display pie chart legend.

* The legend contains data labels for each of the pie chart slices.
* Each data label displays the slice label, number or results and the percentage of the slice size out of the total.
* Data labels are clickable. Clicking a data label will redirect you to the **Devices** or to the **Users** page displaying the corresponding list of assets.

<Image alt="OSType" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OSType.png" />

## Viewing Chart Slice or Section Data

You can hover over parts of the chart to display a tooltip containing more details about the chart's values.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tooltip.png)