# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/configuring-a-visualization-cp-visapi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/configuring-a-visualization-cp-visapi.md

# Configuring a visualization

Your deployed visualization can be configured by third parties using configuration rules in external configuration files. These configurations are merged with default configurations included with the visualization.

A visualization can be configured by third parties using rules in external configuration files. These configurations are merged with any default configuration included in the visualization. You can create a configuration for your [API](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp) visualization.

Before starting, you should have some basic knowledge about how to configure JavaScript modules on the Pentaho platform and what constitutes a visualization. If not, you should first read [Create a visualization](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi).

Visualizations are comprised of a `Model` type and a `IView` type. You can configure both types. The [Stock visualizations identifiers](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Administer/Pentaho%20developer%20center%20overview/Pentaho%20developer%20center%20overview%20\(cp\)/Platform%20JavaScript%20APIs/Visualization%20API%20cp/Configuring%20a%20visualization%20cp%20\(VisAPI\)/Identifiers%20of%20stock%20visualizations%20\(VisAPI\)=GUID-84134240-3FCF-420C-B741-2B7DA80AFC90=7=en=.md) section contains the list of identifiers for stock model and view types. The [Stock color palettes identifiers](#stock-color-palettes-identifiers) section contains the list of identifiers for stock color palettes.

The following sections show examples of typical model and view type configurations. A single `IRule` object is provided in each example, but it should be interpreted as part of a generic configuration ruleset module, as shown in the folllowing code:

```
define(function(){
  "use strict";
  varruleSpec={/* ... */};
  return{rules:[ruleSpec]};
});
```

## Common model configurations

The following examples are for common model configurations.

* **Example: Hiding a visualization from an application’s visualization list**

  The following rule configures the `isBrowsable` type attribute to hide the stock Pie visualization from [Analyzer](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-analytics.html)'s visualizations menu, which prevents the user from creating new visualizations of this type:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/visual/models/Pie",
      application: "pentaho/analyzer"
    },
    apply: {
      isBrowsable: false
    }
  };
  ```
* **Example: Setting the default line width of a line chart and hiding the property**

  The following rule configures the default value of the **lineWidth** property to be `2` pixels for both the Line and the Column/Line Combo stock visualizations. This rule also hides it from Analyzer’s properties panel, preventing the user from changing its default value:

  ```
  var ruleSpec = {
    select: {
      module: [
        "pentaho/visual/models/Line",
        "pentaho/visual/models/BarLine"
      ],
      application: "pentaho/analyzer"
    },
    apply: {
      props: {
        lineWidth: {
          defaultValue: 2,
          isBrowsable: false
        }
      }
    }
  };
  ```
* **Example: Setting the default shape of points of a line chart**

  The following rule configures the default value of the **shape** property to be the diamond shape for both the Line and the Column/Line Combo stock visualizations:

  ```
  var ruleSpec = {
    select: {
      module: [
        "pentaho/visual/models/Line",
        "pentaho/visual/models/BarLine"
      ]
    },
    apply: {
      props: {
        shape: {
          defaultValue: "diamond"
        }
      }
    }
  };
  ```
* **Example: Changing the menu name of a visualization**

  The following rule changes the `label` type attribute of the Bar stock visualization:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/visual/models/Bar"
    },
    apply: {
      label: "Vertical Bars"
    }
  };
  ```

  **Note:** A best practice is to load localizable text from a resource bundle. See `Localization` API for more details.

## Common view configurations

The views of stock visualizations are implemented using the [CCC](https://community.hitachivantara.com/s/article/community-chart-components) charting library. These views can be customized by specifying their set of extension points in an object of the `extension` configuration property.

**Note:** View configuration is typically tied to the technology with which views are built. You should consult the View documentation of your third-party visualization to find out about which configuration properties are supported.

* **Example: Increase the axes rules of stock visualizations**

  The following sample code illustrates the rule which changes the lineWidth property of the `baseAxisRule_` and `orthoAxisRule_` extension points for stock visualizations in any application:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/ccc/visual/Abstract"
    },
    apply: {
      extension: {
        baseAxisRule_lineWidth: 2,
        orthoAxisRule_lineWidth: 2
      }
    }
  };
  ```
* **Example: Change the font of axes labels in stock visualizations**

  The following sample code illustrates the rule which changes the font property of the `baseAxisLabel_` and `orthoAxisLabel_` extension points for Stacked Area visualizations when in the PDI application:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/ccc/visual/AreaStacked",
      application: "pentaho/det"
    },
    apply: {
      extension: {
        baseAxisLabel_font: "12px OpenSansRegular",
        orthoAxisLabel_font: "12px OpenSansRegular"
      }
    }
  };
  ```

## Common color palette configurations

The following examples are for common color palette configurations.

* **Example: Change the colors of the default palette**

  The following sample code illustrates the rule which changes the `colors` of the default nominal color palette, `pentaho.visual.color.palettes.nominalPrimary`, in any application:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/visual/color/palettes/nominalPrimary"
    },
    apply: {
      colors: [
        "red", "#00FF00", "rgb(0,0,255)"
      ]
    }
  };
  ```
* **Example: Change the colors in a specified visualization**

  The following sample codes illustrates the rule which changes the default value of the **palette** property of the stock bar chart visualization in any application, so that a specific ad hoc palette is used:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/visual/models/Bar"
    },
    apply: {
      props: {
        palette: {
          defaultValue: {
            level: "nominal",
            colors: ["red", "#00FF00", "rgb(0,0,255)"]
          }
        }
      }
    }
  };
  ```
* **Example: Use a registered palette in a specified visualization**

  The following sample code is for when you want to use a registered palette:

  ```
  var ruleSpec = {
    select: {
      module: "pentaho/visual/models/Bar"
    },
    deps: [
      "pentaho/visual/color/palettes/nominalLight"
    ],
    apply: function(nominalLightPalette) {
      return {
        props: {
          palette: {
            defaultValue: nominalLightPalette
          }
        }
      };
    }
  };
  ```

## Stock visualizations identifiers

The models of stock visualizations are all sub-modules of the `pentaho/visual/models` module. For example, `pentaho/visual/models/Line` is the identifier of the stock Line visualization model.

The corresponding CCC-based view of a stock visualization is a sub-module of the `pentaho/ccc/visual` module. For example, `pentaho/ccc/visual/Line` is the identifier of the CCC view corresponding to the stock Line visualization model.

The corresponding Echarts-based view of a stock visualization is a sub-module of the `pentaho/visual/views/echarts`. For example, `pentaho/visual/views/echarts/Funnel` is the identifier of the Echarts view corresponding to the stock Funnel visualization model. The Geo Map visualization is the exception to these rules. Its model’s identifier is `pentaho/geo/visual/Model` and its view’s identifier is `pentaho/geo/visual/View`.

The following table contains identifiers for stock visualizations in Analyzer:

| Local Module ID           | Description              |
| ------------------------- | ------------------------ |
| `Abstract`                | All stock visualizations |
| `AreaStacked`             | Area Stacked             |
| `Line`                    | Line                     |
| `LineStacked`             | Line Stacked             |
| `Bar`                     | Column                   |
| `BarStacked`              | Column Stacked           |
| `BarNormalized`           | Column Stacked 100%      |
| `BarHorizontal`           | Bar                      |
| `BarStackedHorizontal`    | Bar Stacked              |
| `BarNormalizedHorizontal` | Bar Stacked 100%         |
| `BarLine`                 | Column/Line Combo        |
| `Scatter`                 | X/Y Scatter              |
| `Bubble`                  | Bubble                   |
| `HeatGrid`                | Heat-Grid                |
| `Pie`                     | Pie                      |
| `Donut`                   | Donut                    |
| `Sunburst`                | Sunburst                 |
| `Boxplot`                 | Boxplot                  |
| `Dot`                     | Dot                      |
| `Funnel`                  | Funnel                   |
| `Treemap`                 | Treemap                  |
| `Waterfall`               | Waterfall                |
| `Gauge`                   | Gauge                    |
| `Radar`                   | Radar                    |

## Stock color palettes identifiers

All stock color palettes are sub-modules of the `pentaho/visual/color/palettes` module. For example, `pentaho/visual/color/palettes/nominalPrimary` is the identifier of the default discrete color palette.

The following identifiers are for the stock color palettes of the local module:

* `nominalPrimary`
* `nominalNeutral`
* `nominalLight`
* `nominalDark`
* `quantitativeBlue3`
* `quantitativeBlue5`
* `quantitativeGray3`
* `quantitativeGray5`
* `divergentRyb3`
* `divergentRyb5`
* `divergentRyg3`
* `divergentRyg5`
