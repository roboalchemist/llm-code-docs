# Source: https://docs.datadoghq.com/dashboards/guide/wildcard_examples.md

---
title: Wildcard Widget Examples
description: >-
  Explore example visualizations and use cases for Wildcard widgets using
  Vega-Lite to create custom charts.
breadcrumbs: Docs > Dashboards > Graphing Guides > Wildcard Widget Examples
---

# Wildcard Widget Examples

## Overview{% #overview %}

The Wildcard widget provides a powerful way to create custom visualizations in Datadog dashboards using Vega-Lite, a declarative language for creating interactive graphics. This flexibility allows you to build visualizations that go beyond the standard widget offerings, enabling you to represent your data in ways that best suit your specific monitoring and analysis needs.

These examples are designed to showcase the flexibility and power of the Wildcard widget, allowing you to create custom visualizations beyond what's available in standard widgets. Each example includes a description of key features, a visual preview, and the complete Vega-Lite configuration code that you can copy and adapt for your own dashboards.

## Geomap with data transform{% #geomap-with-data-transform %}

The Wildcard widget enables the creation of customized geomaps with advanced data transformation capabilities. This example demonstrates a continental European map that visualizes internet service providers based on log data. The map includes interactive tooltips that display additional provider information when hovering over data points.

**Key features**:

- Custom Albers projection focused on Europe
- Color-coded provider locations
- Interactive tooltips with provider details
- Data sourced directly from log queries

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/geomap_with_data_transform.776f29173534d1748035547e2288851b.png?auto=format"
   alt="Continental European geomap showing internet service provider locations with color-coded markers and interactive tooltips" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/geomap_with_data_transform_config.6a7b09fb815520495b2c3553b7295656.png?auto=format"
   alt="Configuration code for the geomap with data transform example" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```gdscript3
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "projection": {
   "type": "albers",
   "rotate": [
     -12,
     -15,
     0
   ],
   "scale": 700
 },
 "layer": [
   {
     "data": {
       "sphere": true
     },
     "mark": {
       "type": "geoshape",
       "fill": "skyblue"
     }
   },
   {
     "data": {
       "url": "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json",
       "format": {
         "type": "topojson",
         "feature": "countries"
       }
     },
     "mark": {
       "type": "geoshape",
       "fill": "#e0ffd4",
       "stroke": "gray",
       "strokeWidth": 5,
       "strokeOpacity": 0.1,
       "strokeJoin": "round",
       "strokeCap": "round"
     }
   },
   {
     "data": {
       "name": "table1"
     },
     "encoding": {
       "latitude": {
         "field": "attributes.network.client.geoip.location.latitude",
         "type": "quantitative"
       },
       "longitude": {
         "field": "attributes.network.client.geoip.location.longitude",
         "type": "quantitative"
       },
       "color": {
         "field": "attributes.network.client.geoip.as.name",
         "type": "ordinal",
         "title": "Provider",
         "scale": {
           "scheme": "set1"
         }
       }
     },
     "mark": {
       "type": "point",
       "filled": true,
       "opacity": 0.75,
       "size": 200,
       "tooltip": true
     }
   }
 ]
}
```

{% /collapsible-section %}

## Joining data with Reference Tables{% #joining-data-with-reference-tables %}

You can enhance your visualizations by joining Wildcard data queries with [Reference Tables](https://docs.datadoghq.com/reference_tables) to add custom mappings. This example demonstrates log volumes by service, with color coding based on team ownership information from a reference table.

**Key features**:

- Combine operational data with business context
- Create meaningful groupings based on your organization's structure
- Simplify complex relationships with custom mappings
- Enable team-based filtering and analysis

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/bar-chart-with-reference-table.c643f76a9ea475c4c4fafeabd1f669b9.png?auto=format"
   alt="Bar chart showing log data connected with service ownership to show the ability to join with a reference table" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/bar-chart-with-reference-table-config.83c1ce002f765ed4aac1020b33878a6a.png?auto=format"
   alt="Configuration code for the bar chart with reference table example." /%}

{% collapsible-section %}
#### Vega-Lite configuration

```javascript
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "description": "Log volume by team ownership.",
 "data": {
   "name": "table1"
 },
 "mark": "bar",
 "encoding": {
   "x": {
     "field": "service",
     "type": "nominal",
     "title": "Service"
   },
   "y": {
     "field": "query1",
     "type": "quantitative",
     "title": "Log Count",
     "scale": {
       "type": "sqrt"
     }
   },
   "color": {
     "field": "team_name",
     "type": "nominal",
     "title": "Team",
     "scale": {
       "range": [
         "#1f77b4",
         "#ff7f0e",
         "#2ca02c",
         "#d62728",
         "#9467bd",
         "#8c564b",
         "#e377c2",
         "#7f7f7f",
         "#bcbd22",
         "#17becf",
         "#393b79",
         "#637939"
       ]
     }
   },
   "tooltip": [
     {
       "field": "team_name",
       "type": "nominal",
       "title": "Team"
     },
     {
       "field": "query1",
       "type": "quantitative",
       "title": "Log Count"
     }
   ]
 }
}
```

{% /collapsible-section %}

## Multi-metric pie chart with Context Menu{% #multi-metric-pie-chart-with-context-menu %}

The Wildcard widget can create pie charts where each slice represents a different metric or formula using the "fold" transform operator. This approach is particularly useful for visualizing data from integrations like Fastly, where separate metrics are reported for each status code instead of a single metric tagged with different status values.

This example demonstrates how to create a multi-metric pie chart with interactive context menu functionality, allowing users to drill down into specific data points.

**Key features**:

- Combine multiple metrics into a single visualization
- Use the "fold" transform to convert separate queries into pie slices
- Apply custom color schemes to differentiate between data categories
- Enable interactive tooltips for detailed information on hover
- Implement context menu functionality for drill-down analysis

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/multi_metric_pie_chart.f996b0f1331e298cb99f849e6d1d69e9.png?auto=format"
   alt="Multi-metric pie chart with context menu" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/multi_metric_pie_chart_config.09d58ff28ba3783c410585174e783727.png?auto=format"
   alt="Configuration for multi-metric pie chart" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```javascript
{
 "description": "A simple pie chart with multiple scalar queries",
 "encoding": {
   "color": {
     "field": "http\\.status_code",
     "scale": {
       "scheme": "dogcat"
     },
     "type": "nominal"
   },
   "theta": {
     "field": "value",
     "type": "quantitative"
   },
   "tooltip": [
     {
       "field": "http.status_code",
       "type": "nominal"
     },
     {
       "field": "value",
       "type": "quantitative"
     }
   ]
 },
 "transform": [
   {
     "fold": [
       "400",
       "403",
       "404"
     ],
     "as": [
       "http.status_code",
       "value"
     ]
   }
 ],
 "mark": "arc",
 "params": [
   {
     "name": "datadogPointSelection",
     "select": "point"
   }
 ],
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "data": {
   "name": "table1"
 }
}
```

{% /collapsible-section %}

## Multi-layer histogram{% #multi-layer-histogram %}

This example demonstrates how to create a multi-layer histogram that compares error durations against overall trace durations. This visualization is particularly useful for identifying performance bottlenecks by showing how error durations distribute compared to normal operations. By overlaying these distributions, you can identify patterns where errors take significantly longer to process, helping you prioritize which issues to address first based on their performance impact.

**Key features:**

- Uses the `joinaggregate` transform to calculate relative frequencies
- Implements custom tooltips with formatted values
- Configures unit formatting for time measurements (nanoseconds)
- Overlays multiple data series for visual comparison

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/multi_layer_histogram_1.30f7d1f12de3c23853ae072f3e8b80d5.png?auto=format"
   alt="Multi-layer histogram comparing error durations against overall trace durations" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/multi_layer_histogram_config.55f8c8e733885d074913eb752e78ab3b.png?auto=format"
   alt="Configuration for multi-layer histogram visualization" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```javascript
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "config": {
   "customFormatTypes": true
 },
 "encoding": {
   "x": {
     "field": "min",
     "type": "quantitative",
     "axis": {
       "formatType": "hoverFormatter",
       "format": {
         "units": [
           "nanosecond",
           null
         ]
       }
     },
     "title": "duration"
   },
   "x2": {
     "field": "max"
   },
   "y": {
     "field": "relative_frequency",
     "type": "quantitative",
     "title": "Relative Frequency"
   },
   "tooltip": [
     {
       "field": "count"
     },
     {
       "field": "min",
       "formatType": "hoverFormatter",
       "format": {
         "units": [
           "nanosecond",
           null
         ]
       }
     },
     {
       "field": "max",
       "formatType": "hoverFormatter",
       "format": {
         "units": [
           "nanosecond",
           null
         ]
       }
     },
     {
       "field": "relative_frequency",
       "format": "0.3f"
     }
   ]
 },
 "layer": [
   {
     "data": {
       "name": "table2"
     },
     "transform": [
       {
         "joinaggregate": [
           {
             "op": "sum",
             "field": "count",
             "as": "total_count"
           }
         ]
       },
       {
         "calculate": "datum.count / datum.total_count",
         "as": "relative_frequency"
       }
     ],
     "mark": {
       "type": "rect",
       "color": "gray",
       "opacity": 0.8
     }
   },
   {
     "data": {
       "name": "table1"
     },
     "transform": [
       {
         "joinaggregate": [
           {
             "op": "sum",
             "field": "count",
             "as": "total_count"
           }
         ]
       },
       {
         "calculate": "datum.count / datum.total_count",
         "as": "relative_frequency"
       }
     ],
     "mark": {
       "type": "rect",
       "color": "pink",
       "tooltip": {
         "content": "data"
       }
     }
   }
 ]
}
```

{% /collapsible-section %}

## Text color scatterplot{% #text-color-scatterplot %}

Create a customized scatterplot that uses text marks instead of points, with automatic coloring from the Datadog palette. This improves readability by displaying the actual text labels directly on the chart while maintaining the positional data relationships of a traditional scatterplot.

**Key features**:

- Text elements as data points for enhanced readability
- Automatic color assignment using the Datadog color scheme
- Customizable axes for different metrics (p50/p95 in this example)
- Visual encoding that combines position and color for multi-dimensional analysis
- Compact representation of categorical data in a quantitative space

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/text_color_scatterplot.92c77d238ac38987c42671565e216d99.png?auto=format"
   alt="Text-based scatterplot using the Datadog color palette to visualize p50 vs p95 metrics" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/text_color_scatterplot_config.37a80da3afb47f2eb0636e234c56b6dd.png?auto=format"
   alt="Configuration for the scatterplot wildcard widget" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```javascript
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "data": {
   "name": "table1"
 },
 "encoding": {
   "x": {
     "field": "query1",
     "type": "quantitative",
     "axis": {
       "title": "p50"
     }
   },
   "y": {
     "field": "query2",
     "type": "quantitative",
     "axis": {
       "title": "p95"
     }
   },
   "text": {
     "field": "viz"
   },
   "color": {
     "field": "viz",
     "type": "nominal",
     "scale": {
       "scheme": "dogcat"
     }
   }
 },
 "mark": {
   "type": "text"
 }
}
```

{% /collapsible-section %}

## Categorical Heatmap with Time Filtering{% #categorical-heatmap-with-time-filtering %}

This example demonstrates how to create a categorical heatmap that displays data across time and categories with advanced filtering capabilities. Heatmaps help reveal patterns and outliers in multidimensional data, making them ideal for tracking metrics across time and categories.

**Key features**:

- Filter data to exclude zero or negative values
- Use time unit formatting to group temporal data
- Interactive tooltips that display detailed information on hover
- Context menu functionality for drill-down analysis
- Color gradient to represent data intensity

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/categorical_heatmap_1.c6866abc60c5bebf54628f2f40077d9a.png?auto=format"
   alt="Hourly variation of the categorical heatmap showing time-of-day patterns in repository activity" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/categorical_heatmap_config.80e80006702c84733d5e159f81599f5d.png?auto=format"
   alt="Configuration panel for the categorical heatmap showing time and category settings" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```javascript
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "name": "table1"
  },
  "encoding": {
    "x": {
      "title": null,
      "field": "_time",
      "type": "temporal",
      "timeUnit": "utcmonthdate"
    },
    "y": {
      "title": null,
      "field": "_time",
      "type": "temporal",
      "timeUnit": "utchours"
    },
    "color": {
      "field": "result1",
      "type": "quantitative",
      "title": "PRs Closed",
      "scale": {
        "scheme": "blues"
      }
    }
  },
  "mark": {
    "type": "rect",
    "tooltip": {
      "content": "data"
    }
  },
  "transform": [
    {
      "filter": "datum.result1 > 0"
    }
  ]
}
```

{% /collapsible-section %}

## Lollipop Chart{% #lollipop-chart %}

This example demonstrates how to create a lollipop chart to clearly rank items and emphasize their relative values. Lollipop charts are useful for comparing values across categories while reducing visual clutter. By combining the precision of point markers with the visual guidance of lines, they make it easier to scan and compare data than traditional bar chartsâparticularly when working with many categories or when exact value comparisons are important.

**Key features**:

- Enhanced visual ranking compared to traditional toplists
- Combines bar and point marks for improved readability
- Automatic sorting to highlight top/bottom performers
- Custom formatting of axis labels for cleaner presentation
- Visually distinguishes between the rank and the metric value

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/lollipop.6ce994c2ef6f9965a9687c6b78807ec9.png?auto=format"
   alt="Lollipop chart showing ranked CPU usage by team with horizontal lines and endpoint circles for clear visual comparison" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/lollipop_config.8eaf96931c8d079b4ca1fde876dd8584.png?auto=format"
   alt="Configuration panel for creating a lollipop chart showing settings for data sources, sorting, and visual styling" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "data": {
   "name": "table1"
 },
 "description": "A lollipop / dot plot",
 "layer": [
   {
     "encoding": {
       "x": {
         "field": "query1",
         "title": "cpu usage",
         "type": "quantitative"
       },
       "y": {
         "sort": "-x",
         "field": "team",
         "type": "nominal"
       }
     },
     "mark": {
       "type": "rule",
       "color": "#3598eccc"
     }
   },
   {
     "encoding": {
       "x": {
         "field": "query1",
         "title": "cpu usage",
         "type": "quantitative"
       },
       "y": {
         "sort": "-x",
         "field": "team",
         "type": "nominal",
         "axis": {
           "labelExpr": "upper(substring(replace(datum.label, /[-_]/g, ' '), 0, 1)) + lower(substring(replace(datum.label, /[-_]/g, ' '), 1))",
           "labelPadding": 10
         }
       }
     },
     "mark": {
       "type": "point",
       "filled": true,
       "color": "#3598ec",
       "size": 100
     }
   }
 ]
}
```

{% /collapsible-section %}

## Custom Status Text Widget{% #custom-status-text-widget %}

Create a responsive text widget that changes color based on conditional logic applied to your metrics.

This example demonstrates how to create a status widget that displays Firefox usage statistics while conditionally changing color based on a comparison with Safari usage data. The text turns green when Firefox usage is at least 10 times higher than Safari usage, and red otherwise.

**Key features**:

- Conditional text coloring based on threshold comparisons
- Custom text formatting that combines multiple metrics in one display
- Responsive font sizing that adjusts to widget dimensions
- Combined display of both absolute values and percentages
- Data transformation to create derived metrics for decision logic

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/custom_status_text.16b8b507ddd75700886b067622425901.png?auto=format"
   alt="Custom status text widget showing Firefox usage statistics with conditional coloring based on comparison with Safari usage" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/wildcard_examples/custom_status_text_config.42061a96af59dc9b511f484b2812fc3e.png?auto=format"
   alt="Configuration for the custom status text widget" /%}

{% collapsible-section %}
#### Vega-Lite Configuration

```
{
 "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
 "description": "Customize a text display using a transform and conditional coloring",
 "data": {
   "name": "table1"
 },
 "transform": [
   {
     "calculate": "'Firefox: ' + datum.num_firefox + ' of ' + format(datum.num_total, '.3s') + ' (' + format(datum['fraction'], '.0%') + ')'",
     "as": "display_text"
   },
   {
     "calculate": "datum.num_firefox >= 10 * datum.num_safari",
     "as": "is_firefox_ahead"
   }
 ],
 "mark": {
   "type": "text",
   "align": "center",
   "baseline": "middle",
   "fontSize": {
     "expr": "width / 18"
   }
 },
 "encoding": {
   "text": {
     "field": "display_text",
     "type": "nominal"
   },
   "color": {
     "condition": {
       "test": "datum.is_firefox_ahead",
       "value": "rgb(45,195,100)"
     },
     "value": "red"
   }
 }
}
```

{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Learn more about the Wildcard widget](https://docs.datadoghq.com/dashboards/widgets/wildcard)
- [Using Vega-Lite in Wildcard Widgets](https://docs.datadoghq.com/dashboards/guide/using_vega_lite_in_wildcard_widgets)
