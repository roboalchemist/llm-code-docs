# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/moving-to-visualization-api-3.0-cp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/moving-to-visualization-api-3.0-cp.md

# Moving to Visualization API 3.0

Visualization API 3.0 is a significant upgrade from Visualization API 2.0. While the previous version worked only within Pentaho Analyzer, Visualization API 3.0 is application independent. It also excludes any functionality not related with data visualization. Like most of the current Pentaho platform, Visualization API 3.0 uses AMD/RequireJS as the module technology. Previously, the API used a global variable paradigm.

See [Analyzer and the Visualization API](#analyzer-and-the-visualization-api) for examples on how Visualization API 3.0 differs from Visualization API 2.0 specifically for Pentaho Analyzer.

## Metadata and registration conversion

The following sections show the metadata and registration of a visualization before and after converting to Visualization API 3.0.

#### Before Visualization API 3.0

Before Visualization API 3.0, the following code defined metadata:

```javascript
pentaho.visualizations.push({ 
  id: 'pentaho_sample_KPI',      // Unique identifier
  name: 'Example KPI',           // Visible name, this will come from a properties file, eventually 
  type: 'kpi',                   // Generic type id 
  source: 'Example',             // Id of the source library 
  'class': 'pentaho.sample.KPI', // Type of the Javascript object to instantiate
  menuOrdinal: 10001,
  menuSeparator: true,
  maxValues: [1000, 2000, 3000], 
  args: {                        // Arguments to provide to the Javascript object 
    aggregate: 'AVG'             //  this allows a single class to act as multiple visualizations
  },
  dataReqs: [                    // dataReqs describes the data requirements of this visualization 
    { 
      name: 'Default', 
      reqs : 
        [ 
          { 
            id: 'rows',               // ID of the data element 
            dataType: 'string',       // data type - 'string', 'number', 'date', 
                                      // 'boolean', 'any' or a comma separated list 
            dataStructure: 'column',  // 'column' or 'row' - only 'column' supported so far 
            caption: 'Level',         // visible name 
            required: true,           // true or false 
            allowMultiple: false, 
            ui: { 
              group: 'data' 
            } 
          }, 
          {
            id: 'measures', 
            dataType: 'number', 
            dataStructure: 'column', 
            caption: 'Measure', 
            required: true, 
            allowMultiple: false, 
            ui: { 
              group: "data" 
            } 
          }, 
          { 
            id: 'aggregate', 
            dataType: 'string', 
            values: ['MIN', 'MAX', 'AVG'], 
            ui: { 
              labels: ['Minimum', 'Maximum', 'Average'], 
              group: 'options', 
              type: 'combo',  // combo, checkbox, slider, textbox, gem, gemBar, and button are valid ui types
              caption: 'Aggregation' 
            }
          }
        ]
    }
  ]
});

```

The `pentaho.visualizations` is a global array where visualizations’ metadata is placed. The visualization has an identifier of `pentaho_sample_KPI` and is presented in the UI as `Example KPI`. The visualization itself is a JavaScript class which should be published globally in the path `pentaho.sample.KPI`.

Then, the visualization needed to be registered with Pentaho Analyzer. The following content would be placed in an Analyzer plugin file:

```javascript
// example_analyzer_plugin.js
var analyzerPlugins = analyzerPlugins || [];

analyzerPlugins.push({
  init: function() { 
	  // Register visualizations to display in Analyzer 
    cv.pentahoVisualizations.push(pentaho.visualizations.getById('pentaho_sample_KPI')); 

    // Helpers contain code that knows about the Analyzer specific context. The one 
    // function that's required "generateOptionsFromAnalyzerState" is called so the 
    // visualization can set its own options based on Analyzer's current report.  
    cv.pentahoVisualizationHelpers['pentaho_sample_KPI'] = { 
      // Use one of Analyzer's stock placeholder images. 
      placeholderImageSrc: CONTEXT_PATH + 'content/analyzer/images/viz/VERTICAL_BAR.png', 

      // This method allows a visualization to generate visualization specific 
      // options based on Analyzer’s report definition. In the following example, 
      // this visualisation is setting a background color using the same background 
      // color setting in Chart Options. You can figure out the existing chart 
      // options by looking at the report XML by clicking the XML link in Analyzer.    
      // return a hash object containing the custom state of your visualization.
      generateOptionsFromAnalyzerState: function(report) { 
        return {myBackgroundColor: report.reportDoc.getChartOption("backgroundColor")}; 
      }
    };

    // LayoutConfig objects manage the interaction between Analyzer's Layout Panel 
    // and the visualization's settings.

    // Declare a new class which extends the built-in version from Analyzer. 
    dojo.declare("SampleConfig", [analyzer.LayoutConfig], { 
      onModelEvent: function(config, item, eventName, args) {
        if(eventName == "value") {
          this.report.visualization.args['aggregate'] = config.byId('aggregate').value; 
  
          // Add a report state item to the undo/redo history stack. 
          this.report.history.add(new cv.ReportState("Update KPI Aggregation"));
  
          // Trigger a report refresh so that the visualization is updated with the change.
          this.report.refreshReport();
        }
        
        this.inherited(arguments);  
      }
    });

    // Register the Layout Panel Configuration Manager. 
    // Note that the string entry matches 'JSON_' plus the visualization id 
    // defined earlier.
    analyzer.LayoutPanel.configurationManagers['JSON_pentaho_sample_KPI'] = SampleConfig; 
  } // init
});

```

#### After converting to Visualization API 3.0

In the Visualization API 3.0, a visualization is identified by its model class. The model class plays the double role of concentrating the metadata of a visualization and of serving as the runtime object used by applications and visualizations to write and read options from.

After converting to Visualization API 3.0, the metadata is now defined in the `model.js` file, as shown in the following code example:

```javascript
// Model.js
define([
  "pentaho/module!_",
  "pentaho/visual/Model",
  "pentaho/i18n!model"
], function(module, BaseModel, bundle) {

  "use strict";
  
  var operDomain = bundle.structured.operation.domain;

  return BaseModel.extend({
    $type: {
      id: module.id,
      props: [
        {
          name: "rows",
          base: "pentaho/visual/role/Property",
          modes: [{dataType: "string"}],
          fields: {isRequired: true}
        },
        {
          name: "measures",
          base: "pentaho/visual/role/Property",
          modes: [{dataType: "number"}],
          fields: {isRequired: true}
        },
        {
          name: "aggregate",
          valueType: "string",
          domain: [
            {v: "min", f: operDomain.min.f},
            {v: "max", f: operDomain.max.f},
            {v: "avg", f: operDomain.avg.f}
          ],
          defaultValue: "avg"
        },
        {
          name: "backgroundColor",
          valueType: "string"
        }
      ]
    }
  })
  .localize({$type: bundle.structured.type})
  .configure();
});

```

It defines a model class, which inherits from the base model class, `pentaho.visual.Model`. The identifier of the visualization is that of its model class’ AMD module, which could be `pentaho/visual/samples/KPI/Model`.

The registration is now defined by the following code:

```
{
  "name": "@pentaho/visual-samples-kpi",
  "version": "0.0.1",
  "paths": {
    "pentaho/visual/samples/KPI": "/"
  },
  "config": {
    "pentaho/modules": {
      "pentaho/visual/samples/KPI/Model": {
        "base": "pentaho/visual/Model",
        "annotations": {
          "pentaho/visual/DefaultView": {
            "module": "./View"
          }
        }
      },
      "pentaho/visual/samples/KPI/config": {
        "type": "pentaho/config/spec/IRuleSet"
      }
    }
  }
}

```

This definition configures AMD for the code contained within the package, to be exposed under the module name `pentaho/visual/samples/KPI`. Then, the contained `Model` module is declared to export a value which is a subclass of `pentaho/visual/Model`, the base class of all visualization models. This declaration allows any interested party to discover existing visualizations in the system.

Another important piece of information is the `pentaho/visual/DefaultView` annotation. It states the module identifier of the default view class to use to render a `pentaho/visual/samples/KPI/Model` visualization model. In the Visualization API 3.0, a visualization is composed of a model and a view, which roughly correspond to the previous API’s metadata definition and visualization class.

In Visualization API 3.0, visualizations are not registered with specific applications. Visualizations can be configured to be presented or not in certain applications. Most applications will opt to offer all visualizations registered with the system.

For Visualization API 3.0, a contained `config` module is registered as exporting an instance of `pentaho/config/spec/IRuleSet`, the system type which represents a set of configurations. The next section presents the configuration file.

## Configuration

Some options in the Visualization API 2.0 were specific to Analyzer. Visualization API 3.0 uses the rule-based configuration system, as shown in the following example:

```javascript
// config.js
define({
  rules: [
    {
      select: {
        module: "./Model",
        application: "pentaho/analyzer"
      },
      apply: {
        category: "kpi",
        ordinal: 10001
      }
    },
    {
      select: {
        module: "./Model",
        application: "pentaho/analyzer",
        annotation: "pentaho/analyzer/visual/Options"
      },
      apply: {
        maxValues: [1000, 2000, 3000],
        generateOptionsFromAnalyzerState: function(report) { 
          return {
            backgroundColor: report.reportDoc.getChartOption("backgroundColor")
          };
        }
      }
    }
  ]
});
```

## Converting the visualization class

In Visualization API 2.0, visually rendering the data and handling user interaction was accomplished in the visualization class, as shown in the following sample code:

```javascript
// Define a namespace for this sample to live in.
pentaho.sample = {};

// Define the KPI Class, which renders a single KPI.
pentaho.sample.KPI = function(canvasElement) {
  this.canvasElement = canvasElement;
  this.numSpan = document.createElement("span"); 
  this.numSpan.style.fontSize = "42px"; 
  this.numSpan.style.position = "relative"; 
  this.canvasElement.appendChild(this.numSpan);
};

// Calculate the location of the KPI relative to the canvas.
pentaho.sample.KPI.prototype.resize = function(width, height) { 
  this.numSpan.style.left = ((this.canvasElement.offsetWidth - this.numSpan.offsetWidth) / 2) + 'px'; 
  this.numSpan.style.top = ((this.canvasElement.offsetHeight - this.numSpan.offsetHeight) / 2) + 'px'; 
};

// Render the KPI.
pentaho.sample.KPI.prototype.draw = function(datView, vizOptions) { 
  // Extract the values from the result set.
  var rows = datView.dataTable.jsonTable.rows;
  var dataArray = []; 
  for(var i = 0; i < rows.length; i++){ 
    dataArray.push(rows[i].c[1].v);
  } 

  // Calculate the KPI to display.
  var value = 0; 

  // Note that the vizOptions contains an aggregate option,
  // this is a custom property specific for this visualization type.
  switch(vizOptions.aggregate) { 
    case "MAX": 
      value = Number.MIN_VALUE;
      for(var i = 0; i < dataArray.length; i++) { 
        value = Math.max(value, dataArray[i]); 
      } 
      break;
      
    case "MIN": 
      value = Number.MAX_VALUE;
      for(var i = 0; i < dataArray.length; i++) { 
        value = Math.min(value, dataArray[i]); 
      } 
      break;
      
    case "AVG": 
      var total = 0;
      for(var i = 0; i < dataArray.length; i++) { 
        total += dataArray[i]; 
      } 
      value = total / dataArray.length; 
      break; 
  }
  
  // Update the background color.
  this.canvasElement.style.backgroundColor = vizOptions['myBackgroundColor'];
  
  // Write the KPI value to the screen.
  this.numSpan.innerHTML = value;
  
  this.resize(); 
}

```

In Visualization API 3.0, the visualization class in now defined in the `View.js` file, as shown in the following sample code:

```javascript
// View.js
define([
  "pentaho/visual/impl/View",
  "pentaho/i18n!view"
], function(BaseView, bundle) {

  "use strict";

  return BaseView.extend({

    constructor: function(viewSpec) {

      this.base(viewSpec);

      var numSpan = document.createElement("span");
      numSpan.style.fontSize = "42px";
      numSpan.style.position = "relative";

      this.domContainer.appendChild(numSpan);
    },

    // Called the first time and when more than the size has changed.
    _updateAll: function() {

      var result = this.__calculate();

      this.domContainer.firstChild.innerHTML = bundle.get("result", [result.toFixed(2)]);
      
      // Update the background color.
      this.domContainer.style.backgroundColor = this.model.backgroundColor || "";
      
      this._updateSize();
    },

    // Called when only size has changed.
    _updateSize: function() {

      var element = this.domContainer.firstChild;

      // Center the span
      var width  = this.model.width;
      var height = this.model.height;
      element.style.left = ((width - element.offsetWidth) / 2) + "px";
      element.style.top  = ((height - element.offsetHeight) / 2) + "px";
    },

    // ---------

    __calculate: function() {
      var dataTable = this.model.data;
      var rowCount = dataTable.getNumberOfRows();
      var measureIndex = this.model.measure.fieldIndexes[0];

      var getValue = function(i) {
        var v = dataTable.getValue(i, measureIndex);
        return !isNaN(v) && v != null ? v : null;
      };

      var aggregatedValue = null;
      var rowIndex;
      var value;

      /* eslint default-case: 0 */
      switch(this.model.aggregate) {
        case "max":
          for(rowIndex = 0; rowIndex < rowCount; rowIndex++)
            if((value = getValue(rowIndex)) != null)
              aggregatedValue = aggregatedValue == null ? value : Math.max(aggregatedValue, value);
          break;

        case "min":
          for(rowIndex = 0; rowIndex < rowCount; rowIndex++)
            if((value = getValue(rowIndex)) != null)
              aggregatedValue = aggregatedValue == null ? value : Math.min(aggregatedValue, value);
          break;

        case "avg":
          var total = aggregatedValue = 0;
          if(rowCount) {
            for(rowIndex = 0; rowIndex < rowCount; rowIndex++)
              if((value = getValue(rowIndex)) != null)
                total += value;
            aggregatedValue = total / rowCount;
          }
          break;
      }

      return aggregatedValue;
    }
  });
});

```

This view class is based on the optional base class `pentaho/visual/impl/View`. The base class handles calling the `_updateXyz` protected method whenever the associated model changes, depending on the model properties that have changed. The view reads data and options from the model object, which is available through the model property. If you prefer, you can also directly implement the `pentaho/visual/IView` interface.

## Packaging

With Visualization API 3.0, you now only need to create an NPM-like package and drop it in the special `Karaf deploy` folder.

[Learn more](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation)

## Analyzer and the Visualization API

[Pentaho Analyzer](https://www.hitachivantara.com/en-us/products/big-data-integration-analytics/pentaho-business-analytics.html) displays visualizations that are based on the [Pentaho Visualization API](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp).

Pentaho 8.3 ships with Visualization API 3.0 along with the previous 2.0 version. Analyzer supports visualizations of both API versions, allowing you to convert any custom visualizations made with Visualization API 2.0 to Visualization API 3.0 at your own pace. All stock visualizations, with the exception of the Geo Map, are available in Visualization API 3.0.

* New Pentaho installations are configured to use the stock visualizations for Visualization API 3.0
* Upgrade installations are configured to keep using the previous Visualization API 2.0 stock visualizations.

You can choose which stock visualizations Analyzer uses by configuring an Analyzer setting as described in [Changing the Visualization API version in Analyzer](#changing-the-visualization-api-version-in-analyzer). This setting does not affect Analyzer reports that use a custom (non-stock) visualization. Your custom visualizations will continue to use their related API version.

### Difference between Visualization API 2.0 and 3.0 in Analyzer

The stock visualizations for Visualization API 3.0 are not completely identical to the corresponding visualizations in Visualization API 2.0. Consider the differences listed in each of these categories.

* **Usability and style**
  * Visualizations scroll horizontally and vertically when too many axis categories exist instead of shrinking to available space.
  * Selection is either enabled or disabled, depending on whether gems are present in the Pivot “Column” gem bar. An intermediate selection state no longer exists where partial selections are possible when one gem was in the Pivot “Column” gem bar.
  * General styling of visualizations now aligns across the Pentaho platform.
  * Standard color palettes now align across the Pentaho platform.
* **Cautions**
  * Moving to 3.0, custom visualizations must be manually converted.
  * Visualization configuration in 3.0 is a different process. Existing Analyzer visualization configurations must be migrated. See [Migrating visualization settings in Analyzer](#migrating-visualization-settings-in-analyzer).
  * Custom translations for properties of stock visualizations may no longer work in 3.0.
* **Printing**
  * Printing of scrolled charts shrinks to fit while preserving their aspect-ratio.
  * Printing only reflects custom configurations that are located in the Global Configuration File.

### Changing the Visualization API version in Analyzer

Perform the following steps to change the API version of your stock visualizations:

1. Go to the Analyzer plugin folder, located at `pentaho-server/pentaho-solutions/system/analyzer` and open the `settings.xml` file.
2. Find the **\<viz-api-version>** setting and change its value according to the following desired API version:
   * To use Visualization API 2.0, set **\<viz-api-version>** to `2.0`, as shown below:

     ```xml
     <viz-api-version>2.0</viz-api-version>
     ```
   * To use Visualization API 3.0, set **\<viz-api-version>** to `3.0`, as shown below:

     ```xml
     <viz-api-version>3.0</viz-api-version>
     ```
3. Save the file and restart the Pentaho Server.

### Migrating visualization settings in Analyzer

Visualizations created in Visualization API 2.0 can be configured in Analyzer. You will need to update the `analyzer.properties` file located in the `pentaho-server/pentaho-solutions/system/analyzer` directory.

Visualizations created in Visualization API 3.0 are configured using the [platform-wide JavaScript configuration system](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/configuring-a-visualization-cp-visapi).

You must migrate the following Analyzer visualization settings in Visualizatio API 2.0 to work with Visualization API 3.0:

* **General visualization property example**

  The following example changes the default value of the **Line width** property in **Line chart** visualizations.

  * **Visualization API 2.0**

    in `analyzer.properties`,

    ```
    viz.ccc_line.args.lineWidth=1
    ```
  * **Visualization API 3.0**

    in a platform configuration file,

    ```
    ddefine(function() {
       return [
         {
           select: {
             application: "pentaho/analyzer",
             module: "pentaho/visual/models/Line"
           },
           apply: {
             props: {
               "lineWidth": {defaultValue: 1}
             }
           }
         }
       ];
     });
    ```
* **Maximum values property example**

  The following example changes the maximum number of results possible in the **Bar chart** visualizations.

  * **Visualization API 2.0**

    in `analyzer.properties`,

    ```
    viz.ccc_bar.maxValues=250,500,1000,5000
    ```
  * **Visualization API 3.0**

    in a platform configuration file,

    ```
    define(function() {
       return [
         {
           select: {
             application: "pentaho/analyzer",
             module: "pentaho/visual/models/BarHorizontal",
             annotation: "pentaho/analyzer/visual/Options"
           },
           apply: {
             maxValues: [250, 500, 1000, 5000]
           }
         }
       ];
     });
    ```
* **Chart series colors property example**

  The following example changes the default discrete color palette.

  * **Visualization API 2.0**

    in `analyzer.properties`,

    ```
    chart.series.colors=#0045a1,#5f9e00,#ffc20f,#ff6600,#3c008f

    ```
  * **Visualization API 3.0**

    in a platform configuration file,

    ```
    define(function() {
       return [
         {
           select: {
             application: "pentaho/analyzer",
             module: "pentaho/visual/color/palettes/nominalPrimary"
           },
           apply: {
             colors: [
               "#0045a1","#5f9e00","#ffc20f","#ff6600","#3c008f"
             ]
           }
         }
       ];
     });
    ```

To perform this migration, you need to know the API version correspondence between [visualization identifiers](#visualization-identifiers-in-visualization-api-2.0-and-3.0) and [property values](#visualization-property-values-in-visualization-api-2.0-and-3.0).

### Differences between Visualization API 2.0 and 3.0

The following tables map the differences between the visualization identifiers and property values from Visualization API 2.0 and Visualization API 3.0.

#### Visualization identifiers in Visualization API 2.0 and 3.0

The following table contains differences between the visualization identifiers of Visualization API 2.0 as compared to the identifiers in Visualization API 3.0:

| Visualization ID in API 2.0 | Visualization ID in API 3.0                     | Description         |
| --------------------------- | ----------------------------------------------- | ------------------- |
| `ccc_area`                  | `pentaho/visual/models/AreaStacked`             | Area Stacked        |
| `ccc_line`                  | `pentaho/visual/models/Line`                    | Line                |
| `ccc_bar`                   | `pentaho/visual/models/Bar`                     | Column              |
| `ccc_barstacked`            | `pentaho/visual/models/BarStacked`              | Column Stacked      |
| `ccc_barnormalized`         | `pentaho/visual/models/BarNormalized`           | Column Stacked 100% |
| `ccc_horzbar`               | `pentaho/visual/models/BarHorizontal`           | Bar                 |
| `ccc_horzbarstacked`        | `pentaho/visual/models/BarStackedHorizontal`    | Bar Stacked         |
| `ccc_horzbarnormalized`     | `pentaho/visual/models/BarNormalizedHorizontal` | Bar Stacked 100%    |
| `ccc_barline`               | `pentaho/visual/models/BarLine`                 | Column/Line Combo   |
| `ccc_scatter`               | `pentaho/visual/models/Bubble`                  | X/Y Scatter/Bubble  |
| `ccc_heatgrid`              | `pentaho/visual/models/HeatGrid`                | Heat-Grid           |
| `ccc_pie`                   | `pentaho/visual/models/Pie`                     | Pie                 |
| `ccc_sunburst`              | `pentaho/visual/models/Sunburst`                | Sunburst            |

#### Visualization property values in Visualization API 2.0 and 3.0

The following table contains differences between the visualization property values of Visualization API 2.0 as compared to the property values in Visualization API 3.0:

| Property name     | Example value in API 2.0                                                                                                                                         | Example value in API 3.0 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| labelsOption      | `inside_end`                                                                                                                                                     | `"insideEnd"`            |
| `inside_base`     | `"insideBase"`                                                                                                                                                   |                          |
| `outside_end`     | `"outsideEnd"`                                                                                                                                                   |                          |
| pattern           | `ryg_3`                                                                                                                                                          | `"ryg-3"`                |
| `ryg_5`           | `"ryg-5"`                                                                                                                                                        |                          |
| `blue_3`          | `"blue-3"`                                                                                                                                                       |                          |
| `blue_5`          | `"blue-5"`                                                                                                                                                       |                          |
| lineWidth         | In both 2.0 and 3.0, the number in the properties file passes verbatim to a JSON number value.                                                                   |                          |
| trendLineWidth    |                                                                                                                                                                  |                          |
| emptySlicesHidden | In both 2.0 and 3.0, the value of `true` or `false` in the properties file passes verbatim to a JSON boolean value.                                              |                          |
| reverseColors     |                                                                                                                                                                  |                          |
| colorSet          | In both 2.0 and 3.0, textual values in the properties file are wrapped in quotation marks to form a JSON string value. For example, `circle` becomes `"circle"`. |                          |
| lineLabelsOption  |                                                                                                                                                                  |                          |
| shape             |                                                                                                                                                                  |                          |
| sliceOrder        |                                                                                                                                                                  |                          |
| trendName         |                                                                                                                                                                  |                          |
| trendType         |                                                                                                                                                                  |                          |
