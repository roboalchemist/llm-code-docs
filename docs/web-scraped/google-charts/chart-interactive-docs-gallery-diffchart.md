# Source: https://developers.google.com/chart/interactive/docs/gallery/diffchart

Title: Diff Charts

URL Source: https://developers.google.com/chart/interactive/docs/gallery/diffchart

Markdown Content:

* Diff charts highlight the differences between two charts with comparable data to reveal variations between datasets.

* You create a diff chart by calling the `computeDiff` method with two datasets.

* Diff charts are available for bar charts, column charts, pie charts, and scatter charts.

* Examples are provided for Diff Scatter Charts, Diff Pie Charts, and Diff Bar and Column Charts.

* [Overview](https://developers.google.com/chart/interactive/docs/gallery/diffchart#Overview)
* [Examples](https://developers.google.com/chart/interactive/docs/gallery/diffchart#Examples)
  * [Diff Scatter Charts](https://developers.google.com/chart/interactive/docs/gallery/diffchart#diffscatter)
  * [Diff Pie Charts](https://developers.google.com/chart/interactive/docs/gallery/diffchart#diffpie)
  * [Diff Bar and Column Charts](https://developers.google.com/chart/interactive/docs/gallery/diffchart#diffbar)

[](https://developers.google.com/chart/interactive/docs/gallery/diffchart)Overview
----------------------------------------------------------------------------------

A _diff chart_ is a chart designed to highlight the differences between two charts with comparable data. By making the changes between analogous values prominent, they can reveal variations between datasets.

You create a diff chart by calling the `computeDiff` method with two datasets to generate a third dataset representing the diff, and then drawing that.

Diff charts are available for [bar charts](https://developers.google.com/chart/interactive/docs/gallery/barchart), [column charts](https://developers.google.com/chart/interactive/docs/gallery/columnchart), [pie charts](https://developers.google.com/chart/interactive/docs/gallery/piechart), and [scatter charts](https://developers.google.com/chart/interactive/docs/gallery/scatterchart).

[](https://developers.google.com/chart/interactive/docs/gallery/diffchart)Examples
----------------------------------------------------------------------------------

In this section you'll see examples and code samples for each diff chart type.

### [](https://developers.google.com/chart/interactive/docs/gallery/diffchart)Diff Scatter Charts

To demonstrate the diff scatter chart, let's consider a pair of experiments, each comparing two medicines. Here are the results from the two experiments, and the resulting diff chart:

If you eyeball those two charts, you can tell something has changed, but it's hard to tell exactly what. The diff scatter chart makes it clear by showing the trajectory of each data point.

Here are the key lines generating the three charts above:

// Create the three charts: before, after, and diff.
var chartBefore = new google.visualization.ScatterChart(document.getElementById('chart_before_div'));
var chartAfter = new google.visualization.ScatterChart(document.getElementById('chart_after_div'));
var chartDiff = new google.visualization.ScatterChart(document.getElementById('chart_diff_div'));

// Draw the before and after charts.
chartBefore.draw(oldData);
chartAfter.draw(newData);

// Draw the diff chart.
**var diffData = chartDiff.computeDiff(oldData, newData); chartDiff.draw(diffData);**

You can change the opacity of the tails with the `diff.oldData.opacity` option, and the opacity of the new data points with the `diff.newData.opacity` option:

### [](https://developers.google.com/chart/interactive/docs/gallery/diffchart)Diff Pie Charts

Here's the code to generate all three charts:

  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load('current', {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var oldData = google.visualization.arrayToDataTable([
      ['Major', 'Degrees'],
      ['Business', 256070], ['Education', 108034],
      ['Social Sciences & History', 127101], ['Health', 81863],
      ['Psychology', 74194]]);

    var newData = google.visualization.arrayToDataTable([
      ['Major', 'Degrees'],
      ['Business', 358293], ['Education', 101265],
      ['Social Sciences & History', 172780], ['Health', 129634],
      ['Psychology', 97216]]);

    var options = { pieSliceText: 'none' };

    var chartBefore = new google.visualization.PieChart(document.getElementById('piechart_before'));
    var chartAfter = new google.visualization.PieChart(document.getElementById('piechart_after'));
    var chartDiff = new google.visualization.PieChart(document.getElementById('piechart_diff'));

    chartBefore.draw(oldData, options);
    chartAfter.draw(newData, options);

    **var diffData = chartDiff.computeDiff(oldData, newData); chartDiff.draw(diffData, options);**
  }
</script>
<span id='piechart_before' style='width: 450px; display: inline-block'></span>
<span id='piechart_after' style='width: 450px; display: inline-block'></span>
<br>
<span id='piechart_diff' style='width: 450px; position: absolute; left: 250px'></span>

You can control the relative size of the circles with `diff.innerCircle.radiusFactor`, the border between the two with `diff.innerCircle.borderFactor`, and the transparency of each with `diff.oldData.opacity` and `diff.newData.opacity`. Finally, you can invert the behavior so that the oldest data surrounds the newest data with `diff.oldData.inCenter`. An example of each:

### [](https://developers.google.com/chart/interactive/docs/gallery/diffchart)Diff Bar and Column Charts

The diff bar and diff column charts overlay newer data on top of older data. Here, we take two simple column charts—one of old data, one of new—and diff them:

For a more complicated example, let's look at how the popularity of some names (in particular, the names of Google Visualization summer interns) has changed from the 1980s to the present (numbers are per millions of babies, courtesy of the [Baby Name Wizard](http://www.babynamewizard.com/)).

The code to generate all four charts:

  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load('current', {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var oldData = google.visualization.arrayToDataTable([
      ['Name', 'Popularity'],
      ['Cesar', 250],
      ['Rachel', 4200],
      ['Patrick', 2900],
      ['Eric', 8200]
    ]);

    var newData = google.visualization.arrayToDataTable([
      ['Name', 'Popularity'],
      ['Cesar', 370],
      ['Rachel', 600],
      ['Patrick', 700],
      ['Eric', 1500]
    ]);

    var colChartBefore = new google.visualization.ColumnChart(document.getElementById('colchart_before'));
    var colChartAfter = new google.visualization.ColumnChart(document.getElementById('colchart_after'));
    var colChartDiff = new google.visualization.ColumnChart(document.getElementById('colchart_diff'));
    var barChartDiff = new google.visualization.BarChart(document.getElementById('barchart_diff'));

    var options = { legend: { position: 'top' } };

    colChartBefore.draw(oldData, options);
    colChartAfter.draw(newData, options);

    **var diffData = colChartDiff.computeDiff(oldData, newData); colChartDiff.draw(diffData, options); barChartDiff.draw(diffData, options);**
  }
</script>

<span id='colchart_before' style='width: 450px; height: 250px; display: inline-block'></span>
<span id='colchart_after' style='width: 450px; height: 250px; display: inline-block'></span>
<span id='colchart_diff' style='width: 450px; height: 250px; display: inline-block'></span>
<span id='barchart_diff' style='width: 450px; height: 250px; display: inline-block'></span>

The diff column and bar charts let you control the relative width of the old and new bars with the `diff.newData.widthFactor` option:
