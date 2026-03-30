# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/custom-analyzer-action-links-to-javascript-functions.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/custom-analyzer-action-links-to-javascript-functions.md

# Custom Analyzer action links to JavaScript functions

Analyzer can be configured with custom action links that call out to JavaScript functions. These action links are available in a context menu by right-clicking on level members or measure cells.

![Sample of custom action links to JavaScript in Analyzer](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-22ca7638d12636366261ca2b12f10f05324f70ee%2FssPAZDefineCustomActionsinMondrian.png?alt=media)

## Define custom actions in Mondrian

Action links can be defined in your Mondrian schema as annotations. These can be defined under a Level or a Measure. There is no limit to the number of custom action links that you can define, but they need to be named in ascending order, such as `AnalyzerCustomAction`, `AnalyzerCustomAction2`, `AnalyzerCustomAction3`.

The annotation value is just a link-label and JavaScript function, separated by a comma. Analyzer will automatically try to add custom action links on a **Type** level or a **Sales** measure whenever they are used in a report.

Annotation defined on a **Type** level:

```
<Dimension foreignKey="STATUS" name="Order Status">
     <Hierarchy hasAll="true" allMemberName="All Status Types" primaryKey="STATUS">
        <Level name="Type" column="STATUS" type="String" uniqueMembers="true" levelType="Regular" hideMemberIf="Never">
                <Annotations>
                    <Annotation name="AnalyzerCustomAction">Custom action 3,customHandlerThree</Annotation>
                    <Annotation name="AnalyzerCustomAction2">Custom action 4,customHandlerFour</Annotation>
                </Annotations>
        </Level>
    </Hierarchy>
</Dimension>
```

Annotation defined on a **Sales** measure:

```
<Measure name="Sales" column="TOTALPRICE" formatString="#,###" aggregator="sum" description="Foo">
    <Annotations>
        <Annotation name="AnalyzerBusinessGroup">Measures</Annotation>
        <Annotation name="AnalyzerCustomAction">Custom action 1,customHandlerOne</Annotation>
        <Annotation name="AnalyzerCustomAction2">Custom action 2,customHandlerTwo</Annotation>    </Annotations>
    <CalculatedMemberProperty name="CHART_SERIES_COLOR" value="#0d8ecf" />
</Measure>
```

## Implement a custom action JavaScript function

In order to implement the JavaScript function, you need to create a new Pentaho plugin that injects your JavaScript functions into Analyzer. Here is an example of an `analyzer_extension_plugin.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin title="analyzer-extension">
   <static-paths>
        <static-path url="/analyzer-extension/resources" localFolder="resources"/>
   </static-paths>
   <external-resources>
         <file context="analyzer">content/analyzer-extension/resources/analyzer_extension_plugin.js</file>
   </external-resources>
</plugin>
```

This basically tells the Pentaho Server to inject the `analyzer_extension_plugin.js` file into Analyzer so that those functions are now available to Analyzer to call when a user clicks on a custom action link.

Here is an example `analyzer_extension_plugin.js`.

```javascript
cv.extension = cv.extension || {};

/** 
 * report - Analyzer report definition.
 * formula - The level or measure that was clicked on.
 * ctx - All levels that intersect on the clicked on level or cell.
 * filter - Filters applied on the report. Only includes filters which includes members.
 */
 
cv.extension.customHandlerOne = function (report, formula, ctx, filter) {
    var year = ctx['[Time].[Years]']; // Returns the member unique name
    if (year) 
        year = cv.util.parseMDXExpression(year); // Extract the name of the member
    var url = window.CONTEXT_PATH + "api/repos/:public:Steel%20Wheels:Country%20Performance%20(heat%20grid).xanalyzer/viewer?yearParameter=" + year;
    if (window.parent && window.parent.parent && window.parent.parent.mantle_openTab) {
        window.parent.parent.mantle_openTab("Custom One", "Custom One", url);
    }
    window.open(url);
}

cv.extension.customHandlerOne_validate = function (report, formula, ctx, filter) {
    var territory = ctx['[Markets].[Territory]'];
    if (territory == "[Markets].[Japan]")
        return false;
    return true;
}    
```

You must define your custom action JavaScript function under the `cv.extension` namespace. The name of the JavaScript function must exactly match the name you used in the *AnalyzerCustomAction* annotation. The function takes four parameters:

* **report**

  This is the Analyzer report object. You normally will not use this, but if you want to access the report XML definition to inspect the state of the current report definition, you can access `report.reportDoc`.
* **formula**

  This is either the level MDX unique name or the measure unique name, depending on what the user clicked on.
* **ctx**

  This is a map of all the levels on the row or column zone and their corresponding MDX members. When clicking on a cell, this map will contain all row and column levels on the report. When clicking on a level member, this map will only contain outer levels which are usually to the left or above the clicked-on level.
* **filter**

  This is a level map-to-filter operator-to-member array of all report filters with the exception of numeric filters like `Top10` or `Greater than`.

The **filter** object is a map of levels to predicate objects. A predicate object is a map of predicate operators to operator arguments. A single level such as *\[Customer].\[Name]* may have more than one predicate operator, such as contains `John` but does not contain `Doe`.

The possible operators are: EQUALS, NOT\_EQUAL, BEFORE, AFTER, BETWEEN, CONTAIN, and NOT\_CONTAIN. For all operators with the exception of CONTAIN and NOT\_CONTAIN, the operator arguments are MDX members such as `[Time].[2014]`. CONTAIN and NOT\_CONTAIN have string literals as operator arguments. Numeric filters such as **Top 10 Account by Sales** are not exposed in the filter object.

As an example, assuming the user clicks on this cell:

![Example of custom JavaScript actions in Analyzer](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-d1e4b35e07e7eb34a5a972f7d197afa55163d6ca%2FssPAZImplementCustomActionJavaScriptFunction.png?alt=media)

Then the **member**, **ctx**, and **filter** arguments will look like:

```javascript
ctx: Object
     [Markets].[Territory]: "[Markets].[APAC]"
     [Measures].[MeasuresLevels]: "[Measures].[Sales]"
     [Order Status].[Type]: "[Order Status].[Shipped]"
     [Time].[Years]: "[Time].[2003]"
     __proto__: Object
filter: Object
    {
    '[Product].[Line]':
    {EQUALS:['[Product].[Trucks and Buses]','[Product].[Trains]','[Product].[Planes]']}
    ,
    '[Time].[Years]':
    {EQUALS: ['[Time].[2013]','[Time].[2014]']}

    }
formula: "[Measures].[Sales]"
```

Here are a couple of helpful tips for implementing the JavaScript functions:

* You can use `cv.util.parseMDXExpression` to extract the name of the member. For example, `[Year].[2003]` would return: `2003`.
* You can construct your own URL and then open the URL in a new **PUC** tab, assuming Analyzer is running within PUC with the function: `window.parent.parent.mantle_openTab`.

## Determine when to show a custom action

There is also another feature to validate whether a custom action link should be included in the context menu or not. You can implement a validation function which returns false to hide the link in the UI. If this validation function is not implemented, then the link will always be shown. This validation function must be named by suffixing the custom action JavaScript function name with `_validate`.

In this example, the **Custom action 1** menu item will not be included if the user right-clicks on a **Measure** cell where the current context includes `Territory: Japan`:

```javascript
cv.extension.customHandlerOne_validate = function (report, formula, ctx, filter) {
var territory = ctx['[Markets].[Territory]'];
if (territory == "[Markets].[Japan]")
return false;
return true;
}
```

![Example of showing a specific custom action in Analyzer](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-7bf4669420c5d7d36a056c94a6586368e5cf8ac8%2FssPAZDetermineWhenToShowCustomAction.png?alt=media)

Notice how **Custom action 1** was not included in the above menu.
