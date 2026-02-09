# Source: https://docs.datadoghq.com/dashboards/widgets/timeseries.md

---
title: Timeseries Widget
description: >-
  Display the evolution of one or more metrics, log events, indexed spans, or
  process metrics over time.
breadcrumbs: Docs > Dashboards > Widgets > Timeseries Widget
---

# Timeseries Widget

The timeseries visualization allows you to display the evolution of one or more metrics, log events, or Indexed Spans over time. The time window depends on what is selected on the [timeboard](https://docs.datadoghq.com/dashboards/#get-started) or [screenboard](https://docs.datadoghq.com/dashboards/#screenboards):

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/timeseries/timeseries.46b7f2b3b54f4895304e060bea9ecdc4.png?auto=format"
   alt="A timeseries widget showing the average system.cpu.user for a host" /%}

## Setup{% #setup %}

### Configuration{% #configuration %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/timeseries/timeseries_setup.fca27d0acac3c0b970115c08793fd6b2.png?auto=format"
   alt="Timeseries setup" /%}

1. Choose the data to graph:

   - Metric: See the [Querying documentation](https://docs.datadoghq.com/dashboards/querying/) to configure a metric query.
   - Indexed Spans: See the [Trace search documentation](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#search-bar) to configure an Indexed Span query.
   - Log Events: See the [Log search documentation](https://docs.datadoghq.com/logs/search_syntax/) to configure a log event query.

1. Customize your graph with the available options.

## Display options{% #display-options %}

Graphs can be displayed as lines, areas, and bars. Datadog graphs aggregate data over [intervals](https://docs.datadoghq.com/dashboards/functions/rollup/) such as sum every hour. By default, the last incomplete time interval in a timeseries graph is shaded and labeled as "partial data".

Line graphs contain additional parameters:

| Parameter | Options                  |
| --------- | ------------------------ |
| Style     | Solid, dashed, or dotted |
| Stroke    | Normal, thin, or thick   |

### Color{% #color %}

For all graph types, Datadog offers various color options to differentiate multiple metrics displayed on the same graph:

| Palette    | Description                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| Classic    | The simple colors light blue, dark blue, light purple, purple, light yellow, and yellow (colors repeat).            |
| Consistent | Using a set of 16 colors, applies a consistent color for each series of data across all widgets for each tag group. |

For line graphs, different metrics can be assigned specific palettes by separating the queries in JSON. For more information, see the guide for [Selecting the right colors for your graphs](https://docs.datadoghq.com/dashboards/guide/widget_colors/).

### Sorting{% #sorting %}

Order the graph by **Tags** or by **Values** to sort timeseries legends and stacked graphs. This only sorts the graph visualization, and does not impact the query. Toggle the **Reverse** option to sort by reverse alphabetical order or by descending values.

### Metric aliasing{% #metric-aliasing %}

Each query or formula, along with any [filtering tags](https://docs.datadoghq.com/dashboards/querying/#filter), can be aliased. The alias overrides the display on the graph and legend, which is useful for long metric names or long lists of filters. At the end of your query or formula, click on **asâ¦** and enter your metric alias:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/timeseries/metric_alias.f4aac6d2f2065e782583c7dcc5448c03.png?auto=format"
   alt="Adding an alias to a search query in the Timeseries widget editor" /%}

### Event overlay{% #event-overlay %}

The event overlay supports all data sources. This allows for easier correlation between business events and data from any Datadog service.

With the event overlay, you can see how actions within the organization impact application and infrastructure performance. Here are some example use cases:

- RUM error rates with deployment events overlaid
- Correlating CPU usage with events related to provisioning extra servers
- Correlating egress traffic with suspicious login activity
- Correlating any timeseries data with monitor alerts to ensure that Datadog has been configured with the appropriate alerts

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/querying/event_overlay_example.7b8bdf995454a3db2da9bf1d3b2d0e9e.png?auto=format"
   alt="Timeseries widgets showing RUM error rates with deployment events overlaid" /%}

You can add events from related systems to add more context to your graph, such as GitHub commits, Jenkins deploys, and Docker creation events. Click **Add Event Overlay** in the **Event Overlays** section and enter a query to display those events.

Use the same query format as for the [Event Explorer](https://docs.datadoghq.com/events/), for example:

| Query                       | Description                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `sources:jenkins`           | Shows all events from the Jenkins source.                                                                          |
| `tag:role:web`              | Shows all events with the `role:web` tag.                                                                          |
| `tags:$<TEMPLATE_VARIABLE>` | Shows all events from the selected [template variable](https://docs.datadoghq.com/dashboards/template_variables/). |

### Markers{% #markers %}

To add markers for additional data sets, click **Add Marker** in the **Markers** section.

1. Select a Line or Range and input a value or a range or values.
1. In the **Show as** field, select an alerting status/color and choose from a solid, bold, or dashed horizontal line.
1. To add a label that displays on the bottom left of the timeseries widget, define a value for the Y-Axis and click the **Label** checkbox.

### Y-Axis controls{% #y-axis-controls %}

Y-axis controls are available in the UI and in the JSON editor. You can set the value and type of the y-axis to:

- Clip the y-axis to specific ranges.
- Automatically change y-axis bounds based on an absolute value threshold. This threshold can be applied to one or both ends of the graph (lower and upper) to remove the "outlier" series.
- Change the y-axis scale from linear to log, pow, or sqrt.

The following configuration options are available:

| Option                | Required | Description                                                                                                                                                                                                   |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Min`                 | No       | Specify the minimum value to show on the y-axis. It takes a number or `Auto` as the default value.                                                                                                            |
| `Max`                 | No       | Specify the maximum value to show on the y-axis. It takes a number or `Auto` as the default value.                                                                                                            |
| `Scale`               | No       | Specifies the scale type. Possible values include:- *linear*: A linear scale (default).- *log*: A logarithmic scale.- *pow*: A Power of 2 scale (2 is default, modify in JSON).- *sqrt*: A square root scale. |
| `Always include zero` | No       | Always include zero or fit the y-axis to the data range. The default is to always include zero.                                                                                                               |

Because the mathematical log function does not accept negative values, the Datadog log scale only works if values are of the same sign (everything > 0 or everything < 0). Otherwise, an empty graph is returned.

### Legend configuration{% #legend-configuration %}

You can add configurable legends to your screenboards by selecting from the following options in the **Legend** section:

- Automatic (default)
- Compact
- Expanded: Configurable columns for value, avg, sum, min, and max
- None

For timeboards, legends display automatically when a dashboard is set to L or XL.

### Context links{% #context-links %}

To add a context link in the dropdown menu that appears when you click in a dashboard widget, click **Add a Context Link** in the **Context Links** section.

For more information about editing and deleting context links, see [Context Links](https://docs.datadoghq.com/dashboards/guide/context-links/).

### Full screen{% #full-screen %}

In addition to the [standard full screen options](https://docs.datadoghq.com/dashboards/widgets/#full-screen), you can apply quick functions, adjust the Y scale, save changes, or save as a new graph.

For more information, see [Explore your data in full-screen graph mode](https://www.datadoghq.com/blog/full-screen-graphs).

### Metrics info{% #metrics-info %}

On a metric graph, click on the context menu (three vertical dots) to find the **Metrics Info** option. This opens a panel with a description of the metric. Clicking on the metric name in this panel opens the metric in the metric summary page for further analysis or edits.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription custom_links[object]List of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`. events[object]List of widget events.q [*required*]stringQuery definition.tags_executionstringThe execution method for multi-value filters.legend_columns[string]Columns displayed in the legend.legend_layoutenumLayout of the legend. Allowed enum values: `auto,horizontal,vertical`legend_sizestringAvailable legend sizes for a widget. Should be one of "0", "2", "4", "8", "16", or "auto". markers[object]List of markers.display_typestringCombination of:
- A severity error, warning, ok, or info
- A line type: dashed, solid, or bold In this case of a Distribution widget, this can be set to be `percentile`.
labelstringLabel to display over the marker.timestringTimestamp for the widget.value [*required*]stringValue to apply. Can be a single value y = 15 or a range of values 0 < y < 10. For Distribution widgets with `display_type` set to `percentile`, this should be a numeric percentile value (for example, "90" for P90). requests [*required*][object]List of timeseries widget requests. apm_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. audit_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.display_typeenumType of display to use for the request. Allowed enum values: `area,bars,line,overlay` event_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. formulas[object]List of formulas that operate on queries.aliasstringExpression alias.cell_display_modeenumDefine a display mode for the table cell. Allowed enum values: `number,bar,trend` cell_display_mode_optionsobjectCell display mode options for the widget formula. (only if `cell_display_mode` is set to `trend`).trend_typeenumTrend type for the cell display mode options. Allowed enum values: `area,line,bars`y_scaleenumY scale for the cell display mode options. Allowed enum values: `shared,independent` conditional_formats[object]List of conditional formats.comparator [*required*]enumComparator to apply. Allowed enum values: `=,>,>=,<,<=`custom_bg_colorstringColor palette to apply to the background, same values available as palette.custom_fg_colorstringColor palette to apply to the foreground, same values available as palette.hide_valuebooleanTrue hides values.image_urlstringDisplays an image as the background.metricstringMetric from the request to correlate this conditional format with.palette [*required*]enumColor palette to apply. Allowed enum values: `blue,custom_bg,custom_image,custom_text,gray_on_white,grey,green,orange,red,red_on_white,white_on_gray,white_on_green,green_on_white,white_on_red,white_on_yellow,yellow_on_white,black_on_light_yellow,black_on_light_green,black_on_light_red`timeframestringDefines the displayed timeframe.value [*required*]doubleValue for the comparator.formula [*required*]stringString expression built from queries, formulas, and functions. limitobjectOptions for limiting results returned.countint64Number of results to return.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
 number_formatobjectNumber format options for the widget. unit <oneOf>Number format unit. Option 1objectCanonical unit.per_unit_namestringThe name of the unit per item.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. Option 2objectCustom unit.labelstringThe label for the custom unit.typeenumThe type of custom unit. Allowed enum values: `custom_unit_label` unit_scaleobjectThe definition of `NumberFormatUnitScale` object.typeenumThe type of unit scale. Allowed enum values: `canonical_unit`unit_namestringThe name of the unit. styleobjectStyling options for widget formulas.palettestringThe color palette used to display the formula. A guide to the available color palettes can be found at [https://docs.datadoghq.com/dashboards/guide/widget_colors](https://docs.datadoghq.com/dashboards/guide/widget_colors)palette_indexint64Index specifying which color to use within the palette. log_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. metadata[object]Used to define expression aliases.alias_namestringExpression alias.expression [*required*]stringExpression name. network_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.on_right_yaxisbooleanWhether or not to display a second y-axis on the right. process_queryobjectThe process query to use in the widget.filter_by[string]List of processes.limitint64Max number of items in the filter list.metric [*required*]stringYour chosen metric.search_bystringYour chosen search term. profile_metrics_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply.qstringWidget query. queries[ <oneOf>]List of queries that can be returned directly or used in formulas. Option 1objectA formula and functions metrics query.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for metrics queries. Allowed enum values: `metrics`name [*required*]stringName of the query for use in formulas.query [*required*]stringMetrics query definition.semantic_modeenumSemantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native` Option 2objectA formula and functions events query. compute [*required*]objectCompute options.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`intervalint64A time interval in milliseconds.metricstringMeasurable attribute to compute.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for event platform-based queries. Allowed enum values: `logs,spans,network,rum,security_signals,profiles,audit,events,ci_tests,ci_pipelines,incident_analytics,product_analytics,on_call_events` group_by[object]Group by options.facet [*required*]stringEvent facet.limitint64Number of groups to return. sortobjectOptions for sorting group by results.aggregation [*required*]enumAggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`metricstringMetric used for sorting group by results.orderenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes[string]An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.name [*required*]stringName of the query for use in formulas. searchobjectSearch options.query [*required*]stringEvents search string.storagestringOption for storage location. Feature in Private Beta. Option 3objectProcess query using formulas and functions.aggregatorenumThe aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData sources that rely on the process backend. Allowed enum values: `process,container`is_normalized_cpubooleanWhether to normalize the CPU percentages.limitint64Number of hits to return.metric [*required*]stringProcess metric name.name [*required*]stringName of query for use in formulas.sortenumDirection of sort. Allowed enum values: `asc,desc`
default: `desc`
tag_filters[string]An array of tags to filter by.text_filterstringText to use as filter. Option 4objectA formula and functions APM dependency stats query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM dependency stats queries. Allowed enum values: `apm_dependency_stats`env [*required*]stringAPM environment.is_upstreambooleanDetermines whether stats for upstream or downstream dependencies should be queried.name [*required*]stringName of query to use in formulas.operation_name [*required*]stringName of operation on service.primary_tag_namestringThe name of the second primary tag used within APM; required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog).primary_tag_valuestringFilter APM data by the second primary tag. `primary_tag_name` must also be specified.resource_name [*required*]stringAPM resource.service [*required*]stringAPM service.stat [*required*]enumAPM statistic. Allowed enum values: `avg_duration,avg_root_duration,avg_spans_per_trace,error_rate,pct_exec_time,pct_of_traces,total_traces_count` Option 5objectAPM resource stats query using formulas and functions.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for APM resource stats queries. Allowed enum values: `apm_resource_stats`env [*required*]stringAPM environment.group_by[string]Array of fields to group results by.name [*required*]stringName of this query to use in formulas.operation_namestringName of operation on service.primary_tag_namestringName of the second primary tag used within APM. Required when `primary_tag_value` is specified. See [https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog)primary_tag_valuestringValue of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.resource_namestringAPM resource name.service [*required*]stringAPM service name.stat [*required*]enumAPM resource stat name. Allowed enum values: `errors,error_rate,hits,latency_avg,latency_distribution,latency_max,latency_p50,latency_p75,latency_p90,latency_p95,latency_p99` Option 6objectA formula and functions metrics query.additional_query_filtersstringAdditional filters applied to the SLO query.cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for SLO measures queries. Allowed enum values: `slo`group_modeenumGroup mode to query measures. Allowed enum values: `overall,components`measure [*required*]enumSLO measures queries. Allowed enum values: `good_events,bad_events,good_minutes,bad_minutes,slo_status,error_budget_remaining,burn_rate,error_budget_burndown`namestringName of the query for use in formulas.slo_id [*required*]stringID of an SLO to query measures.slo_query_typeenumName of the query for use in formulas. Allowed enum values: `metric,monitor,time_slice` Option 7objectA formula and functions Cloud Cost query.aggregatorenumAggregator used for the request. Allowed enum values: `avg,last,max,min,sum,percentile`cross_org_uuids[string]The source organization UUID for cross organization queries. Feature in Private Beta.data_source [*required*]enumData source for Cloud Cost queries. Allowed enum values: `cloud_cost`name [*required*]stringName of the query for use in formulas.query [*required*]stringQuery for Cloud Cost data.response_formatenumTimeseries, scalar, or event list response. Event list response formats are supported by Geomap widgets. Allowed enum values: `timeseries,scalar,event_list` rum_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. security_queryobjectThe log query. computeobjectDefine computation for a log query.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. group_by[object]List of tag prefixes to group by in the case of a cluster check.facet [*required*]stringFacet name.limitint64Maximum number of items in the group. sortobjectDefine a sorting method.aggregation [*required*]stringThe aggregation method.facetstringFacet name.order [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`indexstringA coma separated-list of index names. Use "*" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes) multi_compute[object]This field is mutually exclusive with `compute`.aggregation [*required*]stringThe aggregation method.facetstringFacet name.intervalint64Define a time interval in seconds. searchobjectThe query being made on the logs.query [*required*]stringSearch value to apply. styleobjectDefine request widget style.line_typeenumType of lines displayed. Allowed enum values: `dashed,dotted,solid`line_widthenumWidth of line displayed. Allowed enum values: `normal,thick,thin`order_byenumHow to order series in timeseries visualizations.
- `tags`: Order series alphabetically by tag name (default behavior)
- `values`: Order series by their current metric values (typically descending) Allowed enum values: `tags,values`
palettestringColor palette to apply to the widget. right_yaxisobjectAxis controls for the widget.include_zerobooleanSet to `true` to include zero.labelstringThe label of the axis to display on the graph. Only usable on Scatterplot Widgets.maxstringSpecifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
minstringSpecifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scalestringSpecifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
show_legendboolean(screenboard only) Show the legend for this widget. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringTitle of your widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the timeseries widget. Allowed enum values: `timeseries`
default: `timeseries`
 yaxisobjectAxis controls for the widget.include_zerobooleanSet to `true` to include zero.labelstringThe label of the axis to display on the graph. Only usable on Scatterplot Widgets.maxstringSpecifies maximum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
minstringSpecifies minimum numeric value to show on the axis. Defaults to `auto`.
default: `auto`
scalestringSpecifies the scale type. Possible values are `linear`, `log`, `sqrt`, and `pow##` (for example `pow2` or `pow0.5`).
default: `linear`
{% /tab %}

{% tab title="example" %}

```json
{
  "custom_links": [
    {
      "is_hidden": false,
      "label": "Search logs for {{host}}",
      "link": "https://app.datadoghq.com/logs?query={{host}}",
      "override_label": "logs"
    }
  ],
  "events": [
    {
      "q": "",
      "tags_execution": "string"
    }
  ],
  "legend_columns": [],
  "legend_layout": "string",
  "legend_size": "string",
  "markers": [
    {
      "display_type": "error dashed",
      "label": "Error threshold",
      "time": "string",
      "value": "y = 15"
    }
  ],
  "requests": [
    {
      "apm_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "audit_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "display_type": "string",
      "event_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "formulas": [
        {
          "alias": "string",
          "cell_display_mode": "number",
          "cell_display_mode_options": {
            "trend_type": "area",
            "y_scale": "shared"
          },
          "conditional_formats": [
            {
              "comparator": ">",
              "custom_bg_color": "string",
              "custom_fg_color": "string",
              "hide_value": false,
              "image_url": "string",
              "metric": "string",
              "palette": "blue",
              "timeframe": "string",
              "value": 0
            }
          ],
          "formula": "func(a) + b",
          "limit": {
            "count": "integer",
            "order": "string"
          },
          "number_format": {
            "unit": {
              "per_unit_name": "bytes",
              "type": "canonical_unit",
              "unit_name": "bytes"
            },
            "unit_scale": {
              "type": "canonical_unit",
              "unit_name": "bytes"
            }
          },
          "style": {
            "palette": "classic",
            "palette_index": 1
          }
        }
      ],
      "log_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "metadata": [
        {
          "alias_name": "string",
          "expression": ""
        }
      ],
      "network_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "on_right_yaxis": false,
      "process_query": {
        "filter_by": [],
        "limit": "integer",
        "metric": "system.load.1",
        "search_by": "string"
      },
      "profile_metrics_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "q": "string",
      "queries": [],
      "response_format": "timeseries",
      "rum_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "security_query": {
        "compute": {
          "aggregation": "avg",
          "facet": "@duration",
          "interval": 5000
        },
        "group_by": [
          {
            "facet": "resource_name",
            "limit": 50,
            "sort": {
              "aggregation": "avg",
              "facet": "@string_query.interval",
              "order": "desc"
            }
          }
        ],
        "index": "days-3,days-7",
        "multi_compute": [
          {
            "aggregation": "avg",
            "facet": "@duration",
            "interval": 5000
          }
        ],
        "search": {
          "query": ""
        }
      },
      "style": {
        "line_type": "string",
        "line_width": "string",
        "order_by": "string",
        "palette": "string"
      }
    }
  ],
  "right_yaxis": {
    "include_zero": false,
    "label": "string",
    "max": "string",
    "min": "string",
    "scale": "string"
  },
  "show_legend": false,
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "timeseries",
  "yaxis": {
    "include_zero": false,
    "label": "string",
    "max": "string",
    "min": "string",
    "scale": "string"
  }
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Explore your data in full-screen graph mode](https://www.datadoghq.com/blog/full-screen-graphs)
- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Graph historical SLO data on Dashboards](https://docs.datadoghq.com/dashboards/guide/slo_data_source)
