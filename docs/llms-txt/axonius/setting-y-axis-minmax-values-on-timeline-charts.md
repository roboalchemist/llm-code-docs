# Source: https://docs.axonius.com/docs/setting-y-axis-minmax-values-on-timeline-charts.md

# Timeline Chart Features

Timeline charts display information as line charts on an x,y grid. By default y-axis minimum and maximum values are set automatically. You can also set them manually so that data from different queries that have different value ranges can be displayed properly on one chart.

<Callout icon="📘" theme="info">
  Note

  The manually set minimum and maximum values can be used as an approximation and may be adjusted to fit the data properly.
</Callout>

**To set y-axis minimum/maximum values**

1. Navigate to the dashboard you want and find the chart.

2. Click the **More** (three dots) menu in the upper-right corner of the chart and select **Edit**.

3. Scroll down to **Y-axis settings** and do the following:
   * To set a minimum value, toggle **Axis minimum** and enter a value in the text box.
   * To set a maximum value, toggle **Axis maximum** and enter a value in the text box.

<Callout icon="📘" theme="info">
  Note

  When the calculation method is **Percent**, the y-axis minimum is 0 (zero) and the y-axis maximum is 100.
</Callout>

Changes are applied immediately and appear in the left pane of the Edit window.

4. Click **Save**.

## Gradual Display of Timeline Data

Timeline charts display partial data during the calculation process, starting with the most recent data. Data is calculated in batches—each batch may include one or several days—and added to the chart incrementally as it's processed. This process occurs when creating a new chart, editing an existing chart, manually refreshing a chart or dashboard, or applying filters in the dashboard space. A visual indicator shows that data is still loading.
![image (16).png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image%20\(16\).png)