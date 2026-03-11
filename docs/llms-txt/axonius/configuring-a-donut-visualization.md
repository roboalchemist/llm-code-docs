# Source: https://docs.axonius.com/docs/configuring-a-donut-visualization.md

# Configuring a Donut Chart Visualization

The Donut visualization is available in the following charts:

* [Pivot Chart](https://docs.axonius.com/axonius-help-docs/docs/adv-pivot-chart)
* [Query Intersection Chart](https://docs.axonius.com/axonius-help-docs/docs/query-intersection-chart)
* [Query Comparison Chart](https://docs.axonius.com/axonius-help-docs/docs/query-comparison-chart)
* [Field Segmentation Chart](https://docs.axonius.com/axonius-help-docs/docs/field-segmentation-chart)

The Donut chart visualizes data in a donut shape and displays the total value in the center. A legend of segments is displayed, and you can select which segments to show. You can also set [threshold colors](https://docs.axonius.com/update/docs/asset-cnt-thshld-color) and a background color.

<Image align="center" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/Dashboards/DonutChart.png" />

**To configure a donut chart:**

1. On any editable dashboard, click **Add Chart** or edit an existing chart.
2. In the **Name** field, enter a descriptive name for the chart.
3. From the **Widget** list, select one of the chart types that support a donut visualization.
4. Under **Visualization**, select **Donut**.
5. Under **Data**
   1. Under **Module**, select an asset module and the query that will define which assets to include.
   2. Under **Schema**, select the schema to use, and whether to base the chart on historical data.
6. On a [Pivot Chart](https://docs.axonius.com/axonius-help-docs/docs/adv-pivot-chart), under **Dimensions**, select the fields that determine the category of assets represented by the chart.
7. On a [Pivot Chart](https://docs.axonius.com/axonius-help-docs/docs/adv-pivot-chart) under **Metrics**, select the field whose value is measured per the dimension.
8. Configure **Calculation**and **Presentation** settings.
9. Click **Save**. The chart is displayed on the current dashboard.