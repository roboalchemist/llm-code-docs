# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/walk-through-tutorial-cp-visapi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/walk-through-tutorial-cp-visapi.md

# Develop a visualization in a sandbox

This walk-through tutorial guides you through the development of a simple bar chart visualization, using the Pentaho Visualization API 3.0 and the [D3](https://d3js.org/) graphics library.

The D3 bar chart sample project is provided as an example of a custom visualization. It uses a `Model` class and an `IView` class created from a third party (`D3.js`) chart. The complete code of this sample is available at [pentaho/pentaho-engineering-samples](https://github.com/pentaho/pentaho-engineering-samples/tree/9.4/Samples_for_Extending_Pentaho/javascript-apis/platform/visual-samples-bar-d3).

Before you begin, you must have a basic understanding of JavaScript and D3 along with the [npm](https://www.npmjs.com/) package manager installed.

## Quick start

If you prefer, you can skip the walk-through tutorial for developing a visualization in a sandbox by getting and building the final Pentaho web project.

1. Make sure that you have `git` and `npm` installed.
2. Clone the repository:

   ```
   git clone https://github.com/pentaho/pentaho-engineering-samples
   cd pentaho-engineering-samples
   git checkout -b 10.2
   ```
3. Navigate to the completed sample directory:

   ```
   cd Samples_for_Extending_Pentaho/javascript-apis/platform/visual-samples-bar-d3
   ```
4. Install the dependencies:

   ```
   npm install
   ```

After building the final Pentaho web project, create its package to prepare for deployment. See [Create the Pentaho web package](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation).

## Walk-through tutorial&#x20;

Perform the following steps of this walk-through tutorial to develop a visualization in a sandbox:

1. [Setting up the sandbox environment](#setting-up-the-sandbox-environment)
2. [Creating the model](#creating-the-model)
3. [Creating the view](#creating-the-view)
4. [Styling the view](#styling-the-view)
5. [Styling the model for applications](#styling-the-model-for-applications)
6. [Adding interactive elements to the view](#adding-interactive-elements-to-the-view)
7. [Adding a default configuration](#adding-a-default-configuration)

### Setting up the sandbox environment

Perform the following steps to set up the sandbox environment for the tutorial:

1. Create the `package.json` file:

   ```
   npm init
   ```
2. Use `@pentaho/visual-samples-bar-d3` as the package name.
3. Accept the default for the other fields.
4. Create a file named `.npmrc` with the Pentaho NPM registry configuration:

   ```
   echo '@pentaho:registry=https://nexus.pentaho.org/repository/group-npm' > .npmrc
   ```
5. Add and install the Visualization API development dependency:

   ```
   npm install @pentaho/visual-sandbox@^3.0.0 --save-dev
   ```

   The runtime dependency is provided by the platform.
6. Install the sandbox:

   ```
   npx init-sandbox
   ```
7. Edit the just created `package.json` file and add the `paths` property to it, to define the root `AMD/RequireJS` module identifier as `pentaho/visual/samples/barD3`:

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     "version": "0.0.1",
        
     "paths": {
       "pentaho/visual/samples/barD3": "/"
     },
        
     "devDependencies": {
       "@pentaho/visual-sandbox": "^3.0.0"
     }
   }
   ```

   **Note:** This tutorial assumes the name `@pentaho/visual-samples-bar-d3` as your package name and the name `pentaho/visual/samples/barD3` as the root AMD/RequireJS module identifier. If you want to use different names, you will have to take care to change all the references to the original names throughout the tutorial.

You should now also have the `sandbox.html` and `sandbox-data.json` files. These files form a minimal sandbox from which sandboxes for specific samples or experiments may be derived. As is, it simply displays the `pentaho/visual/samples/calc` visualization, the only visualization that comes bundled with Visualization API development dependency.

Open each file and get acquainted with it.

#### Inspect your sandbox environment

Perform the following steps to inspect your sandbox environment:

1. Open `sandbox.html` in a browser.

   You should see the result of the average operation: `The result is 1002566.29`. The page shows the simplest visualization, a calculator, which just displays the result of aggregating the values of one column of a dataset.

   **Note:** Directly opening the file through the filesystem will not work when using Google Chrome (and possibly other browsers) because of security restrictions that disallow the loading of local resources using XHR, a functionality that is required by the Visualization API to load localization bundles and other resources.
2. To overcome security restrictions, serve the project files through an HTTP server.

   The following possible solutions are available:

   * **Node**

     ```
     npm install -g node-static
     static -p 8000
     ```
   * **PHP**

     ```
     php -S localhost:8000
     ```
   * **Python 2**

     ```
     python -m SimpleHTTPServer 8000
     ```
   * **Python 3**

     ```
     python -m http.server 8000
     ```
   * **Ruby**

     ```
     ruby -run -e httpd . -p 8000
     ```
3. Open `http://localhost:8000/sandbox.html` in the browser.

### Creating the model

For this tutorial, the model consists of a simple bar chart, which shows the series of the following data pairs:

* category, where each category can only occur in one of the pairs
* measure

Each pair (each category for example) is represented by a bar visual element, and is assigned a section of the horizontal space and all of the vertical space, in which the height of the bar encodes the measure value.

The simplest bar chart has two main data-bound visual degrees of freedom, or, as the Visualization API calls them, visual roles of Category and Measure. The values of the fields mapped to visual roles are visually encoded using visual variables and properties such as position, size, orientation, or color.

#### Completing the model code

You must create model code that performs the following tasks:

* Defines a visualization (model) whose ID is the file’s AMD module identifier (depending on how AMD is configured, it can be, for example: `pentaho/visual/samples/barD3/Model`).
* Inherits directly from the base visualization model, `pentaho/visual/Model`.
* Defines properties of three main types: general, visual roles, and color palettes.
* Automatically applies the configuration of the module to the type by calling the `configure` method.

Perform the following steps to create the model with code developed for this tutorial:

1. Create a file named `Model.js`.
2. Add the following code to `Model.js`:

   ```javascript
   define([
     "pentaho/module!_",
     "pentaho/visual/Model"
   ], function(module, BaseModel) {
     
     "use strict";

     // Create and return the Bar Model class
     return BaseModel.extend({
       $type: {
         id: module.id,
       
         // The label may show up in menus
         label: "D3 Bar Chart",
       
         // Properties
         props: [
           // General properties
           {
             name: "barSize",
             valueType: "number",
             defaultValue: 30,
             isRequired: true
           },
       
           // Visual role properties
           {
             name: "category",
             base: "pentaho/visual/role/Property",
             fields: {isRequired: true}
           },
           {
             name: "measure",
             base: "pentaho/visual/role/Property",
             modes: [{dataType: "number"}],
             fields: {isRequired: true}
           },
       
           // Palette property
           {
             name: "palette",
             base: "pentaho/visual/color/PaletteProperty",
             levels: "nominal",
             isRequired: true
           }
         ]
       }
     })
     .configure();
   });
   ```

#### About the model properties

The bar chart model has the following properties:

* **barSize**

  A general property which determines the constant width of bars. It has a `valueType` of `number`, it is `required` and has a `defaultValue` of 30.

  ```
  specification = {
    name: "barSize",
    valueType: "number",
    defaultValue: 30,
    isRequired: true
  }
  ```
* **category**

  Represents the `Category` visual role. The property is of a special type, a `visual role property`.

  The `data` property, which is inherited from the base visualization model, is given a dataset containing data for fields such as `Product Family` and `Sales`. The value of a visual role contains the names of the fields that are mapped to it, `{fields: ["productFamily"]}` for example. The value of a visual role is an object with a list property named `fields`.

  The `modes` attribute was not specified. It defaults to a single mode of the `"string"` data type. Thus, the visual role will accept being mapped to fields of type `"string"`.

  Because the default data type is `"string"`, the visual role can be mapped to at most one `"string"` field (for it to accept more than one `"string"` field, it would need to have the “list of strings” data type: `["string"]`). However, it is optional by default. To make it required, the special `fields` attribute is configured.

  ```
  specification = {
    name: "category",
    base: "pentaho/visual/role/Property",
    fields: {isRequired: true}
  }
  ```
* **measure**

  Represents the `Measure` visual role. Having a single mode with the `"number"` data type, the visual role accepts a single field of data type `"number"`.

  ```
  specification = {
    name: "measure",
    base: "pentaho/visual/role/Property",
    modes: [{dataType: "number"}],
    fields: {isRequired: true}
  }
  ```
* **palette**

  Represents a color palette. See `pentaho/visual/color/PaletteProperty`.

  The value of the property will default to the highest `ranked` system registered color palette that matches the `level` required by it.

  ```
  specification = {
    name: "palette",
    base: "pentaho/visual/color/PaletteProperty",
    levels: "nominal",
    isRequired: true
  }
  ```

#### Registering the model

You must first register your visualization before displaying it in Pentaho applications like Analyzer and PDI. The visualization is registered when the visualization’s `Model` module is registered with `pentaho/modules`, as a subtype of `pentaho/visual/Model`.

Perform the following steps to register your model:

1. Edit the `package.json` file.
2. Add the `config` property, as shown in the following example:

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     "version": "0.0.1",
     "paths": {
       "pentaho/visual/samples/barD3": "/"
     },
     
     "config": {
       "pentaho/modules": {
         "pentaho/visual/samples/barD3/Model": {
           "base": "pentaho/visual/Model"
         }
       }
     },

     "devDependencies": {
       "@pentaho/visual-sandbox": "^3.0.0"
     }
   }
   ```

#### Additional model metadata

You could enhance your model with additional model metadata, as with the following examples:

* Providing localized labels/descriptions for the name of the visualization and that of its properties. See `Localization`.
* Theming it for certain applications and Pentaho themes.

These modifications are beyond the scope of this tutorial and can be done at a later stage. To display your model on the screen, you must create its view.

### Creating the view

Perform the following steps to create the view for your newly created model:

1. Create a file named `View.js` and add the following code to it:

   ```javascript
   define([
     "pentaho/module!_",
     "pentaho/visual/impl/View",
     "d3"
   ], function(module, BaseView, d3) {
     
     "use strict";

     // Create and return the Bar View class
     return BaseView.extend(module.id, {
       
       _updateAll: function() {
         d3.select(this.domContainer).text("Hello World!");
       }
     });
   });
   ```

   This code performs the following tasks:

   * Identifies the view module as `pentaho/visual/samples/barD3/View`, depending on how `AMD/RequireJS` is configured.
   * Inherits directly from the optional base view class, `pentaho/visual/impl/View`.
   * Renders the visualization with the `_updateAll` method. It will use D3 to output `"Hello World!"` in the view’s DOM element, `domContainer`.
2. Install D3 by executing the following command:

   ```
   npm install d3 --save --save-bundle
   ```

   This command also sets D3 as a bundled dependency.
3. Configure the view as the default by editing `package.json` and adding `DefaultView` annotation to the model type, like in (the `"..."` properties stand for omitted content):

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     
     "...": "...",
     
     "config": {
       "pentaho/modules": {
         "pentaho/visual/samples/barD3/Model": {
           "base": "pentaho/visual/Model",
           "annotations": {
             "pentaho/visual/DefaultView": {
               "module": "./View"
             }
           }
         }
       }
     },
     
     "...": "..."
   }
   ```
4. Adapt the HTML sandbox by editing the `sandbox.html` file and replacing the sandbox construction statement with the following code:

   ```json
   var sandbox = new Sandbox({
     id: "pentaho/visual/samples/barD3/Model",
     spec: {
       "data": new Table(datasets.productSales),
       "category": {fields: ["productFamily"]},
       "measure": {fields: ["sales"]}
     },
     container: "viz_div",
     messages: "msg_div"
   });
   ```

   The visualization model `pentaho/visual/samples/barD3/Model` is now used. Your model contains visual role mappings for the `category` and `measure` visual roles.
5. Refresh the `sandbox.html` page in the browser.

   You should read `Hello World!`.
6. Implement the first part of render code by adapting the following D3 sections in the view’s `_updateAll` code:

   1. In `View.js`, add the `pentaho/visual/scene/Base` dependency to the module:

      ```javascript
      define([
        "pentaho/module!_",
        "pentaho/visual/impl/View",
        "d3",
        "pentaho/visual/scene/Base"
      ], function(module, BaseView, d3, Scene) {
        
        // ...
        
      }
      ```
   2. Replace the code of the `_updateAll` method with the following text:

      ```javascript
      // _updateAll:
      function() {
        // Part 1

        var model = this.model;
        
        var dataTable = model.data;

        var scenes = Scene.buildScenesFlat(this).children;

        var container = d3.select(this.domContainer);
        
        // ...
      }
      ```

   The statement `this.model` gives you access to the visualization model object. The data in the data table needs to be converted into an “array of plain objects” form to directly consumed by D3. The `pentaho.visual.scene.Base` helper class is used to help with the conversion. The value of `this.domContainer` is the DOM element where rendering occurs.
7. Implement the second part of render code in the view’s `_updateAll` code by adding the following D3 code adapted from <https://observablehq.com/@d3/bar-chart>, which is used by the community to share D3 examples:

   ```javascript
   // View.js
   // _updateAll:
   function() {
     // Part 1
     // ...
       
     // Part 2
     container.selectAll("*").remove();
     
     var margin = {top: 50, right: 30, bottom: 30, left: 75};

     var width = model.width - margin.left - margin.right;
     var height = model.height - margin.top - margin.bottom;

     var x = d3.scaleBand().rangeRound([0, width]).padding(0.1);
     var y = d3.scaleLinear().rangeRound([height, 0]);
     
     x.domain(scenes.map(function(scene) { return scene.vars.category.toString(); }));
     y.domain([0, d3.max(scenes, function(scene) { return scene.vars.measure.value; })]);

     var svg = container.append("svg")
       .attr("width", model.width)
       .attr("height", model.height);

     // Title
     var title = this.__getRoleLabel(model.measure) + " per " + this.__getRoleLabel(model.category);

     svg.append("text")
       .attr("class", "title")
       .attr("y", margin.top / 2)
       .attr("x", model.width / 2)
       .attr("dy", "0.35em")
       .attr("text-anchor", "middle")
       .text(title);

     // Content
     var g = svg.append("g")
       .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
         
     // X axis
     g.append("g")
       .attr("class", "axis axis-x")
       .attr("transform", "translate(0," + height + ")")
       .call(d3.axisBottom(x));
     
     // Y axis
     g.append("g")
       .attr("class", "axis axis-y")
       .call(d3.axisLeft(y).ticks(10));
     
     // Bars
     var bandWidth = x.bandwidth();
     var barWidth = Math.min(model.barSize, bandWidth);
     var barOffset = bandWidth / 2 - barWidth / 2 + 0.5;

     var selectColor = function(scene) {
       return model.palette.colors.at(scene.index % model.palette.colors.count).value;
     };

     var bar = g.selectAll(".bar")
       .data(scenes)
       .enter().append("rect")
       .attr("class", "bar")
       .attr("fill", selectColor)
       .attr("stroke", selectColor)
       .attr("x", function(scene) { return x(scene.vars.category.toString()) + barOffset; })
       .attr("y", function(scene) { return y(scene.vars.measure.value); })
       .attr("width", barWidth)
       .attr("height", function(scene) { return height - y(scene.vars.measure.value); });
   }
   ```

   The model dimensions are now available through `model.width` and `model.height`. The dynamic chart title is built with the help of the `__getRoleLabel` method, which is introduced in the next step. The model’s `barSize` property is used to limit the width of bars. The scene objects, previously built by the `pentaho.visual.scene.Base` helper class, contain variables, one for each visual role. Each variable has a value and a formatted value, which is obtained by calling the variable’s `toString` method. Scene objects have an `index` property which is being used to cycle through and select each bar’s color from the `palette` property.
8. Implement the final part of render code in the view’s `__getRoleLabel` by adding the `__getRoleLabel` property after `_updateAll` and inserting the following code:

   ```
   // View.js
   // __getRoleLabel: 
   function(mapping) {

     if(!mapping.hasFields) {
       return "";
     }

     var data = this.model.data;

     var columnLabels = mapping.fieldIndexes.map(function(fieldIndex) {
       return data.getColumnLabel(fieldIndex);
     });

     return columnLabels.join(", ");
   }
   ```

   The visual role mapping object’s `fieldIndexes` property conveniently gives you the indexes of the `fields` mapped to a visual role. The label of a field is obtained from the data table’s `getColumnLabel` method.
9. Refresh the `sandbox.html` page in the browser.

   You should see a bar chart.

### Styling the view

You can add CSS classes to style elements with a view.

Perform the following steps to style the elements of the bar chart with CSS classes:

1. Create the CSS file:

   1. Create a folder named `css`.
   2. In the new `css` folder, create a file named `View.css`.
   3. Add the following code to the new `View.css` file:

      ```css
      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .bar {
        stroke-width: 2px;
      }

      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .bar:hover {
        fill-opacity: 0.8;
      }

      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .axis path,
      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .tick line {
        stroke: #cbdde8;
      }

      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .tick text {
        font-family: OpenSansLight, Helvetica, Arial, Sans serif;
        fill: #26363d;
      }

      ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .title {
        font-family: OpenSansLight, Helvetica, Arial, Sans serif;
        font-size: 18px;
        font-style: normal;
        fill: #005f7d;
      }
      ```

   The CSS rules are scoped with the visualization model’s automatically generated CSS class. The CSS class is composed by the hyphenated package name and AMD module identifier of the model type. See `pentaho.visual.util.getCssClasses`, for more information on the structure of the CSS class names.
2. In the `package.json` file, declare the `pentaho/visual/samples/barD3/View` module.

   Its base class is not relevant.
3. Add the `ThemeAnnotation` annotation to the `package.json` file, reference the just-created `View.css` file:

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     
     "...": "...",
     
     "config": {
       "pentaho/modules": {
       
         "...": "...",
         
         "pentaho/visual/samples/barD3/View": {
           "base": null,
           "annotations": {
             "pentaho/theme/Theme": {
               "main": "css!./css/View"
             }
           }
         }
       }
     },
     
     "...": "..."
   }
   ```

   When a view supports CSS theming, it is its responsibility to automatically load any registered themes whenever the view module is loaded.
4. In the `package.json` file, add the `LoadThemeAnnotation` annotation to the view module:

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     
     "...": "...",
     
     "config": {
       "pentaho/modules": {
       
         "...": "...",
         
         "pentaho/visual/samples/barD3/View": {
           "base": null,
           "annotations": {
             
             "...": "...",
             
             "pentaho/theme/LoadTheme": {}
           }
         }
       }
     },
     
     "...": "..."
   }
   ```
5. Refresh the `sandbox.html` page in the browser.

You should see a better styled title and hover effects on the bars.

### Styling the model for applications

When you see your visualization in [Analyzer](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-analytics.html) or [PDI](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-data-integration.html), it will be displayed with “generic visualization” icon:

* **In Analyzer**

  The canvas displays a placeholder image of a generic sunburst visualization:

  ![Generic placeholder image in Analyzer for VisAPI walk-through](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-3b6cc1d1e6f5c763e000ad9ad7a16e3aadacd5dc%2Fsample-bar-d3-analyzer-placeholder-unstyled.png?alt=media)
* **In PDI**

  Each tab has a visualization menu which displays a button icon, a larger two-states icon in the menu’s drop-down and a placeholder image displayed in the canvas. All of these display will be a generic visualization image:

  ![Generic placeholder image in the PDi client for VizAPI walk-through](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-c79571e420e47b8bb91f16d0b91ede5d170d695e%2Fsample-bar-d3-pdi-menu-selected-unstyled.png?alt=media)

Visualization container applications document how visualizations can provide styled content to better integrate with them. You can use custom images for the Analyzer and PDI scenarios by creating and registering a single CSS stylesheet as a theme for the visualization model file. Container application loads any registered visualization model themes.

Perform the following steps to create and register a CSS stylesheet:

1. In the `css` folder, create a file named `Model.css`.
2. Add the following code to the new model CSS file:

   ```css
   /* -- Analyzer -- */

   /* Canvas placeholder image */
   ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-Model.component-icon-landscape {
     background-image: url("./images/analyzer-bar-d3-placeholder.png");
   }

   /* -- PDI -- */

   /* Viz Type Selector - Selected Viz Button */
   ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-Model.visualization-switcher-button-icon {
     background-image: url("./images/pdi-bar-d3-button.svg");
   }

   /* Viz Type Selector - Drop-down icons */
   .visualization-selector ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-Model.component-icon-sprite {
     background-image: url("./images/pdi-bar-d3-sprite.svg");
   }

   /* Canvas placeholder image */
   ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-Model .canvas.message .icon {
     background-image: url("images/pdi-bar-d3-placeholder.svg");
   }
   ```

   The CSS rules are scoped with the visualization model’s automatically generated CSS class, similarly to how you styled the view.
3. Copy the images provided in `pentaho/pentaho-engineering-samples` into an `images` folder, inside of the `css` folder.
4. In the `package.json` file, in the `pentaho/visual/samples/barD3/Model` module declaration, add the `ThemeAnnotation` annotation, referencing the just-created `Model.css` file:

   ```css
   {
     "name": "@pentaho/visual-samples-bar-d3",
     
     "...": "...",
     
     "config": {
       "pentaho/modules": {
         "pentaho/visual/samples/barD3/Model": {
           
           "...": "...",
           
           "annotations": {
             
             "...": "...",
         
             "pentaho/theme/Theme": {
               "main": "css!./css/Model"
             }
           }
         },
         
         "...": "...",
       }
     },
     
     "...": "..."
   }
   ```

You can test the CSS stylesheet later, when deploying the visualization to the Pentaho Server and to PDI.

### Adding interactive elements to the view

You can add interactive elements to your visualization. The Visualization API 3.0 defines two standard types of actions: `Execute` and `Select`. Visualization API 3.0 `data actions` carry information that identifies the visual element with which the user interacted in terms of the subset of data that it visually represents. The interaction is conveyed in the `dataFilter` property.

In this tutorial, because each bar represents a category of the data, and the `Category` visual role is mapped to a single field, then each bar corresponds to a distinct value of the mapped field.

#### Implementing the Execute action

The `Execute` action is typically performed in response to a double-click event on the main visual elements, in this case, the bars.

Perform the following steps to to add the `clickD3.js` dependency and hande the `dblclick` event.

1. Modify the `AMD/RequireJS` module declaration of the `View.js` file to the following:

   ```javascript
   define([
     "pentaho/module!_",
     "pentaho/visual/impl/View",
     "d3",
     "pentaho/visual/scene/Base",
     "./clickD3"
   ], function(module, BaseView, d3, Scene, d3ClickController) {
     // ...
   });
   ```
2. Place the `clickD3.js` file from `pentaho/pentaho-engineering-samples` besides the `View.js` file.

   This file provides a click controller for D3 that handles the correct distinction between click and double-click events.
3. Add the following code to the `_updateAll` method to handle the `dblclick` event of the bar elements:

   ```javascript
   // View.js
   // _updateAll:
   function() {
     // Part 1 & 2
     // ...
     
     // Part 3
     var cc = d3ClickController();
     bar.call(cc);
       
     cc.on("dblclick", function(event, scene) {
       // A filter that selects the data that the bar visually represents
       var filter = scene.createFilter();
       
       // Dispatch an "Execute" action through the model
       model.execute({dataFilter: filter});
     });
   }
   ```

   The `scene` object now knows how to create a filter for the data it represents (see `createFilter` for more information). The `execute` method creates and dispatches an execute action through the model, where action listeners can handle it.
4. Refresh the `sandbox.html` page in the browser, and double-click a bar.

#### Implementing the Select action

The `Select` action is an auxiliary action. Its goal is to mark a subset of data on which a later, real action (such as drilling-down) is performed. The current set of selected data is stored in the model’s `selectionFilter` property. For each `Select` action that is performed, its `dataFilter` may be removed from, be added to, replace, or toggled in the model’s current `selectionFilter` according to the action’s `selectionMode`.

Visualizations typically highlight visual elements that represent data that is selected. Container applications typically expose actions to be performed on the currently selected subset of data. Bars are set up as selected by clicking on them.

Perform the following steps to implement the `Select` action.

1. Add the following code to the `_updateAll` method to handle the click event of the bar elements:

   ```javascript
   // View.js
   // _updateAll:
   function() {
     // Part 1 & 2 & 3
     // ...
     
     // Part 4
     cc.on("click", function(event, scene) {
       // A filter that selects the data that the bar visually represents
       var filter = scene.createFilter();
       
       // Dispatch a "Select" action through the model
       model.select({
         dataFilter: filter,
         selectionMode: event.ctrlKey || event.metaKey ? "toggle" : "replace"
       });
     });
   }
   ```

   Each time a bar is clicked, the current model’s `selectionFilter` is `replaced` with the data filter associated with the clicked bar, or `toggled` if the ctrl/cmd key is pressed.
2. Refresh the `sandbox.html` page in the browser, and click a bar.

   You should see a text under the visualization showing the selected data’s filter.
3. Edit the `View.css` file and append the following rules to it:

   ```css
   ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .bar.selected {
     stroke-opacity: 0.4;
     fill-opacity: 0.6;
   }

   ._pentaho-visual-samples-bar-d3-pentaho-visual-samples-bar-D3-View .bar.selected:hover {
     stroke-opacity: 0.8;
   }
   ```
4. Add the following code to the `_updateAll` method to change the render code:

   ```css
   // View.js
   // _updateAll:
   function() {
     // Part 1 & 2 & 3 & 4
     // ...
     
     // Part 5
     bar.classed("selected", function(scene) {
       var selectionFilter = model.selectionFilter;
       return !!selectionFilter && dataTable.filterMatchesRow(selectionFilter, scene.index);
     });
   }
   ```
5. Refresh the `sandbox.html` page in the browser, and click a bar.

   You should see the selected bar exhibiting different colors.

### Adding a default configuration

While all visualization container applications should be able to use any visualization, you may need configurations between a visualization and an application to improve their integration.

For example, when a visualization named `V1` is developed, an application named `A1` is already in use and has a custom feature that is not part of the standard container application interface, a developer may have to package `V1` with a configuration module to better integrate with the out-of-the-box version of `A1`.

**Note:** If you do not have any knowledge about JavaScript configuration in the Pentaho Platform, you might want to read [Configuring a visualization](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/configuring-a-visualization-cp-visapi) before continuing.

Perform the following steps to create and add a default configuration file:

1. Create a configuration file named `config.js`, and add the following content in it:

   ```javascript
   define(function() {
     
     "use strict";
     
     return {
       rules: [
         // Sample rule
         {
           priority: -1,
           select: {
             module: "./Model"
           },
           apply: {
             props: {
               barSize: {defaultValue: 50}
             }
           }
         }
       ]
     };
   });
   ```

   This configuration is applied to the bar visualization model type in any application, has a lower-than-default-priority, and changes the default value of the **barSize** property to 50 pixels. For now, this configuration only serves to prove that the configuration actually works. You will to verify that the configuration works in the sandbox environment.
2. In the `package.json` file, declare the `pentaho/visual/samples/barD3/config` module as a ruleset module to register the configuration module with the configuration system:

   ```json
   {
     "name": "@pentaho/visual-samples-bar-d3",
     
     "...": "...",
     
     "config": {
       "pentaho/modules": {
       
         "...": "...",
         
         "pentaho/visual/samples/barD3/config": {
           "type": "pentaho/config/spec/IRuleSet"
         }
       }
     },

     "...": "..."
   }
   ```
3. Refresh the `sandbox.html` page in the browser.

   You should see a bar chart with wider bars.
4. Specify the **keepLevelOnDrilldown** configuration property to force replacing the parent field with the child field to allow drilling-down by adding a `pentaho/analyzer/visual/OptionsAnnotation` annotation to the visualization model, via a configuration rule:

   ```
   // config.js
   define(function() {
     
     // ...
     
     return {
       rules: [
         
         // ...
         
         {
           priority: -1,
           select: {
             module: "./Model",
             annotation: "pentaho/analyzer/visual/Options",
             application: "pentaho/analyzer"
           },
           apply: {
             keepLevelOnDrilldown: false
           }
         }
       ]
     };
   });
   ```

   **Note:** When drilling-down in [Analyzer](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-analytics.html), the default behaviour is to add the child field to the visual role after the parent field. The Category visual role of the bar visualization you developed only accepts a single field being mapped to it, which results in Analyzer not allowing you to drill-down. You can configure the Analyzer-specific metadata property, **keepLevelOnDrilldown**, to force replacing the parent field with the child field to allow drilling-down.

   This rule has no effect when testing your visualization in the sandbox environment, but is important if you package your visualization for deployment.

With the default configuration in place, you can now package your visualization in a Pentaho web package to prepare for deployment. See [Create the Pentaho web package](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation) for further instructions.
