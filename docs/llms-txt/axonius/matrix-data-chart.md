# Source: https://docs.axonius.com/docs/matrix-data-chart.md

# Matrix Data Chart

The **Matrix Data** chart lets you visualize in a stacked bar chart a data matrix that consists of multiple data intersections between one or multiple base queries and up to three intersecting queries.

<Image alt="MatrixData" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MatrixData.png" />

To configure a **Matrix Data** chart:

1. In the **Chart title** text box, enter a title for the chart.
2. In the **Description** text box, you can add an optional description.
3. From the **Widget** dropdown, select **Matrix Data Chart**.
4. Under **Chart presentation**, select the chart presentation style you want.
5. Configure the chart according to the presentation style as described in the procedures below.

## Configuring a Matrix Data Stacked Bar Chart

You can present the data as a stacked bar chart:

1. Select the stacked bar chart.
2. From the **Module** dropdown, select an asset module.
3. From **Base query**, select or create a base query or leave empty for all entities. Learn [more](/docs/chart-query-configuration) about creating a query.
   * You may add multiple base queries.
4. From **Intersecting query**, select a saved query or create a new one
   * You can add up to three intersecting queries.
5. Select **Hide Total calculation** to prevent totals from being displayed. See [Hiding the Total Asset Count](/docs/hiding-ttl-asset-cnt).
6. Under **Segment by**, select how to display the data:
   1. Select **Percentage** and **Show Percentage** to see a percentage/normalized chart. See [Configuring the Stacked Bar Chart in a Percentage/Normalized Mode](https://docs.axonius.com/axonius-help-docs/docs/configuring-the-100-stacked-bar-visualization).
   2. Select **Number** and **Show Number** to see an absolute chart showing the actual asset counts.
7. Click **Save**.

Each bar in the stacked bar chart visualizes the intersections between a specific base query and each of the specified intersecting queries.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1268).png" />

An example of the percentage/normalized chart:

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/100PerStackedBarPivotChartExample.png" />

## Configuring a Matrix Data Table

You can present the Matrix data as a table. This shows the common values between two queries, for instance Operating System and Devices.

**To configure a Matrix Data Table chart:**

1. Select the table presentation.

<Image alt="MatrixTable(2)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MatrixTable(2).png" />

2. From the **Module** dropdown, select an asset module.
3. The **Base query** defines the rows of the table. From the **Base query** list, select a saved query or create a new query or leave empty for all entities. From the Field drop down select a field. You can choose an aggregated field, or a field from a specific adapter.
4. The **Intersecting query** defines the columns of the table. Select a saved query or create a new one from the **Intersecting query** or leave empty for all entities. From the Field drop down select a field. You can choose an aggregated field, or a field from a specific adapter.
   Learn [more](/docs/chart-query-configuration) about creating a query.
5. Select **Add rows total** to show the total number of unique devices or users for each row.
6. Select **Add columns total** to show the total number of unique devices or users for each column.
7. Select **Show results with no intersecting values** to show results on the table where there are no values in common between the base query and the intersecting query.
8. Click **Save**.

The top 1000 columns are displayed. The table shows the intersection between all assets which have a value in both of the fields.

<Image align="center" alt="TableMAtrixREs.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TableMAtrixREs.png" />

You can export the table to a CSV file.

Click on an asset bar or table cell to view the Asset summary for the displayed assets. Click the **Asset Page** to view the assets on their relevant Asset page with the query populated in the Query Wizard.

You can change between the chart presentation styles. When moving from stacked bar chart to Matrix data table, only the first query is used.