# Source: https://developers.google.com/chart/interactive/docs/customizing_axes

Title: Customizing Axes

URL Source: https://developers.google.com/chart/interactive/docs/customizing_axes

Markdown Content:

* Dimensions in data are often displayed on horizontal and vertical axes in various chart types.

* Charts with axes allow customization of properties like direction, label positioning and style, axis title text and style, and axis scale.

* An axis can be either discrete, with a finite number of evenly spaced values, or continuous, with an infinite number of possible values.

* The scale of an axis can be set to logarithmic (log) or mirror log scale using the `scaleType` option.

* Label numbers on axes can be formatted using the `hAxis.format` and `vAxis.format` options with various presets like decimal, scientific, currency, and more.

1. [Overview](https://developers.google.com/chart/interactive/docs/customizing_axes#Overview)
2. [Terminology](https://developers.google.com/chart/interactive/docs/customizing_axes#Terminology)
3. [Discrete vs. Continuous](https://developers.google.com/chart/interactive/docs/customizing_axes#Discrete_vs_Continuous)
4. [Axis Scale](https://developers.google.com/chart/interactive/docs/customizing_axes#Axis_Scale)
5. [Number Formats](https://developers.google.com/chart/interactive/docs/customizing_axes#Numbers)

[](https://developers.google.com/chart/interactive/docs/customizing_axes)Overview
---------------------------------------------------------------------------------

Dimensions in the data are often displayed on _axes_, horizontal and vertical. Such is the case for: [Area Chart](https://developers.google.com/chart/interactive/docs/gallery/areachart), [Bar Chart](https://developers.google.com/chart/interactive/docs/gallery/barchart), [Candlestick Chart](https://developers.google.com/chart/interactive/docs/gallery/candlestickchart), [Column Chart](https://developers.google.com/chart/interactive/docs/gallery/columnchart), [Combo Chart](https://developers.google.com/chart/interactive/docs/gallery/combochart), [Line Chart](https://developers.google.com/chart/interactive/docs/gallery/linechart), [Stepped Area Chart](https://developers.google.com/chart/interactive/docs/gallery/steppedareachart) and [Scatter Chart](https://developers.google.com/chart/interactive/docs/gallery/scatterchart).

When you create a chart with axes you can customize some of their properties:

* [Discrete vs. Continuous](https://developers.google.com/chart/interactive/docs/customizing_axes#Discrete_vs_Continuous)
* Direction - You can customize the direction using the hAxis/vAxis.direction option.
* Label positioning and style - You can customize label positioning and style using the hAxis/vAxis.textPosition and hAxis/vAxis.textStyle options.
* Axis title text and style - You can customize the axis title text and style using the hAxis/vAxis.title and hAxis/vAxis.titleTextStyle options.
* [Axis scale](https://developers.google.com/chart/interactive/docs/customizing_axes#Axis_Scale) - You can set the scale of an axis to logarithmic (log) scale using the hAxis/vAxis.logScale or hAxis/vAxis.scaleType options.
* For a complete list of axis configuration options, look at the hAxis and vAxis options in the documentation for your specific chart.

[](https://developers.google.com/chart/interactive/docs/customizing_axes)Terminology
------------------------------------------------------------------------------------

#### Major/minor axis

* The _major_ axis is the axis along the natural orientation of the chart. For line, area, column, combo, stepped area and candlestick charts, this is the horizontal axis. For a bar chart it is the vertical one. Scatter and pie charts don't have a major axis.
* The _minor_ axis is the other axis.

#### Discrete/continuous axis

* A _discrete_ axis has a finite number of evenly spaced values, called categories.
* A _continuous_ axis has an infinite number of possible values.

[](https://developers.google.com/chart/interactive/docs/customizing_axes)Discrete vs Continuous
-----------------------------------------------------------------------------------------------

The major axis of a chart can be either discrete or continuous. When using a discrete axis, the data points of each series are evenly spaced across the axis, according to their row index. When using a continuous axis, the data points are positioned according to their domain value.

The labeling is also different. In a discrete axis, the names of the categories (specified in the domain column of the data) are used as labels. In a continuous axis, the labels are auto-generated: the chart shows evenly spaced grid lines, where each grid line is labeled according to the value it represents.

The following axes are always continuous:

* Both axes of bubble charts.
* The minor axis.

In line, area, bar, column and candlestick charts (and combo charts containing only such series), you can control the type of the major axis:

* For a discrete axis, set the data column type to `string`.
* For a continuous axis, set the data column type to one of: `number`, `date`, `datetime` or `timeofday`.

| Discrete / Continuous | First column type | Example |
| --- | --- | --- |
| **Discrete** | string |  |
| **Continuous** | number |  |
| **Continuous** | date |  |

[](https://developers.google.com/chart/interactive/docs/customizing_axes)Axis Scale
-----------------------------------------------------------------------------------

You can set the scale of an axis using the `scaleType` option. For example, to set the scale of the vertical axis to log scale, use the following option:

  vAxis: {
        scaleType: 'log'
  }

The following line chart shows the growth of the world population in both linear (standard) scale and log scale.

If your data contains zero or negative values, you can plot the points using the `scaleType: 'mirrorLog'` option. In mirror log scale, the plotted value of a negative number is minus the log of the absolute value of the number. Values close to 0 are plotted on a linear scale.

The following example shows positive and negative Fibonacci numbers plotted in both mirror log scale and linear scale.

[](https://developers.google.com/chart/interactive/docs/customizing_axes)Number Formats
---------------------------------------------------------------------------------------

You can control the formatting of label numbers with `hAxis.format` and `vAxis.format`. For instance, `{hAxis: { format:'#,###%'} }` displays the values "1,000%", "750%", and "50%" for values 10, 7.5, and 0.5. You can also supply any of the following presets:

* `{format: 'none'}`: displays numbers with no formatting (e.g., 8000000)
* `{format: 'decimal'}`: displays numbers with thousands separators (e.g., 8,000,000)
* `{format: 'scientific'}`: displays numbers in scientific notation (e.g., 8e6)
* `{format: 'currency'}`: displays numbers in the local currency (e.g., $8,000,000.00)
* `{format: 'percent'}`: displays numbers as percentages (e.g., 800,000,000%)
* `{format: 'short'}`: displays abbreviated numbers (e.g., 8M)
* `{format: 'long'}`: displays numbers as full words (e.g., 8 million)

In the chart below, you can select among the presets:

A complete web page for the above chart follows.

<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {packages:['corechart']});
      google.charts.setOnLoadCallback(drawStuff);

        function drawStuff() {
          var data = new google.visualization.DataTable();
          data.addColumn('string', 'Country');
          data.addColumn('number', 'GDP');
          data.addRows([
            ['US', 16768100],
            ['China', 9181204],
            ['Japan', 4898532],
            ['Germany', 3730261],
            ['France', 2678455]
          ]);

         var options = {
           title: 'GDP of selected countries, in US $millions',
           width: 500,
           height: 300,
           legend: 'none',
           bar: {groupWidth: '95%'},
           vAxis: { gridlines: { count: 4 } }
         };

         var chart = new google.visualization.ColumnChart(document.getElementById('number_format_chart'));
         chart.draw(data, options);

         document.getElementById('format-select').onchange = function() {
           options['vAxis']['format'] = this.value;
           chart.draw(data, options);
         };
      };
    </script>
  </head>
  <body>
    <select id="format-select">
      <option value="">none</option>
      <option value="decimal" selected>decimal</option>
      <option value="scientific">scientific</option>
      <option value="percent">percent</option>
      <option value="currency">currency</option>
      <option value="short">short</option>
      <option value="long">long</option>
    </select>
    <div id="number_format_chart">
  </body>
</html>
When using a format that employs text (e.g., the `long` format, which will render 8,000,000 as "8 million", you can localize the strings into other languages by specifying a language code when you load the Google Charts library. For instance, to change "8 million" into the Russian "8 миллиона", call the library like so:

<script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'></script>
<script type='text/javascript'>
  google.charts.load('current', {'packages': ['corechart'], 'language': 'ru'});
  google.charts.setOnLoadCallback(drawMarkersMap);
</script>
