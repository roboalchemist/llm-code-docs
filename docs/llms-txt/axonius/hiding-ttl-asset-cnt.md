# Source: https://docs.axonius.com/docs/hiding-ttl-asset-cnt.md

# Hiding the Total Asset Count

This feature is available on the following chart types:

* Field Segmentation - Bars
* Comparison - Bars
* Matrix - Bars

<Callout icon="📘" theme="info">
  NOTE

  The **Hide Total calculation** option is selected by default.
</Callout>

Some chart types can display data from more than one query. When comparing the same assets, some may be counted more than once, which is reflected in the total numbers. In such cases, you can choose to hide the total asset count to reduce this complexity.

For example, a chart may include data from several queries reporting the same results from an adapter but over different time periods (i.e. last 7 days, last 30 days). If 100 assets were returned in the last 30 days and 25 assets were returned in the last 7 days, the total would show as 125. At least 25 assets would be counted twice. You can hide the total asset count by using the **Hide Total calculation** option.

For Field Segmentation and Comparison charts:

* When hovering on a bar the percentage is NOT displayed.
* If the change calculation is included, the total change is NOT presented.

<Callout icon="📘" theme="info">
  NOTES

  * When the total asset count is hidden in the chart, it is not included in any reports that include that chart.

  * When comparing current results to a historical date, the selected historical date is displayed below the chart.
</Callout>

**To hide the total asset count**

1. Enter **Edit** mode of a supported chart type.
2. Scroll down and click **Hide Total calculation**.

![HideTotalAssetCount.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideTotalAssetCount.png)