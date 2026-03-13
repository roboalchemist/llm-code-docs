# Source: https://bryntum.com/products/gantt/docs-llm/api/Chart/widget/Chart.md

# [Chart](https://bryntum.com/docs/gantt/api/Chart/widget/Chart)

Displays a chart generated from data. Charts are rendered using the third-party [Chart.js library](https://bryntum.com/docs/gantt/api/https://github.com/chartjs/Chart.js) ([MIT license](https://bryntum.com/docs/gantt/api/https://github.com/chartjs/Chart.js/blob/master/LICENSE.md)).

### Chart types

The following chart types are supported:

* `line`
* `bar` (vertical and horizontal)
* `pie`
* `donut` (nested pie chart)
* `scatter` (X/Y chart)
* `bubble` (scatter chart with varying bubble sizes)
* `radar`

### Configuring data

The chart requires [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) and one or more data [series](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-series) to be defined in order to display data. Series are specified as [DataSeries](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#typedef-DataSeries) objects. In a line chart, each line is one series. Each series normally gets its own color in the chart, except in the case of pie and donut charts, where each series is one full ring, and the colors are assigned to slices (data points) instead.

Data is provided to the chart using the [data](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-data) config. This should be an array of data [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model)s or objects. Data points are drawn from individual fields in the records according to how the `series` of the chart are configured. For example, one line (series) in a line chart might show data values from the records' field `FY2023`, and a second line might show values from the field `FY2024`. In that case there would be two series defined on the chart, each with its `field` property set to `"FY2023"` or `"FY2024"` accordingly.

For chart types that combine multiple data values into a single series, like `scatter` or `bubble`, each series must also specify its `role` and `seriesIndex`. See [DataSeries](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#typedef-DataSeries).

For charts with an X-axis (such as line and bar charts), the [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) configuration specifies the data series to use as the ticks on the X-axis. For pie and donut charts, [labels](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-labels) defines the slice labels.

The [data](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-data) config is also required; these are the records that supply the actual data values used in the chart.

### Customizing appearance

Various configuration options allow you to change the look and feel of the chart. Chart elements can be turned on and off using [showTitle](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showTitle), [showSubtitle](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showSubtitle), [showLegend](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showLegend), [showAxes](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showAxes), and [showControls](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showControls). Spacing can be adjusted with [chartPadding](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-chartPadding), [titlePadding](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-titlePadding), and [subtitlePadding](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-subtitlePadding). Fonts can be set with [titleFont](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-titleFont) and [subtitleFont](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-subtitleFont). Data series line [thickness](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-seriesLineThickness), [dash](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-seriesLineDash), and [opacity](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-seriesLineOpacity) can also be configured.

Try using the controls in the demo below to fine-tune the Chart appearance. To enable similar chart customization UI in your app, see the [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner) widget.

### Interactivity

By default, the chart can be downloaded as an image file using a button at the top right of the chart. To hide the download button, set [showControls](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showControls) to `false`.

Tooltips appear as you mouse over data points on the chart. They can be disabled using [showTooltips](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-showTooltips).

### Animation

Animation is enabled by default. To disable animation, set [animate](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-animate) to `false`.

See also: [ChartDesigner](https://bryntum.com/docs/gantt/api/#Chart/widget/ChartDesigner).

## Fields

Fields belong to a Model class and define the Model data structure

[field](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#field-field)
The name of the record field containing the data for this series.

[label](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#field-label)
The name of the series to display in the legend.

[role](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#field-role)
(Optional) Required when using certain chart types, for example `scatter`, where series can be arbitrarily assigned to different axes. The `role` determines how this series is used in the chart.

[backgroundColorField](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#field-backgroundColorField)
(Optional) The name of a field in the chart data to use as the background color for each data point.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[chartType](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-chartType)
Basic type of chart.

[labels](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-labels)
For line and bar charts, this series defines the data values to use as ticks for the x-axis. For pie and donut chart, it defines the data values to use as slice labels.

[series](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-series)
One or more data series to display in the chart.

[showAxes](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-showAxes)
Whether to show all chart axes (`true`), hide all axes (`false`), or an array indicating which axes to show. If array, valid elements are `'x'` and `'y'`.

[title](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-title)
The chart title.

[subtitle](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-subtitle)
The chart subtitle.

[animate](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-animate)
Whether to animate chart data changes.

[animationDuration](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-animationDuration)
Set the duration in milliseconds for all animations.

[showTooltips](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-showTooltips)
Whether to show tooltips when the mouse cursor hovers over chart elements.

[chartTooltip](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-chartTooltip)
Chart tooltip configuration object. Configures the tooltip that appears when hovering over chart data points. This follows the Chartjs tooltip configuration specification. This will only be applied if [showTooltips](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#property-showTooltips) is `true`.

[showPoints](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-showPoints)
Whether to show data point markers on the chart.

[barDirection](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-barDirection)
Layout direction for the bar chart type.

[interactive](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-interactive)
Whether to do dynamic highlighting and other interactivity as the mouse cursor moves over the chart.

[showTicks](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-showTicks)
Whether to show tick marks and labels on the chart axes.

[pointSize](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-pointSize)
Radius of data points, in pixels.

[bubbleScaleFactor](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-bubbleScaleFactor)
Scale factor to apply to the computed size of bubbles in the bubble chart type.

[showControls](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-showControls)
Whether to show the chart's control button menu, for example, the download button.

[data](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-data)
The data records or objects containing data to display in the chart.

[max](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-max)
Max value for the Y axis, for chart types that have one.

[min](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-min)
Min value for the Y axis, for chart types that have one.

[legendPosition](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-legendPosition)
Where the chart's legend should appear relative to the main chart content. Options `inline-start` and `inline-end` function as in CSS, with horizontal positioning controlled by RTL mode.

[legendScale](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-legendScale)
Optional scale factor to increase or decrease the size of the chart legend.

[tickMarkColor](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-tickMarkColor)
Set the color of the tick mark lines in the axis area, or `null` to default to [axisColor](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-axisColor).

[tickFont](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#config-tickFont)
The font to use for tick labels on the chart axes.

Default:

```
{
   size      : 14,
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChart](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-isChart)
Identifies an object as an instance of [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) class, or subclass thereof.

[isChart](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-isChart-static)
Identifies an object as an instance of [Chart](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart) class, or subclass thereof.

[chartType](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-chartType)
Basic type of chart.

[labels](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-labels)
For line and bar charts, this series defines the data values to use as ticks for the x-axis. For pie and donut chart, it defines the data values to use as slice labels.

[series](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-series)
One or more data series to display in the chart.

[showAxes](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-showAxes)
Whether to show all chart axes (`true`), hide all axes (`false`), or an array indicating which axes to show. If array, valid elements are `'x'` and `'y'`.

[title](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-title)
The chart title.

[subtitle](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-subtitle)
The chart subtitle.

[animate](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-animate)
Whether to animate chart data changes.

[animationDuration](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-animationDuration)
Set the duration in milliseconds for all animations.

[showTooltips](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-showTooltips)
Whether to show tooltips when the mouse cursor hovers over chart elements.

[chartTooltip](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-chartTooltip)
Chart tooltip configuration object. Configures the tooltip that appears when hovering over chart data points. This follows the Chartjs tooltip configuration specification. This will only be applied if [showTooltips](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#property-showTooltips) is `true`.

[showPoints](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-showPoints)
Whether to show data point markers on the chart.

[barDirection](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-barDirection)
Layout direction for the bar chart type.

[interactive](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-interactive)
Whether to do dynamic highlighting and other interactivity as the mouse cursor moves over the chart.

[showTicks](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-showTicks)
Whether to show tick marks and labels on the chart axes.

[pointSize](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-pointSize)
Radius of data points, in pixels.

[bubbleScaleFactor](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-bubbleScaleFactor)
Scale factor to apply to the computed size of bubbles in the bubble chart type.

[showControls](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-showControls)
Whether to show the chart's control button menu, for example, the download button.

[data](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-data)
The data records or objects containing data to display in the chart.

[max](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-max)
Max value for the Y axis, for chart types that have one.

[min](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-min)
Min value for the Y axis, for chart types that have one.

[legendPosition](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-legendPosition)
Where the chart's legend should appear relative to the main chart content. Options `inline-start` and `inline-end` function as in CSS, with horizontal positioning controlled by RTL mode.

[legendScale](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-legendScale)
Optional scale factor to increase or decrease the size of the chart legend.

[tickMarkColor](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-tickMarkColor)
Set the color of the tick mark lines in the axis area, or `null` to default to [axisColor](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-axisColor).

[tickFont](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#property-tickFont)
The font to use for tick labels on the chart axes.

Default:

```
{
   size      : 14,
}
```

## Functions

Functions are methods available for calling on the class

[applyFont](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#function-applyFont)
Apply a Font to the ChartJS options for a specific element.

[setData](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#function-setData)
Set data for the chart, an alternative to setting the [data](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#config-data) config for when you want control over if the chart animates the change or not.

Note that a chart configured with `animate: false` will never animate, even if you call this method with `skipAnimation` set to `false`.

[download](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#function-download)
Download the chart as a PNG image with the given filename (if any).

## Typedefs

Typedefs are type definitions for the class

[Font](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#typedef-Font)
A font configuration for display.

[DataSeries](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#typedef-DataSeries)
Defines a data series for use in a chart.

[DataSeriesRole](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#typedef-DataSeriesRole)
An object that defines the role a given [DataSeries](https://bryntum.com/docs/gantt/api/#Chart/widget/Chart#typedef-DataSeries) plays in defining data series, when the chart type allows series to be assigned to different axes.

[ChartTooltipCallbacks](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#typedef-ChartTooltipCallbacks)
Chart tooltip callback functions configuration object. Refer to the ChartJS tooltip [callbacks](https://bryntum.com/docs/gantt/api/https://www.chartjs.org/docs/latest/configuration/tooltip.html#tooltip-callbacks) documentation for details.

[ChartTooltipConfig](https://bryntum.com/docs/gantt/api/Chart/widget/Chart#typedef-ChartTooltipConfig)
Chart tooltip configuration object that defines the appearance and behavior of chart tooltip. See the [ChartJS documentation](https://bryntum.com/docs/gantt/api/https://www.chartjs.org/docs/latest/configuration/tooltip.html) for more information.
