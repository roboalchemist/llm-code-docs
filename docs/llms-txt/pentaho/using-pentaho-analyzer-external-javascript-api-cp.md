# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp.md

# Using Pentaho Analyzer External JavaScript API

This API set gives OEMs more control over Analyzer when working in an embedded fashion. These APIs allow for more fine-grained interaction with the Analyzer viewer, reports, and data.

## How to Access the APIs

You can access the APIs using the following embedded iFrame methods:

* **Same Domain**

  While using Analyzer inside of PUC, you can execute your custom API code in two ways: placing the code directly in the parent frame or by including the code within an external resource file.
* **Different Domain**

  The APIs are exposed in the global scope of each Analyzer iFrame. The Analyzer iFrame looks for an `onAnalyzerReady` function attached to the parent window.

## Embedded in an iFrame with the Same Domain within Parent Frame

Inside of the parent html file, add the following script block. It will be executed for each Analyzer report that is either opened or created when Analyzer is initialized.

```javascript
<script type="text/javascript">
  window.onAnalyzerReady = function(api, frameId) {
      // Perform Analyzer API actions
  };
</script>

```

Since the `onAnalyzerReady` code is executed when Analyzer is initialized, api.event.registerInitListener is not available from within this code block.

## Embedded in an iFrame with the Same Domain as External Resource

Additionally, you can achieve the same result by including your custom javascript as an external resource. The only difference is that you do not have to use the "onAnalyzerReady" function since Analyzer is already loading this file at the appropriate time. Inside of your own plugin.xml file, add a path to your custom javascript file, which will be executed when Analyzer is loading:

```javascript
<file context="analyzer">path/to/your/javascript/ExternalFile.js</file>

```

The same code that is in the first javascript block is the same, but without using the "onAnalyzerReady" function. Instead, you will require the API using RequireJS.

```javascript
require([ "analyzer/cv_api" ], function(api) {
  api.event.registerInitListener(function(e, cv) {
    // Perform Analyzer API actions
  });
});

```

## Embedded in an iFrame on a Different Domain

The APIs are exposed in the global scope of each Analyzer iFrame. The Analyzer iFrame looks for an `onAnalyzerReady` function attached to the parent window. Due to cross-site scripting issues, you must configure the iFrame in which Analyzer is embedded. You can do this by adding an external resource file to any plugin's plugin.xml file. It is common to use the `default-plugin` for adding such scripts. It is is located in `pentaho-solutions/system/default-plugin/`.

Inside of the plugin's `plugin.xml` file, you will add a path to your own javascript file which will be executed when Analyzer is loading.

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>File</td><td>Example path</td><td>Addition information</td></tr><tr><td><code>Plugin.xml</code></td><td><pre class="language-javascript"><code class="lang-javascript">&#x3C;file context="analyzer">path/to/your/global/javascript/GlobalFile.js&#x3C;/file>

</code></pre></td><td>Inside of your external javascript file, you must set a custom domain property on the window of the Analyzer iFrame.</td></tr><tr><td><code>ExternalFile.js</code></td><td><pre class="language-javascript"><code class="lang-javascript">// iFrame source = "<http://example.company.org:8080/pentaho/api/repos/xanalyzer/editor>"
window\.customDomain = "company.org";

</code></pre></td><td>Additionally, you must set the document.domain inside of the parent page or frame where you will be embedding Analyzer. When you are embedding the Analyzer iFrame into your page, you can bind an <code>onAnalyzerReady</code> function to the window. Analyzer will automatically look for this function and execute the function once the API has been loaded and made available.</td></tr><tr><td><code>[www.company.org/index.html](http://www.company.org/index.html)</code></td><td><pre class="language-javascript"><code class="lang-javascript">\<html>
\<head>
\<script type="text/javascript">
document.domain = "company.org"

```
  window.onAnalyzerReady = function(api, frameId) {
    // Perform Analyzer API actions
  };
&#x3C;/script>
```

\</head>

\<body>
\<iframe id="analyzer-frame" src="[http://example.company.org:8080/pentaho/api/repos/xanalyzer/editor">\&#x3C;/iframe>](http://example.company.org:8080/pentaho/api/repos/xanalyzer/editor">\&#x3C;/iframe>)
\</body>
\</html>

</code></pre></td><td>When Analyzer loads, you will have access to the API and the <code>frameID</code> of which frame is calling your code, so that you can customize each frame appropriately. Analyzer executes the <code>onAnalyzerReady</code> code for each frame located in the page, therefore, the <code>frameID</code> will be different for each frame, and the API you receive will be related to that frame.</td></tr></tbody></table>

The following code is an example of calling embedded content in an iFrame on a different domain:

```javascript
//Example calls into namespaced functions
cv.api.report.setLayoutFields("test");
cv.api.report.getLayoutFields();

```

## Direct URL

To access the API when Analyzer is loaded directly by its URL, you will need to use the **Embedded in an iFrame with the Same Domain as External Resource** approach.

## Service Calls Reference

References for the following categories of JavaScript API service calls are available:

* **Analyzer Module**

  Details the methods for `analyzer.AnalyzerModule`, which allows for the deployment and control of Analyzer in a DOM element.
* **Event**

  Details the methods for `cv.api.event` class, which contains all necessary calls for creating and registering `Events`.
* **Operation**

  Details the methods for `cv.api.operation` class, which contains available operation-related API calls.
* **Report**

  Details the methods for `cv.api.report` class, which contains the available report-related API calls.
* **User Interface**

  Details the methods for `cv.api.ui` class, which contains the available user interface-related API calls.
* **Utility**

  Details the methods for `cv.api.util` class, which contains the available utility-related API calls.
