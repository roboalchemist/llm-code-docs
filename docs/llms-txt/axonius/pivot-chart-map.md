# Source: https://docs.axonius.com/docs/pivot-chart-map.md

# Using the Pivot Chart Map Visualization

The Map chart is a visualization of the Pivot chart that displays data on a geographical map. This feature works with the “Activities” module and supports location fields for specific adapters: [Okta](https://docs.axonius.com/axonius-help-docs/docs/okta), [Microsoft Azure](https://docs.axonius.com/axonius-help-docs/docs/microsoft-azure-1), and [Microsoft Active Directory (AD)](https://docs.axonius.com/axonius-help-docs/docs/microsoft-active-directory-ad).

<Image align="center" alt="MapChartConfig.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/MapChartConfig.png" />

**To configure a map chart:**

1. On any editable dashboard, click **Add Chart** or edit an existing chart.
2. In the **Name** field, enter a descriptive name for the chart.
3. From the **Widget** list, select **Pivot Chart**.
4. Under **Visualization**, select **Map**.
5. Under **Data**, select the Activities module and the query that will define which assets to include.
6. Under **Dimensions**, select the field whose values will be on the axis of the chart.
7. Under **Metrics**, select the field whose value is measured per the axis.
8. Under **Calculation**, select whether to use [historical data](https://docs.axonius.com/axonius-help-docs/docs/historical-query-results) and whether to [include entities with no value](https://docs.axonius.com/axonius-help-docs/docs/including-entities-with-no-value).
9. Under **Presentation**, you can set [threshold colors](https://docs.axonius.com/axonius-help-docs/docs/asset-cnt-thshld-color) and whether to show the chart title on the chart.
10. Click **Save**.

When you hover over a location with data, the data is displayed in a popup.

<Image alt="MapChartHover.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/MapChartHover.png" />

<br />

<br />