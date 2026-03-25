# Source: https://docs.axonius.com/docs/asset-cnt-thshld-color.md

# Setting Threshold Colors

This feature is available for the following chart types:

* [Query Intersection](/docs/query-intersection-chart)
* [Query Comparison](/docs/query-comparison-chart)
* [Field Segmentation](/docs/field-segmentation-chart)
* [Field Summary](/docs/field-summary-chart)
* [Matrix Data Chart](/docs/matrix-data-chart)
* [Pivot Chart](/docs/adv-pivot-chart)

## Setting Threshold Colors

You can configure visual color-codes to charts to easily identify the status of assets by setting asset count threshold colors. **Set threshold colors** allows you to set a color to indicate when the asset count exceeds a set threshold. Multiple threshold colors can be set to indicate different levels.

<Callout icon="📘" theme="info">
  Note

  When threshold colors are set, the colors for individual chart segments are disabled.
</Callout>

For example, you can set thresholds for asset counts of 10, 25, and 50. When each threshold is met or exceeded, the appropriate color is applied to the chart. Asset counts are set as fixed numbers for most chart types.

![SetAssetCountThresholdColors.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetAssetCountThresholdColors.png)

The chart is updated with the configured threshold and color selections.

![SetAssetCountThresholdColors-Chart.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetAssetCountThresholdColors-Chart.png)

For pie charts, thresholds are expressed as a percentage. When the returned asset count meets or exceeds a set threshold, the configured color is applied to the chart.

![SetAssetCountThresholdColors-Percentage.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetAssetCountThresholdColors-Percentage.png)

The chart is updated with the configured threshold and color selections.

![SetAssetCountThresholdColors-Pie.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetAssetCountThresholdColors-Pie.png)

**To set threshold colors:**

<Callout icon="📘" theme="info">
  NOTE

  The first threshold always has a **From** value of 0 (zero).
</Callout>

1. Toggle on **Set threshold colors**.
2. Do one of the following:
   * For all chart types, except for pie charts, enter a **To** value. If there is another threshold, the **From** value is automatically set to be one more than the **To** value in the previous threshold level. Then, in the color palette select a threshold color.
   * For pie charts, enter a percentage value in the **To** field. If there is another threshold, the **From** value is automatically set to be one more than the **To** value in the previous threshold level.  Then, in the color palette select a threshold color.

<Callout icon="📘" theme="info">
  NOTE

  The sum of all thresholds is limited to 100%.
</Callout>

3. To add a threshold level, click `+`  and enter the appropriate values.