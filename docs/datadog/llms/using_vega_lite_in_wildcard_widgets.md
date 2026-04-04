# Source: https://docs.datadoghq.com/dashboards/guide/using_vega_lite_in_wildcard_widgets.md

---
title: Using Vega-Lite with Wildcard Widgets in Datadog
description: >-
  Create advanced custom visualizations using Vega-Lite grammar in Wildcard
  widgets with context menus and interactivity.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > Using Vega-Lite with Wildcard Widgets in
  Datadog
---

# Using Vega-Lite with Wildcard Widgets in Datadog

## Overview{% #overview %}

When using Vega-Lite with Wildcard widgets in Datadog, you'll find extensions to the Vega-Lite specification which are unique to Datadog. This guide outlines the necessary configurations and considerations for effectively using Vega-Lite for data visualization in Datadog, ensuring compatibility with its unique specifications. By understanding and leveraging these specifications, you can create visually appealing and interactive data visualizations that are both effective and responsive to your thematic preferences.

**Note**: Some extensions in Vega-Lite are exclusive to Datadog and might not function in the same way if exported to other tools that have Vega-lite.

## Customizing the theming and color palettes{% #customizing-the-theming-and-color-palettes %}

Datadog provides a range of theming and color palette options to enhance the visual appeal of widgets. You can specify custom colors so that they blend in with the styling choices used by native Datadog widgets. If you set custom colors, the graph will not adjust colors when the app theme changes. By default, Datadog graphs adjust colors for text and axis marks to ensure readable contrast when viewed in dark mode. It's best to avoid setting custom colors for graph axes.

Customized color, font, spacing, and other design settings are available. These settings apply automatically when using the theme switcher (`CTRL + OPT + D`).

### Custom color palette{% #custom-color-palette %}

While you can create custom color palettes using hex codes, using the Datadog color palette ensures automated switching between light and dark modes.

Datadog offers additional color palettes beyond the public Vega color schemes, including:

- `dog_classic_area`
- `datadog16`
- `hostmap_blues`

- [Learn more about Datadog color schemes and themes](https://docs.datadoghq.com/dashboards/guide/widget_colors/)
- [See Vega color schemes](https://vega.github.io/vega/docs/schemes/)

## Customize visualization units{% #customize-visualization-units %}

Datadog offers unit-aware number formatting for [over 150 units](https://docs.datadoghq.com/metrics/units/#unit-list), enabling you to easily format values such as 3600 (seconds) as 1 (hour). To use this feature in your Vega-Lite definition, add the `"config": {"customFormatTypes": true}` parameter to the root of your JSON block.

Next, wherever you set a `format` key, use `formatType: hoverFormatter` and define your units as an array. For example:

{% collapsible-section %}
#### Example Vega-Lite Spec with custom units

```json
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "A simple bar chart with embedded data.",
    "data": {
    "values": [
        {"grade": "A", "total": 28},
        {"grade": "B", "total": 55},
        {"grade": "C", "total": 43}
    ]
    },
    "config": {"customFormatTypes": true},
    "mark": "bar",
    "encoding": {
        "x": {"field": "total", "type": "quantitative"},
        "y": {
            "field": "grade",
            "type": "nominal",
            "axis": {
                "formatType": "hoverFormatter",
                "format": {"units": ["second", null]}
            }
        }
    }
}
```

{% /collapsible-section %}

The second element of the "units" array represents a "per" unit, such as in "bits per second." Units should be provided in singular form (such as, "second" instead of "seconds"). Regular number formatting, such as specifying precision, scientific notation, or integers, is possible using [d3-format](https://d3js.org/d3-format#locale_format) tokens. Two popular formats include:

- `~s`: scientific prefix (for example, 2000 -> 2k), with trailing zeros removed
- `.2f`: floating point to 2 decimals

The `hoverFormatter` may also be called in [Vega expressions](https://vega.github.io/vega/docs/expressions/). This function has the signature of:

```mysql
# `CanonicalUnitName` refers to any of the strings listed as a Datadog unit.

(
   datum: number,
   params?: {
       units?: [CanonicalUnitName, CanonicalUnitName];
   },
)
```

- [Full list of Datadog units](https://docs.datadoghq.com/metrics/units/#unit-list)
- [Vega-Lite format customization](https://vega.github.io/vega-lite/docs/format.html)
- [Vega Expression Language for writing basic formulas](https://vega.github.io/vega/docs/expressions/)

## Responsive sizing{% #responsive-sizing %}

Widgets typically use responsive sizing by default, adjusting automatically to fit the available space. However, you have the option to set a fixed height for each data element, particularly if you want to enable scrolling within a bar chart. Similar to customizing colors, customizing sizing disables automatic responsive sizing.

For example, you can use the following configuration to specify a height increment for each element:

{% collapsible-section %}
#### Example Vega-Lite Spec with custom height

```json
{
    "width": 120,
    "height": 120,
    "data": {"url": "data/cars.json"},
    "mark": "bar",
    "encoding": {
        "x": {
            "field": "Name",
            "scale": {"round": false}
        },
        "y": {"aggregate": "count"}
    }
}
```

{% /collapsible-section %}

## Referencing Datadog Data in Vega-Lite{% #referencing-datadog-data-in-vega-lite %}

In Datadog, each "request" or query corresponds to a Vega [named data source](https://vega.github.io/vega-lite/docs/data.html#named). The numbering for these sources starts at one. This means if your widget makes multiple requests, it generates corresponding datasets named `table1`, `table2`, and so forth.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/using_vega_lite_in_wildcard_widgets/wildcard_multiple_requests.c1c121e8ef636243e9c9efba4d954a83.png?auto=format"
   alt="Example wildcard widget with multiple requests" /%}

Whenever possible, Datadog widgets preserve tag names from your request's "group by" field. For formula and function requests, such as Scalar or Timeseries, "Formula Aliases" are used as field names. For an example, see the [Wildcard widget](https://docs.datadoghq.com/dashboards/widgets/wildcard/#map-datadog-data-to-vega-lite-specifications) documentation.

### Additional Field Information{% #additional-field-information %}

- Timeseries requests include a `_time` field for timestamps in milliseconds.
- Histogram request rows consist of three fields: `start`, `end`, and `count`.
- List request responses vary by data source. Use the [DataPreview](https://docs.datadoghq.com/dashboards/widgets/wildcard/#data-preview) to determine available fields.

### Field names with special characters{% #field-names-with-special-characters %}

Special considerations apply to field names that contain non-alphanumeric characters. Datadog Metrics tags [prohibit most non-alphanumeric characters](https://docs.datadoghq.com/getting_started/tagging/#define-tags). However, not all products have this constraint and they allow characters in attribute names that may have dual meanings in Vega-Lite. These characters include square brackets `[]` and periods `.` which are used to access nested properties in object-shaped data. They need to be escaped because the backend flattens the data before returning it to you for /scalar and /timeseries data.

To ensure these characters are interpreted correctly by the Wildcard widget, you must escape these characters with `\\`. For example, when using the RUM query field `@view.name`, write it as `@view\\.name` in the Vega-Lite specification.

For more information on supported data formats, see the [Wildcard widget](https://docs.datadoghq.com/dashboards/widgets/wildcard/#compatible-data-formats) documentation.

## Context menu and context links{% #context-menu-and-context-links %}

With Datadog widgets, you have the ability to click on a graph datapoint to open a [graph context menu](https://docs.datadoghq.com/dashboards/widgets/#graph-menu) with context links. You can enable this feature on Wildcard widgets by adding specific parameters to your widget's configuration.

To enable the context menu feature, include the following parameters in your Vega-Lite configuration:

```json
"params": [
  {
    "name": "datadogPointSelection",
    "select": "point"
  }
]
```

If the graph contains the `layer` key, the param must be added to one of the layer objects, not to the root of the spec. This is because parameters at the root are applied to all layers, which can cause conflicts. To avoid this, give each layer a uniquely named parameter by prefixing it with`datadogPointSelection_`, such as`datadogPointSelection_squares` or`datadogPointSelection_circles`. For example:

```json
"layer": [
  {
    "mark": "line",
    "encoding": {
      "x": { "field": "_time", "type": "temporal" },
      "y": { "field": "cpu", "type": "quantitative" },
      "color": { "field": "host", "type": "nominal" },
      "opacity": { "value": 0.4 }
    },
    "params": [
      {
        "name": "datadogPointSelection_lines",
        "select": { "type": "point", "on": "click" }
      }
    ]
  },
  {
    "mark": "point",
    "encoding": {
      "x": { "field": "_time", "type": "temporal" },
      "y": { "field": "cpu", "type": "quantitative" },
      "color": { "field": "host", "type": "nominal" },
      "size": { "value": 50 }
    },
    "params": [
      {
        "name": "datadogPointSelection_circles",
        "select": { "type": "point", "on": "click" }
      }
    ]
  }
],
```

After you enable this feature, you can click on datapoints in the widget to open a context menu. Use the graph context menu with the context links of the graph editor. Context links bridge dashboard widgets with other pages in Datadog, as well as the third-party applications you have integrated into your workflows. For more information, see [Context Links](https://docs.datadoghq.com/dashboards/guide/context-links/#context-links-variables).

You can also add dynamic custom links through the [`href` encoding](https://vega.github.io/vega-lite/docs/encoding.html). This is useful if you do not need a full context menu of choices.

## Further reading{% #further-reading %}

- [Learn more about the Wildcard widget](https://docs.datadoghq.com/dashboards/widgets/wildcard/)
- [Wildcard Widget Examples](https://docs.datadoghq.com/dashboards/guide/wildcard_examples)
- [Using Context Links in Dashboards](https://docs.datadoghq.com/dashboards/guide/context-links/#context-links-variables)
