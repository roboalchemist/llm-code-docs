# Source: https://developers.google.com/chart/interactive/docs/basic_load_libs

Title: Load the Libraries

URL Source: https://developers.google.com/chart/interactive/docs/basic_load_libs

Markdown Content:

* All webpages using Google Charts should include `<script src="https://www.gstatic.com/charts/loader.js"></script>` in the `<head>` section to load the necessary libraries.

* After loading the loader, use `google.charts.load()` to specify the version and required chart packages.

* The first argument of `google.charts.load()` is the version, which can be `'current'` for the latest release, `'upcoming'` for the next release candidate, or a specific frozen version number.

* The second argument of `google.charts.load()` is an object for settings, including `packages` to list required chart types, `language` for locale customization, and `callback` to specify a function to run after loading.

* To ensure chart packages are loaded before use, register a callback function using `google.charts.setOnLoadCallback()` or by chaining `.then()` to the `google.charts.load()` Promise.

This page shows how to load the Google Chart libraries.

[](https://developers.google.com/chart/interactive/docs/basic_load_libs)Basic Library Loading
---------------------------------------------------------------------------------------------

With few exceptions, all web pages with Google Charts should include the following lines in the `<head>` of the web page:

<script **src="https://www.gstatic.com/charts/loader.js"**></script>
<script>
  **google.charts.load('current', {packages: ['corechart']});**
  **google.charts.setOnLoadCallback(drawChart);**
  ...
</script>
The first line of this example loads the loader itself. You can only load the loader one time no matter how many charts you plan to draw. After loading the loader, you can call the `google.charts.load` function one or more times to load packages for particular chart types.

The first argument to `google.charts.load` is the version name or number, as a string. If you specify `'current'`, this causes the latest official release of Google Charts to be loaded. If you want to try the candidate for the next release, use `'upcoming'` instead. In general there will be very little difference between the two, and they'll be completely identical except when a new release is underway. A common reason to use `upcoming` is that you want to test a new chart type or feature that Google is about to release in the next month or two. (We announce upcoming releases on our [forum](https://groups.google.com/group/google-visualization-api) and recommend that you try them out when announced, to be sure that any changes to your charts are acceptable.)

The example above assumes you want to display a `corechart` (bar, column, line, area, stepped area, bubble, pie, donut, combo, candlestick, histogram, scatter). If you want a different or additional chart type, substitute or add the appropriate package name for `corechart` above (e.g.,

```
{packages: ['corechart',
'table', 'sankey']}
```

. You can find the package name in the 'Loading' section of the documentation page for each chart.

This example also assumes that you have a JavaScript function named `drawChart` defined somewhere in your web page. You can name that function whatever you like, but be sure it is globally unique and that it is defined before you reference it in your call to `google.charts.setOnLoadCallback`.

**Note:** Previous versions of Google Charts used code that differs from the above to load the libraries. To update your existing charts to use the new code, see [Update Library Loader Code](https://developers.google.com/chart/interactive/docs/basic_load_libs#updateloader).

Here is a complete example of drawing a pie chart using the basic loading technique:

<head>
  <script **src="https://www.gstatic.com/charts/loader.js"**></script>
  <script>
    google.charts.load('current', {packages: ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      // Define the chart to be drawn.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Element');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Nitrogen', 0.78],
        ['Oxygen', 0.21],
        ['Other', 0.01]
      ]);

      // Instantiate and draw the chart.
      var chart = new google.visualization.PieChart(document.getElementById('myPieChart'));
      chart.draw(data, null);
    }
  </script>
</head>
<body>
  <!-- Identify where the chart should be drawn. -->
  <div id="myPieChart"/>
</body>
[](https://developers.google.com/chart/interactive/docs/basic_load_libs)Loading Details
---------------------------------------------------------------------------------------

First you must load the loader itself, which is done in a separate `script` tag with `src="https://www.gstatic.com/charts/loader.js"`. This tag can be either in the `head` or `body` of the document, or it can be inserted dynamically into the document while it is being loaded or after loading is completed.

<script **src="https://www.gstatic.com/charts/loader.js"**></script>
After the loader is loaded, you are free to call `google.charts.load`. Where you call it can be in a `script` tag in the `head` or `body` of the document, and you could call it either while the document is still loading or any time after it has finished loading.

As of version 45, you _may_ call `google.charts.load` more than one time in order to load additional packages, though it is safer if you can avoid doing so. You must provide the same version number and language settings each time.

You can now use the old JSAPI `autoload` URL parameter, but the value of this parameter must use strict JSON formatting and URL encoding. In JavaScript, you can do the encoding of `jsonObject` with this code: `encodeURIComponent(JSON.stringify(jsonObject))`.

### [](https://developers.google.com/chart/interactive/docs/basic_load_libs)Limitations

If you are using versions **prior to v45**, there are a couple minor but important limitations with how you load Google Charts:

1. You can only call `google.charts.load`_once_. But you can list all the packages that you'll need in one call, so there's no need to make separate calls.
2. If you're using a ChartWrapper, you must explicitly load all the packages you'll need, rather than relying on the ChartWrapper to automatically load them for you.
3. For [Geochart](https://developers.google.com/chart/interactive/docs/gallery/geochart) and [Map Chart](https://developers.google.com/chart/interactive/docs/gallery/map), you must load both the old library loader and the new library loader. Again, this is _only_ for versions prior to v45, and you should _not_ do this for later versions. <script **src="https://www.gstatic.com/charts/loader.js"**></script>

<script **src="https://www.google.com/jsapi"**></script>

### [](https://developers.google.com/chart/interactive/docs/basic_load_libs)Load Version Name or Number

The first argument of your `google.charts.load` call is the version name or number. There are only two special version names at this time, and several frozen versions.

current This is for the latest official release which changes each time we push out a new release. This version is ideally well tested and bug free, but you may want to specify a particular frozen version instead once you are satisfied it is working.upcoming This is for the next release, while it is still being tested and before it becomes the official current release. Please test this version regularly so that you know as soon as possible whether there are any problems that should be addressed before this version becomes the official release.
When we release new versions of Google Charts, some of the changes are big, like entirely new chart types. Other changes are small, like enhancements to the appearance or behavior of existing charts.

Many Google Chart creators fine-tune the look and feel of their charts until it's exactly what they want. Some creators might feel more comfortable knowing that their charts will never change, regardless of what improvements we make in the future. For those users, we support _frozen_ Google Charts.

Frozen chart versions are identified by number, and they're described in our [Official Releases](https://developers.google.com/chart/interactive/docs/release_notes#Releases). To load a frozen version, replace `current` or `upcoming` in your call of `google.charts.load` with the frozen version number:

<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
    google.charts.load(**'43'**, {packages: ['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    ...
</script>
We expect that frozen versions will remain available indefinitely, though we may retire frozen versions that have security concerns. We will typically not provide support for frozen versions, except to unhelpfully suggest that you upgrade to a newer version.

### [](https://developers.google.com/chart/interactive/docs/basic_load_libs)Load Settings

The second parameter in your call of `google.charts.load` is an object for specifying settings. The following properties are supported for settings.

packages An array of zero or more packages. Each package that is loaded will have the code required to support a set of functionality, typically a type of chart. The package or packages you need to load are listed in the documentation for each type of chart. You can avoid specifying any packages if you use a [ChartWrapper](https://developers.google.com/chart/interactive/docs/reference#chartwrapper-class) to automatically load what will be required. language The code for the language or locale that should be to customize text that might be part of the chart. See [Locales](https://developers.google.com/chart/interactive/docs/basic_load_libs#Locales) for more details. callback A function that will be called once the packages have been loaded. Alternatively, you can specify this function by calling `google.charts.setOnLoadCallback` as demonstrated in the example above. See [Callback](https://developers.google.com/chart/interactive/docs/basic_load_libs#Callback) for more details.   google.charts.load('current', { packages: [ 'corechart'], **callback: drawChart** });mapsApiKey(v45) This setting lets you specify a key that you may use with [Geochart](https://developers.google.com/chart/interactive/docs/gallery/geochart) and [Map Chart](https://developers.google.com/chart/interactive/docs/gallery/map). You may want to do this rather than use the default behavior which may result in occasional throttling of service for your users. Learn how to set up your own key for using the 'Google Maps JavaScript API' service here: [Get a Key/Authentication](https://developers.google.com/maps/documentation/javascript/get-api-key). Your code will look something like this:   var myMapsApiKey = 'SomeMagicToSetThis';
  google.charts.load('45', { packages: [ 'geochart'], **mapsApiKey: myMapsApiKey**  });safeMode(v47) When set to true, all charts and tooltips that generate HTML from user-supplied data will sanitize it by stripping out unsafe elements and attributes. Alternatively (v49+), the library can be loaded in the safe mode using a shortcut that accepts the same loading settings, but always loads the "current" version:   google.charts.safeLoad({ packages: ['corechart'] });

### Locales

_Locales_ are used to customize text for a country or language, affecting the formatting of values such as currencies, dates, and numbers.

By default, the Google Charts is loaded with the "en" locale. You can override this default by explicitly specifying a locale in the loading settings.

To load a chart formatted for a specific locale, use the `language` setting like so:

 // Load Google Charts for the Japanese locale.
 google.charts.load('current', {'packages':['corechart'], 'language': 'ja'});
[Follow this link for a live example.](https://developers.google.com/chart/interactive/docs/examples/specificlocale)

### Callback

Before you can use any of the packages loaded by `google.charts.load` you have to wait for the loading to finish. It is not enough to just wait for the document to finish loading. Since it can take some time before this loading is finished, you need to register a callback function. There are three ways this can be done. Either specify a `callback` setting in your `google.charts.load` call, or call `setOnLoadCallback` passing a function as the argument, or use the Promise that is returned by the call of `google.charts.load`.

Note that for all of these ways, you need to provide a function definition, rather than call the function. The function definition you provide can be either a named function (so you just give its name) or an anonymous function. When the packages have finished loading, this callback function will be called with no arguments. The loader will also wait for the document to finish loading before calling the callback.

If you want to draw more than one chart, you can either register more than one callback function using `setOnLoadCallback`, or you can combine them into one function. Learn more about how to [Draw Multiple Charts on One Page](https://developers.google.com/chart/interactive/docs/basic_multiple_charts).

  google.charts.setOnLoadCallback(**drawChart1**);
  google.charts.setOnLoadCallback(**drawChart2**);
  // OR
  google.charts.setOnLoadCallback(
    **function() { // Anonymous function that calls drawChart1 and drawChart2 drawChart1(); drawChart2(); }**);

### [](https://developers.google.com/chart/interactive/docs/basic_load_libs) Callback via Promise

Another way of registering your callback is to use the Promise that is returned from the `google.charts.load` call. You do this by adding a call to the `then()` method with code that looks like the following.

 google.charts.load('upcoming', {packages: ['corechart']})**.****then(drawChart)**;
One benefit of using the Promise is that then you can easily draw more charts just by chaining more `.then(anotherFunction)` calls. Using the Promise also ties the callback to the specific packages required for that callback, which is important if you want to load more packages with another call of `google.charts.load()`.

[Update Library Loader Code](https://developers.google.com/chart/interactive/docs/basic_load_libs)
--------------------------------------------------------------------------------------------------

Previous versions of Google Charts used different code to load the libraries. The table below shows the old library loader code versus the new.

| Old Library Loader Code |
| --- |
| <script type="text/javascript" src="https://www.google.com/jsapi"></script> <script type="text/javascript"> google.load("visualization", "1", {packages:["corechart"]}); google.setOnLoadCallback(drawChart); </script> |
| New Library Loader Code |
| <script **src="https://www.gstatic.com/charts/loader.js"**></script> <script> **google.charts.load('current', {packages: ['corechart']});** **google.charts.setOnLoadCallback(drawChart);** </script> |

To update your existing charts, you can replace the old library loader code with the new code. However, keep in mind the [limitations](https://developers.google.com/chart/interactive/docs/basic_load_libs#limitations) on loading libraries described above.
