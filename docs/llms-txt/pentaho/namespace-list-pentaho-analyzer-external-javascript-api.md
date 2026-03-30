# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/namespace-list-pentaho-analyzer-external-javascript-api.md

# Namespace List

The `pentaho-analyzer-client` is where all of the client-side code goes for the analyzer plugin (javascript, html, css, images, and so on).

You can create new configurations for other browsers if desired. You just need to place them in the same folder and reference them in the same way, as shown in the following example structure:

* **analyzer**

  Classes:

  * AnalyzerModule
* **analyzer.visual**
  * Interfaces:
    * ICanAddFieldInfo
  * Classes:
    * Application
    * ApplicationType
    * Registry
* **cv**

  cv.api Classes:

  * event
  * operatiom
  * report
  * reportUtil
  * ui
  * util
