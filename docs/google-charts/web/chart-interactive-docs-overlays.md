# Source: https://developers.google.com/chart/interactive/docs/overlays

Title: Overlays

URL Source: https://developers.google.com/chart/interactive/docs/overlays

Markdown Content:

* Overlays are areas placed on top of a Google Chart, typically used to highlight statistics.

* Simple overlays can be created using HTML and CSS without JavaScript.

* More advanced overlays can be positioned and customized using Google Charts JavaScript to react to data.

* Positioning overlays relative to data ensures they remain correctly placed even if the chart data changes, often achieved by listening for the chart's `ready` event.

1. [Overview](https://developers.google.com/chart/interactive/docs/overlays#overview)
2. [A Simple Example](https://developers.google.com/chart/interactive/docs/overlays#simple)
3. [Positioning Overlays Relative to Data](https://developers.google.com/chart/interactive/docs/overlays#positioning)

[](https://developers.google.com/chart/interactive/docs/overlays)Overview
-------------------------------------------------------------------------

An _overlay_ is an area laid on top of a Google Chart. It's typically used to call out a particular statistic, but can be anything you want since it's just HTML and CSS.

Simple uses involve creating a CSS class and simply referring to it in your HTML; no JavaScript required. More advanced uses can involve using Google Charts to customize the positioning and content of the overlay.

[](https://developers.google.com/chart/interactive/docs/overlays)A Simple Example
---------------------------------------------------------------------------------

For our first example, we'll avoid JavaScript entirely and simply overlay some text on a line chart:

Here, an internal stylesheet defines two classes that we call `chartWithOverlay` and `overlay`. Note that we use relative positioning in `chartWithOverlay` and absolute positioning in `overlay`.

Then, in the body of our web page, we use a `chartWithOverlay` as a container into which we place our chart (`line-chart`) and then our `overlay`.

**.chartWithOverlay {**
 **position: relative;**
 width: 700px;
**}**
**.overlay {**
 width: 200px;
 height: 200px;
 **position: absolute;**
 top: 60px; /*chartArea top _/
 left: 180px; /_ chartArea left*/
**}**<div class="chartWithOverlay">

 <div id="line-chart" style="width: 700px; height: 500px;"></div>

 <div class="overlay">
   <div style="font-family:'Arial Black'; font-size: 128px;">88</div>
   <div style="color: #b44; font-family:'Arial Black'; font-size: 32px; letter-spacing: .21em; margin-top:50px; margin-left:5px;">zombie</div>
   <div style="color: #444; font-family:'Arial Black'; font-size: 32px; letter-spacing: .15em; margin-top:15px; margin-left:5px;">attacks</div>
 </div>

</div> <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
 <script type="text/javascript">
 google.charts.load("current", {packages:['corechart']});
 google.charts.setOnLoadCallback(drawChart);
 function drawChart() {
 var data = new google.visualization.arrayToDataTable([
 ['Threat', 'Attacks'],
 ['Chandrian', 38],
 ['Ghosts', 12],
 ['Ghouls', 6],
 ['UFOs', 44],
 ['Vampires', 28],
 ['Zombies', 88]
 ]);

 var options = {
 legend: 'none',
 colors: ['#760946'],
 vAxis: { gridlines: { count: 4 } }
 };

 var chart = new google.visualization.LineChart(document.getElementById('line-chart'));
 chart.draw(data, options);
 }
 </script><html>
 <head>
   <style>
    **.chartWithOverlay { position: relative; width: 700px; }**
    **.overlay { width: 200px; height: 200px; position: absolute; top: 60px; /* chartArea top */ left: 180px; /* chartArea left */ }**
   </style>
   <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

   <script type="text/javascript">
    google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = new google.visualization.arrayToDataTable([
        ['Threat', 'Attacks'],
        ['Chandrian', 38],
        ['Ghosts', 12],
        ['Ghouls', 6],
        ['UFOs', 44],
        ['Vampires', 28],
        ['Zombies', 88]
      ]);

      var options = {
        legend: 'none',
        colors: ['#760946'],
        vAxis: { gridlines: { count: 4 } }
      };

      var chart = new google.visualization.LineChart(document.getElementById('line-chart'));
      chart.draw(data, options);
    }
    </script>
 </head>

 <body>
  <div class="chartWithOverlay">

   <div id="line-chart" style="width: 700px; height: 500px;"></div>

   <div class="overlay">
    <div style="font-family:'Arial Black'; font-size: 128px;">88</div>
    <div style="color: #b44; font-family:'Arial Black'; font-size: 32px; letter-spacing: .21em; margin-top:50px; margin-left:5px;">zombie</div>
    <div style="color: #444; font-family:'Arial Black'; font-size: 32px; letter-spacing: .15em; margin-top:15px; margin-left:5px;">attacks</div>
  </div>

 </div>

</body>

</html>
[](https://developers.google.com/chart/interactive/docs/overlays)Positioning Overlays Relative to Data
------------------------------------------------------------------------------------------------------

Sometimes the best position for an overlay depends on where the data ends up on the chart. For instance, we might want to place an image close to a data element.

Let's say we wanted to draw attention to the number of zombie attacks in the chart above. We'll do this by placing a scary zombie head at the end of the line.

One way to do this would be to render the chart and hardcode our coordinates. That will work, but would require updating whenever the chart data changes. A more robust solution would have us placing the overlay relative to wherever the data element ends up onscreen. Since we can't know where that will be until the chart has finished rendering, we'll listen for the `ready` event (called when the chart is done rendering) and access the coordinates programmatically with `getXLocation` and `getYLocation`:

.chartWithMarkerOverlay {
 position: relative;
 width: 700px;
}
.overlay-text {
 width: 200px;
 height: 200px;
 position: absolute;
 top: 50px; /*chartArea top _/
 left: 200px; /_ chartArea left*/
}
*_.overlay-marker { width: 50 px; height: 50 px; position: absolute; top: 53 px; /_ chartArea top _/ left: 528 px; /_ chartArea left*/}**<div class="chartWithMarkerOverlay">

 <div id="line-chart-marker" style="width: 700px; height: 500px;"></div>

 <div class="overlay-text">
   <div style="font-family:'Arial Black'; font-size: 128px;">88</div>
   <div style="color: #b44; font-family:'Arial Black'; font-size: 32px; letter-spacing: .21em; margin-top:50px; margin-left:5px;">zombie</div>
   <div style="color: #444; font-family:'Arial Black'; font-size: 32px; letter-spacing: .15em; margin-top:15px; margin-left:5px;">attacks</div>
 </div>

**<div class="overlay-marker"> <img src="https://developers.google.com/chart/interactive/images/zombie_150.png" height="50"> </div>**

</div> <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
 <script type="text/javascript">
 google.charts.load("current", {packages:['corechart']});
 google.charts.setOnLoadCallback(drawChart);
 function drawChart() {
 var data = new google.visualization.arrayToDataTable([
 ['Threat', 'Attacks'],
 ['Chandrian', 38],
 ['Ghosts', 12],
 ['Ghouls', 6],
 ['UFOs', 44],
 ['Vampires', 28],
 ['Zombies', 88]
 ]);

 var options = {
 legend: 'none',
 colors: ['#760946'],
 lineWidth: 4,
 vAxis: { gridlines: { count: 4 } }
 };

 **function placeMarker(dataTable) { var cli = this.getChartLayoutInterface(); var chartArea = cli.getChartAreaBoundingBox(); // "Zombies" is element #5. document.querySelector('.overlay-marker').style.top = Math.floor(cli.getYLocation(dataTable.getValue(5, 1))) - 50 + "px"; document.querySelector('.overlay-marker').style.left = Math.floor(cli.getXLocation(5)) - 10 + "px"; };**

 var chart = new google.visualization.LineChart(document.getElementById('line-chart-marker'));
 google.visualization.events.addListener(chart, 'ready',
 placeMarker.bind(chart, data));
 chart.draw(data, options);
 }
 </script><html>
 <head>
  <style>
   .chartWithMarkerOverlay {
       position: relative;
       width: 700px;
   }
   .overlay-text {
       width: 200px;
       height: 200px;
       position: absolute;
       top: 50px;   /* chartArea top */
       left: 200px; /* chartArea left */
   }
**.overlay-marker { width: 50px; height: 50px; position: absolute; top: 53px; /* chartArea top */ left: 528px; /* chartArea left */ }**
  </style>

  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = new google.visualization.arrayToDataTable([
        ['Threat', 'Attacks'],
        ['Chandrian', 38],
        ['Ghosts', 12],
        ['Ghouls', 6],
        ['UFOs', 44],
        ['Vampires', 28],
        ['Zombies', 88]
      ]);

      var options = {
        legend: 'none',
        colors: ['#760946'],
        lineWidth: 4,
        vAxis: { gridlines: { count: 4 } }
      };

      **function placeMarker(dataTable) { var cli = this.getChartLayoutInterface(); var chartArea = cli.getChartAreaBoundingBox(); // "Zombies" is element #5. document.querySelector('.overlay-marker').style.top = Math.floor(cli.getYLocation(dataTable.getValue(5, 1))) - 50 + "px"; document.querySelector('.overlay-marker').style.left = Math.floor(cli.getXLocation(5)) - 10 + "px"; };**

      var chart = new google.visualization.LineChart(document.getElementById('line-chart-marker'));
      google.visualization.events.addListener(chart, 'ready',
        placeMarker.bind(chart, data));
      chart.draw(data, options);
    }
  </script>
 </head>
 <body>
  <div class="chartWithMarkerOverlay">

   <div id="line-chart-marker" style="width: 700px; height: 500px;"></div>

   <div class="overlay-text">
    <div style="font-family:'Arial Black'; font-size: 128px;">88</div>
    <div style="color: #b44; font-family:'Arial Black'; font-size: 32px; letter-spacing: .21em; margin-top:50px; margin-left:5px;">zombie</div>
    <div style="color: #444; font-family:'Arial Black'; font-size: 32px; letter-spacing: .15em; margin-top:15px; margin-left:5px;">attacks</div>
  </div>

  **<div class="overlay-marker"> <img src="https://developers.google.com/chart/interactive/images/zombie_150.png" height="50"> </div>**

  </div>
 </body>
</html>
