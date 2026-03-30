# Source: https://developers.google.com/chart/interactive/docs/gallery/toolbar

Title: Toolbar

URL Source: https://developers.google.com/chart/interactive/docs/gallery/toolbar

Markdown Content:

* A toolbar element can be added to visualizations to allow users to export data to CSV or HTML, or get code to embed the visualization.

* To use a toolbar, the visualization must get its data from a URL.

* The toolbar can offer various output types including CSV, HTML table, embeddable iframe code, or a link to add to iGoogle.

* You add a toolbar by calling the `google.visualization.drawToolbar()` method with a container element and an array of component objects.

* No data is sent to any server as all code and data are processed in the browser.

1. [Overview](https://developers.google.com/chart/interactive/docs/gallery/toolbar#Overview)
2. [Example](https://developers.google.com/chart/interactive/docs/gallery/toolbar#Example)
3. [Usage](https://developers.google.com/chart/interactive/docs/gallery/toolbar#usage)
    1.   [Output Types](https://developers.google.com/chart/interactive/docs/gallery/toolbar#outputtypes)
    2.   [Syntax](https://developers.google.com/chart/interactive/docs/gallery/toolbar#syntax)

4. [Data Policy](https://developers.google.com/chart/interactive/docs/gallery/toolbar#data_policy)

[](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Overview
--------------------------------------------------------------------------------

You can add a toolbar element to any visualization to enable the user to export the underlying data into a CSV file or an HTML table, or to provide code to embed the visualization into an arbitrary web page or gadget.

By: Google

[](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Example
-------------------------------------------------------------------------------

Select one of the options in the toolbar.

<html>
<head>
 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
 <script type="text/javascript">
 google.charts.load('current', {packages: ['corechart']});
 var visualization;

 function draw() {
 drawVisualization();
 drawToolbar();
 }

 function drawVisualization() {
 var container = document.getElementById('visualization_div');
 visualization = new google.visualization.PieChart(container);
 new google.visualization.Query('https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA').
 send(queryCallback);
 }

 function queryCallback(response) {
 visualization.draw(response.getDataTable(), {is3D: true});
 }

 function drawToolbar() {
 var components = [
 {type: 'igoogle', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA',
 gadget: 'https://www.google.com/ig/modules/pie-chart.xml',
 userprefs: {'3d': 1}},
 {type: 'html', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA'},
 {type: 'csv', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA'},
 {type: 'htmlcode', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA',
 gadget: 'https://www.google.com/ig/modules/pie-chart.xml',
 userprefs: {'3d': 1},
 style: 'width: 800px; height: 700px; border: 3px solid purple;'}
 ];

 var container = document.getElementById('toolbar_div');
 google.visualization.drawToolbar(container, components);
 };

 google.charts.setOnLoadCallback(draw);
 </script>
</head>
<body>
 <div id="visualization_div" style="width: 270px; height: 200px;"></div>
 <div id="toolbar_div"></div>
</body>
</html>
[](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Usage
-----------------------------------------------------------------------------

Add a toolbar to your page by calling the `google.visualization.drawToolbar()` method, populating it with the types of export allowed, and the data required for each.

To use a toolbar, your visualization must get its data from a URL; you cannot pass in hand-populated DataTable or DataView objects. You will pass the URL of the data used to populate your visualization into the `drawToolbar()` method.

If you want to provide an iGoogle component or an embeddable iFrame that holds the gadget, you must have a URL for a gadgetized version of the visualization.

### [](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Output Types

The toolbar can offer the user the choice of one or more of the following output types, depending on how you configure your toolbar in the `drawToolbar()` method:

* A simple CSV version of the data (which your browser will either render or offer to download and save, depending on your browser configuration, and/or
* An HTML table holding the data, opened in a new browser window, and/or
* HTML <iframe> code to embed this visualization in a web page, and/or
* A link to page enabling the user to embed this gadget in their iGoogle page.

### [](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Syntax

google.visualization.drawToolbar(_container_, _components_)

#### Parameters

_container_ A handle to a DOM element on the page. The API will draw the toolbar into this element. This is similar to the container parameter for a standard visualization. You should put the toolbar adjacent to the visualization that uses it._components_ An array of objects, each describing a format that the data, or the visualization, can be exported to. The toolbar will expose the options to the user in the order added to the array. Each object has a type property describing the format, and one or more additional properties, depending on the type:

* `type: 'csv'` - This option exports the data to a comma-separated value file. A 'save as' dialog will open in the browser.
  * **datasource**: '_string_' - The data source url.

* `type: html'` - This option exports the data to an HTML table. The page with the data table will open in a new window in the browser.
  * **datasource**: The data source url string.

* `type: igoogle` - This option enables the user to add the visualization to their iGoogle page. An 'add to iGoogle' page will open in the browser. _Use this only if the visualization is available in a gadgetized version._
  * **datasource**: The data source url string.
  * **gadget**: The gadgetized version's xml url string. Note that the visualization that the toolbar is associated with does not have to be the gadgetized version.
  * **userprefs**: An optional preferences object appropriate for this visualization, specifying the visualization preferences.

* `type: htmlcode` - This option creates a block of HTML code that the user can embed in a web page to display the visualization inside an iframe. A popup window with the exact html element of the gadget will open in the browser._Use this only if the visualization is available in a gadgetized version._
  * **datasource**: The data source url string.
  * **gadget**: The gadget xml url string.
  * **userprefs**: An optional preferences object appropriate for this visualization, specifying the visualization preferences.
  * **style**: An optional string for the style of the iframe. For example: 'width: 300px; height: 500px;'.

### Example

function drawToolbar() {
 var components = [
 {type: 'igoogle', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA',
 gadget: 'https://www.google.com/ig/modules/pie-chart.xml',
 userprefs: {'3d': 1}},
 {type: 'html', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA'},
 {type: 'csv', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA'},
 {type: 'htmlcode', datasource: 'https://spreadsheets.google.com/tq?key=pCQbetd-CptHnwJEfo8tALA',
 gadget: 'https://www.google.com/ig/modules/pie-chart.xml'}
 ];

var container = document.getElementById('toolbar_div');
 google.visualization.drawToolbar(container, components);
};
[](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Data Policy
-----------------------------------------------------------------------------------

All code and data are processed and rendered in the browser. No data is sent to any server. For some components, the data is taken from the respective data source given to the toolbar.

[](https://developers.google.com/chart/interactive/docs/gallery/toolbar)Localization
------------------------------------------------------------------------------------

The toolbar currently only supports US English.
