# Source: https://developers.google.com/chart/interactive/docs/queries

Title: Data Queries

URL Source: https://developers.google.com/chart/interactive/docs/queries

Markdown Content:

* This page explains how to send a SQL query to a Datasource, a web service supporting the Chart Tools Datasource protocol, to receive a DataTable with the requested data.

* You can use a Query object to send a request with optional parameters for sending method and a query language string for filtering data, receiving a response handled by a callback function.

* The response handler checks for errors and, if successful, retrieves the DataTable from the QueryResponse for use in visualizations like charts.

* CSV data can be either manually converted to Google Charts datatable format or placed on a web server and queried using the techniques described on the page.

* More detailed information on query language syntax, the Query class, and the QueryResponse class can be found via provided links.

This page describes how to send a query to a data source that supports the Chart Tools Datasource protocol.

Contents
--------

1. [Overview](https://developers.google.com/chart/interactive/docs/queries#overview)
2. [Sending a request](https://developers.google.com/chart/interactive/docs/queries#Sending_a_Query)
3. [Processing the response](https://developers.google.com/chart/interactive/docs/queries#Processing_the_Query_Response)
4. [Reading CSV files](https://developers.google.com/chart/interactive/docs/queries#csv)
5. [More information](https://developers.google.com/chart/interactive/docs/queries#moreinfo)

Overview
--------

A Datasource is a web service that supports the Chart Tools Datasource protocol. You can send a SQL query to a Datasource, and in response you will receive a DataTable populated with the appropriate information. Some examples of Datasources include [Google Spreadsheets](https://developers.google.com/chart/interactive/docs/spreadsheets) and SalesForce.

[](https://developers.google.com/chart/interactive/docs/queries)Sending a request
---------------------------------------------------------------------------------

**To send a request:**

1. Instantiate a [Query](https://developers.google.com/chart/interactive/docs/reference#Query) object with the URL of your Datasource. The URL should indicate what data is being requested, in a syntax understood by that data source.
2. Optionally specify request options such as sending method as an optional second parameter in the `Query` object constructor (see the Query constructor's [`opt_options`](https://developers.google.com/chart/interactive/docs/reference#Query) parameter for details):
3. Optionally add a [query language string](https://developers.google.com/chart/interactive/docs/querylanguage) to sort or filter the results, and then send the request. Datasources are not required to support the Chart Tools Datasource query language. If the Datasource does not support the query language, it will ignore the SQL query string, but still return a `DataTable`. The query language is a SQL language variant; read the full [query language syntax here](https://developers.google.com/chart/interactive/docs/querylanguage).
4. Send the query, specifying a callback handler that will be called when the response is received: see next section for details.

Here's an example of sending a request for data in a Google Spreadsheet cell range; to learn how to get the URL for a Google Spreadsheet, see [here](https://developers.google.com/chart/interactive/docs/spreadsheets#Google_Spreadsheets_as_a_Data_Source):

function initialize() {
 var opts = {sendMethod: 'auto'};
 // Replace the data source URL on next line with your data source URL.
 var query = new google.visualization.Query('http://spreadsheets.google.com?key=123AB&...', opts);

 // Optional request to return only column C and the sum of column B, grouped by C members.
 query.setQuery('select C, sum(B) group by C');

 // Send the query with a callback function.
 query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
 // Called when the query response is returned.
 ...
}
If you are sending your query from within Apps Script, be sure to use [`IFRAME` mode](https://developers.google.com/apps-script/reference/html/sandbox-mode).

[](https://developers.google.com/chart/interactive/docs/queries)Processing the response
---------------------------------------------------------------------------------------

Your response handler function will be called when the request returns. The parameter passed in to your response handler function is of type [google.visualization.QueryResponse](https://developers.google.com/chart/interactive/docs/reference#QueryResponse). If the request was successful, the response contains a data table (class `google.visualization.DataTable`). If the request failed, the response contains information about the error, and no `DataTable`.

**Your response handler should do the following:**

1. Check whether the request succeeded or failed by calling `response.isError()`. You shouldn't need to display any error messages to the user; the Visualization library will display an error message for you in your container `<div>`. However, if you do want to handle errors manually, you can use the [`goog.visualization.errors`](https://developers.google.com/chart/interactive/docs/reference#errordisplay) class to display custom messages (see the [Query Wrapper Example](https://developers.google.com/chart/interactive/docs/examples#querywrapper) for an example of custom error handling).
2. If the request succeeded, the response will include a `DataTable` that you can retrieve by calling `getDataTable()`. Pass it to your chart.

The following code demonstrates handling the previous request to draw a pie chart:

function handleQueryResponse(response) {

 if (response.isError()) {
 alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
 return;
 }

var data = response.getDataTable();
 var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
 chart.draw(data, {width: 400, height: 240, is3D: true});
}
[](https://developers.google.com/chart/interactive/docs/queries)Reading CSV files
---------------------------------------------------------------------------------

If you want to build a chart out of CSV (comma-separated values) data, you have two choices. Either manually convert the CSV data into the [Google Charts datatable format](https://developers.google.com/chart/interactive/docs/datatables_dataviews#creatingpopulating), or place the CSV file on the web server serving the chart, and query it using the technique on this page.

[](https://developers.google.com/chart/interactive/docs/queries)More information
--------------------------------------------------------------------------------

* [Query Language Syntax](https://developers.google.com/chart/interactive/docs/querylanguage) - Describes the syntax of the language used to make data queries.
* [Query Class](https://developers.google.com/chart/interactive/docs/reference#Query) - Reference page for the class that wraps a query.
* [QueryResponse Class](https://developers.google.com/chart/interactive/docs/reference#QueryResponse) - Reference page for the class that wraps the response to a query.
