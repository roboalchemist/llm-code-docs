# Source: https://docs.datadoghq.com/dashboards/querying.md

---
title: Querying
description: Query your data to gain insight
breadcrumbs: Docs > Dashboards > Querying
---

# Querying

## Overview{% #overview %}

Whether you are using metrics, logs, traces, monitors, dashboards, notebooks, etc., all graphs in Datadog have the same basic functionality. This page describes querying with the graphic editor. Advanced users can create and edit graphs with JSON. To learn more, see [Graphing with JSON](https://docs.datadoghq.com/dashboards/graphing_json/).

You can query using the graph editor on the Dashboards or Notebooks pages, or you can use **Quick Graphs** available on any page. Open Quick Graphs by pressing `G` on any page. To learn more, see the [Quick Graphs Guide](https://docs.datadoghq.com/dashboards/guide/quick-graphs/).

## Graphing editor{% #graphing-editor %}

On widgets, open the graphing editor by clicking on the pencil icon in the upper right corner. The graphing editor has the following tabs:

- **Share**: Embed the graph on any external web page.
- **JSON**: A more flexible editor, which requires knowledge of the graph definition language.
- **Edit**: The default UI tab for graphing options.

When you first open the graphing editor, you are on the **Edit** tab. Here, you can use the UI to choose most settings. Here is an example:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/references-graphing-edit-window-with-y-2.e2fead6b04aa6c492e75b947ea44b51f.png?auto=format"
   alt="Graphing Edit Tab" /%}

## Configuring a graph{% #configuring-a-graph %}

To configure your graph on dashboards, follow this process:

1. Select the visualization
1. Define the metric
1. Filter your metric
1. Configure the time aggregation
1. Configure the space aggregation
1. Apply function
1. Title the graph

### Select your visualization{% #select-your-visualization %}

Select your visualization from the available [widgets](https://docs.datadoghq.com/dashboards/widgets/).

### Define the metric{% #define-the-metric %}

Choose the metric to graph by searching or selecting it from the dropdown next to **Metric**. If you don't know which metric to use, the metric dropdown provides additional information, including the `unit`, `type`, `interval`, `description`, `tags`, and number of `tag values`.

You may also see Datadog or OpenTelemetry source indicators. If your environment uses both, you can use Datadog's **Semantic Mode** selector to [Query Across Datadog and OpenTelemetry Metrics](https://docs.datadoghq.com/metrics/open_telemetry/query_metrics) in a single graph.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/metric_dropdown.449f537c445abddd9e92e768c897c21e.png?auto=format"
   alt="Metric Selector Dropdown" /%}

Explore your metrics further with the [Metrics Explorer](https://app.datadoghq.com/metric/explorer), a [Notebook](https://app.datadoghq.com/notebook/list), or see a list of metrics on the [Metrics Summary](https://app.datadoghq.com/metric/summary) page.

### Filter{% #filter %}

Your chosen metric can be filtered by host or tag using the **from** dropdown to the right of the metric. The default filter is *(everywhere)*.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/filter-3.951eb67212f9ea09268f61caca4cf512.png?auto=format"
   alt="Filter the graph with the 'from' field, using template variables and boolean logic" /%}

- Use [advanced filtering](https://docs.datadoghq.com/metrics/advanced-filtering/) within the `from` dropdown to evaluate boolean filtered or wildcard filtered queries.
- Filter queries dynamically, using Template Variables. Add the `$` with the tag key and the graph automatically applies the tag you choose in the template variable dropdown. For more information, see the [Template Variable documentation](https://docs.datadoghq.com/dashboards/template_variables/).

To learn more about tags, see the [Tagging documentation](https://docs.datadoghq.com/getting_started/tagging/).

### Aggregate and rollup{% #aggregate-and-rollup %}

#### Aggregation method{% #aggregation-method %}

Aggregation method is next to the filter dropdown. This defaults to `avg by` but you can change the method to `max by`, `min by`, or `sum by`. In most cases, the metric has many values for each time interval, coming from many hosts or instances. The aggregation method chosen determines how the metrics are aggregated into a single line.

#### Configure the time aggregation{% #configure-the-time-aggregation %}

Regardless of the options chosen above, there is always some aggregation of data due to the physical size constraints of the window holding the graph. If a metric is updated every second, and you are looking at 4 hours of data, you need 14,400 points to display everything. Each graph displayed has about 300 points shown at any given time. Therefore, each point displayed on the screen represents 48 data points.

In practice, metrics are collected by the Agent every 15-20 seconds. So one day's worth of data is 4,320 data points. If you display a day's worth of data on single graph, Datadog automatically rolls up the data. For more details on time aggregation, see the [Metrics Introduction](https://docs.datadoghq.com/metrics/#time-aggregation). See the [Rollup](https://docs.datadoghq.com/dashboards/functions/rollup/#rollup-interval-enforced-vs-custom) documentation to learn more about the rollup intervals and how Datadog automatically rolls up data points.

To manually rollup the data, use the [rollup function](https://docs.datadoghq.com/dashboards/functions/rollup/). Click the sigma icon to add a function and select `rollup` from the dropdown menu. Then choose how you want to aggregate the data and the interval in seconds.

This query creates a single line that represents the total available disk space, on average, across all machines rolled up in one minute buckets:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/references-graphing-rollup-example-minutes.7d9c1b4e7eb570db0e906e8f9b4a3275.png?auto=format"
   alt="rollup example of the system.disk.free metric across all machines" /%}

When switching to the JSON view, the query looks like this:

```text
"query": "avg:system.disk.free{*}.rollup(avg, 60)"
```

The full JSON looks like this:

```text
{
    "viz": "timeseries",
    "requests": [
        {
            "formulas": [
                {
                    "formula": "query1"
                }
            ],
            "queries": [
                {
                    "data_source": "metrics",
                    "name": "query1",
                    "query": "avg:system.disk.free{*}.rollup(avg, 60)"
                }
            ],
            "response_format": "timeseries",
            "type": "line",
            "style": {
                "palette": "dog_classic",
                "type": "solid",
                "width": "normal"
            }
        }
    ],
    "yaxis": {
        "scale": "linear",
        "min": "auto",
        "max": "auto",
        "include_zero": true,
        "label": ""
    },
    "markers": []
}
```

For more about using the JSON view, see [Graphing with JSON](https://docs.datadoghq.com/dashboards/graphing_json/).

#### Configure the space aggregation{% #configure-the-space-aggregation %}

Next to the aggregation method dropdown, choose what constitutes a line or grouping on a graph. For example, if you choose `host`, there is a line for every `host`. Each line is made up of the selected metric on a particular `host` aggregated using the chosen method.

Additionally, you can click the tags in the metric dropdown used for defining the metric to group and aggregate your data.

### Nested Queries{% #nested-queries %}

Datadog's nested queries feature allows you to add additional layers of time and/or space aggregation on the results of existing metric queries. This advanced query capability also allows you to compute percentiles and standard deviations on aggregated query results of count/rate/gauge type metrics and access higher resolution queries over historical time frames.

For more information, see the [Nested Queries](https://docs.datadoghq.com/metrics/nested_queries/) documentation.

### Advanced graphing{% #advanced-graphing %}

Depending on your analysis needs, you may choose to apply other mathematical functions to the query. Examples include rates and derivatives, smoothing, and others. See the [list of available functions](https://docs.datadoghq.com/dashboards/functions/#function-types).

Datadog also supports the ability to graph your metrics, logs, traces, and other data sources with various arithmetic operations. Use: `+`, `-`, `/`, `*`, `min`, and `max` to modify the values displayed on your graphs. This syntax allows for both integer values and arithmetic using multiple metrics.

To graph metrics separately, use the comma (`,`). For example, `a, b, c`.

**Note**: Queries using commas are only supported in visualizations, they do not work on monitors. Use [boolean operators](https://docs.datadoghq.com/metrics/advanced-filtering/#boolean-filtered-queries) or arithmetic operations to combine multiple metrics in a monitor.

#### Metric arithmetic using an integer{% #metric-arithmetic-using-an-integer %}

Modify the displayed value of a metric on a graph by performing an arithmetic operation. For example, to visualize the double of a specific metric, click the **Advancedâ¦** link in the graph editor. Then enter your arithmetic in the `Formula` box, in this case: `a * 2`:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/arithmetic_4.1149385306d2e7e1ade42c5450eea1b6.png?auto=format"
   alt="Formula example - multiply" /%}

#### Arithmetic between two metrics{% #arithmetic-between-two-metrics %}

Visualize the percentage of a metric by dividing one metric over another, for example:

```text
jvm.heap_memory / jvm.heap_memory_max
```

Use the **Advancedâ¦** option in the graph editor and select **Add Query**. Each query is assigned a letter in alphabetical order: the first metric is represented by `a`, the second metric is represented by `b`, etc.

Then in the `Formula` box, enter the arithmetic (`a / b` for this example). To display only the formula on your graph, click on the check marks next to the metrics `a` and `b`.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/arithmetic_5.9bec8c5e13c3d3e54e6fce3380c8b006.png?auto=format"
   alt="Formula example - ratio" /%}

Here is another example showing how you can graph the ratio between `error` logs and `info` logs.

```text
status:error / status:info
```

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/arithmetic_6.d03ea7d3a672d242b134d87d1a0703b9.png?auto=format"
   alt="Formula example - logs ratio" /%}

**Note**: Formulas are not lettered. Arithmetic cannot be done between formulas.

#### Minimum or Maximum between two queries{% #minimum-or-maximum-between-two-queries %}

Here is an example using the `max` operator to find the maximum CPU usage between two availability zones.

```text
max(system.cpu.user{availability-zone:eastus-1}, system.cpu.user{availability-zone:eastus-2})
```

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/minmax_metrics_example.f07b8697703d10937353d6cc4a7f3872.png?auto=format"
   alt="Formula example for 'max' showing max count value between two metric queries" /%}

Additionally, you can also calculate the maximum (or minimum) between two queries on different products. Here is another example using the `min` operator to find the minimum between logs with error statuses and warning statuses.

```text
min(status:error, status:warn)
```

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/minmax_logs_platform_example.3e6070a42547b405393f1d204f9a101f.png?auto=format"
   alt="Formula example for 'min' showing min count value between two log queries" /%}

#### Exponentiation{% #exponentiation %}

You can now use the `pow()` function to raise a constant or a metric to the power of another constant or metric. This allows you to model exponential growth or decay.

Here is an example of how to forecast user growth by applying an exponential growth factor to a prior time window:

```text
users.sessions{*} * pow(1.1, timeshift(-1))
```

Here is an example of how to surface anomalies by amplifying value using exponentiation:

```text
pow(ping{region:*}, 2)
```

To use `pow(a, b)`, `a`, and `b` can be constants or metrics. This function is only available on metrics.

### Create an alias{% #create-an-alias %}

You can create a custom alias for your data sources to make it easier for your users to interpret the graph results.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/custom_alias.3c5231edc1ffe4a6f3c7ff5b2349a00c.png?auto=format"
   alt="Custom alias" /%}

### Create a title{% #create-a-title %}

If you do not enter a title, one is automatically generated based on your selections. However, it is recommended that you create a title that describes the purpose of the graph.

### Save{% #save %}

Click **Done** to save your work and exit the editor. You can always come back to the editor to change the graph. If you make changes you don't want to save, click **Cancel**.

## Additional options{% #additional-options %}

### Event overlays{% #event-overlays %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/event_overlay_example.7b8bdf995454a3db2da9bf1d3b2d0e9e.png?auto=format"
   alt="Timeseries widgets showing RUM error rates with deployment events overlaid" /%}

View event correlations by using the **Event Overlays** section in the graphing editor for the [Timeseries](https://docs.datadoghq.com/dashboards/widgets/timeseries/#event-overlay) visualization. In the search field, enter any text or structured search query. Events search uses the [logs search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).

The event overlay supports all data sources. This allows for easier correlation between business events and data from any Datadog service.

With the event overlay, you can quickly see how actions within the organization impact application and infrastructure performance. Here are some example use cases:

- RUM error rates with deployment events overlaid
- Correlating CPU usage with events related to provisioning extra servers
- Correlating egress traffic with suspicious login activity
- Correlating any timeseries data with monitor alerts to ensure that Datadog has been configured with the appropriate alerts

### Split graph{% #split-graph %}

With split graphs, you can see your metric visualizations broken out by tags.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/split_graph_beta.a7234bd927065b96a14b4c2bc1eb4a57.png?auto=format"
   alt="View split graphs of metric container.cpu.usage in the fullscreen widget" /%}

1. Access this feature through the **Split Graph** tab when viewing graphs.
1. You can change the *sort by* metric to see the relationship between the data you are graphing and other metrics.
1. Limit the number of graphs that are displayed by changing the *limit to* value.

## Further Reading{% #further-reading %}

- [Building Better Dashboards](https://learn.datadoghq.com/courses/building-better-dashboards)
