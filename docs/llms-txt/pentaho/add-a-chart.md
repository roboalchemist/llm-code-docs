# Source: https://docs.pentaho.com/pba-report-designer/add-a-chart.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/add-a-chart.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-a-chart.md

# Add a chart

A chart can be the most important graphical element in your report. Charts show the report data visually so that readers can more easily see how the numbers compare. There are two types of charts in Report Designer: Traditional JFreeChart elements, and sparkline charts.

For information on adding a chart, see the following sections:

* [Choose a chart type](#choose-a-chart-type)
* [Create a JFreeChart element](#create-a-jfreechart-element)
* [Create a sparkline chart](#create-a-sparkline-chart)
* [Sparkline attributes](#sparkline-attributes)

## Choose a chart type

There are 17 JFreeChart chart types built into Report Designer, with some of them changing significantly based on which data collector you choose.

If you want to show the strength of a trend for a single value over time, the best chart types are:

* Line
* Area
* XY StepArea
* XY Step
* XY Line

If you are directly comparing two or more related values, the best chart types to choose are:

* Pie
* Ring
* Bar
* Line
* Area
* Radar

If you want to show how one set of values directly affects another, the best chart types are:

* Bar line combination
* Waterfall

If you are comparing a large number of data points, the best chart types are:

* XY Difference
* XY Dot (Scatter plot)
* Bubble
* Pie Grid (Multi-Pie)

If you need to show a trend among a small number of related numerical data points, a sparkline chart may be appropriate.

## Create a JFreeChart element

Perform the following steps to add a traditional graph or a chart to your report:

1. Drag and drop a **Chart** element into a layout band.
2. Using the resize handles, change the size of the chart to fit your specifications.
3. Double-click the chart.

   An Edit Chart dialog box will appear with dozens of customizable options and settings.
4. Adjust the chart options to your preference, then click **OK**.
5. Click **Preview** to verify that your chart appears as intended.

You should now have a suitable chart that visually represents the selected data.

## Create a sparkline chart

Sparkline charts require comma-separated values (CSV) for input. If your data is not in CSV format, you must create a Pentaho Data Integration transformation to put commas between each data point, or you can manually insert commas between your data points.

Perform the following steps to add a sparkline chart to your report:

1. Drag and drop a **Sparkline Pie**, **Sparkline Bar**, or **Sparkline Line** element into a layout band.
2. Using the resize handles, change the size of the chart to fit your specifications.
3. Click the round green **+** icon in the **Value** row.

   A formula field will appear.
4. In the formula field, select the function that formats your sparkline data, or type in comma-separated values by hand directly, then click **Close**.
5. Click **Preview** to verify that your chart appears as intended.

## Sparkline attributes

The following attributes belong to the sparkline property:

| Attribute Name    | Purpose                                                           | Values                                                    |
| ----------------- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| spacing           | Specify the spacing (in pixels) between bars for a bar sparkline. | Integer; default is 0.                                    |
| start-angle       | Specify the start angle (in degrees) on a pie sparkline.          | Integer; values are from 1 to 360. Default is 1.          |
| counter-clockwise | Specify the plot direction on a pie sparkline.                    | Boolean; default is false, which represents clockwise.    |
| high-slice        | Specify the hexadecimal color for the high slice.                 | String; there is no default, you must define it manually. |
| medium-slice      | Specify the hexadecimal color for the medium slice.               | String; there is no default, you must define it manually. |
| low-slice         | Specify the hexadecimal color for the low slice.                  | String; there is no default, you must define it manually. |
