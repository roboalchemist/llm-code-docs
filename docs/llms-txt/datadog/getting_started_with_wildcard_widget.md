# Source: https://docs.datadoghq.com/dashboards/guide/getting_started_with_wildcard_widget.md

---
title: Getting Started with the Wildcard Widget
description: >-
  Learn to build custom visualizations using the Wildcard widget with Vega-Lite
  grammar and imported queries.
breadcrumbs: Docs > Dashboards > Graphing Guides > Getting Started with the Wildcard Widget
---

# Getting Started with the Wildcard Widget

## Overview{% #overview %}

The Wildcard widget is a powerful and flexible visualization tool in Datadog that lets you build custom visual representations using the [Vega-Lite grammar](https://vega.github.io/vega-lite/).

### Tutorial Objectives{% #tutorial-objectives %}

By the end of this tutorial, you will be able to:

- Use Vega-Lite concepts to define visualizations in Wildcard widgets.
- Import a query from an existing widget.

### Prerequisites{% #prerequisites %}

- A Datadog account with access to [Notebooks](https://app.datadoghq.com/notebook/list) or [Dashboards](https://app.datadoghq.com/dashboard/lists?p=1).
- You have telemetry such as APM trace data or request duration metrics.
- You are familiar with basic Datadog widgets and dashboards and can [add a widget and edit it](https://docs.datadoghq.com/dashboards/widgets/wildcard/#setup).

## Step 1: Import an existing query{% #step-1-import-an-existing-query %}

Rather than starting from scratch, import a request from an existing widget. Copy the query from a widget you're interested in exploring further (such as a Top List). To get started, you can use widgets from your [prebuilt dashboards](https://app.datadoghq.com/dashboard/lists/preset/3?p=1).

1. Navigate to an existing dashboard with a useful widget (Top List of database queries).
1. Use the widget menu or use the keyboard shortcut (`Ctrl`/`CMD` + `C`) to copy the widget.
1. In a new dashboard, add a Wildcard widget.
1. In the editor, clear the default query ().
1. Paste the copied request with `Ctrl`/`Cmd` + `V`. The query and associated fields carry over automatically.

{% video
   url="https://datadog-docs.imgix.net/images//dashboards/guide/analyze_p50_vs_p95_latency_with_the_wildcard_widget/import_widget_walkthrough.mp4" /%}

## Step 2: Refine the query{% #step-2-refine-the-query %}

In the query editor:

1. Expand the **Data Preview** to identify the fields returned from the query.
1. Next to your query, click **As** to add an alias to your query. This adds clarity, for example, rename `p50:trace.http.request{*} by {service}`â `p50`.

{% video
   url="https://datadog-docs.imgix.net/images//dashboards/guide/analyze_p50_vs_p95_latency_with_the_wildcard_widget/refine_query_walkthrough.mp4" /%}

## Step 3: Auto-generate a visualization{% #step-3-auto-generate-a-visualization %}

At the top of the query editor:

1. Click the **Define Visual** tab.
1. Press `Cmd` + `Shift` + `P` (Mac) or `Ctrl` + `Shift` + `P` (Windows/Linux) to open the **Command Palette**.
1. Select **Auto-select chart**.

{% video
   url="https://datadog-docs.imgix.net/images//dashboards/guide/analyze_p50_vs_p95_latency_with_the_wildcard_widget/command_palette.mp4" /%}

Datadog automatically creates a visualization based on your query.
Use the Command Palette (`Cmd` + `Shift` + `P`) to auto-select a chart type based on your query, add or edit encodings, or rotate axes/switch chart types.
{% collapsible-section %}
#### Guided example of Auto-generate

1. In a new Wildcard widget, click the JSON tab of the query editor and paste the following query:
   ```json
   {
     "response_format": "scalar",
     "queries": [
       {
         "query":       "avg:system.cpu.user{*} by {env}",
         "data_source": "metrics",
         "name":        "query1",
         "aggregator":  "last"
       },
       {
         "query":       "max:system.cpu.user{*} by {env}",
         "data_source": "metrics",
         "name":        "query2",
         "aggregator":  "last"
       }
     ],
     "formulas": [
       { "formula": "query1" },
       { "formula": "query2" }
     ],
     "sort": {
       "count": 15,
       "order_by": [
         {
           "type":   "formula",
           "index":  0,
           "order":  "desc"
         }
       ]
     }
   }
   ```
1. Click **Save Edits**.
1. At the top of your query editor, click the **Define Visual** tab.
1. Press `Cmd` + `Shift` + `P` (Mac) or `Ctrl` + `Shift` + `P` (Windows/Linux) to open the **Command Palette**.
1. Select **Auto-select chart**. The graph should automatically change from a bar chart to a scatterplot.

{% /collapsible-section %}

## Step 4: Add a context menu{% #step-4-add-a-context-menu %}

To add interactivity to your graph, enable context menu support.

1. In the visual JSON editor, copy and paste the following example bar chart widget to see how to add a context menu. This example includes a Tooltip and Context Menu configurations.
   ```json
   {
     "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
     "description": "Bar chart showing CPU usage by environment with Datadog context menu support",
     "data": {
    "name": "table1"
     },
     "mark": "bar",
     "encoding": {
    "x": {
      "field": "env",
      "type": "nominal",
      "sort": "-y",
      "title": "Environment"
    },
    "y": {
      "field": "query1",
      "type": "quantitative",
      "title": "CPU Usage (%)"
    },
    "tooltip": [
      {
        "field": "env",
        "type": "nominal"
      },
      {
        "field": "query1",
        "type": "quantitative",
        "title": "CPU Usage (%)"
      },
      {
        "field": "timestamp",
        "type": "temporal",
        "title": "Timestamp"
      }
    ]
     },
     "params": [
    {
      "name": "datadogPointSelection",
      "select": "point"
    }
     ]
   }
```
1. Run and save the widget.
1. On your dashboard, find the widget you just created and click any data point in graph to bring up a **context menu**.

For more information, see [Using Vega-Lite with Wildcard Widgets in Datadog](https://docs.datadoghq.com/dashboards/guide/using_vega_lite_in_wildcard_widgets/#context-menu-and-context-links).

## Next Steps{% #next-steps %}

Wildcard widgets support a wide range of customizations, including:

- [Adjusting the thickness of lines to show weight and intensity](https://vega.github.io/vega-lite/examples/trail_color.html)
- [Adding images to visually represent values](https://vega.github.io/vega-lite/examples/isotype_bar_chart_emoji.html)
- [Layering visualizations for richer context](https://vega.github.io/vega-lite/examples/layer_line_rolling_mean_point_raw.html)

For more inspiration, see [Datadog Wildcard widget examples](https://docs.datadoghq.com/dashboards/guide/wildcard_examples/) and [Vega-Lite Examples](https://vega.github.io/vega-lite/examples/).

## Further reading{% #further-reading %}

- [Wildcard widget Overview](https://docs.datadoghq.com/dashboards/widgets/wildcard/)
- [Wildcard widget example visualizations](https://docs.datadoghq.com/dashboards/guide/wildcard_examples/)
- [Using Vega-Lite in Wildcard widgets](https://docs.datadoghq.com/dashboards/guide/using_vega_lite_in_wildcard_widgets/)
