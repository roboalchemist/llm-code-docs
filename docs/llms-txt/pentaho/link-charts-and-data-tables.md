# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-charts-and-data-tables.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-charts-and-data-tables.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards/link-charts-and-data-tables.md

# Link charts and data tables

The instructions below explain how to create links to charts and data tables in a dashboard. Adjust the examples show in these instructions, as necessary, when working with your own data.

1. Create a simple dashboard that contains a chart and a data table.

   At this point, none of the content has been linked and you have a "static" dashboard.

   ![Simple dashboard](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-255a15b7b0cecfc81edaec517d3df237fc2bd7fe%2FPDD_simple_dashboard_sample.png?alt=media)

   In the pie chart in this example, you want the data table on the right to update with the values associated with a pie chart slice when your dashboard consumers click that slice (NA, APAC, Japan, and EMEA). For example, if a report consumer clicks the EMEA slice, the data table will display values associated with EMEA and nothing else. To get the correct filter display, you must first create a parameterized query that drives the content in the data table.
2. Click the **Edit** button to open up the **Edit** pane at the bottom of the screen.
3. Within the **Objects** pane, choose the report you want to parameterize.

   Parameterizing a query, as described here, allows you to pass values dynamically and update the chart based on events triggered by other elements of the dashboard such as a user choosing an item from a filter control or following links defined in content associated with another panel in the dashboard.
4. Click the **{p}** button next to the **Title** box.

   The parameters will populate after the title in the **Title** box.
5. Click the **Parameters** tab and ensure that the parameters name is linking to the correct source.
6. Click **Apply**.

   The new source for the parameter corresponds to the title of the dashboard panel that contains the chart as shown in the example above. This new source will now drive the display in the data table.
7. Click the **Edit** button (pencil icon) to exit the edit mode.

   The filters will appear after the panel titles.
8. Save your dashboard.

   See [Saving Your Dashboard](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/save-a-dashboard).

When users click a pie slice or bar in a chart, the data table displays content associated with that specific pie slice or bar. The currently applied filters appear after the title.
